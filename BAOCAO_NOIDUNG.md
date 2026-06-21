<!--
==================================================================
  BAOCAO_NOIDUNG.md — FILE GROUND-TRUTH NỘI DUNG BÁO CÁO ĐATN
  Sinh từ: DATN_BT.docx (nội dung) × BAOCAO_OUTLINE.md (cấu trúc)
  Theo MERGE_PLAN.md. Đây là nguồn nội dung chính; .docx là bản render.
==================================================================
  QUY ƯỚC (LEGEND):
  • Nhãn trạng thái cuối mỗi mục:
      ✅ = đã có nội dung (bê từ docx)   ⚠️ = cần sửa / đối chiếu code
      ❌ = chưa có, viết mới sau (đọc code read-only)
      🔄 = số liệu đang cập nhật (đang train)
  • Ảnh:  [[HÌNH: ten_file.png | Chú thích]]   → placeholder, thay ảnh thủ công.
  • Bảng: [[BẢNG: | Chú thích]] đặt ngay trên bảng markdown.
  • KHÔNG hardcode số "Hình 1", "Bảng 2"… — số đánh theo CHƯƠNG, do
    SEQ field tự sinh khi xuất .docx (Hình 2.1, Bảng 3.1…).
==================================================================
-->

# BÁO CÁO ĐỒ ÁN TỐT NGHIỆP — HỆ THỐNG DỊCH GIỌNG NÓI THỜI GIAN THỰC SONG HƯỚNG ANH–VIỆT (S2ST)

## TRANG THỦ TỤC & DẪN NHẬP

- TRANG TIÊU ĐỀ — *giữ nguyên trong .docx* ✅
- LỜI CẢM ƠN — *giữ nguyên nội dung hiện có trong docx* ✅
- DANH MỤC CÁC CHỮ VIẾT TẮT — *giữ bảng 19×4 hiện có* ✅
- DANH MỤC BẢNG — *tự sinh bằng Table of Tables field khi xuất docx* (xóa danh mục rác cũ) ⚠️
- DANH MỤC HÌNH VẼ – ĐỒ THỊ — *tự sinh bằng Table of Figures field* (xóa danh mục rác cũ) ⚠️

---

# CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

> Nguồn: phần "LỜI MỞ ĐẦU" trong docx, tái cấu trúc theo outline 1.1–1.5.

## 1.1. Lý do chọn đề tài

Trong bối cảnh toàn cầu hóa và sự phát triển mạnh mẽ của công nghệ số, các nền tảng họp trực tuyến như Zoom, Google Meet hay Microsoft Teams đã trở thành công cụ quan trọng trong hoạt động giao tiếp và hợp tác quốc tế. Tuy nhiên, khác biệt ngôn ngữ vẫn là một rào cản lớn khiến quá trình trao đổi thông tin gặp nhiều khó khăn. Các giải pháp truyền thống như thuê phiên dịch viên tuy mang lại chất lượng dịch thuật cao nhưng thường tốn kém chi phí, khó triển khai linh hoạt và tiềm ẩn những vấn đề liên quan đến bảo mật thông tin. Trong khi đó, các công cụ dịch văn bản thông thường yêu cầu người dùng thao tác thủ công, làm gián đoạn dòng hội thoại và không đáp ứng được nhu cầu giao tiếp thời gian thực.

Trước thực tế đó, hệ thống dịch giọng nói sang giọng nói thời gian thực (Speech-to-Speech Translation – S2ST) được xem là một hướng tiếp cận đầy tiềm năng. Tuy nhiên, việc triển khai hệ thống trong môi trường họp trực tuyến vẫn đối mặt với nhiều thách thức: độ trễ phát sinh qua các giai đoạn STT → NMT → TTS có thể làm giảm tính tự nhiên của hội thoại; đặc điểm thanh điệu và cách ngắt nghỉ trong tiếng Việt khiến hệ thống dễ xác định sai điểm kết thúc câu; nguồn mô hình tổng hợp giọng nam tiếng Việt chất lượng cao, nhẹ còn hạn chế; và hiện tượng phản hồi âm học khi âm thanh đã dịch bị micro thu lại gây vòng lặp dịch không mong muốn.

Do đó, nghiên cứu các giải pháp giảm độ trễ, nâng cao độ chính xác nhận dạng, phát triển mô hình TTS phù hợp và kiểm soát phản hồi âm học là cần thiết, làm cơ sở xây dựng một hệ thống dịch giọng nói thời gian thực có tính ứng dụng cao. ✅

## 1.2. Phát biểu bài toán

- 1.2.1. Nhận dạng tiếng nói (STT) dạng streaming trên luồng âm thanh liên tục không mất ngữ cảnh.
- 1.2.2. Dịch máy hội thoại (NMT) bảo toàn ngữ nghĩa và tính tự nhiên của vế nói ngắn, rời rạc.
- 1.2.3. Thiếu hụt mô hình TTS giọng nam Việt chất lượng cao, dung lượng nhẹ phục vụ thời gian thực.
- 1.2.4. Cô lập luồng thu/phát chống vòng lặp phản hồi âm học (feedback loop) trong môi trường họp. ✅

## 1.3. Mục tiêu và Đóng góp của đề tài

