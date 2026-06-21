# KẾ HOẠCH MERGE: DATN_BT.docx × BAOCAO_OUTLINE.md → file .md ground-truth

> Trạng thái: **BẢN NHÁP CHỜ DUYỆT** — chưa thực thi bất kỳ thao tác nào.
> Mục tiêu: tạo một file `.md` ground-truth theo **outline 5 chương mới**, giữ trọn nội dung S2ST đã viết trong `DATN_BT.docx`, loại bỏ rác từ template khóa trước.

---

## A. CẤU TRÚC THỰC TẾ CỦA DATN_BT.docx (sau khi đọc 848 đoạn / 13 bảng / 35 ảnh)

File đang theo **khung CŨ 4 chương kiểu đồ án phần mềm**, lệch hẳn outline mới (5 chương kiểu NCKH):

| Khối trong docx | Tình trạng nội dung |
|---|---|
| Lời cảm ơn | ✅ Đã viết |
| Mục lục | (auto, rỗng) |
| Danh mục chữ viết tắt (bảng 19×4) | ✅ Có |
| **Danh mục bảng** | ❌ **RÁC** — của project khóa trước (Đăng nhập, Quản lý bài viết, Quản lý Tags...) |
| **Danh mục hình** | ❌ **RÁC** — XLM-RoBERTa, BERT, Dataset Toxic, RAG "VKU AI"... |
| Lời mở đầu | ✅ Đã viết (lý do, mục tiêu, đối tượng/phạm vi, cách tiếp cận, phương pháp) |
| CHƯƠNG 1: Cơ sở lý thuyết và công nghệ | ✅ Đã viết (STT/Whisper/PhoWhisper, NMT/NLLB-200, TTS/VITS/Piper, công nghệ & thư viện) |
| CHƯƠNG 2: Phân tích thiết kế hệ thống | ✅ Đã viết (yêu cầu, tác nhân, usecase, sơ đồ hoạt động, sơ đồ tuần tự) — *kiểu phần mềm* |
| CHƯƠNG 3: Triển khai hệ thống | ✅ Viết nhiều nhất (VAD, STT context, Short-MT, Watchdog, dataset, fine-tuning, âm vị, đánh giá, **kết quả train**) |
| CHƯƠNG 4: Mô phỏng hệ thống | ❌ **Gần như rỗng** (chỉ có heading "Giao diện trang chủ") |
| Kết luận và hướng phát triển | ✅ Đã viết (ngắn) |
| **Danh mục tài liệu tham khảo** | ❌ **RÁC** — placeholder nông nghiệp/kinh tế ("lúa lai", "pearl millet", Anderson 1985...) |
| Cuối file | ⚠️ 2 khối code **PlantUML thô** (@startuml) định nghĩa sơ đồ kiến trúc 2 chế độ — note làm việc sót lại |

**Lỗi định dạng:** đánh số heading loạn (Chương 1 có "1.4.1", "1.3.3" lẫn lộn; Chương 2,3 heading không số); số hình loạn ("Hình 0.1", "Hình 2", "Hình 18"→"Hình 27").

---

## B. NỘI DUNG RÁC / LỆCH ĐỀ TÀI — XỬ LÝ DỨT ĐIỂM

1. **Danh mục bảng + Danh mục hình hiện tại** → XÓA toàn bộ. Sẽ tái sinh tự động từ caption thật ở bước xuất docx (SEQ field + Table of Figures).
2. **Danh mục tài liệu tham khảo (placeholder nông nghiệp)** → XÓA. Thay bằng tài liệu thật (cần thu thập sau: Whisper, PhoWhisper, NLLB-200, VITS, Piper, Silero VAD, CTranslate2, NISQA...).
3. **2 khối PlantUML cuối file** → GIỮ làm tư liệu, chuyển thành sơ đồ kiến trúc (render ảnh / placeholder) đặt đúng mục 3.1, không để code thô lẫn trong thân báo cáo.

---

## C. BẢNG ÁNH XẠ docx → OUTLINE 5 CHƯƠNG MỚI

