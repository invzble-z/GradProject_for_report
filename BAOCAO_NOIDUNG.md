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

# NGHIÊN CỨU VÀ PHÁT TRIỂN HỆ THỐNG DỊCH THUẬT GIỌNG NÓI THỜI GIAN THỰC ANH – VIỆT VỚI TỐI ƯU HÓA ĐỘ TRỄ SỬ DỤNG DEEP LEARNING

> Tên đề tài (EN — Claude đề xuất, chờ xác nhận): *Research and Development of a Real-time English–Vietnamese Speech Translation System with Latency Optimization using Deep Learning.*

## TRANG THỦ TỤC & DẪN NHẬP

- TRANG TIÊU ĐỀ — Tên đề tài VI/EN (như trên); **Họ tên + MSSV thành viên: `<<PLACEHOLDER — user điền>>`**; GVHD: ThS. Trần Uyên Trang. ⚠️
- LỜI CẢM ƠN — *giữ nguyên nội dung hiện có trong docx* ✅
- DANH MỤC CÁC CHỮ VIẾT TẮT — *giữ bảng 19×4 hiện có* ✅
- DANH MỤC BẢNG — *tự sinh bằng Table of Tables field khi xuất docx* (xóa danh mục rác cũ) ⚠️
- DANH MỤC HÌNH VẼ – ĐỒ THỊ — *tự sinh bằng Table of Figures field* (xóa danh mục rác cũ) ⚠️

---

# CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

> Nguồn: phần "LỜI MỞ ĐẦU" trong docx, bê **đầy đủ** và tái cấu trúc theo outline. (Bổ sung 1.5 Cách tiếp cận & PPNC để giữ trọn nội dung gốc; 1.6 Bố cục viết mới.)

## 1.1. Lý do chọn đề tài

Trong bối cảnh toàn cầu hóa và sự phát triển mạnh mẽ của công nghệ số, các nền tảng họp trực tuyến như Zoom, Google Meet hay Microsoft Teams đã trở thành công cụ quan trọng trong hoạt động giao tiếp và hợp tác quốc tế. Tuy nhiên, khác biệt ngôn ngữ vẫn là một rào cản lớn khiến quá trình trao đổi thông tin gặp nhiều khó khăn. Các giải pháp truyền thống như thuê phiên dịch viên tuy mang lại chất lượng dịch thuật cao nhưng thường tốn kém chi phí, khó triển khai linh hoạt và tiềm ẩn những vấn đề liên quan đến bảo mật thông tin. Trong khi đó, các công cụ dịch văn bản thông thường yêu cầu người dùng thao tác thủ công, làm gián đoạn dòng hội thoại và không đáp ứng được nhu cầu giao tiếp thời gian thực.

Trước thực tế đó, hệ thống dịch giọng nói sang giọng nói thời gian thực (Speech-to-Speech Translation – S2ST) được xem là một hướng tiếp cận đầy tiềm năng. Tuy nhiên, việc triển khai hệ thống trong môi trường họp trực tuyến vẫn đối mặt với nhiều thách thức. Độ trễ phát sinh qua các giai đoạn nhận dạng tiếng nói (STT), dịch máy (NMT) và tổng hợp tiếng nói (TTS) có thể làm giảm tính tự nhiên của cuộc hội thoại nếu không được tối ưu hiệu quả. Bên cạnh đó, đặc điểm thanh điệu và cách ngắt nghỉ trong tiếng Việt khiến hệ thống dễ xác định sai điểm kết thúc câu, ảnh hưởng đến chất lượng nhận dạng và dịch thuật. Ngoài ra, nguồn tài nguyên mô hình tổng hợp giọng nam tiếng Việt chất lượng cao, có khả năng vận hành trên thiết bị cấu hình thấp vẫn còn hạn chế. Một vấn đề thực tế khác là hiện tượng phản hồi âm học khi âm thanh đã được dịch tiếp tục bị micro thu nhận, dẫn đến vòng lặp dịch không mong muốn và gây nhiễu trong quá trình giao tiếp.

Do đó, việc nghiên cứu các giải pháp giảm độ trễ xử lý, nâng cao độ chính xác nhận dạng, phát triển mô hình tổng hợp giọng nói phù hợp và kiểm soát hiệu quả hiện tượng phản hồi âm học là những yêu cầu cần thiết. Đây cũng là cơ sở quan trọng để xây dựng một hệ thống dịch giọng nói thời gian thực có tính ứng dụng cao, đáp ứng nhu cầu giao tiếp đa ngôn ngữ trong môi trường trực tuyến hiện nay. ✅

## 1.2. Phát biểu bài toán

Từ bối cảnh và những thách thức nêu trên, đề tài xác định bốn bài toán cốt lõi cần giải quyết:

**1.2.1. Nhận dạng tiếng nói (STT) dạng streaming trên luồng âm thanh liên tục.** Hệ thống phải nhận dạng tiếng nói trên luồng âm thanh được truyền liên tục theo từng đoạn ngắn thay vì trên tệp hoàn chỉnh, đồng thời duy trì ngữ cảnh hội thoại giữa các lần nhận dạng để không làm mất ý nghĩa của câu nói.

**1.2.2. Dịch máy hội thoại đa ngữ (NMT) trong môi trường thời gian thực.** Văn bản đầu vào sinh ra từ tầng STT thường ngắn, rời rạc và chưa hoàn chỉnh về ngữ pháp do người nói ngắt nhịp, lấy hơi; bài toán đặt ra là dịch sao cho bảo toàn ngữ nghĩa và tính tự nhiên của vế nói trong khi vẫn đáp ứng yêu cầu độ trễ thấp.

**1.2.3. Thiếu hụt mô hình tổng hợp tiếng nói (TTS) giọng nam tiếng Việt.** Cần một mô hình TTS giọng nam tiếng Việt chất lượng cao, dung lượng nhẹ, có thể chạy thời gian thực trên thiết bị phổ thông — trong khi tài nguyên công khai hiện có còn rất hạn chế.

**1.2.4. Cô lập luồng âm thanh thu/phát chống vòng lặp phản hồi âm học.** Hệ thống phải tách biệt luồng âm thanh đầu vào và đầu ra để âm thanh đã dịch phát ra từ loa không bị micro thu ngược trở lại, tránh hiện tượng feedback loop gây nhiễu trong môi trường họp trực tuyến. ✅

## 1.3. Mục tiêu và Đóng góp của đề tài

Đồ án hướng tới các mục tiêu chính sau:

