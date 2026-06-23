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

---

## 11. BẢN ĐỒ REPO FINETUNE (annotated tree — đọc đúng file cần, cập nhật 2026-06-22)

> Quét qua 2 subagent. Repo `piper_vi_vais1000_finetuning/` có **HAI pipeline**. Notebook là `.ipynb` → đọc bằng Read tool (parse cell), KHÔNG đọc JSON thô.

### 11.0. BA MÔ HÌNH GIỌNG NAM (làm rõ để khỏi nhầm)
- **Model 1 — VieNeu e5219:** pipeline GỐC, cross-gender FT từ `vais1000-medium` (nữ) trên **VieNeu** 1500 clip ~2.5h, FP32. *(Đây là model đang mô tả trong báo cáo Ch4 hiện tại.)*
- **Model 2 — Run A:** full fine-tune trên **dữ liệu tự thu thập YouTube** (2061 clip ~4.22h), chuẩn hóa **vinorm**.
- **Model 3 — Run B1:** **partial-freeze (freeze enc_p + dp)** + **vietnormalizer**, trên dữ liệu tự thu thập. ⭐ **BẢN DEPLOY CUỐI = `vi_VN-male-medium-runB1_e4868.onnx` (FP32, 63.5 MB)** — thắng eval 4-model.
- Eval 4-model (phase9): vais1000(nữ, ref) vs VieNeu e5219 vs Run A vs **Run B1 (thắng)**. Số chốt B1: WER 4.1% (PhoWhisper)/5.4% (Whisper-v3), CER 2.0%, NISQA **4.13**, F0 **112.8 Hz** (nam), RTF 0.15 CPU.
- ⚠️ FP16 vẫn defer ở CẢ HAI pipeline (lỗi 143 Cast node VITS). ⚠️ `csonet_abstract/` (bài báo IEEE) mô tả BẢN CŨ (chỉ VieNeu e5219) — cần cập nhật ở GĐ3.

### 11.1. PIPELINE GỐC — `docs_for_report/` + `notebooks/` (Model 1)
Tài liệu báo cáo (đọc kỹ khi viết Ch3/4):
- `00_overview.md` — toàn cảnh 9 phase, quyết định kỹ thuật, snapshot winner e5219.
- `phase0_dataset_survey.md` — khảo sát 11 nguồn; FPT-FOSD FAIL (ASR corpus) → pivot **VieNeu-TTS-140h**.
- `phase2_dataset_acquisition.md` — explore VieNeu + ghép 3 speaker nam → 1999 clip LJSpeech 22.05kHz.
- `phase2_5_qc_validation.md` — QC bằng PhoWhisper-large, WER/CER per-clip → chốt 1500 clip.
- `phase3_text_normalize.md` — Per-speaker hybrid filter + **vinorm**.
- `phase4_preprocess.md` — `piper_train.preprocess`; **2-pass phoneme_id_map** khớp 154 của vais1000.
- `phase5_train.md` — fine-tune VITS medium từ vais1000 (batch 16, LR 1e-4, FP32, ckpt/10 epoch).
- `phase5_inference_quality.md` — audit ckpt: fix padding bug, vấn đề phụ âm cuối/English loanword.
- `phase6.5_log_recovery.md` — recompute loss 84 ckpt → best = **e5219** (không phải 5599).
- `phase7_export_onnx.md` — export ONNX FP32 (~63.5MB); FP16 FAIL.
- `phase8_inference_latency.md` — **doc trọng tâm Ch4 gốc**: latency/RTF/NISQA/spectrogram/WER, winner e5219.
- `incidents_and_fixes.md` — log lỗi+fix (Ch3 lessons / Ch5). `docs_for_compact_context_15.6.2026.md` — handoff tiết lộ pipeline mới.
- Notebook: `notebooks/phase2_dataset/01-05`, `phase3_text/01`, `phase4_preprocess/01`, `phase5_train/01-02`, `phase6_recovery/01`, `phase7_export/01`, `phase8_eval/01-06` (inference→latency→nisqa→spectrogram→wer→final_decision).

