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

Trong những năm gần đây, các mô hình nhận dạng tiếng nói dựa trên kiến trúc Transformer [26] đã đạt được nhiều thành công nhờ khả năng khai thác ngữ cảnh dài hạn và xử lý hiệu quả trên nhiều ngôn ngữ khác nhau. Một trong những mô hình tiêu biểu là Whisper do OpenAI phát triển [19]. Mô hình được huấn luyện trên tập dữ liệu âm thanh đa ngôn ngữ có quy mô lớn, cho phép thực hiện các tác vụ như nhận dạng tiếng nói, nhận diện ngôn ngữ và dịch thuật trực tiếp từ tín hiệu âm thanh.

Về mặt kiến trúc, Whisper sử dụng mô hình Encoder-Decoder dựa trên Transformer. Tín hiệu âm thanh đầu vào trước tiên được chuyển đổi thành đặc trưng Mel Spectrogram, sau đó được đưa vào bộ mã hóa (Encoder) để trích xuất các đặc trưng ngữ âm. Bộ giải mã (Decoder) sử dụng cơ chế Self-Attention và Cross-Attention để học mối quan hệ giữa các đặc trưng âm thanh và chuỗi văn bản, từ đó sinh ra kết quả nhận dạng tương ứng. Nhờ khả năng học đầu cuối (End-to-End), Whisper có thể chuyển đổi trực tiếp từ âm thanh sang văn bản mà không cần xây dựng riêng biệt mô hình âm học và mô hình ngôn ngữ như các hệ thống truyền thống.

[[HÌNH: whisper_architecture.png | Kiến trúc tổng quát của mô hình Whisper]]

Để tối ưu tốc độ suy luận phục vụ nhận dạng thời gian thực, đề tài sử dụng Faster-Whisper [24] — bản hiện thực lại của Whisper trên thư viện CTranslate2, hỗ trợ lượng tử hóa và khai thác hiệu quả tài nguyên phần cứng — cho luồng nhận dạng tiếng Anh. Trong cấu hình thực tế, hệ thống dùng biến thể Faster-Whisper *small* (đa ngôn ngữ) với kiểu tính toán float16 trên GPU (fallback float32 khi chạy CPU). ✅ *(đã đối chiếu code: `server/core_ai/stt_engine/base.py`, `faster_whisper_engine.py`)*

### 2.1.3. Mô hình PhoWhisper cho tiếng Việt

Đối với tiếng Việt, đề tài sử dụng PhoWhisper [8] – phiên bản được tinh chỉnh từ Whisper trên dữ liệu tiếng Việt nhằm cải thiện khả năng nhận dạng các đặc điểm ngữ âm và từ vựng đặc thù. So với mô hình gốc, PhoWhisper cho độ chính xác cao hơn khi xử lý tên riêng, thuật ngữ chuyên ngành và các phát ngôn tiếng Việt trong môi trường thực tế. Nhờ những ưu điểm đó, PhoWhisper được lựa chọn làm mô hình nhận dạng tiếng nói cho luồng tiếng Việt trong hệ thống của đồ án. Cụ thể, đề tài sử dụng biến thể **PhoWhisper-medium** đã được chuyển sang định dạng CTranslate2 (`phowhisper-medium-ct2`) để tăng tốc suy luận. ✅ *(đã đối chiếu code: `server/core_ai/stt_engine/base.py`)*

## 2.2. Cơ sở lý thuyết về Dịch máy thần kinh (NMT)

### 2.2.1. Tổng quan kiến trúc NLLB-200

Dịch máy thần kinh (Neural Machine Translation – NMT) là thành phần chịu trách nhiệm chuyển đổi văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích trong hệ thống dịch giọng nói thời gian thực. Những năm gần đây, các mô hình dịch máy dựa trên kiến trúc Transformer đã đạt được nhiều thành tựu nổi bật nhờ khả năng học ngữ cảnh và biểu diễn ngữ nghĩa hiệu quả. Trong số đó, NLLB-200 (No Language Left Behind) [12] là một mô hình dịch đa ngôn ngữ được phát triển nhằm hỗ trợ dịch thuật giữa hàng trăm ngôn ngữ khác nhau, trong đó có tiếng Anh và tiếng Việt.

Khác với bài toán dịch văn bản truyền thống, dữ liệu đầu vào của hệ thống dịch hội thoại thời gian thực được tạo ra từ tầng nhận dạng tiếng nói và thường mang tính tự phát, không hoàn chỉnh về mặt ngữ pháp. Người nói có thể ngắt quãng giữa chừng, sử dụng từ đệm hoặc thay đổi cấu trúc câu trong quá trình phát biểu. Điều này làm cho các đoạn văn bản đầu vào thường ngắn, thiếu ngữ cảnh và khó xác định đầy đủ ý nghĩa của câu nói.

[[HÌNH: nllb200_architecture.png | Kiến trúc tổng quát mô hình NLLB-200]]

Mục tiêu của dự án NLLB là mở rộng khả năng dịch thuật chất lượng cao cho hàng trăm ngôn ngữ trên thế giới, bao gồm cả những ngôn ngữ có nguồn tài nguyên dữ liệu hạn chế. Quá trình huấn luyện bắt đầu từ việc thu thập dữ liệu từ nhiều nguồn khác nhau như NLLB Seed, Public Bitext và các tập dữ liệu đơn ngữ (Monolingual Data). Các nguồn dữ liệu này sau đó được đưa qua bước nhận diện ngôn ngữ và làm sạch nhằm loại bỏ các mẫu dữ liệu không chính xác hoặc không phù hợp. Tiếp theo, công cụ LASER3 được sử dụng để biểu diễn câu dưới dạng vector ngữ nghĩa và khai thác các cặp câu song ngữ có nội dung tương đồng, tạo thành tập dữ liệu song ngữ chất lượng cao (Mined Bitext) phục vụ cho quá trình huấn luyện.

Trên cơ sở nguồn dữ liệu đã được xử lý, mô hình NLLB-200 được huấn luyện bằng nhiều kỹ thuật hiện đại như Mixture of Experts (MoE), Curriculum Learning, Self-Supervised Training và Back-Translation. Các kỹ thuật này giúp mô hình tận dụng hiệu quả cả dữ liệu song ngữ và dữ liệu đơn ngữ, đồng thời nâng cao khả năng dịch thuật đối với các ngôn ngữ có ít tài nguyên huấn luyện. Sau khi hoàn thành quá trình huấn luyện, mô hình được đánh giá thông qua bộ dữ liệu FLORES-200, bộ tiêu chí Toxicity-200 và các đánh giá chủ quan từ con người nhằm kiểm tra độ chính xác, tính tự nhiên cũng như mức độ an toàn của bản dịch.

Nhờ được huấn luyện trên tập dữ liệu đa ngôn ngữ quy mô lớn và hỗ trợ hơn 200 ngôn ngữ khác nhau, NLLB-200 có khả năng tạo ra các bản dịch có chất lượng cao, giữ được ngữ nghĩa của câu nguồn và hạn chế hiện tượng dịch từng từ rời rạc. Đây là một trong những lý do mô hình được lựa chọn làm thành phần dịch máy trong hệ thống dịch giọng nói thời gian thực của đề tài. ✅

### 2.2.2. Lượng tử hóa và tối ưu suy luận với CTranslate2

CTranslate2 [14] là thư viện tối ưu hóa suy luận dành cho các mô hình Transformer. Thư viện hỗ trợ lượng tử hóa mô hình và khai thác hiệu quả tài nguyên phần cứng, giúp tăng tốc độ xử lý của cả Faster-Whisper và NLLB-200. Nhờ đó, hệ thống có thể đáp ứng yêu cầu suy luận thời gian thực ngay cả trong điều kiện tài nguyên GPU hạn chế.

**Khái niệm lượng tử hóa (Quantization).** Lượng tử hóa là kỹ thuật giảm độ chính xác biểu diễn số của trọng số và/hoặc giá trị kích hoạt trong mạng nơ-ron, thay vì lưu và tính toán ở dạng dấu phẩy động 32-bit (FP32) như mặc định. Mục tiêu là giảm dung lượng mô hình, giảm băng thông bộ nhớ và tăng tốc độ tính toán, trong khi vẫn giữ được độ chính xác ở mức chấp nhận được. Cơ sở của kỹ thuật là quan sát rằng các mạng học sâu có khả năng chịu lỗi cao đối với nhiễu lượng tử nhỏ, nên việc hạ độ chính xác thường chỉ làm suy giảm chất lượng không đáng kể.

**Cơ chế lượng tử hóa số nguyên (INT8/INT16).** Với lượng tử hóa số nguyên, dải giá trị dấu phẩy động được ánh xạ tuyến tính (affine) sang dải số nguyên thông qua một hệ số tỷ lệ (scale) và đôi khi một điểm-không (zero-point). Quá trình lượng tử hóa và giải lượng tử hóa có thể biểu diễn xấp xỉ như sau:

$$q = \text{round}(x / s) , \qquad \hat{x} = s \cdot q$$

trong đó $x$ là giá trị FP32 gốc, $s$ là hệ số tỷ lệ, $q$ là giá trị nguyên đã lượng tử, và $\hat{x}$ là giá trị khôi phục. Hệ số $s$ thường được xác định theo từng tensor hoặc theo từng kênh (per-channel) dựa trên biên độ lớn nhất của trọng số. Khi suy luận, các phép nhân ma trận được thực hiện trên số nguyên 8-bit — vốn nhanh hơn nhiều và tiêu thụ ít bộ nhớ hơn so với FP32 — rồi kết quả được giải lượng tử về dấu phẩy động khi cần.

**Lượng tử hóa dấu phẩy động nửa độ chính xác (FP16/BF16).** Bên cạnh số nguyên, mô hình có thể được chuyển sang dạng FP16 hoặc BF16 (16-bit). Cách này giảm một nửa dung lượng so với FP32 và tận dụng được các nhân Tensor Core trên GPU, cho tốc độ cao trong khi mức suy giảm độ chính xác rất nhỏ vì vẫn giữ định dạng dấu phẩy động.

**Vận dụng trong CTranslate2.** CTranslate2 hỗ trợ nhiều chế độ tính toán như `int8`, `int16`, `float16`, `bfloat16` và chế độ lai `int8_float16`; việc lượng tử hóa có thể thực hiện ngay khi nạp mô hình. Ngoài lượng tử hóa, thư viện còn áp dụng các tối ưu khác như hợp nhất lớp (layer fusion), gộp lô (batching) và bộ nhớ đệm cho cơ chế Attention. Trong hệ thống của đề tài, mô hình dịch **NLLB-200 distilled-600M** được chạy qua CTranslate2 với kiểu tính toán **`int8`**, còn mô hình **Faster-Whisper** dùng **`float16`** trên GPU. Nhờ kết hợp các kỹ thuật này, hai mô hình đạt tốc độ suy luận cao và mức tiêu thụ VRAM thấp, phù hợp triển khai trên GPU tầm trung (Google Colab T4). ✅ *(số cấu hình đã đối chiếu code: `mt_engine/base.py`, `nllb_ct2_engine.py`)*

## 2.3. Cơ sở lý thuyết về Tổng hợp tiếng nói (TTS) dựa trên kiến trúc VITS

