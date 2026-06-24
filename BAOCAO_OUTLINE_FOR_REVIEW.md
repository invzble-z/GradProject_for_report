# ĐỀ CƯƠNG CHI TIẾT VÀ TÓM TẮT NỘI DUNG BÁO CÁO ĐỒ ÁN TỐT NGHIỆP
## PHỤC VỤ CÔNG TÁC RÀ SOÁT VÀ ĐÁNH GIÁ (REVIEW OUTLINE)

**Tên đề tài:** NGHIÊN CỨU VÀ PHÁT TRIỂN HỆ THỐNG DỊCH THUẬT GIỌNG NÓI THỜI GIAN THỰC ANH – VIỆT VỚI TỐI ƯU HÓA ĐỘ TRỄ SỬ DỤNG DEEP LEARNING  
**Giáo viên hướng dẫn:** ThS. Trần Uyên Trang  
**Định hướng đồ án:** Nghiên cứu và Phát triển hệ thống (R&D)  

---

## 📌 TRANG THỦ TỤC & DẪN NHẬP
*   **Tiêu đề & Thông tin thủ tục:** Cung cấp thông tin hành chính của đề tài bằng hai ngôn ngữ (Anh - Việt), thông tin sinh viên thực hiện, giáo viên hướng dẫn và các biểu mẫu theo chuẩn định dạng đồ án tốt nghiệp của trường VKU.
*   **Lời cảm ơn:** Bày tỏ lòng biết ơn sâu sắc tới các thầy cô giáo khoa Khoa học Máy tính, gia đình, bạn bè và đặc biệt là Giáo viên hướng dẫn đã đồng hành, hỗ trợ công cụ, tài nguyên và định hướng khoa học suốt quá trình thực hiện đồ án.
*   **Danh mục viết tắt:** Tổng hợp bảng định nghĩa 19 thuật ngữ chuyên ngành cốt lõi được sử dụng xuyên suốt trong báo cáo (ví dụ: *ASR, STT, NMT, TTS, VITS, VAD, MOS, WER, CER, RTF, WS, WASAPI*...).
*   **Danh mục bảng & hình vẽ:** Hệ thống tự động trích xuất danh sách các bảng biểu thực nghiệm và sơ đồ kiến trúc để người đọc dễ dàng định vị nhanh các minh chứng khoa học.

---

## 📘 CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI (5 - 7 trang)

### 1.1. Lý do chọn đề tài
*   **Nội dung chính:** Phân tích nhu cầu giao tiếp song ngữ Anh - Việt trong môi trường hội họp trực tuyến thời gian thực (Zoom, Google Meet) và chỉ ra các rào cản ngôn ngữ. 
*   **Khó khăn kỹ thuật:** Trình bày các hạn chế của giải pháp truyền thống (chi phí cao, không bảo mật) và các thách thức lớn của hệ thống dịch giọng nói tự động (Speech-to-Speech Translation - S2ST) hiện nay: độ trễ tích lũy (cumulative latency) qua 3 tầng xử lý, đặc thù tiếng Việt (thanh điệu, ngắt nghỉ dễ gây cắt câu sai), sự thiếu hụt nghiêm trọng của mô hình tổng hợp tiếng nói (TTS) giọng nam Việt chất lượng cao chạy thời gian thực trên CPU phổ thông, và hiện tượng phản hồi âm học (feedback loop) khi micro thu ngược lại âm thanh dịch từ loa.

### 1.2. Phát biểu bài toán
*   **Nội dung chính:** Xác lập và định nghĩa rõ ràng 4 bài toán kỹ thuật cốt lõi cần giải quyết trong đồ án:
    1.  **STT dạng streaming:** Nhận dạng tiếng nói trên luồng âm thanh liên tục theo thời gian thực và phải duy trì ngữ cảnh hội thoại liên tiếp để tránh mất ý nghĩa câu.
    2.  **Dịch máy hội thoại (NMT):** Dịch các câu thoại ngắn, rời rạc, chưa hoàn chỉnh ngữ pháp do người nói ngắt nhịp mà vẫn bảo toàn ngữ nghĩa và đạt độ trễ cực thấp.
    3.  **Thiếu hụt mô hình TTS giọng nam tiếng Việt:** Nghiên cứu phương pháp tối ưu huấn luyện mô hình tổng hợp giọng nam tự nhiên, dung lượng nhẹ hoạt động không cần GPU chuyên dụng.
    4.  **Chống vòng lặp phản hồi âm học:** Thiết kế cơ chế cô lập vật lý và định tuyến ảo dòng âm thanh thu/phát để triệt tiêu hiện tượng tự dịch tuần hoàn.

### 1.3. Mục tiêu và Đóng góp của đề tài
*   **Nội dung chính:** 
    *   **Mục tiêu:** Xây dựng thành công hệ thống S2ST song hướng thời gian thực Client-Server qua kết nối WebSocket; tối ưu hóa độ trễ; fine-tune mô hình giọng nam tiếng Việt tự nhiên; thiết kế giải pháp phần mềm cô lập âm thanh chống phản hồi; đánh giá định lượng chi tiết hệ thống.
    *   **Đóng góp thực tiễn:** (1) Một pipeline S2ST song hướng hoàn chỉnh tích hợp 3 tầng AI kết hợp công nghệ định tuyến ảo VoiceMeeter Banana chống vòng lặp tự dịch; (2) Mô hình Piper TTS giọng nam tiếng Việt (Run B1) đạt chất lượng vượt trội (WER ~4.1%, NISQA MOS 4.13), dung lượng nhẹ (~63.5 MB) chạy mượt trên CPU phổ thông; (3) Quy trình tự xây dựng, làm sạch và kiểm định dữ liệu giọng nói tự động bằng ba hệ ASR độc lập kết hợp hiệu đính bằng LLM Gemini 3.5 Flash.

