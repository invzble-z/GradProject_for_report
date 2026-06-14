# BÁO CÁO ĐỒ ÁN TỐT NGHIỆP KỸ SƯ AI
## ĐỀ TÀI: HỆ THỐNG DỊCH GIỌNG NÓI THỜI GIAN THỰC SONG HƯỚNG ANH - VIỆT (S2ST) TỐI ƯU HÓA ĐỘ TRỄ VÀ CHẤT LƯỢNG GIỌNG NÓI TỔNG HỢP

---

## TRANG THỦ TỤC & DẪN NHẬP

### TRANG TIÊU ĐỀ (Title Page)

```
BỘ GIÁO DỤC VÀ ĐÀO TẠO
TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG VIỆT - HÀN

KHOA KHOA HỌC MÁY TÍNH VÀ KỸ THUẬT
---***---



BÁO CÁO ĐỒ ÁN TỐT NGHIỆP KỸ SƯ NGÀNH TRÍ TUỆ NHÂN TẠO (AI)

ĐỀ TÀI:
HỆ THỐNG DỊCH GIỌNG NÓI THỜI GIAN THỰC SONG HƯỚNG ANH - VIỆT (S2ST) 
TỐI ƯU HÓA ĐỘ TRỄ VÀ CHẤT LƯỢNG GIỌNG NÓI TỔNG HỢP




Sinh viên thực hiện:   [Tên sinh viên thực hiện]
Lớp:                  [Tên lớp, ví dụ: 22AI]
Giảng viên hướng dẫn:  [Tên giảng viên hướng dẫn]
Bộ môn:               Trí tuệ nhân tạo và Khoa học dữ liệu




Đà Nẵng - Năm 2026
```

---

### TRANG NỘI DUNG (Content Page)

*(Mục lục chi tiết cấp 3 được trình bày chi tiết trong tệp BAOCAO_OUTLINE.md và sẽ tự động biên dịch sang danh mục trang của báo cáo chính thức)*

---

### LỜI CẢM ƠN (Acknowledgements)

Lời đầu tiên, em xin bày tỏ lòng biết ơn chân thành và sâu sắc nhất đến Ban Giám hiệu cùng toàn thể quý thầy cô giáo Trường Đại học Công nghệ Thông tin và Truyền thông Việt - Hàn (VKU), đặc biệt là các thầy cô thuộc Khoa Khoa học Máy tính và Kỹ thuật, những người đã truyền dạy tri thức và định hướng tư duy học thuật quý báu cho em trong suốt những năm học tập tại trường.

Đặc biệt, em xin gửi lời cảm ơn sâu sắc nhất tới Giảng viên hướng dẫn - **[Tên giảng viên hướng dẫn]**, người đã tận tình chỉ bảo, định hướng khoa học và luôn dành cho em những lời khuyên, sự động viên quý báu để em vượt qua các thách thức kỹ thuật lớn trong suốt quá trình hoàn thiện đồ án này.

Em cũng xin chân thành cảm ơn các bạn sinh viên lớp [Tên lớp] cùng tập thể các bạn trong nhóm nghiên cứu đã luôn chia sẻ tài nguyên tính toán, đóng góp những ý kiến phản biện khoa học sắc bén và hỗ trợ em thực nghiệm kiểm định chất lượng giọng nói.

Cuối cùng, em xin kính dâng lòng biết ơn vô hạn tới gia đình và những người thân yêu, những người luôn là chỗ dựa tinh thần vững chắc, tiếp thêm động lực để em hoàn thành chặng đường học tập ý nghĩa này. Do giới hạn về thời gian và năng lực nghiên cứu, đồ án chắc chắn không tránh khỏi những thiếu sót nhất định. Em rất mong nhận được những ý kiến đóng góp, chỉ dẫn quý báu từ Hội đồng đánh giá để hệ thống được hoàn thiện hơn.

*Đà Nẵng, ngày ... tháng ... năm 2026*  
Sinh viên thực hiện  
**[Tên sinh viên]**

---

### DANH MỤC CÁC CHỮ VIẾT TẮT (Acronym List)

| Từ viết tắt | Thuật ngữ tiếng Anh đầy đủ | Ý nghĩa tiếng Việt |
| :--- | :--- | :--- |
| **STT** | Speech-to-Text | Nhận dạng tiếng nói (Chuyển giọng nói thành văn bản) |
| **MT** | Machine Translation | Dịch máy |
| **NMT** | Neural Machine Translation | Dịch máy thần kinh |
| **TTS** | Text-to-Speech | Tổng hợp tiếng nói (Chuyển văn bản thành giọng nói) |
| **S2ST** | Speech-to-Speech Translation | Dịch giọng nói sang giọng nói thời gian thực |
| **VAD** | Voice Activity Detection | Phân đoạn hoạt động giọng nói |
| **VITS** | Variational Inference with adversarial learning for end-to-end Text-to-Speech | Mô hình tổng hợp giọng nói đầu-cuối dựa trên biến phân đối nghịch |
| **ONNX** | Open Neural Network Exchange | Định dạng trao đổi mạng thần kinh mở |
| **WER** | Word Error Rate | Tỉ lệ lỗi từ |
| **CER** | Character Error Rate | Tỉ lệ lỗi ký tự |
| **RTF** | Real-Time Factor | Hệ số thời gian thực |
| **MOS** | Mean Opinion Score | Điểm đánh giá trung bình chất lượng âm thanh |
| **VRAM** | Video Random Access Memory | Bộ nhớ truy cập ngẫu nhiên đồ họa |
| **WASAPI** | Windows Audio Session API | Giao diện lập trình phiên âm thanh Windows |
| **VBD** | Sentence Boundary Detection | Phân đoạn ranh giới câu |
| **SNR** | Signal-to-Noise Ratio | Tỉ lệ tín hiệu trên nhiễu |
| **GAN** | Generative Adversarial Network | Mạng đối nghịch tạo sinh |
| **KL** | Kullback-Leibler (Divergence) | Độ phân kỳ KL (Độ đo sự khác biệt hai phân phối) |

---

### DANH MỤC BẢNG (List of Tables)

*(Danh mục bảng biểu sẽ tự động sinh và liên kết từ nội dung chi tiết của Chương 3 và Chương 4)*

---

### DANH MỤC HÌNH VẼ - ĐỒ THỊ (List of Figures)

*(Danh mục hình vẽ, sơ đồ luồng dữ liệu và đồ thị hội tụ sẽ được sinh tự động)*

---

### LỜI MỞ ĐẦU (Introduction)

Trong bối cảnh toàn cầu hóa và sự bùng nổ của chuyển đổi số, giao tiếp xuyên ngôn ngữ trở thành cầu nối quyết định sự thành công của các doanh nghiệp, tổ chức và hoạt động hợp tác khoa học quốc tế. Tuy nhiên, rào cản ngôn ngữ, đặc biệt trong các cuộc họp trực tuyến trực tiếp song hướng giữa hai ngôn ngữ Anh và Việt, vẫn là một thách thức lớn. Hệ thống dịch giọng nói trực tiếp sang giọng nói (Speech-to-Speech Translation - S2ST) là giải pháp tối ưu nhằm tái tạo chu kỳ hội thoại tự nhiên của con người: lắng nghe giọng nói nguồn, dịch thuật ngữ nghĩa và tổng hợp lại bằng giọng nói đích. Đồ án này tập trung nghiên cứu, phát triển và tối ưu hóa **Hệ thống dịch giọng nói thời gian thực song hướng Anh - Việt (S2ST)** hoạt động dưới mô hình máy khách - máy chủ (Client-Server) qua kết nối WebSocket song công, nhằm hướng tới sự cân bằng tối ưu giữa độ trễ và chất lượng tự nhiên của giọng nói dịch thuật.

#### 1. Lý do lựa chọn đề tài
Trong kỷ nguyên toàn cầu hóa, nhu cầu giao tiếp trực tuyến xuyên biên giới qua các nền tảng như Zoom, Google Meet hay Microsoft Teams trở thành một phần thiết yếu của hoạt động vận hành doanh nghiệp và hợp tác quốc tế. Tuy nhiên, việc bất đồng ngôn ngữ giữa các bên tham gia thường gây ra những gián đoạn lớn về mặt truyền đạt thông tin. Các giải pháp dịch thuật truyền thống như thuê biên dịch viên cabin thường tốn kém chi phí, thiếu tính linh hoạt và không đảm bảo độ bảo mật thông tin nội bộ. Trong khi đó, việc sử dụng các công cụ dịch văn bản thông thường lại yêu cầu người dùng phải gõ chữ hoặc copy-paste liên tục, phá hỏng hoàn toàn sự liền mạch của một buổi đối thoại trực tiếp. Xuất phát từ nhu cầu thực tiễn đó, việc phát triển một hệ thống dịch giọng nói sang giọng nói thời gian thực (S2ST) trực diện là lời giải tối ưu. Tuy nhiên, khi triển khai hệ thống này vào thực tế phòng họp ảo song hướng với nguồn tài nguyên tính toán giới hạn, người phát triển phải đối mặt với nhiều trở ngại thực tế rất lớn.

Trước hết, độ trễ tích lũy qua ba phân tầng nhận dạng (STT), dịch máy (NMT) và tổng hợp tiếng nói (TTS) là rào cản trực tiếp nhất. Nếu không được tối ưu hóa, tổng thời gian từ lúc người nói dứt câu cho đến khi người nghe nhận được âm thanh dịch có thể kéo dài từ 4.0 đến 6.0 giây, khiến các bên tham gia dễ nói đè lên nhau, tạo ra các khoảng lặng ngượng ngùng và làm mất đi nhịp điệu của cuộc đối thoại. Bên cạnh đó, đặc thù tiếng Việt có tính thanh điệu phức tạp, người nói thường ngắt nhịp ngắn giữa các từ, dễ làm mô hình phân đoạn giọng nói (VAD) hiểu lầm là đã kết thúc câu và kích hoạt lệnh dịch sớm khi câu chưa trọn vẹn ngữ nghĩa. Ngược lại, khi người nói phát âm nhanh, các phụ âm cuối yếu dễ bị mô hình VAD cắt mất, làm giảm sút độ chính xác nhận dạng chặng đầu. Ở chặng tổng hợp (TTS), việc thiếu hụt một mô hình giọng nam miền Nam tự nhiên, rõ chữ và đủ nhẹ để chạy trực tiếp trên CPU máy khách là một thực trạng rõ rệt, do các tài nguyên mở hiện nay hầu như chỉ cung cấp giọng nữ. Cuối cùng, hiện tượng vòng lặp phản hồi âm học là lỗi thực tế phổ biến nhất; nếu âm thanh dịch phát ra từ loa máy khách bị chính micro của họ thu lại, hệ thống sẽ tự động gửi lên server để dịch đi dịch lại vô hạn, gây nhiễu loạn thông tin và tạo ra tiếng hú lớn gây hỏng thiết bị. Do đó, việc nghiên cứu các giải pháp tối ưu hóa độ trễ, tinh chỉnh mô hình giọng nam từ dữ liệu giới hạn và thiết lập giải pháp cô lập luồng âm thanh máy khách là vô cùng cấp thiết nhằm giải quyết triệt để các vấn đề thực tiễn này.

#### 2. Mục tiêu nghiên cứu
Đồ án hướng tới các mục tiêu cụ thể sau:
- **Thiết kế hệ thống S2ST song hướng thời gian thực:** Xây dựng hoàn chỉnh kiến trúc Client-Server kết nối qua giao thức WebSocket, kiểm soát và giảm thiểu tổng độ trễ cumulative đầu-cuối xuống dưới ngưỡng nhận thức tự nhiên của hội thoại thường nhật.
- **Tối ưu hóa các chặng trung gian:** Đề xuất và triển khai các thuật toán xử lý luồng (VAD Hangover, Short-MT Buffering kết hợp Watchdog flush và Comma Fallback Splitter) nhằm giảm thiểu độ trễ Time-to-First-Audio (TTFA) của chặng TTS mà vẫn đảm bảo tính toàn vẹn ngữ nghĩa.
- **Nghiên cứu quy trình tinh chỉnh Piper TTS giọng nam Việt:** Ứng dụng phương pháp chuyển giới tính giọng nói (*Cross-Gender Fine-tuning*) để tạo ra mô hình giọng nam miền Nam từ tập dữ liệu giới hạn, nén lượng tử hóa sang định dạng FP16 siêu nhẹ (~32MB) chạy mượt mà trên CPU phân khúc phổ thông.
- **Cách ly phản hồi âm học ngầm:** Xây dựng giải pháp định tuyến âm thanh ảo hai lộ tuyến độc lập, sử dụng API ghi âm loopback WASAPI để cô lập triệt để vòng lặp phản hồi âm mà không yêu cầu đặc quyền Quản trị viên (Administrator).

#### 3. Đối tượng và phạm vi nghiên cứu
- **Đối tượng nghiên cứu:** 
  - Các kiến trúc học sâu tiên tiến phục vụ xử lý giọng nói và ngôn ngữ: Mạng tự chú ý và Transformer trong Whisper/PhoWhisper, mô hình dịch máy đa ngôn ngữ NLLB-200 và thư viện tối ưu hóa CTranslate2, kiến trúc VITS nén nhẹ (Piper TTS) dựa trên Normalizing Flows và GANs, mô hình phát hiện hoạt động giọng nói Silero VAD.
  - Các giao thức truyền thông mạng song công thời gian thực (WebSocket) và cơ chế định tuyến âm thanh ảo trên hệ điều hành Windows (WASAPI, VB-Audio Virtual Cable).