- Xây dựng hệ thống dịch giọng nói sang giọng nói thời gian thực (S2ST) theo mô hình Client–Server, cho phép hai người dùng sử dụng ngôn ngữ khác nhau có thể giao tiếp trực tiếp thông qua kết nối WebSocket. Hệ thống cần đảm bảo khả năng xử lý gần thời gian thực, giảm thiểu độ trễ để duy trì tính tự nhiên của cuộc hội thoại.
- Nghiên cứu và triển khai các giải pháp tối ưu cho quá trình xử lý dữ liệu âm thanh, bao gồm phát hiện khoảng dừng trong lời nói, phân đoạn câu và quản lý bộ đệm dịch. Mục tiêu là rút ngắn thời gian phản hồi của hệ thống nhưng vẫn đảm bảo nội dung dịch đầy đủ và chính xác.
- Xây dựng và tinh chỉnh mô hình tổng hợp tiếng nói tiếng Việt giọng nam dựa trên nền tảng Piper TTS. Mô hình được tối ưu để có chất lượng phát âm tự nhiên, dung lượng nhỏ và có thể hoạt động trên các máy tính phổ thông mà không yêu cầu phần cứng chuyên dụng.
- Thiết kế cơ chế kiểm soát phản hồi âm học trong môi trường họp trực tuyến nhằm ngăn chặn hiện tượng âm thanh dịch phát ra từ loa bị thu ngược trở lại micro. Giải pháp cần đảm bảo hệ thống hoạt động ổn định mà không làm ảnh hưởng đến trải nghiệm của người dùng.
- Đánh giá hiệu năng của hệ thống thông qua các tiêu chí như độ trễ xử lý, chất lượng nhận dạng tiếng nói, độ chính xác của bản dịch và chất lượng âm thanh tổng hợp, từ đó xác định khả năng ứng dụng của hệ thống trong các tình huống giao tiếp trực tuyến thực tế.

**Đóng góp chính của đề tài:** (1) một hệ thống pipeline S2ST song hướng thời gian thực được tối ưu độ trễ, tích hợp đầy đủ ba tầng STT–MT–TTS; và (2) một mô hình Piper TTS giọng nam tiếng Việt dung lượng nhẹ, chất lượng tốt, có thể chạy thời gian thực trên CPU phổ thông, đóng góp cho cộng đồng nghiên cứu. ⚠️ *(mục Đóng góp tổng hợp từ kết luận docx — rà lại sau khi chốt Chương 4/5)*

## 1.4. Đối tượng và Phạm vi nghiên cứu

**Đối tượng nghiên cứu.** Đồ án tập trung nghiên cứu các công nghệ và mô hình trí tuệ nhân tạo phục vụ bài toán dịch giọng nói sang giọng nói thời gian thực, bao gồm nhận dạng tiếng nói, dịch máy và tổng hợp tiếng nói. Bên cạnh đó, đề tài cũng nghiên cứu các phương pháp phát hiện hoạt động giọng nói, cơ chế truyền dữ liệu thời gian thực giữa máy khách và máy chủ, cũng như các giải pháp xử lý âm thanh nhằm nâng cao chất lượng và tính ổn định của hệ thống trong môi trường hội thoại trực tuyến.

**Phạm vi nghiên cứu.**

- Xây dựng hệ thống dịch giọng nói song hướng cho cặp ngôn ngữ tiếng Việt và tiếng Anh.
- Triển khai hệ thống theo mô hình Client–Server, trong đó các tác vụ xử lý trí tuệ nhân tạo được thực hiện trên máy chủ và người dùng tương tác thông qua ứng dụng máy khách trên hệ điều hành Windows.
- Nghiên cứu và đánh giá hệ thống trong điều kiện tài nguyên tính toán giới hạn, sử dụng một GPU tầm trung cho phía máy chủ và các máy tính cá nhân phổ thông cho phía người dùng.
- Xây dựng mô hình tổng hợp tiếng nói tiếng Việt giọng nam dựa trên dữ liệu giọng đọc tiếng Việt đã được tiền xử lý và chuẩn hóa.
- Đánh giá hiệu năng hệ thống dựa trên các tiêu chí như độ trễ xử lý, chất lượng nhận dạng tiếng nói, độ chính xác dịch thuật và chất lượng âm thanh đầu ra. ✅

## 1.5. Cách tiếp cận và Phương pháp nghiên cứu

### 1.5.1. Cách tiếp cận

Để đáp ứng yêu cầu xử lý thời gian thực trong điều kiện tài nguyên tính toán hạn chế, đề tài áp dụng một số hướng tiếp cận chính sau:

- **Tiếp cận kiến trúc phân tán Client–Server:** Các tác vụ AI có yêu cầu tính toán cao như nhận dạng tiếng nói (STT) và dịch máy (NMT) được thực hiện trên máy chủ có GPU, còn máy khách đảm nhận việc thu/phát, định tuyến âm thanh và hiển thị giao diện. Trong thiết kế ban đầu, tác vụ tổng hợp tiếng nói (TTS) dự kiến đặt tại máy khách nhằm tối ưu độ trễ và dự phòng cho trường hợp máy chủ không đủ VRAM khi chạy các mô hình lớn; bản thân mô hình TTS cũng đủ nhẹ để chạy trên CPU của máy khách. Tuy nhiên, khi triển khai thực tế, máy chủ có đủ tài nguyên nên TTS được đặt luôn trên GPU máy chủ cùng với STT và NMT. Cách tiếp cận phân tán này giúp tận dụng hiệu quả tài nguyên phần cứng giữa hai phía và giữ cho ứng dụng máy khách nhẹ, dễ triển khai trên thiết bị phổ thông.
- **Tiếp cận xử lý bất đồng bộ:** Hệ thống được thiết kế theo cơ chế xử lý song song giữa các thành phần nhằm giảm thời gian chờ giữa các giai đoạn nhận dạng, dịch và tổng hợp tiếng nói. Đồng thời, các mô hình được khởi tạo sẵn khi hệ thống bắt đầu hoạt động để hạn chế độ trễ phát sinh trong lần suy luận đầu tiên.
- **Tiếp cận chuyển giao học tập cho mô hình tổng hợp tiếng nói:** Thay vì huấn luyện mô hình từ đầu, đề tài sử dụng phương pháp tinh chỉnh từ mô hình đã được huấn luyện trước nhằm xây dựng giọng nam tiếng Việt từ tập dữ liệu có quy mô hạn chế. Cách tiếp cận này giúp rút ngắn thời gian huấn luyện, giảm yêu cầu dữ liệu và vẫn đảm bảo chất lượng âm thanh đầu ra.
- **Tiếp cận kiểm soát phản hồi âm học:** Hệ thống sử dụng cơ chế tách biệt các luồng âm thanh đầu vào và đầu ra thông qua thiết bị âm thanh ảo. Giải pháp này xử lý **triệt để** bài toán vòng lặp ở mức phần mềm: khi ứng dụng thu âm thanh hệ thống rồi phát lại âm thanh đã dịch (vốn cũng là âm thanh hệ thống), việc định tuyến tách biệt qua thiết bị âm thanh ảo bảo đảm âm phát ra không bị thu ngược trở lại để tạo thành vòng lặp dịch. Riêng hiện tượng vọng âm ở mức phần cứng — loa vật lý phát ra bị micro thu lại — không thể loại bỏ bằng định tuyến phần mềm (ví dụ khi người dùng dùng loa và micro mặc định của laptop); do đó trong quá trình demo và sử dụng, người dùng được yêu cầu dùng tai nghe để tách biệt loa với micro, qua đó giải quyết triệt để vấn đề này.

