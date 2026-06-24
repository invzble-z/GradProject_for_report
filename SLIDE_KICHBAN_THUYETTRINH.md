# KỊCH BẢN NÓI VÀ HƯỚNG DẪN THIẾT KẾ SLIDE BẢO VỆ ĐỒ ÁN TỐT NGHIỆP

*   **Đề tài:** Nghiên cứu và Phát triển hệ thống dịch thuật giọng nói thời gian thực Anh – Việt với tối ưu hóa độ trễ sử dụng Deep Learning
*   **Thời lượng thuyết trình mục tiêu:** 8 - 10 phút (Khoảng 480 - 600 giây)
*   **Tốc độ nói đề xuất:** ~130 từ/phút (thong thả, rõ ràng, nhấn giọng ở các số liệu định lượng)
*   **Tổng số Slide:** 18 Slide

---

## 💻 SLIDE 1: MỞ ĐẦU & GIỚI THIỆU ĐỀ TÀI
*   **Thời lượng dự kiến:** 30 giây (Nói nhanh, trang trọng)
*   **Bố cục & Ghi chú thiết kế:**
    *   Thiết kế tối giản, hiện đại với tông màu xanh navy chủ đạo (`#1a365d`).
    *   Tiêu đề đề tài viết chữ in hoa, nổi bật ở trung tâm.
    *   Phía dưới ghi rõ: Sinh viên thực hiện, Mã số sinh viên, và Giáo viên hướng dẫn: ThS. Trần Uyên Trang.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Logo trường Đại học Công nghệ Thông tin và Truyền thông Việt - Hàn (VKU) ở góc trên bên trái.
*   **Kịch bản nói (Speech Script):**
    *   "Kính thưa các thầy cô trong Hội đồng đánh giá Đồ án tốt nghiệp. Em tên là **[Họ tên của bạn]**, mã số sinh viên là **[MSSV của bạn]**. Hôm nay, em xin phép được trình bày báo cáo đồ án tốt nghiệp của mình với đề tài: **'Nghiên cứu và Phát triển hệ thống dịch thuật giọng nói thời gian thực Anh – Việt với tối ưu hóa độ trễ sử dụng Deep Learning'**, dưới sự hướng dẫn khoa học của cô **ThS. Trần Uyên Trang**. Sau đây, em xin phép được bắt đầu phần trình bày của mình."

---

## 💻 SLIDE 2: LÝ DO CHỌN ĐỀ TÀI & PHÁT BIỂU BÀI TOÁN
*   **Thời lượng dự kiến:** 40 giây (Nêu bật khó khăn thực tế)
*   **Bố cục & Ghi chú thiết kế:**
    *   Chia làm hai cột trực quan: Cột trái là **Bối cảnh & Nhu cầu**; Cột phải là **4 Thách thức kỹ thuật** tương ứng với 4 bài toán cốt lõi.
    *   Dùng các icon tương ứng để tăng tính sinh động.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Hình ảnh minh họa cuộc họp trực tuyến đa ngôn ngữ bị gián đoạn hoặc gặp rào cản giao tiếp.
*   **Kịch bản nói (Speech Script):**
    *   "Kính thưa Hội đồng, trong kỷ nguyên toàn cầu hóa, nhu cầu giao tiếp song ngữ Anh - Việt qua các nền tảng họp trực tuyến như Zoom hay Google Meet là cực kỳ lớn. Tuy nhiên, việc sử dụng phiên dịch viên truyền thống rất tốn kém và bảo mật kém, còn các công cụ dịch văn bản thông thường lại gây gián đoạn hội thoại. 
    *   Để giải quyết triệt để, chúng ta cần một hệ thống dịch giọng nói sang giọng nói thời gian thực (S2ST). Dù vậy, việc triển khai S2ST trong môi trường thực tế gặp phải 4 bài toán cốt lõi: (1) Nhận dạng tiếng nói streaming trên luồng âm thanh liên tục; (2) Dịch máy hội thoại ngắn, rời rạc mà vẫn bảo toàn ngữ cảnh; (3) Sự thiếu hụt mô hình tổng hợp tiếng nói TTS giọng nam tiếng Việt chất lượng cao, dung lượng nhẹ; và (4) Hiện tượng phản hồi âm học tự dịch tuần hoàn do micro thu ngược lại âm thanh đã dịch từ loa."

