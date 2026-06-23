# ĐỀ XUẤT OUTLINE CHI TIẾT — CHƯƠNG 3 & 4 (bản 2, chờ duyệt)

> Cập nhật theo góp ý user: (1) trọng tâm **finetune mô hình ~65%**, hệ thống ứng dụng ~35% (do Khoa buộc chọn định hướng NCKH); (2) **gộp/thu nhỏ** phần hệ thống, **bung** phần finetune; (3) **cả Ch3 và Ch4 đều trình bày FINETUNE TRƯỚC, HỆ THỐNG SAU** (nhất quán + đúng trọng tâm).
> Gỡ rối "2 lần xử lý dữ liệu": tách **Giai đoạn 1 (VieNeu)** → Model 1; **Giai đoạn 2 (tự thu thập YouTube)** → Model 2 & 3. Thiết kế quy trình ở Ch3, số liệu ở Ch4.
> FP16: bản deploy dùng **FP32** (FP16 chỉ là dự kiến); giữ cả số liệu đánh giá **GPU + CPU**.

---

## CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT

> Phần A — Phương pháp xây dựng mô hình TTS giọng nam (3.1–3.5, ~65%). Phần B — Hệ thống S2ST tích hợp (3.6–3.7, ~35%).

### 3.1. Tổng quan phương pháp & bài toán nghiên cứu
- Bối cảnh: hệ thống S2S cần giọng nam tiếng Việt nhẹ, tự nhiên — nguồn công khai khan hiếm.
- Hướng tiếp cận: cross-gender fine-tuning + tự xây dựng dữ liệu; sơ đồ tổng quát quy trình 2 giai đoạn → 3 mô hình.

### 3.2. Chiến lược Cross-Gender Fine-tuning trên kiến trúc VITS
- 3.2.1. Nguyên lý kế thừa nền `vais1000-medium` (giọng nữ) → giọng nam; dịch chuyển F0/formant.
- 3.2.2. Cơ chế huấn luyện đối kháng VITS & các hàm mất mát liên quan khi fine-tune.

### 3.3. Giai đoạn 1 — Xây dựng dữ liệu từ nguồn công khai VieNeu
- 3.3.1. Khảo sát & chọn nguồn (FPT-FOSD fail → VieNeu-140h); ghép 3 speaker nam.
- 3.3.2. Kiểm soát chất lượng QC bằng PhoWhisper-large + lọc Per-Speaker Hybrid → 1500 clip ~2.5h.
- 3.3.3. Hạn chế của Giai đoạn 1 (dữ liệu ít, WER cao) → động lực sang Giai đoạn 2.

### 3.4. Giai đoạn 2 — Tự thu thập & xử lý dữ liệu từ YouTube
- 3.4.1. Thu thập & tiền xử lý: yt-dlp → transcribe (faster-whisper large-v3) → segment ~6s → khử nhiễu Demucs → chuẩn hóa (22050Hz/-23LUFS, pad lead).
- 3.4.2. Kiểm định nhãn đa nguồn: crosscheck 3 ASR (faster-whisper large-v3 + Qwen3-ASR-1.7B + Deepgram Nova-3) + LLM Gemini hiệu đính batch → 2061 clip ~4.22h.
- 3.4.3. Chuẩn hóa văn bản: vinorm (Run A) vs vietnormalizer + protect-list (Run B1).

### 3.5. Hai chiến lược huấn luyện & tối ưu mô hình
- 3.5.1. Run A — Full fine-tune (train toàn bộ tensor).
- 3.5.2. Run B1 — Partial-freeze (freeze enc_p + dp) giữ phát âm/thanh điệu, chỉ học màu giọng nam.
- 3.5.3. Đồng bộ âm vị 2-pass & tương thích phoneme set (espeak-ng / phoneme_id_map) ⚠️ *(xác minh notebook khi fill)*.
- 3.5.4. Các fix huấn luyện: max-phoneme-ids động, force-LR khi resume, checkpoint mỗi epoch (`train_selfcollect.py`).

### 3.6. Thiết kế hệ thống S2ST realtime (Client–Server) — *gọn*
- 3.6.1. Kiến trúc Client–Server song công qua WebSocket; hai chế độ (hội thoại 2 chiều / 1 chiều). *(gộp khung truyền + mode-dispatch ở mức tổng quan)*
- 3.6.2. Client: thu âm 2 tuyến (mic Route 0 / WASAPI loopback Route 1) + định tuyến **VoiceMeeter Banana** (đa bus, chống vòng lặp tự dịch).
- 3.6.3. Server phân tầng hướng engine: Facade 3 engine, Execution Lane, Preload/Warmup. *(gộp, mô tả tổng quan)*