Đồ án hướng tới các mục tiêu chính: (1) Xây dựng hệ thống S2ST thời gian thực theo mô hình Client–Server qua WebSocket, xử lý gần thời gian thực, giảm độ trễ; (2) Nghiên cứu các giải pháp tối ưu xử lý âm thanh: phát hiện khoảng dừng, phân đoạn câu, quản lý bộ đệm dịch; (3) Xây dựng và tinh chỉnh mô hình TTS tiếng Việt giọng nam trên nền Piper, dung lượng nhỏ, chạy trên máy phổ thông; (4) Thiết kế cơ chế kiểm soát phản hồi âm học; (5) Đánh giá hiệu năng qua độ trễ, chất lượng STT, độ chính xác dịch và chất lượng âm thanh tổng hợp. ✅

## 1.4. Đối tượng và Phạm vi nghiên cứu

**Đối tượng:** các công nghệ và mô hình AI cho bài toán S2ST (STT, NMT, TTS), phương pháp VAD, cơ chế truyền dữ liệu thời gian thực Client–Server và các giải pháp xử lý âm thanh.

**Phạm vi:** hệ thống dịch song hướng cặp Việt–Anh; mô hình Client–Server (xử lý AI trên server, client Windows); điều kiện tài nguyên giới hạn (1 GPU tầm trung phía server, máy cá nhân phổ thông phía client); xây dựng mô hình TTS giọng nam Việt từ dữ liệu đã tiền xử lý; đánh giá qua độ trễ, chất lượng STT, độ chính xác dịch và chất lượng âm thanh đầu ra.

*Cách tiếp cận & phương pháp nghiên cứu (kiến trúc phân tán Client–Server; xử lý bất đồng bộ + preload; transfer learning cho TTS; kiểm soát phản hồi âm học qua thiết bị âm thanh ảo) — đã có prose trong docx, đưa vào 1.4 hoặc tách 1.4.x.* ✅

## 1.5. Bố cục của Báo cáo

Tóm tắt nội dung 5 chương + sơ đồ liên kết logic giữa các chương. ❌ *(viết mới)*

---

# CHƯƠNG 2. TỔNG QUAN TÀI LIỆU VÀ CƠ SỞ LÝ THUYẾT

> Nguồn: docx "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ".

## 2.1. Cơ sở lý thuyết về Nhận dạng tiếng nói (STT)

### 2.1.1. Bài toán nhận dạng tiếng nói streaming trên luồng âm thanh liên tục

Nhận dạng tiếng nói (STT) là quá trình chuyển tín hiệu âm thanh thành văn bản — thành phần quan trọng nhất của hệ thống S2ST vì chất lượng văn bản đầu ra ảnh hưởng trực tiếp đến các giai đoạn dịch và tổng hợp phía sau. Trong hệ thống truyền thống, âm thanh được thu thành tệp hoàn chỉnh trước khi xử lý, cho độ chính xác cao nhờ khai thác toàn bộ ngữ cảnh; nhưng với ứng dụng thời gian thực, chờ người dùng nói xong sẽ làm tăng đáng kể độ trễ. Vì vậy hệ thống hiện đại dùng kỹ thuật Streaming STT: âm thanh được chia thành các đoạn ngắn và truyền liên tục đến máy chủ để xử lý ngay khi người dùng đang nói.

Khác với nhận dạng trên tệp hoàn chỉnh, streaming yêu cầu xử lý liên tục các đoạn ngắn khi chưa có đủ ngữ cảnh. Hệ thống thường cung cấp hai loại kết quả: kết quả tạm thời (Interim) cập nhật liên tục để phản hồi tức thời, và kết quả cuối cùng (Final) chính xác hơn khi xác định người dùng đã kết thúc phát ngôn. Thách thức lớn nhất là thiếu hụt ngữ cảnh khi suy luận, đặc biệt với từ đồng âm, câu phức tạp hoặc thuật ngữ chuyên ngành. ✅

### 2.1.2. Mô hình Whisper và Faster-Whisper

Whisper (OpenAI) dùng kiến trúc Encoder–Decoder dựa trên Transformer, huấn luyện trên tập âm thanh đa ngôn ngữ quy mô lớn. Tín hiệu âm thanh được chuyển thành Mel Spectrogram, đưa vào Encoder để trích đặc trưng ngữ âm; Decoder dùng Self-Attention và Cross-Attention sinh kết quả nhận dạng. Nhờ học đầu-cuối, Whisper chuyển trực tiếp âm thanh sang văn bản mà không cần tách riêng mô hình âm học và ngôn ngữ.

[[HÌNH: whisper_architecture.png | Kiến trúc tổng quát của mô hình Whisper]] ✅

### 2.1.3. Mô hình PhoWhisper cho tiếng Việt

PhoWhisper là phiên bản tinh chỉnh từ Whisper trên dữ liệu tiếng Việt, cải thiện khả năng nhận dạng đặc điểm ngữ âm và từ vựng đặc thù, cho độ chính xác cao hơn với tên riêng, thuật ngữ chuyên ngành và phát ngôn tiếng Việt thực tế. Đây là lý do PhoWhisper được chọn làm mô hình STT cho luồng tiếng Việt của hệ thống. ✅

## 2.2. Cơ sở lý thuyết về Dịch máy thần kinh (NMT)

### 2.2.1. Tổng quan kiến trúc NLLB-200