### 1.4. Đối tượng và Phạm vi nghiên cứu
*   **Nội dung chính:** 
    *   **Đối tượng:** Các mô hình học sâu hiện đại (PhoWhisper, Faster-Whisper, NLLB-200, VITS/Piper TTS, Silero VAD), giao thức WebSocket song công, và các kỹ thuật xử lý âm thanh kỹ thuật số.
    *   **Phạm vi:** Giới hạn ở cặp ngôn ngữ Anh - Việt, hoạt động theo mô hình Client-Server (Server chạy GPU T4 đám mây, Client chạy ứng dụng PySide6 trên hệ điều hành Windows), thực nghiệm huấn luyện và thực thi trong điều kiện tài nguyên tính toán giới hạn.

### 1.5. Cách tiếp cận và Phương pháp nghiên cứu
*   **1.5.1. Cách tiếp cận:** Áp dụng kiến trúc phân tán Client-Server (đẩy toàn bộ STT-MT-TTS lên GPU Server để tối ưu hiệu năng và giữ ứng dụng Client nhẹ); xử lý bất đồng bộ kết hợp cơ chế preload/warmup loại bỏ độ trễ cold-start; chuyển giao học tập (cross-gender fine-tuning) để tối ưu hóa thời gian huấn luyện giọng nam từ tập dữ liệu hạn chế; cô lập âm thanh triệt để bằng định tuyến phần mềm (VoiceMeeter Banana) kết hợp đeo tai nghe ở phần cứng.
*   **1.5.2. Phương pháp nghiên cứu:** Nghiên cứu lý thuyết các kiến trúc mạng nơ-ron Transformer và bộ tự mã hóa biến phân đối kháng (VITS); xây dựng thực nghiệm hệ thống phần mềm thực tế; áp dụng phương pháp đánh giá định lượng bằng các chỉ số khoa học tiêu chuẩn (WER, CER, NISQA MOS, RTF, F0) kết hợp khảo sát định tính chủ quan từ người dùng thực tế.

### 1.6. Bố cục của Báo cáo
*   **Nội dung chính:** Tóm tắt ngắn gọn cấu trúc và nhiệm vụ nghiên cứu của từng chương trong 5 chương của báo cáo đồ án tốt nghiệp theo đúng quy định của Nhà trường.

---

## 📗 CHƯƠNG 2. TỔNG QUAN TÀI LIỆU VÀ CƠ SỞ LÝ THUYẾT (Tối đa 25 trang)

### 2.1. Cơ sở lý thuyết về Nhận dạng tiếng nói (STT)
*   **2.1.1. Bài toán nhận dạng tiếng nói streaming:** Phân tích sự khác biệt giữa STT trên file hoàn chỉnh và STT dạng streaming (chia nhỏ âm thanh truyền liên tục). Nêu rõ đặc điểm của kết quả tạm thời (Interim Result) và kết quả cuối cùng (Final Result), cùng thách thức lớn nhất là sự thiếu hụt ngữ cảnh khi suy luận cuốn chiếu trên các đoạn âm thanh ngắn.
*   **2.1.2. Mô hình Whisper và Faster-Whisper:** Giải thích sâu kiến trúc Encoder-Decoder dựa trên Transformer của mô hình Whisper (OpenAI) hoạt động trực tiếp từ Mel Spectrogram sang văn bản. Trình bày cấu hình tăng tốc suy luận của thư viện **Faster-Whisper** dựa trên CTranslate2 giúp giảm độ trễ vượt trội cho luồng tiếng Anh (sử dụng bản *small* đa ngữ với kiểu tính toán float16 trên GPU).
*   **2.1.3. Mô hình PhoWhisper cho tiếng Việt:** Giới thiệu mô hình PhoWhisper được tinh chỉnh chuyên biệt cho ngôn ngữ tiếng Việt để cải thiện độ chính xác đối với tên riêng, từ mượn và thuật ngữ chuyên ngành. Hệ thống tích hợp phiên bản chuyển đổi **PhoWhisper-medium-ct2** (CTranslate2) nhằm đảm bảo tốc độ suy luận thời gian thực.

### 2.2. Cơ sở lý thuyết về Dịch máy thần kinh (NMT)
*   **2.2.1. Tổng quan kiến trúc NLLB-200:** Trình bày kiến trúc mô hình dịch máy đa ngôn ngữ NLLB-200 (Meta) hỗ trợ dịch chất lượng cao giữa hơn 200 ngôn ngữ. Mô tả quy trình thu thập dữ liệu (LASER3, Mined Bitext) và các kỹ thuật huấn luyện tiên tiến (Mixture of Experts - MoE, Curriculum Learning). Nhấn mạnh khả năng dịch bảo toàn ngữ nghĩa của NLLB đối với các câu hội thoại tự phát, ngắn và thiếu ngữ pháp.
*   **2.2.2. Lượng tử hóa và tối ưu suy luận với CTranslate2:** Giải thích cơ chế toán học của kỹ thuật lượng tử hóa (Quantization) từ FP32 sang số nguyên INT8/INT16 và dấu phẩy động nửa độ chính xác FP16/BF16 nhằm giảm dung lượng mô hình, tiết kiệm băng thông và tăng tốc độ tính toán. Trình bày cấu hình thực tế trong hệ thống: mô hình **NLLB-200 distilled-600M** được lượng tử hóa ở mức **`int8`** trên GPU T4 thông qua thư viện CTranslate2 để đạt tốc độ tối đa.

