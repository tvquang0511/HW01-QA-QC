# Appendix A: Full AI Prompt Log (PROMPT_LOG.md)

**Exercise ID:** HW01-AI  
**Course:** Software Testing (FIT - VNUHCM University of Science)  
**Student Name:** Trần Vũ Quang  
**Student ID:** 23120346  
**Target Hardware:** Bếp hồng ngoại Sunhouse SHD6012A (2024)  
**Date Range:** 02/10/2026 – 04/10/2026  

---

## Log Entry 1: Thiết kế Mindmap vai trò QA/QC và Quy trình Kiểm thử ISTQB (Requirement 1 - CLO G9.1)
- **Thời gian (Timestamp):** 14:20 02/10/2026
- **Công cụ (Tool):** Google Gemini 2.5 Flash
- **Tham số mô hình:** Default settings (Temperature 0.7, Web Search enabled)
- **Câu lệnh (Prompt):**
  ```text
  Hãy đóng vai trò một Chuyên gia Kiểm thử Cấp cao (Senior QA Architect), hãy thiết kế một sơ đồ tư duy (mindmap) bằng định dạng Mermaid thể hiện toàn diện bức tranh ngành QA/QC, phân định rạch ròi vai trò QA vs QC, các cấp độ kiểm thử (test levels), các loại kiểm thử (test types), và quy trình kiểm thử phần mềm từ đầu đến cuối theo chuẩn giáo trình ISTQB Foundation Level mới nhất.
  ```
- **Kết quả AI trả về:** Sơ đồ Mermaid gồm 4 nhánh chính: Quality Assurance vs Quality Control, Test Levels, Test Types, và Test Process.
- **Phân tích & Kiểm toán của sinh viên (Student Audit):**
  - Phát hiện 3 sai phạm nghiêm trọng đối chiếu với chuẩn ISTQB CTFL v4.0:
    1. Đảo ngược định nghĩa QA và QC (xếp QA là đi tìm bug, QC là xây dựng quy trình).
    2. Bỏ quên hoàn toàn Kiểm thử tĩnh (Static Testing - Reviews, Static Analysis).
    3. Đặt bước Giám sát và Điều khiển (Test Monitoring & Control) vào bước tuần tự số 4 sau Test Execution thay vì là hoạt động quản trị song hành liên tục.
  - Sinh viên đã tự mình thiết kế lại toàn bộ Mindmap chuẩn xác và viết bản giải trình chi tiết trong file `01-job-market/MINDMAP.md`.

---

## Log Entry 2: Khảo sát & Phân tích 20 Sự cố Phần mềm Giai đoạn 2022–2026 (Requirement 2)
- **Thời gian (Timestamp):** 20:15 03/10/2026
- **Công cụ (Tool):** ChatGPT (GPT-4o) & Tìm kiếm thông tin
- **Câu lệnh (Prompt):**
  ```text
  Hãy cung cấp danh sách phân tích kỹ thuật của 20 sự cố phần mềm nghiêm trọng gây chấn động toàn cầu trong giai đoạn từ năm 2022 đến 2026, trong đó bắt buộc phải có ít nhất 5 sự cố liên quan trực tiếp đến Trí tuệ Nhân tạo / LLM (như ảo giác, jailbreak, prompt injection, thiên kiến thuật toán). Với mỗi sự cố, hãy nêu rõ: Thời gian, Tổ chức, Nguyên nhân gốc rễ, Mức độ nghiêm trọng, Hậu quả thiệt hại và Giải pháp khắc phục.
  ```
