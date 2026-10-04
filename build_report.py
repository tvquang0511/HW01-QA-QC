import os
import re

def build_master_report():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Read components
    with open(os.path.join(base_dir, "01-job-market", "job_market_report.md"), "r", encoding="utf-8") as f:
        r1_jobs = f.read()
    
    with open(os.path.join(base_dir, "01-job-market", "MINDMAP.md"), "r", encoding="utf-8") as f:
        r1_mindmap = f.read()
        
    with open(os.path.join(base_dir, "02-software-defects", "software_defects.md"), "r", encoding="utf-8") as f:
        r2_defects = f.read()
        
    with open(os.path.join(base_dir, "03-physical-product", "physical_product.md"), "r", encoding="utf-8") as f:
        r3_physical = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "AI-02_Audit_Report.md"), "r", encoding="utf-8") as f:
        ai_02 = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "AI-03_Disclosure_Form.md"), "r", encoding="utf-8") as f:
        ai_03 = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "AI-05_Privacy_Checklist.md"), "r", encoding="utf-8") as f:
        ai_05 = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "AI-06_Student_Acknowledgement.md"), "r", encoding="utf-8") as f:
        ai_06 = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "AI_Critique.md"), "r", encoding="utf-8") as f:
        ai_critique = f.read()
        
    with open(os.path.join(base_dir, "04-ai", "PROMPT_LOG.md"), "r", encoding="utf-8") as f:
        prompt_log = f.read()

    # Adjust image paths for root context
    # In r1_jobs: 'image/' -> '01-job-market/image/'
    r1_jobs_fixed = re.sub(r'!\[(.*?)\]\(image/(.*?)\)', r'![\1](01-job-market/image/\2)', r1_jobs)
    
    # In r3_physical: 'assets/' -> '03-physical-product/assets/'
    r3_physical_fixed = re.sub(r'!\[(.*?)\]\(assets/(.*?)\)', r'![\1](03-physical-product/assets/\2)', r3_physical)

    header = """# BÁO CÁO BÀI TẬP 01: QA/QC JOBS · 20 DEFECTS · TEST A PHYSICAL PRODUCT

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
"""

    rubric_and_refs = """
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
"""

    master_content = "\n\n".join([
        header,
        r1_jobs_fixed,
        "\n---\n",
        r1_mindmap,
        "\n---\n",
        r2_defects,
        "\n---\n",
        r3_physical_fixed,
        "\n---\n",
        "# Requirement 4 – Giao thức Cộng tác & Kiểm toán AI (Mandatory AI Compliance)\n",
        ai_02,
        "\n---\n",
        ai_03,
        "\n---\n",
        ai_05,
        "\n---\n",
        ai_06,
        "\n---\n",
        ai_critique,
        "\n---\n",
        prompt_log,
        rubric_and_refs
    ])

    report_md_path = os.path.join(base_dir, "REPORT.md")
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write(master_content)
    print(f"REPORT.md built successfully: {report_md_path}")

    sub_md_path = os.path.join(base_dir, "23120346_HW01_AI_100.md")
    with open(sub_md_path, "w", encoding="utf-8") as f:
        f.write(master_content)
    print(f"23120346_HW01_AI_100.md built successfully: {sub_md_path}")

if __name__ == "__main__":
    build_master_report()