---

## 💻 SLIDE 3: MỤC TIÊU & ĐÁNG CHÚ Ý TRONG ĐÓNG GÓP ĐỀ TÀI
*   **Thời lượng dự kiến:** 30 giây (Nhấn mạnh đóng góp)
*   **Bố cục & Ghi chú thiết kế:**
    *   Sử dụng cấu trúc 3 hộp thẻ (card) nằm ngang đại diện cho 3 đóng góp lớn nhất của đề tài.
    *   Mỗi thẻ có tiêu đề viết đậm và số liệu nổi bật.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Biểu tượng huy chương hoặc ngôi sao đại diện cho đóng góp khoa học.
*   **Kịch bản nói (Speech Script):**
    *   "Từ những thách thức đó, đồ án hướng tới xây dựng một hệ thống dịch giọng nói song hướng thời gian thực ổn định và tối ưu độ trễ. Đồ án tự hào mang lại 3 đóng góp thực tiễn chính:
    *   **Thứ nhất:** Một hệ thống pipeline S2ST song hướng hoàn chỉnh tích hợp 3 tầng AI qua kết nối WebSocket song công, đi kèm giải pháp cô lập âm thanh ảo chống vòng lặp phản hồi âm học.
    *   **Thứ hai:** Tinh chỉnh thành công mô hình **Piper TTS giọng nam tiếng Việt Run B1** đạt chất lượng vượt trội với WER ~4.1%, NISQA MOS 4.13, dung lượng siêu nhẹ ~63.5 MB chạy tốt trên CPU phổ thông.
    *   **Thứ ba:** Một quy trình tự xây dựng và kiểm định nhãn dữ liệu giọng nói tự động bằng ba hệ ASR độc lập kết hợp hiệu đính bằng LLM Gemini."

---

## 💻 SLIDE 4: TỔNG QUAN GIẢI PHÁP & CƠ SỞ LÝ THUYẾT
*   **Thời lượng dự kiến:** 40 giây (Nói lướt nhanh)
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ hóa quy trình 3 tầng: STT -> MT -> TTS.
    *   Ghi rõ tên mô hình được lựa chọn dưới mỗi khối để hội đồng thấy rõ cơ sở công nghệ.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\whisper_architecture.png | Kiến trúc Whisper]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\vits_architecture.png | Kiến trúc VITS]]`
*   **Kịch bản nói (Speech Script):**
    *   "Về mặt cơ sở lý thuyết, hệ thống được thiết kế theo kiến trúc phân tầng (cascaded) để tận dụng các mô hình học sâu mạnh nhất hiện nay cho từng chặng. 
    *   Luồng nhận dạng tiếng nói (STT) sử dụng **Faster-Whisper** cho tiếng Anh và **PhoWhisper-medium** được tối ưu hóa qua CTranslate2 cho tiếng Việt. 
    *   Tầng dịch máy (NMT) sử dụng mô hình đa ngôn ngữ **NLLB-200 distilled-600M** lượng tử hóa INT8 giúp bảo toàn ngữ nghĩa hội thoại. 
    *   Tầng tổng hợp tiếng nói (TTS) dựa trên kiến trúc **VITS** - một mạng tự mã hóa biến phân đối kháng (CVAE) sinh trực tiếp sóng âm từ văn bản, được triển khai qua bộ công cụ **Piper TTS** để suy luận tốc độ cao. Luồng dữ liệu được phân đoạn động bởi **Silero VAD** siêu nhẹ chạy trên CPU."

---

## 💻 SLIDE 5: CHIẾN LƯỢC CROSS-GENDER FINE-TUNING TRÊN KIẾN TRÚC VITS
*   **Thời lượng dự kiến:** 45 giây (Bắt đầu phần TTS - Chiếm 65-70% thời lượng chặng kỹ thuật)
*   **Bố cục & Ghi chú thiết kế:**
    *   Giải thích trực quan cơ chế chuyển đổi giới tính giọng nói (Cross-Gender Fine-tuning).
    *   Dùng sơ đồ mũi tên chỉ sự dịch chuyển từ không gian giọng Nữ ( vais1000 ) sang không gian giọng Nam trầm ấm.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Sơ đồ các khối kiến trúc VITS: Đánh dấu đỏ các khối được cập nhật (Decoder, Flow, Posterior Encoder) và màu xanh băng các khối được giữ nguyên (Prior Encoder, Duration Predictor).
*   **Kịch bản nói (Speech Script):**
    *   "Bây giờ, em xin trình bày phần nghiên cứu trọng tâm của đồ án: **Xây dựng mô hình tổng hợp giọng nam tiếng Việt chất lượng cao**. Hiện tại, cộng đồng Piper chỉ có duy nhất một mô hình tiếng Việt giọng nữ là `vais1000-medium`. Việc huấn luyện một mô hình giọng nam từ đầu đòi hỏi tài nguyên GPU và dữ liệu khổng lồ.
    *   Do đó, đồ án đề xuất chiến lược **Cross-Gender Fine-tuning (tinh chỉnh chéo giới tính)**. Ý tưởng cốt lõi là kế thừa toàn bộ 'tri thức ngôn ngữ' (cách phát âm, thanh điệu, ngữ điệu tiếng Việt) đã học rất tốt của mô hình giọng nữ nền. Thông qua quá trình huấn luyện đối kháng và tối ưu hóa hàm loss tái tạo phổ Mel, chúng ta chỉ cần dịch chuyển các đặc trưng âm học như tần số cơ bản F0 và âm sắc từ không gian giọng nữ sang giọng nam trầm ấm mà không cần huấn luyện lại từ đầu bộ mã hóa văn bản."

---

## 💻 SLIDE 6: GIAI ĐOẠN 1 — KHAI THÁC VIENEU & QUY TRÌNH LỌC STT QC
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ hóa quy trình Giai đoạn 1: Dữ liệu thô VieNeu -> Lọc âm lượng/độ dài -> Nhận dạng ngược STT QC -> Bộ lọc Per-Speaker Hybrid -> Tập sạch 1500 clip.
    *   Nhấn mạnh số liệu định lượng: 1999 clip (~3.65h) giảm xuống còn 1500 clip (~2.5h) sạch.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\pipeline_giai_doan_1_vieneu.png | Sơ đồ quy trình Giai đoạn 1]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\vieneu_phanbo_thoiluong_1999.png | Phân bố thời lượng VieNeu]]`