Dịch máy thần kinh (NMT) chuyển văn bản từ ngôn ngữ nguồn sang đích. NLLB-200 (No Language Left Behind) là mô hình dịch đa ngôn ngữ hỗ trợ hơn 200 ngôn ngữ, gồm Anh và Việt. Khác với dịch văn bản truyền thống, đầu vào của dịch hội thoại thời gian thực sinh ra từ tầng STT nên thường tự phát, không hoàn chỉnh ngữ pháp, ngắn và thiếu ngữ cảnh.

[[HÌNH: nllb200_architecture.png | Kiến trúc tổng quát mô hình NLLB-200]]

Quá trình huấn luyện NLLB bắt đầu từ thu thập dữ liệu (NLLB Seed, Public Bitext, dữ liệu đơn ngữ), nhận diện ngôn ngữ và làm sạch, dùng LASER3 để biểu diễn câu thành vector ngữ nghĩa và khai thác cặp song ngữ tương đồng (Mined Bitext). Mô hình huấn luyện bằng Mixture of Experts (MoE), Curriculum Learning, Self-Supervised Training và Back-Translation; đánh giá qua FLORES-200, Toxicity-200 và đánh giá chủ quan. Nhờ đó NLLB-200 tạo bản dịch chất lượng cao, giữ ngữ nghĩa câu nguồn, hạn chế dịch từng từ rời rạc. ✅

### 2.2.2. Lượng tử hóa và tối ưu suy luận với CTranslate2

CTranslate2 là thư viện tối ưu suy luận cho mô hình Transformer, hỗ trợ lượng tử hóa và khai thác hiệu quả phần cứng, tăng tốc cả Faster-Whisper và NLLB-200. ✅

## 2.3. Cơ sở lý thuyết về Tổng hợp tiếng nói (TTS) dựa trên kiến trúc VITS

Trong S2ST, tầng cuối chuyển văn bản đã dịch thành tín hiệu âm thanh, gồm tổng hợp tiếng nói (TTS) và quản lý luồng âm thanh đầu ra. TTS thời gian thực không chỉ cần âm thanh rõ ràng mà còn phải suy luận nhanh để hạn chế độ trễ toàn hệ thống. Các kiến trúc tối ưu như VITS và Piper TTS được thiết kế học sâu đầu-cuối, tạo giọng tự nhiên với tốc độ nhanh và dung lượng nhỏ, phù hợp thiết bị phổ thông.

[[HÌNH: vits_architecture.png | Kiến trúc tổng quát mô hình VITS trong huấn luyện và suy luận]]

### 2.3.1. Phân tích kiến trúc VITS

VITS cho phép chuyển trực tiếp văn bản thành tín hiệu âm thanh, không tách riêng dự đoán phổ và vocoder như TTS truyền thống. Ở huấn luyện, chuỗi văn bản → âm vị (Phonemes) → Text Encoder để trích đặc trưng ngôn ngữ; đồng thời phổ tuyến tính (Linear Spectrogram) của câu thực đưa vào Posterior Encoder để học biểu diễn tiềm ẩn. Monotonic Alignment Search (MAS) căn chỉnh tự động giữa âm vị và tín hiệu; Stochastic Duration Predictor dự đoán thời lượng phát âm tạo ngữ điệu tự nhiên. Ở suy luận, mô hình nhận đầu vào là chuỗi âm vị, qua Flow Decoder và Decoder sinh trực tiếp dạng sóng (Raw Waveform). ✅

### 2.3.2. Posterior Encoder & Prior Encoder
### 2.3.3. Normalizing Flows
### 2.3.4. HiFi-GAN Decoder & Discriminators (MPD, MSD)

> Các tiểu mục 2.3.2–2.3.4 cần phân tích toán học sâu hơn theo outline; docx mới mô tả ở mức tổng quan trong 2.3.1. ⚠️

### 2.3.5. Kiến trúc Piper TTS và mã hóa âm vị espeak-ng cho tiếng Việt

Piper TTS kế thừa và tối ưu VITS, hỗ trợ xuất ONNX để chạy trực tiếp trên CPU, phục vụ tổng hợp tiếng nói thời gian thực trên thiết bị tài nguyên hạn chế. Cơ chế phonemize dùng espeak-ng. ✅ *(bổ sung chi tiết espeak-ng ⚠️)*

## 2.4. Phân đoạn hoạt động giọng nói bằng Silero VAD

Silero VAD là mô hình phát hiện hoạt động giọng nói (Voice Activity Detection) kích thước nhỏ, tốc độ cao, xác định chính xác thời điểm bắt đầu/kết thúc phát ngôn, giảm dữ liệu dư thừa và cải thiện hiệu quả nhận dạng. Vai trò: chia đoạn tín hiệu đầu vào cho pipeline dịch streaming. ✅ *(bổ sung 2.4.1 thuật toán phân lớp speech/silence ⚠️)*

## 2.5. Các nghiên cứu liên quan & Khoảng trống nghiên cứu

- 2.5.1. Đánh giá các giải pháp S2S hiện có (đa số cascaded offline hoặc tính phí cao).
- 2.5.2. Hiện trạng mô hình Piper tiếng Việt: chỉ có base `vi_VN-vais1000-medium` giọng nữ, thiếu giọng nam Việt chất lượng.
- 2.5.3. Khoảng trống: tối ưu độ trễ cumulative cho pipeline streaming song hướng trên GPU/VRAM giới hạn.

❌ *(viết mới — cần tổng hợp tài liệu)*

## 2.6. Các công nghệ và thư viện sử dụng

> Quyết định: giữ làm mục con ngắn gọn ở Chương 2.

