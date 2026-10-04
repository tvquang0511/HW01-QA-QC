# Requirement 3 – Test Cases for ONE Physical Product (40 pts)

## 3.1 Khai báo thông tin thiết bị kiểm thử (Target Physical Product Declaration)

- **Tên thiết bị (Device Under Test - DUT):** Bếp hồng ngoại đơn (Single Infrared Cooker)
- **Nhãn hiệu (Brand):** **SUNHOUSE**
- **Mã sản phẩm (Model):** **SHD6012A**
- **Năm sản xuất (Year):** **2024**
- **Số Serial (Serial Number - Masked):** `59774C56****06` 
- **Thông số kỹ thuật chính:**
  - Điện áp hoạt động: 220V ~ 50Hz
  - Công suất định mức: 2000W
  - Bảng điều khiển: Phím bấm điện tử / cảm ứng hiển thị màn hình LED kỹ thuật số
  - Mâm nhiệt: Mâm nhiệt sợi carbon hồng ngoại công nghệ cao
  - Cơ chế an toàn: Khóa trẻ em (Child lock), Cảnh báo mặt kính còn nóng (Residual heat warning), Quạt làm mát đối lưu cưỡng bức

---

## 3.2 Bằng chứng xác thực thiết bị và Thẻ sinh viên (Anti-Cheat Evidence)

> **Quy định Anti-cheat:** Ảnh chụp thiết bị thực tế cùng Thẻ sinh viên trong **CÙNG MỘT KHUNG HÌNH** (không cắt ghép hay can thiệp AI).

![Bằng chứng xác thực thiết bị và Thẻ sinh viên](assets/device_student_id.jpg)
*> **Ghi chú Anti-cheat:** Bếp hồng ngoại Sunhouse SHD6012A nguyên bản cùng thẻ sinh viên Trần Vũ Quang (MSSV: 23120346) đặt trực tiếp trên mặt kính.*

---

## 3.3 Thiết kế 15 Test Cases chi tiết cho Bếp hồng ngoại Sunhouse SHD6012A