*   **Kịch bản nói (Speech Script):**
    *   "Quy trình R&D được chia thành hai giai đoạn dữ liệu. Trong **Giai đoạn 1**, đồ án khai thác tập dữ liệu studio công khai **VieNeu-TTS-140h**. Chúng em đã ghép dữ liệu của 3 speaker nam có giọng đọc đồng nhất để đạt tổng thời lượng thô là 1999 clip, tương đương 3.65 giờ thoại.
    *   Để kiểm soát chất lượng nhãn văn bản, chúng em thiết kế quy trình **nhận dạng ngược (STT QC)**: dùng **PhoWhisper-large** nhận dạng lại toàn bộ audio, đối sánh và tính toán WER cho từng clip để phát hiện lệch nhãn. Sau khi áp dụng bộ lọc lai theo speaker (Per-Speaker Hybrid), chúng em thu được **1500 clip sạch (~2.5 giờ)**. 
    *   Tuy nhiên, do tham số lọc độ dài âm vị mặc định của Piper đặt quá thấp (`max-phoneme-ids 400`), 390 clip dài (26% dữ liệu) đã bị loại bỏ khi train Model 1. Chúng em đã giữ lại 390 clip này làm **tập kiểm thử độc lập (held-out validation)** để đánh giá khách quan các mô hình sau này."

---

## 💻 SLIDE 7: HẠN CHẾ CỦA GIAI ĐOẠN 1 & ĐỘNG LỰC SANG GIAI ĐOẠN 2
*   **Thời lượng dự kiến:** 40 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Thiết kế đối chiếu: Bên trái là **Hạn chế của Model 1 (VieNeu)**, bên phải là **Giải pháp/Cải tiến đề xuất cho Giai đoạn 2**.
    *   Dùng các gạch đầu dòng ngắn gọn, rõ ý.
