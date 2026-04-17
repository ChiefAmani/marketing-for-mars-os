import markdown

with open('ad_copy.md', 'r') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MARS OS Ad Copy</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        h2 {{ margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
        ul {{ margin-bottom: 20px; }}
        li {{ margin-bottom: 5px; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""

with open('final_ad_copy.html', 'w') as f:
    f.write(full_html)
