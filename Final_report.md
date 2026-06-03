# BÁO CÁO ĐỒ ÁN TỐT NGHIỆP KỸ SƯ AI
## ĐỀ TÀI: HỆ THỐNG DỊCH GIỌNG NÓI THỜI GIAN THỰC SONG HƯỚNG ANH - VIỆT (S2ST) TỐI ƯU HÓA ĐỘ TRỄ VÀ CHẤT LƯỢNG GIỌNG NÓI TỔNG HỢP

---

## TRANG THỦ TỤC & DẪN NHẬP

### TRANG TIÊU ĐỀ (Title Page)
*(Nội dung trang tiêu đề theo mẫu của trường)*

### TRANG NỘI DUNG (Content Page)
*(Mục lục tự động sinh ra)*

### LỜI CẢM ƠN (Acknowledgements)
*(Lời cảm ơn từ tác giả)*

### DANH MỤC CÁC CHỮ VIẾT TẮT (Acronym List)
*(Bảng danh mục viết tắt)*

### DANH MỤC BẢNG (List of Tables)
*(Danh mục các bảng biểu sử dụng trong báo cáo)*

### DANH MỤC HÌNH VẼ - ĐỒ THỊ (List of Figures)
*(Danh mục các hình vẽ, đồ thị và sơ đồ)*

### LỜI MỞ ĐẦU / TÓM TẮT ĐỒ ÁN (Executive Summary)
*(Tóm tắt nội dung chính, lý do, phương pháp và kết quả đạt được)*

---

## CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

### 1.1. Lý do chọn đề tài (Motivation)
#### 1.1.1. Nhu cầu dịch thuật trực tuyến đa ngôn ngữ trong kỷ nguyên toàn cầu hóa
#### 1.1.2. Thách thức về độ trễ tích lũy và chất lượng âm phổ tự nhiên của giọng nói tiếng Việt
#### 1.1.3. Ý nghĩa thực tiễn của giải pháp dịch giọng nói thời gian thực song hướng (Anh - Việt)

### 1.2. Phát biểu bài toán (Problem Statement)
#### 1.2.1. Bài toán nhận dạng tiếng nói (STT) dạng streaming trên luồng âm thanh liên tục không mất ngữ cảnh
#### 1.2.2. Bài toán dịch máy hội thoại đa ngữ (NMT) bảo toàn tính tự nhiên và ngữ nghĩa của vế nói ngắn
#### 1.2.3. Bài toán thiếu hụt mô hình tổng hợp giọng nói (TTS) giọng nam Việt chất lượng cao, dung lượng nhẹ phục vụ thời gian thực
#### 1.2.4. Bài toán cô lập luồng âm thanh thu/phát hệ thống chống vòng lặp phản hồi âm thanh (feedback loop)

### 1.3. Mục tiêu và Đóng góp của đề tài
#### 1.3.1. Thiết lập hệ thống S2ST thời gian thực song hướng tối ưu hóa độ trễ cumulative
#### 1.3.2. Nghiên cứu phương pháp Cross-Gender Fine-tuning Piper TTS tạo giọng nam miền Nam Việt chất lượng từ dataset giới hạn
#### 1.3.3. Xây dựng giải pháp định tuyến âm thanh ảo cô lập loopback chống lặp tiếng không cần can thiệp Admin hệ thống

### 1.4. Đối tượng và Phạm vi nghiên cứu
#### 1.4.1. Đối tượng công nghệ cốt lõi: VITS, espeak-ng, Faster-Whisper, PhoWhisper, NLLB-200, Silero VAD
#### 1.4.2. Phạm vi triển khai thực nghiệm: FastAPI Server trên Google Colab GPU T4 và Client PySide6 trên hệ điều hành Windows

### 1.5. Bố cục của Báo cáo Đồ án tốt nghiệp
#### 1.5.1. Tóm tắt nội dung chính từ Chương 1 đến Chương 5
#### 1.5.2. Sơ đồ liên kết logic học thuật giữa các chương

---

## CHƯƠNG 2. TỔNG QUAN TÀI LIỆU VÀ CƠ SỞ LÝ THUYẾT

### 2.1. Cơ sở lý thuyết về Nhận dạng tiếng nói (STT)
#### 2.1.1. Nguyên lý hoạt động của kiến trúc Self-Attention và Transformer trong xử lý tiếng nói
#### 2.1.2. Cơ chế nhận dạng tiếng nói dạng Transformer của mô hình OpenAI Whisper và Faster-Whisper
#### 2.1.3. Kiến trúc mô hình PhoWhisper được tinh chỉnh chuyên biệt cho ngôn ngữ tiếng Việt

### 2.2. Cơ sở lý thuyết về Dịch máy thần kinh (NMT)
#### 2.2.1. Tổng quan cấu trúc dịch máy đa ngôn ngữ NLLB-200 (No Language Left Behind)
#### 2.2.2. Kỹ thuật lượng tử hóa và tối ưu hóa tốc độ suy luận ctranslate2 (CTranslate2)