Trong hệ thống Speech-to-Speech Translation (S2ST), tầng cuối cùng chịu trách nhiệm chuyển đổi văn bản đã dịch thành tín hiệu âm thanh để truyền tải tới người nghe. Tầng này bao gồm hai thành phần quan trọng là tổng hợp tiếng nói (Text-to-Speech – TTS) và quản lý luồng âm thanh đầu ra. Chất lượng của giai đoạn này ảnh hưởng trực tiếp đến trải nghiệm giao tiếp thông qua độ tự nhiên của giọng nói, tốc độ phản hồi và khả năng vận hành ổn định trong môi trường hội nghị trực tuyến.

Tổng hợp tiếng nói thời gian thực (Text-to-Speech – TTS) là quá trình chuyển đổi văn bản thành giọng nói nhân tạo. Trong các hệ thống dịch hội thoại, mô hình TTS không chỉ cần tạo ra âm thanh rõ ràng, dễ nghe mà còn phải đảm bảo tốc độ suy luận nhanh để hạn chế độ trễ của toàn bộ hệ thống. Hiện nay, nhiều mô hình TTS hiện đại có thể tạo ra giọng nói với chất lượng rất cao, tuy nhiên thường yêu cầu tài nguyên tính toán lớn và phụ thuộc vào GPU chuyên dụng. Trong khi đó, các kiến trúc tối ưu như VITS và Piper TTS được thiết kế theo hướng học sâu đầu cuối (End-to-End), cho phép tạo ra giọng nói tự nhiên với tốc độ suy luận nhanh và dung lượng mô hình nhỏ, phù hợp cho các ứng dụng thời gian thực trên thiết bị phổ thông.

[[HÌNH: vits_architecture.png | Kiến trúc tổng quát mô hình VITS trong huấn luyện và suy luận]]

### 2.3.1. Phân tích kiến trúc VITS

Mô hình tổng hợp tiếng nói đầu-cuối VITS [6] được sử dụng làm nền tảng cho Piper TTS. VITS cho phép chuyển đổi trực tiếp văn bản đầu vào thành tín hiệu âm thanh mà không cần tách riêng các bước dự đoán phổ âm và vocoder như các hệ thống TTS truyền thống.

Ở giai đoạn huấn luyện (Training Procedure), chuỗi văn bản sau khi được chuyển thành các đơn vị âm vị (Phonemes) sẽ được đưa vào Text Encoder để trích xuất đặc trưng ngôn ngữ. Đồng thời, phổ âm (Linear Spectrogram) của câu nói thực tế được đưa vào Posterior Encoder nhằm học biểu diễn tiềm ẩn của tín hiệu âm thanh. Thành phần Monotonic Alignment Search (MAS) có nhiệm vụ căn chỉnh tự động giữa chuỗi âm vị và tín hiệu âm thanh, giúp mô hình học được mối quan hệ giữa văn bản và giọng nói mà không cần dữ liệu căn chỉnh thủ công. Bên cạnh đó, Stochastic Duration Predictor được sử dụng để dự đoán thời lượng phát âm của từng âm vị, góp phần tạo nên ngữ điệu tự nhiên cho giọng nói tổng hợp.

Trong giai đoạn suy luận (Inference Procedure), mô hình chỉ cần nhận đầu vào là chuỗi âm vị. Text Encoder và Stochastic Duration Predictor sẽ xác định đặc trưng ngôn ngữ và thời lượng phát âm tương ứng. Sau đó, thông qua Flow Decoder và Decoder, mô hình sinh trực tiếp dạng sóng âm thanh (Raw Waveform) ở đầu ra. Nhờ cơ chế học đầu-cuối cùng khả năng căn chỉnh tự động, VITS có thể tạo ra giọng nói có chất lượng tự nhiên cao, đồng thời đạt tốc độ suy luận nhanh hơn nhiều kiến trúc TTS truyền thống. Đây cũng là nền tảng được Piper TTS kế thừa và tối ưu hóa nhằm phục vụ các ứng dụng tổng hợp tiếng nói thời gian thực trên thiết bị có tài nguyên hạn chế. ✅

VITS được xây dựng dưới dạng một bộ tự mã hóa biến phân có điều kiện (Conditional Variational Autoencoder – CVAE), trong đó một biến tiềm ẩn $z$ đóng vai trò cầu nối giữa văn bản (điều kiện $c$) và tín hiệu âm thanh. Mục tiêu huấn luyện là tối đa hóa cận dưới của hàm hợp lý (Evidence Lower Bound – ELBO), gồm thành phần tái tạo và thành phần điều chuẩn Kullback–Leibler (KL) giữa phân phối hậu nghiệm và phân phối tiên nghiệm.

### 2.3.2. Posterior Encoder và Prior Encoder

**Posterior Encoder** nhận đầu vào là phổ tuyến tính (Linear Spectrogram) của câu nói thực và sinh ra phân phối hậu nghiệm $q(z \mid x_{lin})$ của biến tiềm ẩn, thường được mô hình hóa dưới dạng phân phối chuẩn $\mathcal{N}(\mu_\phi, \sigma_\phi)$. Thành phần này được hiện thực bằng các khối tích chập kiểu WaveNet (non-causal) và chỉ tham gia trong giai đoạn huấn luyện, vì khi suy luận hệ thống không có sẵn âm thanh thực.

**Prior Encoder (Text Encoder)** nhận chuỗi âm vị và sinh ra phân phối tiên nghiệm $p(z \mid c)$ có điều kiện theo văn bản. Bộ mã hóa văn bản dựa trên Transformer trích đặc trưng ngôn ngữ, sau đó một lớp chiếu tạo ra các tham số $(\mu_\theta, \sigma_\theta)$ của phân phối tiên nghiệm. Trong huấn luyện, mô hình tối thiểu hóa độ phân kỳ KL giữa $q(z \mid x_{lin})$ và $p(z \mid c)$ để buộc không gian tiềm ẩn học được từ âm thanh khớp với không gian suy ra từ văn bản [6].

### 2.3.3. Normalizing Flows

Phân phối tiên nghiệm chuẩn đơn giản thường không đủ biểu cảm để khớp với phân phối hậu nghiệm phức tạp của tín hiệu âm thanh. Để khắc phục, VITS bổ sung một **luồng chuẩn hóa (Normalizing Flow)** $f_\theta$ — một chuỗi các phép biến đổi khả nghịch — áp lên phân phối tiên nghiệm nhằm tăng độ biểu cảm. Theo công thức đổi biến (change of variables):

$$p(z \mid c) = \mathcal{N}\big(f_\theta(z); \mu_\theta, \sigma_\theta\big) \left| \det \frac{\partial f_\theta(z)}{\partial z} \right|$$

Luồng chuẩn hóa trong VITS được cấu thành từ các lớp ghép affine (affine coupling layers) xếp chồng, bảo đảm vừa khả nghịch vừa tính được định thức Jacobian một cách hiệu quả. Nhờ đó, phân phối tiên nghiệm có thể được "uốn" thành dạng phức tạp gần với phân phối hậu nghiệm, giúp chất lượng tổng hợp tự nhiên hơn [6].

### 2.3.4. HiFi-GAN Decoder và các bộ phân biệt (MPD, MSD)

**Bộ giải mã (Decoder)** của VITS chính là bộ sinh (Generator) của HiFi-GAN [7]: từ biến tiềm ẩn $z$, nó nâng tần số lấy mẫu (upsampling) bằng các lớp tích chập chuyển vị (transposed convolution) kết hợp khối hợp nhất đa trường tiếp nhận (Multi-Receptive Field Fusion – MRF) để sinh trực tiếp dạng sóng âm thanh.

Quá trình huấn luyện sử dụng cơ chế đối kháng (adversarial) với hai nhóm bộ phân biệt:

- **Multi-Period Discriminator (MPD):** biến tín hiệu âm thanh một chiều thành dạng hai chiều theo các chu kỳ khác nhau (ví dụ 2, 3, 5, 7, 11) nhằm nắm bắt các cấu trúc tuần hoàn của giọng nói.
- **Multi-Scale Discriminator (MSD):** đánh giá tín hiệu trên nhiều mức độ phân giải khác nhau (tín hiệu gốc và các phiên bản hạ mẫu) nhằm nắm bắt đặc trưng dài hạn và cấu trúc tổng thể.

Hàm mất mát tổng hợp gồm mất mát đối kháng (GAN loss), mất mát so khớp đặc trưng (feature matching loss) và mất mát tái tạo phổ Mel (mel-spectrogram reconstruction loss). Sự phối hợp giữa bộ sinh và các bộ phân biệt buộc tín hiệu sinh ra ngày càng gần với giọng nói thật về cả độ tự nhiên lẫn chi tiết phổ.

### 2.3.5. Kiến trúc Piper TTS và mã hóa âm vị espeak-ng cho tiếng Việt

Piper TTS [5] là một hệ tổng hợp tiếng nói mã nguồn mở kế thừa và tối ưu kiến trúc VITS, hướng tới chạy nhanh trên thiết bị tài nguyên hạn chế. Mô hình sau huấn luyện được xuất sang định dạng ONNX, cho phép suy luận trực tiếp trên CPU với độ trễ thấp mà không cần GPU, rất phù hợp để triển khai phía máy khách.

Trước khi đưa vào mô hình, văn bản phải được chuyển thành chuỗi âm vị (phonemes) thông qua bước mã hóa âm vị (phonemization). Piper sử dụng **eSpeak-NG** [4] — một công cụ chuyển văn bản thành âm vị (Grapheme-to-Phoneme – G2P) mã nguồn mở, hỗ trợ nhiều ngôn ngữ và xuất âm vị theo bảng ký hiệu ngữ âm quốc tế (IPA). Với tiếng Việt, eSpeak-NG ánh xạ chữ viết (bao gồm dấu thanh) sang chuỗi âm vị tương ứng để mô hình học mối quan hệ giữa âm vị và tín hiệu âm thanh. Một hạn chế cần lưu ý là khi gặp từ tiếng Anh, tên riêng nước ngoài hoặc ký tự lạ, eSpeak-NG có thể sinh ra các âm vị nằm ngoài tập âm vị mà mô hình nền đã học — vấn đề tương thích âm vị này được xử lý ở khâu tiền xử lý dữ liệu huấn luyện (bảo đảm tập âm vị khớp với mô hình nền). ✅

## 2.4. Phân đoạn hoạt động giọng nói bằng Silero VAD

### 2.4.1. Thuật toán phân lớp tín hiệu giọng nói và khoảng lặng

Phát hiện hoạt động giọng nói (Voice Activity Detection – VAD) là bài toán phân loại nhị phân nhằm xác định một đoạn tín hiệu âm thanh là *tiếng nói* (speech) hay *khoảng lặng/nhiễu nền* (silence/noise). Silero VAD [22] là một mô hình mạng nơ-ron nhẹ, được huấn luyện trên tập dữ liệu âm thanh đa ngôn ngữ quy mô lớn. Mô hình nhận đầu vào là các khung âm thanh ngắn (theo từng đoạn vài chục mili-giây) và đưa ra xác suất chứa tiếng nói cho mỗi khung. Bằng cách so xác suất này với một ngưỡng kích hoạt, hệ thống quyết định khung tương ứng là tiếng nói hay khoảng lặng. Nhờ kích thước nhỏ và tốc độ xử lý cao, Silero VAD có thể chạy thời gian thực trên CPU mà không tạo thêm độ trễ đáng kể. ✅