**Phía máy chủ (Server-side):** FastAPI (framework Web API bất đồng bộ chuẩn ASGI, làm máy chủ trung tâm nhận audio và trả kết quả STT/MT thời gian thực); WebSocket (giao thức song công truyền audio chunk và nhận kết quả tức thời trên một kết nối).

**Phía máy khách (Client-side):** PySide6 (GUI Qt cho Python, hiển thị văn bản/trạng thái/kết quả dịch); PyAudio (thu âm từ micro, phát âm thanh tổng hợp); SoundCard (truy cập thiết bị âm thanh Windows qua WASAPI, ghi Loopback Capture không cần quyền admin); VB-Audio Virtual Cable (trình điều khiển âm thanh ảo định tuyến âm thanh dịch tới phần mềm họp, hạn chế phản hồi âm học).

**Thư viện mô hình AI:** CTranslate2 (tối ưu suy luận Transformer, tăng tốc Faster-Whisper & NLLB-200); Silero VAD (phát hiện hoạt động giọng nói). Ngôn ngữ nền tảng: Python. ✅

---

# CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT

> Nguồn: docx "CHƯƠNG 2: PHÂN TÍCH THIẾT KẾ" (rút gọn) + "CHƯƠNG 3: TRIỂN KHAI" (phần thiết kế).

## 3.1. Thiết kế Kiến trúc Hệ thống Tổng quát (S2ST Client–Server)

**Yêu cầu hệ thống.** Hệ thống hỗ trợ dịch song ngữ Anh–Việt trong họp trực tuyến thời gian thực: thu đồng thời hai luồng âm thanh (người dùng nội bộ và nền tảng họp), xử lý độc lập; dịch hai chiều Việt–Anh; hiển thị transcript nhận dạng và bản dịch; lưu/khôi phục cấu hình (thiết bị âm thanh, ngôn ngữ, tham số kết nối). Yêu cầu phi chức năng: độ trễ mục tiêu < 1,5 giây; kết nối ổn định; tối ưu tài nguyên cho máy phổ thông; hạn chế vọng tiếng/phản hồi vòng lặp; kiến trúc dễ mở rộng và bảo trì. ✅

**Tác nhân chính (rút gọn).** Người dùng nội bộ (Local User) dùng client PySide6; Thành viên họp từ xa (gián tiếp qua nền tảng họp); Máy chủ dịch thuật AI (FastAPI: STT–MT–TTS); Hệ thống họp trực tuyến (Zoom/Google Meet). ✅
*(Lược bỏ: bộ usecase chi tiết, kịch bản và 13 sơ đồ tuần tự kiểu phần mềm theo quyết định merge — không phù hợp khung NCKH.)*

### 3.1.1. Sơ đồ khối kiến trúc kết nối song công qua WebSocket

Hệ thống vận hành hai chế độ định tuyến âm thanh:

[[HÌNH: che_do_2_chieu_meeting.png | Chế độ hội thoại 2 chiều – Online Meeting Platform]]

Chế độ 2 chiều (Bidirectional – Online Meeting): Route 0 (Việt→Anh) lấy âm thanh từ micro → STT PhoWhisper → NLLB VI→EN → TTS English → RoutePlayer → VB-Cable (đưa vào phần mềm họp); Route 1 (Anh→Việt) lấy âm thanh họp qua WASAPI Loopback → STT Faster-Whisper → NLLB EN→VI → TTS Vietnamese → loa/tai nghe vật lý.

[[HÌNH: che_do_1_chieu.png | Chế độ dịch một chiều (video/bài giảng)]]

Chế độ 1 chiều (Unidirectional – video/YouTube/bài giảng): nguồn audio tiếng Anh qua WASAPI Loopback → Route 1 → STT EN → NLLB EN→VI → TTS Vietnamese → loa vật lý. ✅
*(Định nghĩa sơ đồ gốc bằng PlantUML đã được lưu giữ từ docx; cần render thành ảnh để chèn.)*

### 3.1.2. Khung truyền nhị phân (Binary Pipeline Frame) và khung điều khiển JSON (Control Frame)

Thiết kế định dạng frame nhị phân (audio chunk + route) và JSON control frame. ❌ *(viết mới — đọc code `GradProject/server/api/websocket/`, `shared_docs/`)*

### 3.1.3. Cấu trúc Session State và cơ chế định tuyến Mode-Dispatch

❌ *(viết mới — đọc code, read-only)*

## 3.2. Thiết kế Client App (PySide6) và Giải pháp Cô lập Loopback

- 3.2.1. Tích hợp PySide6 với vòng lặp sự kiện `qasync` trên Windows. ❌
- 3.2.2. Định tuyến hai tuyến Route 0 (loa mặc định) và Route 1 (VB-CABLE Input). ✅ *(ý đã có ở 3.1.1, mở rộng)*
- 3.2.3. Tự nhận diện và ánh xạ thiết bị VB-Audio Virtual Cable không cần quyền Administrator. ⚠️
- 3.2.4. Thu âm loopback WASAPI cô lập âm phản hồi (Acoustic Echo & Feedback Loop Mitigation). ⚠️

## 3.3. Thiết kế Server App (FastAPI) phân tầng Hướng Engine

