# BÁO CÁO PHÂN TÍCH JUPYTER NOTEBOOKS - DỰ ÁN FINE-TUNE PIPER TTS GIỌNG NAM VIỆT (.agent/NOTEBOOK_AUDIT_REPORT.md)

Tài liệu này ghi lại kết quả phân tích kỹ thuật chi tiết từ việc quét các file Jupyter Notebooks (`.ipynb`) cốt lõi trong thư mục `piper_vi_vais1000_finetuning/notebooks/` bằng công cụ MCP `jupyter-notebook` chuyên dụng. Nội dung này sẽ đóng vai trò là "khung sườn kỹ thuật thực nghiệm" để ánh xạ trực tiếp vào **Chương 3 (Phương pháp đề xuất)** và **Chương 4 (Thực nghiệm & Kết quả)** của báo cáo Đồ án tốt nghiệp VKU.

---

## 1. PHÂN TÍCH PHASES THỰC NGHIỆM TỪ CODEBASE NOTEBOOKS

### Phase 3 — Chuẩn hóa văn bản & Bộ lọc Speaker Hybrid
*   **Notebook:** `notebooks/phase3_text/01_normalize_metadata.ipynb`
*   **Quy trình kỹ thuật thực tế:**
    1.  **Bộ lọc Per-speaker Hybrid:** Áp dụng bộ lọc tùy biến trên tập dữ liệu raw `metadata.qc.csv` (1999 clips) để loại bỏ mismatch từ kết quả STT QC:
        *   `jellyfish1010_0004`: Lọc nghiêm ngặt (chỉ giữ class `keep`) $\rightarrow$ 409 clips (do drop rate gốc của speaker này rất cao: 47.5%).
        *   `jellyfish1010_0013`: Lọc tiêu chuẩn (giữ class `keep` + `warn`) $\rightarrow$ 509 clips (drop rate 7.1%).
        *   `jellyfish1010_0032`: Lọc tiêu chuẩn (giữ class `keep` + `warn`) $\rightarrow$ 582 clips (drop rate cực thấp: 0.2%).
        *   **Tổng số lượng dataset thu về:** 1500 clips sạch ($\approx$ 2.5 giờ âm thanh, đạt sweet spot huấn luyện few-speaker).
    2.  **Chuẩn hóa văn bản:** Sử dụng thư viện `vinorm.TTSnorm()` trên CPU Colab để chuyển đổi số, ngày, giờ, ký hiệu viết tắt sang dạng chữ tiếng Việt chuẩn (phục vụ espeak-ng biểu diễn âm vị).
    3.  **Vá lỗi hệ thống (Python 3.12 Compatibility):** Kịch bản chèn module giả lập `imp` (`fake_imp = types.ModuleType('imp')` với hàm `fake_find_module`) để vượt qua lỗi gỡ bỏ thư viện `imp` trên Python 3.12+ giúp `vinorm` không bị crash.
    4.  **Sản phẩm đầu ra:** File `metadata.filtered.csv` định dạng LJSpeech (`id|text_norm`) không chứa tiêu đề (no header).

### Phase 4 — Tiền xử lý Dữ liệu & Giải pháp Phù hợp Không gian Âm vị
*   **Notebook:** `notebooks/phase4_preprocess/01_piper_preprocess.ipynb`
*   **Quy trình kỹ thuật thực tế:**
    1.  **Tải Base Checkpoint:** Đồng bộ tự động checkpoint `vais1000-medium` (epoch=4769, kích thước 845.9 MB) và file cấu hình `config.json` từ HuggingFace dataset `rhasspy/piper-checkpoints`.
    2.  **Trích xuất đặc trưng âm thanh và âm vị:** Chạy module `piper_train.preprocess` bất đồng bộ trên CPU (`--max-workers 2` để tránh lỗi tính toán phân phối luồng nhỏ hơn số CPU) với tần số lấy mẫu `22050 Hz`, cấu hình `--single-speaker` để tương thích với kiến trúc model base.
    3.  **Vá lỗi Mismatch Âm vị (2-Pass Workaround):** 
        *   *Vấn đề:* Bản cài đặt `piper-train` không hỗ trợ flag `--phoneme-id-map` trực tiếp nên khi chạy preprocess tự động sẽ sinh ra bản đồ âm vị mới chứa 157 âm vị (lọc thêm các ký tự lạ từ tiếng Anh pha trộn như `'X'`, `'g'`, `'ʦ'`). Điều này sẽ làm lệch không gian nhúng của model base (154 âm vị), gây lỗi Index/Garbage output khi train.
        *   *Giải pháp:* Chạy preprocess tự động để discover đặc trưng âm thanh $\rightarrow$ Ghi đè file `config.json` tự sinh bằng file `config.json` chuẩn của `vais1000` $\rightarrow$ Chạy kịch bản kiểm chứng tự động 4 bước nghiêm ngặt:
            *   *Check 1:* Tìm ID âm vị lớn nhất trong `dataset.jsonl` (Kết quả thực tế đạt `max_id = 142` nằm trong ngưỡng an toàn $\le 153$ của vais1000).
            *   *Check 2:* So sánh tập hợp khóa của bản đồ âm vị hiện tại với bản base (Kết quả: Khớp hoàn toàn keys, các ký tự lạ được bỏ qua an toàn).
            *   *Check 3:* Xác nhận model embedding size an toàn không lỗi IndexError lookup.
            *   *Check 4:* Đối soát cấu trúc xen kẽ BOS/Pad của Piper (`pids[0]=BOS=1`, `pids[1]=pad=0`, `pids[2]=phoneme_0`) khớp tuyệt đối.
    4.  **Sản phẩm đầu ra:** Thư mục `training_dir` hoàn chỉnh chứa 3000 file đặc trưng phổ âm `.pt` (nằm tại sub-folder `cache/22050/`) và file mapping `dataset.jsonl` (1500 dòng).