### 2.4.2. Vai trò của Silero VAD trong pipeline dịch streaming

Trong hệ thống, Silero VAD đảm nhiệm việc chia đoạn (segmentation) luồng âm thanh đầu vào: xác định chính xác thời điểm bắt đầu và kết thúc phát ngôn để cắt câu động trước khi đưa sang mô-đun nhận dạng. Việc này giúp loại bỏ dữ liệu dư thừa (khoảng lặng), giảm khối lượng tính toán cho STT và cải thiện độ chính xác nhận dạng. Chi tiết thiết kế cắt câu dựa trên ngưỡng thời gian im lặng và cơ chế hangover frame được trình bày ở Chương 3 (mục 3.4.1). ✅

### 2.5.1. Các giải pháp dịch giọng nói hiện có

Các hệ thống dịch giọng nói hiện nay có thể chia thành hai hướng tiếp cận chính. Hướng thứ nhất là kiến trúc phân tầng (cascaded), nối tiếp ba mô-đun STT → MT → TTS; đây là hướng phổ biến nhờ tận dụng được các mô hình mạnh sẵn có cho từng tầng, dễ thay thế và gỡ lỗi, nhưng dễ tích lũy độ trễ và lỗi qua các tầng. Hướng thứ hai là dịch giọng nói đầu-cuối (end-to-end S2ST), tiêu biểu như Translatotron của Google [29] hay SeamlessM4T của Meta [30], cho phép dịch trực tiếp từ giọng nói nguồn sang giọng nói đích; tuy giàu tiềm năng về bảo toàn ngữ điệu nhưng thường đòi hỏi dữ liệu và tài nguyên tính toán rất lớn.

Về mặt sản phẩm, nhiều nền tảng thương mại đã cung cấp tính năng dịch hội thoại thời gian thực (ví dụ chế độ phiên dịch của Google Translate, Microsoft Translator). Tuy nhiên, các giải pháp này phần lớn vận hành trên hạ tầng đám mây khép kín, tính phí theo mức sử dụng, khó tùy biến và đặt ra lo ngại về quyền riêng tư khi xử lý nội dung cuộc họp.

### 2.5.2. Hiện trạng mô hình tổng hợp giọng nói tiếng Việt trên Piper

Trong cộng đồng Piper/Rhasspy [5], tài nguyên mô hình tiếng Việt còn rất hạn chế. Tại thời điểm thực hiện đề tài, mô hình tiếng Việt công khai phổ biến nhất là `vi_VN-vais1000-medium` — một mô hình **giọng nữ**. Cộng đồng gần như chưa có một mô hình **giọng nam** tiếng Việt chất lượng tốt, dung lượng nhẹ, phù hợp cho ứng dụng thời gian thực. Đây là một khoảng trống tài nguyên rõ rệt đối với các hệ thống cần giọng nam tự nhiên cho hội thoại song ngữ.

### 2.5.3. Khoảng trống nghiên cứu

Từ phân tích trên, đề tài xác định hai khoảng trống chính. Thứ nhất, về mặt **hệ thống**, còn thiếu các nghiên cứu tập trung tối ưu độ trễ tích lũy (cumulative latency) cho pipeline dịch giọng nói **song hướng theo luồng (streaming bidirectional)** trong điều kiện tài nguyên tính toán giới hạn (một GPU tầm trung như Google Colab T4), đặc biệt là các cơ chế cắt câu động, đệm dịch ngữ cảnh và song song hóa nhằm cân bằng giữa độ trễ và chất lượng. Thứ hai, về mặt **mô hình**, còn thiếu một mô hình TTS giọng nam tiếng Việt chất lượng cao, dung lượng nhẹ, chạy được thời gian thực trên CPU phổ thông. Đề tài hướng tới lấp đồng thời hai khoảng trống này. ✅

## 2.6. Các công nghệ và thư viện sử dụng

> Theo quyết định merge: giữ làm mục con trong Chương 2. Các logo công nghệ (Python, FastAPI, WebSocket, PySide6, PyAudio…) trong docx cũ là ảnh trang trí — tùy chọn chèn lại, không bắt buộc.

### 2.6.1. Ngôn ngữ lập trình Python

Python là ngôn ngữ lập trình bậc cao, mục đích chung, thường được sử dụng để xây dựng phần mềm, tự động hóa tác vụ và phân tích dữ liệu; có thể dùng để tạo nhiều loại chương trình khác nhau mà không chuyên biệt cho một vấn đề cụ thể nào. Trong lĩnh vực khoa học dữ liệu và học máy, Python cho phép thực hiện các phép tính thống kê phức tạp, trực quan hóa dữ liệu, xây dựng thuật toán học máy và xử lý dữ liệu nhờ hệ sinh thái thư viện phong phú như TensorFlow, Keras… Vì những lý do đó, Python được chọn làm ngôn ngữ nền tảng cho cả phía máy chủ và máy khách của hệ thống. ✅

### 2.6.2. Công nghệ phát triển phía máy chủ (Server-side)

Phía máy chủ đảm nhận các tác vụ xử lý trí tuệ nhân tạo có yêu cầu tính toán cao như nhận dạng tiếng nói (STT), dịch máy thần kinh (NMT) và quản lý kết nối thời gian thực giữa các máy khách.

- **FastAPI** [20] là framework phát triển Web API hiện đại cho Python, được xây dựng dựa trên chuẩn ASGI. Framework này hỗ trợ lập trình bất đồng bộ (async/await), giúp xử lý hiệu quả nhiều kết nối đồng thời với độ trễ thấp. Trong đề tài, FastAPI được sử dụng để xây dựng máy chủ trung tâm tiếp nhận dữ liệu âm thanh từ các máy khách và trả về kết quả nhận dạng, dịch thuật theo thời gian thực.
- **WebSocket** là giao thức truyền thông song công (Full-Duplex Communication) cho phép trao đổi dữ liệu hai chiều liên tục giữa máy khách và máy chủ trên cùng một kết nối. Công nghệ này được sử dụng để truyền các khối âm thanh (audio chunks) từ client đến server và nhận kết quả xử lý tức thời mà không cần liên tục tạo mới kết nối HTTP. ✅

### 2.6.3. Công nghệ phát triển phía máy khách (Client-side)

Phía máy khách chịu trách nhiệm thu nhận âm thanh, hiển thị giao diện người dùng, phát âm thanh dịch và quản lý định tuyến âm thanh trong hệ thống.

- **PySide6** [17] là bộ thư viện Python chính thức của Qt Framework. Thư viện được sử dụng để xây dựng giao diện đồ họa người dùng (GUI), cung cấp các thành phần hiển thị văn bản, trạng thái kết nối và kết quả dịch theo thời gian thực.
- **PyAudio** [15] là thư viện giao tiếp với hệ thống âm thanh của máy tính. Trong đề tài, PyAudio được sử dụng để thu âm từ microphone vật lý và phát âm thanh tổng hợp ra loa hoặc tai nghe.
- **SoundCard** [1] là thư viện hỗ trợ truy cập thiết bị âm thanh trên Windows thông qua WASAPI. Thư viện cho phép ghi âm dạng Loopback Capture để thu nhận âm thanh đang phát trên hệ thống mà không yêu cầu quyền quản trị viên.
- **VoiceMeeter Banana** [27] là phần mềm trộn và định tuyến âm thanh ảo (virtual audio mixer) cung cấp **nhiều bus/cáp ảo** thay vì chỉ một cáp đơn. Hệ thống sử dụng VoiceMeeter Banana để định tuyến âm thanh dịch tới phần mềm họp trực tuyến và kiểm soát triệt để hiện tượng vòng lặp tự dịch (self-translation feedback). Cụ thể, luồng dịch của người dùng (Route 0) được đẩy qua `VoiceMeeter Input` rồi ra ngõ micro ảo (bus B1) cho Google Meet/Zoom, trong khi luồng âm thanh cuộc họp (Route 1) đi qua `VoiceMeeter Aux Input` để ứng dụng thu lại và dịch — nhờ tách hai luồng trên các kênh ảo độc lập nên không bị thu chéo gây vòng lặp. Việc định tuyến được điều khiển bằng mã thông qua thư viện `VoicemeeterRemote64.dll`, và ứng dụng có cơ chế tự cài đặt VoiceMeeter (silent install) nếu máy chưa có. ✅ *(đã đối chiếu code: `client/audio/voicemeeter_controller.py`, `install_voicemeeter.py`, `device_router.py`; doc `client/docs/implementation_plan_voicemeeter_routing.md`)*

  > Lưu ý lý do thay đổi: phiên bản trước dùng **VB-Audio Virtual Cable** (một cáp ảo duy nhất) nhưng một luồng ảo đơn không đủ để tách bạch đồng thời luồng phát-đi và luồng thu-về trong chế độ hội thoại song hướng, dẫn tới lặp tiếng hệ thống. VoiceMeeter Banana khắc phục bằng nhiều bus ảo.

### 2.6.4. Thư viện phát triển mô hình AI

Ngoài các mô hình STT/NMT/TTS và VAD đã trình bày ở các mục 2.1–2.4, hệ thống sử dụng thư viện **CTranslate2** để tối ưu hóa suy luận cho Faster-Whisper và NLLB-200 (chi tiết ở mục 2.2.2), và mô hình **Silero VAD** để phát hiện hoạt động giọng nói (chi tiết ở mục 2.4). ✅

---

# CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU ĐỀ XUẤT

> Trọng tâm: phương pháp finetune mô hình (3.1–3.5, ~65%); hệ thống S2ST tích hợp (3.6–3.7, ~35%). Nguồn: `docs_for_report/` + `data_collection/docs_for_report/` (bản đồ CLAUDE.md §11) + code GradProject (§10).

## 3.1. Tổng quan phương pháp và bài toán nghiên cứu

Mục tiêu cốt lõi của phần nghiên cứu là xây dựng một mô hình tổng hợp tiếng nói (TTS) **giọng nam tiếng Việt** chất lượng cao, dung lượng nhẹ, chạy được thời gian thực — phục vụ tầng TTS của hệ thống dịch giọng nói. Thách thức là nguồn mô hình công khai cho tiếng Việt gần như chỉ có giọng nữ (`vi_VN-vais1000-medium`), còn huấn luyện một mô hình giọng nam từ đầu đòi hỏi lượng dữ liệu và tài nguyên rất lớn.

Để giải quyết, đồ án đề xuất hướng **chuyển đổi giới tính giọng nói bằng fine-tuning (cross-gender fine-tuning)** kết hợp **tự xây dựng dữ liệu giọng nam**. Quá trình được tổ chức thành **hai giai đoạn dữ liệu** dẫn tới **ba mô hình**: Giai đoạn 1 dùng dữ liệu công khai VieNeu (mục 3.3) → Model 1 (checkpoint e5219); Giai đoạn 2 tự thu thập dữ liệu từ YouTube (mục 3.4), được thúc đẩy bởi hạn chế của Giai đoạn 1, rồi huấn luyện hai mô hình theo hai chiến lược — Run A (full fine-tune) và Run B1 (partial-freeze + vietnormalizer) (mục 3.5). Ba mô hình được so sánh ở Chương 4 để chọn bản triển khai cuối (Run B1).

