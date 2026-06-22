# CLAUDE.md — Quy ước làm việc cho dự án Báo cáo ĐATN (S2ST)

> File này định hướng MỌI phiên làm việc của Claude trong thư mục này. Đọc trước khi làm bất cứ việc gì.
> Cập nhật lần cuối: 2026-06-21.

---

## 1. BỐI CẢNH DỰ ÁN

Đây là **workspace soạn Báo cáo Đồ án Tốt nghiệp Kỹ sư AI (VKU 2026, định hướng NCKH)**, không phải repo code thuần. Đề tài: **Hệ thống Dịch Giọng nói Thời gian thực song hướng Anh–Việt (Speech-to-Speech Translation – S2ST)**.

Hai repo con (chỉ để đọc, lấy dữ liệu viết báo cáo):
- `GradProject/` — pipeline S2S realtime: server FastAPI (Colab T4) với 3 tầng `STT → MT → TTS` (FasterWhisper/PhoWhisper, NLLB-200 CTranslate2, Piper TTS) qua WebSocket; client PySide6.
- `piper_vi_vais1000_finetuning/` — fine-tune Piper TTS giọng nam Việt (cross-gender từ `vais1000-medium`), notebook thực nghiệm, dataset QC, đánh giá NISQA MOS.

---

## 2. NGUYÊN TẮC HOẠT ĐỘNG (BẮT BUỘC)

1. **READ-ONLY tuyệt đối với mã nguồn.** KHÔNG sửa/thêm/xóa bất kỳ dòng code nào trong `GradProject/` và `piper_vi_vais1000_finetuning/`. Chỉ đọc để trích dữ kiện.
2. **Quyền ghi:** chỉ tạo/sửa file `.md` ở thư mục gốc và file báo cáo `.docx`. (Kế thừa tinh thần `AGENTS.md` của agent trước.)
3. **Không bịa số liệu.** Mọi con số/thông số kỹ thuật phải neo vào code/notebook/log thật hoặc nội dung đã có trong báo cáo. Nếu chưa xác minh được → đánh dấu `❌`/`⚠️`, KHÔNG đoán.
4. **Tách người viết và người soát:** sau khi sửa nội dung quan trọng, tự kiểm tra chéo (đối chiếu lại nguồn) trước khi coi là xong.

---

## 3. SOURCE OF TRUTH & LUỒNG LÀM VIỆC

| File | Vai trò |
|---|---|
| `BAOCAO_NOIDUNG.md` | **GỐC nội dung** — nơi viết/sửa/review mọi nội dung. Theo dõi bằng git. |
| `DATN_BT.docx` | **Bản render cuối** — sinh/cập nhật TỪ `.md`. Mở bằng Word để xem format & số trang. |
| `MERGE_PLAN.md` | Lịch sử & kế hoạch gộp docx cũ × outline mới (tham chiếu). |
| `BAOCAO_OUTLINE.md` | Outline chi tiết tới cấp 3 (tham chiếu cấu trúc). |

**Quy tắc vàng:** sửa nội dung ở `.md` trước → rồi mới đồng bộ sang `.docx`. KHÔNG sửa nội dung trực tiếp trong docx rồi mong md tự cập nhật (hai chiều sẽ lệch).

**Lưu ý kỹ thuật docx ↔ md:**
- Word khóa file khi đang mở → đóng `.docx` trước khi Claude ghi, nếu không lệnh ghi sẽ lỗi permission.
- Số trang trong Mục lục / Danh mục hình / Danh mục bảng do Word tính lúc phân trang → chỉ đúng khi mở trong Word và cập nhật field (Ctrl+A → F9). Không kiểm số trang trong `.md`.
- `.docx` là binary → git diff vô dụng; version hóa chủ yếu ở `.md` + log. Rollback docx như file nhị phân.

---

## 4. CẤU TRÚC BÁO CÁO (ĐÃ XÁC NHẬN VỚI HƯỚNG DẪN CỦA KHOA)

Theo *Hướng dẫn Báo cáo ĐATN Định hướng NCKH 2026 v2* — bảng cấu trúc dành cho **Khoa KHMT / KTMT&ĐT**. Outline 5 chương hiện tại **KHỚP** yêu cầu:

1. **Chương 1. Giới thiệu** — Lý do chọn đề tài, Phát biểu bài toán, Mục tiêu & Đóng góp, (Đối tượng/Phạm vi), Bố cục.
2. **Chương 2. Tổng quan tài liệu & Cơ sở lý thuyết** — Background + Related Work (nêu rõ điểm mạnh & **khoảng trống nghiên cứu**).
3. **Chương 3. Phương pháp nghiên cứu đề xuất** — Mô hình tổng quát (sơ đồ khối/kiến trúc/phần mềm đề xuất) + Phương pháp đề xuất.
4. **Chương 4. Kết quả thực nghiệm** — Môi trường & kịch bản thử nghiệm + Các chỉ số đánh giá định lượng/định tính.
5. **Chương 5. Kết luận & Hướng phát triển** — Đóng góp + Hạn chế + Kiến nghị/Hướng phát triển.
- **Reference list** — chuẩn **APA**.
- **Appendices** — tư liệu thêm (nếu có).
- **Summary / Tóm tắt** — dạng **bài báo mẫu IEEE** (hoặc bài báo đã công bố).