- 3.3.1. Polymorphic Facade Pattern: đồng bộ ~85% kiến trúc giao tiếp 3 AI Engine (STT, MT, TTS) qua contract chung (`load_async`, `infer_async`, `cleanup_session`...).
- 3.3.2. Kiến trúc song song hóa Execution Lane (worker pools + operation locks) ngăn race condition trên GPU VRAM.
- 3.3.3. Preload & Warmup triệt tiêu độ trễ cold-start lúc startup.

❌ *(viết mới — đọc code `GradProject/server/core_ai/`, read-only)*

## 3.4. Thiết kế Pipeline Streaming STT–MT–TTS thời gian thực

### 3.4.1. Cơ chế phân đoạn câu thoại bằng Silero VAD

Luồng âm thanh PCM 16 kHz truyền từ client tới server dưới dạng khối 200 ms. Mỗi khối sau chuẩn hóa biên độ được đưa vào Silero VAD để ước lượng xác suất chứa tiếng nói; vượt ngưỡng kích hoạt thì coi là tiếng nói và bổ sung vào bộ đệm câu hiện tại, ngược lại tăng bộ đếm thời gian im lặng. Thay vì cắt câu ngay khi có khoảng lặng đầu tiên, hệ thống dùng cơ chế phát hiện điểm kết thúc động theo ngưỡng im lặng liên tục; qua thực nghiệm chọn **450 ms** để cân bằng tốc độ phản hồi và tính toàn vẹn câu. Khi đạt ngưỡng, hệ thống đóng bộ đệm và kích hoạt nhận dạng chính thức (`stt.final`).

Cơ chế **Hangover Frame**: khi phát hiện điểm kết thúc, giữ thêm hai khung âm thanh (~400 ms) trước khi chuyển sang STT, để bảo toàn các phụ âm cuối năng lượng thấp (/s/, /t/, /z/) dễ bị VAD nhận nhầm thành khoảng lặng. ✅

### 3.4.2. Quy trình nhận dạng và duy trì ngữ cảnh hội thoại

Phân đoạn câu hoàn chỉnh được chuyển tới STTEngine: PhoWhisper-medium-ct2 cho tiếng Việt, Faster-Whisper cho tiếng Anh. Tín hiệu → Log-Mel Spectrogram → Encoder–Decoder của Whisper. Sau mỗi `stt.final`, bộ đệm âm thanh được giải phóng để tránh tích lũy độ trễ, nhưng mất ngữ cảnh câu trước. Khắc phục bằng **Context Sliding Buffer**: lưu văn bản đầu ra vào bộ nhớ ngữ cảnh phiên, trích phần gần nhất cấp cho mô hình qua `initial_prompt` ở câu kế tiếp — giúp nhất quán thuật ngữ, tên riêng, từ viết tắt. Tham số `condition_on_previous_text` đặt `False` để tránh lặp từ/sinh văn bản ngoài ý muốn. ✅

### 3.4.3. Trực quan hóa kết quả nhận dạng thời gian thực

Kết quả truyền ngược về client qua WebSocket dưới hai dạng: interim (cập nhật liên tục nội dung đang nói) và final (kèm `segment_id` để khóa nội dung, chuyển sang dịch máy). ✅

### 3.4.4. Cơ chế đệm dịch ngữ cảnh ngắn (Short-MT Buffering)

Trước khi kích hoạt NLLB-200, hệ thống đánh giá độ dài văn bản đầu vào theo số từ. Nếu nhỏ hơn ngưỡng, lưu vào pending buffer; nếu đạt/vượt ngưỡng, ghép với nội dung đang đệm thành câu hoàn chỉnh hơn rồi mới gửi NLLB-200. Kết quả đóng gói thành `mt.result` chuyển tới TTS. Cơ chế giúp dịch khai thác nhiều ngữ cảnh, tăng độ chính xác ngữ nghĩa và tự nhiên hơn. ✅

### 3.4.5. Cơ chế Watchdog và giải phóng bộ đệm dịch

Watchdog Timer chạy song song luồng WebSocket, theo dõi trạng thái bộ đệm dịch và thời gian từ gói âm thanh cuối. Khi bộ đệm còn dữ liệu chờ và im lặng vượt ngưỡng, kích hoạt **Force Flush**: gửi toàn bộ phần còn lại tới NLLB-200 không cần thỏa điều kiện độ dài tối thiểu, rồi chuyển ngay sang TTS. Watchdog đóng vai trò bảo vệ độ trễ, cân bằng với bộ đệm ngữ cảnh (vốn ưu tiên chất lượng). ✅

### 3.4.6. Chia tách câu đa tầng (SBD) và Comma Fallback Splitter

❌ *(viết mới — đọc code streaming)*

### 3.4.7. Telemetry pipeline.metric và rollup segment_id

❌ *(viết mới — đọc code)*

## 3.5. Quy trình Fine-tuning mô hình Piper TTS giọng Nam Việt

### 3.5.1. Chiến lược Cross-Gender Fine-tuning trên kiến trúc VITS

Thay vì huấn luyện từ đầu, đồ án áp dụng **Cross-Gender Fine-tuning** để tận dụng tri thức ngôn ngữ của mô hình nền tiếng Việt. Mô hình khởi tạo: `vi_VN-vais1000-medium` (Piper/VITS, giọng nữ, huấn luyện trên tập tiếng Việt lớn). Dù khác biệt âm học giọng nữ–nam, các thành phần xử lý ngôn ngữ (biểu diễn âm vị, quy tắc phát âm, ngữ điệu, thanh điệu) đã được học đầy đủ, nên dùng làm điểm khởi đầu giúp rút ngắn hội tụ và giữ chất lượng phát âm ngay từ đầu.