- **Kết quả AI trả về:** Danh sách 20 sự cố với thông tin mô tả tổng quan.
- **Phân tích & Kiểm toán của sinh viên (Student Audit):**
  - AI bộc lộ nhiều điểm ảo giác (Hallucination) và bịa đặt chi tiết kỹ thuật: ví dụ gán sự cố sập màn hình xanh toàn cầu của CrowdStrike Falcon (19/07/2024) cho lỗi "con trỏ C++ trỏ vào vùng nhớ null trong kernel", trong khi tài liệu Post-mortem chính thức từ CrowdStrike chỉ rõ lỗi là "Out-of-bounds array read" khi trình phân tích Channel File 291 đọc 21 tham số đầu vào trong khi chỉ có 20 trường hợp lệ.
  - Sinh viên đã trực tiếp tra cứu tài liệu gốc, mã lỗi CVE, và viết riêng 20 phân tích ảo giác/thiên kiến độc lập cho từng sự cố trong `02-software-defects/software_defects.md`.

---

## Log Entry 3: Khởi tạo kịch bản kiểm thử ban đầu cho Bếp hồng ngoại Sunhouse (Requirement 3)
- **Thời gian (Timestamp):** 16:45 04/10/2026
- **Công cụ (Tool):** ChatGPT (GPT-4o)
- **Câu lệnh (Prompt):**
  ```text
  Tôi có một chiếc bếp hồng ngoại đơn Sunhouse SHD6012A công suất 2000W với các phím bấm điện tử: Bật/Tắt, Menu/Chế độ, Tăng (+), Giảm (-), Hẹn giờ, Khóa an toàn, và màn hình LED hiển thị. Hãy thiết kế bộ 15 test cases toàn diện cho thiết bị vật lý này theo định dạng QA chuẩn (ID, Objective, Input, Steps, Expected Result, Actual Result, Verdict). Hãy bổ sung các edge cases phức tạp nhất.
  ```
- **Kết quả AI trả về:** 15 test cases chỉ xoay quanh các tương tác bấm nút giao diện đơn giản (nhấn nút tăng, giảm, chuyển chế độ lẩu, bấm khóa, bấm còi bíp...).
- **Phân tích & Kiểm toán của sinh viên (Student Audit):**
  - AI hoàn toàn không có nhận thức về các điều kiện vật lý thực tế: cơ học tải trọng, trường nhiệt độ phi tuyến và quán tính nhiệt.
  - Sinh viên chụp lại bằng chứng đối thoại chứng minh AI sinh thiếu edge cases vật lý (`03-physical-product/assets/MC1.png` và `MC2.png`).
  - Sinh viên tự xây dựng 3 edge cases vật lý chuyên sâu: Tải trọng bình nước 20L (TC-13), Sốc nhiệt đáy nồi cong vênh gây mù cảm biến NTC (TC-14), và Rút phích cắm đột ngột khi quạt làm mát đang chạy xả nhiệt dư (TC-15).

---

## Log Entry 4: Hướng dẫn lựa chọn kịch bản quay video thực tế tối ưu
- **Thời gian (Timestamp):** 21:10 04/10/2026
- **Công cụ (Tool):** Claude 3.5 Sonnet / Antigravity Assistant
- **Câu lệnh (Prompt):**
  ```text
  Trong số 15 test case của bếp hồng ngoại Sunhouse SHD6012A, hãy tư vấn cho tôi 5 test case tiêu biểu, trực quan nhất và an toàn nhất để thực hiện quay video thực tế có thuyết minh dưới 60 giây.
  ```
- **Kết quả & Thực thi thực tế:**
  - Lựa chọn 5 kịch bản: TC-01 (Cắm nguồn & Standby), TC-02 (Bật chế độ Lẩu 2000W & mâm phát sáng), TC-03 (Tăng giảm nấc công suất), TC-06 (Khóa an toàn trẻ em vô hiệu hóa nút bấm), TC-08 (Tắt bếp và quạt tản nhiệt quay trễ xả nhiệt dư).
  - Sinh viên tự mình thực hiện và quay 5 video trực tiếp trên bếp thật, có giọng thuyết minh thật của sinh viên Trần Vũ Quang (MSSV: 23120346), upload lên YouTube Unlisted.