[[HÌNH: pipeline_finetune_overview.png | Sơ đồ tổng quát quy trình xây dựng mô hình TTS giọng nam qua hai giai đoạn dữ liệu]] ⚠️ *(cần vẽ sơ đồ tổng quát)*

## 3.2. Chiến lược Cross-Gender Fine-tuning trên kiến trúc VITS

### 3.2.1. Nguyên lý kế thừa mô hình nền

Thay vì huấn luyện từ đầu, đồ án áp dụng **Cross-Gender Fine-tuning** để tận dụng tri thức ngôn ngữ của mô hình nền tiếng Việt. Mô hình khởi tạo là `vi_VN-vais1000-medium` (Piper/VITS, giọng **nữ**, huấn luyện trên tập tiếng Việt lớn, epoch nền 4769). Dù khác biệt âm học giữa giọng nữ và nam, các thành phần xử lý ngôn ngữ của mô hình (biểu diễn âm vị, quy tắc phát âm, ngữ điệu, hệ thanh điệu) đã được học đầy đủ; do đó dùng làm điểm khởi đầu giúp rút ngắn thời gian hội tụ và giữ chất lượng phát âm ngay từ những epoch đầu. Toàn bộ trọng số mô hình nền được dùng làm tham số khởi tạo, sau đó tiếp tục huấn luyện trên tập giọng nam đã tiền xử lý. ✅

### 3.2.2. Dịch chuyển đặc trưng âm học và huấn luyện đối kháng

Về mặt âm học, fine-tuning dịch chuyển không gian biểu diễn từ miền giọng nữ sang miền giọng nam: tần số cơ bản (F0), cấu trúc formant, phổ cộng hưởng và âm sắc được cập nhật dựa trên dữ liệu mới. Kiến trúc VITS dùng huấn luyện đối kháng (Adversarial Training) kết hợp các hàm mất mát tái tạo phổ Mel (Mel-Spectrogram Reconstruction Loss), căn chỉnh đơn điệu (Monotonic Alignment Loss) và các hàm mất mát đặc trưng khác. Bộ phân biệt (Discriminator) liên tục đánh giá để bộ sinh (Generator) tạo tín hiệu ngày càng gần dữ liệu thực, nhờ đó mô hình học đặc trưng giọng nam mà vẫn bảo toàn khả năng phát âm tiếng Việt. ✅

## 3.3. Giai đoạn 1 — Xây dựng dữ liệu từ nguồn công khai VieNeu

### 3.3.1. Khảo sát và lựa chọn nguồn dữ liệu

Đồ án khảo sát nhiều nguồn dữ liệu tiếng nói tiếng Việt. Phương án ban đầu (FPT-FOSD) không phù hợp vì là kho dữ liệu phục vụ nhận dạng (ASR, đa người nói) chứ không phải TTS đơn giọng. Đồ án chuyển sang bộ **VieNeu-TTS-140h** [16] (giấy phép mở, audio chất lượng studio, có nhãn giới tính và người nói). Do thời lượng mỗi người nói nam đơn lẻ nhỏ hơn ngưỡng khuyến nghị (2–3 giờ cho fine-tuning Piper VITS medium), đồ án **ghép ba speaker nam** đồng nhất chất giọng (`jellyfish1010_0004`, `_0013`, `_0032`) để đạt thời lượng đủ. ✅

### 3.3.2. Kiểm soát chất lượng và lọc dữ liệu

Sau khi lọc theo giới tính, theo thời lượng [1,5–16 giây] rồi lấy mẫu theo tỷ lệ, thu được tập thô **1999 clip (~3,65 giờ)**; toàn bộ được chuẩn hóa về 22.050 Hz mono PCM 16-bit, chuẩn loudness -23 LUFS và cắt khoảng lặng đầu/cuối. Để phát hiện hiện tượng lệch nhãn văn bản (do lỗi phân đoạn của bộ dữ liệu gốc), đồ án xây dựng quy trình **kiểm định chất lượng bằng nhận dạng ngược (STT QC)**: dùng **PhoWhisper-large** nhận dạng lại từng clip, chuẩn hóa đối xứng văn bản giả thuyết và tham chiếu rồi tính WER/CER cho mỗi clip. Phân tích cho thấy tỷ lệ lỗi phân bố **rất lệch theo từng speaker**, do đó áp **bộ lọc lai theo speaker (Per-Speaker Hybrid)**: speaker có chất lượng thấp chỉ giữ các mẫu đạt ("Keep"), speaker chất lượng cao được giữ thêm các mẫu sai lệch nhẹ ("Warn"). Kết quả còn **1500 clip ≈ 2,5 giờ** dữ liệu sạch, sau đó chuẩn hóa văn bản bằng **vinorm**.

**Lưu ý quan trọng về số clip thực sự huấn luyện.** Tuy tập sạch có 1500 clip, nhưng khi huấn luyện Model 1, tham số `--max-phoneme-ids 400` của Piper (lọc theo *độ dài chuỗi âm vị* của câu, đặt thấp do lo ngại tràn bộ nhớ GPU với câu dài) đã **loại bỏ 390 clip dài (≈26%)**, nên Model 1 **thực tế chỉ được huấn luyện trên ~1110 clip**. Hạn chế này được rút kinh nghiệm và khắc phục ở Giai đoạn 2 (đo ngưỡng động để giữ 100% clip — xem mục 3.5). Đáng chú ý, **390 clip dài bị loại bỏ lại được tận dụng làm tập kiểm thử (held-out validation) độc lập** ở khâu đánh giá 4 mô hình (Chương 4) — nhờ đó các mô hình được so sánh trên cùng một tập câu chưa từng thấy khi huấn luyện, tăng tính khách quan. ✅

### 3.3.3. Hạn chế của Giai đoạn 1 và động lực sang Giai đoạn 2

Model 1 đạt được giọng nam với độ tự nhiên tốt, nhưng bộc lộ hạn chế rõ về **độ rõ chữ**: tỷ lệ lỗi nhận dạng ngược (WER) cao, nhiều từ bị phát âm sai. Phân tích cho thấy nguyên nhân **không chỉ do dữ liệu ít** (~2,5 giờ, lại chỉ 1110 clip thực huấn luyện), mà còn do **quy trình huấn luyện chưa được tối ưu**: Model 1 thực hiện *full fine-tune* với Learning Rate đi theo lịch mặc định của mô hình nền (chưa kiểm soát chủ động), khiến quá trình huấn luyện dịch chuyển cả những phần vốn đã được huấn luyện tốt của mô hình nền (đặc biệt bộ mã hóa văn bản/thanh điệu), làm phát âm tiếng Việt suy giảm dù vẫn chuyển thành công sang giọng nam.

Hai nhóm hạn chế — *dữ liệu* và *quy trình huấn luyện* — là động lực trực tiếp cho Giai đoạn 2: vừa **tự thu thập một bộ dữ liệu lớn và sạch hơn**, vừa **tối ưu lại quy trình huấn luyện** (đo ngưỡng độ dài động, chủ động kiểm soát Learning Rate, và thử chiến lược đóng băng một phần). ✅

## 3.4. Giai đoạn 2 — Tự thu thập và xử lý dữ liệu từ YouTube

### 3.4.1. Thu thập và tiền xử lý dữ liệu

Đồ án tự xây dựng pipeline thu thập dữ liệu giọng nam từ YouTube (sách nói/podcast cùng một giọng nam đã chọn nghe tay). Quy trình: tải audio bằng **yt-dlp** [28] → nhận dạng kèm mốc thời gian từ bằng **faster-whisper large-v3** [24] → **cắt clip** theo ranh giới câu (mục tiêu ~6 giây) → **khử nhiễu bằng Demucs (htdemucs)** [21] → **chuẩn hóa** về 22.050 Hz mono, loudness -23 LUFS, đệm khoảng lặng đầu 0,2 giây để tránh mất phụ âm đầu câu. ✅

### 3.4.2. Kiểm định nhãn đa nguồn (ASR cross-check) và hiệu đính bằng LLM

Vì nhãn văn bản tự sinh dễ sai, đồ án thiết kế quy trình **kiểm định chéo bằng ba hệ ASR độc lập về kiến trúc**: faster-whisper large-v3, **Qwen3-ASR-1.7B** [18] (chạy cục bộ) và **Deepgram Nova-3** [3] (API). Mỗi clip được so WER chéo giữa ba nguồn, phân loại Keep/Review/Drop theo ngưỡng WER, sau đó dùng **LLM API model Gemini 3.5 flash mới nhất của google hiệu đính theo lô (batch)** để sửa các trường hợp lệch (đặc biệt tên riêng/từ tiếng Anh), tận dụng ngữ cảnh câu lân cận. Kết quả: bộ dữ liệu cuối **2061 clip ≈ 4,22 giờ** (2023 Keep / 306 Drop / 38 Review). ✅

### 3.4.3. Chuẩn hóa văn bản: vinorm và vietnormalizer

Hai chiến lược huấn luyện ở Giai đoạn 2 dùng hai bộ chuẩn hóa văn bản khác nhau: **vinorm** [2] (cho Run A) và **vietnormalizer + danh sách bảo vệ (protect-list)** [11] (cho Run B1). vietnormalizer xử lý tốt hơn các từ tiếng Anh/tên riêng (phiên âm) và làm sạch dấu câu phù hợp với espeak-ng; protect-list ngăn một số từ tiếng Việt không dấu bị phiên âm sai. ✅

## 3.5. Hai chiến lược huấn luyện và tối ưu mô hình

Cả hai mô hình của Giai đoạn 2 đều resume từ nền `vais1000-medium` (epoch nền 4769), preset VITS medium 22.050 Hz, trên cùng bộ dữ liệu tự thu thập 2061 clip. Điểm khác biệt nằm ở **cách khắc phục các vấn đề rút ra từ Model 1** và ở **chiến lược đóng băng tham số**.

### 3.5.1. Bốn cải tiến quy trình huấn luyện ở Giai đoạn 2

Từ kinh nghiệm huấn luyện Model 1, Giai đoạn 2 áp dụng bốn cải tiến quan trọng trong quy trình huấn luyện:

1. **Ngưỡng `max-phoneme-ids` quá thấp làm mất dữ liệu.** Tham số đặt cố định 400 (≈200 âm vị, ~8–10 giây thoại) khiến 26% clip dài bị loại. Khắc phục: ở Giai đoạn 2 **đo phân bố độ dài chuỗi âm vị ngay trong bước tiền xử lý** (max thực đo 857) rồi đặt ngưỡng phủ 100% clip (865 cho Run A, 837 cho Run B1) → **drop 0**.

2. **Mất log loss khi huấn luyện đa phiên.** Việc ghi log TensorBoard bị phân mảnh theo từng phiên Colab và chỉ đồng bộ ở cuối phiên, nên mọi lần mất kết nối giữa chừng đều mất log (Model 1 phải *tính lại loss* từ 84 checkpoint). Khắc phục: **ghi CSV chỉ số mỗi epoch và đẩy lên Drive ngay** (file vài KB, bền vững), kèm cố định một thư mục TensorBoard duy nhất.

3. **Tần suất lưu checkpoint thưa.** Model 1 lưu mỗi 10 epoch, dễ bỏ lỡ checkpoint tốt nhất vì mô hình hội tụ rất nhanh. Khắc phục: **lưu checkpoint mỗi epoch**.