Toàn bộ trọng số mô hình nền làm tham số khởi tạo, tiếp tục huấn luyện trên tập giọng nam miền Nam đã tiền xử lý. Về âm học, fine-tuning dịch chuyển không gian biểu diễn từ miền giọng nữ sang nam: F0, cấu trúc formant, phổ cộng hưởng, âm sắc được cập nhật. VITS dùng huấn luyện đối kháng (Adversarial Training) kết hợp Mel-Spectrogram Reconstruction Loss, Monotonic Alignment Loss... Discriminator liên tục đánh giá để Generator tạo tín hiệu ngày càng gần dữ liệu thực. ✅

### 3.5.2. Giải pháp 2-Pass Phoneme Mapping (xử lý tương thích âm vị)

G2P của Piper dựa trên eSpeak-NG. Dữ liệu huấn luyện mới có thể xuất hiện âm vị chưa có trong mô hình gốc (do từ tiếng Anh, tên riêng nước ngoài, từ mượn), gây không tương thích chỉ số âm vị ở Embedding Layer → lỗi khi nạp trọng số. Giải pháp **Two-Pass Phoneme Mapping**: Pass 1 tiền xử lý toàn bộ dữ liệu để thu thập đầy đủ tập âm vị, đối chiếu với tập âm vị mô hình nền để phát hiện ký hiệu mới/sai lệch ánh xạ; xây lại bảng ánh xạ âm vị thống nhất. Pass 2 tiền xử lý lại toàn bộ dữ liệu bằng bảng đã đồng bộ → mọi chỉ số âm vị tương thích không gian nhúng của mô hình gốc, fine-tuning ổn định mà vẫn kế thừa trọng số. ✅

### 3.5.3. Tinh chỉnh siêu tham số huấn luyện

Siêu tham số mặc định của Piper chưa phù hợp fine-tuning trên tập nhỏ (loss dao động mạnh giai đoạn đầu). Đồ án điều chỉnh Learning Rate (1e-4) và tham số tối ưu để giảm dao động gradient, ổn định huấn luyện, hạn chế phân kỳ. ✅

---

# CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ

> Nguồn: docx "CHƯƠNG 3" (phần dữ liệu/đánh giá/kết quả) + "CHƯƠNG 4" (rỗng).

## 4.1. Môi trường thực nghiệm và Kịch bản thử nghiệm

- 4.1.1. Phần cứng huấn luyện: Google Colab Pro GPU **NVIDIA Tesla T4 16GB**; chạy local: WSL2 Ubuntu, Windows. ✅
- 4.1.2. Đóng gói môi trường ảo (Virtual Environment Snapshotting) khôi phục venv Colab trong ~30 giây. ⚠️ *(đối chiếu `piper_vi_vais1000_finetuning/colab/`)*
- 4.1.3. Tập dữ liệu VieNeu-TTS-140h giọng nam và bộ **25 câu test chuẩn** đánh giá. ✅

## 4.2. Quy trình xử lý dữ liệu thực nghiệm và Kiểm soát chất lượng (Audio QC)

### 4.2.1. Khảo sát và lựa chọn dữ liệu

Nguồn: tập tiếng nói tiếng Việt công khai **VieNeu-TTS-140h**, tổng 73.882 đoạn đã phân đoạn, trong đó 49.553 clips giọng nam (~94,09 giờ) và 24.329 clips giọng nữ. Dữ liệu giọng nam phân bố theo nhiều Person (nguồn thu âm độc lập).

[[HÌNH: vieneu_xephang_person_nam.png | Biểu đồ xếp hạng tổng thời lượng theo từng Person nam trong VieNeu]]

Phân tích cấp Speaker để tìm giọng nam miền Nam chất lượng ổn định, thời lượng đủ lớn.

[[HÌNH: vieneu_xephang_speaker_nam.png | Biểu đồ xếp hạng các Speaker nam đơn lẻ có thời lượng lớn nhất]]

Ba speaker `jellyfish1010_0004`, `jellyfish1010_0013`, `jellyfish1010_0032` có thời lượng lớn nhất và chất giọng tương đối đồng nhất. Do từng speaker đều < mức khuyến nghị 2–3 giờ cho fine-tuning Piper VITS Medium, đồ án gộp dữ liệu cả ba. Sau loại đoạn quá ngắn/dài và lấy mẫu theo tỷ lệ, tập thô gồm **1.999 clips (~3,65 giờ)**.

[[HÌNH: vieneu_phanbo_thoiluong_1999.png | Biểu đồ phân bố thời lượng tập 1999 clips gộp giọng nam]]

Phần lớn đoạn nằm trong 1,5–8 giây, trung bình ~3,65 giây. ✅

### 4.2.2. Tiền xử lý âm thanh

Chuẩn hóa WAV về 22.050 Hz, mono PCM 16-bit (Librosa); chuẩn hóa âm lượng về **-23 LUFS** (EBU R128, Pyloudnorm); cắt khoảng lặng đầu/cuối bằng `librosa.effects.trim` ngưỡng 30 dB. ✅

### 4.2.3. Kiểm soát chất lượng bằng nhận dạng ngược + Per-Speaker Hybrid Filter