Thông qua các hướng tiếp cận trên, đề tài hướng đến mục tiêu xây dựng một hệ thống dịch giọng nói thời gian thực có độ trễ thấp, hoạt động ổn định và có khả năng triển khai trên hạ tầng phần cứng phổ thông. ✅

### 1.5.2. Phương pháp nghiên cứu

**Phương pháp nghiên cứu lý thuyết.** Tiến hành nghiên cứu, tổng hợp và phân tích các tài liệu, công trình khoa học liên quan đến lĩnh vực xử lý tiếng nói và trí tuệ nhân tạo. Nội dung nghiên cứu tập trung vào các mô hình nhận dạng tiếng nói, dịch máy và tổng hợp tiếng nói hiện đại, đồng thời tìm hiểu các kiến trúc học sâu và kỹ thuật tối ưu hóa được sử dụng trong các hệ thống dịch giọng nói thời gian thực.

**Phương pháp thực nghiệm và xây dựng hệ thống.** Trên cơ sở lý thuyết đã nghiên cứu, đề tài tiến hành thiết kế và xây dựng hệ thống dịch giọng nói song hướng theo mô hình Client–Server. Quá trình thực hiện bao gồm thu thập và tiền xử lý dữ liệu, tinh chỉnh mô hình tổng hợp tiếng nói tiếng Việt giọng nam, triển khai các thành phần nhận dạng tiếng nói, dịch máy và tổng hợp tiếng nói, đồng thời phát triển ứng dụng máy khách phục vụ việc thu nhận, truyền tải và phát lại âm thanh trong thời gian thực. Bên cạnh đó, các giải pháp tối ưu độ trễ, quản lý luồng dữ liệu và kiểm soát phản hồi âm học cũng được nghiên cứu, triển khai và đánh giá thông qua nhiều kịch bản thử nghiệm khác nhau nhằm nâng cao hiệu năng của hệ thống.

**Phương pháp đánh giá và kiểm chứng.** Hiệu năng của hệ thống được đánh giá thông qua cả phương pháp định lượng và định tính. Về mặt định lượng, đề tài đo lường các chỉ số như độ trễ xử lý, độ chính xác của mô hình nhận dạng tiếng nói, tốc độ tổng hợp tiếng nói và chất lượng âm thanh đầu ra bằng các công cụ đánh giá phù hợp. Về mặt định tính, hệ thống được khảo sát trên nhóm người dùng thử nghiệm nhằm đánh giá mức độ tự nhiên, độ rõ ràng và khả năng đáp ứng trong quá trình giao tiếp thực tế. Kết quả thu được là cơ sở để đánh giá tính khả thi và hiệu quả của hệ thống được đề xuất. ✅

## 1.6. Bố cục của Báo cáo

Báo cáo được tổ chức thành năm chương:

- **Chương 1 – Giới thiệu đề tài:** trình bày bối cảnh, lý do chọn đề tài, phát biểu bài toán, mục tiêu và đóng góp, đối tượng và phạm vi, cách tiếp cận và phương pháp nghiên cứu.
- **Chương 2 – Tổng quan tài liệu và Cơ sở lý thuyết:** trình bày nền tảng lý thuyết về STT (Whisper/PhoWhisper), NMT (NLLB-200), TTS (VITS/Piper), VAD (Silero), các công nghệ – thư viện sử dụng, cùng các nghiên cứu liên quan và khoảng trống nghiên cứu.
- **Chương 3 – Phương pháp nghiên cứu đề xuất:** trình bày kiến trúc hệ thống Client–Server, thiết kế client và cơ chế cô lập loopback, thiết kế server phân tầng hướng engine, pipeline streaming STT–MT–TTS và quy trình fine-tuning Piper TTS giọng nam.
- **Chương 4 – Kết quả thực nghiệm:** trình bày môi trường và kịch bản thử nghiệm, quy trình xử lý dữ liệu và kiểm soát chất lượng, các chỉ số đánh giá, kết quả thực nghiệm hệ thống và kết quả huấn luyện mô hình Piper TTS.
- **Chương 5 – Kết luận và Hướng phát triển:** tổng kết đóng góp, nêu hạn chế và đề xuất hướng phát triển trong tương lai.

❌ *(mới viết — rà lại lần cuối sau khi hoàn thiện toàn bộ các chương để khớp tiêu đề/thứ tự thực tế)*

---

# CHƯƠNG 2. TỔNG QUAN TÀI LIỆU VÀ CƠ SỞ LÝ THUYẾT

> Nguồn: docx "CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ", bê **đầy đủ** và sắp xếp lại theo outline 2.1–2.6.

## 2.1. Cơ sở lý thuyết về Nhận dạng tiếng nói (STT)

### 2.1.1. Bài toán nhận dạng tiếng nói streaming trên luồng âm thanh liên tục

Nhận dạng tiếng nói (Speech-to-Text - STT) là quá trình chuyển đổi tín hiệu âm thanh thành văn bản. Đây là một trong những thành phần quan trọng nhất của hệ thống dịch giọng nói sang giọng nói (Speech-to-Speech Translation - S2ST), bởi chất lượng của văn bản đầu ra sẽ ảnh hưởng trực tiếp đến độ chính xác của các giai đoạn dịch máy và tổng hợp tiếng nói phía sau.

Trong các hệ thống nhận dạng tiếng nói truyền thống, dữ liệu âm thanh thường được thu thập dưới dạng một tệp hoàn chỉnh trước khi đưa vào mô hình xử lý. Cách tiếp cận này cho phép mô hình khai thác toàn bộ ngữ cảnh của câu nói để đạt độ chính xác cao. Tuy nhiên, đối với các ứng dụng giao tiếp thời gian thực như hội họp trực tuyến hoặc trợ lý hội thoại, việc chờ người dùng nói xong toàn bộ câu mới tiến hành nhận dạng sẽ làm gia tăng đáng kể độ trễ của hệ thống. Vì vậy, các hệ thống hiện đại thường sử dụng kỹ thuật Streaming STT, trong đó âm thanh được chia thành các đoạn ngắn và truyền liên tục đến máy chủ để xử lý ngay trong quá trình người dùng đang phát biểu.

**Đặc điểm của nhận dạng tiếng nói dạng Streaming.** Khác với nhận dạng tiếng nói trên tệp âm thanh hoàn chỉnh, nhận dạng dạng streaming yêu cầu hệ thống xử lý liên tục các đoạn âm thanh được gửi từ máy khách trong thời gian thực. Mỗi đoạn âm thanh thường chỉ chứa một phần nhỏ của phát ngôn, do đó mô hình phải đưa ra kết quả nhận dạng khi chưa có đầy đủ ngữ cảnh của toàn bộ câu.