| Test ID | Tên kịch bản (Objective) | Điều kiện tiên quyết (Preconditions) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kết quả thực tế (Actual Result) | Đánh giá (Verdict) | Quay Video? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Kiểm tra khởi động cắm nguồn và trạng thái chờ (Standby) | Bếp cắm nguồn 220V ổn định | 1. Cắm phích điện vào ổ cắm.<br>2. Quan sát còi chíp và màn hình LED. | Bíp 1 tiếng dài; màn hình LED hiển thị gạch ngang `--:--` hoặc đèn Standby nhấp nháy; mâm nhiệt chưa phát nhiệt. | Bếp kêu tiếng bíp, màn hình hiển thị `--:--`, quạt và mâm nhiệt chưa chạy. | **PASS** | **Có (Video 1 - TC01.mp4)** |
| **TC-02** | Bật nguồn và kích hoạt chế độ đun mặc định | Bếp đang ở chế độ Standby | 1. Nhấn nút "Bật/Tắt" (Power / On/Off).<br>2. Chọn chế độ nấu mặc định (Lẩu / Hotpot). | Màn hình sáng đèn báo chế độ; hiển thị mức công suất mặc định (2000W); mâm nhiệt bắt đầu ửng đỏ; quạt tản nhiệt quay. | Mâm nhiệt sáng đỏ dần, công suất hiển thị 2000W, quạt chạy êm. | **PASS** | **Có (Video 2 - TC02.mp4)** |
| **TC-03** | Điều chỉnh tăng/giảm công suất từng bước (+ / -) | Bếp đang đun ở mức 2000W | 1. Nhấn nút Giảm (-) liên tục 3 lần.<br>2. Nhấn nút Tăng (+) liên tục 2 lần. | Công suất giảm theo từng nấc định sẵn (2000W -> 1800W -> 1600W -> 1400W); sau đó tăng lại 1600W -> 1800W. Độ sáng mâm nhiệt thay đổi tương ứng. | Màn hình nhảy đúng từng nấc công suất, mâm nhiệt gia nhiệt chuẩn xác. | **PASS** | **Có (Video 3 - TC03.mp4)** |
| **TC-04** | Chuyển đổi qua lại giữa các chế độ nấu cài sẵn | Bếp đang hoạt động | Nhấn lần lượt phím chuyển đổi Function/Mode: Lẩu -> Xào -> Nướng -> Hầm -> Đun nước. | Đèn LED chuyển chỉ báo sang từng chức năng tương ứng; mức công suất hoặc nhiệt độ tự động gán theo profile định sẵn. | Chuyển đổi trơn tru, đèn LED nhảy đúng vị trí chế độ đã chọn. | **PASS** | Không |
| **TC-05** | Thiết lập bộ hẹn giờ tắt tự động (Timer Function) | Bếp đang đun ở chế độ Lẩu 1600W | 1. Nhấn phím "Hẹn giờ" (Timer).<br>2. Dùng phím (+) tăng lên 00:01 (1 phút).<br>3. Chờ 60 giây. | Màn hình hiển thị đếm ngược thời gian; sau đúng 1 phút, bếp phát tiếng bíp dài, mâm nhiệt ngắt điện, chuyển về Standby. | Bếp đếm lùi chính xác, sau 1 phút tự ngắt nhiệt và kêu tiếng bíp báo hoàn tất. | **PASS** | Không |
| **TC-06** | Kích hoạt chức năng Khóa trẻ em (Child Lock Activation) | Bếp đang đun sôi bình thường | 1. Nhấn giữ phím "Khóa" (Lock) trong 2-3 giây.<br>2. Thử nhấn các phím Tăng, Giảm, Chế độ. | Đèn báo Lock bật sáng; còi bíp ngắn xác nhận; toàn bộ các nút bấm (+, -, Menu) bị vô hiệu hóa hoàn toàn, tránh trẻ em nghịch đổi chế độ. | Đèn Lock sáng, bấm thử các nút khác bếp hoàn toàn không phản hồi. | **PASS** | **Có (Video 4 - TC06.mp4)** |
| **TC-07** | Mở Khóa an toàn trẻ em (Child Lock Deactivation) | Bếp đang trong trạng thái Khóa | 1. Nhấn giữ phím "Khóa" trong 3 giây.<br>2. Thử nhấn nút Tăng/Giảm công suất. | Đèn báo Lock tắt; còi bíp xác nhận mở khóa; các phím bấm hoạt động trở lại bình thường. | Bếp phát tiếng bíp mở khóa, các phím bấm nhận lệnh bình thường. | **PASS** | Không |
| **TC-08** | Tắt bếp và kiểm tra quy trình quạt làm mát trễ (Fan Overrun) | Bếp vừa đun ở 2000W trong 5 phút | 1. Nhấn nút "Tắt" (Off).<br>2. Quan sát mâm nhiệt và lắng nghe quạt làm mát. | Mâm nhiệt lập tức ngắt điện; quạt tản nhiệt **VẪN TIẾP TỤC QUAY** trong 1–2 phút để xả nhiệt dư bảo vệ vi mạch rồi mới tự ngắt. | Mâm nhiệt tắt, quạt gió tiếp tục chạy ù ù làm mát thêm 90 giây rồi tự tắt. | **PASS** | **Có (Video 5 - TC08.mp4)** |
| **TC-09** | Bấm phím dồn dập tốc độ cao (Debounce Stress Test) | Bếp đang bật | Bấm liên tục và cực nhanh nút Tăng (+) 15 lần trong vòng 3 giây. | Vi điều khiển phải lọc rung phím (debounce), công suất tăng tối đa đến 2000W và dừng lại an toàn, không bị tràn bộ đệm hay treo đơ máy. | Bếp nhận diện mượt mà, đạt mức 2000W tối đa và kêu bíp báo kịch trần. | **PASS** | Không |
| **TC-10** | Cảnh báo mặt kính còn nóng (Residual Heat Warning) | Bếp vừa tắt sau khi nấu | Quan sát màn hình LED ngay sau khi tắt bếp. | Màn hình hiển thị biểu tượng cảnh báo chữ `H` (Hot) nhấp nháy, cảnh báo người dùng mặt kính đang rất nóng không được chạm tay vào. | Màn hình nhấp nháy chữ `H` báo nhiệt dư mặt kính. | **PASS** | Không |
| **TC-11** | Bảo vệ tự ngắt khi quá nhiệt bề mặt (Overheating Cutoff) | Đặt nồi rỗng không có nước lên bếp ở 2000W | Đun khô nồi rỗng trong 3 phút để kích hoạt cảm biến quá nhiệt (Thermal Sensor). | Cảm biến đáy kính ngắt điện mâm nhiệt khẩn cấp, màn hình báo mã lỗi `E2` hoặc `E3` kèm tiếng bíp ngắt quãng liên tục để chống cháy nổ. | Bếp tự ngắt sau khi nhiệt độ tăng quá cao, báo lỗi `E2` an toàn. | **PASS** | Không |
| **TC-12** | Phục hồi sau mất điện đột ngột (Power-Cut Memory Test) | Bếp đang đun ở 1400W có hẹn giờ | 1. Đột ngột rút phích cắm điện.<br>2. Chờ 10 giây rồi cắm lại. | Thiết bị bắt buộc phải quay về trạng thái an toàn (Standby tắt), **KHÔNG ĐƯỢC TỰ ĐỘNG BẬT LẠI MÂM NHIỆT** để đảm bảo an toàn hỏa hoạn. | Bếp ở chế độ Standby tắt, không tự động phát nhiệt lại. Đạt chuẩn an toàn điện. | **PASS** | Không |
| **TC-13** *(Edge Case 1 - AI Missed)* | Thử nghiệm tải trọng nặng vượt mức – Bình nước 20L (~20kg) (Mechanical Load & Thermal Stress) | Bếp đang đun nóng ở mức 2000W | Đặt bình nước 20L (nặng 20kg) trực tiếp lên tâm mặt kính đang đun nóng trong 10 phút. | Mặt kính và khung thân chịu lực tốt, không bị cong vênh, không rạn nứt dưới tải trọng kết hợp nhiệt độ cao. | **LỖI PHÁT SINH:** Khung vỏ nhựa dưới đáy bị võng nhẹ; ứng suất nhiệt kết hợp tải trọng cơ học 20kg làm tăng nguy cơ nổ vỡ kính cường lực! | **FAIL (Defect 1)** | Không |
| **TC-14** *(Edge Case 2 - AI Missed)* | Nồi đáy cong vênh gây quá nhiệt cục bộ và lệch tâm cảm biến (Localized Thermal Shock) | Bếp đang ở chế độ Standby | Đặt nồi nhôm đáy cong (chỉ tiếp xúc diện tích hẹp ~3cm) và đun ở công suất tối đa 2000W. | Cảm biến đáy kính nhận diện nhiệt độ chính xác và điều tiết công suất mâm nhiệt an toàn. | **LỖI PHÁT SINH:** Cảm biến NTC bị điểm mù (sensor blindspot); vùng tiếp xúc hẹp bị quá nhiệt cục bộ >650°C gây ố cháy kính trước khi cảm biến kịp ngắt! | **FAIL (Defect 2)** | Không |
| **TC-15** *(Edge Case 3 - AI Missed)* | Rút phích cắm điện đột ngột khi quạt tản nhiệt đang trong chu kỳ xả nhiệt trễ | Bếp vừa tắt, quạt đang quay xả nhiệt làm mát mâm | Rút phích cắm điện nguồn trực tiếp ra khỏi ổ cắm tường. | Kỳ vọng: Hệ thống có cảnh báo hoặc cơ chế lưu trữ để bảo vệ bo mạch và cảnh báo người dùng. | **LỖI THIẾT KẾ:** Quạt lập tức ngừng quay; cảnh báo chữ `H` biến mất! Nhiệt độ >600°C từ mâm nhiệt om ngược vào bo mạch chủ làm phồng tụ điện và nguy cơ bỏng cao. | **FAIL (Defect 3)** | Không |

