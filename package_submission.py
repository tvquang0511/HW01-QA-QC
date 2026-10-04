import os
import zipfile

def package_zip():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_name = "23120346_HW01_AI_100.zip"
    zip_path = os.path.join(base_dir, zip_name)

    files_to_pack = [
        "23120346_HW01_AI_100.pdf",
        "REPORT.pdf",
        "23120346_HW01_AI_100.md",
        "REPORT.md",
        "REPORT.html",
        "Test_Cases_and_Checklist.xlsx",
        os.path.join("03-physical-product", "TEST_CASES.csv"),
        os.path.join("03-physical-product", "GITHUB_ISSUES_GUIDE.md"),
        os.path.join("01-job-market", "MINDMAP.md"),
        os.path.join("04-ai", "AI-02_Audit_Report.md"),
        os.path.join("04-ai", "AI-03_Disclosure_Form.md"),
        os.path.join("04-ai", "AI-05_Privacy_Checklist.md"),
        os.path.join("04-ai", "AI-06_Student_Acknowledgement.md"),
        os.path.join("04-ai", "AI_Critique.md"),
        os.path.join("04-ai", "PROMPT_LOG.md"),
        os.path.join("03-physical-product", "assets", "device_student_id.jpg"),
        os.path.join("03-physical-product", "assets", "github_issues.png"),
        os.path.join("03-physical-product", "assets", "MC1.png"),
        os.path.join("03-physical-product", "assets", "MC2.png"),
    ]

    # Add 10 job screenshot images
    for i in range(1, 11):
        job_dir = os.path.join(base_dir, "01-job-market", "image")
        for f in os.listdir(job_dir):
            if f.endswith(".png"):
                rel_p = os.path.join("01-job-market", "image", f)
                if rel_p not in files_to_pack:
                    files_to_pack.append(rel_p)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for rel_path in files_to_pack:
            full_path = os.path.join(base_dir, rel_path)
            if os.path.exists(full_path):
                zipf.write(full_path, arcname=rel_path)
                print(f"Added: {rel_path}")
            else:
                print(f"Warning: File not found: {full_path}")

    print(f"\nSuccessfully created {zip_name} (Size: {os.path.getsize(zip_path)} bytes)")

if __name__ == "__main__":
    package_zip()