| Nội dung docx (cũ) | → Mục outline mới | Ghi chú |
|---|---|---|
| Lời mở đầu: lý do | → **1.1** Lý do chọn đề tài | Tách ý vào 1.1.1–1.1.3 |
| Lời mở đầu: (rải rác) | → **1.2** Phát biểu bài toán | Bổ sung 1.2.4 (chống feedback loop) đã có ý |
| Lời mở đầu: mục tiêu | → **1.3** Mục tiêu & đóng góp | |
| Lời mở đầu: đối tượng/phạm vi | → **1.4** Đối tượng & phạm vi | |
| (chưa có) | → **1.5** Bố cục báo cáo | ❌ Viết mới |
| Ch1: STT/Whisper/PhoWhisper | → **2.1** | Map tốt |
| Ch1: NMT/NLLB-200 | → **2.2** | Map tốt |
| Ch1: TTS/VITS/Piper | → **2.3** | Map tốt (espeak-ng → 2.3.5) |
| Ch1: Silero VAD (rải trong thư viện) | → **2.4** | Gom lại thành mục riêng |
| Ch1: Công nghệ & thư viện (Python, FastAPI, WebSocket, PySide6, PyAudio, SoundCard, VB-Cable, CTranslate2) | → **❓ cần quyết định** | Outline mới không có mục "công cụ" riêng → xem Quyết định #2 |
| (chưa có) | → **2.5** Related work & khoảng trống NC | ❌ Viết mới |
| Ch2: yêu cầu chức năng/phi chức năng | → **3.1** (mở đầu) | Giữ phần khung |
| Ch2: tác nhân + usecase + sơ đồ hoạt động + sơ đồ tuần tự (12+ hình, 6 bảng) | → **❓ cần quyết định** | Outline NCKH không có mục usecase → xem Quyết định #1 |
| Ch2: sơ đồ kiến trúc tổng quát + WebSocket | → **3.1.1–3.1.3** | + ghép 2 sơ đồ PlantUML |
| Ch3: chế độ 2 chiều / 1 chiều + loopback | → **3.2** Client & cô lập loopback | |
| (chưa có) Facade, Execution Lane, Preload/Warmup | → **3.3** | ❌ Viết mới (đọc code) |
| Ch3: Silero VAD, STT context, Short-MT, Watchdog | → **3.4** Pipeline streaming | Map tốt |
| (chưa có) SBD/Comma fallback, telemetry | → **3.4.3–3.4.4** | ❌ Viết mới (đọc code) |
| Ch3: Cross-Gender Fine-tuning + 2-Pass phoneme | → **3.5** Thiết kế fine-tuning | Map tốt |
| (chưa có) môi trường + venv snapshotting | → **4.1** | ❌ Viết mới (có rải rác) |
| Ch3: dataset VieNeu + QC + Per-Speaker Filter + vinorm | → **4.2** Xử lý dữ liệu & QC | Map tốt |
| Ch3: chỉ số đánh giá (RTF/WER/Mel, bảng 10–12) | → **4.3** | Map tốt |
| Ch4 (rỗng): client app test | → **4.4** | ❌ Viết mới — gắn nhãn `[⚠️ Bug đang fix]` |
| Ch3: Mel/KL loss, FP16 quant, NISQA/Human MOS, WER (hình 21–25, bảng 13) | → **4.5** Kết quả train Piper | Map tốt — gắn nhãn `[🔄 Đang train]` nếu còn cập nhật |
| (chưa có) so sánh latency E2E | → **4.6** | Một phần có ở bảng đo, cần bổ sung |
| Kết luận & hướng phát triển | → **Chương 5** | Mở rộng theo 5.1/5.2/5.3 |
| Tài liệu tham khảo (rác) | → mục TLTK | ❌ Thay mới |

**Lưu ý mapping quan trọng:** docx gộp *thiết kế + dữ liệu + kết quả* chung trong "Chương 3 Triển khai". Outline mới TÁCH **phương pháp (Ch3)** khỏi **thực nghiệm/kết quả (Ch4)**. Khi merge phải xẻ đôi: phần *thiết kế/giải pháp* → Ch3, phần *số liệu/kết quả/dataset* → Ch4.

---

## D. DANH SÁCH THAO TÁC (để duyệt)

**XÓA**
- D1. Danh mục bảng cũ (rác forum project).
- D2. Danh mục hình cũ (rác forum project).
- D3. Danh mục tài liệu tham khảo placeholder (nông nghiệp/kinh tế).

**DI CHUYỂN / TÁI CẤU TRÚC**
- M1. Lời mở đầu → xẻ thành Chương 1 (1.1–1.4).
- M2. docx Ch1 → Chương 2 (2.1–2.4).
- M3. docx Ch3 (thiết kế VAD/STT/MT/fine-tuning) → Chương 3; (dataset/kết quả) → Chương 4.
- M4. 2 sơ đồ PlantUML cuối file → mục 3.1 (dạng ảnh/placeholder).
- M5. Kết luận → Chương 5 (giãn theo 5.1–5.3).

**SỬA / CHUẨN HÓA**
- E1. Bỏ hardcode số hình/bảng; dùng placeholder caption (số do SEQ field tự đánh ở docx).
- E2. Chuẩn hóa cấp heading khớp outline tới cấp 3.
- E3. Gắn nhãn trạng thái mỗi mục: ✅ đã viết / ⚠️ cần sửa-đối chiếu code / ❌ chưa có.

**VIẾT MỚI (sau, khi đọc code — read-only)**
- N1. 1.5 Bố cục báo cáo. N2. 2.5 Related work & gaps. N3. 3.3 Facade/Execution Lane/Preload. N4. 3.4.3–3.4.4 SBD/telemetry. N5. 4.1 môi trường. N6. 4.4 kết quả client app. N7. 4.6 latency E2E. N8. Tài liệu tham khảo thật.

---

## E. QUYẾT ĐỊNH ĐÃ CHỐT ✅

1. **Khối usecase/tác nhân/sơ đồ tuần tự (docx Ch2)** → **Rút gọn vào Ch3.1**: giữ phần kiến trúc/luồng cốt lõi, lược bỏ usecase chi tiết và sơ đồ tuần tự kiểu phần mềm.
2. **Mục "Công nghệ & thư viện"** → **giữ thành mục con ngắn trong Chương 2**.
3. **Đánh số hình–bảng** → **theo chương** (Hình 2.1, Bảng 3.1...). Ở docx sẽ dùng SEQ field cấu hình đánh số theo chương.
4. **File ground-truth** → **một file `BAOCAO_NOIDUNG.md`** duy nhất.