- **Phạm vi nghiên cứu:**
  - Cặp ngôn ngữ dịch thuật song hướng: Anh - Việt và Việt - Anh.
  - Môi trường thử nghiệm máy chủ: Phân bổ tài nguyên trên duy nhất một GPU tầm trung NVIDIA Tesla T4 (Google Colab / FastAPI server).
  - Môi trường thử nghiệm máy khách: Chạy ứng dụng đồ họa PySide6 tích hợp `qasync` trực tiếp trên hệ điều hành Windows 10/11 local.
  - Tập dữ liệu huấn luyện TTS: Lọc và chuẩn hóa dữ liệu giọng nam miền Nam từ bộ dữ liệu `VieNeu-TTS-140h`.

#### 4. Cách tiếp cận
Để giải quyết bài toán đặt ra dưới điều kiện giới hạn về phần cứng, đồ án đề xuất các phương pháp tiếp cận sau:
- **Tiếp cận kiến trúc phân tán tối ưu hóa tài nguyên:** Phân bổ các tác vụ STT và NMT nặng (đòi hỏi tính toán ma trận lớn) lên GPU đám mây của máy chủ thông qua các facade bất đồng bộ; đồng thời đẩy tác vụ suy luận TTS (nhờ mô hình Piper nén nhẹ) và điều phối âm thanh về CPU máy khách nhằm triệt tiêu băng thông truyền tải âm thanh chặng cuối trên mạng.
- **Tiếp cận tối ưu hóa song song bất đồng bộ:** Thiết lập các "Execution Lane" song song có cơ chế khóa hoạt động (`operation_lock`) trên từng model entry để tránh nghẽn GPU VRAM, kết hợp cơ chế Warmup khởi động nóng để giảm trễ cold-start về 0.
- **Tiếp cận chuyển giao tri thức (Transfer Learning) cho TTS:** Thay vì huấn luyện mô hình VITS giọng nam từ đầu vốn cần lượng dữ liệu khổng lồ, đồ án thực hiện Cross-Gender Fine-tuning dựa trên không gian nhúng âm vị có sẵn của checkpoint gốc giọng nữ `vais1000-medium`, giúp mô hình nhanh chóng hội tụ và đạt độ tự nhiên cao chỉ với 2.5 giờ dữ liệu nam sạch.
- **Tiếp cận cô lập tuyến âm vật lý - ảo (Routing Isolation):** Cô lập luồng dịch xuôi (VI-EN) đẩy thẳng vào thiết bị âm thanh ảo đầu vào làm micro cho phần mềm họp, tách biệt hoàn toàn với luồng dịch ngược (EN-VI) phát ra loa ngoài, triệt tiêu phản hồi âm học mà không can thiệp sâu vào nhân hệ điều hành.

#### 5. Phương pháp nghiên cứu
Đồ án áp dụng kết hợp các phương pháp nghiên cứu sau:
- **Phương pháp nghiên cứu lý thuyết:** Nghiên cứu tài liệu chuyên khảo về xử lý tín hiệu số, kiến trúc Transformer chú ý tự thân, mô hình biến phân tự động điều kiện (Conditional VAE), Normalizing Flows, và mạng đối nghịch tạo sinh (GAN) trong tổng hợp tiếng nói.
- **Phương pháp thực nghiệm và xây dựng hệ thống:**
  - Xây dựng quy trình tự động hóa kiểm soát chất lượng dữ liệu (STT QC) sử dụng mô hình *PhoWhisper-large* đánh giá chéo Word Error Rate (WER) nhằm loại bỏ clips lệch pha, trích xuất tập dữ liệu sạch 1500 câu chuẩn.
  - Tiến hành huấn luyện thực nghiệm mô hình TTS trên Google Colab qua 3000 epochs, theo dõi các đường cong hội tụ loss (Generator/Discriminator/Mel/KL), sau đó lượng tử hóa mô hình sang FP16 ONNX.
  - Xây dựng phần mềm client PySide6 thực thi định tuyến và ghi âm loopback WASAPI.
- **Phương pháp đánh giá và kiểm chứng:**
  - Đo đạc định lượng khách quan: Sử dụng hệ thống telemetry đo trễ xử lý từng phân tầng, tính toán chỉ số WER của STT, hệ số thời gian thực RTF của TTS và ứng dụng mô hình deep learning *NISQA* để chấm điểm MOS khách quan cho giọng nói tổng hợp.
  - Đo đạc định tính chủ quan: Khảo sát và lấy điểm Mean Opinion Score (Human MOS) từ người dùng thực tế dựa trên bộ 25 câu test chuẩn để đánh giá độ tự nhiên, rõ chữ và tính biểu cảm của giọng nam miền Nam được tinh chỉnh.

---

## CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

### 1.1. Lý do chọn đề tài (Motivation)

#### 1.1.1. Nhu cầu dịch thuật trực tuyến đa ngôn ngữ trong kỷ nguyên toàn cầu hóa

Trong kỷ nguyên toàn cầu hóa và sự phát triển mạnh mẽ của nền kinh tế số, nhu cầu giao tiếp xuyên biên giới đã trở thành một yếu tố sống còn đối với các doanh nghiệp, tổ chức giáo dục và các cơ quan nghiên cứu khoa học. Sự phổ biến của các nền tảng họp trực tuyến như Zoom, Google Meet và Microsoft Teams đã phá bỏ các rào cản vật lý về địa lý, cho phép các cá nhân từ khắp nơi trên thế giới cộng tác trong cùng một không gian ảo. Tuy nhiên, rào cản ngôn ngữ vẫn là một thách thức lớn nhất đối với việc truyền đạt thông tin một cách chính xác, tự nhiên và tức thời.

Hệ thống dịch thuật giọng nói sang giọng nói trực tiếp (Speech-to-Speech Translation - S2ST) đại diện cho đỉnh cao của công nghệ xử lý ngôn ngữ tự nhiên (NLP) và xử lý tín hiệu âm thanh. Khác với các giải pháp dịch thuật văn bản (Text-to-Text) truyền thống hoặc nhận dạng giọng nói thành văn bản đơn thuần (Speech-to-Text), hệ thống S2ST hướng tới việc tái tạo toàn bộ chu kỳ giao tiếp tự nhiên của con người: lắng nghe giọng nói ở ngôn ngữ nguồn, dịch thuật ngữ nghĩa sang ngôn ngữ đích và tổng hợp lại thành giọng nói tự nhiên ở ngôn ngữ đích. Đặc biệt, đối với cặp ngôn ngữ Anh - Việt, nhu cầu này là vô cùng to lớn tại Việt Nam trong bối cảnh các doanh nghiệp công nghệ trong nước liên tục hội nhập quốc tế, đòi hỏi các cuộc họp song phương diễn ra trơn tru mà không bị gián đoạn bởi các khoảng ngừng dịch thuật thủ công hoặc chi phí đắt đỏ cho biên dịch viên cabin chuyên nghiệp.

#### 1.1.2. Thách thức về độ trễ tích lũy và chất lượng âm phổ tự nhiên của giọng nói tiếng Việt

Mặc dù có nhu cầu thực tiễn rất cao, việc xây dựng và triển khai một hệ thống S2ST thời gian thực song hướng (bidirectional) vẫn đang đối mặt với những thách thức công nghệ rất lớn, cụ thể được phân rã thành hai khía cạnh cốt lõi sau:

##### 1. Độ trễ tích lũy của kiến trúc phân tầng (Cascaded Latency Accumulation)
Một hệ thống S2ST tiêu chuẩn thường được xây dựng theo kiến trúc phân tầng bao gồm ba khối chức năng hoạt động nối tiếp nhau: Nhận dạng tiếng nói (STT) $\rightarrow$ Dịch máy (MT) $\rightarrow$ Tổng hợp tiếng nói (TTS). Mỗi phân tầng này đều tự giới thiệu một khoảng trễ xử lý riêng biệt:
- **Độ trễ STT ($L_{STT}$):** Phụ thuộc vào mô hình Phân đoạn hoạt động giọng nói (VAD) để phát hiện khoảng nghỉ giữa các câu, sau đó là thời gian suy luận của mô hình nhận dạng tiếng nói để xuất ra văn bản.
- **Độ trễ MT ($L_{MT}$):** Thời gian mô hình dịch máy thần kinh chuyển đổi cấu trúc ngữ pháp và từ vựng của văn bản nguồn sang văn bản đích.
- **Độ trễ TTS ($L_{TTS}$):** Thời gian mô hình tổng hợp chuyển đổi văn bản đích thành dữ liệu âm phổ và giải mã thành sóng âm (waveform).
- **Độ trễ mạng ($L_{network}$):** Trễ truyền tải gói tin âm thanh giữa client và server thông qua giao thức truyền thông.

Độ trễ đầu-cuối tổng cộng được xác định theo công thức:

$$L_{total} = L_{STT} + L_{MT} + L_{TTS} + L_{network}$$

Trong các hệ thống S2ST ngây thơ, độ trễ $L_{total}$ có thể dễ dàng vượt quá ngưỡng 4.0 đến 6.0 giây. Khoảng trễ quá lớn này phá hỏng hoàn toàn nhịp điệu hội thoại tự nhiên, gây ra hiện tượng nói đè, nói trùng hoặc tạo ra những khoảng lặng khó xử trong các cuộc họp trực tuyến. Do đó, việc nghiên cứu tối ưu hóa độ trễ ở từng chặng, đặc biệt là cơ chế cắt câu động của VAD và xử lý song song hóa luồng dữ liệu, là một bài toán sống còn.

##### 2. Đặc thù ngôn ngữ và thách thức cắt câu của tiếng Việt
Tiếng Việt là một ngôn ngữ đơn âm tiết, có tính thanh điệu phức tạp (gồm 6 thanh điệu khác nhau). Trong giao tiếp thực tế, người nói thường có xu hướng kéo dài các âm tiết có thanh huyền, thanh hỏi hoặc tạo ra các khoảng dừng nghỉ ngắn tự nhiên giữa các từ để nhấn mạnh ngữ nghĩa. Các mô hình VAD thông thường (như Silero VAD) nếu không được tinh chỉnh phù hợp sẽ dễ dàng nhận nhầm các khoảng ngắt nhịp tự nhiên này là khoảng lặng kết thúc câu, dẫn đến việc kích hoạt lệnh dịch sớm (premature final trigger), làm câu nói bị cắt vụn và mất ngữ cảnh nghiêm trọng ở tầng dịch máy. Ngược lại, các phụ âm cuối trong tiếng Anh hoặc tiếng Việt khi phát âm nhanh thường có năng lượng âm học (energy) rất yếu, dễ bị mô hình VAD hiểu nhầm là nhiễu nền hoặc khoảng lặng và cắt bỏ (tail consonant drop), làm suy giảm độ chính xác nhận dạng của tầng STT từ 95% xuống dưới 80%.

##### 3. Sự thiếu hụt mô hình tổng hợp tiếng nói (TTS) giọng nam Việt chất lượng cao
Trong tầng tổng hợp tiếng nói (TTS), để đảm bảo tính thời gian thực, mô hình cần phải có dung lượng nhẹ để triển khai được trực tiếp tại CPU phía client mà không cần phụ thuộc vào GPU đắt đỏ. Hiện tại, cộng đồng mã nguồn mở (như Rhasspy Piper) chỉ cung cấp các mô hình giọng nữ tiếng Việt khá tốt (như `vi_VN-vais1000-medium`), hoàn toàn thiếu vắng các mô hình giọng nam tiếng Việt có ngữ điệu tự nhiên, rõ chữ và tối ưu hóa dung lượng nhẹ. Việc tự huấn luyện một mô hình TTS giọng nam từ đầu đòi hỏi khối lượng dữ liệu studio khổng lồ (từ 10 đến 20 giờ) và tài nguyên tính toán rất lớn, điều này không khả thi đối với các dự án nghiên cứu có tài nguyên hạn chế. Do đó, việc nghiên cứu các kỹ thuật tinh chỉnh chuyển đổi giới tính giọng nói (Cross-Gender Fine-tuning) từ các checkpoint giọng nữ sẵn có là một khoảng trống nghiên cứu cần được giải quyết.

#### 1.1.3. Ý nghĩa thực tiễn của giải pháp dịch giọng nói thời gian thực song hướng (Anh - Việt)

Đề tài nghiên cứu và phát triển hệ thống dịch giọng nói song hướng Anh - Việt thời gian thực mang lại những giá trị thực tiễn vô cùng to lớn:

1.  **Cung cấp một giải pháp hội thoại xuyên ngôn ngữ độ trễ thấp:** Hệ thống giúp người dùng Việt Nam và các đối tác nói tiếng Anh giao tiếp trực tiếp trong các cuộc họp trực tuyến một cách tự nhiên. Người nói chỉ cần phát âm bình thường, hệ thống sẽ tự động cắt câu thông minh, dịch thuật và phát ra âm thanh dịch sang tai người nghe bên kia với độ trễ tối thiểu (dưới mức nhận thức thông thường).
2.  **Đóng góp mô hình giọng nam tiếng Việt chất lượng cao cho cộng đồng:** Quy trình thực nghiệm tinh chỉnh mô hình Piper TTS giọng nam miền Nam từ tập dữ liệu hạn chế sẽ cung cấp cho cộng đồng nghiên cứu AI tại Việt Nam một mô hình tổng hợp giọng nam có dung lượng cực nhẹ (~32MB sau lượng tử hóa FP16) nhưng vẫn đảm bảo độ tự nhiên và tốc độ suy luận vượt trội trên các CPU máy tính phổ thông.
3.  **Khả năng triển khai thực tế với chi phí tối ưu:** Việc thiết kế hệ thống hoạt động trên kiến trúc Client-Server tối ưu hóa tài nguyên (tận dụng GPU đám mây T4 miễn phí/giá rẻ của Google Colab cho các tác vụ STT/MT nặng và đẩy tác vụ TTS/định tuyến âm thanh về CPU máy khách) chứng minh tính khả thi của việc triển khai ứng dụng thực tế mà không đòi hỏi chi phí đầu tư hạ tầng phần cứng đắt đỏ.
4.  **Giải quyết triệt để các vấn đề nhiễu âm học phòng họp:** Giải pháp cách ly loopback âm thanh qua WASAPI trên Windows giúp loại bỏ hiện tượng vòng lặp phản hồi âm thanh (feedback loop) và tiếng vọng (acoustic echo) mà không cần can thiệp sâu vào quyền quản trị của hệ điều hành, đảm bảo hệ thống có thể tích hợp an toàn và trực tiếp vào bất kỳ phần mềm họp trực tuyến hiện có nào như Zoom hay Google Meet.

### 1.2. Phát biểu bài toán (Problem Statement)

#### 1.2.1. Bài toán nhận dạng tiếng nói (STT) dạng streaming trên luồng âm thanh liên tục không mất ngữ cảnh

Trong hệ thống Speech-to-Speech Translation thời gian thực, chặng đầu tiên là nhận dạng giọng nói (STT) đóng vai trò quyết định đối với chất lượng của toàn bộ pipeline. Trong các hệ thống xử lý offline truyền thống, âm thanh được thu nhận dưới dạng một tệp hoàn chỉnh, sau đó đưa vào mô hình suy luận một lần. Phương pháp này không thể áp dụng cho kịch bản hội thảo trực tuyến thời gian thực do độ trễ quá lớn. Thay vào đó, máy khách (client) phải gửi liên tục các đoạn âm thanh nhỏ (chunk) có thời lượng ngắn (200ms) lên máy chủ (server) thông qua kết nối WebSocket.

Thách thức cốt lõi của nhận dạng tiếng nói dạng streaming là làm sao hiển thị văn bản tạm thời kịp thời (Interim results) để người dùng có phản hồi thị giác tức thì, trong khi vẫn phải đảm bảo độ chính xác tuyệt đối của câu nói khi kết thúc (Final results). Cụ thể, bài toán đặt ra hai khó khăn chính:
1.  **Sự thiếu hụt ngữ cảnh trong suy luận tạm thời (Interim Inference):** Các mô hình Transformer nhận dạng giọng nói mạnh mẽ (như OpenAI Whisper hay Faster-Whisper) không phải là mô hình dạng Transducer suy luận cuốn chiếu theo từng khung. Khi suy luận trên các phân đoạn âm thanh ngắn (~1.5 giây), mô hình thiếu đi ngữ cảnh dài hạn ở phía trước và phía sau, dẫn đến hiện tượng ảo giác (hallucination), lặp từ hoặc nhận dạng sai các từ đồng âm. Hệ thống cần có cơ chế đệm âm thanh và ghi đè thông minh (Interim → Final overwrite) sử dụng cùng một định danh phân đoạn (`segment_id`) để văn bản cuối cùng chỉnh sửa lại các lỗi nhận dạng tạm thời.
2.  **Mất ngữ cảnh liên tục giữa các câu (Inter-utterance Context Loss):** Khi một câu kết thúc và được trigger bởi VAD phát ra kết quả Final, bộ đệm âm thanh được giải phóng để chuẩn bị cho câu tiếp theo. Điều này làm cho mô hình STT hoàn toàn mất đi ngữ cảnh của các câu đã nói trước đó, dẫn đến việc nhận dạng sai các danh từ riêng, thuật ngữ viết tắt của cuộc họp (ví dụ: `"VKU"`, `"WebSocket"`, `"FastAPI"`) hoặc các từ tiếng Anh xen kẽ vốn xuất hiện nhiều lần trong phiên. Hệ thống đòi hỏi một giải pháp chuyển tiếp ngữ cảnh bằng cách sử dụng một bộ đệm trượt lưu giữ văn bản của các câu trước và đưa ngược lại vào mô hình dưới dạng tham số gợi ý âm học (`initial_prompt`), đồng thời phải tắt tính năng tự hồi quy ngữ cảnh của Whisper (`condition_on_previous_text=False`) để tránh rơi vào vòng lặp hallucination vô hạn.

#### 1.2.2. Bài toán dịch máy hội thoại đa ngữ (NMT) bảo toàn tính tự nhiên và ngữ nghĩa của vế nói ngắn

Tầng dịch máy thần kinh (NMT) chịu trách nhiệm dịch thuật ngữ nghĩa từ văn bản nguồn sang văn bản đích. Khác với các tài liệu văn bản viết có cấu trúc ngữ pháp chuẩn chỉnh, ngôn ngữ hội thoại trong các cuộc họp trực tuyến thường có đặc điểm:
-   Câu nói ngắn, không đầy đủ thành phần chủ-vị.
-   Có nhiều từ đệm, từ ngắt quãng hoặc ngắt nghỉ hơi giữa chừng.
-   Cấu trúc câu linh hoạt và thay đổi nhanh chóng.

Nếu mô hình dịch máy (như NLLB-200) thực hiện dịch ngay lập tức mọi cụm từ nhỏ nhận được từ tầng STT (ví dụ khi đoạn văn bản nguồn chỉ có 2-3 từ), kết quả dịch thuật thu được sẽ mang tính dịch thô từng từ (literal translation), rời rạc và hoàn toàn sai lệch về trật tự từ giữa hai cấu trúc ngữ pháp Anh - Việt (SVO của tiếng Anh và tính linh hoạt trong ngữ pháp tiếng Việt). Ví dụ, vế nói ngắn `"I think we should"` nếu dịch riêng rẽ sẽ ra `"Tôi nghĩ chúng tôi nên"`, thiếu đi vị ngữ chính và nghe rất cụ cụt, phá hỏng ngữ điệu khi đưa vào tầng tổng hợp giọng nói TTS tiếp theo.

Do đó, bài toán đặt ra là cần thiết lập một **giải thuật đệm dịch ngắn (Short-MT buffering)** tại bộ quản lý phiên streaming. Thuật toán này có nhiệm vụ trì hoãn việc dịch các phân đoạn văn bản nhỏ hơn một ngưỡng ký tự hoặc số từ nhất định, tạm thời giữ chúng lại để ghép nối với ngữ cảnh của các phân đoạn tiếp theo nhằm nâng cao tính tự nhiên và toàn vẹn ngữ nghĩa của bản dịch. Tuy nhiên, việc đệm dịch lại mâu thuẫn trực tiếp với yêu cầu tối ưu hóa độ trễ. Nếu người nói dừng lại quá lâu mà hệ thống vẫn tiếp tục đợi để ghép câu, độ trễ sẽ tăng lên vô hạn. Vì vậy, hệ thống bắt buộc phải tích hợp một cơ chế giám sát thời gian thực (Watchdog flush) tự động giải phóng bộ đệm và ép dịch sau một khoảng im lặng được calibrate chính xác (ví dụ: 3 giây), đảm bảo bản dịch cuối cùng không bị kẹt lại trong hàng đợi.

#### 1.2.3. Bài toán thiếu hụt mô hình tổng hợp giọng nói (TTS) giọng nam Việt chất lượng cao, dung lượng nhẹ phục vụ thời gian thực

Tầng cuối cùng của hệ thống S2ST là tổng hợp tiếng nói (TTS) từ văn bản dịch. Để hệ thống có thể hoạt động trơn tru trong thời gian thực, độ trễ suy luận của tầng TTS ($L_{TTS}$) cộng với hệ số thời gian thực (Real-Time Factor - RTF) phải luôn duy trì ở mức nhỏ hơn 1.0 (suy luận nhanh hơn tốc độ nói thực tế) ngay trên phần cứng CPU thông thường của máy khách. Các kiến trúc TTS nặng ký như Coqui XTTS v2 dù cho chất lượng tốt nhưng đòi hỏi tài nguyên tính toán GPU rất lớn và dung lượng bộ nhớ VRAM cao, không phù hợp cho việc triển khai đại trà tại máy khách.

Mô hình Piper TTS (dựa trên kiến trúc VITS đầu-cuối) nổi lên như một giải pháp tối ưu nhờ tốc độ suy luận cực nhanh và dung lượng gọn nhẹ. Tuy nhiên, rào cản lớn nhất đối với cặp ngôn ngữ tiếng Việt là:
1.  **Thiếu hụt trầm trọng checkpoint giọng nam Việt chất lượng:** Cộng đồng mã nguồn mở hiện chỉ cung cấp checkpoint giọng nữ miền Nam (`vais1000-medium`). Chưa có bất kỳ mô hình giọng nam tiếng Việt nào đạt độ tự nhiên cao để phục vụ hội thoại chuyên nghiệp.
2.  **Bài toán dữ liệu giới hạn và chi phí huấn luyện:** Huấn luyện một mô hình VITS từ đầu yêu cầu tập dữ liệu đơn phát biểu (single-speaker) sạch sẽ có thời lượng từ 10 đến 20 giờ ghi âm studio và tài nguyên GPU khổng lồ để hội tụ. Bài toán thực tế đòi hỏi phải tận dụng phương pháp **Cross-Gender Fine-tuning** (tinh chỉnh chuyển đổi giới tính giọng nói) từ checkpoint giọng nữ vais1000 sẵn có trên một tập dữ liệu giọng nam cực kỳ hạn chế (chỉ khoảng 2.5 giờ). Kỹ thuật này bắt buộc mô hình phải học cách thay đổi các đặc trưng âm học nhạy cảm với giới tính (như cao độ - pitch, và formant của giọng nam miền Nam) trong khi phải giữ nguyên không gian nhúng âm vị (phoneme embeddings) và thanh điệu tiếng Việt đã học từ mô hình gốc.
3.  **Lượng tử hóa tối ưu hóa phần cứng (Quantization):** Mô hình sau huấn luyện ở dạng FP32 cần phải được chuyển đổi sang ONNX FP16 để giảm dung lượng xuống dưới 35MB và tăng tốc độ suy luận CPU. Tuy nhiên, việc lượng tử hóa VITS thường gặp lỗi load mô hình trên ONNX Runtime do các node ép kiểu ngầm định (`Cast` nodes) xuất ra định dạng FP16 không khớp với mong đợi của đầu vào tiếp theo. Hệ thống cần một bản vá cấu hình lượng tử hóa chính xác (như `op_block_list`) để đảm bảo chất lượng phổ âm (spectrogram) và điểm chất lượng NISQA MOS không bị suy giảm sau khi nén.

#### 1.2.4. Bài toán cô lập luồng âm thanh thu/phát hệ thống chống vòng lặp phản hồi âm thanh (feedback loop)

Trong kịch bản dịch thuật song hướng thời gian thực của một cuộc họp trực tuyến, hệ thống máy khách phải xử lý đồng thời hai luồng âm thanh độc lập nhưng diễn ra song song:
-   **Luồng 0 (Dịch xuôi - VI $\rightarrow$ EN):** Thu âm thanh từ Micro thật của người dùng nội bộ (nói tiếng Việt) $\rightarrow$ Dịch sang tiếng Anh $\rightarrow$ Phát ra cho các thành viên nước ngoài trong cuộc họp nghe.
-   **Luồng 1 (Dịch ngược - EN $\rightarrow$ VI):** Thu âm thanh hệ thống (tiếng nói tiếng Anh của các thành viên nước ngoài phát ra từ phần mềm họp như Zoom/Meet) $\rightarrow$ Dịch sang tiếng Việt $\rightarrow$ Phát ra loa vật lý/tai nghe của người dùng nội bộ.

Mối nguy hiểm lớn nhất và là nguyên nhân gây đổ vỡ toàn bộ hệ thống âm thanh là **vòng lặp phản hồi âm thanh (feedback loop)** hay tiếng vọng âm học (acoustic echo). Nếu âm thanh dịch tiếng Việt của Luồng 1 (phát ra loa vật lý để người dùng nội bộ nghe) bị thu ngược lại bởi chính Micro của người dùng đó, hệ thống STT sẽ hiểu nhầm đó là giọng nói mới, tiếp tục gửi lên server dịch ngược lại tiếng Anh và phát ra cuộc họp. Quá trình này lặp đi lặp lại vô hạn, tạo ra một vòng lặp dịch thuật hỗn loạn và tiếng hú lớn do cộng hưởng âm học.