Để đáp ứng yêu cầu phản hồi nhanh, nhiều hệ thống streaming cung cấp hai loại kết quả nhận dạng. Kết quả tạm thời (Interim Result) được cập nhật liên tục trong khi người dùng đang nói nhằm cung cấp phản hồi tức thời. Khi hệ thống xác định người dùng đã kết thúc phát ngôn, kết quả cuối cùng (Final Result) sẽ được sinh ra với độ chính xác cao hơn và thay thế các kết quả tạm thời trước đó.

Một trong những thách thức lớn nhất của nhận dạng tiếng nói dạng streaming là sự thiếu hụt ngữ cảnh trong quá trình suy luận. Do mô hình chỉ nhận được một đoạn âm thanh ngắn tại mỗi thời điểm, kết quả nhận dạng tạm thời có thể chưa chính xác hoặc thay đổi khi có thêm dữ liệu đầu vào. Điều này đặc biệt dễ xảy ra đối với các từ đồng âm, các câu có cấu trúc phức tạp hoặc thuật ngữ chuyên ngành. ✅

### 2.1.2. Mô hình Whisper và Faster-Whisper

Trong những năm gần đây, các mô hình nhận dạng tiếng nói dựa trên kiến trúc Transformer đã đạt được nhiều thành công nhờ khả năng khai thác ngữ cảnh dài hạn và xử lý hiệu quả trên nhiều ngôn ngữ khác nhau. Một trong những mô hình tiêu biểu là Whisper do OpenAI phát triển. Mô hình được huấn luyện trên tập dữ liệu âm thanh đa ngôn ngữ có quy mô lớn, cho phép thực hiện các tác vụ như nhận dạng tiếng nói, nhận diện ngôn ngữ và dịch thuật trực tiếp từ tín hiệu âm thanh.

Về mặt kiến trúc, Whisper sử dụng mô hình Encoder-Decoder dựa trên Transformer. Tín hiệu âm thanh đầu vào trước tiên được chuyển đổi thành đặc trưng Mel Spectrogram, sau đó được đưa vào bộ mã hóa (Encoder) để trích xuất các đặc trưng ngữ âm. Bộ giải mã (Decoder) sử dụng cơ chế Self-Attention và Cross-Attention để học mối quan hệ giữa các đặc trưng âm thanh và chuỗi văn bản, từ đó sinh ra kết quả nhận dạng tương ứng. Nhờ khả năng học đầu cuối (End-to-End), Whisper có thể chuyển đổi trực tiếp từ âm thanh sang văn bản mà không cần xây dựng riêng biệt mô hình âm học và mô hình ngôn ngữ như các hệ thống truyền thống.

[[HÌNH: whisper_architecture.png | Kiến trúc tổng quát của mô hình Whisper]]

Để tối ưu tốc độ suy luận phục vụ nhận dạng thời gian thực, đề tài sử dụng Faster-Whisper — bản hiện thực lại của Whisper trên thư viện CTranslate2, hỗ trợ lượng tử hóa và khai thác hiệu quả tài nguyên phần cứng — cho luồng nhận dạng tiếng Anh. Trong cấu hình thực tế, hệ thống dùng biến thể Faster-Whisper *small* (đa ngôn ngữ) với kiểu tính toán float16 trên GPU (fallback float32 khi chạy CPU). ✅ *(đã đối chiếu code: `server/core_ai/stt_engine/base.py`, `faster_whisper_engine.py`)*

### 2.1.3. Mô hình PhoWhisper cho tiếng Việt

Đối với tiếng Việt, đề tài sử dụng PhoWhisper – phiên bản được tinh chỉnh từ Whisper trên dữ liệu tiếng Việt nhằm cải thiện khả năng nhận dạng các đặc điểm ngữ âm và từ vựng đặc thù. So với mô hình gốc, PhoWhisper cho độ chính xác cao hơn khi xử lý tên riêng, thuật ngữ chuyên ngành và các phát ngôn tiếng Việt trong môi trường thực tế. Nhờ những ưu điểm đó, PhoWhisper được lựa chọn làm mô hình nhận dạng tiếng nói cho luồng tiếng Việt trong hệ thống của đồ án. Cụ thể, đề tài sử dụng biến thể **PhoWhisper-medium** đã được chuyển sang định dạng CTranslate2 (`phowhisper-medium-ct2`) để tăng tốc suy luận. ✅ *(đã đối chiếu code: `server/core_ai/stt_engine/base.py`)*

## 2.2. Cơ sở lý thuyết về Dịch máy thần kinh (NMT)

### 2.2.1. Tổng quan kiến trúc NLLB-200

Dịch máy thần kinh (Neural Machine Translation – NMT) là thành phần chịu trách nhiệm chuyển đổi văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích trong hệ thống dịch giọng nói thời gian thực. Những năm gần đây, các mô hình dịch máy dựa trên kiến trúc Transformer đã đạt được nhiều thành tựu nổi bật nhờ khả năng học ngữ cảnh và biểu diễn ngữ nghĩa hiệu quả. Trong số đó, NLLB-200 (No Language Left Behind) là một mô hình dịch đa ngôn ngữ được phát triển nhằm hỗ trợ dịch thuật giữa hàng trăm ngôn ngữ khác nhau, trong đó có tiếng Anh và tiếng Việt.

Khác với bài toán dịch văn bản truyền thống, dữ liệu đầu vào của hệ thống dịch hội thoại thời gian thực được tạo ra từ tầng nhận dạng tiếng nói và thường mang tính tự phát, không hoàn chỉnh về mặt ngữ pháp. Người nói có thể ngắt quãng giữa chừng, sử dụng từ đệm hoặc thay đổi cấu trúc câu trong quá trình phát biểu. Điều này làm cho các đoạn văn bản đầu vào thường ngắn, thiếu ngữ cảnh và khó xác định đầy đủ ý nghĩa của câu nói.

[[HÌNH: nllb200_architecture.png | Kiến trúc tổng quát mô hình NLLB-200]]

Mục tiêu của dự án NLLB là mở rộng khả năng dịch thuật chất lượng cao cho hàng trăm ngôn ngữ trên thế giới, bao gồm cả những ngôn ngữ có nguồn tài nguyên dữ liệu hạn chế. Quá trình huấn luyện bắt đầu từ việc thu thập dữ liệu từ nhiều nguồn khác nhau như NLLB Seed, Public Bitext và các tập dữ liệu đơn ngữ (Monolingual Data). Các nguồn dữ liệu này sau đó được đưa qua bước nhận diện ngôn ngữ và làm sạch nhằm loại bỏ các mẫu dữ liệu không chính xác hoặc không phù hợp. Tiếp theo, công cụ LASER3 được sử dụng để biểu diễn câu dưới dạng vector ngữ nghĩa và khai thác các cặp câu song ngữ có nội dung tương đồng, tạo thành tập dữ liệu song ngữ chất lượng cao (Mined Bitext) phục vụ cho quá trình huấn luyện.