### 11.2. PIPELINE MỚI — `data_collection/` (Model 2 & 3 + dữ liệu tự thu thập)
Tài liệu báo cáo `data_collection/docs_for_report/` (đọc kỹ):
- `00_pipeline_overview.md` — pivot 2026-06-05 theo GVHD, kiến trúc 2 module, dataset cuối **2061 clip ~4.22h**.
- `phase1_download.md` — yt-dlp tải 6 video YouTube (1 giọng nam) → WAV 48k.
- `phase2_transcribe.md` — faster-whisper **large-v3** word-timestamps (bỏ WhisperX do conflict).
- `phase3_segment.md` — cắt clip ~6s tại ranh giới câu → 2368 clip.
- `phase4_denoise.md` — **Demucs htdemucs** (A/B test → apply).
- `phase5_normalize.md` — 22050Hz/-23LUFS + pad lead 0.2s → 2367 clip.
- `phase6_asr_transcription.md` — 3 ASR độc lập: faster-whisper large-v3 + **Qwen3-ASR-1.7B** (local) + **Deepgram Nova-3** (API).
- `phase7_asr_crosscheck.md` — WER chéo 3 nguồn + **LLM Gemini hiệu đính** batch → 2023 Keep/306 Drop/38 Review.
- `phase8_finetune_train_v2.md` — thiết kế train v2: 4 fix baseline + partial-freeze + `train_selfcollect.py`.
- `phase8_runA_train_results.md` — **Run A** (full FT): 99 epoch/3.70h, val MA5 ~29.1.
- `phase8_runB_plan.md` — kế hoạch Run B (B1 freeze + B2 gác lại) + nghiên cứu vietnormalizer.
- `phase8_runB1_train_results.md` — **Run B1** (freeze enc_p,dp + vietnormalizer): froze 395/673 tensor.
- `phase9_monitor_results.md` — monitor 3-run (VieNeu/A/B1) hội tụ.
- `phase9_eval_results.md` — **eval 4-model → chốt deploy B1** (doc trọng tâm Ch4 mới).
- `phase10_export_onnx.md` — export ONNX FP32 B1 e4868 (63.5MB; FP16 defer).
- Kế hoạch/hợp đồng: `data_collection/PLAN.md`, `MODULE_B_CONTRACT.md`, `asr_crosscheck/{BRIEF,PLAN_CROSSCHECK}.md`.
- Notebook: `data_collection/notebooks/00-12` (download→…→05_build_metadata→**06_train Run A**→08_train **Run B1**→09 norm compare→10 rebuild vietn→11 monitor→12 export); `phase9_eval/00-06`; `asr_crosscheck/notebooks/01-03`.
- Scripts: `data_collection/scripts/` (download, segment, denoise, normalize, build_metadata, **train_selfcollect.py**, eval_synth, **vn_text_normalize.py** + `vn_protect_words.txt`).

### 11.3. SỐ LIỆU GỐC (để lấy khi viết Ch4)
- `reports/training_curves/*.csv|png` (loss/weight/LR + `*_runA/runB1` + `compare_*`), `reports/eval/*` (gốc) và `reports/eval/phase9/*` (Run A/B1), `reports/plots/*` (boxplot, radar, `final_radar_phase9.png`, spectrograms).

### 11.4. KÉO DÀI SUBAGENT (nếu cần đào sâu)
- Pipeline gốc: agent id `a077781c441d2388c`. Pipeline mới: agent id `a851511cdddfb85e0`. (Dùng SendMessage để hỏi tiếp, đỡ quét lại.)

**⚠️ HAI ĐIỂM LỆCH CẦN XỬ LÝ Ở CHƯƠNG SAU (không thuộc Ch1–2):**
1. **TTS FP16 vs FP32:** code triển khai hiện chạy **FP32**; bản FP16 bị disable do lỗi Cast node của ONNX Runtime. Báo cáo Chương 4 (4.5.2) đang trình bày kết quả lượng tử hóa FP16 (63,5→32,1 MB, RTF 0,120). → Cần làm rõ ở Ch4: FP16 là *kết quả thực nghiệm đo được*, nhưng *bản deploy dùng FP32*. (warmup_language mặc định "en" có pitfall với PhoWhisper chỉ hỗ trợ vi — lưu ý khi viết Ch3.)
2. **2-Pass Phoneme Mapping & espeak-ng:** KHÔNG tìm thấy trong code Python của 2 repo (có thể nằm trong notebook finetune hoặc trong dependency piper-train). → Khi làm Chương 3 (mục 3.5.2) phải kiểm tra `piper_vi_vais1000_finetuning/notebooks/`, `scripts/` để xác minh, nếu không có thì chỉnh cách diễn đạt.