Để giải quyết triệt để bài toán này, hệ thống bắt buộc phải triển khai một cơ chế **cô lập âm thanh vật lý và ảo (Audio Routing Isolation)** ở tầng máy khách Windows:
1.  **Cách ly thiết bị phát Luồng 1:** Âm thanh dịch tiếng Việt dành cho người dùng nội bộ nghe phải được phát trực tiếp ra loa ngoài hoặc tai nghe vật lý của họ, và micro của họ phải được cấu hình định hướng hoặc giảm nhạy để tránh thu lại âm thanh này.
2.  **Cách ly và định tuyến Luồng 0 qua thiết bị ảo:** Âm thanh dịch tiếng Anh dành cho đối tác nước ngoài phải được định tuyến ngầm vào đầu vào của một trình điều khiển âm thanh ảo (VB-Audio Virtual Cable Input). Phần mềm họp trực tuyến (Zoom/Meet) tại máy khách sẽ chọn đầu ra ảo tương ứng (CABLE Output) làm thiết bị Micro đầu vào của nó. Nhờ đó, luồng dịch thuật được "bơm" trực tiếp vào luồng thoại của cuộc họp dưới dạng tín hiệu số sạch sẽ, tách biệt hoàn toàn với loa vật lý của máy khách và không bị thu lại bởi các trình ghi âm hệ thống (system loopback recorder) vốn chỉ ghi nhận kênh âm thanh hệ thống chính.
3.  **Thu âm hệ thống không cần đặc quyền Administrator:** Việc ghi nhận âm thanh hệ thống để dịch ngược (Luồng 1) phải được triển khai thông qua API ghi âm loopback WASAPI (Windows Audio Session API) chỉ nhắm mục tiêu vào thiết bị phát mặc định của cuộc họp, đảm bảo chương trình hoạt động ổn định trên các máy tính người dùng phổ thông mà không yêu cầu quyền Admin để cấu hình card âm thanh phức tạp.

---

### 1.3. Mục tiêu và Đóng góp của đề tài

#### 1.3.1. Thiết lập hệ thống S2ST thời gian thực song hướng tối ưu hóa độ trễ cumulative

Mục tiêu hàng đầu của đề tài là xây dựng một hệ thống dịch giọng nói sang giọng nói thời gian thực (S2ST) song hướng hoàn chỉnh cho cuộc họp trực tuyến Anh - Việt, đảm bảo giảm thiểu tối đa độ trễ cumulative đầu-cuối xuống mức dưới ngưỡng nhận nhận thức tự nhiên của con người. Để đạt được mục tiêu này, đồ án đã mang lại các đóng góp cụ thể về mặt thiết kế hệ thống và thuật toán:

1.  **Thiết kế Pipeline bất đồng bộ đa luồng trên Server FastAPI:** Chuyển đổi toàn bộ luồng xử lý từ dạng khối đồng bộ (batch) sang luồng streaming liên tục thông qua giao thức WebSocket. Phát triển bộ quản lý phiên truyền phát `StreamingSTTSessionManager` tích hợp sâu mô hình phân đoạn *Silero VAD* chạy trực tiếp trên máy chủ.
2.  **Giải thuật tối ưu hóa độ trễ chặng giữa (STT-MT-TTS Parallelism):** Thay vì xử lý tuần tự chặn luồng, đồ án triển khai kiến trúc song song hóa *Execution Lane* (sử dụng thread pool executor kết hợp khóa thao tác `operation_lock` trên từng entry) giúp cô lập tài nguyên tính toán GPU VRAM. Triển khai giải thuật *Preload & Warmup* lúc FastAPI startup, loại bỏ hoàn toàn độ trễ khởi động lạnh (cold-start latency) lần đầu từ 60-90 giây xuống 0 giây.
3.  **Thuật toán cắt câu động và đệm dịch thông minh:**
    -   *VAD Hangover (400ms):* Giữ lại 2 khung âm thanh tĩnh sau khi phát hiện khoảng lặng để bảo toàn các phụ âm gió/phụ âm cuối yếu của người nói, ngăn chặn lỗi dịch cụt.
    -   *Short-MT Buffering & Watchdog (3s):* Tạm hoãn dịch vế nói quá ngắn dưới 4 từ để tăng tính tự nhiên ngữ nghĩa, và tự động xả hàng đợi dịch sau 3 giây im lặng để bảo toàn trễ nhận thức đầu ra (Time-To-First-Audio - TTFA).
    -   *Comma Fallback Splitter:* Tự động ngắt dấu câu mềm trên kết quả dịch giúp bộ tổng hợp TTS phát âm cuốn chiếu song song với chặng dịch tiếp theo.

#### 1.3.2. Nghiên cứu phương pháp Cross-Gender Fine-tuning Piper TTS tạo giọng nam miền Nam Việt chất lượng từ dataset giới hạn

Đóng góp khoa học quan trọng nhất của đồ án ở tầng tổng hợp tiếng nói (TTS) là nghiên cứu và thực nghiệm thành công phương pháp **Cross-Gender Fine-tuning** (huấn luyện chuyển giới tính giọng nói từ checkpoint nữ sang nam) dựa trên kiến trúc nén VITS của mô hình *Rhasspy Piper*, khắc phục tình trạng thiếu hụt tài nguyên mô hình giọng nam tiếng Việt trên cộng đồng.
Các đóng góp chi tiết bao gồm:

1.  **Quy trình chuẩn hóa dữ liệu & Kiểm soát chất lượng STT QC:** Xây dựng quy trình xử lý âm thanh tự động (resample 22.05kHz, chuẩn hóa độ to -23 LUFS và trim khoảng lặng). Ứng dụng mô hình *PhoWhisper-large* thực hiện nhận dạng kiểm định chéo văn bản trên 1999 clips của tập dữ liệu *VieNeu-TTS-140h*, đề xuất bộ lọc *Per-Speaker Hybrid Filter* giúp loại bỏ sạch sẽ 499 clips lỗi lệch pha (offset error) để tạo ra tập dữ liệu 1500 clips (~2.5h) sạch hoàn toàn.
2.  **Giải pháp 2-Pass Phoneme Mapping Workaround:** Thiết kế giải pháp căn chỉnh và đồng bộ hóa âm vị 2 bước để bypass hạn chế của thư viện *piper-train*, giải quyết triệt để lỗi Index Out of Bounds của mô hình VITS khi gặp các âm vị latin lạ từ các từ tiếng Anh xen kẽ trong văn bản tiếng Việt.
3.  **Lượng tử hóa tối ưu hóa CPU:** Triển khai quy trình lượng tử hóa FP16 cho mô hình Piper ONNX, đóng gói thành công tệp mô hình siêu nhẹ chỉ **32MB** (giảm 50% so với bản gốc 63MB) mà không làm suy giảm điểm chất lượng khách quan (NISQA MOS) và hệ số thời gian thực (RTF) trên CPU.

#### 1.3.3. Xây dựng giải pháp định tuyến âm thanh ảo cô lập loopback chống lặp tiếng không cần can thiệp Admin hệ thống

Đóng góp thực tiễn nổi bật ở phía máy khách (Client PySide6) là thiết kế giải pháp cách ly và định tuyến luồng âm thanh hai chiều hoàn toàn tự động trên hệ điều hành Windows, triệt tiêu triệt để hiện tượng vòng lặp phản hồi âm thanh (feedback loop) mà không cần can thiệp quyền Admin.
Các giải pháp kỹ thuật cụ thể gồm:

1.  **Nhận diện thiết bị âm thanh ảo không đặc quyền (Admin-free Detection):** Viết module quét driver âm thanh ảo ngầm thông qua thư viện PyAudio (`is_vb_cable_installed`), kiểm tra sự hiện diện của driver **VB-Audio Virtual Cable** bằng cơ chế lọc chuỗi từ khóa mà không cần truy vấn Registry Windows (vốn yêu cầu quyền Administrator).
2.  **Thiết kế bộ phát âm thanh đa lộ tuyến (RoutePlayer):** Xây dựng bộ điều phối âm thanh `RoutePlayer` quản lý song song hai luồng phát `AdaptiveJitterPlayer`:
    -   *Route 0 (Dịch Việt $\rightarrow$ Anh):* Định tuyến và đẩy dữ liệu âm thanh số vào cổng phát ảo "CABLE Input" để làm micro ảo cấp cho Zoom/Google Meet (các thành viên cuộc họp nghe).
    -   *Route 1 (Dịch Anh $\rightarrow$ Việt):* Phát trực tiếp ra loa/tai nghe mặc định để người dùng nội bộ nghe.
3.  **Bộ thu âm Loopback WASAPI an toàn:** Triển khai lớp ghi âm `LoopbackCaptureService` gọi API âm thanh WASAPI trực tiếp trên thiết bị đầu ra mặc định của hệ thống với cờ `include_loopback=True`. Điều này giúp ứng dụng thu lại chính xác tiếng đối tác phát ra từ cuộc họp trực tuyến mà không bị lẫn tạp âm phòng hay tiếng nói của người dùng nội bộ, đảm bảo tính cô lập tuyệt đối của vòng lặp dịch thuật.

### 1.4. Đối tượng và Phạm vi nghiên cứu

#### 1.4.1. Đối tượng công nghệ cốt lõi

Đồ án tập trung nghiên cứu, tối ưu hóa và tích hợp các công nghệ trí tuệ nhân tạo hiện đại trong lĩnh vực xử lý tiếng nói và ngôn ngữ tự nhiên:

1.  **Nhận dạng tiếng nói (STT):**
    -   **Faster-Whisper:** Bản tái triển khai mô hình *OpenAI Whisper* sử dụng thư viện *CTranslate2*. Công nghệ này áp dụng các kỹ thuật tối ưu hóa bộ nhớ và tính toán (như lượng tử hóa trọng số, hợp nhất các phép toán chú ý - attention fusion), giúp tăng tốc độ suy luận gấp 4 lần so với mô hình gốc mà không làm suy giảm độ chính xác nhận dạng.
    -   **PhoWhisper:** Mô hình nhận dạng tiếng nói chuyên biệt cho tiếng Việt được huấn luyện bởi VinAI. Với quy mô 1.55 tỷ tham số và được tinh chỉnh trên 844 giờ dữ liệu tiếng Việt thực tế, PhoWhisper mang lại khả năng xử lý vượt trội đối với các đặc thù về giọng vùng miền (Bắc, Trung, Nam) và các từ mượn trong tiếng Việt.
2.  **Dịch máy thần kinh (NMT):**
    -   **NLLB-200 (No Language Left Behind):** Mô hình dịch máy đa ngôn ngữ thế hệ mới của Meta AI, hỗ trợ dịch thuật trực tiếp giữa 200 ngôn ngữ mà không cần thông qua ngôn ngữ trung gian (English pivot). Đồ án sử dụng mô hình NLLB-200 được lượng tử hóa dưới thư viện *CTranslate2* để tối ưu hóa tài nguyên VRAM và tăng tốc độ dịch thời gian thực cho cặp ngôn ngữ Anh (`eng_Latn`) - Việt (`vieu_Latn`).
3.  **Tổng hợp tiếng nói (TTS):**
    -   **Kiến trúc VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech):** Mô hình tổng hợp tiếng nói đầu-cuối kết hợp mạng biến phân tự động điều kiện (Conditional VAE), luồng chuẩn hóa (Normalizing Flows) và mạng đối nghịch tạo sinh (GAN) để sinh trực tiếp sóng âm (waveform) từ văn bản mà không cần thông qua mel-spectrogram trung gian.
    -   **espeak-ng:** Thư viện mã nguồn mở chuyển đổi văn bản sang âm vị (grapheme-to-phoneme - G2P), đóng vai trò bộ mã hóa tiền xử lý văn bản cho mô hình VITS.
    -   **Piper TTS:** Bộ suy luận TTS siêu tốc tối ưu hóa bằng C++ chạy trực tiếp trên CPU, cho phép tổng hợp tiếng nói với hệ số thời gian thực RTF cực thấp.
4.  **Phân đoạn giọng nói (VAD):**
    -   **Silero VAD:** Mô hình mạng thần kinh nhân tạo siêu nhẹ (~1.8MB ở định dạng JIT/ONNX) chuyên biệt cho tác vụ phát hiện hoạt động tiếng nói, có độ trễ cực thấp (<1ms) và hoạt động ổn định trên cả CPU.

#### 1.4.2. Phạm vi triển khai thực nghiệm

Nghiên cứu được giới hạn và triển khai thực nghiệm trong phạm vi môi trường kỹ thuật sau:

1.  **Phía Máy chủ (Server Layer):**
    -   **Nền tảng:** Triển khai trên môi trường điện toán đám mây *Google Colab Pro* sử dụng GPU đơn **Nvidia Tesla T4 (16 GB VRAM, kiến trúc Turing)** kết hợp với môi trường ảo Python 3.10 ổn định.
    -   **Giao thức truyền thông:** Sử dụng máy chủ Web dịch vụ *FastAPI*, thiết lập kết nối song công thông qua giao thức **WebSocket** (`/ws`) để truyền tải đồng thời các khung dữ liệu nhị phân (audio chunks) và khung điều khiển JSON.
2.  **Phía Máy khách (Client Layer):**
    -   **Hệ điều hành:** Chạy trực tiếp trên hệ điều hành **Microsoft Windows 10/11** vật lý để kiểm thử tính tương thích của driver âm thanh và giao tiếp phần cứng thực tế.
    -   **Ứng dụng Giao diện:** Thiết lập ứng dụng đồ họa GUI sử dụng thư viện **PySide6** (Python Qt6), tích hợp vòng lặp sự kiện bất đồng bộ qua thư viện `qasync` để đồng bộ hóa luồng giao diện UI và luồng thu phát âm thanh.
    -   **Định tuyến âm thanh:** Sử dụng thư viện *PyAudio* và *soundcard* để kết nối với driver ảo **VB-Audio Virtual Cable** và API **WASAPI loopback** trên card âm thanh vật lý của máy tính máy khách.