### 2.3. Cơ sở lý thuyết về Tổng hợp tiếng nói (TTS) dựa trên kiến trúc VITS
*   **2.3.1. Phân tích kiến trúc VITS:** Giới thiệu sâu về VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech) - mô hình tổng hợp giọng nói đầu-cuối (End-to-End) mạnh mẽ. Giải thích cơ chế hoạt động của VITS dưới dạng một bộ tự mã hóa biến phân có điều kiện (CVAE) giúp chuyển đổi trực tiếp văn bản sang dạng sóng âm thanh (Raw Waveform) mà không cần qua tầng vocoder trung gian.
*   **2.3.2. Posterior Encoder và Prior Encoder:** Phân tích vai trò của bộ mã hóa hậu nghiệm (Posterior Encoder - WaveNet non-causal) trích xuất phân phối từ spectrogram thật trong lúc train, và bộ mã hóa tiên nghiệm (Prior Encoder - Text Transformer) trích xuất đặc trưng ngôn ngữ từ chuỗi âm vị. Hai bộ này được khớp không gian tiềm ẩn bằng cách tối thiểu hóa độ phân kỳ Kullback-Leibler (KL Divergence).
*   **2.3.3. Normalizing Flows:** Giải thích cơ chế toán học của luồng chuẩn hóa (Normalizing Flows) gồm các lớp ghép affine khả nghịch xếp chồng. Vai trò của thành phần này là biến đổi phân phối tiên nghiệm chuẩn đơn giản của văn bản thành phân phối phức tạp của spectrogram, giúp giọng nói tổng hợp đạt độ tự nhiên và biểu cảm cao.
*   **2.3.4. HiFi-GAN Decoder và các bộ phân biệt (MPD, MSD):** Trình bày cấu trúc bộ giải mã (Decoder) dựa trên bộ sinh của HiFi-GAN sử dụng các khối tích chập chuyển vị và Multi-Receptive Field Fusion (MRF). Mô tả cơ chế huấn luyện đối kháng (Adversarial) thông qua các bộ phân biệt đa chu kỳ (Multi-Period Discriminator - MPD) và đa tỷ lệ (Multi-Scale Discriminator - MSD) để kiểm soát chất lượng âm thanh tần số cao và cấu trúc sóng âm tổng thể.
*   **2.3.5. Kiến trúc Piper TTS và mã hóa âm vị espeak-ng cho tiếng Việt:** Giới thiệu Piper TTS - hệ thống tổng hợp giọng nói tối ưu hóa từ VITS, xuất ra định dạng ONNX giúp chạy cực nhanh trên CPU. Trình bày cơ chế chuyển văn bản thành âm vị (G2P) theo bảng phiên âm quốc tế IPA thông qua công cụ **eSpeak-NG** hỗ trợ tiếng Việt.

### 2.4. Phân đoạn hoạt động giọng nói bằng Silero VAD
*   **2.4.1. Thuật toán phân lớp tín hiệu giọng nói và khoảng lặng:** Trình bày nguyên lý hoạt động của Silero VAD - mô hình mạng nơ-ron tích chập (CNN) siêu nhẹ, tính toán xác suất có tiếng nói trong các khung âm thanh ngắn để phân biệt với khoảng lặng/nhiễu nền.
*   **2.4.2. Vai trò của Silero VAD trong pipeline dịch streaming:** Giải thích vai trò của Silero VAD như một bộ lọc tiền xử lý, thực hiện nhiệm vụ cắt câu động (segmentation) trên luồng âm thanh liên tục gửi từ client để loại bỏ khoảng lặng dư thừa, giảm tải cho tầng STT và cải thiện độ chính xác nhận dạng.

### 2.5. Các nghiên cứu liên quan & Khoảng trống nghiên cứu
*   **2.5.1. Các giải pháp dịch giọng nói hiện có:** Đánh giá các giải pháp S2ST hiện nay (dạng phân tầng cascaded và đầu-cuối end-to-end thương mại như Google, SeamlessM4T) và chỉ ra các hạn chế về chi phí, tính đóng của công nghệ và tính bảo mật thông tin cuộc họp.
*   **2.5.2. Hiện trạng mô hình tổng hợp giọng nói tiếng Việt trên Piper:** Nêu rõ thực trạng cộng đồng Piper TTS tiếng Việt hiện chỉ có duy nhất một mô hình giọng nữ công khai (`vi_VN-vais1000-medium`), hoàn toàn khuyết thiếu mô hình giọng nam Việt tự nhiên, nhẹ phục vụ dịch hội thoại song hướng.
*   **2.5.3. Khoảng trống nghiên cứu:** Xác định hai khoảng trống khoa học đồ án tập trung giải quyết: (1) Thiếu các nghiên cứu tối ưu độ trễ tích lũy cho hệ thống dịch song hướng theo luồng (streaming bidirectional) trên phần cứng hạn chế (GPU T4); (2) Thiếu mô hình Piper TTS giọng nam Việt chất lượng cao, chạy nhanh trên CPU máy khách phổ thông.

### 2.6. Các công nghệ và thư viện sử dụng
*   **Nội dung chính:** Tổng hợp chi tiết và phân loại vai trò của từng công nghệ trong hệ thống:
    *   *Ngôn ngữ:* Python (nền tảng chung cho Server và Client).
    *   *Server-side:* FastAPI (framework bất đồng bộ độ trễ thấp), WebSocket (truyền thông song công thời gian thực).
    *   *Client-side:* PySide6 (giao diện đồ họa), PyAudio (thu/phát âm thanh vật lý), SoundCard (WASAPI Loopback capture thu âm hệ thống không cần quyền admin), và **VoiceMeeter Banana** (trình trộn âm ảo đa bus: bus ảo B1 cho Google Meet/Zoom, Aux Input cho luồng cuộc họp, điều khiển tự động qua thư viện C `VoicemeeterRemote64.dll` để chống vòng lặp phản hồi âm học).
    *   *Thư viện AI:* PyTorch, CTranslate2, ONNX Runtime, Silero VAD, Demucs (khử nhiễu dữ liệu), Librosa & pyloudnorm (chuẩn hóa âm lượng -23 LUFS), vinorm & vietnormalizer (chuẩn hóa văn bản tiếng Việt).

---

## 📙 CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT (Tối đa 20 trang)