Phát hiện lệch nhãn văn bản (lỗi phân đoạn của bộ gốc) bằng quy trình QC dựa trên **PhoWhisper-large**: nhận dạng lại mỗi đoạn → văn bản giả thuyết, chuẩn hóa rồi so với tham chiếu bằng **WER**. Chia ba mức: Keep (giữ), Warn (sai lệch nhỏ — thường do chữ số/từ tiếng Anh), Drop (loại). Lỗi căn chỉnh tập trung ở `jellyfish1010_0004`; áp dụng **Per-Speaker Hybrid Filter**: speaker chất lượng thấp chỉ giữ lớp Keep, speaker chất lượng cao giữ cả Warn. Sau lọc còn **~1.500 clips (~2,5 giờ)** sạch, định dạng LJSpeech. ✅

### 4.2.4. Chuẩn hóa văn bản cho huấn luyện TTS

Chuẩn hóa bằng **Vinorm**: chuyển chữ số, ngày tháng, ký hiệu, từ viết tắt sang dạng phát âm đầy đủ (ví dụ "2026" → "hai nghìn không trăm hai mươi sáu"). Vá lỗi tương thích Vinorm với Python 3.12 (module `imp` bị loại bỏ) bằng lớp tương thích dựa trên `importlib` + monkey-patch. ✅

## 4.3. Chỉ số và Phương pháp đánh giá thực nghiệm

### 4.3.1. Các chỉ số khách quan

Ba chỉ số: Real-Time Factor (RTF), Word Error Rate (WER), Mel Reconstruction Loss.

[[BẢNG: | Tổng hợp ba chỉ số khách quan (Chỉ số / Mục đích đánh giá / Ý nghĩa)]]

| Chỉ số | Mục đích đánh giá | Ý nghĩa |
|---|---|---|
| RTF | Tốc độ suy luận | Thời gian suy luận / thời lượng âm thanh; <1,0 đạt thời gian thực |
| WER | Độ chính xác phát âm (hồi chuyển) | Tỷ lệ lỗi từ khi nhận dạng ngược bằng PhoWhisper-large |
| Mel Recon. Loss | Hội tụ huấn luyện | Chọn checkpoint tối ưu |

RTF đo trên client (so thời gian suy luận với thời lượng âm thanh tạo ra); WER tính qua hồi chuyển (PhoWhisper-large nhận dạng lại âm thanh tổng hợp, đối chiếu văn bản gốc); Mel Loss theo dõi hội tụ. ✅

### 4.3.2. Đánh giá độ trễ hệ thống

[[BẢNG: | Các thành phần đo đạc độ trễ và nội dung đo (telemetry pipeline.metric)]] ⚠️ *(số liệu cần bổ sung từ telemetry)*

### 4.3.3. Đánh giá chất lượng giọng nói

[[BẢNG: | Phương pháp đánh giá chất lượng giọng nói (khách quan / chủ quan)]]

Khách quan: **NISQA-TTS** dự đoán điểm MOS thang 1–5 trên toàn tập thử nghiệm. Chủ quan: nhóm người nghe bản địa chấm theo Naturalness, Intelligibility, Expressiveness; đối chiếu với NISQA MOS. ✅

## 4.4. Kết quả thực nghiệm Client App (PySide6) `[⚠️ Bug đang fix]`

- 4.4.1. Kiểm thử giao thức WebSocket và hiển thị transcript interim/final. ❌ `[⚠️ Bug đang fix]`
- 4.4.2. Tính ổn định, giảm giật cục luồng phát AdaptiveJitterPlayer. ❌ `[⚠️ Bug đang fix]`
- 4.4.3. Đánh giá cô lập âm thanh loopback chống vọng tiếng khi họp song hướng thực tế. ❌ `[⚠️ Bug đang fix]`

## 4.5. Kết quả thực nghiệm và huấn luyện mô hình Piper TTS `[🔄 đang train — số liệu có thể cập nhật]`

### 4.5.1. Đường cong hội tụ Mel Loss và KL Loss

Fine-tuning từ checkpoint `vi_VN-vais1000-medium` trên Colab GPU T4, lưu checkpoint mỗi 10 epochs, tổng **84 checkpoint** đánh giá trên validation.

[[HÌNH: piper_mel_kl_loss.png | Đường cong hội tụ Mel Loss và KL Loss của mô hình Piper TTS]]

Mel Reconstruction Loss giảm nhanh giai đoạn đầu: ~500 epochs đầu giảm từ ~36,5 xuống gần 33,0; sau đó chậm dần và hội tụ ổn định. Checkpoint **e5219** đạt Mel Loss trung bình thấp nhất **32,977** (tốt nhất). Từ ~epoch 5300 hình thành vùng hội tụ (loss plateau); tại **e5599** Mel Loss = 33,833. KL Divergence Loss giảm dần và ổn định cuối kỳ, không phân kỳ. LR 1e-4 + huấn luyện đối kháng VITS giữ ổn định, hạn chế quá khớp. ✅ 🔄

### 4.5.2. Lượng tử hóa FP32 → FP16 và phân tích đặc trưng âm học

Xuất checkpoint tốt nhất sang ONNX, lượng tử hóa FP32→FP16: dung lượng giảm từ **63,5 MB → 32,1 MB** (~49,4%). RTF trung bình trên AMD Ryzen 5 = **0,120** (suy luận nhanh ~8,3× thời gian phát, << ngưỡng 1,0).

