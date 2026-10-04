# Hướng dẫn tạo 5 Issues trên GitHub (Bếp hồng ngoại Sunhouse SHD6012A)

**Target Repository:** [https://github.com/tvquang0511/HW01-QA-QC](https://github.com/tvquang0511/HW01-QA-QC)  
**Issues URL:** [https://github.com/tvquang0511/HW01-QA-QC/issues](https://github.com/tvquang0511/HW01-QA-QC/issues)  

---

### Hướng dẫn thao tác:
1. Bạn mở trình duyệt, truy cập vào link: [https://github.com/tvquang0511/HW01-QA-QC/issues](https://github.com/tvquang0511/HW01-QA-QC/issues)
2. Bấm nút màu xanh lá cây **"New issue"** ở góc phải.
3. Lần lượt tạo 5 Issues dưới đây (copy Title và Nội dung Body dán vào).
4. Sau khi tạo xong cả 5 issues, quay lại màn hình danh sách Issues, chụp toàn màn hình sao cho thấy rõ **Avatar + Username `tvquang0511`** ở góc trên bên phải.
5. Lưu ảnh chụp đó thành: `HW01-QA-QC/03-physical-product/github_issues.png`.

---

### Issue 1
- **Title:** `[DEFECT-01] [Touch Panel] Loạn cảm ứng và tự nhảy công suất khi bị tràn nước trên mặt kính`
- **Labels:** `bug`, `hardware`, `severity:high`
- **Body:**
  ```markdown
  ### Mô tả sự cố (Description)
  Khi nước canh hoặc chất lỏng sôi trào ra khu vực cụm phím cảm ứng, bếp không tự động khóa an toàn mà bị hiện tượng nhảy nấc công suất liên tục do điện dung của nước kích hoạt phím ảo.

  ### Thiết bị & Môi trường (Environment)
  - Thiết bị: Bếp hồng ngoại đơn Sunhouse SHD6012A (Năm 2024)
  - Nguồn điện: 220V / 50Hz
  - Số Serial: SHD6012A-24****88

  ### Các bước tái hiện (Steps to Reproduce)
  1. Bật bếp hoạt động ở mức công suất 1600W.
  2. Dùng muỗng làm tràn khoảng 20-30ml nước lọc lên cụm phím điều khiển (Tăng/Giảm/Chức năng).
  3. Quan sát phản ứng của màn hình LED và mâm nhiệt.

  ### Kết quả kỳ vọng (Expected Result)
  Cảm biến nhận diện chạm đa điểm bất thường (ghost touches) và phát tiếng kêu bíp cảnh báo, đồng thời tự động ngắt nhiệt hoặc vô hiệu hóa phím để tránh nguy hiểm.

  ### Kết quả thực tế (Actual Result)
  Bếp kêu bíp liên tục, công suất tự động nhảy loạn xạ (từ 1600W nhảy lên 2000W rồi tụt xuống mức khác), tiềm ẩn nguy cơ cháy khét thức ăn.

  ### Mức độ nghiêm trọng (Severity)
  High (Ảnh hưởng trực tiếp đến an toàn vận hành và nguy cơ trào thức ăn gây hỏng linh kiện).
  ```

---

### Issue 2
- **Title:** `[DEFECT-02] [Safety] Không có cảm biến phát hiện nồi, mâm nhiệt tiếp tục đỏ rực 2000W khi nhấc nồi ra`
- **Labels:** `bug`, `safety`, `severity:critical`
- **Body:**
  ```markdown
  ### Mô tả sự cố (Description)
  Không giống như bếp từ tự động ngắt mạch báo lỗi E0 khi nhấc dụng cụ nấu ra ngoài, mâm nhiệt hồng ngoại của Sunhouse SHD6012A vẫn tiếp tục đốt đỏ rực ở công suất cực đại 2000W khi không có nồi trên bếp.

  ### Thiết bị & Môi trường (Environment)
  - Thiết bị: Bếp hồng ngoại Sunhouse SHD6012A
  - Công suất kiểm tra: 2000W (Mức tối đa)

  ### Các bước tái hiện (Steps to Reproduce)
  1. Đặt nồi nước lên bếp và bật chế độ đun ở 2000W.
  2. Mâm nhiệt phát sáng đỏ rực.
  3. Dùng tay nhấc bổng nồi ra khỏi mặt bếp trong 2 phút.

  ### Kết quả kỳ vọng (Expected Result)
  Hệ thống cảm biến hồng ngoại / quang học phát hiện không có tải nhiệt (No-load) và phát cảnh báo âm thanh hoặc tự động hạ công suất sau 30 giây để chống lãng phí năng lượng và hỏa hoạn.

  ### Kết quả thực tế (Actual Result)
  Bếp vẫn tiếp tục phát nhiệt tối đa vô tận (>650°C), tỏa nhiệt lượng khổng lồ ra môi trường xung quanh, cực kỳ nguy hiểm nếu người dùng quên tắt bếp.

  ### Mức độ nghiêm trọng (Severity)
  Critical (Rủi ro hỏa hoạn và gây bỏng nghiêm trọng cho người xung quanh).
  ```

---

### Issue 3
- **Title:** `[DEFECT-03] [Thermal Architecture] Mất hoàn toàn cảnh báo nhiệt dư "H" và tắt quạt cưỡng bức khi rút phích cắm điện`
- **Labels:** `bug`, `thermal`, `ux`, `severity:high`
- **Body:**
  ```markdown
  ### Mô tả sự cố (Description)
  Khi người dùng rút phích cắm điện ngay sau khi tắt bếp, quạt làm mát lập tức ngừng quay và màn hình cảnh báo nhiệt dư chữ "H" (Hot) biến mất hoàn toàn, dù mặt kính lúc này vẫn ở nhiệt độ >250°C.

  ### Thiết bị & Môi trường (Environment)
  - Thiết bị: Bếp hồng ngoại Sunhouse SHD6012A
  - Nhiệt độ mâm nhiệt lúc tắt: ~300°C

  ### Các bước tái hiện (Steps to Reproduce)
  1. Đun nước ở công suất 2000W trong 5 phút.
  2. Nhấn nút Tắt (Off). Màn hình nhấp nháy chữ "H" và quạt tản nhiệt đang quay để xả nhiệt.
  3. Rút phích cắm điện trực tiếp khỏi ổ cắm tường.

  ### Kết quả kỳ vọng (Expected Result)
  Bếp nên có tụ lưu hoặc cảnh báo trực quan cơ học (hoặc tem đổi màu theo nhiệt độ) để người dùng nhận biết mặt kính còn rất nóng ngay cả khi không cắm điện.

  ### Kết quả thực tế (Actual Result)
  Toàn bộ màn hình tắt ngúm, không còn dấu hiệu nhận biết nhiệt độ; quạt dừng quay đột ngột làm nhiệt dư om ngược vào bo mạch chủ bên dưới, làm giảm tuổi thọ tụ điện và linh kiện bán dẫn.

  ### Mức độ nghiêm trọng (Severity)
  High (Gây nguy cơ bỏng tay bất ngờ cho người khác khi dọn dẹp và giảm độ bền của bếp).
  ```

---

### Issue 4
- **Title:** `[DEFECT-04] [Child Lock UX] Phím Nguồn (Power) vẫn hoạt động khi đang ở chế độ Khóa trẻ em`
- **Labels:** `bug`, `ux`, `severity:medium`
- **Body:**
  ```markdown
  ### Mô tả sự cố (Description)
  Khi chế độ Khóa trẻ em (Child Lock) đang được bật, phím Nguồn (Power / On-Off) vẫn không bị khóa, cho phép bấm tắt phụt bếp bất kỳ lúc nào.

  ### Thiết bị & Môi trường (Environment)
  - Thiết bị: Bếp hồng ngoại Sunhouse SHD6012A
  - Chế độ: Hầm canh kéo dài có khóa trẻ em

  ### Các bước tái hiện (Steps to Reproduce)
  1. Bật bếp ở chế độ Hầm 800W.
  2. Nhấn giữ phím Lock trong 2 giây để kích hoạt khóa trẻ em (đèn Lock sáng).
  3. Thử nhấn nút Tăng, Giảm -> bị vô hiệu hóa (Đúng).
  4. Nhấn phím Bật/Tắt (Power).

  ### Kết quả kỳ vọng (Expected Result)
  Phím Nguồn phải yêu cầu nhấn giữ 3 giây hoặc mở khóa trước mới cho tắt, nhằm ngăn trẻ nhỏ vô tình chạm tay làm ngắt quãng chu trình nấu nướng.

  ### Kết quả thực tế (Actual Result)
  Bếp tắt ngay lập tức chỉ với 1 lần chạm nhẹ vào nút Nguồn, hủy bỏ toàn bộ cài đặt hẹn giờ và làm gián đoạn chu trình nấu ăn.

  ### Mức độ nghiêm trọng (Severity)
  Medium (Ảnh hưởng đến trải nghiệm người dùng, gây hỏng món ăn đang ninh hầm nhiều giờ).
  ```

---

### Issue 5
- **Title:** `[DEFECT-05] [Volatile Memory] Mất toàn bộ cấu hình hẹn giờ và mức công suất khi điện lưới sụt áp ngắn hạn`
- **Labels:** `bug`, `firmware`, `hardware-limitation`, `severity:medium`
- **Body:**
  ```markdown
  ### Mô tả sự cố (Description)
  Bộ vi điều khiển của bếp không có bộ nhớ lưu trạng thái (Non-volatile memory / EEPROM) cho các tác vụ hẹn giờ; khi điện lưới bị sụt áp hoặc chớp nháy trong 0.5s - 1s, bếp bị xóa sạch cấu hình.

  ### Thiết bị & Môi trường (Environment)
  - Thiết bị: Bếp hồng ngoại Sunhouse SHD6012A
  - Kịch bản: Hẹn giờ 45 phút ở 1000W

  ### Các bước tái hiện (Steps to Reproduce)
  1. Bật bếp ở mức 1000W và cài đặt hẹn giờ đếm lùi 45 phút.
  2. Bếp đếm lùi được 10 phút.
  3. Tạo gián đoạn nguồn điện trong 1 giây (rút phích cắm rồi cắm lại ngay).

  ### Kết quả kỳ vọng (Expected Result)
  Vi điều khiển lưu vết thời gian vào bộ nhớ tạm hoặc phát tiếng bíp cảnh báo lỗi nguồn để người dùng biết bếp đã ngừng hoạt động.

  ### Kết quả thực tế (Actual Result)
  Bếp trở về trạng thái Standby ban đầu (`--:--`), toàn bộ bộ đếm thời gian 35 phút còn lại bị xóa sạch và bếp ngừng nấu trong im lặng, người dùng không hề hay biết thức ăn bị nguội ngắt.

  ### Mức độ nghiêm trọng (Severity)
  Medium (Gây gián đoạn trải nghiệm nấu nướng gia đình khi điện áp không ổn định).
  ```