Trên cơ sở nguồn dữ liệu đã được xử lý, mô hình NLLB-200 được huấn luyện bằng nhiều kỹ thuật hiện đại như Mixture of Experts (MoE), Curriculum Learning, Self-Supervised Training và Back-Translation. Các kỹ thuật này giúp mô hình tận dụng hiệu quả cả dữ liệu song ngữ và dữ liệu đơn ngữ, đồng thời nâng cao khả năng dịch thuật đối với các ngôn ngữ có ít tài nguyên huấn luyện. Sau khi hoàn thành quá trình huấn luyện, mô hình được đánh giá thông qua bộ dữ liệu FLORES-200, bộ tiêu chí Toxicity-200 và các đánh giá chủ quan từ con người nhằm kiểm tra độ chính xác, tính tự nhiên cũng như mức độ an toàn của bản dịch.

Nhờ được huấn luyện trên tập dữ liệu đa ngôn ngữ quy mô lớn và hỗ trợ hơn 200 ngôn ngữ khác nhau, NLLB-200 có khả năng tạo ra các bản dịch có chất lượng cao, giữ được ngữ nghĩa của câu nguồn và hạn chế hiện tượng dịch từng từ rời rạc. Đây là một trong những lý do mô hình được lựa chọn làm thành phần dịch máy trong hệ thống dịch giọng nói thời gian thực của đề tài. ✅

### 2.2.2. Lượng tử hóa và tối ưu suy luận với CTranslate2

CTranslate2 là thư viện tối ưu hóa suy luận dành cho các mô hình Transformer. Thư viện hỗ trợ lượng tử hóa mô hình và khai thác hiệu quả tài nguyên phần cứng, giúp tăng tốc độ xử lý của cả Faster-Whisper và NLLB-200. Nhờ đó, hệ thống có thể đáp ứng yêu cầu suy luận thời gian thực ngay cả trong điều kiện tài nguyên GPU hạn chế.

**Khái niệm lượng tử hóa (Quantization).** Lượng tử hóa là kỹ thuật giảm độ chính xác biểu diễn số của trọng số và/hoặc giá trị kích hoạt trong mạng nơ-ron, thay vì lưu và tính toán ở dạng dấu phẩy động 32-bit (FP32) như mặc định. Mục tiêu là giảm dung lượng mô hình, giảm băng thông bộ nhớ và tăng tốc độ tính toán, trong khi vẫn giữ được độ chính xác ở mức chấp nhận được. Cơ sở của kỹ thuật là quan sát rằng các mạng học sâu có khả năng chịu lỗi cao đối với nhiễu lượng tử nhỏ, nên việc hạ độ chính xác thường chỉ làm suy giảm chất lượng không đáng kể.

**Cơ chế lượng tử hóa số nguyên (INT8/INT16).** Với lượng tử hóa số nguyên, dải giá trị dấu phẩy động được ánh xạ tuyến tính (affine) sang dải số nguyên thông qua một hệ số tỷ lệ (scale) và đôi khi một điểm-không (zero-point). Quá trình lượng tử hóa và giải lượng tử hóa có thể biểu diễn xấp xỉ như sau:

$$q = \text{round}(x / s) , \qquad \hat{x} = s \cdot q$$

trong đó $x$ là giá trị FP32 gốc, $s$ là hệ số tỷ lệ, $q$ là giá trị nguyên đã lượng tử, và $\hat{x}$ là giá trị khôi phục. Hệ số $s$ thường được xác định theo từng tensor hoặc theo từng kênh (per-channel) dựa trên biên độ lớn nhất của trọng số. Khi suy luận, các phép nhân ma trận được thực hiện trên số nguyên 8-bit — vốn nhanh hơn nhiều và tiêu thụ ít bộ nhớ hơn so với FP32 — rồi kết quả được giải lượng tử về dấu phẩy động khi cần.

**Lượng tử hóa dấu phẩy động nửa độ chính xác (FP16/BF16).** Bên cạnh số nguyên, mô hình có thể được chuyển sang dạng FP16 hoặc BF16 (16-bit). Cách này giảm một nửa dung lượng so với FP32 và tận dụng được các nhân Tensor Core trên GPU, cho tốc độ cao trong khi mức suy giảm độ chính xác rất nhỏ vì vẫn giữ định dạng dấu phẩy động.

**Vận dụng trong CTranslate2.** CTranslate2 hỗ trợ nhiều chế độ tính toán như `int8`, `int16`, `float16`, `bfloat16` và chế độ lai `int8_float16`; việc lượng tử hóa có thể thực hiện ngay khi nạp mô hình. Ngoài lượng tử hóa, thư viện còn áp dụng các tối ưu khác như hợp nhất lớp (layer fusion), gộp lô (batching) và bộ nhớ đệm cho cơ chế Attention. Trong hệ thống của đề tài, mô hình dịch **NLLB-200 distilled-600M** được chạy qua CTranslate2 với kiểu tính toán **`int8`**, còn mô hình **Faster-Whisper** dùng **`float16`** trên GPU. Nhờ kết hợp các kỹ thuật này, hai mô hình đạt tốc độ suy luận cao và mức tiêu thụ VRAM thấp, phù hợp triển khai trên GPU tầm trung (Google Colab T4). ✅ ⚠️ *(bổ sung trích dẫn APA; số cấu hình đã đối chiếu code: `mt_engine/base.py`, `nllb_ct2_engine.py`)*

## 2.3. Cơ sở lý thuyết về Tổng hợp tiếng nói (TTS) dựa trên kiến trúc VITS

Trong hệ thống Speech-to-Speech Translation (S2ST), tầng cuối cùng chịu trách nhiệm chuyển đổi văn bản đã dịch thành tín hiệu âm thanh để truyền tải tới người nghe. Tầng này bao gồm hai thành phần quan trọng là tổng hợp tiếng nói (Text-to-Speech – TTS) và quản lý luồng âm thanh đầu ra. Chất lượng của giai đoạn này ảnh hưởng trực tiếp đến trải nghiệm giao tiếp thông qua độ tự nhiên của giọng nói, tốc độ phản hồi và khả năng vận hành ổn định trong môi trường hội nghị trực tuyến.