### 1.5. Bố cục của Báo cáo Đồ án tốt nghiệp

#### 1.5.1. Tóm tắt nội dung chính từ Chương 1 đến Chương 5

Nội dung báo cáo Đồ án tốt nghiệp Kỹ sư AI được cấu trúc thành 5 chương chính với các nội dung tóm tắt cụ thể như sau:

*   **CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI:** Trình bày bối cảnh, lý do lựa chọn đề tài dịch giọng nói song hướng Anh - Việt thời gian thực (S2ST). Phát biểu chi tiết bốn bài toán nghiên cứu chính (độ trễ tích lũy, đặc thù ngắt câu tiếng Việt, thiếu hụt giọng nam tổng hợp và vòng lặp phản hồi âm học). Xác lập mục tiêu, các đóng góp kỹ thuật cốt lõi và phạm vi nghiên cứu thực nghiệm của đề tài.
*   **CHƯƠNG 2. TỔNG QUAN TÀI LIỆU VÀ CƠ SỞ LÝ THUYẾT:** Hệ thống hóa toàn bộ nền tảng lý thuyết liên quan đến hệ thống S2ST. Phân tích nguyên lý mạng Transformer trong nhận dạng giọng nói (Whisper, PhoWhisper), cấu trúc dịch máy đa ngôn ngữ (NLLB-200) và tối ưu suy luận CTranslate2. Nghiên cứu sâu toán học của mô hình tổng hợp tiếng nói đầu-cuối *VITS* (Posterior/Prior Encoder, Normalizing Flows, HiFi-GAN Decoder và đối nghịch Discriminators) cùng thuật toán phát hiện hoạt động giọng nói *Silero VAD*. Chỉ ra các nghiên cứu liên quan và khoảng trống công nghệ hiện tại.
*   **CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT:** Chi tiết hóa thiết kế kiến trúc hệ thống Client-Server sử dụng kết nối song công WebSocket và định dạng khung truyền tải dữ liệu. Trình bày thiết kế Client PySide6 kết hợp giải pháp cách ly WASAPI loopback và định tuyến RoutePlayer tự động nhận diện VB-Cable. Chi tiết hóa kiến trúc FastAPI Server với mô hình thiết kế *Polymorphic Facade Pattern* đồng bộ 3 AI Engine và các giải thuật tối ưu độ trễ (VAD Hangover, Short-MT Buffering, Comma Fallback Splitter). Đề xuất quy trình thực nghiệm Cross-Gender Fine-tuning Piper TTS giọng nam Việt và giải pháp đồng bộ hóa âm vị 2-Pass.
*   **CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ:** Mô tả môi trường phần cứng, giải pháp đóng gói môi trường ảo và quy trình tiền xử lý tập dữ liệu VieNeu-TTS-140h bằng kiểm định chéo STT QC. Trình bày các chỉ số đo đạc hiệu năng khách quan (Mel loss, KL loss, WER, RTF, trễ telemetry đầu-cuối) và khảo sát chủ quan Human MOS cùng mô hình học sâu NISQA MOS. Phân tích so sánh kết quả thực nghiệm hệ thống client, so sánh chất lượng mô hình Piper FP32 và bản lượng tử hóa FP16, đối## CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT

### 3.1. Thiết kế Hệ thống Tổng quát và Quy trình Kết nối

#### 3.1.1. Luồng dữ liệu S2ST song hướng thời gian thực

Hệ thống dịch giọng nói sang giọng nói thời gian thực song hướng (Speech-to-Speech Translation - S2ST) được thiết kế theo mô hình kiến trúc phân tán Máy khách - Máy chủ (Client-Server). Việc phân bổ tài nguyên tính toán được tối ưu hóa bằng cách đẩy các tác vụ nhận dạng (STT) và dịch thuật (MT) có độ phức tạp tính toán lớn lên GPU NVIDIA Tesla T4 của máy chủ Cloud. Ngược lại, chặng tổng hợp giọng nói (TTS) nhờ sử dụng mô hình ONNX siêu nhẹ sẽ được đẩy về thực thi trực tiếp tại CPU của máy khách local. Thiết kế này giúp triệt tiêu hoàn toàn độ trễ truyền tải băng thông âm thanh chặng cuối trên mạng internet, đồng thời đảm bảo khả năng đáp ứng song song cho nhiều người dùng.

Để liên kết các chặng xử lý và truyền nhận âm thanh liên tục, hệ thống sử dụng giao thức kết nối song công **WebSocket** (`/ws`). Sơ đồ luồng dữ liệu hai chiều (dịch xuôi Luồng 0 và dịch ngược Luồng 1) được thiết kế và mô tả chi tiết như sau:

```mermaid
sequenceDiagram
    autonumber
    actor User as Người dùng nội bộ (VI)
    participant Client as Ứng dụng PySide6 (Windows)
    participant WS as Kênh WebSocket (Song công)
    participant Server as Server FastAPI (GPU T4 Cloud)
    actor Partner as Đối tác nước ngoài (EN)

    %% Luồng dịch xuôi (VI -> EN)
    Note over User, Partner: LUỒNG 0: DỊCH XUÔI (VI -> EN)
    User->>Client: Nói tiếng Việt
    Client->>Client: Ghi âm Micro vật lý (PCM16 16kHz Mono, chunk 200ms)
    Client->>WS: Gửi khung nhị phân 0x02 (chứa timestamp + audio chunk)
    WS->>Server: Truyền tải streaming thời gian thực
    Server->>Server: Phân đoạn Silero VAD -> Trích xuất cụm thoại (utterance)
    Server->>Server: Nhận dạng PhoWhisper -> Văn bản tiếng Việt
    Server->>WS: Trả kết quả JSON stt.final
    WS->>Client: Hiển thị văn bản gốc tiếng Việt lên giao diện
    Server->>Server: Dịch máy NLLB-200 -> Văn bản tiếng Anh
    Server->>WS: Trả kết quả JSON mt.result
    WS->>Client: Hiển thị văn bản dịch tiếng Anh
    Client->>Client: Suy luận Piper TTS trên CPU -> Khung sóng âm tiếng Anh
    Client->>Client: RoutePlayer (Route 0) -> Đẩy vào thiết bị phát ảo VB-Cable Input
    Client->>Partner: Trình hội thoại (Zoom/Meet) đọc CABLE Output làm Mic -> Loa đối tác

    %% Luồng dịch ngược (EN -> VI)
    Note over User, Partner: LUỒNG 1: DỊCH NGƯỢC (EN -> VI)
    Partner->>Client: Nói tiếng Anh qua Zoom/Meet
    Client->>Client: WASAPI Loopback Capture (Thu âm hệ thống PCM16 16kHz)
    Client->>WS: Gửi khung nhị phân 0x02 (Định vị Route 1 + audio chunk)
    WS->>Server: Truyền tải streaming thời gian thực
    Server->>Server: Phân đoạn Silero VAD -> Trích xuất cụm thoại (utterance)
    Server->>Server: Nhận dạng Faster-Whisper -> Văn bản tiếng Anh
    Server->>WS: Trả kết quả JSON stt.final (tiếng Anh)
    WS->>Client: Hiển thị văn bản đối tác lên giao diện
    Server->>Server: Dịch máy NLLB-200 -> Văn bản tiếng Việt
    Server->>WS: Trả kết quả JSON mt.result (tiếng Việt)
    WS->>Client: Hiển thị văn bản dịch tiếng Việt
    Client->>Client: Suy luận Piper TTS trên CPU -> Khung sóng âm tiếng Việt (Nam)
    Client->>Client: RoutePlayer (Route 1) -> Phát ra Loa/Tai nghe vật lý của Người dùng
```

#### 3.1.2. Cơ chế đồng bộ hóa thời gian và luồng truyền tải dữ liệu

Để giải quyết bài toán đồng bộ hóa và đo lường hiệu năng của hệ thống S2ST thời gian thực, quy trình truyền tải dữ liệu được thiết kế tập trung vào việc theo dõi dòng thời gian (timeline tracking) và phối hợp bất đồng bộ giữa máy khách và máy chủ.

##### 1. Quy trình đồng bộ hóa dòng thời gian
Khi ứng dụng máy khách ghi âm từ Micro vật lý hoặc card âm thanh hệ thống (WASAPI Loopback), luồng âm thanh PCM được chia cắt thành các phân đoạn ngắn (chunk) 200ms. Để đo đạc chính xác độ trễ tích lũy chặng mạng và chặng xử lý mà không bị ảnh hưởng bởi sự lệch múi giờ giữa client và server, quy trình đồng bộ hóa dòng thời gian được thiết lập như sau:
1.  **Gắn nhãn thời gian tại nguồn (Client-side Timestamping):** Trước khi gửi mỗi chunk âm thanh đi qua kênh WebSocket, máy khách ghi nhận một nhãn thời gian có độ chính xác cao $t_{client\_send}$ (độ chính xác micro-giây). Nhãn thời gian này được đóng gói trực tiếp vào phần đầu (header) của gói tin truyền phát.
2.  **Đo đạc telemetry trên máy chủ:** Khi máy chủ nhận được gói tin, nó ghi nhận nhãn thời gian $t_{server\_recv}$. Khi quá trình suy luận nhận dạng (STT) hoặc dịch thuật (MT) hoàn tất, máy chủ trả về kết quả kèm theo chính xác nhãn thời gian gốc $t_{client\_send}$ và thời gian xử lý nội bộ của máy chủ $L_{proc\_server}$.
3.  **Tính toán độ trễ mạng hai chiều (RTT Latency):** Phía máy khách khi nhận được kết quả cuối cùng từ WebSocket sẽ đối chiếu thời điểm hiện tại $t_{client\_recv}$ với nhãn thời gian gốc để xác định tổng trễ chặng mạng $L_{network}$ và trễ suy luận thực tế:
    $$L_{network} = (t_{client\_recv} - t_{client\_send}) - L_{proc\_server}$$
    Chỉ số này được đẩy về module telemetry `pipeline.metric` của máy khách để thống kê hiệu năng hệ thống theo thời gian thực.

##### 2. Quy trình phối hợp luồng dữ liệu (Data Coordination Flow)
Để tránh tình trạng chồng chéo dữ liệu văn bản hiển thị khi người dùng nói liên tục, hệ thống áp dụng cơ chế đánh chỉ số phân đoạn (`segment_id`) và nhãn phân tuyến (`route_id`):
*   **Phân tuyến luồng dịch:** Byte định danh `Route ID` (giá trị `0` cho luồng dịch xuôi và `1` cho luồng dịch ngược) giúp bộ định tuyến của máy chủ phân phối dữ liệu âm thanh đến đúng luồng quản lý độc lập, ngăn ngừa sự lẫn lộn giữa tiếng nói của người dùng nội bộ và đối tác nước ngoài.
*   **Đồng bộ hóa kết quả tạm thời (Interim) và chính thức (Final):** Trong khi người nói đang nói, chặng STT liên tục cập nhật kết quả tạm thời dựa trên cùng một `segment_id`. Khi VAD kích hoạt tín hiệu kết thúc câu thoại, máy chủ gửi gói tin đánh dấu trạng thái chính thức (`stt.final`). Cơ chế này giúp giao diện máy khách hiển thị văn bản cập nhật cuốn chiếu (chèn đè nội dung tạm thời) và chỉ khóa dữ liệu khi nhận được tín hiệu chính thức, đảm bảo tính trực quan và chính xác cho giao diện người dùng.

#### 3.1.3. Cơ chế định tuyến bất đồng bộ Mode-Dispatch và Quản lý Session State

Quy trình quản lý phiên dịch thuật tại máy chủ FastAPI được vận hành thông qua lớp đối tượng `SessionState`. Lớp này hoạt động như một kho lưu trữ trạng thái bất đồng bộ của kết nối WebSocket hiện hành, lưu giữ thông tin cấu hình ngôn ngữ, bộ đệm âm thanh tạm thời và hàng đợi kết quả đầu ra (`outbound_queue`).

Quy trình định tuyến và quản lý tài nguyên tính toán trên máy chủ được thiết kế theo 3 cấu trúc kỹ nghệ cốt lõi nhằm tối ưu hóa hiệu năng suy luận:

##### 1. Thiết kế Facade đa hình (Polymorphic Facade Pattern)
Để chuẩn hóa giao tiếp giữa luồng xử lý WebSocket và các mô hình học sâu bên dưới, cả ba chặng STT, MT, và TTS đều được bao bọc bởi các lớp Facade kế thừa từ một giao ước chung (Contract). Quy trình suy luận được thực hiện qua các phương thức bất đồng bộ `load_async()` và `infer_async()`. Cách tiếp cận này giúp cô lập logic xử lý luồng khỏi chi tiết cài đặt của từng thư viện (như Faster-Whisper hay PhoWhisper), cho phép cắm-và-chạy (Plug-and-play) các mô hình AI khác nhau mà không phải thay đổi cấu trúc lõi của server.