### 2.3. Cơ sở lý thuyết về Tổng hợp tiếng nói (TTS) dựa trên kiến trúc VITS
#### 2.3.1. Phân tích sâu kiến trúc VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech)
#### 2.3.2. Vai trò toán học của Posterior Encoder (Mel-spectrogram sang latent z) và Prior Encoder (Text sang latent)
#### 2.3.3. Cơ chế biến đổi phân bố đơn giản sang spectrogram phức tạp thông qua hệ thống Normalizing Flows
#### 2.3.4. Mô hình tổng hợp sóng âm trực tiếp HiFi-GAN Decoder và cơ chế đánh giá qua đối nghịch (Discriminators: MPD, MSD)
#### 2.3.5. Kiến trúc Piper TTS và cơ chế mã hóa âm vị (Phonemize) espeak-ng cho tiếng Việt

### 2.4. Phân đoạn hoạt động giọng nói bằng mô hình Silero VAD
#### 2.4.1. Thuật toán phân lớp Tín hiệu giọng nói (Speech) và Khoảng lặng (Silence) bằng mạng thần kinh nhân tạo nhẹ
#### 2.4.2. Vai trò của Silero VAD trong việc chia đoạn tín hiệu đầu vào cho pipeline dịch streaming

### 2.5. Các nghiên cứu liên quan & Khoảng trống nghiên cứu (Related Work & Research Gaps)
#### 2.5.1. Đánh giá các giải pháp dịch thuật Speech-to-Speech hiện có trên thế giới (ưu nhược điểm và chi phí)
#### 2.5.2. Hiện trạng các mô hình Piper tiếng Việt trên cộng đồng Rhasspy (sự thiếu hụt trầm trọng mô hình giọng nam Việt chất lượng)
#### 2.5.3. Khoảng trống nghiên cứu về tối ưu độ trễ cumulative chặng S2S cho tài nguyên tính toán GPU/VRAM giới hạn

---

## CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT

### 3.1. Thiết kế Kiến trúc Hệ thống Tổng quát (S2ST Client-Server)
#### 3.1.1. Sơ đồ khối kiến trúc kết nối song công thời gian thực qua giao thức WebSocket
#### 3.1.2. Thiết kế định dạng khung truyền tải nhị phân (Binary Pipeline Frame) định tuyến route và khung điều khiển JSON (Control Frame)
#### 3.1.3. Cấu trúc Session State và cơ chế định tuyến bất đồng bộ Mode-Dispatch trên Server FastAPI

### 3.2. Thiết kế Client App (PySide6) và Giải pháp Cô lập Loopback
#### 3.2.1. Cơ chế bất đồng bộ tích hợp ứng dụng PySide6 với vòng lặp sự kiện `qasync` trên môi trường Windows
#### 3.2.2. Giải pháp định tuyến âm thanh hai tuyến Route 0 (Local Default Speaker) và Route 1 (VB-CABLE Input)
#### 3.2.3. Thuật toán tự động nhận diện và ánh xạ thiết bị âm thanh ảo VB-Audio Virtual Cable không cần quyền Administrator
#### 3.2.4. Cơ chế thu âm loopback WASAPI cô lập âm phản hồi (Acoustic Echo & Feedback Loop Mitigation)

### 3.3. Thiết kế Server App (FastAPI) phân tầng Hướng Engine (Plug-and-play)
#### 3.3.1. Polymorphic Facade Pattern: Đồng bộ hóa 85% kiến trúc giao tiếp 3 AI Engine (STT, MT, TTS)
#### 3.3.2. Kiến trúc song song hóa Execution Lane (Worker pools và operation locks) ngăn ngừa race condition trên GPU VRAM
#### 3.3.3. Giải thuật Preload & Warmup triệt tiêu hoàn toàn độ trễ khởi động lạnh (Cold-start latency) lúc startup

### 3.4. Thiết kế Pipeline Streaming STT-MT-TTS tối ưu hóa thời gian thực
#### 3.4.1. Cơ chế cắt câu động Silero VAD tích hợp hangover frame bảo toàn phụ âm cuối cho bộ nhận dạng Whisper
#### 3.4.2. Giải thuật đệm dịch ngắn (Short-MT buffering) nâng cao ngữ điệu và Watchdog tự động flush sau 3 giây im lặng
#### 3.4.3. Quy trình chia tách câu đa tầng (SBD) và Comma Fallback Splitter cho suy luận TTS cuốn chiếu liên tục
#### 3.4.4. Cơ chế đo đạc hiệu năng chặng mạng bằng telemetry pipeline.metric và giải pháp rollup segment_id đầu cuối

### 3.5. Quy trình thực nghiệm huấn luyện mô hình Piper TTS giọng Nam Việt
#### 3.5.1. Phương pháp Cross-Gender Fine-tuning kế thừa không gian nhúng âm vị từ base checkpoint `vais1000-medium`
#### 3.5.2. Giải pháp tiền xử lý và đồng bộ âm vị 2-Pass Workaround loại bỏ ký tự lạ espeak-ng tránh lỗi IndexError VITS
#### 3.5.3. Kỹ thuật vá mã nguồn (Regex Inline Patching) tối ưu hóa Tốc độ học (Learning Rate = 1e-4) trong PyTorch Lightning