*   **Kịch bản nói (Speech Script):**
    *   "Sau khi huấn luyện Model 1 (VieNeu) đạt 830 epoch, mô hình đã chuyển đổi thành công sang giọng nam trầm ấm nhưng bộc lộ hai hạn chế lớn: **độ rõ chữ chưa cao, phát âm một số từ bị méo** và **tỷ lệ WER nhận dạng ngược còn lớn**.
    *   Phân tích sâu cho thấy nguyên nhân ngoài việc dữ liệu thực train quá ít (chỉ 1110 clip), thì quy trình huấn luyện chưa được tối ưu: việc huấn luyện toàn bộ trọng số (full fine-tune) đã vô tình làm dịch chuyển và làm trôi các tham số ngôn ngữ, thanh điệu tiếng Việt vốn đã được học rất tốt ở mô hình nền. 
    *   Hai hạn chế này là động lực trực tiếp để đồ án bước sang **Giai đoạn 2**: vừa tự xây dựng một bộ dữ liệu lớn và sạch hơn từ YouTube, vừa cải tiến triệt để quy trình huấn luyện và đề xuất chiến lược đóng băng tham số."

---

## 💻 SLIDE 8: GIAI ĐOẠN 2 — TỰ THU THẬP DỮ LIỆU & KIỂM ĐỊNH NHÃN ĐA NGUỒN
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ hóa quy trình Giai đoạn 2: Tải video YouTube -> Cắt câu -> Khử nhiễu Demucs -> Kiểm định chéo 3 ASR (Whisper, Qwen, Deepgram) -> Hiệu đính LLM Gemini -> Tập sạch 2061 clip (~4.22h).
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\pipeline_giai_doan_2_selfcollect.png | Sơ đồ quy trình Giai đoạn 2]]`
*   **Kịch bản nói (Speech Script):**
    *   "Trong **Giai đoạn 2**, chúng em tự xây dựng pipeline thu thập dữ liệu giọng nam đơn nguồn từ YouTube. Audio sau khi tải được cắt câu tự động, đưa qua mô hình **Demucs** để khử nhiễu môi trường, chuẩn hóa mono 22.050 Hz và loudness -23 LUFS.
    *   Để đảm bảo nhãn văn bản chính xác tuyệt đối, chúng em đề xuất quy trình **kiểm định chéo đa nguồn (ASR Cross-check)** sử dụng 3 hệ nhận dạng độc lập: Faster-Whisper, Qwen3-ASR (chạy local) và Deepgram Nova-3 (API). Các clip có sự sai lệch nhãn được đưa qua **LLM Gemini 3.5 Flash theo lô (batch)** để hiệu đính nhãn tự động dựa trên ngữ cảnh câu lân cận. Kết quả thu được tập dữ liệu sạch hoàn hảo **2061 clip (~4.22 giờ)** - gấp 1.9 lần số clip thực train ở Giai đoạn 1. Văn bản được chuẩn hóa chuyên biệt bằng `vietnormalizer` kết hợp danh sách bảo vệ từ ngữ."

---

## 💻 SLIDE 9: SO SÁNH HAI CHIẾN LƯỢC HUẤN LUYỆN: RUN A & RUN B1
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Bảng so sánh cấu hình huấn luyện của 3 mô hình: Model 1, Run A và Run B1.
    *   Tô đậm các ô đặc trưng của Run B1: *Đóng băng enc_p + dp*, *vietnormalizer*, *drop 0*.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Bảng so sánh cấu hình huấn luyện (Trích xuất từ bảng 3.5.1 trong báo cáo).
*   **Kịch bản nói (Speech Script):**
    *   "Trên tập dữ liệu tự thu thập chất lượng cao này, đồ án đã triển khai 4 cải tiến quy trình huấn luyện cốt lõi: (1) Đo ngưỡng âm vị động để giữ trọn 100% dữ liệu (drop 0); (2) Ghi log loss CSV thời gian thực tránh mất log; (3) Lưu checkpoint mỗi epoch; và (4) Chủ động ép Learning Rate về đúng 1e-4 có dry-run kiểm chứng để tránh làm trôi mô hình.
    *   Chúng em thiết lập hai chiến lược huấn luyện để đối chứng:
    *   **Run A:** Tiến hành huấn luyện toàn bộ trọng số (full fine-tune) truyền thống.
    *   **Run B1 (Đóng băng một phần - Partial-Freeze):** Chúng em tiến hành **đóng băng bộ mã hóa văn bản tiên nghiệm `enc_p` và bộ dự đoán thời lượng `dp` (khóa chặt 395 trên tổng số 673 tensor)**. Chúng em chỉ cho phép huấn luyện các tầng quyết định âm sắc giọng nam như Decoder, Flow và Posterior Encoder. Mục tiêu là giữ vững khả năng phát âm tiếng Việt chuẩn xác của mô hình nền và bắt buộc mô hình chỉ tập trung học đặc trưng giọng nam ở các tầng sinh âm."

---

## 💻 SLIDE 10: PHÂN TÍCH ĐƯỜNG CONG HUẤN LUYỆN & SỰ HỘI TỤ
*   **Thời lượng dự kiến:** 40 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Đặt hai đồ thị loss cạnh nhau để so sánh trực quan tốc độ hội tụ.
    *   Chỉ rõ thời điểm Run B1 hội tụ vượt trội.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\piper_mel_kl_loss.png | Đường cong hội tụ Model 1]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\compare_normalized.png | So sánh tốc độ hội tụ chuẩn hóa ba run]]`