##### 2. Bộ điều phối luồng song song (Execution Lane Flow)
GPU NVIDIA Tesla T4 có dung lượng VRAM giới hạn và không hỗ trợ thực thi đồng thời nhiều tác vụ tính toán ma trận lớn từ nhiều luồng PyTorch khác nhau mà không bị suy giảm hiệu năng hoặc lỗi tràn bộ nhớ (CUDA OOM). Quy trình xử lý song song được thiết kế như sau:
*   Hệ thống thiết lập các tuyến thực thi độc lập (`ExecutionLane`) tương ứng với từng tác vụ STT, MT, TTS.
*   Mỗi thực thể mô hình trong lane được bảo vệ bởi một khóa loại trừ tương hỗ (`operation_lock`).
*   Khi có chunk âm thanh hoặc văn bản cần xử lý, tác vụ được nạp vào một Thread Pool chuyên biệt của Python và phải xếp hàng chờ nhận khóa `operation_lock`.
*   Quy trình này tuần tự hóa việc truy cập vào GPU VRAM, ngăn chặn hiện tượng tranh chấp tài nguyên tính toán của card đồ họa, bảo vệ tính ổn định của server khi xử lý đa luồng.

##### 3. Quy trình Khởi động nóng (Preload & Warmup Workflow)
Để giải quyết độ trễ khởi động lạnh (cold-start latency) lên tới 15 - 20 giây ở lần suy luận đầu tiên (do mô hình cần thời gian nạp các tensor từ ổ đĩa vào VRAM và khởi tạo nhân CUDA), hệ thống áp dụng quy trình khởi động nóng tại sự kiện `startup` của FastAPI:
1.  **Tải trước (Preload):** Nạp toàn bộ các mô hình (PhoWhisper, Faster-Whisper, NLLB-200, các voice của Piper TTS) vào bộ nhớ VRAM ngay khi máy chủ bắt đầu chạy.
2.  **Chạy giả lập (Warmup):** Gửi các tensor rỗng (zeros tensor) hoặc chuỗi văn bản giả định qua các facade `infer_async()` để ép GPU khởi tạo sẵn các đồ thị tính toán (execution graphs) và nhân CUDA.
3.  **Sẵn sàng vận hành:** Sau khi hoàn tất quá trình khởi động nóng, hệ thống mới mở cổng WebSocket tiếp nhận kết nối từ client. Toàn bộ các yêu cầu dịch thuật đầu tiên của người dùng sẽ đạt được tốc độ suy luận tối ưu ngay lập tức.

---

### 3.2. Nhận dạng Tiếng nói Streaming và Trực quan hóa Văn bản (Bài toán 1)

#### 3.2.1. Quy trình phân đoạn giọng nói động Silero VAD và Hangover Frame

Nhận dạng tiếng nói streaming trên luồng âm thanh liên tục yêu cầu một cơ chế phân đoạn thông minh để xác định chính xác thời điểm bắt đầu và kết thúc câu nói của người dùng, làm cơ sở nạp dữ liệu vào mô hình nhận dạng. Quy trình xử lý tín hiệu âm thanh thô qua bộ lọc hoạt động giọng nói (Voice Activity Detection - VAD) được thiết kế như sau:

```
[Audio Chunk 200ms] ──> [Chuẩn hóa biên độ] ──> [Suy luận Silero VAD]
                                                         │
                                        ┌────────────────┴────────────────┐
                                        ▼ P_speech > 0.5                  ▼ P_speech <= 0.5
                                 [Trạng thái SPEECH]               [Trạng thái SILENCE]
                                        │                                 │
                                [Nạp vào bộ đệm câu]             [Đếm khung im lặng]
                                                                          │
                                                         ┌────────────────┴────────────────┐
                                                         ▼ Khung lặng < Threshold          ▼ Khung lặng >= Threshold (450ms)
                                                  [Tiếp tục ghi nhận]               [Trigger stt.final & Gửi đi]
                                                                                    [Ghép thêm 2 Hangover Frames]
```

##### 1. Quy trình phân lớp trạng thái âm thanh
Tín hiệu âm thanh PCM 16kHz ghi nhận từ máy khách được đưa vào mô hình mạng thần kinh nhân tạo siêu nhẹ **Silero VAD** theo từng chu kỳ 200ms. Mô hình tính toán xác suất có chứa tiếng nói $P_{speech}$ trong đoạn âm thanh:
*   Nếu $P_{speech} > \theta_{VAD}$ (với ngưỡng kích hoạt $\theta_{VAD} = 0.5$), phân đoạn được gắn nhãn là hoạt động tiếng nói (`SPEECH`). Hệ thống bắt đầu đẩy dữ liệu âm thanh vào bộ đệm của phân đoạn hiện tại.
*   Nếu $P_{speech} \le \theta_{VAD}$, phân đoạn được gắn nhãn là khoảng lặng (`SILENCE`). Hệ thống tăng biến đếm số khung im lặng liên tục.

##### 2. Thuật toán cắt câu động điểm ngọt ngào (Sweet Spot VAD)
Để xác định thời điểm người nói kết thúc câu thoại thực tế nhằm phát lệnh dịch, hệ thống sử dụng hằng số cấu hình `SILENCE_THRESHOLD_FRAMES`. Qua các thực nghiệm tối ưu hóa trải nghiệm hội thoại, giá trị này được calibrate ở mức **2.25 khung** (tương đương với $2.25 \times 200\text{ms} = 450\text{ms}$):
*   Khi biến đếm khung im lặng vượt qua ngưỡng 450ms, hệ thống sẽ trigger trạng thái kết thúc câu (`stt.final`), đóng bộ đệm âm thanh hiện tại và gửi toàn bộ phân đoạn sang mô hình STT để nhận dạng chính thức.
*   Ngưỡng **450ms** được lựa chọn làm "điểm ngọt ngào" vì nó phản ánh chính xác khoảng dừng lấy hơi tự nhiên của người Việt giữa các câu nói độc lập. Nếu đặt quá ngắn (<400ms), câu nói sẽ bị băm nhỏ; nếu đặt quá dài (>500ms), trễ phản hồi của hệ thống sẽ tăng lên rõ rệt gây cảm giác gián đoạn.

##### 3. Quy trình bù khung âm thanh (Hangover Frame Workflow)
Để giải quyết bài toán mất phụ âm cuối (tail consonant drop) do năng lượng âm học của các phụ âm gió ở cuối câu nói (như /s/, /t/, /z/) thường giảm xuống rất thấp khiến bộ lọc VAD hiểu lầm là khoảng lặng và cắt bỏ sớm, hệ thống áp dụng cơ chế bù khung **Hangover Frame**:
*   Khi bộ đếm im lặng đạt ngưỡng trigger kết thúc câu, hệ thống không cắt bỏ phân đoạn âm thanh tại đúng thời điểm đó.
*   Hệ thống tiếp tục giữ lại và trích xuất thêm `HANGOVER_FRAMES = 2` khung âm thanh tiếp theo (tương đương 400ms âm thanh tĩnh) để ghép nối vào đuôi của bộ đệm âm thanh hiện tại.
*   Toàn bộ phân đoạn âm thanh mở rộng này mới được chuyển giao cho mô hình Whisper nhận dạng. Cơ chế này đảm bảo bảo toàn toàn vẹn đặc trưng âm phổ chặng cuối của từ cuối cùng trong câu thoại, giúp nâng cao độ chính xác nhận dạng STT.

#### 3.2.2. Quy trình nhận dạng tiếng nói bất đồng bộ và cơ chế đệm trượt ngữ cảnh

Sau khi phân đoạn âm thanh được tạo ra bởi bộ lọc VAD, quy trình nhận dạng tiếng nói được kích hoạt bất đồng bộ trên máy chủ thông qua lớp facade `STTEngine`. Hệ thống áp dụng **Faster-Whisper** cho luồng nhận dạng tiếng Anh và mô hình **PhoWhisper-medium-ct2** lượng tử hóa cho luồng tiếng Việt để đạt độ chính xác tối ưu cho từng ngôn ngữ mục tiêu.

Quy trình nhận dạng tiếng nói và đồng bộ ngữ cảnh được mô tả qua các bước sau:

##### 1. Quy trình suy luận nhận dạng
*   **Tiền xử lý phổ âm:** Đoạn âm thanh PCM thô nhận được từ WebSocket được chuyển đổi sang đặc trưng Log-Mel Spectrogram với 80 kênh tần số.
*   **Suy luận Encoder-Decoder:** Log-Mel Spectrogram được đưa qua các lớp tích chập của Encoder để nén chiều thời gian, sau đó Decoder tự hồi quy thực hiện chú ý chéo (Cross-Attention) để sinh ra chuỗi ký tự văn bản nguồn.

##### 2. Quy trình đệm trượt ngữ cảnh (Contextual Prompt Workflow)
Do bộ đệm âm thanh của mô hình STT bắt buộc phải giải phóng sau mỗi lần trigger câu thoại chính thức (`stt.final`) để giải tỏa bộ nhớ và ngăn trễ tích lũy, mô hình STT sẽ bị mất ngữ cảnh của các câu đã nói trước đó. Để khắc phục hiện trạng này, hệ thống thiết lập quy trình đệm trượt ngữ cảnh bất đồng bộ:
1.  **Lưu trữ văn bản lịch sử:** Mỗi khi chặng STT xuất ra một văn bản chính thức hoàn chỉnh, văn bản này được lưu vào một bộ đệm trượt lịch sử `_last_final_text` của phiên kết nối (giới hạn dung lượng tối đa `LAST_FINAL_TEXT_MAX_CHARS = 1000` ký tự).
2.  **Trích xuất gợi ý âm học (Prompt Extraction):** Khi bắt đầu nhận dạng phân đoạn âm thanh tiếp theo, hệ thống trích xuất khoảng 150 ký tự cuối cùng từ bộ đệm trượt (`INITIAL_PROMPT_MAX_CHARS = 500` ký tự) để làm văn bản gợi ý.
3.  **Nạp tham số suy luận:** Văn bản gợi ý này được nạp ngược lại vào mô hình Faster-Whisper thông qua tham số `initial_prompt`.
4.  **Cô lập tự hồi quy:** Để ngăn chặn mô hình bị rơi vào vòng lặp ảo giác hoặc lặp từ vô hạn (hallucination loop) do ảnh hưởng từ các câu cũ, tham số `condition_on_previous_text` được cấu hình cố định ở mức `False`. Quy trình này giúp mô hình nhận dạng chính xác các danh từ riêng, từ viết tắt chuyên ngành xuất hiện lặp lại xuyên suốt buổi họp mà không làm tăng độ trễ tính toán.

---

### 3.3. Dịch máy Hội thoại và Bộ đệm Xử lý Thời gian thực (Bài toán 2)

#### 3.3.1. Quy trình đệm dịch ngắn (Short-MT buffering) nâng cao ngữ nghĩa

Khi văn bản nguồn được nhận dạng hoàn tất từ chặng STT, nó được đẩy trực tiếp sang chặng dịch máy thần kinh (NMT) thông qua facade `MTEngine` sử dụng mô hình đa ngôn ngữ **NLLB-200** tối ưu hóa bằng thư viện CTranslate2. 

Do ngôn ngữ hội thoại thực tế thường có nhiều câu ngắn hoặc cụm từ ngắt quãng do thói quen nói ngắt nhịp của người dùng, nếu hệ thống dịch ngay lập tức mọi cụm từ đơn lẻ, bản dịch thu được sẽ bị rời rạc, sai lệch cấu trúc ngữ pháp và nghe rất giật cục khi đưa sang chặng TTS tiếp theo. Quy trình đệm dịch ngắn (Short-MT Buffering) được thiết kế để giải quyết bài toán này:

```
[STT Text Output] ──> [Tính số lượng từ]
                             │
            ┌────────────────┴────────────────┐
            ▼ Số từ < 4                       ▼ Số từ >= 4
     [Nạp vào bộ đệm pending]           [Ghép với bộ đệm cũ (nếu có)]
     [Hoãn kích hoạt TTS]               [Gửi sang NLLB-200 dịch thuật]
                                              │
                                              ▼
                                    [Trả kết quả mt.result]
                                    [Kích hoạt chặng TTS]
```

1.  **Đánh giá độ dài văn bản nguồn:** Khi nhận được chuỗi văn bản từ STT, hệ thống đếm số từ của chuỗi đầu vào.
2.  **Quyết định trì hoãn (Buffering Decision):** Hệ thống so sánh số từ với hằng số cấu hình `MIN_MT_WORDS_FOR_TTS = 4` từ:
    *   Nếu chiều dài câu nhỏ hơn 4 từ, hệ thống sẽ tạm hoãn việc gọi suy luận dịch máy và tổng hợp TTS. Văn bản này được lưu tạm vào bộ đệm trượt bất đồng bộ `_pending_mt_text`.
    *   Nếu chiều dài câu bằng hoặc lớn hơn 4 từ, hệ thống sẽ lấy toàn bộ văn bản đang lưu trong bộ đệm pending ghép nối tiếp với văn bản mới để tạo thành một vế câu hoàn chỉnh ngữ nghĩa.
3.  **Dịch máy ngữ cảnh:** Toàn bộ chuỗi văn bản ghép được gửi đến mô hình NLLB-200 để thực hiện dịch thuật sang ngôn ngữ đích. Kết quả dịch thu được có cấu trúc ngữ pháp trọn vẹn, giúp chặng tổng hợp giọng nói TTS tiếp theo có đủ thông tin để tạo ra âm phổ tự nhiên.

#### 3.3.2. Quy trình giám sát Watchdog flush giải phóng hàng đợi dịch thuật