[[HÌNH: melspec_baseline_vs_male.png | So sánh phổ Mel-Spectrogram giữa mô hình nền (nữ) và mô hình giọng nam sau fine-tuning]]

Phổ giọng nam dịch năng lượng xuống dải tần thấp, cấu trúc hài âm rõ và liên tục hơn. Spectral Centroid giảm 1614→1360 Hz (−15,7%); rolloff 85% giảm 3147→2620 Hz (−16,8%); ZCR giảm 0,0727→0,0541 (−25,6%) — xác nhận học được đặc trưng giọng nam miền Nam. ✅ 🔄

### 4.5.3. Đối sánh NISQA MOS, Human MOS và WER

So sánh 3 mô hình (baseline giọng nữ, e5219, e5599) trên 25 câu test chuẩn.

[[HÌNH: nisqa_mos_boxplot.png | Biểu đồ hộp phân bố điểm NISQA MOS của ba mô hình]]
[[HÌNH: wer_boxplot.png | Biểu đồ hộp phân bố chỉ số WER của ba mô hình]]
[[BẢNG: | Kết quả đánh giá chất lượng và hiệu năng của các mô hình]]

NISQA MOS: e5219 = **3,379** (+8,7% so baseline 3,109), e5599 = 3,366 (+8,3%). Độ lệch chuẩn MOS giảm: 0,685 (nền) → 0,472 (e5219) → 0,400 (e5599) — ổn định hơn. RTF cả ba <0,13, e5219 thấp nhất (0,1198). Đánh đổi: WER tăng — baseline 0,119 → e5219 0,311 → e5599 0,329 (do dữ liệu nhỏ, một số phụ âm đầu/cuối phát âm chưa ổn định). Tuy nhiên câu trung bình/dài (phổ biến trong họp) vẫn giữ WER thấp.

[[HÌNH: radar_3models.png | Biểu đồ Radar tổng hợp các chỉ số đánh giá của ba mô hình]]

**e5219** cân bằng nhất (MOS cao nhất, Mel Loss thấp nhất, RTF tốt nhất) → chọn làm mô hình cuối triển khai. ✅ 🔄

## 4.6. Phân tích so sánh Độ trễ tích lũy chặng S2S (End-to-End Latency)

- 4.6.1. Đối sánh độ trễ nạp model động lúc suy luận vs warmup preload lúc startup.
- 4.6.2. Đối sánh độ trễ tổng S2S dùng Piper FP32 vs FP16.
- 4.6.3. Ảnh hưởng của Silero VAD-chunking và Comma Fallback Splitter lên TTFA.

⚠️ *(một phần có ở bảng đo độ trễ; cần tổng hợp số liệu E2E đầy đủ)*

---

# CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

> Nguồn: docx "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN" (mở rộng theo 5.1–5.3).

## 5.1. Những đóng góp chính

Đồ án đã thiết kế và triển khai hệ thống dịch giọng nói song hướng thời gian thực Anh–Việt theo kiến trúc Client–Server, tích hợp STT, MT, TTS, hỗ trợ dịch hội thoại trực tuyến độ trễ thấp, chất lượng ổn định. Các giải pháp tối ưu đã giảm đáng kể thời gian phản hồi và loại bỏ phản hồi âm thanh trong họp trực tuyến. Đồng thời xây dựng và tinh chỉnh thành công mô hình **Piper TTS giọng nam miền Nam Việt** nhỏ gọn, chất lượng tốt, chạy thời gian thực trên CPU phổ thông. ✅
- 5.1.1. Pipeline S2ST song hướng thời gian thực độ trễ tối ưu.
- 5.1.2. Mô hình Piper TTS giọng nam Việt đóng góp cho cộng đồng nghiên cứu.

## 5.2. Các hạn chế hiện tại

- 5.2.1. Phụ thuộc GPU đám mây (Google Colab T4) cho luồng server.
- 5.2.2. Vấn đề **stuck outbound queue** khi client ngắt kết nối đột ngột không qua handshake (cấu trúc push-driven queue). ✅

## 5.3. Kiến nghị và Hướng phát triển

- 5.3.1. Lượng tử hóa sâu INT8/INT4 chạy trực tiếp trên CPU client; giảm phụ thuộc đám mây.
- 5.3.2. Giao thức ping/keep-alive hoặc VAD-dummy chunk tự giải phóng hàng đợi triệt để.
- 5.3.3. Nghiên cứu kiến trúc dịch giọng nói đầu-cuối (End-to-End S2ST) giảm độ trễ, bảo toàn ngữ điệu/cảm xúc; mở rộng đa ngôn ngữ (EN-VI-JA-KO). ✅

---

# DANH MỤC TÀI LIỆU THAM KHẢO

❌ *(XÓA placeholder rác nông nghiệp/kinh tế trong docx. Thu thập & trích dẫn chuẩn APA 7th: Whisper, PhoWhisper, NLLB-200, VITS, Piper/Rhasspy, Silero VAD, CTranslate2, NISQA, VieNeu-TTS...)*

# PHỤ LỤC

❌ *(Mã nguồn core_ai, kịch bản lọc dataset hybrid, file cấu hình warmup — theo outline.)*

<!-- TƯ LIỆU GỐC GIỮ LẠI: định nghĩa PlantUML 2 sơ đồ kiến trúc (chế độ 2 chiều & 1 chiều) đã có trong docx cũ, dùng để render ảnh cho mục 3.1.1. -->