### 3.7. Pipeline streaming STT–MT–TTS thời gian thực — *gọn*
- 3.7.1. Phân đoạn câu Silero VAD (450ms + hangover) & duy trì ngữ cảnh (Context Sliding Buffer).
- 3.7.2. Đệm dịch ngắn (Short-MT Buffering) + Watchdog/Force Flush; SBD & Comma Fallback (nhắc gọn). ⚠️/❌
- 3.7.3. Tích hợp TTS giọng nam **runB1_e4868** vào luồng phát realtime.

---

## CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM

> Thứ tự khớp Ch3: kết quả finetune trước (4.1–4.5), kết quả hệ thống sau (4.6).

### 4.1. Môi trường & kịch bản thử nghiệm
- 4.1.1. Phần cứng huấn luyện (Colab Pro T4 16GB) & thực thi (WSL2/Windows); venv snapshotting.
- 4.1.2. Bộ dữ liệu kiểm thử: 25 câu chuẩn + 300 câu held-out; đo trên **cả GPU và CPU**.

### 4.2. Kết quả xây dựng tập dữ liệu (2 giai đoạn)
- 4.2.1. Giai đoạn 1 — VieNeu sau lọc: 1500 clip ~2.5h (WER QC, drop per-speaker).
- 4.2.2. Giai đoạn 2 — Tự thu thập YouTube: 2061 clip ~4.22h (thống kê crosscheck 3 ASR; LLM: 2023 Keep/306 Drop/38 Review).

### 4.3. Chỉ số & phương pháp đánh giá
- 4.3.1. Khách quan: RTF (GPU & CPU), WER/CER (round-trip 2 ASR), Mel loss.
- 4.3.2. Chất lượng giọng: NISQA MOS + Human MOS; F0 & đặc trưng phổ (cross-gender).
- 4.3.3. Độ trễ từng chặng & End-to-End (telemetry). ⚠️

### 4.4. Kết quả huấn luyện các mô hình
- 4.4.1. Model 1 (VieNeu e5219): đường cong Mel/KL loss, log recovery, chọn checkpoint.
- 4.4.2. Run A & Run B1: đường cong loss, monitor 3-run (epochs-to-95%), freeze-verify (B1 froze 395/673 tensor).

### 4.5. Đánh giá & so sánh chất lượng mô hình
- 4.5.1. Đánh giá Giai đoạn 1 (3-model: baseline nữ vs e5219 vs e5599) → chọn e5219. *(ngắn, thể hiện tiến trình)*
- 4.5.2. Đánh giá 4-model Giai đoạn 2 (vais1000, VieNeu e5219, Run A, Run B1): WER/CER, NISQA, F0/phổ, RTF.
- 4.5.3. Quyết định triển khai: **Run B1 (`runB1_e4868`)** — bảng tổng hợp + biểu đồ radar.
- 4.5.4. Hiệu năng suy luận **GPU & CPU** + dung lượng ONNX: bản deploy **FP32 63.5MB**; FP16 (32.1MB) chỉ là phương án dự kiến, không dùng vì model đã đủ nhẹ/nhanh.

### 4.6. Kết quả tích hợp & vận hành hệ thống S2ST — *gọn*
- 4.6.1. Client app: WebSocket, transcript interim/final, AdaptiveJitterPlayer. ❌ `[⚠️ bug đang fix]`
- 4.6.2. Cô lập loopback VoiceMeeter trong họp song hướng thực tế. ⚠️
- 4.6.3. Độ trễ tích lũy End-to-End: preload vs nạp động; ảnh hưởng VAD/SBD lên TTFA. ⚠️

---

## GHI CHÚ
1. Tỷ lệ ~65 (finetune 3.1–3.5 / 4.1–4.5) — 35 (hệ thống 3.6–3.7 / 4.6).
2. Thứ tự nhất quán: finetune trước, hệ thống sau ở cả 2 chương.
3. FP16 = dự kiến; deploy FP32; giữ số liệu GPU+CPU. ✅ (đã chốt)
4. Hai eval: giữ 4.5.1 ngắn + 4.5.2 trọng tâm. ✅ (đã chốt)
5. Thứ tự fill: ưu tiên 3.2–3.5 + 4.2/4.4/4.5 (bằng chứng mạnh) → sau đó mục hệ thống ❌ (đọc code).
