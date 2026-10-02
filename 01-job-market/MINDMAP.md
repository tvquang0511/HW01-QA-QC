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