*   **Kịch bản nói (Speech Script):**
    *   "Phân tích động học huấn luyện qua các đồ thị Mel loss và KL loss mang lại những phát hiện khoa học rất thú vị.
    *   Đầu tiên, tập dữ liệu tự thu thập chất lượng cao ở Giai đoạn 2 giúp mô hình hội tụ nhanh hơn hẳn so với tập dữ liệu công khai VieNeu ở Giai đoạn 1. 
    *   Đặc biệt, cấu hình **Run B1 (đóng băng một phần) đạt tốc độ hội tụ nhanh nhất nhóm, chạm mốc 95% chất lượng hội tụ chỉ sau 68 epoch** (so với 78 epoch của Run A và 450 epoch của VieNeu). Điều này chứng minh việc đóng băng `enc_p` và `dp` đã giúp thu hẹp không gian tối ưu hóa, loại bỏ các tính toán dư thừa, giúp quá trình học diễn ra cực kỳ hiệu quả và ổn định mà không hề xảy ra hiện tượng sụp đổ mạng hay quá khớp."

---

## 💻 SLIDE 11: ĐÁNH GIÁ CHẤT LƯỢNG MÔ HÌNH TRÊN TẬP HELD-OUT 300 CÂU
*   **Thời lượng dự kiến:** 60 giây (Slide số liệu vàng - Nói chậm, nhấn giọng ở các số liệu)
*   **Bố cục & Ghi chú thiết kế:**
    *   Thiết kế bảng số liệu đánh giá 4 mô hình (nền nữ, VieNeu, Run A, Run B1) thật rõ ràng, chữ to, dễ đọc.
    *   Tô màu nổi bật (ví dụ màu vàng hoặc cam) cho dòng số liệu của **Run B1** để làm nổi bật kết quả xuất sắc nhất.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Bảng kết quả đánh giá tổng hợp trên tập held-out 300 câu (Bảng 4.5.2 trong báo cáo).
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\nisqa_mos_boxplot.png | Phân bố điểm NISQA MOS]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\wer_boxplot.png | Phân bố chỉ số WER]]`
*   **Kịch bản nói (Speech Script):**
    *   "Kính thưa Hội đồng, đây chính là **bảng số liệu chứng minh tính đúng đắn và đóng góp khoa học lớn nhất của đồ án**. Chúng em đã thực hiện đánh giá chéo khách quan cả 4 mô hình trên tập kiểm thử độc lập 300 câu held-out chưa từng xuất hiện trong quá trình huấn luyện.
    *   **Về độ rõ chữ (Intelligibility):** Cả hai hệ ASR nhận dạng ngược độc lập đều đồng thuận xếp hạng Run B1 đứng đầu nhóm giọng nam. Chỉ số WER PhoWhisper của **Run B1 chỉ còn 4.1%**, giảm thiểu 24% lỗi từ so với Run A (5.4%) và giảm gần 3 lần so với VieNeu e5219 (12.0%). Điểm CER của Run B1 cũng đạt mức cực thấp là 2.0%, tiệm cận sát nút giọng nữ nền chuẩn studio.
    *   **Về độ tự nhiên (Naturalness):** Mô hình **Run B1 đạt điểm NISQA MOS cao nhất toàn bộ thử nghiệm với 4.13 điểm (mức GOOD)**, vượt qua Run A (4.10) và vượt trội hoàn toàn so với mô hình giọng nữ nền gốc (3.21)."

---

## 💻 SLIDE 12: PHÂN TÍCH ĐẶC TRƯNG ÂM HỌC & QUYẾT ĐỊNH TRIỂN KHAI
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Trực quan hóa sự dịch chuyển tần số cơ bản F0.
    *   Đặt hình ảnh spectrogram của giọng nữ nền và giọng nam Run B1 cạnh nhau để so sánh các dải formant.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\final_radar_phase9.png | Biểu đồ radar tổng hợp]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\melspec_baseline_vs_male.png | So sánh phổ Mel-Spectrogram]]`