### 3.1. Tổng quan phương pháp và bài toán nghiên cứu
*   **Nội dung chính:** Đề xuất giải pháp toàn diện xây dựng mô hình Piper TTS giọng nam tiếng Việt chất lượng cao thông qua chiến lược **Cross-Gender Fine-tuning** kết hợp **tự xây dựng dữ liệu giọng nam đơn nguồn**. Tiến trình nghiên cứu được tổ chức thành hai giai đoạn dữ liệu dẫn tới việc huấn luyện và so sánh ba mô hình cụ thể: Giai đoạn 1 (VieNeu công khai) -> Model 1; Giai đoạn 2 (Tự thu thập YouTube) -> Run A (Full fine-tune) và Run B1 (Partial-freeze + đóng băng tham số). Sơ đồ hóa toàn bộ quy trình R&D từ dữ liệu thô đến mô hình tối ưu cuối cùng.

### 3.2. Chiến lược Cross-Gender Fine-tuning trên kiến trúc VITS
*   **3.2.1. Nguyên lý kế thừa mô hình nền:** Trình bày phương pháp tinh chỉnh chéo giới tính (cross-gender). Hệ thống khởi tạo trọng số từ mô hình nền giọng nữ `vi_VN-vais1000-medium` (đã được huấn luyện sâu qua 4769 epoch trên kho tiếng Việt lớn). Mô hình kế thừa nguyên vẹn tri thức ngôn ngữ, bộ mã hóa âm vị và hệ thanh điệu tiếng Việt của mô hình nữ, giúp rút ngắn thời gian hội tụ và bảo toàn chất lượng phát âm.
*   **3.2.2. Dịch chuyển đặc trưng âm học và huấn luyện đối kháng:** Giải thích cơ chế dịch chuyển không gian biểu diễn âm học (tần số cơ bản F0 từ dải ~230 Hz của nữ xuống ~110 Hz của nam, thay đổi cấu trúc formant và âm sắc) thông qua quá trình tiếp tục huấn luyện đối kháng (Adversarial Training) với bộ phân biệt (Discriminator) để bộ sinh (Generator) học được đặc trưng giọng nam thực tế.

### 3.3. Giai đoạn 1 — Xây dựng dữ liệu từ nguồn công khai VieNeu
*   **3.3.1. Khảo sát và lựa chọn nguồn dữ liệu:** Khảo sát các kho dữ liệu tiếng Việt. Lựa chọn bộ dữ liệu chất lượng studio **VieNeu-TTS-140h**. Do thời lượng giọng nam đơn lẻ quá ngắn, đồ án tiến hành **ghép ba speaker nam** có chất giọng đồng nhất (`jellyfish1010_0004`, `_0013`, `_0032`) để đạt thời lượng mục tiêu.
*   **3.3.2. Kiểm soát chất lượng và lọc dữ liệu:** Thu thập tập thô 1999 clip (~3.65 giờ). Xây dựng quy trình **kiểm định chất lượng bằng nhận dạng ngược (STT QC)**: dùng **PhoWhisper-large** nhận dạng lại toàn bộ clip, tính WER/CER để phát hiện lệch nhãn văn bản. Áp dụng bộ lọc lai theo speaker (Per-Speaker Hybrid) để làm sạch, thu được tập dữ liệu sạch **1500 clip (~2.5 giờ)**. 
*   *Hạn chế thực tế:* Tham số lọc độ dài mặc định của Piper (`max-phoneme-ids 400`) đã vô tình loại bỏ 390 clip dài (26% dữ liệu) khiến Model 1 thực tế chỉ train trên 1110 clip. Phần 390 clip dài bị loại này được giữ lại làm **tập kiểm thử độc lập (held-out validation)** để đánh giá khách quan tất cả mô hình ở Chương 4.
*   **3.3.3. Hạn chế của Giai đoạn 1 và động lực sang Giai đoạn 2:** Phân tích hạn chế của Model 1 (WER nhận dạng ngược còn cao, phát âm một số từ bị méo, ngọng). Chỉ ra nguyên nhân do dữ liệu thực train ít (~1110 clip) và quy trình huấn luyện chưa tối ưu (huấn luyện toàn bộ trọng số khiến phần mã hóa văn bản tiếng Việt bị trôi theo lịch Learning Rate mặc định của mô hình nền). Đây là động lực để chuyển sang Giai đoạn 2: tự xây dựng tập dữ liệu lớn hơn và thiết lập các chiến lược đóng băng tham số.

### 3.4. Giai đoạn 2 — Tự thu thập và xử lý dữ liệu từ YouTube
*   **3.4.1. Thu thập và tiền xử lý dữ liệu:** Thiết kế pipeline tự động thu thập từ kênh sách nói/podcast của một giọng nam chọn lọc trên YouTube: tải audio bằng `yt-dlp` -> phân đoạn câu kèm timestamp bằng `faster-whisper large-v3` -> cắt clip mục tiêu ~6 giây -> khử nhiễu môi trường bằng **Demucs (htdemucs)** -> chuẩn hóa mono 22.050 Hz, loudness -23 LUFS và đệm khoảng lặng đầu câu 0.2 giây để bảo toàn phụ âm đầu.
*   **3.4.2. Kiểm định nhãn đa nguồn (ASR cross-check) và hiệu đính bằng LLM:** Để giải quyết lỗi nhãn tự động, đề xuất cơ chế **kiểm định chéo bằng ba hệ ASR độc lập**: Faster-Whisper, Qwen3-ASR (chạy local) và Deepgram Nova-3 (API). Tính WER chéo giữa ba nguồn để lọc Keep/Review/Drop, sau đó đưa các clip cần hiệu chỉnh qua **LLM Gemini 3.5 Flash theo lô (batch)** để sửa nhãn văn bản dựa trên ngữ cảnh câu lân cận. Kết quả thu được bộ dữ liệu sạch chất lượng cao **2061 clip (~4.22 giờ)** (gấp 1.9 lần số clip thực train của Giai đoạn 1).
*   **3.4.3. Chuẩn hóa văn bản:** So sánh hai bộ chuẩn hóa: `vinorm` (dùng cho Run A) và **`vietnormalizer` kết hợp danh sách bảo vệ từ ngữ (protect-list)** (dùng cho Run B1) để xử lý triệt để các lỗi phiên âm từ tiếng Anh, từ mượn và dấu câu đặc thù trước khi đưa vào bộ mã hóa âm vị eSpeak-NG.

