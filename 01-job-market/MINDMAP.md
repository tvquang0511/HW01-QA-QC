# QA/QC Role & ISTQB Test Process Mindmap (CLO G9.1)

**Exercise:** HW01 – Requirement 1 (CLO G9.1)  
**Standard Referenced:** ISTQB Certified Tester Foundation Level (CTFL) Syllabus v4.0  

---

## 1. Initial AI-Generated Mindmap (Raw AI Mindmap)
Sơ đồ thô do AI sinh ra chứa 3 sai sót trọng yếu về lý thuyết kiểm thử phần mềm:

```mermaid
mindmap
  root((Software Quality))
    Quality Assurance & Control
      ["QA: Bug Finding and Test Execution (Lỗi: sai định nghĩa)"]
      ["QC: Process Improvement and Audits (Lỗi: sai định nghĩa)"]
    Test Levels
      Component Testing
      Integration Testing
      System Testing
      Acceptance Testing
    Test Types
      Functional Testing
      Non-Functional Testing
      Black-box Testing
      White-box Testing
    Test Process
      1. Test Planning
      2. Test Analysis & Design (Lỗi: gộp chung 2 pha)
      3. Test Execution
      4. Test Monitoring & Control (Lỗi: vẽ thành bước tuần tự #4)
      5. Test Completion
```

---

## 2. Phân tích chi tiết 3 lỗi sai của AI (đối chiếu ISTQB CTFL v4.0)

### Lỗi 1: Đảo ngược hoàn toàn định nghĩa cốt lõi giữa QA và QC
- **Sai sót của AI:** AI gán *"Tìm lỗi và thực thi kiểm thử"* cho **QA**, và gán *"Cải tiến quy trình và đánh giá chất lượng"* cho **QC**.
- **Cơ sở chuẩn mực ISTQB CTFL v4.0 (Mục 1.2.2):**
  - **QA (Quality Assurance)** là hoạt động mang tính **phòng ngừa và định hướng quy trình (process-oriented)**, tập trung vào việc thiết lập và cải tiến các quy trình phát triển nhằm ngăn ngừa lỗi phát sinh ngay từ đầu.
  - **QC (Quality Control)** là hoạt động mang tính **sửa sai và định hướng sản phẩm (product-oriented)**, bao gồm việc thực thi kiểm thử phần mềm để phát hiện lỗi cụ thể trong sản phẩm.
- **Tác động:** Làm sai lệch hoàn toàn vai trò và trách nhiệm trong tổ chức kỹ thuật.

### Lỗi 2: Bỏ sót hoàn toàn Kiểm thử tĩnh (Static Testing)
- **Sai sót của AI:** AI chỉ liệt kê các khái niệm kiểm thử động, hoàn toàn bỏ qua nhánh **Static Testing**, đồng thời gộp lẫn lộn giữa *Kỹ thuật kiểm thử (Black-box / White-box)* và *Loại kiểm thử (Functional / Non-functional)*.
- **Cơ sở chuẩn mực ISTQB CTFL v4.0 (Chương 3):**
  - Kiểm thử bao gồm hai trụ cột song hành: **Static Testing** (rà soát yêu cầu, thiết kế và phân tích tĩnh mã nguồn mà không cần chạy code) và **Dynamic Testing** (thực thi mã với dữ liệu đầu vào). Bỏ qua Static Testing làm mất đi phương pháp ngăn chặn lỗi sớm và tiết kiệm chi phí nhất.

### Lỗi 3: Vẽ Test Monitoring & Control thành bước tuần tự thứ 4
- **Sai sót của AI:** AI xếp *"Test Monitoring & Control"* thành bước thứ 4 (nằm sau Test Execution và trước Test Completion); đồng thời gộp chung *Test Analysis & Design* và bỏ quên pha *Test Implementation*.
- **Cơ sở chuẩn mực ISTQB CTFL v4.0 (Mục 1.4.1 & 1.4.2):**
  - **Test Monitoring and Control** là hoạt động **quản trị xuyên suốt (transversal governance)**, diễn ra liên tục song song trong tất cả các giai đoạn kiểm thử.
  - Quy trình kiểm thử chuẩn gồm các giai đoạn phân định rõ: *Test Planning, Test Analysis (phân tích CÁI GÌ cần test), Test Design (thiết kế test case NHƯ THẾ NÀO), Test Implementation (chuẩn bị dữ liệu/môi trường/kịch bản tự động), Test Execution, và Test Completion*.

---