4. **Chủ động kiểm soát Learning Rate khi fine-tune.** Ở Model 1, Learning Rate khi resume đi theo lịch suy giảm mặc định của mô hình nền (≈1,1e-4 → 9,9e-5) — chưa được kiểm soát chủ động. Từ Run A, đồ án **chủ động ép Learning Rate về 1e-4** bằng một callback `on_train_start` (chạy *sau khi* optimizer được khôi phục từ checkpoint) áp cho cả hai optimizer Generator và Discriminator, đồng thời **kiểm chứng giá trị LR thực tế ở bước chạy thử (dry-run)** trước khi huấn luyện đầy đủ (xác nhận `lr_g ≈ lr_d ≈ 1e-4`). Giữ Learning Rate ổn định ở mức thấp giúp fine-tune cross-gender an toàn hơn, hạn chế làm dịch chuyển các tham số ngôn ngữ đã học tốt của mô hình nền.

Để các sửa đổi này minh bạch và kiểm soát được (thay vì vá mù mã nguồn cài sẵn — chính kiểu lỗi "chạy không báo lỗi nhưng âm thầm sai" ở Model 1), đồ án viết một **script huấn luyện tùy biến `train_selfcollect.py`**: tự dựng `Trainer`, gán logger phiên bản cố định, và định nghĩa trực tiếp các callback (ép LR, ghi CSV, đóng băng tham số).

**Bảng so sánh ba mô hình giọng nam:**

[[BẢNG: | So sánh cấu hình huấn luyện ba mô hình Model 1, Run A, Run B1]]

| Tiêu chí | Model 1 (VieNeu) | Run A | Run B1 |
|---|---|---|---|
| Nguồn dữ liệu | VieNeu (công khai) | Tự thu thập YouTube | Tự thu thập YouTube |
| Số clip thực train | 1110 / 1500 (drop 26%) | 2061 (drop 0) | 2061 (drop 0) |
| Chuẩn hóa văn bản | vinorm | vinorm | vietnormalizer + protect-list |
| Kiểm soát LR khi fine-tune | Theo mặc định mô hình nền (chưa chủ động) | Chủ động ép 1e-4 (có kiểm chứng) | Như Run A |
| `max-phoneme-ids` | 400 (cố định) | 865 (đo động) | 837 (đo động) |
| Đóng băng tham số | Không (full FT) | Không (full FT) | **Freeze `enc_p` + `dp`** (395/673 tensor) |

### 3.5.2. Run A — Full fine-tune trên dữ liệu tự thu thập

Run A huấn luyện **toàn bộ trọng số** mô hình (không đóng băng), trên dữ liệu tự thu thập chuẩn hóa bằng vinorm, đã áp dụng đủ bốn sửa đổi ở mục 3.5.1 (đặc biệt là ép đúng LR 1e-4 có kiểm chứng). Run A đóng vai trò **cấu hình đối chứng** kiểu fine-tune truyền thống trên dữ liệu mới — để tách bạch phần cải thiện đến từ *dữ liệu/quy trình* với phần cải thiện đến từ *đóng băng tham số* (Run B1). ✅

### 3.5.3. Run B1 — Đóng băng một phần (partial-freeze)

Run B1 kế thừa toàn bộ cải tiến của Run A nhưng thêm hai thay đổi: dùng bộ chuẩn hóa **vietnormalizer** và **đóng băng một phần** mô hình. Cụ thể, đóng băng bộ mã hóa văn bản/tiên nghiệm `enc_p` và bộ dự đoán thời lượng `dp` (đóng băng **395/673 tensor**), chỉ huấn luyện các thành phần sinh âm. Cơ sở: phân tích biến thiên trọng số của Model 1 cho thấy `enc_p` dịch chuyển nhiều nhất (+1,27%) — chính là phần "hiểu phát âm/thanh điệu tiếng Việt" mà ta **không** muốn để trôi; trong khi đặc trưng giọng nam lại nằm ở decoder và flow.

[[BẢNG: | Phân vai đóng băng/huấn luyện các thành phần VITS ở Run B1]]

| Thành phần | Vai trò | Run B1 |
|---|---|---|
| `enc_p` (Text/Prior Encoder) | Phát âm + thanh điệu tiếng Việt | 🧊 Đóng băng |
| `dp` (Duration Predictor) | Nhịp/ngắt nghỉ | 🧊 Đóng băng |
| `dec` (HiFi-GAN Decoder) | Render timbre/cao độ → quyết định giọng nam | 🔥 Huấn luyện |
| `flow` (Normalizing Flow) | Dịch chuyển latent (pitch/timbre) | 🔥 Huấn luyện |
| `enc_q` (Posterior Encoder) | Mã hóa mel giọng nam (chỉ lúc train) | 🔥 Huấn luyện |
| `model_d` (Discriminator MPD+MSD) | Cân bằng huấn luyện đối kháng | 🔥 Huấn luyện |

> Lưu ý phương pháp: Run A → Run B1 thay đổi **đồng thời hai biến** (đóng băng + bộ chuẩn hóa), nên B1 là một "cấu hình cải tiến tổng hợp" so với Run A, **không phải** một ablation đóng băng thuần túy. ⚠️

## 3.6. Thiết kế hệ thống S2ST realtime (Client–Server)

> Phần ứng dụng tích hợp — trình bày gọn. Mô hình TTS giọng nam tích hợp là **Run B1 (`runB1_e4868`)**.

### 3.6.1. Kiến trúc Client–Server và hai chế độ vận hành

Hệ thống theo mô hình Client–Server, giao tiếp **hai chiều thời gian thực qua WebSocket** (`/ws`) — tức client và server có thể gửi/nhận dữ liệu đồng thời trên cùng một kết nối: client thu/gửi audio và nhận kết quả; server FastAPI chạy ba engine STT–MT–TTS. Khung truyền gồm gói nhị phân (audio chunk kèm route) và khung điều khiển JSON; server định tuyến theo `SessionState` và cơ chế mode-dispatch. ⚠️ *(chi tiết frame/dispatch đọc code khi cần)*

Hệ thống vận hành hai chế độ định tuyến âm thanh:

[[HÌNH: che_do_2_chieu_meeting.png | Chế độ hội thoại 2 chiều – Online Meeting Platform]]

Chế độ 2 chiều (hội thoại – Online Meeting): Route 0 (Việt→Anh) thu từ micro → STT PhoWhisper → NLLB VI→EN → TTS English → định tuyến qua **VoiceMeeter** vào phần mềm họp; Route 1 (Anh→Việt) thu âm cuộc họp qua WASAPI Loopback → STT Faster-Whisper → NLLB EN→VI → TTS Vietnamese → loa/tai nghe vật lý.

[[HÌNH: che_do_1_chieu.png | Chế độ dịch một chiều (video/bài giảng)]]

Chế độ 1 chiều (video/bài giảng): nguồn audio tiếng Anh qua WASAPI Loopback → Route 1 → STT EN → NLLB EN→VI → TTS Vietnamese → loa vật lý. ✅

### 3.6.2. Client (PySide6) và cô lập âm thanh bằng VoiceMeeter Banana

Client xây dựng trên PySide6 + vòng lặp bất đồng bộ `qasync`, thu âm hai tuyến: micro (Route 0) và **WASAPI loopback** (Route 1). Để chống vòng lặp tự dịch trong chế độ hội thoại, hệ thống dùng **VoiceMeeter Banana** (nhiều bus ảo): luồng dịch đi qua `VoiceMeeter Input` → bus B1 (micro ảo cho Meet/Zoom), luồng âm cuộc họp qua `VoiceMeeter Aux Input` để thu và dịch — tách hai luồng trên kênh ảo độc lập nên không bị thu chéo. Điều khiển qua `VoicemeeterRemote64.dll`. ✅

### 3.6.3. Server phân tầng hướng engine

Server áp dụng **Polymorphic Facade** cho ba engine STT/MT/TTS với contract chung (`load_async`, `infer_async`, `cleanup_session`...). Cơ chế **Execution Lane** (thread pool `max_workers=4` + `operation_lock` theo từng entry) ngăn tranh chấp tài nguyên GPU. **Preload & Warmup** nạp sẵn và làm nóng mô hình lúc khởi động để triệt tiêu độ trễ cold-start. ✅

## 3.7. Pipeline streaming STT–MT–TTS thời gian thực

### 3.7.1. Phân đoạn câu bằng Silero VAD và duy trì ngữ cảnh

Luồng PCM 16 kHz được gửi theo khối 200 ms, đưa vào **Silero VAD** ước lượng xác suất tiếng nói. Hệ thống cắt câu động theo ngưỡng im lặng liên tục **450 ms** (thay vì cắt ngay khi có khoảng lặng đầu tiên), kèm **Hangover Frame** (giữ thêm ~400 ms cuối câu) để bảo toàn phụ âm cuối năng lượng thấp (/s/, /t/, /z/). Sau mỗi `stt.final`, bộ đệm âm thanh được giải phóng để tránh tích lũy độ trễ; để không mất ngữ cảnh, hệ thống dùng **Context Sliding Buffer** cấp phần văn bản gần nhất cho mô hình qua `initial_prompt` (đặt `condition_on_previous_text=False` để tránh lặp từ). STT dùng PhoWhisper-medium-ct2 (tiếng Việt) và Faster-Whisper (tiếng Anh). ✅

### 3.7.2. Đệm dịch ngắn, Watchdog và tách câu

**Short-MT Buffering**: gom các cụm ngắn thành câu đủ ngữ cảnh trước khi gửi NLLB-200 (đánh giá theo số từ; chưa đủ ngưỡng thì giữ ở pending buffer), tăng độ chính xác ngữ nghĩa và độ tự nhiên bản dịch; kết quả đóng gói `mt.result` chuyển sang TTS. **Watchdog/Force Flush**: nếu bộ đệm còn dữ liệu và thời gian im lặng vượt ngưỡng thì cưỡng bức đẩy phần còn lại đi (không cần đủ độ dài tối thiểu) để bảo vệ độ trễ — cân bằng với mục tiêu chất lượng của bộ đệm ngữ cảnh. Ngoài ra có cơ chế tách câu đa tầng (SBD) và Comma Fallback Splitter cho suy luận TTS cuốn chiếu, cùng telemetry `pipeline.metric` đo độ trễ từng chặng. ✅ ⚠️ *(SBD & telemetry — đọc code khi rà cuối)*

### 3.7.3. Tích hợp TTS giọng nam và trực quan hóa kết quả

Kết quả nhận dạng truyền về client qua WebSocket dạng interim (cập nhật liên tục nội dung đang nói) và final (kèm `segment_id` để khóa nội dung). Tầng TTS dùng mô hình giọng nam tiếng Việt **`runB1_e4868`** (ONNX) cùng các giọng còn lại, phát ra theo tuyến tương ứng (Route 0/Route 1). ✅

---

# CHƯƠNG 4. THỰC NGHIỆM VÀ KẾT QUẢ

> Nguồn: docx "CHƯƠNG 3" (phần dữ liệu/đánh giá/kết quả) + "CHƯƠNG 4" (rỗng).

## 4.1. Môi trường và kịch bản thử nghiệm

### 4.1.1. Môi trường