### 3.5. Hai chiến lược huấn luyện và tối ưu mô hình
*   **3.5.1. Bốn cải tiến quy trình huấn luyện ở Giai đoạn 2:** Khắc phục triệt để lỗi hệ thống từ Giai đoạn 1 bằng 4 cải tiến thực hành tốt:
    1.  *Đo ngưỡng âm vị động:* Phân tích độ dài chuỗi âm vị thực tế (max 857) và đặt ngưỡng `max-phoneme-ids` phù hợp (865 cho Run A, 837 cho Run B1) -> **tỷ lệ loại bỏ clip bằng 0%** (giữ trọn vẹn 2061 clip).
    2.  *Ghi log loss CSV trực tiếp:* Lưu trữ chỉ số huấn luyện theo từng epoch lên Google Drive ngay lập tức để tránh mất mát log khi ngắt kết nối Colab giữa chừng.
    3.  *Lưu checkpoint dày:* Lưu checkpoint sau mỗi epoch thay vì mỗi 10 epoch để không bỏ lỡ trạng thái hội tụ tốt nhất.
    4.  *Chủ động ép Learning Rate:* Viết script tùy biến `train_selfcollect.py` tích hợp callback `on_train_start` để khống chế Learning Rate chính xác ở mức **1e-4** cho cả Generator và Discriminator sau khi resume (có bước dry-run kiểm chứng), ngăn hiện tượng trôi tham số ngôn ngữ.
*   **3.5.2. Run A — Full fine-tune trên dữ liệu tự thu thập:** Mô hình đối chứng, thực hiện huấn luyện toàn bộ trọng số (full fine-tune) trên tập dữ liệu tự thu thập mới (chuẩn hóa bằng vinorm), sử dụng đầy đủ 4 cải tiến quy trình huấn luyện nêu trên.
*   **3.5.3. Run B1 — Đóng băng một phần (partial-freeze):** Mô hình cải tiến trọng tâm. Đề xuất đóng băng bộ mã hóa văn bản/tiên nghiệm `enc_p` và bộ dự đoán thời lượng `dp` (đóng băng **395 trên tổng số 673 tensor** trọng số), chỉ cho phép huấn luyện các tầng sinh âm sắc và dịch chuyển latent (Decoder, Normalizing Flow, Posterior Encoder và Discriminator). Giải pháp này giúp bảo toàn tuyệt đối khả năng phát âm và thanh điệu tiếng Việt chuẩn xác của mô hình nền, trong khi vẫn cập nhật đặc trưng giọng nam. Run B1 sử dụng bộ chuẩn hóa văn bản cải tiến `vietnormalizer`.

### 3.6. Thiết kế hệ thống S2ST realtime (Client–Server)
*   **3.6.1. Kiến trúc Client-Server và hai chế độ vận hành:** Thiết kế hệ thống giao tiếp song công qua giao thức WebSocket với máy trạng thái quản lý phiên chặt chẽ. Dữ liệu âm thanh được truyền dưới dạng các khung nhị phân (chứa byte định danh tuyến `route_id` để phân loại luồng Việt-Anh), văn bản truyền dạng JSON.
    *   *Chế độ 2 chiều (Online Meeting):* Route 0 (Việt -> Anh: Mic -> STT PhoWhisper -> NLLB VI-EN -> TTS English -> đưa vào Zoom/Meet qua VoiceMeeter); Route 1 (Anh -> Việt: WASAPI Loopback cuộc họp -> STT Faster-Whisper -> NLLB EN-VI -> TTS giọng nam Run B1 -> phát ra tai nghe).
    *   *Chế độ 1 chiều:* WASAPI Loopback -> Route 1 -> STT EN -> NLLB EN-VI -> TTS giọng nam Run B1 -> phát ra loa vật lý.
*   **3.6.2. Client (PySide6) và cô lập âm thanh bằng VoiceMeeter Banana:** Xây dựng giao diện Client bằng PySide6 chạy bất đồng bộ với thư viện `qasync`. Tích hợp giải pháp **VoiceMeeter Banana** để định tuyến âm thanh ảo (Virtual Audio Routing): luồng dịch phát đi được đẩy vào cổng micro ảo (bus B1), luồng họp thu về đi qua cổng Aux Input ảo độc lập. Sự cô lập này triệt tiêu hoàn toàn hiện tượng phản hồi âm học ở mức phần mềm.
*   **3.6.3. Server phân tầng hướng engine:** Thiết kế server FastAPI sử dụng mẫu thiết kế Facade đa hình (Polymorphic Facade) định nghĩa hợp đồng chung cho cả ba engine STT/MT/TTS. Cơ chế Execution Lane sử dụng thread pool kết hợp khóa thao tác `operation_lock` trên từng model để tránh xung đột tài nguyên GPU. Thiết lập bước Preload & Warmup để "làm nóng" toàn bộ mô hình lúc khởi động server, triệt tiêu độ trễ khởi động lạnh (cold-start).