*   **Kịch bản nói (Speech Script):**
    *   "Để kiểm chứng đặc trưng vật lý của giọng nam, chúng em tiến hành phân tích tần số cơ bản F0. Kết quả cho thấy **Run B1 đã dịch chuyển tần số F0 cực kỳ thành công về vùng trầm ấm của giọng nam trung bình là 112.8 Hz** (so với giọng nữ nền gốc là 231.6 Hz). Phân tích phổ Mel-Spectrogram cho thấy cấu trúc phổ hài âm và các dải formant được tái tạo rất rõ nét, âm sắc nam tính tự nhiên.
    *   Về mặt hiệu năng, cả 4 mô hình đều đạt hệ số thời gian thực **RTF cực thấp ~0.15 trên CPU 2 nhân** (nhanh gấp 6.7 lần thời gian thực) và **~0.009 trên GPU** (chỉ mất 64ms/câu).
    *   Với chất lượng vượt trội về cả độ rõ chữ, độ tự nhiên và tốc độ suy luận, mô hình **Run B1 (`runB1_e4868`)** xuất định dạng **ONNX FP32 với dung lượng nhẹ ~63.5 MB** đã được quyết định lựa chọn làm mô hình giọng nam Việt chính thức để tích hợp vào hệ thống S2ST."

---