## 3. Sơ đồ chuẩn hóa toàn diện theo ISTQB CTFL v4.0

```mermaid
flowchart TD
    %% Root
    Root(["HỆ THỐNG QUẢN LÝ CHẤT LƯỢNG PHẦN MỀM<br/>(Software Quality Management - ISTQB v4.0)"]):::rootNode

    %% 2 Branch chính: QA & QC
    Root --> QA["QUẢNG LÝ ĐẢM BẢO CHẤT LƯỢNG (QA)<br/><i>(Process-oriented / Prevention)</i>"]:::qaNode
    Root --> QC["KIỂM SOÁT CHẤT LƯỢNG (QC)<br/><i>(Product-oriented / Detection)</i>"]:::qcNode

    %% QA Activities
    QA --> QA1["Xây dựng quy trình chuẩn & Best Practices"]
    QA --> QA2["Đánh giá chất lượng định kỳ (Quality Audits)"]
    QA --> QA3["Phân tích nguyên nhân gốc rễ (Root Cause Analysis)"]
    QA --> QA4["Đào tạo văn hóa chất lượng ngăn ngừa lỗi sớm"]

    %% QC Activities
    QC --> QC1["Đánh giá sản phẩm trung gian (Work Product Inspection)"]
    QC --> QC2["Kiểm thử phần mềm (Software Testing)"]

    %% Nhánh kiểm thử (Testing Disciplines)
    QC2 --> Static["KIỂM THỬ TĨNH (Static Testing)<br/><i>(Không thực thi mã nguồn)</i>"]:::staticNode
    QC2 --> Dynamic["KIỂM THỬ ĐỘNG (Dynamic Testing)<br/><i>(Thực thi mã với dữ liệu đầu vào)</i>"]:::dynamicNode

    %% Static Testing details
    Static --> S1["Reviews tài liệu (Requirements, User Stories, Design)"]
    Static --> S2["Phân tích mã nguồn tĩnh (Static Analysis / Linters / SAST)"]

    %% Dynamic Testing details
    Dynamic --> D1["Kiểm thử chức năng (Functional Testing)"]
    Dynamic --> D2["Kiểm thử phi chức năng (Performance, Security, Usability)"]
    Dynamic --> D3["Kiểm thử liên quan thay đổi (Confirmation & Regression)"]

    %% Quy trình kiểm thử chuẩn 7 bước (Transversal Governance)
    Root ==> Process["QUY TRÌNH KIỂM THỬ CHUẨN (ISTQB Test Process)"]:::processNode

    subgraph Governance ["HOẠT ĐỘNG GIÁM SÁT XUYÊN SUỐT (Transversal Activity)"]
        MonCtrl["Test Monitoring & Control<br/><i>(Chạy liên tục, song song qua tất cả các pha)</i>"]:::monNode
    end

    subgraph CoreProcess ["CÁC GIAI ĐOẠN KIỂM THỬ TUẦN TỰ (Sequential Phases)"]
        direction TB
        P1["1. Test Planning<br/><i>(Xác định phạm vi, mục tiêu, rủi ro, nguồn lực)</i>"]
        P2["2. Test Analysis<br/><i>(Phân tích cơ sở kiểm thử - CÁI GÌ cần test?)</i>"]
        P3["3. Test Design<br/><i>(Thiết kế Test Cases, dữ liệu kiểm thử - Test NHƯ THẾ NÀO?)</i>"]
        P4["4. Test Implementation<br/><i>(Chuẩn bị môi trường, test suites, automation scripts)</i>"]
        P5["5. Test Execution<br/><i>(Chạy test suites, ghi nhận kết quả và log Defect)</i>"]
        P6["6. Test Completion<br/><i>(Đánh giá tiêu chí kết thúc, lưu trữ testware, bài học)</i>"]
        
        P1 --> P2 --> P3 --> P4 --> P5 --> P6
    end

    Process --> Governance
    Process --> CoreProcess
    MonCtrl -.->|Giám sát liên tục| CoreProcess

    %% Class styles
    classDef rootNode fill:#1E293B,stroke:#0F172A,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef qaNode fill:#0284C7,stroke:#0369A1,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef qcNode fill:#0D9488,stroke:#0F766E,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef processNode fill:#4F46E5,stroke:#4338CA,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef monNode fill:#DC2626,stroke:#B91C1C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef staticNode fill:#F59E0B,stroke:#D97706,stroke-width:1px,color:#000000
    classDef dynamicNode fill:#10B981,stroke:#059669,stroke-width:1px,color:#FFFFFF
```