### 3.7. Pipeline streaming STT–MT–TTS thời gian thực
*   **3.7.1. Phân đoạn câu bằng Silero VAD và duy trì ngữ cảnh:** Khối âm thanh PCM 200 ms được gửi liên tục, mô hình Silero VAD tính xác suất tiếng nói để xác định khoảng lặng. Cắt câu động dựa trên ngưỡng im lặng liên tục **450 ms** kết hợp đệm thêm **Hangover Frame ~400 ms** ở cuối câu để bảo toàn các âm đuôi năng lượng thấp. Áp dụng bộ đệm trượt ngữ cảnh (Context Sliding Buffer) để duy trì tính liên tục cho tầng STT mà không gây lặp từ.
*   **3.7.2. Đệm dịch ngắn, Watchdog và tách câu:** Thiết kế cơ chế đệm dịch ngắn (Short-MT Buffering) tích lũy văn bản STT đến độ dài tối thiểu để đảm bảo NLLB-200 dịch đủ ngữ cảnh và tự nhiên. Thiết lập bộ giám sát thời gian (Watchdog/Force Flush) cưỡng bức đẩy bản dịch đi sau 3 giây im lặng dù chưa đạt độ dài tối thiểu để đảm bảo độ trễ thấp. Áp dụng Comma Fallback Splitter để cắt câu dài thành các đoạn nhỏ cho TTS suy luận cuốn chiếu.
*   **3.7.3. Tích hợp TTS giọng nam và trực quan hóa kết quả:** Tích hợp mô hình giọng nam tối ưu **`runB1_e4868`** (đã xuất sang ONNX) vào tầng TTS phía server để nhận diện luồng dịch Route 1, sinh âm thanh và gửi trả về client dạng khung nhị phân để phát cuốn chiếu theo cơ chế hàng đợi bất đồng bộ.

---

## 🔬 CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ (Tối đa 25 trang)

### 4.1. Môi trường và kịch bản thử nghiệm
*   **4.1.1. Môi trường:** Huấn luyện trên **Google Colab Pro (GPU NVIDIA Tesla T4 16GB VRAM)**. Các tiến trình tiền xử lý, kiểm định dữ liệu và đánh giá chạy cục bộ (WSL2 Ubuntu / Windows). Áp dụng kỹ thuật snapshotting nén môi trường ảo để khôi phục môi trường làm việc trên Colab trong vòng 30 giây.
*   **4.1.2. Kịch bản và tập câu thử nghiệm:** Đánh giá mô hình trên hai tập câu: tập **25 câu curated** (kiểm tra các trường hợp khó như số, ngày tháng, từ mượn tiếng Anh, câu dài) và tập **300 câu held-out chung** (được lấy từ 390 clip dài bị loại ở Giai đoạn 1 của VieNeu, đảm bảo cả 4 mô hình chưa từng được huấn luyện trên tập câu này để đảm bảo tính khách quan tối đa). Đo lường hiệu năng suy luận trên cả CPU (2 nhân phổ thông) và GPU.

### 4.2. Kết quả xây dựng tập dữ liệu
*   **4.2.1. Giai đoạn 1 — Tập VieNeu sau lọc:** Từ 1999 clip thô (~3.65 giờ) của VieNeu-TTS-140h ghép từ 3 speaker nam, sau khi chạy bộ lọc chất lượng nhận dạng ngược (STT QC) bằng PhoWhisper-large và lọc Per-Speaker Hybrid, thu được tập sạch **1500 clip (~2.5 giờ)**. Do giới hạn `max-phoneme-ids 400` cố định, Model 1 thực tế huấn luyện trên **1110 clip** (390 clip dài bị loại chuyển thành tập held-out test).
*   **4.2.2. Giai đoạn 2 — Tập tự thu thập từ YouTube:** Quy trình cắt câu tự động từ YouTube đạt 2367 clip sạch. Qua kiểm định nhãn chéo bằng ba hệ ASR (Faster-Whisper, Qwen3-ASR, Deepgram Nova-3) và hiệu đính bằng LLM Gemini, thu được bộ dữ liệu sạch hoàn hảo **2061 clip (~4.22 giờ)**. Nhờ đo ngưỡng độ dài âm vị động, hai cấu hình Run A và Run B1 **giữ được 100% dữ liệu huấn luyện (drop 0)**.

### 4.3. Chỉ số và phương pháp đánh giá
*   **Nội dung chính:** Xây dựng hệ thống chỉ số đánh giá đa chiều bao gồm:
    *   *Độ rõ chữ (Intelligibility):* Tính WER và CER bằng phương pháp hồi chuyển (suy luận ra âm thanh -> dùng hai hệ ASR độc lập là PhoWhisper-large và Whisper-large-v3 nhận dạng ngược lại -> so sánh với văn bản gốc).
    *   *Độ tự nhiên (Naturalness):* Chấm điểm tự động bằng mô hình học sâu **NISQA-TTS MOS** (thang điểm 1-5) kết hợp khảo sát lấy điểm số trung bình từ người nghe thực tế (Human MOS).
    *   *Đặc trưng giọng nam:* Đo tần số cơ bản trung bình F0 (Hz) để xác thực sự dịch chuyển giới tính giọng đọc và đo trọng tâm phổ (spectral centroid) để phân tích âm sắc.
    *   *Hiệu năng:* Đo hệ số thời gian thực (Real-Time Factor - RTF) trên cả CPU và GPU.

### 4.4. Kết quả huấn luyện các mô hình
*   **4.4.1. Model 1 (VieNeu):** Khảo sát đường cong loss bằng cách chạy kiểm định lại 84 checkpoint. Mel loss và KL loss hội tụ rất nhanh trong 10 epoch đầu và đi vào vùng phẳng. Checkpoint **e5219** (đạt val_loss trung bình trượt thấp nhất **≈32.98**) được chọn làm mô hình tốt nhất của Giai đoạn 1.
*   **4.4.2. Run A và Run B1:** Đánh giá tốc độ hội tụ trên tập dữ liệu tự thu thập. Kết quả thực nghiệm cho thấy dữ liệu tự thu thập đạt tốc độ hội tụ nhanh và dứt khoát hơn hẳn VieNeu (Run B1 đạt 95% chất lượng hội tụ chỉ sau **68 epoch**, Run A là 78 epoch, trong khi VieNeu cần tới 450 epoch). Quá trình huấn luyện GAN ổn định, không xảy ra hiện tượng sụp đổ (collapse) hay quá khớp (overfitting). Checkpoint tốt nhất được chọn tương ứng là `ep4862` (Run A) và `ep4868` (Run B1).