Toàn bộ quá trình huấn luyện và đánh giá mô hình TTS được thực hiện trên **Google Colab Pro với GPU NVIDIA Tesla T4 16GB**; các bước xử lý và đánh giá phụ trợ chạy trên môi trường cục bộ (WSL2 Ubuntu / Windows). Do giới hạn thời lượng GPU mỗi phiên Colab, đồ án áp dụng kỹ thuật **đóng gói nhanh môi trường ảo (virtual environment snapshotting)** để khôi phục môi trường giữa các phiên, kết hợp lưu và đồng bộ checkpoint qua Google Drive (rclone). ⚠️ *(đối chiếu `colab/` khi rà cuối)*

### 4.1.2. Kịch bản và tập câu thử nghiệm

Việc đánh giá dùng hai tập câu: **25 câu curated** (đa dạng: câu thông thường, số/ngày/giờ, từ tiếng Anh xen, thanh điệu khó, câu dài) và **300 câu held-out** — lấy từ các clip dài của VieNeu bị loại khỏi huấn luyện Model 1 (xem mục 3.3.2), nên **chưa từng được thấy bởi cả bốn mô hình**, tăng tính khách quan khi so sánh. Hiệu năng suy luận được đo trên **cả CPU và GPU** để phản ánh nhiều ngữ cảnh triển khai. ✅

## 4.2. Kết quả xây dựng tập dữ liệu

### 4.2.1. Giai đoạn 1 — Tập VieNeu sau lọc

Nguồn: tập tiếng nói tiếng Việt công khai **VieNeu-TTS-140h** (73.882 đoạn; trong đó 49.553 clip giọng nam ~94 giờ). Sau khi ghép ba speaker nam đồng nhất chất giọng (`jellyfish1010_0004`, `_0013`, `_0032`) và lấy mẫu theo tỷ lệ, thu được tập thô **1.999 clip (~3,65 giờ)**.

[[HÌNH: vieneu_xephang_person_nam.png | Biểu đồ xếp hạng tổng thời lượng theo từng Person nam trong VieNeu]]
[[HÌNH: vieneu_xephang_speaker_nam.png | Biểu đồ xếp hạng các Speaker nam đơn lẻ có thời lượng lớn nhất]]

Sau chuẩn hóa (22.050 Hz, -23 LUFS, cắt khoảng lặng — bằng Librosa [9] và pyloudnorm [23]) và kiểm soát chất lượng bằng nhận dạng ngược (PhoWhisper-large) + lọc Per-Speaker Hybrid, tập sạch còn **1.500 clip (~2,5 giờ)**. Bước tiền xử lý Piper dùng đúng bản đồ 154 âm vị của mô hình nền (61 âm vị thực dùng, max-id 142). Tuy nhiên khi huấn luyện Model 1, ngưỡng `max-phoneme-ids 400` đã loại 390 clip dài → **thực huấn luyện 1110 clip** (xem mục 3.3.2).

[[HÌNH: vieneu_phanbo_thoiluong_1999.png | Biểu đồ phân bố thời lượng tập 1999 clip giọng nam]]

Phần lớn đoạn nằm trong 1,5–8 giây, trung bình ~3,65 giây. ✅

### 4.2.2. Giai đoạn 2 — Tập tự thu thập từ YouTube

Pipeline tự thu thập (mục 3.4) tạo bộ dữ liệu lớn và sạch hơn. Từ 6 video (cùng một giọng nam) → cắt **2368 clip** → khử nhiễu Demucs → chuẩn hóa → còn **2367 clip**. Khâu kiểm định nhãn đa nguồn (3 hệ ASR + LLM Gemini hiệu đính theo lô) phân loại **2023 Keep / 306 Drop / 38 Review**, cho bộ dữ liệu cuối **2061 clip (~4,22 giờ)** — gấp khoảng 1,7 lần thời lượng và gần 1,9 lần số clip *thực huấn luyện* so với Giai đoạn 1. Nhờ đo ngưỡng độ dài âm vị động (max thực 857 → đặt 865 cho Run A, 837 cho Run B1), hai run **giữ 100% clip** (drop 0), khác hẳn mức loại ~27% nếu vẫn giữ ngưỡng 400. ✅

## 4.3. Chỉ số và phương pháp đánh giá

Mô hình được đánh giá đa chiều, **so sánh tương đối giữa các mô hình trên cùng tập câu** (do âm thanh tổng hợp không có giọng nam tham chiếu gốc để so tuyệt đối):

- **Độ rõ chữ (Intelligibility):** WER/CER theo phương pháp hồi chuyển — nhận dạng ngược âm thanh tổng hợp rồi so với văn bản gốc (tính bằng thư viện jiwer [25]) — dùng **hai hệ ASR độc lập** (PhoWhisper-large [8] và Whisper-large-v3 [19]) để tăng độ tin cậy của thứ hạng.
- **Độ tự nhiên (Naturalness):** điểm **NISQA-TTS MOS** [10] (thang 1–5); kèm khảo sát chủ quan (Human MOS) để đối chiếu.
- **Đặc trưng giọng nam:** tần số cơ bản **F0** (xác thực việc chuyển giới tính giọng) và trọng tâm phổ (spectral centroid) cho âm sắc.
- **Hiệu năng:** **Real-Time Factor (RTF)** đo trên cả CPU và GPU; Mel Reconstruction Loss theo dõi hội tụ huấn luyện.

[[BẢNG: | Tổng hợp các nhóm chỉ số đánh giá mô hình TTS]]

| Nhóm | Chỉ số | Ý nghĩa |
|---|---|---|
| Độ rõ chữ | WER, CER (2 ASR, hồi chuyển) | Tỷ lệ lỗi từ/ký tự khi nhận dạng lại |
| Tự nhiên | NISQA MOS, Human MOS | Mức độ giống giọng người (1–5) |
| Giọng nam | F0, spectral centroid | Cao độ và âm sắc (xác thực cross-gender) |
| Hiệu năng | RTF (CPU/GPU), Mel loss | Tốc độ suy luận; hội tụ huấn luyện |

*(Đo độ trễ tích lũy End-to-End của pipeline S2S được trình bày ở mục 4.6.)* ✅

## 4.4. Kết quả huấn luyện các mô hình

### 4.4.1. Model 1 (VieNeu) — đường cong hội tụ và chọn checkpoint

Model 1 fine-tune từ `vais1000-medium` (epoch nền 4769). Do log TensorBoard bị phân mảnh theo phiên, đồ án **tính lại loss** cho 84 checkpoint bằng `trainer.validate()`. Loss giảm rất nhanh ở giai đoạn đầu (giảm ~72% chỉ trong 10 epoch đầu) rồi đi vào vùng phẳng. Checkpoint **e5219** đạt val_loss trung bình trượt (MA5) thấp nhất **≈32,98** nên được chọn (thay vì checkpoint cuối e5599 ≈ 33,98).

[[HÌNH: piper_mel_kl_loss.png | Đường cong hội tụ loss của Model 1 (VieNeu)]] ✅

### 4.4.2. Run A và Run B1 — giám sát và so sánh quá trình huấn luyện

Run A và Run B1 đều huấn luyện ~99 epoch (≈3,5–3,7 giờ trên T4), lưu checkpoint mỗi epoch. So sánh động học ba run trên trục epoch tương đối so với mô hình nền:

[[HÌNH: compare_normalized.png | So sánh tốc độ hội tụ chuẩn hóa ba run (VieNeu, Run A, Run B1)]]
[[BẢNG: | So sánh quá trình huấn luyện ba run]]

| Run | Số epoch | Epochs-to-95% | Best checkpoint |
|---|---|---|---|
| VieNeu (Model 1) | ~830 | 450 | e5219 |
| Run A (full FT) | 99 | 78 | ep4862 |
| Run B1 (đóng băng) | 99 | **68** | ep4868 |

Quan sát: dữ liệu tự thu thập (Run A/B1) **hội tụ nhanh và dứt khoát hơn** dataset VieNeu (chạm 95% quãng hội tụ chỉ sau ~70–80 epoch so với ~450); Run B1 (đóng băng `enc_p`+`dp`) hội tụ nhanh hơn Run A một chút do ít tham số huấn luyện. Cả ba run đều **GAN ổn định, không collapse và không quá khớp** (checkpoint tốt nhất nằm ở cuối quỹ đạo); xác nhận đóng băng ở Run B1: `enc_p` giữ nguyên (|Δ| = 0) suốt quá trình.

> Lưu ý phương pháp: **val_loss giữa ba run không so sánh tuyệt đối được** vì ba tập validation khác nhau cả về clip lẫn văn bản đích (vinorm so với vietnormalizer); mọi phán quyết chất lượng vì vậy phải dựa trên **tập test chung** (mục 4.5). ⚠️

## 4.5. Đánh giá và so sánh chất lượng mô hình

### 4.5.1. Đánh giá Giai đoạn 1 (ba mô hình)

Ở Giai đoạn 1, đồ án so sánh ba mô hình (baseline giọng nữ, e5219, e5599) trên 25 câu test bằng aggregate-rank năm chỉ số. Cả hai checkpoint fine-tune đạt **NISQA MOS cao hơn baseline** (e5219 = 3,379 so với 3,109, +8,7%) và độ lệch chuẩn MOS giảm (ổn định hơn: 0,685 → 0,472). Đánh đổi: WER tăng (baseline 0,119 → e5219 0,311) do dữ liệu nhỏ và phát âm chưa ổn định. Tổng hợp năm chỉ số, **e5219 cân bằng tốt nhất** (MOS cao nhất, Mel loss thấp nhất, RTF tốt nhất 0,1198) → được chọn làm kết quả Giai đoạn 1. ✅

### 4.5.2. Đánh giá bốn mô hình trên tập chung (Giai đoạn 2)

Giai đoạn 2 đánh giá khách quan **bốn mô hình** — vais1000 (nền, nữ, tham chiếu), VieNeu e5219, Run A, Run B1 — trên **300 câu held-out chung** (đầu vào cả bốn đều qua vietnormalizer để công bằng). Mỗi mô hình tổng hợp 325 câu (tổng 1300 WAV), được chấm bằng hai ASR, NISQA và phân tích F0/phổ.

[[HÌNH: nisqa_mos_boxplot.png | Phân bố điểm NISQA MOS của bốn mô hình]]
[[HÌNH: wer_boxplot.png | Phân bố chỉ số WER của bốn mô hình]]
[[BẢNG: | Kết quả đánh giá tổng hợp bốn mô hình trên tập held-out 300 câu]]

| Mô hình | F0 (Hz) | Giới | WER (PhoWhisper) | WER (Whisper-v3) | CER (Pho) | NISQA MOS | RTF (CPU) |
|---|---|---|---|---|---|---|---|
| vais1000 (nền) | 231,6 | nữ | 3,0 | 4,5 | 1,4 | 3,21 | 0,150 |
| VieNeu e5219 | 114,8 | nam | 12,0 | 25,9 | 7,2 | 3,49 | 0,149 |
| Run A (4862) | 114,5 | nam | 5,4 | 7,6 | 2,9 | 4,10 | 0,152 |
| **Run B1 (4868)** | **112,8** | **nam** | **4,1** | **5,4** | **2,0** | **4,13** | 0,150 |