Tổng hợp tiếng nói thời gian thực (Text-to-Speech – TTS) là quá trình chuyển đổi văn bản thành giọng nói nhân tạo. Trong các hệ thống dịch hội thoại, mô hình TTS không chỉ cần tạo ra âm thanh rõ ràng, dễ nghe mà còn phải đảm bảo tốc độ suy luận nhanh để hạn chế độ trễ của toàn bộ hệ thống. Hiện nay, nhiều mô hình TTS hiện đại có thể tạo ra giọng nói với chất lượng rất cao, tuy nhiên thường yêu cầu tài nguyên tính toán lớn và phụ thuộc vào GPU chuyên dụng. Trong khi đó, các kiến trúc tối ưu như VITS và Piper TTS được thiết kế theo hướng học sâu đầu cuối (End-to-End), cho phép tạo ra giọng nói tự nhiên với tốc độ suy luận nhanh và dung lượng mô hình nhỏ, phù hợp cho các ứng dụng thời gian thực trên thiết bị phổ thông.

[[HÌNH: vits_architecture.png | Kiến trúc tổng quát mô hình VITS trong huấn luyện và suy luận]]

### 2.3.1. Phân tích kiến trúc VITS

Mô hình tổng hợp tiếng nói đầu-cuối VITS được sử dụng làm nền tảng cho Piper TTS. VITS cho phép chuyển đổi trực tiếp văn bản đầu vào thành tín hiệu âm thanh mà không cần tách riêng các bước dự đoán phổ âm và vocoder như các hệ thống TTS truyền thống.

Ở giai đoạn huấn luyện (Training Procedure), chuỗi văn bản sau khi được chuyển thành các đơn vị âm vị (Phonemes) sẽ được đưa vào Text Encoder để trích xuất đặc trưng ngôn ngữ. Đồng thời, phổ âm (Linear Spectrogram) của câu nói thực tế được đưa vào Posterior Encoder nhằm học biểu diễn tiềm ẩn của tín hiệu âm thanh. Thành phần Monotonic Alignment Search (MAS) có nhiệm vụ căn chỉnh tự động giữa chuỗi âm vị và tín hiệu âm thanh, giúp mô hình học được mối quan hệ giữa văn bản và giọng nói mà không cần dữ liệu căn chỉnh thủ công. Bên cạnh đó, Stochastic Duration Predictor được sử dụng để dự đoán thời lượng phát âm của từng âm vị, góp phần tạo nên ngữ điệu tự nhiên cho giọng nói tổng hợp.

Trong giai đoạn suy luận (Inference Procedure), mô hình chỉ cần nhận đầu vào là chuỗi âm vị. Text Encoder và Stochastic Duration Predictor sẽ xác định đặc trưng ngôn ngữ và thời lượng phát âm tương ứng. Sau đó, thông qua Flow Decoder và Decoder, mô hình sinh trực tiếp dạng sóng âm thanh (Raw Waveform) ở đầu ra. Nhờ cơ chế học đầu-cuối cùng khả năng căn chỉnh tự động, VITS có thể tạo ra giọng nói có chất lượng tự nhiên cao, đồng thời đạt tốc độ suy luận nhanh hơn nhiều kiến trúc TTS truyền thống. Đây cũng là nền tảng được Piper TTS kế thừa và tối ưu hóa nhằm phục vụ các ứng dụng tổng hợp tiếng nói thời gian thực trên thiết bị có tài nguyên hạn chế. ✅

VITS được xây dựng dưới dạng một bộ tự mã hóa biến phân có điều kiện (Conditional Variational Autoencoder – CVAE), trong đó một biến tiềm ẩn $z$ đóng vai trò cầu nối giữa văn bản (điều kiện $c$) và tín hiệu âm thanh. Mục tiêu huấn luyện là tối đa hóa cận dưới của hàm hợp lý (Evidence Lower Bound – ELBO), gồm thành phần tái tạo và thành phần điều chuẩn Kullback–Leibler (KL) giữa phân phối hậu nghiệm và phân phối tiên nghiệm.

### 2.3.2. Posterior Encoder và Prior Encoder

**Posterior Encoder** nhận đầu vào là phổ tuyến tính (Linear Spectrogram) của câu nói thực và sinh ra phân phối hậu nghiệm $q(z \mid x_{lin})$ của biến tiềm ẩn, thường được mô hình hóa dưới dạng phân phối chuẩn $\mathcal{N}(\mu_\phi, \sigma_\phi)$. Thành phần này được hiện thực bằng các khối tích chập kiểu WaveNet (non-causal) và chỉ tham gia trong giai đoạn huấn luyện, vì khi suy luận hệ thống không có sẵn âm thanh thực.

**Prior Encoder (Text Encoder)** nhận chuỗi âm vị và sinh ra phân phối tiên nghiệm $p(z \mid c)$ có điều kiện theo văn bản. Bộ mã hóa văn bản dựa trên Transformer trích đặc trưng ngôn ngữ, sau đó một lớp chiếu tạo ra các tham số $(\mu_\theta, \sigma_\theta)$ của phân phối tiên nghiệm. Trong huấn luyện, mô hình tối thiểu hóa độ phân kỳ KL giữa $q(z \mid x_{lin})$ và $p(z \mid c)$ để buộc không gian tiềm ẩn học được từ âm thanh khớp với không gian suy ra từ văn bản. ⚠️ *(bổ sung trích dẫn APA: Kim et al., 2021 – VITS)*

### 2.3.3. Normalizing Flows

Phân phối tiên nghiệm chuẩn đơn giản thường không đủ biểu cảm để khớp với phân phối hậu nghiệm phức tạp của tín hiệu âm thanh. Để khắc phục, VITS bổ sung một **luồng chuẩn hóa (Normalizing Flow)** $f_\theta$ — một chuỗi các phép biến đổi khả nghịch — áp lên phân phối tiên nghiệm nhằm tăng độ biểu cảm. Theo công thức đổi biến (change of variables):

$$p(z \mid c) = \mathcal{N}\big(f_\theta(z); \mu_\theta, \sigma_\theta\big) \left| \det \frac{\partial f_\theta(z)}{\partial z} \right|$$

Luồng chuẩn hóa trong VITS được cấu thành từ các lớp ghép affine (affine coupling layers) xếp chồng, bảo đảm vừa khả nghịch vừa tính được định thức Jacobian một cách hiệu quả. Nhờ đó, phân phối tiên nghiệm có thể được "uốn" thành dạng phức tạp gần với phân phối hậu nghiệm, giúp chất lượng tổng hợp tự nhiên hơn. ⚠️ *(bổ sung trích dẫn APA)*

### 2.3.4. HiFi-GAN Decoder và các bộ phân biệt (MPD, MSD)

**Bộ giải mã (Decoder)** của VITS chính là bộ sinh (Generator) của HiFi-GAN: từ biến tiềm ẩn $z$, nó nâng tần số lấy mẫu (upsampling) bằng các lớp tích chập chuyển vị (transposed convolution) kết hợp khối hợp nhất đa trường tiếp nhận (Multi-Receptive Field Fusion – MRF) để sinh trực tiếp dạng sóng âm thanh.