### 4.5. Đánh giá và so sánh chất lượng mô hình
*   **4.5.1. Đánh giá Giai đoạn 1:** Đối sánh 3 mô hình ở Giai đoạn 1 trên 25 câu test cho thấy e5219 cải thiện điểm NISQA MOS rõ rệt so với baseline nữ (+8.7%, đạt 3.379) và giọng đọc ổn định hơn, tuy nhiên độ rõ chữ bị suy giảm (WER tăng từ 0.119 lên 0.311) do dữ liệu huấn luyện thực tế ít (~1110 clip) và full fine-tune làm trôi tham số ngôn ngữ.
*   **4.5.2. Đánh giá bốn mô hình trên tập held-out 300 câu:** Thực nghiệm đánh giá chéo quy mô lớn trên tập 300 câu held-out chưa từng thấy trong huấn luyện của cả 4 mô hình (vais1000 nữ nền, VieNeu e5219, Run A, Run B1) mang lại các số liệu định lượng quan trọng:
    1.  *Chuyển giới tính thành công:* Cả 3 mô hình fine-tune nam đều dịch chuyển tần số cơ bản F0 cực tốt về vùng giọng nam trầm ấm (**~112.8 Hz đến ~114.8 Hz**) so với giọng nữ nền (~231.6 Hz).
    2.  *Độ rõ chữ vượt trội:* **Run B1 đạt độ rõ chữ cao nhất trong nhóm nam với chỉ số WER PhoWhisper chỉ 4.1%** (giảm thiểu 24% lỗi từ so với Run A là 5.4% và giảm gần 3 lần so với VieNeu e5219 là 12.0%). Điểm CER của Run B1 đạt mức cực thấp là 2.0%.
    3.  *Độ tự nhiên cao nhất:* **Run B1 đạt điểm NISQA MOS cao nhất nhóm nam là 4.13** (mức GOOD), vượt qua Run A (4.10), VieNeu e5219 (3.49) và vượt trội cả mô hình giọng nữ gốc (3.21).
*   **4.5.3. Quyết định triển khai cuối cùng:** Chọn mô hình **Run B1 (`runB1_e4868`)** làm mô hình giọng nam tiếng Việt chính thức để tích hợp vào hệ thống S2ST nhờ đứng đầu tuyệt đối tất cả các chỉ số chất lượng âm học và độ rõ chữ trong nhóm giọng nam.
*   **4.5.4. Hiệu năng suy luận và dung lượng mô hình:** Cả 4 mô hình đều đạt hệ số thời gian thực **RTF cực thấp ~0.15 trên CPU 2 nhân** (tốc độ suy luận nhanh gấp 6.7 lần thời gian thực, mất khoảng 1.02 giây cho một câu thoại trung bình) và **~0.009 trên GPU** (chỉ mất 64 ms/câu). Mô hình Run B1 được xuất ra định dạng **ONNX FP32 với dung lượng nhẹ ~63.5 MB**, đảm bảo chạy mượt mà ngay trên các CPU máy khách phổ thông.

### 4.6. Kết quả tích hợp và vận hành hệ thống S2ST
*   **4.6.1. Kết quả chức năng ứng dụng client:** Ứng dụng GUI PySide6 vận hành chính xác tất cả các tính năng thiết kế: bắt tay kết nối WebSocket động, tự động warmup làm nóng mô hình triệt tiêu trễ câu đầu, nhận dạng và hiển thị song song hai luồng transcript Route 0 và Route 1 thời gian thực mượt mà, không bị chồng chéo dữ liệu hay lẫn lộn kênh.
*   **4.6.2. Kiểm thử chức năng end-to-end:** Hệ thống vượt qua thành công 100% các kịch bản kiểm thử chức năng tích hợp bao gồm dịch văn bản thuần, nhận dạng streaming (cập nhật liên tục interim và chốt final), tự động kết nối lại khi ngắt mạng và kết thúc phiên sạch.
*   **4.6.3. Cô lập âm thanh loopback bằng VoiceMeeter:** Chứng minh thực nghiệm giải pháp phần mềm VoiceMeeter Banana định tuyến đa bus ảo đã cô lập hoàn toàn luồng âm dịch phát đi và luồng họp thu về, giải quyết triệt để lỗi vòng lặp phản hồi âm học (feedback loop) và tự dịch tuần hoàn trong môi trường họp trực tuyến (Google Meet, Zoom) khi kết hợp đeo tai nghe.
*   **4.6.4. Đặc tính độ trễ và khả năng thời gian thực:** Phân tích thực tế cho thấy độ trễ tích lũy toàn hệ thống đối với **câu ngắn (~5-10 từ) dao động trong khoảng ~1 - 2 giây** (phản hồi interim xuất hiện cực nhanh sau ~0.3 - 0.5 giây). Phân rã độ trễ định lượng chỉ ra:
    *   *Chờ điểm kết thúc câu (VAD 450ms + hangover ~400ms):* ~0.85 giây (thành phần cố định, chiếm tỷ trọng cao nhất để đảm bảo dịch đủ ngữ cảnh).
    *   *Nhận dạng STT:* ~0.2 - 0.4 giây.
    *   *Dịch máy NMT (CTranslate2 int8):* ~0.1 - 0.2 giây.
    *   *Tổng hợp TTS (ONNX Runtime) + phát:* ~0.1 - 0.3 giây.
    *   *Nhận xét:* Độ trễ tỷ lệ thuận với độ dài câu do thiết kế chờ trọn câu để dịch máy đạt chất lượng cao nhất. Đây là sự đánh đổi kỹ thuật có chủ đích và hoàn toàn nằm trong ngưỡng chấp nhận được cho hội thoại trực tuyến.