Nhận xét chính: (1) hai ASR **đồng thuận thứ hạng độ rõ chữ** `vais1000 < B1 < A < VieNeu`; (2) **Run B1 rõ chữ nhất nhóm nam** (WER giảm ~24–29% so với Run A) và sát baseline nữ — chứng tỏ đóng băng `enc_p`/`dp` cùng vietnormalizer giúp giữ phát âm tiếng Việt; (3) Run A và Run B1 **tự nhiên nhất** (NISQA ≥4,0 mức GOOD), cao hơn cả baseline; (4) cả ba mô hình nam đạt **F0 ~113 Hz** (đúng vùng giọng nam) so với 231,6 Hz của giọng nữ nền → **xác thực chuyển giới tính giọng thành công**; (5) self-collect (Run A/B1) cải thiện toàn diện so với VieNeu e5219.

[[HÌNH: final_radar_phase9.png | Biểu đồ radar tổng hợp chuẩn hóa bốn mô hình]]

### 4.5.3. Quyết định triển khai: Run B1

Loại vais1000 (giọng nữ, sai mục tiêu) khỏi nhóm ứng viên, **Run B1 (`runB1_e4868`) đứng đầu cả bốn chỉ số nhóm nam** (WER hai ASR, CER, NISQA) — thứ hạng tổng hoàn hảo, vượt Run A và VieNeu — nên được **chọn làm mô hình triển khai cuối** trong hệ thống S2S. Ghi nhận trung thực: các chỉ số WER/NISQA là so sánh *tương đối* trên audio tổng hợp (không có giọng nam tham chiếu gốc); và Run A → B1 đổi đồng thời hai biến (đóng băng + vietnormalizer) nên không phải ablation thuần. ✅

### 4.5.4. Hiệu năng suy luận (CPU/GPU) và dung lượng mô hình

Bốn mô hình có RTF gần như bằng nhau (cùng kiến trúc medium 22.050 Hz): **~0,15 trên CPU 2 nhân** (nhanh ~6,7× thời gian thực) và **~0,009 trên GPU** (~64 ms/câu) → đủ đáp ứng pipeline S2S thời gian thực ngay cả khi chỉ có CPU.

[[BẢNG: | Hiệu năng suy luận RTF trên CPU và GPU của bốn mô hình]]

| Mô hình | RTF CPU | ms/câu (CPU) | RTF GPU | ms/câu (GPU) |
|---|---|---|---|---|
| vais1000 | 0,150 | 1019 | 0,0094 | 64 |
| VieNeu e5219 | 0,149 | 1111 | 0,0091 | 68 |
| Run A | 0,152 | 1044 | 0,0092 | 64 |
| Run B1 | 0,150 | 1023 | 0,0093 | 64 |

Mô hình được xuất sang **ONNX FP32 (~63,5 MB)** [13] để triển khai. Phương án lượng tử hóa **FP16** (giảm khoảng một nửa dung lượng) từng được dự kiến nhưng **không áp dụng**: bản FP32 đã đủ nhẹ và nhanh trên cả CPU lẫn GPU (RTF rất thấp), đồng thời việc xuất FP16 cho kiến trúc VITS còn gặp vướng mắc tương thích (Cast node) ở ONNX Runtime. Phần phân tích phổ và F0 (centroid giảm dần vais1000 → Run B1, xác nhận âm sắc nam tính nhất ở B1) được trình bày kèm các biểu đồ phổ. ✅

[[HÌNH: melspec_baseline_vs_male.png | So sánh phổ Mel-Spectrogram giữa mô hình nền (nữ) và mô hình giọng nam sau fine-tuning]]

## 4.6. Kết quả tích hợp và vận hành hệ thống S2ST

Hệ thống S2S đã được hoàn thiện và vận hành ổn định end-to-end cho cả hai chiều dịch trong cùng một phiên WebSocket. Phần này trình bày kết quả ở mức **chức năng và định tính**; các đặc tính tối ưu độ trễ được phân tích theo cơ chế thiết kế (việc đo độ trễ tích lũy định lượng đầy đủ được xem là hạn chế, nêu ở Chương 5).

### 4.6.1. Kết quả chức năng ứng dụng client

Ứng dụng client (PySide6) hoàn thiện các chức năng cốt lõi và chạy ổn định:

- **Kết nối và phiên làm việc:** kết nối server qua WebSocket (hỗ trợ URL động/cố định), bắt tay phiên và khởi tạo đồng thời hai tuyến dịch; tự kết nối lại khi mất kết nối.
- **Hai chiều song song:** Route 0 (Việt→Anh) từ micro và Route 1 (Anh→Việt) từ âm thanh hệ thống chạy đồng thời, hiển thị trên **hai khung transcript riêng** với kết quả tạm thời (interim) cập nhật liên tục rồi chốt thành kết quả cuối (final), không lẫn hai chiều.
- **Warmup tự động:** sau khi vào phiên, client tự "làm nóng" pipeline để **loại bỏ độ trễ cold-start ở câu đầu tiên**.
- **Phát âm thanh dịch:** hàng đợi phát theo từng tuyến (không chồng tiếng); âm dịch được định tuyến đúng đích (đưa vào phần mềm họp hoặc phát ra loa người dùng).
- **Cấu hình:** chọn thiết bị micro/loopback/đầu ra, chọn giọng đọc, cỡ chữ; lưu cấu hình giữa các phiên.

Giao diện gồm các thành phần: bảng kết nối, thanh công cụ, khung transcript hai chiều, đồng hồ mức âm (audio level), chân trang chẩn đoán (diagnostics), hộp thoại cài đặt.

[[HÌNH: client_giao_dien_chinh.png | Giao diện chính của ứng dụng client (hai khung transcript Việt–Anh)]]
[[HÌNH: client_settings_dialog.png | Hộp thoại cấu hình thiết bị âm thanh và giọng đọc]]

⚠️ *(ảnh giao diện do người dùng chụp khi chạy thực tế — xem `user_manual_action.md`)*

### 4.6.2. Kiểm thử chức năng end-to-end

Hệ thống được kiểm thử qua các kịch bản chức năng chính, tất cả đều hoạt động đúng:

[[BẢNG: | Các kịch bản kiểm thử chức năng hệ thống]]

| Kịch bản | Kết quả |
|---|---|
| Dịch văn bản một tuyến (mode MT) | Đạt |
| Nhận dạng streaming một tuyến (interim + final) | Đạt |
| Dịch hai tuyến song song (mic + loopback), hai khung không lẫn | Đạt |
| Tách câu dài thành nhiều đoạn TTS (chunk theo thứ tự) | Đạt |
| Tự kết nối lại khi mất kết nối server | Đạt |
| Kết thúc phiên sạch (flush câu cuối) | Đạt |
| Warmup loại bỏ trễ cold-start câu đầu | Đạt |

⚠️ *(xác nhận lại kết quả từng kịch bản với người dùng nếu cần ghi chi tiết hơn)*

### 4.6.3. Cô lập âm thanh loopback bằng VoiceMeeter

Trong kịch bản họp trực tuyến song hướng thực tế (Google Meet/Zoom), giải pháp định tuyến qua **VoiceMeeter Banana** (nhiều bus ảo) cho phép đưa luồng dịch vào micro ảo của phần mềm họp và thu âm cuộc họp trên một bus riêng, **xử lý triệt để vòng lặp tự dịch ở mức phần mềm** (âm dịch phát ra không bị thu ngược trở lại). Vọng âm phần cứng (loa↔micro) được loại bỏ bằng cách dùng tai nghe khi sử dụng (xem mục 1.5.1, 3.6.2). ✅

### 4.6.4. Đặc tính độ trễ và khả năng thời gian thực

Hệ thống được thiết kế để giảm độ trễ theo nhiều cơ chế đã trình bày ở Chương 3: **preload + warmup** triệt tiêu độ trễ khởi động lạnh; **cắt câu động bằng VAD + hangover**; **đệm dịch ngắn (Short-MT) và watchdog** cân bằng giữa ngữ cảnh và độ trễ. Tầng TTS đạt RTF rất thấp (~0,009 trên GPU, ~0,15 trên CPU — mục 4.5.4) nên không phải nút thắt.

**Quan sát độ trễ (đo thủ công khi sử dụng thực tế):** độ trễ tích lũy của toàn hệ thống **tăng dần theo độ dài câu** và tập trung chủ yếu ở **bước STT** — do cơ chế VAD phải đợi hết câu (ngưỡng im lặng 450 ms + hangover ~400 ms ≈ 0,85 s) rồi mới phát kết quả cuối (`stt.final`) để chuyển sang dịch. Cụ thể:

- **Kết quả tạm thời (interim)** xuất hiện gần như tức thời, chỉ **~0,3–0,5 s** sau khi người dùng bắt đầu nói → phản hồi thị giác rất mượt.
- **Câu ngắn (~5–10 từ):** độ trễ tích lũy toàn hệ thống khoảng **1–2 s** (tính từ lúc dứt câu đến khi nghe bản dịch).
- **Câu dài:** độ trễ cao hơn, tỷ lệ thuận với độ dài câu, vì VAD chờ trọn câu trước khi nhận dạng.

[[BẢNG: | Ước lượng phân rã độ trễ tích lũy cho một câu ngắn (~5–10 từ)]]

| Thành phần | Ước lượng | Ghi chú |
|---|---|---|
| Chờ điểm kết thúc câu (VAD 450 ms + hangover ~400 ms) | ~0,85 s | thành phần cố định, chiếm chủ yếu |
| Nhận dạng STT (sau khi đủ câu) | ~0,2–0,4 s | |
| Dịch máy MT (NLLB-200 int8) | ~0,1–0,2 s | |
| Tổng hợp TTS + truyền/phát | ~0,1–0,3 s | RTF rất thấp |
| **Tổng (câu ngắn)** | **~1–2 s** | khớp quan sát thực tế |

> Lưu ý: các con số trên là **ước lượng từ đo thủ công kết hợp cấu hình hệ thống**, chưa phải đo bằng công cụ tự động trên nhiều kịch bản (nêu ở Chương 5). Phần lớn độ trễ đến từ thiết kế *chờ trọn câu* của VAD — một đánh đổi có chủ đích để bản dịch đủ ngữ cảnh và tự nhiên hơn. ⚠️

---

# CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

> Nguồn: docx "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN" (mở rộng theo 5.1–5.3).

## 5.1. Những đóng góp chính của đồ án

**5.1.1. Hệ thống dịch giọng nói thời gian thực song hướng Anh–Việt.** Đồ án thiết kế và hiện thực một hệ thống S2S hoàn chỉnh theo kiến trúc Client–Server, tích hợp ba tầng STT–MT–TTS theo luồng (streaming) trong cùng một kết nối WebSocket cho cả hai chiều dịch. Hệ thống áp dụng nhiều cơ chế tối ưu độ trễ (preload/warmup triệt tiêu cold-start, cắt câu động bằng VAD, đệm dịch ngắn kết hợp watchdog) và giải pháp **cô lập âm thanh bằng VoiceMeeter (nhiều bus ảo)** xử lý triệt để vòng lặp tự dịch trong họp trực tuyến. Hệ thống vận hành ổn định, phản hồi gần thời gian thực (~1–2 giây với câu ngắn).

