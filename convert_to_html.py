import os
import sys
import subprocess

# Tu dong kiem tra va cai dat thu vien markdown neu chua co
try:
    import markdown
except ImportError:
    print("Thu vien 'markdown' chua duoc cai dat. Tien hanh cai dat tu dong...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

# Duong dan file
md_path = "BAOCAO_OUTLINE_FOR_REVIEW.md"
html_path = "BAOCAO_OUTLINE_FOR_REVIEW.html"

if not os.path.exists(md_path):
    print(f"Khong tim thay file nguon: {md_path}")
    sys.exit(1)

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Chuyen doi markdown sang html (ho tro tables va fenced code)
html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Template HTML voi thiet ke hoc thuat cao cap (Academic & Clean)
html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đề cương chi tiết Đồ án tốt nghiệp - Review Outline</title>
    <style>
        :root {{
            --primary-color: #1a365d;
            --secondary-color: #2b6cb0;
            --text-color: #2d3748;
            --bg-color: #f7fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: var(--text-color);
            background-color: var(--bg-color);
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }}

        .container {{
            max-width: 850px;
            margin: 40px auto;
            background: var(--card-bg);
            padding: 50px 60px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            border-radius: 12px;
            border-top: 6px solid var(--primary-color);
        }}

        /* Typography */
        h1 {{
            color: var(--primary-color);
            font-size: 24px;
            text-align: center;
            margin-top: 0;
            margin-bottom: 15px;
            line-height: 1.4;
            font-weight: 700;
        }}

        h2 {{
            color: var(--primary-color);
            font-size: 18px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 6px;
            margin-top: 35px;
            margin-bottom: 15px;
            font-weight: 600;
        }}

        h3 {{
            color: var(--secondary-color);
            font-size: 15px;
            margin-top: 22px;
            margin-bottom: 10px;
            font-weight: 600;
        }}

        p {{
            margin-top: 0;
            margin-bottom: 12px;
            text-align: justify;
            font-size: 14.5px;
        }}

        ul, ol {{
            margin-top: 0;
            margin-bottom: 18px;
            padding-left: 20px;
        }}

        li {{
            margin-bottom: 6px;
            font-size: 14.5px;
        }}

        hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 25px 0;
        }}

        strong {{
            color: #1a202c;
        }}

        /* Table Styling */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 13.5px;
        }}

        table th, table td {{
            border: 1px solid var(--border-color);
            padding: 8px 12px;
            text-align: left;
        }}

        table th {{
            background-color: #edf2f7;
            color: var(--primary-color);
            font-weight: 600;
        }}

        table tr:nth-child(even) {{
            background-color: #f8fafc;
        }}

        /* Floating Print Button */
        .print-btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(26, 54, 93, 0.3);
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            z-index: 1000;
        }}

        .print-btn:hover {{
            background-color: var(--secondary-color);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(43, 108, 176, 0.4);
        }}

        .print-btn svg {{
            width: 16;
            height: 16;
        }}

        /* CSS Academic Print Specification (A4) */
        @media print {{
            body {{
                background-color: #ffffff;
                color: #000000;
                font-family: "Times New Roman", Times, serif;
                font-size: 12pt;
                line-height: 1.5;
            }}

            .container {{
                margin: 0;
                padding: 0;
                box-shadow: none;
                max-width: 100%;
                border: none;
            }}

            .print-btn {{
                display: none;
            }}

            h1 {{
                font-size: 16pt;
                font-weight: bold;
                text-transform: uppercase;
            }}

            h2 {{
                font-size: 13pt;
                font-weight: bold;
                border-bottom: 1px solid #000000;
                margin-top: 25pt;
                margin-bottom: 12pt;
            }}

            h3 {{
                font-size: 12pt;
                font-weight: bold;
                margin-top: 18pt;
                margin-bottom: 8pt;
            }}

            p, li {{
                font-size: 12pt;
            }}

            table {{
                font-size: 11pt;
                page-break-inside: avoid;
            }}

            tr {{
                page-break-inside: avoid;
            }}
            
            @page {{
                size: A4;
                margin: 20mm 20mm 20mm 25mm; /* Le chuan hoc thuat: trai 2.5cm, cac le khac 2cm */
            }}
        }}
    </style>
</head>
<body>

    <div class="container">
        {html_body}
    </div>

    <button class="print-btn" onclick="window.print()">
        <svg fill="currentColor" viewBox="0 0 16 16">
            <path d="M2.5 8a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/>
            <path d="M5 1a2 2 0 0 0-2 2v2H2a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h1v1a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1h1a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1V3a2 2 0 0 0-2-2H5zM4 3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2H4V3zm1 5a2 2 0 0 0-2 2v1H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v-1a2 2 0 0 0-2-2H5zm7 2v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1z"/>
        </svg>
        In báo cáo (Xuất PDF)
    </button>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"SUCCESS: Da tao file {html_path} thanh cong!")
