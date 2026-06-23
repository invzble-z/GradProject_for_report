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

> 13 ảnh đang là placeholder `[[HÌNH: ...]]`. Lưu ý: `DATN_BT.docx` cũ đã nhúng ~35 ảnh — nhiều ảnh lý thuyết/sơ đồ có thể tái dùng. **Claude có thể trích ảnh sẵn từ docx cũ ra file nếu bạn yêu cầu.**

Ảnh lý thuyết (có thể đã có trong docx cũ → trích lại):
- [ ] `whisper_architecture.png` — Kiến trúc tổng quát Whisper
- [ ] `nllb200_architecture.png` — Kiến trúc NLLB-200
- [ ] `vits_architecture.png` — Kiến trúc VITS

Sơ đồ cần VẼ MỚI (code PlantUML cũ đã bỏ; xử lý sau):
- [ ] `pipeline_finetune_overview.png` — Sơ đồ tổng quát quy trình finetune 2 giai đoạn → 3 model (mục 3.1)
- [ ] `che_do_2_chieu_meeting.png` — Chế độ hội thoại 2 chiều, Online Meeting (mục 3.6.1)
- [ ] `che_do_1_chieu.png` — Chế độ dịch một chiều, video/bài giảng (mục 3.6.1)

Biểu đồ thực nghiệm (từ training / Google Drive — cần bạn cung cấp file gốc hoặc ảnh):
- [ ] `vieneu_xephang_person_nam.png` — Xếp hạng thời lượng theo Person nam
- [ ] `vieneu_xephang_speaker_nam.png` — Xếp hạng Speaker nam đơn lẻ
- [ ] `vieneu_phanbo_thoiluong_1999.png` — Phân bố thời lượng tập 1999 clips
- [ ] `piper_mel_kl_loss.png` — Đường cong Mel Loss & KL Loss
- [ ] `melspec_baseline_vs_male.png` — So sánh phổ Mel baseline vs giọng nam
- [ ] `nisqa_mos_boxplot.png` — Box plot NISQA MOS các mô hình (mục 4.5.2)
- [ ] `wer_boxplot.png` — Box plot WER các mô hình (mục 4.5.2)
- [ ] `compare_normalized.png` — So sánh tốc độ hội tụ chuẩn hóa 3 run (mục 4.4.2)
- [ ] `final_radar_phase9.png` — Radar tổng hợp 4 mô hình (mục 4.5.2)

Ảnh giao diện hệ thống (chụp khi chạy client thực tế — phục vụ mục 4.6):
- [ ] `client_giao_dien_chinh.png` — Giao diện chính (2 khung transcript Việt–Anh khi đang dịch)
- [ ] `client_settings_dialog.png` — Hộp thoại cài đặt thiết bị âm thanh + giọng đọc
- [ ] (tùy chọn) `demo_meeting.png` — Ảnh demo trong cuộc họp Meet/Zoom (overlay + định tuyến VoiceMeeter)

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