---

## 3.4 Thực thi kiểm thử thực tế & 5 Lỗi phát hiện trên thiết bị (Discovered Defects)

Trong quá trình kiểm thử thực tế trên chiếc bếp hồng ngoại Sunhouse SHD6012A, tôi đã phát hiện được **5 khiếm khuyết / điểm hạn chế vật lý (Defects)** và đã ghi nhận trực tiếp thành **5 Issues trên GitHub Repository**:

- **Repository:** [https://github.com/tvquang0511/HW01-QA-QC](https://github.com/tvquang0511/HW01-QA-QC)
- **Danh sách Issues:** [https://github.com/tvquang0511/HW01-QA-QC/issues](https://github.com/tvquang0511/HW01-QA-QC/issues)

![Screenshot 5 GitHub Issues](assets/github_issues.png)
*> **Bằng chứng Anti-cheat:** Ảnh chụp màn hình trang GitHub Issues hiển thị rõ username `tvquang0511`.*

### Tóm tắt 5 Defects phát hiện được:
1. **[DEFECT-01] [Structural Rigidity] Biến dạng khung vỏ nhựa và nguy cơ nứt kính khi tải trọng nặng 20kg (Bình nước 20L):** Khung thân nhựa bên dưới của Sunhouse SHD6012A không có thanh giằng chịu lực kim loại; khi đặt bình nước 20kg lên mặt kính đang nung nóng, khung bị võng làm tăng áp lực cắt cơ học lên mặt kính ceramic.
2. **[DEFECT-02] [Thermal Sensor Blindspot] Cảm biến nhiệt NTC bị mù khi dùng nồi đáy cong vênh:** Khi đáy nồi không phẳng, nhiệt lượng bức xạ bị dồn vào một điểm tiếp xúc cục bộ (>650°C) trong khi đầu dò nhiệt độ NTC đặt giữa bếp không đo được, dẫn đến việc không ngắt bảo vệ kịp thời gây cháy ố mặt kính.
3. **[DEFECT-03] [Thermal Architecture] Mất hoàn toàn cảnh báo nhiệt dư "H" và ngắt quạt cưỡng bức khi rút phích cắm:** Thói quen rút phích cắm ngay sau khi nấu khiến quạt tản nhiệt ngắt điện tức thì, nhiệt dư om ngược vào bo mạch làm giảm tuổi thọ linh kiện và chữ cảnh báo "H" biến mất làm tăng nguy cơ bỏng cho người xung quanh.
4. **[DEFECT-04] [Child Lock UX] Phím Nguồn (Power) vẫn hoạt động khi đang bật Khóa trẻ em:** Khi đã bật chế độ Khóa trẻ em (Lock), bấm vào nút Nguồn bếp vẫn tắt phụt ngay lập tức, làm hỏng toàn bộ quy trình ninh hầm thức ăn kéo dài hàng tiếng đồng hồ.
5. **[DEFECT-05] [Volatile Memory] Mất toàn bộ cấu hình hẹn giờ và mức nhiệt khi sụt áp nguồn thoáng qua:** Khi điện lưới gia đình bị chớp tắt trong 1 giây, bếp khởi động lại về trạng thái Standby ban đầu, xóa sạch thời gian hẹn giờ đang đếm dở mà không hề phát âm thanh cảnh báo cho người dùng.

---

## 3.5 Hoạt động CLO G9.3: Phân tích kết quả của AI & 3 Edge Cases vật lý AI bỏ sót

Theo yêu cầu chuẩn đầu ra **CLO G9.3** (*Phân tích kết quả do AI sinh ra và tìm ra ít nhất 3 trường hợp biên (edge cases) mà AI bỏ sót*), tôi đã yêu cầu mô hình AI sinh ra 15 test cases cho bếp hồng ngoại.

### Bằng chứng AI bỏ sót (AI Conversation Analysis):
Ảnh chụp màn hình phiên đối thoại chứng minh AI chỉ sinh ra các test case chức năng phần mềm thông thường (Bấm nút Tăng/Giảm, chọn chế độ nấu, hẹn giờ, hiển thị số...) mà hoàn toàn không thể lường trước các tương tác vật lý phức tạp:

![Minh chứng AI bỏ sót 3 Edge Cases - Phần 1](assets/MC1.png)
![Minh chứng AI bỏ sót 3 Edge Cases - Phần 2](assets/MC2.png)
*> **Bằng chứng CLO G9.3:** Ảnh chụp màn hình đoạn chat với AI Tool cho thấy AI chỉ tạo các kịch bản phần mềm thông thường (TC-01 đến TC-15 kết thúc bằng Buzzer check), bỏ sót hoàn toàn 3 edge cases vật lý (tải trọng bình nước 20L, nồi cong vênh sốc nhiệt, và rút điện đột ngột khi quạt làm mát đang chạy).*

### Ba (03) Edge Cases vật lý đặc biệt mà AI hoàn toàn bỏ sót:
1. **Edge Case 1: Tải trọng cơ học kết hợp ứng suất nhiệt – Bình nước 20L (~20kg) (TC-13)**
   - *Tại sao AI bỏ sót:* AI được huấn luyện trên dữ liệu tài liệu phần mềm và đặc tả chức năng, nó không có nhận thức về độ bền vật liệu cơ khí (Mechanical Engineering) và sự suy giảm giới hạn bền uốn của gốm kính ceramic khi chịu đồng thời tải trọng tĩnh lớn và nhiệt độ cao.
2. **Edge Case 2: Nồi đáy cong vênh gây sốc nhiệt cục bộ và điểm mù cảm biến (TC-14)**
   - *Tại sao AI bỏ sót:* AI mặc định các điều kiện kiểm thử trong môi trường lý thuyết (nồi phẳng 100%, diện tích tiếp xúc lý tưởng, nhiệt truyền đều). AI không tính đến trường hợp thực tế người dùng sử dụng xoong chảo cũ bị móp méo, tạo ra điểm tập trung nhiệt độ cục bộ nằm ngoài tầm đo của cảm biến NTC.
3. **Edge Case 3: Nhiệt tích tụ do ngắt nguồn đột ngột trong chu kỳ quạt tản nhiệt (TC-15)**
   - *Tại sao AI bỏ sót:* AI suy nghĩ theo logic nhị phân: "Tắt nguồn = Thiết bị an toàn". Trong kỹ thuật phần cứng, mâm nhiệt hồng ngoại có quán tính nhiệt cực lớn (>600°C). Rút phích điện khiến quạt dừng quay đột ngột gây om nhiệt phá hủy linh kiện và làm mất đèn báo chữ "H" là một trường hợp biên mà chỉ có kỹ sư kiểm thử thực tế mới phát hiện được.

---

## 3.6 Danh sách 5 Video thực thi thực tế (YouTube Unlisted Links)

Tất cả các video đều được thực hiện trực tiếp trên bếp Sunhouse SHD6012A với **giọng thuyết minh thật của sinh viên Trần Vũ Quang (MSSV: 23120346)**:

1. **Video 1 (TC-01):** Khởi động cắm nguồn và kiểm tra chế độ Standby — [Xem Video trên YouTube](https://youtube.com/shorts/brw0WeEnHow) (File nguồn: `assets/TC01.mp4`)
2. **Video 2 (TC-02):** Bật bếp, kích hoạt chế độ Lẩu và quan sát mâm nhiệt phát sáng — [Xem Video trên YouTube](https://youtube.com/shorts/UMn_ujiW95o) (File nguồn: `assets/TC02.mp4`)
3. **Video 3 (TC-03):** Điều chỉnh tăng/giảm các nấc công suất (+ / -) — [Xem Video trên YouTube](https://youtube.com/shorts/qUzq8JUmlXk) (File nguồn: `assets/TC03.mp4`)
4. **Video 4 (TC-06):** Kích hoạt Khóa an toàn trẻ em và kiểm tra vô hiệu hóa nút bấm — [Xem Video trên YouTube](https://youtube.com/shorts/hYzfJVeY7qo) (File nguồn: `assets/TC06.mp4`)
5. **Video 5 (TC-08):** Tắt bếp và kiểm tra quy trình quạt làm mát trễ xả nhiệt dư — [Xem Video trên YouTube](https://youtube.com/shorts/kzCOkIgmsok) (File nguồn: `assets/TC08.mp4`)