Việc trì hoãn dịch các câu ngắn để cải thiện ngữ nghĩa lại tạo ra mâu thuẫn trực tiếp với yêu cầu tối ưu hóa độ trễ thời gian thực của hệ thống S2ST. Nếu người nói kết thúc câu nói ngắn của họ và dừng lại hoàn toàn, vế câu ngắn đó sẽ bị kẹt lại trong bộ đệm pending vĩnh viễn, khiến đối tác bên kia cuộc họp không thể nghe được nội dung dịch chặng cuối.

Để giải quyết mâu thuẫn này, hệ thống thiết lập một quy trình giám sát tự động **Watchdog Timer** hoạt động song song trong luồng xử lý WebSocket:

1.  **Giám sát thời gian im lặng:** Hệ thống tích hợp một vòng lặp giám sát bất đồng bộ (chạy với chu kỳ quét 200ms) để theo dõi thời điểm nhận gói tin cuối cùng của phiên kết nối.
2.  **Kiểm tra điều kiện kích hoạt:** Bộ giám sát liên tục kiểm tra hai điều kiện:
    *   Bộ đệm `_pending_mt_text` hiện tại đang có dữ liệu chờ dịch.
    *   Khoảng thời gian im lặng từ gói tin âm thanh cuối cùng gửi lên đã vượt quá ngưỡng cấu hình `PENDING_MT_TIMEOUT_S = 3.0` giây.
3.  **Kích hoạt xả bộ đệm cưỡng bức (Force Flush):** Khi cả hai điều kiện trên được thỏa mãn, Watchdog Timer sẽ phát tín hiệu xả bộ đệm. Hệ thống ngay lập tức rút toàn bộ văn bản đang bị kẹt trong bộ đệm pending, bỏ qua điều kiện độ dài từ tối thiểu, gửi trực tiếp sang mô hình NLLB-200 dịch thuật và đẩy thẳng kết quả dịch đến chặng TTS để sinh âm thanh phát ra loa của người nghe. Quy trình này bảo toàn độ trễ nhận thức đầu ra tối đa không vượt quá 3.0 giây trong các khoảng tạm nghỉ hội thoại.

---

### 3.4. Thực nghiệm Huấn luyện và Đánh giá Mô hình Piper TTS (Bài toán 3)

#### 3.4.1. Thiết kế quy trình xây dựng và làm sạch dữ liệu huấn luyện

Để huấn luyện thành công mô hình Piper TTS giọng nam miền Nam Việt từ tập dữ liệu công khai `VieNeu-TTS-140h`, hệ thống thiết lập một quy trình tiền xử lý dữ liệu tự động và kiểm soát chất lượng căn chỉnh chéo văn bản (STT QC). Quy trình này bao gồm các bước cụ thể sau:

```mermaid
graph TD
    A[Dataset VieNeu gốc: 1999 Clips] --> B[Tiền xử lý âm thanh cơ bản]
    B --> B1[Resample về 22.05 kHz mono]
    B --> B2[Chuẩn hóa độ to -23 LUFS]
    B --> B3[Cắt khoảng lặng top_db=30]
    B3 --> C[Kiểm định chất lượng chéo STT QC]
    C --> C1[Transcribe ngược bằng PhoWhisper-large]
    C1 --> C2[Tính WER đối xứng ref/hyp]
    C2 --> D[Bộ lọc lai Per-Speaker Hybrid Filter]
    D --> |Speaker _0004: keep chỉ khi WER < 0.15| E[Lớp lọc Strict: 409 clips]
    D --> |Speaker _0013, _0032: keep + warn WER < 0.30| F[Lớp lọc Standard: 1091 clips]
    E & F --> G[Tập dữ liệu sạch: 1500 clips ~2.5h]
    G --> H[Chuẩn hóa văn bản bằng vinorm]
    H --> I[Monkey-patch fake_imp cho Python 3.12+]
```

##### 1. Tiền xử lý âm thanh cơ bản (Audio Preprocessing)
Toàn bộ các tệp âm thanh WAV của các speaker giọng nam miền Nam được chuyển đổi định dạng tần số lấy mẫu về $22,050 \text{ Hz}$ (khớp với tần số của cấu hình mô hình Piper medium), chuyển đổi về kênh mono PCM 16-bit bằng thư viện `librosa`. Hệ thống chuẩn hóa độ to âm lượng về mức chuẩn $-23 \text{ LUFS}$ theo tiêu chuẩn phát thanh EBU R128 bằng thư viện `pyloudnorm`, đảm bảo mức năng lượng đồng đều trên toàn bộ tập dữ liệu huấn luyện. Thuật toán `librosa.effects.trim` với ngưỡng năng lượng $\theta_{\text{trim}} = 30 \text{ dB}$ được áp dụng để cắt bỏ khoảng lặng thừa ở hai đầu file âm thanh, tối ưu hóa quá trình học căn chỉnh âm phổ của mô hình.

##### 2. Quy trình kiểm định chất lượng căn chỉnh chéo văn bản (STT QC Pipeline)
Trải nghiệm thực tế phát hiện tập dữ liệu gốc `VieNeu-TTS-140h` gặp lỗi lệch offset dịch chuyển nhãn văn bản giữa các tệp âm thanh liền kề (offset error) trong quá trình cắt phân đoạn tự động của tác giả gốc. Điều này dẫn đến sự không khớp nghiêm trọng giữa văn bản ghi nhận và âm thanh thực tế. Để tự động phát hiện và loại bỏ các clips lỗi này, hệ thống thiết kế quy trình kiểm định chéo STT QC bằng mô hình học sâu **PhoWhisper-large** (1.55B tham số) chuyên biệt cho tiếng Việt:
*   Mô hình PhoWhisper-large thực hiện nhận dạng ngược lại toàn bộ 1999 clips âm thanh thành văn bản nhận dạng tương ứng ($T_{\text{hyp}}$).
*   Văn bản gốc ($T_{\text{ref}}$) và văn bản nhận dạng ngược ($T_{\text{hyp}}$) được xử lý thông qua cùng một hàm chuẩn hóa đối xứng (Symmetric Normalization Function) để loại bỏ toàn bộ dấu câu, ký tự đặc biệt, chuyển chuỗi về chữ thường và đồng bộ định dạng Unicode NFC, ngăn ngừa sai số giả tạo do định dạng viết hoa hoặc dấu câu khác nhau:
    $$\text{Norm}(T) = \text{NormalizeWS}(\text{RemovePunct}(\text{ToLowerCase}(\text{ToNFC}(T))))$$
*   Hệ thống tính toán chỉ số tỷ lệ lỗi từ (Word Error Rate - WER) giữa văn bản đối chiếu $T_{\text{ref\_norm}}$ và $T_{\text{hyp\_norm}}$:
    $$\text{WER} = \frac{S + D + I}{N}$$
    Trong đó $S, D, I$ lần lượt là số từ bị thay thế (Substitution), xóa (Deletion), và chèn thêm (Insertion); $N$ là tổng số từ trong văn bản đối chiếu.
*   **Thiết lập các ngưỡng phân loại chất lượng clip:**
    *   Lớp `keep` ($\text{WER} < 0.15$): Căn chỉnh sạch hoàn hảo, văn bản khớp hoàn toàn với âm thanh.
    *   Lớp `warn` ($0.15 \le \text{WER} < 0.30$): Borderline, đa số là các câu chứa từ tiếng Anh hoặc chữ số phiên âm tiếng Việt (ví dụ: viết *"GPT-4"* nhưng PhoWhisper đọc ngược là *"gi pi ti bốn"*). Audio thực tế vẫn khớp với nội dung nguyên bản của câu.
    *   Lớp `drop` ($\text{WER} \ge 0.30$): Mismatch thực tế, văn bản và âm thanh lệch hoàn toàn do lỗi offset.
*   **Thiết kế bộ lọc lai Per-Speaker Hybrid Filter:** Phân tích thực nghiệm chỉ ra lỗi lệch offset không phân bố ngẫu nhiên toàn dataset mà tập trung rất nặng vào speaker `_0004` (lên tới 47.5% drop rate), trong khi speaker `_0032` cực kỳ sạch (chỉ 0.2% drop rate). Từ đó thiết lập quy tắc lọc lai:
    *   Đối với Speaker chất lượng kém (`_0004`): Chỉ giữ lại các clip thuộc lớp `keep` (lọc nghiêm ngặt).
    *   Đối với Speaker chất lượng tốt (`_0013` và `_0032`): Giữ lại các clip thuộc cả lớp `keep` và `warn` (lọc tiêu chuẩn).
    *   Kết quả lọc thu được một tập dữ liệu đồng nhất gồm **1500 clips** (~2.5 giờ âm thanh chất lượng studio sạch hoàn toàn), được hiển thị qua biểu đồ WER phân bố lưỡng cực (Bimodal Distribution) trong thực nghiệm ở Chương 4.

##### 3. Chuẩn hóa văn bản học thuật bằng vinorm
Văn bản của 1500 clips sạch này được đưa qua thư viện `vinorm` để chuyển đổi toàn bộ các chữ số (ví dụ: *"2026"* thành *"hai nghìn không trăm hai mươi sáu"*), ngày tháng và các ký tự viết tắt sang dạng chữ viết tiếng Việt đầy đủ phục vụ cho TTS phonemization. Do môi trường runtime Python 3.12+ loại bỏ hoàn toàn mô đun cũ `imp` khiến `vinorm` bị lỗi `ModuleNotFoundError`, đồ án thiết kế một bản vá khẩn cấp monkey-patch (`fake_imp`) vào hệ thống `sys.modules` để khôi phục lớp `imp` giả lập thông qua thư viện `importlib` tiêu chuẩn mới, đảm bảo tính tương thích và vận hành trơn tru của quy trình chuẩn hóa văn bản.

#### 3.4.2. Thiết kế chiến lược Cross-Gender Fine-tuning trên kiến trúc VITS

Để tối ưu hóa thời gian huấn luyện và chất lượng âm thanh trong điều kiện tài nguyên tính toán giới hạn trên GPU Google Colab T4, đồ án đề xuất quy trình huấn luyện **Cross-Gender Fine-tuning** (huấn luyện thích ứng chuyển đổi giới tính giọng đọc) dựa trên kiến trúc nén **VITS**:

##### 1. Nguyên lý kiến trúc VITS áp dụng
Kiến trúc VITS là một mô hình tổng hợp tiếng nói đầu-cuối (end-to-end) tích hợp mạng biến phân tự động điều kiện (Conditional VAE), hệ thống luồng chuẩn hóa (Normalizing Flows) và mạng đối nghịch tạo sinh (GAN) để sinh trực tiếp sóng âm từ văn bản.
*   **Prior Text Encoder:** Ánh xạ chuỗi ký tự/âm vị đầu vào sang phân phối latent đại diện cho thông tin ngôn ngữ có điều kiện. Lớp nhúng âm vị (Phoneme Embeddings) đóng vai trò ánh xạ định danh âm vị sang vector biểu diễn đặc trưng ngôn ngữ.
*   **Posterior Encoder:** Trích xuất các phân phối đặc trưng âm học $z$ từ mel-spectrogram của âm thanh gốc.
*   **Normalizing Flows:** Thực hiện các phép biến đổi khả nghịch (Jacobian) để chuyển đổi phân phối đơn giản từ Text Encoder thành phân phối mel-spectrogram phức tạp của giọng đọc đích.
*   **HiFi-GAN Decoder:** Giải mã vector không gian latent $z$ thành sóng âm vật lý (waveform) trực tiếp. Mô hình được huấn luyện đối nghịch cùng hệ thống Discriminators gồm Multi-Period Discriminator (MPD) và Multi-Scale Discriminator (MSD) để đánh giá tính tự nhiên và độ sắc nét âm phổ.

##### 2. Chiến lược chuyển đổi giới tính giọng đọc (Female-to-Male Adaptation)
Với lượng dữ liệu giọng nam thu được có giới hạn (~2.5 giờ) và tài nguyên tính toán giới hạn, việc huấn luyện từ đầu (train from scratch) sẽ dẫn đến chất lượng âm thanh kém, dễ bị méo tiếng và không hội tụ. Đồ án đề xuất giải pháp tinh chỉnh chuyển giới tính:
*   **Kế thừa không gian nhúng âm vị:** Mô hình kế thừa toàn bộ cấu trúc Prior Text Encoder và bản đồ nhúng âm vị gồm 154 âm vị tiếng Việt chuẩn của mô hình giọng nữ gốc `vi_VN-vais1000-medium` đã được huấn luyện hơn 4769 epochs trên tập dữ liệu VAIS1000. Điều này giúp giữ vững khả năng phát âm chuẩn xác và ngắt nghỉ tự nhiên của tiếng Việt.
*   **Đóng băng và tinh chỉnh chọn lọc:** Trong quá trình huấn luyện với dữ liệu giọng nam sạch, hệ thống đóng băng một phần cấu trúc Text Encoder để bảo toàn biểu diễn ngôn ngữ chuẩn. Tập trung cập nhật trọng số của khối **Normalizing Flows, Decoder (HiFi-GAN)** và các **Discriminators**. Quá trình huấn luyện đối nghịch buộc Decoder và Flows phải học cách dịch chuyển phân phối âm phổ, kéo dải formant và tần số cao độ cơ bản $F_0$ từ giọng nữ (khoảng 200 - 240 Hz) xuống giọng nam miền Nam tự nhiên (khoảng 100 - 140 Hz), tạo nên sắc âm ấm áp đặc trưng.