---

## 🔚 CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN (Tối đa 5 trang)

### 5.1. Những đóng góp chính của đồ án
*   **Nội dung chính:** Tổng kết 3 đóng góp khoa học và thực tiễn lớn nhất của đồ án tốt nghiệp:
    1.  *Về mặt hệ thống:* Hiện thực hóa thành công hệ thống dịch giọng nói sang giọng nói (S2ST) song hướng, streaming thời gian thực qua kết nối WebSocket song công, tích hợp 3 tầng AI và giải pháp chống phản hồi âm học triệt để bằng VoiceMeeter Banana.
    2.  *Về mặt mô hình:* Đóng góp cho cộng đồng nghiên cứu mô hình **Piper TTS giọng nam tiếng Việt Run B1** chất lượng cao (WER ~4.1%, NISQA 4.13), dung lượng siêu nhẹ (~63.5 MB) chạy tốt trên CPU phổ thông.
    3.  *Về mặt quy trình dữ liệu:* Đóng gói quy trình tự động xây dựng và kiểm định chất lượng dữ liệu giọng nói đa nguồn (ASR cross-check + LLM hiệu đính) cùng các bài học phương pháp huấn luyện (đóng băng tham số tiên nghiệm, ép Learning Rate chủ động).

### 5.2. Các hạn chế
*   **Nội dung chính:** Thẳng thắn nhìn nhận các điểm hạn chế kỹ thuật hiện tại của đề tài:
    1.  Tầng máy chủ xử lý AI vẫn phụ thuộc vào hạ tầng GPU đám mây (Google Colab T4), chưa chạy hoàn toàn offline cục bộ.
    2.  Độ trễ tích lũy tăng dần theo độ dài câu nói do thiết kế VAD chờ dứt câu; hệ thống mới chỉ đo độ trễ bằng phương pháp ước lượng/thủ công, chưa xây dựng bộ đo định lượng tự động hoàn chỉnh.
    3.  Tập dữ liệu tự thu thập mới chỉ giới hạn ở một giọng nam đọc sách nói (~4.22 giờ), chưa đa dạng vùng miền và phong cách nói tự nhiên.
    4.  Chưa tích hợp thành công lượng tử hóa FP16 cho mô hình TTS do lỗi tương thích nút Cast của ONNX Runtime đối với kiến trúc VITS.

### 5.3. Kiến nghị và Hướng phát triển
*   **5.3.1. Mô hình giọng nam độ nét cao hơn (Run B2 — đang nghiên cứu):** Đề xuất giải pháp nâng cấp mô hình lên cấu hình độ nét cao (high-resolution) bằng cách ghép các tầng ngôn ngữ đã đóng băng của mô hình medium (`enc_p`, `dp`) vào khung của Piper cấu hình "high" (tăng số kênh decoder HiFi-GAN lên 512 kênh ở cùng sample rate 22.050 Hz) để nâng cao độ nét sóng âm. Hướng này hiện đang tạm gác lại do chi phí huấn luyện lớn, sẽ tiếp tục triển khai khi có đủ tài nguyên phần cứng.
*   **5.3.2. Các hướng phát triển khác:** 
    *   *Về độ trễ:* Nghiên cứu cơ chế dịch gia tăng cuốn chiếu (incremental translation) cho tầng STT/MT để giảm thời gian chờ đợi dứt câu; phát triển công cụ đo độ trễ tự động chuẩn xác trên nhiều kịch bản.
    *   *Về triển khai:* Tiến hành lượng tử hóa sâu (INT8/INT4) cho tất cả các mô hình và đưa STT/MT chạy trực tiếp tại client nhằm tiến tới một hệ thống hoạt động hoàn toàn offline không phụ thuộc internet.
    *   *Về mở rộng:* Thu thập dữ liệu đa giọng đọc, đa vùng miền cho TTS; mở rộng sang các cặp ngôn ngữ khác (Nhật, Hàn); nghiên cứu tích hợp các kiến trúc dịch giọng nói đầu-cuối (End-to-End S2ST) để bảo toàn tối đa cảm xúc và ngữ điệu người nói trong tương lai.

---

## 📚 DANH MỤC TÀI LIỆU THAM KHẢO
*   **Nội dung chính:** Tổng hợp danh mục tài liệu tham khảo chất lượng cao bao gồm 30 tài liệu khoa học, bài báo hội thảo quốc tế uy tín (ICML, Interspeech, ICLR, SciPy) và các kho mã nguồn mở được định dạng chuẩn xác theo chuẩn **APA 7th** (sắp xếp theo thứ tự bảng chữ cái tên tác giả).

---

## 📎 PHỤ LỤC
*   **Phụ lục A — Trích đoạn mã nguồn tiêu biểu:** Trình bày các cấu trúc mã nguồn cốt lõi của hệ thống bao gồm: Hợp đồng đa hình Polymorphic Facade của 3 engine; Script huấn luyện tùy biến `train_selfcollect.py` tích hợp callback khóa tham số và ép Learning Rate chủ động; và module wrapper chuẩn hóa văn bản.
*   **Phụ lục B — Cấu hình hệ thống tiêu biểu:** Cung cấp các file cấu hình hyperparameter huấn luyện mô hình Piper TTS, cấu hình preload/warmup của server, và bảng thông số định tuyến kênh âm thanh ảo của VoiceMeeter Banana.
*   **Phụ lục C — Dữ liệu thực nghiệm bổ sung:** Lưu trữ bảng số liệu đánh giá chi tiết của 1300 tệp âm thanh kiểm thử held-out, biểu đồ phân bố và danh sách 25 câu curated dùng để rà soát chất lượng âm học.