Quá trình huấn luyện sử dụng cơ chế đối kháng (adversarial) với hai nhóm bộ phân biệt:

- **Multi-Period Discriminator (MPD):** biến tín hiệu âm thanh một chiều thành dạng hai chiều theo các chu kỳ khác nhau (ví dụ 2, 3, 5, 7, 11) nhằm nắm bắt các cấu trúc tuần hoàn của giọng nói.
- **Multi-Scale Discriminator (MSD):** đánh giá tín hiệu trên nhiều mức độ phân giải khác nhau (tín hiệu gốc và các phiên bản hạ mẫu) nhằm nắm bắt đặc trưng dài hạn và cấu trúc tổng thể.

Hàm mất mát tổng hợp gồm mất mát đối kháng (GAN loss), mất mát so khớp đặc trưng (feature matching loss) và mất mát tái tạo phổ Mel (mel-spectrogram reconstruction loss). Sự phối hợp giữa bộ sinh và các bộ phân biệt buộc tín hiệu sinh ra ngày càng gần với giọng nói thật về cả độ tự nhiên lẫn chi tiết phổ. ⚠️ *(bổ sung trích dẫn APA: Kong et al., 2020 – HiFi-GAN)*

### 2.3.5. Kiến trúc Piper TTS và mã hóa âm vị espeak-ng cho tiếng Việt

Piper TTS là một hệ tổng hợp tiếng nói mã nguồn mở kế thừa và tối ưu kiến trúc VITS, hướng tới chạy nhanh trên thiết bị tài nguyên hạn chế. Mô hình sau huấn luyện được xuất sang định dạng ONNX, cho phép suy luận trực tiếp trên CPU với độ trễ thấp mà không cần GPU, rất phù hợp để triển khai phía máy khách.

Trước khi đưa vào mô hình, văn bản phải được chuyển thành chuỗi âm vị (phonemes) thông qua bước mã hóa âm vị (phonemization). Piper sử dụng **eSpeak-NG** — một công cụ chuyển văn bản thành âm vị (Grapheme-to-Phoneme – G2P) mã nguồn mở, hỗ trợ nhiều ngôn ngữ và xuất âm vị theo bảng ký hiệu ngữ âm quốc tế (IPA). Với tiếng Việt, eSpeak-NG ánh xạ chữ viết (bao gồm dấu thanh) sang chuỗi âm vị tương ứng để mô hình học mối quan hệ giữa âm vị và tín hiệu âm thanh. Một hạn chế cần lưu ý là khi gặp từ tiếng Anh, tên riêng nước ngoài hoặc ký tự lạ, eSpeak-NG có thể sinh ra các âm vị nằm ngoài tập âm vị mà mô hình nền đã học — đây là vấn đề được xử lý ở Chương 3 (mục 3.5.2, cơ chế đồng bộ âm vị hai giai đoạn). ✅ ⚠️ *(bổ sung trích dẫn APA cho Piper/eSpeak-NG)*

## 2.4. Phân đoạn hoạt động giọng nói bằng Silero VAD

### 2.4.1. Thuật toán phân lớp tín hiệu giọng nói và khoảng lặng

Phát hiện hoạt động giọng nói (Voice Activity Detection – VAD) là bài toán phân loại nhị phân nhằm xác định một đoạn tín hiệu âm thanh là *tiếng nói* (speech) hay *khoảng lặng/nhiễu nền* (silence/noise). Silero VAD là một mô hình mạng nơ-ron nhẹ, được huấn luyện trên tập dữ liệu âm thanh đa ngôn ngữ quy mô lớn. Mô hình nhận đầu vào là các khung âm thanh ngắn (theo từng đoạn vài chục mili-giây) và đưa ra xác suất chứa tiếng nói cho mỗi khung. Bằng cách so xác suất này với một ngưỡng kích hoạt, hệ thống quyết định khung tương ứng là tiếng nói hay khoảng lặng. Nhờ kích thước nhỏ và tốc độ xử lý cao, Silero VAD có thể chạy thời gian thực trên CPU mà không tạo thêm độ trễ đáng kể. ✅ ⚠️ *(bổ sung trích dẫn APA cho Silero VAD)*

### 2.4.2. Vai trò của Silero VAD trong pipeline dịch streaming

Trong hệ thống, Silero VAD đảm nhiệm việc chia đoạn (segmentation) luồng âm thanh đầu vào: xác định chính xác thời điểm bắt đầu và kết thúc phát ngôn để cắt câu động trước khi đưa sang mô-đun nhận dạng. Việc này giúp loại bỏ dữ liệu dư thừa (khoảng lặng), giảm khối lượng tính toán cho STT và cải thiện độ chính xác nhận dạng. Chi tiết thiết kế cắt câu dựa trên ngưỡng thời gian im lặng và cơ chế hangover frame được trình bày ở Chương 3 (mục 3.4.1). ✅

### 2.5.1. Các giải pháp dịch giọng nói hiện có

Các hệ thống dịch giọng nói hiện nay có thể chia thành hai hướng tiếp cận chính. Hướng thứ nhất là kiến trúc phân tầng (cascaded), nối tiếp ba mô-đun STT → MT → TTS; đây là hướng phổ biến nhờ tận dụng được các mô hình mạnh sẵn có cho từng tầng, dễ thay thế và gỡ lỗi, nhưng dễ tích lũy độ trễ và lỗi qua các tầng. Hướng thứ hai là dịch giọng nói đầu-cuối (end-to-end S2ST), tiêu biểu như Translatotron của Google hay SeamlessM4T của Meta, cho phép dịch trực tiếp từ giọng nói nguồn sang giọng nói đích; tuy giàu tiềm năng về bảo toàn ngữ điệu nhưng thường đòi hỏi dữ liệu và tài nguyên tính toán rất lớn.

Về mặt sản phẩm, nhiều nền tảng thương mại đã cung cấp tính năng dịch hội thoại thời gian thực (ví dụ chế độ phiên dịch của Google Translate, Microsoft Translator). Tuy nhiên, các giải pháp này phần lớn vận hành trên hạ tầng đám mây khép kín, tính phí theo mức sử dụng, khó tùy biến và đặt ra lo ngại về quyền riêng tư khi xử lý nội dung cuộc họp. ⚠️ *(bổ sung trích dẫn APA: Translatotron; SeamlessM4T; v.v.)*

### 2.5.2. Hiện trạng mô hình tổng hợp giọng nói tiếng Việt trên Piper

Trong cộng đồng Piper/Rhasspy, tài nguyên mô hình tiếng Việt còn rất hạn chế. Tại thời điểm thực hiện đề tài, mô hình tiếng Việt công khai phổ biến nhất là `vi_VN-vais1000-medium` — một mô hình **giọng nữ**. Cộng đồng gần như chưa có một mô hình **giọng nam** tiếng Việt chất lượng tốt, dung lượng nhẹ, phù hợp cho ứng dụng thời gian thực. Đây là một khoảng trống tài nguyên rõ rệt đối với các hệ thống cần giọng nam tự nhiên cho hội thoại song ngữ. ⚠️ *(bổ sung trích dẫn nguồn kho mô hình Piper/Rhasspy)*