Ghi chú: hướng dẫn cho phép *không bắt buộc đánh số chương* với chương quá ngắn (1–2 trang). Mốc số trang chi tiết (5–7 trang, ≤25 trang…) trong `BAOCAO_OUTLINE.md` là tham khảo, bảng dành cho Khoa KHMT không quy định cứng.

---

## 5. FORMAT (theo de-facto trong DATN_BT.docx + cần chốt thêm)

Hướng dẫn của Khoa **không quy định typography chi tiết** (chỉ quy định cấu trúc + APA + IEEE summary). Format thực tế đang dùng trong `DATN_BT.docx`:

- **Lề:** trái 3.0 cm, phải 2.0 cm, trên 2.0 cm, dưới 2.0 cm. ✅
- **Font:** Times New Roman. ✅
- **Cỡ chữ thân:** **13pt** (chuẩn hóa toàn bộ, bỏ chỗ đang lẫn 12pt). ✅ CHỐT
- **Giãn dòng:** **1.3**. ✅ CHỐT
- **Heading:** Heading 1/2/3 đậm; đánh số `1.1.1` (Numbering style theo hướng dẫn).

### Quy ước hình & bảng (BẮT BUỘC)
- **Đánh số theo CHƯƠNG**: Hình 2.1, Hình 3.4; Bảng 3.1… Dùng **SEQ field** trong docx để tự đánh số (không gõ số tay).
- **Caption dùng style "Caption"**, KHÔNG dùng Heading (tránh lọt vào Mục lục chính).
- **Danh mục hình / Danh mục bảng** sinh tự động bằng **Table of Figures field** (`TOC \c "Hình"` / `\c "Bảng"`), riêng biệt.
- Trong `.md`: KHÔNG hardcode số. Dùng `[[HÌNH: ten_file.png | Chú thích]]` và `[[BẢNG: | Chú thích]]`.

---

## 6. QUY ƯỚC NHÃN TRẠNG THÁI (dùng trong BAOCAO_NOIDUNG.md)

- `✅` đã có nội dung (đã viết / bê từ docx).
- `⚠️` cần sửa hoặc đối chiếu lại code.
- `❌` chưa có, viết mới sau (đọc code read-only).
- `🔄` số liệu đang cập nhật (đang train).

---

## 7. GIT

- Version hóa: `BAOCAO_NOIDUNG.md`, `MERGE_PLAN.md`, `CLAUDE.md`, và các `.md` khác.
- Commit **theo từng sửa đổi/từng mục có ý nghĩa**, message dẫn chiếu mục báo cáo hoặc nguồn code, để rollback gọn.
- Không tự ý commit khi working tree còn file dở của user; hỏi trước hoặc chỉ stage đúng file liên quan.

---

## 8. THÔNG TIN CẦN USER CUNG CẤP (điền dần)

- [x] **Typography:** Times New Roman, **13pt, giãn dòng 1.3**, lề 3/2/2/2 cm. (Không dùng template riêng.) ✅
- [x] **Tài liệu tham khảo:** **Claude đề xuất** danh sách APA từ các mô hình/thư viện đã dùng → user duyệt. ✅
- [x] **IEEE summary:** **Đã có sẵn 1 bài báo định dạng IEEE** nhưng nội dung CHƯA cập nhật theo code mới nhất. → Để **giai đoạn cuối**, chỉ cần sửa nội dung cho khớp. *(User cung cấp file bài báo này khi tới bước đó.)*
- [x] **Tên đề tài (VI):** "Nghiên cứu và phát triển hệ thống dịch thuật giọng nói thời gian thực Anh – Việt với tối ưu hóa độ trễ sử dụng Deep Learning". ✅
- [~] **Trang tiêu đề:** tên đề tài EN (Claude đề xuất, chờ xác nhận), họ tên + MSSV thành viên (**placeholder, user tự điền** — xem `user_manual_action.md`), GVHD *ThS. Trần Uyên Trang*.
- [x] **Số liệu train (🔄):** **ĐÃ HOÀN THÀNH, code đã cập nhật mới nhất.** Lưu ý: một số file CSV/metadata nằm trên Google Drive — khi cần Claude sẽ yêu cầu user tải về cung cấp.
- [ ] **Cặp ngôn ngữ/độ rộng phạm vi:** xác nhận chỉ EN↔VI (không mở rộng trong phạm vi báo cáo này).