### Phase 5 — Huấn luyện & Giám sát Chuyển đổi Giọng nói (Fine-tuning)
*   **Notebook:** `notebooks/phase5_train/01_train_medium.ipynb`
*   **Quy trình kỹ thuật thực tế:**
    1.  **Cơ chế Tự động khôi phục (Auto-resume):** Quét thư mục `lightning_logs` tìm checkpoint `.ckpt` mới nhất ở phiên chạy trước. Nếu là phiên đầu tiên, tự động fallback về checkpoint vais1000 gốc (`epoch=4769-step=919580.ckpt`). Cơ chế này cực kỳ quan trọng giúp khắc phục giới hạn 12 tiếng của Google Colab GPU T4.
    2.  **Cập nhật Tốc độ học (Learning Rate Patch):** Do CLI của `piper_train` không hỗ trợ thay đổi LR trực tiếp, notebook sử dụng regex thay thế dòng code (`re.subn`) ngay trong file `lightning.py` của thư viện cài đặt để ép tốc độ học từ $2\times10^{-4}$ (mặc định cho train từ đầu) xuống còn **$1\times10^{-4}$** (tối ưu cho fine-tuning để bảo toàn thanh điệu).
    3.  **Giám sát Live & Số liệu thực nghiệm:**
        *   Tích hợp TensorBoard inline để giám sát `train/loss_mel`, `val/loss_mel`, và các discriminator loss.
        *   Chạy tiến trình nền ghi nhận thông số tài nguyên phần cứng `nvidia-smi` mỗi 30 giây lưu vào `gpu_log.csv` (lấy cột Memory và GPU Utilization).
        *   Tích hợp kịch bản suy luận thủ công (manual audit) trên 25 câu test chuẩn khoa học tại `evaluation/test_sentences.txt` sau mỗi 200 epochs để tác giả trực tiếp nghe và đánh giá chất lượng giọng nam.
    4.  **Hậu xử lý & Dọn dẹp:** Kịch bản dọn dẹp các checkpoint trung gian (mỗi checkpoint nặng ~846MB dễ gây đầy Google Drive), chỉ giữ lại `last.ckpt` và các checkpoint chia hết cho 200 epochs để tối ưu hóa không gian lưu trữ.

---

## 2. Ý NGHĨA ÁNH XẠ VÀO NỘI DUNG BÁO CÁO ĐỒ ÁN VKU

Từ kết quả phân tích mã nguồn thực tế ở trên, khung nội dung học thuật cho báo cáo ĐATN sẽ được làm dày bằng các chi tiết kỹ thuật có độ tin cậy cao:

### CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT
*   **Mô tả Quy trình Huấn luyện Chuyển đổi Giọng nói (Cross-Gender Fine-tuning):** Giải thích cách kế thừa trọng số tầng nhúng phoneme (Text Encoder) của giọng nữ tiếng Việt chuẩn `vais1000-medium` để tập trung huấn luyện Generator (Decoder HiFi-GAN) và Discriminator học đặc trưng sinh học giọng nam Việt (f0, pitch, formants) từ dataset 2.5 giờ.
*   **Giải thuật 2-Pass Phoneme Mapping Workaround:** Mô hình hóa quy trình giải quyết xung đột âm vị ngoại lai tiếng Anh pha trộn thành một sơ đồ giải thuật (Algorithm Flowchart) cụ thể.
*   **Giải pháp vá lỗi Learning Rate & Python 3.12 inline:** Đưa vào mục cải tiến kỹ thuật hệ thống, chứng minh tính chủ động giải quyết xung đột thư viện (Dependency Hell).

### CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ
*   **Quy trình Kiểm soát Chất lượng Dữ liệu (Audio QC):** Trình bày số liệu thực tế về Word Error Rate (WER) bimodal distribution khi dùng PhoWhisper-large nhận dạng ngược toàn bộ 1999 clips để đưa ra quyết định thiết kế bộ lọc Speaker Hybrid (drop 22.6% clips rác).
*   **Môi trường Huấn luyện Bất đồng bộ:** Trình bày cấu trúc venv snapshotting giúp phục hồi môi trường Colab T4 trong 30 giây và biểu đồ giám sát tài nguyên GPU tiêu thụ từ file `gpu_log.csv`.
*   **Đường cong hội tụ & Chất lượng âm phổ:** Đưa ra biểu đồ so sánh Mel Reconstruction Loss (biểu thị độ tự nhiên, rõ chữ) và spectrogram trực quan giữa model vais1000 gốc, model fine-tuned FP32 và model lượng tử hóa FP16.
