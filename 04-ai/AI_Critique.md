# AI Critique: Giới hạn của Mô hình AI trong Kiểm thử Thiết bị Phần cứng Vật lý
*(Academic Critique on the Limitations of Large Language Models in Physical Hardware QA)*

**Sinh viên thực hiện:** Trần Vũ Quang (MSSV: 23120346)  
**Đối tượng khảo sát:** Bếp hồng ngoại Sunhouse SHD6012A (Single Infrared Cooker)  

Quá trình áp dụng các mô hình ngôn ngữ lớn (LLMs như GPT-4o, Gemini) vào việc thiết kế kịch bản kiểm thử cho thiết bị phần cứng gia dụng bộc lộ những giới hạn căn bản bắt nguồn từ sự phân tách giữa không gian biểu diễn ký hiệu số (symbolic representation) và thực tại vật lý liên tục (continuous analog reality).

Trước hết, các mô hình AI hiện đại được huấn luyện chủ yếu trên dữ liệu phần mềm, văn bản và mã nguồn web, dẫn đến thiên kiến nhận thức số hóa sâu sắc. Khi được yêu cầu kiểm thử bếp hồng ngoại, AI chỉ trừu tượng hóa thiết bị thành một cỗ máy trạng thái hữu hạn với các nút bấm rời rạc (Bật, Tắt, Tăng, Giảm công suất, Hẹn giờ). AI hoàn toàn bất lực trong việc mô hình hóa các quy luật cơ học và nhiệt động lực học phi tuyến tính diễn ra đồng thời. Cụ thể, AI không thể dự đoán được hiện tượng võng khung nhựa chịu lực khi đặt bình nước 20kg lên bề mặt kính đang ở nhiệt độ 600°C, cũng như không thể nhận diện được điểm mù của cảm biến nhiệt độ NTC khi người dùng sử dụng đáy chảo cong vênh làm nhiệt lượng tích tụ cục bộ gây rạn nứt mặt kính ceramic.

Thứ hai, AI thiếu hoàn toàn nhận thức về quán tính vật lý (physical inertia) và yếu tố an toàn trễ. Trong khi phần mềm có thể ngắt kết nối tức thì, mâm nhiệt sợi carbon vẫn duy trì mức nhiệt nguy hiểm hàng trăm độ C sau khi ngắt điện. AI không thể lường trước kịch bản người dùng rút phích cắm đột ngột, làm vô hiệu hóa chu kỳ quạt tản nhiệt trễ và xóa sạch ký hiệu cảnh báo nhiệt dư "H" trên màn hình LED. 

Tóm lại, dù AI có thể hỗ trợ phác thảo nhanh khung kịch bản chức năng ban đầu, việc kiểm thử phần cứng và hệ thống nhúng đòi hỏi kiến thức chuyên sâu về cơ điện tử, sự nhạy bén thực nghiệm và lương tâm nghề nghiệp của người kỹ sư QA thực tế mà không một thuật toán tạo sinh nào hiện nay có thể thay thế được. *(330 từ)*