> **LƯU Ý CHƯƠNG 3 (Phương pháp đề xuất / training):** đây là chương trọng điểm, đã thay đổi nhiều và đang rối. **CHƯA đụng nội dung Chương 3** — ưu tiên chuẩn hóa các phần lặt vặt khác trước, khi nào user yêu cầu mới tập trung xử lý Chương 3.

---

## 9. LỘ TRÌNH & THEO DÕI TIẾN ĐỘ

> Đây là bảng theo dõi tiến độ tổng. Cập nhật checkbox khi xong từng mục. 4 giai đoạn.

### GIAI ĐOẠN 1 — Rà soát & chuẩn hóa Chương 1, 2  ⏳ *(đang/ kế tiếp)*
- [ ] 1.1. Đối chiếu nội dung Ch1 (Giới thiệu) giữa `BAOCAO_NOIDUNG.md` ↔ docx cũ; viết mục `1.5 Bố cục`.
- [ ] 1.2. Đối chiếu Ch2 (Tổng quan & CSLT) với docx; bổ sung `2.3.2–2.3.4` (toán VITS), `2.4.1` (Silero), espeak-ng.
- [ ] 1.3. Viết `2.5 Related Work & khoảng trống nghiên cứu`.
- [ ] 1.4. **Verify chéo thông số kỹ thuật** Ch1/2 với code/config (tên & phiên bản model: PhoWhisper-medium-ct2, Faster-Whisper, NLLB-200 ct2; ngưỡng VAD 450ms; v.v.) — đọc **read-only**.
- [ ] 1.5. Rà soát front matter: Danh mục chữ viết tắt, Lời cảm ơn.
- **Kết quả GĐ1:** Ch1, Ch2 đạt ✅ và đã verify.

### GIAI ĐOẠN 2 — Thiết kế & viết Chương 3, 4 (TRỌNG TÂM)
> Đây là lúc xử lý Chương 3 (gỡ lưu ý "chưa đụng" ở §8).
- [ ] 2.1. Đọc **read-only** docs repo finetune (`piper_vi_vais1000_finetuning/docs_for_report/`, `reports/`, `evaluation/`) + `GradProject/server/docs/`, `shared_docs/`. Lập kho dữ kiện (fact inventory).
- [ ] 2.2. **THIẾT KẾ TRÌNH BÀY**: chốt outline chi tiết Ch3 (phương pháp) vs Ch4 (thực nghiệm/kết quả) — nội dung nào ở chương nào, thứ tự viết.
- [ ] 2.3. **User DUYỆT outline chi tiết Ch3+Ch4** trước khi fill.
- [ ] 2.4. Fill nội dung: ưu tiên phần có bằng chứng mạnh trước (dataset, fine-tuning, kết quả train), sau đó các mục `❌` từ code (frame protocol, Facade/Execution Lane/Preload, SBD/telemetry, kết quả client app).
- [ ] 2.5. Verify chéo toàn bộ số liệu Ch4 với log/CSV thật.
- **Kết quả GĐ2:** Ch3, Ch4 hoàn chỉnh & verify.

### GIAI ĐOẠN 3 — Chương 5, Tài liệu tham khảo, IEEE
- [ ] 3.1. Viết/giãn Ch5 (Kết luận) — **sau khi Ch4 chốt số liệu**, bám kết quả thật.
- [ ] 3.2. Claude đề xuất danh sách **tài liệu tham khảo APA** → user duyệt.
- [ ] 3.3. Cập nhật **IEEE summary** từ bài báo có sẵn cho khớp code (user cung cấp file).
- **Kết quả GĐ3:** đủ nội dung toàn báo cáo.

### GIAI ĐOẠN 4 — Tinh chỉnh & xuất bản
- [ ] 4.1. Soát cuối toàn văn (mạch lạc, thuật ngữ, đối chiếu nguồn lần cuối — có thể dùng subagent).
- [ ] 4.2. Cấu hình template docx: style (TNR 13pt, giãn 1.3, lề 3/2/2/2) + SEQ field + Table of Figures/Tables.
- [ ] 4.3. Đồng bộ `BAOCAO_NOIDUNG.md` → `DATN_BT.docx` theo template.
- [ ] 4.4. User làm các task trong `user_manual_action.md` (placeholder, ảnh, `Ctrl+A→F9` cập nhật field).
- [ ] 4.5. Kiểm tra bản render cuối trong Word (số trang, danh mục, định dạng).
- **Kết quả GĐ4:** `DATN_BT.docx` hoàn chỉnh nộp được.

---

## 10. KHO DỮ KIỆN KỸ THUẬT ĐÃ VERIFY (đối chiếu code, read-only — cập nhật 2026-06-22)