##### 3. Thiết lập siêu tham số huấn luyện (Training Hyperparameters)
*   **Tốc độ học tinh chỉnh tối ưu:** Thiết lập $LR_{\text{finetune}} = 1.0 \times 10^{-4}$ (giảm một nửa so với mức mặc định $2.0 \times 10^{-4}$ của Piper huấn luyện từ đầu để tránh phá vỡ không gian latent đã học và gây hiện tượng phân kỳ loss).
*   **Batch size và Precision:** Cấu hình batch size 16 (tối ưu hóa bộ nhớ GPU VRAM 16GB trên Tesla T4) và độ chính xác tính toán FP32 để bảo vệ các phép toán log/exp phức tạp của Normalizing Flows tránh lỗi tràn số và sụp đổ chế độ (mode collapse).
*   **Chu kỳ lưu checkpoint:** Lưu mỗi 10 epochs (giảm overhead I/O đồng bộ lên Drive).
*   **Chiến lược Local I/O chống nghẽn mạng:** Quá trình đọc dữ liệu và tập tin cache `.pt` được thực hiện hoàn toàn trên SSD cục bộ của Colab (`/content/training_dir`) để loại bỏ hoàn toàn hiện tượng thắt nút cổ chai I/O qua Drive FUSE (random reads latency). Các tệp checkpoints và tệp nhật ký TensorBoard được ghi trực tiếp sang Google Drive đồng bộ để đảm bảo khả năng tự động khôi phục trạng thái (auto-resume) khi mất kết nối.

#### 3.4.3. Giải pháp đồng bộ âm vị 2-Pass và vá mã nguồn PyTorch Lightning

Quá trình chuẩn bị dữ liệu và huấn luyện Piper TTS đối mặt với hai rào cản kỹ thuật lớn được giải quyết bằng các giải pháp tùy biến trực tiếp:

##### 1. Giải pháp đồng bộ âm vị 2-Pass Workaround
Trình tiền xử lý `piper_train.preprocess` của phiên bản Piper hiện tại không hỗ trợ cấu hình bản đồ âm vị trực tiếp từ dòng lệnh. Khi chạy trên tập dữ liệu VieNeu có chứa một số từ tiếng Anh pha trộn (codeswitching), bộ grapheme-to-phoneme `espeak-ng` tự động sinh ra 3 âm vị ngoại lai (`'X'`, `'g'`, `'ʦ'`), nâng tổng số âm vị lên 157 và gây lỗi sập chương trình `IndexError` khi nạp vào base model (chỉ hỗ trợ tối đa 154 âm vị chuẩn).

Đồ án thiết lập giải thuật tiền xử lý 2 bước (2-Pass Workaround):
*   **Pass 1 (Khảo sát âm vị):** Chạy trình tiền xử lý của Piper trên một thư mục trống để hệ thống tự động phát hiện và sinh tệp cấu hình `config.json` thô chứa đầy đủ 157 âm vị thực tế xuất hiện trong tập dữ liệu.
*   **Pass 2 (Cưỡng bức đồng bộ):** Hệ thống thực hiện ghi đè tệp `config.json` thô này bằng tệp cấu hình âm vị chuẩn (chứa đúng 154 âm vị gốc của base model `vais1000-medium`), sau đó chạy lại lệnh tiền xử lý dữ liệu chính thức. Khi phát hiện tệp cấu hình đã tồn tại, trình tiền xử lý của Piper buộc phải sử dụng lại bản đồ 154 âm vị gốc, các âm vị lạ tự động bị loại bỏ (drop) hoặc ánh xạ về âm vị gần nhất mà không làm sập chương trình.
*   **Quy trình kiểm tra 4-Checks (Four-stage Validation):** Trước khi đưa dữ liệu vào huấn luyện, hệ thống chạy một kịch bản kiểm tra tự động gồm 4 bước: (1) Quét toàn bộ tệp `dataset.jsonl` để tìm các ID âm vị lớn hơn 153; (2) Đối chiếu chéo từ điển âm vị; (3) Xác thực cấu trúc tensor đầu vào; (4) Chạy thử nghiệm suy luận 1 epoch để đảm bảo an toàn tuyệt đối cho PyTorch.

##### 2. Vá mã nguồn tối ưu tốc độ học
Để cưỡng bức tốc độ học trong PyTorch Lightning khi bộ mã lệnh của Piper không hiển thị tham số này ra ngoài giao diện dòng lệnh, hệ thống áp dụng kỹ thuật vá mã nguồn trực tiếp bằng biểu thức chính quy (Regex Inline Patching). Kịch bản Python tự động tìm kiếm mẫu Regex `[12]e-0?4` trong tệp cấu hình huấn luyện `vits/lightning.py` trên máy chủ và ghi đè giá trị học mặc định `2e-4` thành tốc độ tinh chỉnh tối ưu $LR_{\text{finetune}} = 1.0 \times 10^{-4}$ một cách tự động và đảm bảo tính lặp lại an toàn (idempotency).

#### 3.4.4. Thiết kế hệ thống đánh giá chất lượng và hiệu năng mô hình

Để đánh giá khoa học và toàn diện mô hình Piper TTS giọng Nam Việt sau tinh chỉnh và lượng tử hóa, đồ án thiết lập khung phương pháp đánh giá thực nghiệm đa chiều bao gồm:

##### 1. Chỉ số đánh giá hiệu năng và độ chính xác khách quan (Objective Metrics)
*   **Hệ số thời gian thực (Real-Time Factor - RTF):** Đo tỉ số giữa thời gian xử lý suy luận của mô hình TTS trên CPU máy khách ($T_{\text{infer}}$, loại bỏ hoàn toàn thời gian ghi file WAV) và thời lượng thực tế của đoạn âm thanh sinh ra ($T_{\text{audio}}$):
    $$\text{RTF} = \frac{T_{\text{infer}}}{T_{\text{audio}}}$$
    Mô hình đạt yêu cầu thời gian thực khi chỉ số $\text{RTF} < 1.0$ trên phần cứng CPU mục tiêu của máy khách. Để bảo đảm headroom cho các chặng khác (STT, MT) chạy song song, chỉ số RTF hướng tới mức tối ưu $\text{RTF} < 0.3$.
*   **Tỷ lệ lỗi từ hồi chuyển (Round-trip STT WER):** Để đo lường khách quan độ rõ tiếng (intelligibility), các tệp âm thanh tổng hợp được gửi qua mô hình nhận dạng giọng nói PhoWhisper-large để giải mã ngược thành văn bản. Hệ thống tính toán Word Error Rate (WER) và Character Error Rate (CER) giữa văn bản gốc ban đầu và văn bản nhận dạng ngược để phát hiện các âm vị bị phát âm "ngọng" hoặc méo tiếng.
*   **Đo đạc chất lượng âm phổ qua thống kê phổ (Spectral Stats):** Hệ thống tính toán các chỉ số thống kê trên phổ âm gồm: Trọng tâm phổ (Spectral Centroid - Hz) để đánh giá độ trầm của giọng, Tần số Rolloff 85% để đánh giá phân bố năng lượng tần số cao, và Tỷ lệ vượt ngưỡng qua điểm không (Zero-Crossing Rate - ZCR) để đo lượng tiếng xì/ồn âm học.

##### 2. Đánh giá chất lượng giọng tự nhiên tự động và chủ quan
*   **Độ tự nhiên khách quan tự động (NISQA MOS):** Hệ thống tích hợp mô hình học sâu **NISQA-TTS** (Neural Speech Quality Assessment) để dự đoán tự động điểm số cảm nhận chất lượng tự nhiên (Mean Opinion Score - Predictor MOS) của các file âm thanh sinh ra trên thang điểm từ 1.0 đến 5.0.
*   **Khảo sát ý kiến người dùng (Human MOS):** Đồ án thiết lập bộ **25 câu test chuẩn hóa** nằm ngoài tập huấn luyện, phân chia thành 5 danh mục: cơ bản (Generic), số/ngày/giờ, tiếng Anh pha trộn (codeswitching), tongue-twister thanh điệu khó, và câu thoại dài 10-15s để kiểm tra tính ổn định của cao độ (prosody). Khảo sát thu thập ý kiến từ người nghe bản địa để chấm điểm MOS độc lập trên 3 khía cạnh: Độ tự nhiên (Naturalness), Độ rõ chữ (Intelligibility), và Tính biểu cảm (Expressiveness) theo thang điểm 5.0 chuẩn.



### 3.5. Điều phối Âm thanh Đầu ra và Cô lập Loopback Máy khách

#### 3.5.1. Cơ chế định tuyến RoutePlayer phân tách kênh phát

Tại máy khách PySide6, việc phát âm thanh tổng hợp nhận được từ WebSocket được điều phối bất đồng bộ bởi đối tượng `RoutePlayer`. Lớp này đóng vai trò quản lý song song hai trình phát âm thanh `AdaptiveJitterPlayer` tương ứng với hai tuyến phát độc lập:

```
[Server trả về văn bản dịch] ──> [Suy luận Piper TTS tại Client]
                                           │
                                           ▼
                                 [Dispatcher RoutePlayer]
                                           │
                     ┌─────────────────────┴─────────────────────┐
                     v (Route ID = 0)                            v (Route ID = 1)
           [AdaptiveJitterPlayer 0]                    [AdaptiveJitterPlayer 1]
                     │                                           │
             (select_output_device)                      (select_output_device)
                     │                                           │
                     v                                           v
       [VB-Audio Cable Input (Ảo)]                 [Default Audio Speaker (Thật)]
```

##### 1. Quy trình định tuyến kênh phát
*   **Tuyến Route 0 (Dịch xuôi - tiếng Anh):** Khi nhận được âm phổ tiếng Anh dịch từ tiếng Việt của người dùng nội bộ, `RoutePlayer` chuyển hướng dữ liệu âm thanh số float32 đến trình phát `AdaptiveJitterPlayer 0`. Trình phát này được cấu hình thiết bị đầu ra ngầm định là cổng vào ảo `"CABLE Input (VB-Audio Virtual Cable)"`. Phần mềm họp trực tuyến (Zoom/Meet) tại máy khách sẽ chọn đầu ra ảo tương ứng (`CABLE Output`) làm thiết bị Micro đầu vào của nó để truyền đi họp.
*   **Tuyến Route 1 (Dịch ngược - tiếng Việt):** Khi nhận được âm phổ dịch tiếng Việt của đối tác nước ngoài nói, `RoutePlayer` chuyển hướng dữ liệu âm thanh đến trình phát `AdaptiveJitterPlayer 1`. Trình phát này chọn thiết bị đầu ra mặc định là loa vật lý hoặc tai nghe thật của người dùng nội bộ nghe trực tiếp.

##### 2. Quy trình xử lý bộ đệm chống giật (Jitter Buffer Workflow)
Mỗi trình phát `AdaptiveJitterPlayer` duy trì một hàng đợi đệm âm thanh (Jitter Queue) để sắp xếp các mảnh âm thanh nhị phân nhận được từ mạng WebSocket. Quy trình này tự động bù trừ các khoảng trễ mạng biến động (network jitter), đảm bảo luồng phát âm thanh liên tục, không bị giật cục hay đứt gãy tín hiệu.

#### 3.5.2. Ghi âm WASAPI Loopback cô lập âm phản hồi (Echo Mitigation)

Quy trình cô lập âm học là chặng chốt chặn quan trọng nhất để hệ thống S2ST hoạt động trong môi trường thực tế mà không gây ra vòng lặp phản hồi âm thanh (feedback loop) và tiếng vọng âm học (acoustic echo). Quy trình này được thiết kế phối hợp giữa ghi âm loopback kỹ thuật số và cô lập tuyến phát:

1.  **Quy trình ghi âm loopback WASAPI:** Lớp dịch vụ `LoopbackCaptureService` gọi API âm thanh WASAPI trực tiếp trên thiết bị đầu ra mặc định của hệ thống Windows với cờ ghi âm loopback hoạt động. Tín hiệu âm thanh của đối tác phát ra từ phần mềm họp trực tuyến (Zoom/Meet) được thu lại trực tiếp từ tầng số học của card âm thanh. Quy trình này giúp thu âm thanh sạch hoàn toàn, loại bỏ 100% tiếng ồn vật lý trong phòng họp và giọng nói của người dùng nội bộ.
2.  **Quy trình triệt tiêu phản hồi âm học:** 
    *   Âm thanh dịch tiếng Anh (Route 0) được đẩy ngầm bằng tín hiệu số vào driver ảo VB-Cable, loa ngoài của người dùng hoàn toàn không phát ra âm thanh này. Do đó micro thật của người dùng không thể thu lại tiếng dịch tiếng Anh.
    *   Âm thanh dịch tiếng Việt (Route 1) phát ra loa vật lý để người dùng nghe. Tuy nhiên, WASAPI loopback chỉ ghi âm luồng âm thanh hệ thống chính (tiếng của đối tác nói tiếng Anh phát ra từ phần mềm họp), hoàn toàn không ghi nhận âm thanh phát ra từ trình phát dịch tiếng Việt của hệ thống.
    *   Sự cô lập luồng âm vật lý và kỹ thuật số này triệt tiêu hoàn toàn khả năng micro của máy khách thu lại âm thanh dịch của chính mình, đảm bảo tính cô lập âm học tuyệt đối cho toàn bộ pipeline S2ST song hướng mà không cần đặc quyền Administrator hệ thống.



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
