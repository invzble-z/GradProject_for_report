# USER MANUAL ACTION — Việc cần user làm thủ công

> Nơi ghi các task USER tự làm (Claude không làm thay được hoặc cần dữ liệu từ user).
> Quy ước: `[ ]` chưa làm · `[x]` xong · `(P)` ưu tiên · `(sau)` để sau.
> Khi một task cần thiết để Claude tiếp tục, Claude sẽ nhắc; bạn làm luôn hoặc báo Claude lấy dữ liệu.

---

## A. ĐIỀN PLACEHOLDER (văn bản)

- [ ] (P) **Trang tiêu đề** — điền Họ tên + MSSV các thành viên vào `<<PLACEHOLDER>>` (trong `BAOCAO_NOIDUNG.md`, mục TRANG TIÊU ĐỀ).
- [ ] **Xác nhận tên đề tài tiếng Anh** Claude đề xuất: *Research and Development of a Real-time English–Vietnamese Speech Translation System with Latency Optimization using Deep Learning.* (sửa nếu cần)
- [ ] **Xác nhận GVHD**: ThS. Trần Uyên Trang (đúng/sai).
- [ ] **Xác nhận phạm vi ngôn ngữ**: chỉ EN↔VI, không mở rộng trong báo cáo này.

## B. CUNG CẤP / CHÈN ẢNH

> Ảnh đã được trích/gom vào thư mục **`assets/`**. `[x]` = đã có trong `assets/` · `[ ]` = còn thiếu.
> ⚠️ **Cần xóa tay** các file rác `assets/misc_*.png` + `assets/misc_05.jpeg` và thư mục `assets/_unused/` (sót từ lần trích đầu / ảnh usecase-logo cũ không dùng — sandbox không xóa được).

**ĐÃ CÓ — trích từ `DATN_BT.docx`:**
- [x] `whisper_architecture.png` — Kiến trúc Whisper (2.1.2)
- [x] `nllb200_architecture.png` — Kiến trúc NLLB-200 (2.2.1)
- [x] `vits_architecture.png` — Kiến trúc VITS (2.3)
- [x] `vieneu_xephang_person_nam.png` (4.2.1)
- [x] `vieneu_xephang_speaker_nam.png` (4.2.1)
- [x] `vieneu_phanbo_thoiluong_1999.png` (4.2.1)
- [x] `piper_mel_kl_loss.png` — đường cong loss Model 1 (4.4.1)
- [x] `melspec_baseline_vs_male.png` (4.5.4)
- [x] `che_do_2_chieu_meeting.png` (3.6.1)
- [x] `che_do_1_chieu.png` (3.6.1)

**ĐÃ CÓ — gom từ `reports/` (bản phase9 4-model, đúng cho Chương 4):**
- [x] `nisqa_mos_boxplot.png` (4.5.2)
- [x] `wer_boxplot.png` (4.5.2)
- [x] `final_radar_phase9.png` (4.5.2)
- [x] `compare_normalized.png` (4.4.2)
- *(trong assets/ còn `*__OLD3model.png` = bản cũ 3-model trích từ docx — KHÔNG dùng, có thể xóa)*

**CÒN THIẾU — cần tạo/cung cấp:**
- [x] `pipeline_giai_doan_1_vieneu.png` — sơ đồ quy trình Giai đoạn 1 (3.3) — *có PNG + nguồn `.svg` trong assets/*
- [x] `pipeline_giai_doan_2_selfcollect.png` — sơ đồ quy trình Giai đoạn 2 (3.4) — *có PNG + nguồn `.svg` trong assets/*
- [ ] `client_giao_dien_chinh.png` — giao diện chính client khi đang dịch (4.6.1) — **bạn chụp**
- [ ] `client_settings_dialog.png` — hộp thoại cài đặt (4.6.1) — **bạn chụp**
- [ ] (tùy chọn) `demo_meeting.png` — ảnh demo họp Meet/Zoom (4.6.3) — **bạn chụp**

## C. CUNG CẤP DỮ LIỆU (khi Claude cần)

- [ ] **CSV / metadata trên Google Drive** (vd `gpu_log.csv`, log train, bảng số liệu NISQA/WER/RTF…): tải về bỏ vào thư mục khi Claude yêu cầu, để lấp:
  - Bảng độ trễ telemetry (mục 4.3.2)
  - Bảng kết quả đánh giá & hiệu năng mô hình (mục 4.5.3)
- [ ] **File bài báo IEEE đã có sẵn** (nội dung cũ) — cung cấp ở giai đoạn cuối để Claude cập nhật khớp code.

## D. THAO TÁC TRONG WORD (lúc render .docx)

- [ ] Đóng `DATN_BT.docx` trước khi Claude ghi (Word khóa file).
- [ ] Sau khi mở bản render: cập nhật toàn bộ field để đúng số trang — `Ctrl+A` → `F9` (Mục lục, Danh mục hình, Danh mục bảng).
- [ ] Thay ảnh thật vào đúng vị trí placeholder (nếu Claude chưa chèn được).

## E. TASK ĐỂ SAU

- [ ] (sau) Hoàn thiện **Chương 3** (phương pháp/training) — chương trọng điểm, đang rối, xử lý sau khi chuẩn hóa xong phần khác.
- [ ] (sau) Cập nhật nội dung **IEEE summary** cho khớp code mới nhất.
- [ ] (sau) Duyệt danh sách **tài liệu tham khảo APA** do Claude đề xuất.