> Để các phiên sau khỏi quét lại codebase. Tất cả đã đối chiếu qua subagent với 2 repo con.

**Bản đồ file code quan trọng (GradProject):**
- STT: `server/core_ai/stt_engine/base.py`, `faster_whisper_engine.py`, `stt_engine.py` (facade)
- VAD: `server/core_ai/vad/silero_vad.py`; cắt câu: `server/api/websocket/streaming/stt_session_manager.py`
- MT: `server/core_ai/mt_engine/base.py`, `models_engine/nllb_ct2_engine.py`
- TTS: `server/core_ai/tts_engine/tts_engine.py`, `models_engine/piper_onnx_engine.py`, `selection/factory.py`
- Runtime: `server/core_ai/stt_engine/runtime/execution_lane.py`; WebSocket: `server/api/websocket/router.py`
- Client: `client/main.py`, `audio/pyaudio_manager.py`, `audio/capture_loopback.py`, `audio/player.py`, `audio/install_vb_cable.py`, `gui/components/settings_dialog.py`

**Thông số ĐÃ XÁC MINH KHỚP (dùng tự tin):**
- STT VI: **PhoWhisper-medium** (CTranslate2, `phowhisper-medium-ct2`); STT EN: **Faster-Whisper small** đa ngôn ngữ, compute **float16** (CPU: float32).
- Đầu vào STT: PCM **16 kHz**, chunk **200 ms**.
- VAD: **Silero VAD**; ngưỡng im lặng **450 ms** (`SILENCE_THRESHOLD_FRAMES=2.25`); **Hangover 2 frames (~400 ms)**; ngưỡng xác suất **0.5**.
- MT: **NLLB-200 distilled-600M** qua **CTranslate2**, compute **int8**.
- TTS: nền **vi_VN-vais1000-medium**, **4 giọng** (vi/en × nam/nữ), ONNX, **22050 Hz**, chạy trên **server (GPU)**.
- Server: **FastAPI + WebSocket** (`/ws`); có **Facade** 3 engine, **Preload/Warmup**, **ExecutionLane** (thread pool max_workers=4 + operation_lock).
- Client: **PySide6 + qasync**, **PyAudio**, **SoundCard** (WASAPI loopback), **Route 0** (mic/dịch đi) / **Route 1** (loopback/âm cuộc họp).
- **ĐỊNH TUYẾN ÂM THANH = VoiceMeeter Banana** (KHÔNG còn dùng VB-Audio Cable — VB-Cable một cáp đơn không đủ chống vòng lặp tự dịch). VoiceMeeter cho nhiều bus ảo: Route 0 → `VoiceMeeter Input` → bus B1 (mic ảo cho Meet/Zoom); Route 1 → `VoiceMeeter Aux Input` (thu âm cuộc họp). Điều khiển qua `VoicemeeterRemote64.dll`. File: `client/audio/voicemeeter_controller.py`, `install_voicemeeter.py`, `uninstall_voicemeeter.py`, `virtual_setup.py`, `device_router.py`; doc `client/docs/implementation_plan_voicemeeter_routing.md`. Hai chế độ: `system` (Hệ thống) & `conversation` (Hội thoại). `install_vb_cable.py` & `shared_docs/audio_routing_solution.md` là DI SẢN CŨ (VB-Cable), bỏ qua.
  - ⚠️ CHƯƠNG 3 còn nhắc "VB-Cable" ở 3.1.1 (mô tả chế độ 2 chiều) và 3.2.3 → phải sửa thành VoiceMeeter khi viết Ch3.

**⚠️ HAI ĐIỂM LỆCH CẦN XỬ LÝ Ở CHƯƠNG SAU (không thuộc Ch1–2):**
1. **TTS FP16 vs FP32:** code triển khai hiện chạy **FP32**; bản FP16 bị disable do lỗi Cast node của ONNX Runtime. Báo cáo Chương 4 (4.5.2) đang trình bày kết quả lượng tử hóa FP16 (63,5→32,1 MB, RTF 0,120). → Cần làm rõ ở Ch4: FP16 là *kết quả thực nghiệm đo được*, nhưng *bản deploy dùng FP32*. (warmup_language mặc định "en" có pitfall với PhoWhisper chỉ hỗ trợ vi — lưu ý khi viết Ch3.)
2. **2-Pass Phoneme Mapping & espeak-ng:** KHÔNG tìm thấy trong code Python của 2 repo (có thể nằm trong notebook finetune hoặc trong dependency piper-train). → Khi làm Chương 3 (mục 3.5.2) phải kiểm tra `piper_vi_vais1000_finetuning/notebooks/`, `scripts/` để xác minh, nếu không có thì chỉnh cách diễn đạt.