## 💻 SLIDE 13: KIẾN TRÚC TỔNG QUÁT HỆ THỐNG S2ST & WEBSOCKET
*   **Thời lượng dự kiến:** 45 giây (Bắt đầu phần Hệ thống - Chiếm 35% thời lượng chặng kỹ thuật)
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ kiến trúc Client-Server tương tác qua WebSocket song công.
    *   Dùng các mũi tên động thể hiện luồng truyền nhận đồng thời: âm thanh nhị phân đi lên, transcript JSON và âm thanh dịch đi về.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\che_do_2_chieu_meeting.png | Chế độ hội thoại 2 chiều song hướng]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\che_do_1_chieu.png | Chế độ dịch một chiều]]`
*   **Kịch bản nói (Speech Script):**
    *   "Tiếp theo, em xin phép trình bày về **Thiết kế và Tích hợp hệ thống dịch giọng nói thời gian thực S2ST**. Hệ thống được xây dựng theo kiến trúc Client-Server, kết nối qua giao thức **WebSocket song công** cho phép truyền nhận dữ liệu hai chiều đồng thời trên một kênh duy nhất.
    *   Mỗi gói tin âm thanh gửi lên server mang theo một byte định danh tuyến `route_id`. Máy chủ FastAPI đóng vai trò bộ định tuyến (dispatcher) bất đồng bộ, phân phối chính xác gói tin tới đúng luồng xử lý và trả kết quả về client. Hệ thống hỗ trợ hai chế độ vận hành: **Chế độ 1 chiều** dịch video/bài giảng và **Chế độ 2 chiều song hướng** phục vụ hội họp trực tuyến. Cơ chế Preload và Warmup được thiết lập tại server để làm nóng sẵn các mô hình lúc khởi động, loại bỏ hoàn toàn độ trễ khởi động lạnh (cold-start) ở câu thoại đầu tiên."

---

## 💻 SLIDE 14: THIẾT KẾ TỐI ƯU ĐỘ TRỄ: VAD, SHORT-MT & WATCHDOG
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ luồng xử lý streaming: Khối PCM 200ms -> Silero VAD -> Ngưỡng im lặng 450ms + Hangover 400ms -> STT -> Short-MT -> Watchdog (3s) -> NMT -> TTS.
    *   Nhấn mạnh các tham số thời gian được tối ưu bằng chữ nổi bật.
*   **Kịch bản nói (Speech Script):**
    *   "Để tối ưu hóa độ trễ tích lũy qua 3 tầng AI mà vẫn đảm bảo độ chính xác dịch thuật, đồ án đã thiết kế các cơ chế điều phối luồng dữ liệu thông minh:
    *   **Cắt câu động bằng Silero VAD:** Luồng âm thanh được gửi liên tục mỗi 200 ms. VAD sẽ cắt câu động khi phát hiện khoảng im lặng liên tục đạt **450 ms**, kết hợp đệm thêm một khoảng **Hangover Frame ~400 ms** để tránh mất các phụ âm cuối năng lượng thấp.
    *   **Đệm dịch ngắn (Short-MT):** Gom các cụm từ ngắn từ STT lại để NLLB-200 dịch đủ ngữ cảnh và tự nhiên.
    *   **Giám sát Watchdog (Force Flush):** Nếu người nói ngắt quãng quá lâu, bộ watchdog sẽ cưỡng bức đẩy bản dịch đi sau **3 giây** im lặng dù chưa đạt độ dài tối thiểu, giúp cân bằng hoàn hảo giữa chất lượng dịch thuật và độ trễ."

---

## 💻 SLIDE 15: GIẢI PHÁP CÔ LẬP ÂM THANH CHỐNG PHẢN HỒI ÂM HỌC
*   **Thời lượng dự kiến:** 45 giây
*   **Bố cục & Ghi chú thiết kế:**
    *   Sơ đồ định tuyến âm thanh ảo qua phần mềm VoiceMeeter Banana.
    *   Chỉ rõ sự cô lập giữa luồng phát đi (Route 0 - bus B1 ảo) và luồng thu về (Route 1 - Aux Input ảo) để chứng minh không có đường truyền chéo gây vòng lặp tự dịch.
*   **Kịch bản nói (Speech Script):**
    *   "Một bài toán cực kỳ nan giải khi tích hợp S2ST vào họp trực tuyến (Meet, Zoom) là **vòng lặp phản hồi âm học tự dịch**. Khi loa máy tính phát ra âm thanh đã dịch, micro sẽ vô tình thu lại âm thanh đó và gửi lên server để dịch ngược lại, tạo ra vòng lặp vô hạn.
    *   Đồ án đã giải quyết triệt để vấn đề này ở mức phần mềm bằng cách tích hợp **VoiceMeeter Banana** - bộ trộn âm ảo đa cổng. Chúng em viết code Python điều khiển qua thư viện DLL để tự động định tuyến: Luồng dịch của người dùng được đẩy vào cổng micro ảo (bus B1) của Zoom/Meet. Trong khi đó, luồng âm thanh cuộc họp của đối tác được định tuyến qua cổng Aux Input ảo độc lập để ứng dụng thu và dịch sang tiếng Việt. Sự cô lập các kênh ảo này đảm bảo âm thanh dịch phát ra không bao giờ bị thu ngược trở lại micro. Chúng em cũng khuyến nghị người dùng đeo tai nghe vật lý để triệt tiêu hoàn toàn hiện tượng vọng âm phần cứng."

---

## 💻 SLIDE 16: GIAO DIỆN CLIENT PYSIDE6 & KẾT QUẢ KIỂM THỬ CHỨC NĂNG
*   **Thời lượng dự kiến:** 30 giây (Nói nhanh, tập trung tính ổn định)
*   **Bố cục & Ghi chú thiết kế:**
    *   Đặt hai ảnh giao diện chính và giao diện cấu hình của Client cạnh nhau.
    *   Ghi ngắn gọn bảng kết quả kiểm thử chức năng đạt 100%.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\client_giao_dien_chinh.png | Giao diện chính Client]]`
    *   `[[HÌNH: D:\VKU\GraProject\For_report\assets\client_settings_dialog.png | Hộp thoại cấu hình]]`