### 2.5.3. Khoảng trống nghiên cứu

Từ phân tích trên, đề tài xác định hai khoảng trống chính. Thứ nhất, về mặt **hệ thống**, còn thiếu các nghiên cứu tập trung tối ưu độ trễ tích lũy (cumulative latency) cho pipeline dịch giọng nói **song hướng theo luồng (streaming bidirectional)** trong điều kiện tài nguyên tính toán giới hạn (một GPU tầm trung như Google Colab T4), đặc biệt là các cơ chế cắt câu động, đệm dịch ngữ cảnh và song song hóa nhằm cân bằng giữa độ trễ và chất lượng. Thứ hai, về mặt **mô hình**, còn thiếu một mô hình TTS giọng nam tiếng Việt chất lượng cao, dung lượng nhẹ, chạy được thời gian thực trên CPU phổ thông. Đề tài hướng tới lấp đồng thời hai khoảng trống này. ✅

## 2.6. Các công nghệ và thư viện sử dụng

> Theo quyết định merge: giữ làm mục con trong Chương 2. Các logo công nghệ (Python, FastAPI, WebSocket, PySide6, PyAudio…) trong docx cũ là ảnh trang trí — tùy chọn chèn lại, không bắt buộc.

### 2.6.1. Ngôn ngữ lập trình Python

Python là ngôn ngữ lập trình bậc cao, mục đích chung, thường được sử dụng để xây dựng phần mềm, tự động hóa tác vụ và phân tích dữ liệu; có thể dùng để tạo nhiều loại chương trình khác nhau mà không chuyên biệt cho một vấn đề cụ thể nào. Trong lĩnh vực khoa học dữ liệu và học máy, Python cho phép thực hiện các phép tính thống kê phức tạp, trực quan hóa dữ liệu, xây dựng thuật toán học máy và xử lý dữ liệu nhờ hệ sinh thái thư viện phong phú như TensorFlow, Keras… Vì những lý do đó, Python được chọn làm ngôn ngữ nền tảng cho cả phía máy chủ và máy khách của hệ thống. ✅

### 2.6.2. Công nghệ phát triển phía máy chủ (Server-side)

Phía máy chủ đảm nhận các tác vụ xử lý trí tuệ nhân tạo có yêu cầu tính toán cao như nhận dạng tiếng nói (STT), dịch máy thần kinh (NMT) và quản lý kết nối thời gian thực giữa các máy khách.

- **FastAPI** là framework phát triển Web API hiện đại cho Python, được xây dựng dựa trên chuẩn ASGI. Framework này hỗ trợ lập trình bất đồng bộ (async/await), giúp xử lý hiệu quả nhiều kết nối đồng thời với độ trễ thấp. Trong đề tài, FastAPI được sử dụng để xây dựng máy chủ trung tâm tiếp nhận dữ liệu âm thanh từ các máy khách và trả về kết quả nhận dạng, dịch thuật theo thời gian thực.
- **WebSocket** là giao thức truyền thông song công (Full-Duplex Communication) cho phép trao đổi dữ liệu hai chiều liên tục giữa máy khách và máy chủ trên cùng một kết nối. Công nghệ này được sử dụng để truyền các khối âm thanh (audio chunks) từ client đến server và nhận kết quả xử lý tức thời mà không cần liên tục tạo mới kết nối HTTP. ✅

### 2.6.3. Công nghệ phát triển phía máy khách (Client-side)

Phía máy khách chịu trách nhiệm thu nhận âm thanh, hiển thị giao diện người dùng, phát âm thanh dịch và quản lý định tuyến âm thanh trong hệ thống.

- **PySide6** là bộ thư viện Python chính thức của Qt Framework. Thư viện được sử dụng để xây dựng giao diện đồ họa người dùng (GUI), cung cấp các thành phần hiển thị văn bản, trạng thái kết nối và kết quả dịch theo thời gian thực.
- **PyAudio** là thư viện giao tiếp với hệ thống âm thanh của máy tính. Trong đề tài, PyAudio được sử dụng để thu âm từ microphone vật lý và phát âm thanh tổng hợp ra loa hoặc tai nghe.
- **SoundCard** là thư viện hỗ trợ truy cập thiết bị âm thanh trên Windows thông qua WASAPI. Thư viện cho phép ghi âm dạng Loopback Capture để thu nhận âm thanh đang phát trên hệ thống mà không yêu cầu quyền quản trị viên.
- **VoiceMeeter Banana** là phần mềm trộn và định tuyến âm thanh ảo (virtual audio mixer) cung cấp **nhiều bus/cáp ảo** thay vì chỉ một cáp đơn. Hệ thống sử dụng VoiceMeeter Banana để định tuyến âm thanh dịch tới phần mềm họp trực tuyến và kiểm soát triệt để hiện tượng vòng lặp tự dịch (self-translation feedback). Cụ thể, luồng dịch của người dùng (Route 0) được đẩy qua `VoiceMeeter Input` rồi ra ngõ micro ảo (bus B1) cho Google Meet/Zoom, trong khi luồng âm thanh cuộc họp (Route 1) đi qua `VoiceMeeter Aux Input` để ứng dụng thu lại và dịch — nhờ tách hai luồng trên các kênh ảo độc lập nên không bị thu chéo gây vòng lặp. Việc định tuyến được điều khiển bằng mã thông qua thư viện `VoicemeeterRemote64.dll`, và ứng dụng có cơ chế tự cài đặt VoiceMeeter (silent install) nếu máy chưa có. ✅ *(đã đối chiếu code: `client/audio/voicemeeter_controller.py`, `install_voicemeeter.py`, `device_router.py`; doc `client/docs/implementation_plan_voicemeeter_routing.md`)*

  > Lưu ý lý do thay đổi: phiên bản trước dùng **VB-Audio Virtual Cable** (một cáp ảo duy nhất) nhưng một luồng ảo đơn không đủ để tách bạch đồng thời luồng phát-đi và luồng thu-về trong chế độ hội thoại song hướng, dẫn tới lặp tiếng hệ thống. VoiceMeeter Banana khắc phục bằng nhiều bus ảo.

### 2.6.4. Thư viện phát triển mô hình AI

Ngoài các mô hình STT/NMT/TTS và VAD đã trình bày ở các mục 2.1–2.4, hệ thống sử dụng thư viện **CTranslate2** để tối ưu hóa suy luận cho Faster-Whisper và NLLB-200 (chi tiết ở mục 2.2.2), và mô hình **Silero VAD** để phát hiện hoạt động giọng nói (chi tiết ở mục 2.4). ✅

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