---

## CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ

### 4.1. Môi trường thực nghiệm và Kịch bản thử nghiệm
#### 4.1.1. Cấu hình phần cứng huấn luyện (Colab Pro GPU T4 16GB) và chạy local (WSL2 Ubuntu, Windows 10)
#### 4.1.2. Giải pháp đóng gói môi trường bất đồng bộ (Virtual Environment Snapshotting) khôi phục venv trong 30 giây
#### 4.1.3. Mô tả tập dữ liệu VieNeu-TTS-140h giọng Nam Việt và bộ 25 câu test chuẩn đánh giá chủ quan

### 4.2. Quy trình xử lý dữ liệu thực nghiệm và Kiểm soát chất lượng (Audio QC)
#### 4.2.1. Phân tích bimodal WER của PhoWhisper-large trên 1999 clips VieNeu để phát hiện mismatch văn bản gốc
#### 4.2.2. Cơ chế lọc lai per-speaker hybrid lọc sạch tập dữ liệu còn 1500 clips (~2.5h) chuẩn định dạng LJSpeech
#### 4.2.3. Chuẩn hóa chữ số, ngày tháng bằng vinorm và bản vá lỗi thư viện imp trên môi trường Python 3.12+

### 4.3. Chỉ số và Phương pháp đánh giá thực nghiệm
#### 4.3.1. Các chỉ số đo đạc khách quan (Objective Metrics): Mel reconstruction loss, WER, real-time factor (RTF)
#### 4.3.2. Đo đạc độ trễ từng stage và End-to-End Latency thông qua telemetry pipeline.metric
#### 4.3.3. Phương pháp đánh giá chất lượng giọng nói: Chấm điểm NISQA MOS (khách quan) và khảo sát Human MOS (chủ quan)

### 4.4. Kết quả thực nghiệm hệ thống máy khách Client App (PySide6)
*(Nội dung phần kiểm thử kết nối WebSocket, đồ họa văn bản dịch interim/final, AdaptiveJitterPlayer, cô lập loopback)*

### 4.5. Kết quả thực nghiệm và huấn luyện mô hình Piper TTS
*(Phân tích đường cong hội tụ Mel/KL loss, hiệu năng phần cứng gpu_log.csv, lượng tử hóa FP16, so sánh phổ âm và điểm NISQA MOS)*

### 4.6. Phân tích so sánh Độ trễ tích lũy chặng S2S (End-to-End Latency Comparison)
#### 4.6.1. Đối sánh độ trễ chặng khi nạp dynamic mô hình tại thời điểm suy luận vs cơ chế warmup preload tại startup
#### 4.6.2. Đối sánh độ trễ tổng cộng của luồng S2S sử dụng Piper FP32 vs Piper quantized FP16
#### 4.6.3. Đánh giá ảnh hưởng của cơ chế Silero VAD-chunking và Comma Fallback Splitter lên tổng trễ nhận thức (TTFA)

---

## CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 5.1. Những đóng góp khoa học chính của Đồ án tốt nghiệp
#### 5.1.1. Pipeline dịch thuật Speech-to-Speech song hướng thời gian thực độ trễ tối ưu
#### 5.1.2. Mô hình Piper TTS giọng nam miền Nam Việt tự nhiên, cực nhẹ đóng góp cho cộng đồng nghiên cứu Việt Nam

### 5.2. Các hạn chế kỹ thuật hiện tại của hệ thống
#### 5.2.1. Sự phụ thuộc vào GPU đám mây (Google Colab T4) để chạy luồng server
#### 5.2.2. Vấn đề stuck outbound queue khi client ngắt kết nối đột ngột mà không qua handshake

### 5.3. Kiến nghị và Hướng phát triển tương lai
#### 5.3.1. Nghiên cứu lượng tử hóa sâu mức INT8/INT4 chạy trực tiếp trên CPU thiết bị đầu cuối của client
#### 5.3.2. Thiết kế giao thức giữ kết nối (ping/keep-alive) hoặc VAD-dummy chunk tự giải phóng hàng đợi triệt để
#### 5.3.3. Mở rộng tích hợp mô hình End-to-End dạng nén nhẹ, hướng tới giảm thiểu tối đa kiến trúc 3 tầng phân rã

---

## TÀI LIỆU VÀ PHỤ LỤC THAM KHẢO

### DANH MỤC TÀI LIỆU THAM KHẢO (Reference List)
*(Danh mục theo chuẩn APA 7th Edition)*

### PHỤ LỤC (Appendices)
*(Mã nguồn core_ai, kịch bản lọc dataset hybrid, file cấu hình warmup)*

### TÓM TẮT BÁO CÁO DẠNG BÀI BÁO KHOA HỌC THEO MẪU IEEE (IEEE Paper Summary)
*(Bài báo IEEE tóm tắt tối đa 10 trang)*