*   **Kịch bản nói (Speech Script):**
    *   "Phía máy khách được xây dựng bằng **PySide6** với giao diện trực quan. Màn hình chính chia làm hai khung transcript độc lập hiển thị văn bản dịch tiếng Anh và tiếng Việt theo thời gian thực dưới dạng kết quả tạm thời (interim) và kết quả cuối cùng (final). 
    *   Hộp thoại cài đặt cho phép người dùng cấu hình linh hoạt thiết bị âm thanh đầu vào, đầu ra, lựa chọn giọng đọc và kích hoạt VoiceMeeter. 
    *   Hệ thống đã trải qua các kịch bản kiểm thử chức năng nghiêm ngặt (từ dịch một tuyến, nhận dạng streaming, tự động kết nối lại khi mất mạng đến flush sạch câu cuối) và đều đạt tỷ lệ thành công 100%, chứng minh tính ổn định cao của phần mềm trong vận hành thực tế."

---

## 💻 SLIDE 17: KẾT QUẢ VẬN HÀNH THỰC TẾ & PHÂN RÃ ĐỘ TRỄ TÍCH LŨY
*   **Thời lượng dự kiến:** 45 giây (Nhấn mạnh tính khả thi thời gian thực)
*   **Bố cục & Ghi chú thiết kế:**
    *   Biểu đồ phân rã độ trễ của một câu thoại ngắn (~5-10 từ) dưới dạng biểu đồ thanh chồng hoặc sơ đồ timeline.
    *   Chỉ rõ tổng độ trễ dao động từ 1 đến 2 giây.
*   **Hình ảnh/Bảng biểu (Placeholder):**
    *   Bảng phân rã độ trễ tích lũy (Trích từ bảng 4.6.4 trong báo cáo).
*   **Kịch bản nói (Speech Script):**
    *   "Về hiệu năng vận hành thực tế, hệ thống phản hồi cực kỳ mượt mà. Kết quả nhận dạng tạm thời (interim) hiển thị gần như tức thời chỉ sau **0.3 đến 0.5 giây** khi người dùng bắt đầu nói. 
    *   Đối với một câu thoại ngắn trung bình từ 5 đến 10 từ, **tổng độ trễ tích lũy từ lúc dứt câu đến khi nghe được âm thanh dịch hoàn chỉnh dao động từ 1 đến 2 giây**. 
    *   Phân rã định lượng chỉ ra: Khoảng thời gian chờ dứt câu của VAD chiếm tỷ trọng lớn nhất với **~0.85 giây** (đây là hằng số vật lý bắt buộc để bảo toàn ngữ cảnh); thời gian nhận dạng STT mất ~0.3 giây; dịch máy NMT mất ~0.15 giây; và tổng hợp TTS cùng truyền phát chỉ mất ~0.2 giây nhờ RTF cực thấp của mô hình Run B1. Độ trễ này hoàn toàn nằm trong ngưỡng tối ưu cho hội thoại trực tuyến thời gian thực."

---

## 💻 SLIDE 18: KẾT LUẬN & HƯỚNG PHÁT TRIỂN TƯƠNG LAI
*   **Thời lượng dự kiến:** 30 giây (Kết luận tự tin, mở rộng khoa học)
*   **Bố cục & Ghi chú thiết kế:**
    *   Thiết kế đối chiếu: Một bên là **Đóng góp/Ưu điểm**, một bên là **Hạn chế & Hướng đi tương lai**.
    *   Kết thúc bằng lời cảm ơn trang trọng.
*   **Kịch bản nói (Speech Script):**
    *   "Tóm lại, đồ án đã hoàn thành xuất sắc các mục tiêu đề ra: xây dựng thành công pipeline S2ST song hướng thời gian thực tối ưu độ trễ, đóng góp mô hình TTS giọng nam Việt Run B1 chất lượng cao cho cộng đồng và đề xuất quy trình xây dựng dữ liệu giọng nói khoa học. 
    *   Mặc dù vẫn còn một số hạn chế như phụ thuộc vào GPU server đám mây và dữ liệu đơn nguồn, đồ án đã xác định các hướng đi rõ ràng cho tương lai: nghiên cứu mô hình Run B2 high-resolution để tăng độ nét sóng âm, phát triển cơ chế dịch cuốn chiếu incremental để giảm trễ câu dài, và lượng tử hóa sâu để đưa hệ thống chạy offline hoàn toàn trên thiết bị client.
    *   Em xin chân thành cảm ơn quý thầy cô trong Hội đồng đã lắng nghe. Em rất mong nhận được những ý kiến đóng góp và câu hỏi từ quý thầy cô để đồ án được hoàn thiện hơn. Em xin trân trọng cảm ơn!"