**5.1.2. Mô hình TTS giọng nam tiếng Việt nhẹ, chất lượng cao.** Thông qua quy trình tự thu thập dữ liệu, cross-gender fine-tuning và chiến lược đóng băng một phần, đồ án tạo ra mô hình **Piper TTS giọng nam (Run B1)** đạt WER ~4,1%, NISQA MOS 4,13 (mức GOOD), F0 ~113 Hz (đúng vùng giọng nam), chạy thời gian thực trên CPU (RTF ~0,15) lẫn GPU (RTF ~0,009), dung lượng ONNX ~63,5 MB — góp phần lấp khoảng trống thiếu giọng nam Việt chất lượng trên nền Piper.

**5.1.3. Quy trình xây dựng và kiểm định dữ liệu giọng nói.** Đồ án xây dựng quy trình tự thu thập dữ liệu giọng nam từ nguồn công khai (tải, cắt câu, khử nhiễu, chuẩn hóa) kèm **kiểm định nhãn đa nguồn bằng ba hệ ASR độc lập và hiệu đính bằng LLM**; đồng thời rút ra các bài học phương pháp (chủ động kiểm soát Learning Rate khi resume, đóng băng `enc_p`/`dp` để giữ phát âm tiếng Việt, đo ngưỡng độ dài âm vị động) có thể tái sử dụng cho các bài toán fine-tuning TTS tương tự. ✅

## 5.2. Các hạn chế

- **Phụ thuộc GPU đám mây:** tầng server (STT, MT, TTS) hiện chạy trên Google Colab T4, chưa triển khai hoàn toàn cục bộ trên máy người dùng.
- **Độ trễ tăng theo độ dài câu:** do cơ chế VAD chờ trọn câu mới nhận dạng, câu càng dài độ trễ càng cao; đồ án mới đo độ trễ End-to-End ở mức **quan sát/ước lượng thủ công**, chưa đo định lượng tự động trên nhiều kịch bản.
- **Dữ liệu giọng nam còn hạn chế:** ~4,22 giờ từ một người đọc → mô hình mang đặc trưng một giọng, chưa đa giọng/đa vùng miền.
- **Đánh giá mang tính tương đối:** các chỉ số WER/NISQA so sánh trên audio tổng hợp (không có giọng nam tham chiếu gốc); cấu hình Run B1 đổi đồng thời hai biến (đóng băng + vietnormalizer) nên không phải một ablation thuần.
- **Chưa lượng tử hóa FP16:** việc xuất FP16 cho VITS gặp lỗi tương thích (Cast node) ở ONNX Runtime; hiện dùng FP32 (đã đủ nhẹ và nhanh). ⚠️

## 5.3. Kiến nghị và Hướng phát triển

**5.3.1. Mô hình giọng nam độ nét cao hơn (Run B2 — đang nghiên cứu).** Một hướng đang được nghiên cứu là **chuyển giao kiến trúc liên-cấu-hình (medium → high)**: tái sử dụng các thành phần "lõi ngôn ngữ" (Text/Prior Encoder `enc_p`, Duration Predictor `dp`, Flow, Posterior Encoder) của mô hình medium, ghép vào khung "high" của Piper (decoder HiFi-GAN lớn hơn — 512 kênh, ResBlock1, 4 tầng upsampling), đóng băng `enc_p`/`dp` để giữ phát âm tiếng Việt, rồi huấn luyện lại phần decoder lớn trên **cùng tần số 22.050 Hz**. Mục tiêu là tăng **độ nét và độ tự nhiên của sóng âm** (cần lưu ý: đây là *tăng dung lượng decoder ở cùng sample rate*, không phải nâng tần số lấy mẫu). Hướng này hiện **tạm gác lại** do chi phí huấn luyện lớn (decoder khởi tạo ngẫu nhiên phải học lại từ đầu, cần nhiều phiên GPU), sẽ triển khai khi đủ tài nguyên.

**5.3.2. Các hướng phát triển khác.** Bên cạnh Run B2, đồ án đề xuất thêm một số hướng hoàn thiện. Về **độ trễ**, nghiên cứu cơ chế phát kết quả nhận dạng sớm/tăng dần (incremental) thay vì chờ trọn câu nhằm rút ngắn độ trễ với câu dài, đồng thời xây dựng công cụ đo độ trễ End-to-End định lượng trên nhiều kịch bản để đánh giá chính xác hơn. Về **triển khai**, lượng tử hóa sâu (INT8/INT4) và đưa các mô hình STT/MT chạy trực tiếp trên client nhằm giảm phụ thuộc hạ tầng đám mây, tiến tới một hệ thống có thể hoạt động hoàn toàn cục bộ. Về **mở rộng**, thu thập dữ liệu đa giọng và đa vùng miền cho TTS, hỗ trợ thêm nhiều cặp ngôn ngữ, và nghiên cứu kiến trúc dịch giọng nói đầu-cuối (End-to-End S2ST) nhằm tiếp tục giảm độ trễ và bảo toàn ngữ điệu, cảm xúc của người nói. ✅

---

# DANH MỤC TÀI LIỆU THAM KHẢO

> Định dạng **APA 7th**, sắp xếp theo bảng chữ cái. Ngày truy cập các nguồn phần mềm/online tạm đặt **23/6/2026** — chỉnh theo ngày bạn chốt báo cáo. ⚠️ *(một vài tên tác giả/năm của phần mềm là best-effort, bạn rà lại: vinorm, VietNormalizer)*

[1] Bechtold, B. (n.d.). *SoundCard: A Python library for playing and recording audio* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/bastibe/SoundCard

[2] Dang, N. (n.d.). *Vinorm: Vietnamese text normalization* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/v-nhandt21/Vinorm

[3] Deepgram. (2025). *Nova-3 speech-to-text* [API]. Truy cập ngày 23/6/2026, từ https://deepgram.com/learn/introducing-nova-3-speech-to-text-api

[4] eSpeak NG contributors. (n.d.). *eSpeak NG text-to-speech* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/espeak-ng/espeak-ng

[5] Hansen, M. (n.d.). *Piper: A fast, local neural text-to-speech system* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/rhasspy/piper

[6] Kim, J., Kong, J., & Son, J. (2021). Conditional variational autoencoder with adversarial learning for end-to-end text-to-speech. *Proceedings of the 38th International Conference on Machine Learning (ICML)*, 5530–5540. https://arxiv.org/abs/2106.06103

[7] Kong, J., Kim, J., & Bae, J. (2020). HiFi-GAN: Generative adversarial networks for efficient and high fidelity speech synthesis. *Advances in Neural Information Processing Systems, 33*. https://arxiv.org/abs/2010.05646

[8] Le, T.-T., Nguyen, L. T., & Nguyen, D. Q. (2024). *PhoWhisper: Automatic speech recognition for Vietnamese*. ICLR 2024 (Tiny Papers). https://arxiv.org/abs/2406.02555

[9] McFee, B., Raffel, C., Liang, D., Ellis, D. P. W., McVicar, M., Battenberg, E., & Nieto, O. (2015). librosa: Audio and music signal analysis in Python. *Proceedings of the 14th Python in Science Conference (SciPy 2015)*, 18–24.

[10] Mittag, G., Naderi, B., Chehadi, A., & Möller, S. (2021). NISQA: A deep CNN-self-attention model for multidimensional speech quality prediction with crowdsourced datasets. *Interspeech 2021*, 2127–2131. https://arxiv.org/abs/2104.09494

[11] Nghime Studio. (2026). *VietNormalizer: An open-source, dependency-free Python library for Vietnamese text normalization in TTS and NLP applications*. arXiv. https://arxiv.org/abs/2603.04145 (mã nguồn: https://github.com/nghimestudio/vietnormalizer)

[12] NLLB Team, Costa-jussà, M. R., Cross, J., Çelebi, O., Elbayad, M., Heafield, K., … Wang, J. (2022). *No language left behind: Scaling human-centered machine translation*. arXiv. https://arxiv.org/abs/2207.04672

[13] ONNX Runtime developers. (n.d.). *ONNX Runtime: Cross-platform, high-performance ML inferencing* [Computer software]. Truy cập ngày 23/6/2026, từ https://onnxruntime.ai

[14] OpenNMT. (n.d.). *CTranslate2: Fast inference engine for Transformer models* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/OpenNMT/CTranslate2

[15] Pham, H. (n.d.). *PyAudio: PortAudio bindings for Python* [Computer software]. Truy cập ngày 23/6/2026, từ https://people.csail.mit.edu/hubert/pyaudio/

[16] pnnbao-ump. (n.d.). *VieNeu-TTS-140h* [Data set]. Hugging Face. Truy cập ngày 23/6/2026, từ https://huggingface.co/datasets/pnnbao-ump/VieNeu-TTS-140h

[17] Qt Company. (n.d.). *PySide6 (Qt for Python)* [Computer software]. Truy cập ngày 23/6/2026, từ https://www.qt.io/qt-for-python

[18] Qwen Team. (2026). *Qwen3-ASR* [Speech recognition model]. Alibaba Cloud / Hugging Face. Truy cập ngày 23/6/2026, từ https://huggingface.co/collections/Qwen/qwen3-asr

[19] Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). *Robust speech recognition via large-scale weak supervision*. arXiv. https://arxiv.org/abs/2212.04356

[20] Ramírez, S. (n.d.). *FastAPI* [Computer software]. Truy cập ngày 23/6/2026, từ https://fastapi.tiangolo.com

[21] Rouard, S., Massa, F., & Défossez, A. (2023). Hybrid transformers for music source separation. *ICASSP 2023*. https://arxiv.org/abs/2211.08553

[22] Silero Team. (n.d.). *Silero VAD: Pre-trained enterprise-grade voice activity detector* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/snakers4/silero-vad

[23] Steinmetz, C. J., & Reiss, J. D. (2021). pyloudnorm: A simple yet flexible loudness meter in Python. *150th AES Convention*. https://github.com/csteinmetz1/pyloudnorm

[24] SYSTRAN. (n.d.). *faster-whisper* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/SYSTRAN/faster-whisper

[25] Vaessen, N. (n.d.). *jiwer: Evaluate speech recognition with word error rate* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/jitsi/jiwer

[26] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*. https://arxiv.org/abs/1706.03762

[27] VB-Audio Software. (n.d.). *VoiceMeeter Banana* [Computer software]. Truy cập ngày 23/6/2026, từ https://vb-audio.com/Voicemeeter/banana.htm

[28] yt-dlp project. (n.d.). *yt-dlp: A feature-rich command-line audio/video downloader* [Computer software]. GitHub. Truy cập ngày 23/6/2026, từ https://github.com/yt-dlp/yt-dlp

[29] Jia, Y., Weiss, R. J., Biadsy, F., Macherey, W., Johnson, M., Chen, Z., & Wu, Y. (2019). Direct speech-to-speech translation with a sequence-to-sequence model. *Interspeech 2019*. https://arxiv.org/abs/1904.06037

[30] Seamless Communication. (2023). *SeamlessM4T: Massively multilingual & multimodal machine translation*. arXiv. https://arxiv.org/abs/2308.11596

# PHỤ LỤC

❌ *(Mã nguồn core_ai, kịch bản lọc dataset hybrid, file cấu hình warmup — theo outline.)*

<!-- TƯ LIỆU GỐC GIỮ LẠI: định nghĩa PlantUML 2 sơ đồ kiến trúc (chế độ 2 chiều & 1 chiều) đã có trong docx cũ, dùng để render ảnh cho mục 3.1.1. -->

