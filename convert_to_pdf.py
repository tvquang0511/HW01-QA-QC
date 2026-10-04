import markdown
import os
import subprocess
import shutil

def convert_md_to_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(base_dir, "REPORT.md")
    
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists'])

    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>HW01 - Trần Vũ Quang - 23120346</title>
<style>
    @page {{
        size: A4;
        margin: 18mm 15mm 18mm 15mm;
        @bottom-right {{
            content: counter(page);
        }}
    }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 13px;
        line-height: 1.6;
        color: #24292e;
        padding: 0;
        margin: 0;
    }}
    h1 {{
        font-size: 20px;
        border-bottom: 2px solid #1f497d;
        padding-bottom: 8px;
        color: #1f497d;
        margin-top: 24px;
        page-break-after: avoid;
    }}
    h2 {{
        font-size: 16px;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 6px;
        color: #2b579a;
        margin-top: 20px;
        page-break-after: avoid;
    }}
    h3 {{
        font-size: 14px;
        color: #1f497d;
        margin-top: 16px;
        page-break-after: avoid;
    }}
    h4 {{
        font-size: 13px;
        color: #333;
        margin-top: 12px;
        page-break-after: avoid;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 14px 0;
        page-break-inside: avoid;
        font-size: 11px;
    }}
    th, td {{
        border: 1px solid #d0d7de;
        padding: 6px 8px;
        text-align: left;
        vertical-align: top;
    }}
    th {{
        background-color: #f2f5f9;
        font-weight: 600;
        color: #1f497d;
    }}
    tr:nth-child(even) {{
        background-color: #f8fafc;
    }}
    blockquote {{
        border-left: 4px solid #1f497d;
        padding: 6px 14px;
        color: #4a5568;
        background-color: #f7fafc;
        margin: 12px 0;
        border-radius: 0 4px 4px 0;
    }}
    code {{
        font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 11px;
        background-color: #f3f4f6;
        padding: 2px 4px;
        border-radius: 3px;
    }}
    pre {{
        background-color: #f6f8fa;
        padding: 10px;
        border-radius: 6px;
        overflow-x: auto;
        font-size: 11px;
        border: 1px solid #e1e4e8;
        page-break-inside: avoid;
    }}
    pre code {{
        background: none;
        padding: 0;
    }}
    img {{
        max-width: 85%;
        max-height: 480px;
        object-fit: contain;
        display: block;
        margin: 15px auto;
        border: 1px solid #d0d7de;
        border-radius: 4px;
        page-break-inside: avoid;
    }}
    hr {{
        border: 0;
        height: 1px;
        background: #e1e4e8;
        margin: 20px 0;
    }}
    ul, ol {{
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 4px;
    }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    html_file = os.path.join(base_dir, "REPORT.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    print("REPORT.html written successfully.")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_path):
        pdf_file = os.path.join(base_dir, "23120346_HW01_AI_100.pdf")
        cmd = [
            edge_path,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_file}",
            html_file
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
            print(f"23120346_HW01_AI_100.pdf generated successfully! Size: {os.path.getsize(pdf_file)} bytes")
            # Also copy to REPORT.pdf
            shutil.copyfile(pdf_file, os.path.join(base_dir, "REPORT.pdf"))
            print("REPORT.pdf copied successfully.")
        else:
            print("Edge print failed:", res.stderr)
    else:
        print("Edge binary not found.")

if __name__ == "__main__":
    convert_md_to_pdf()
