#!/usr/bin/python3
import sys
import os

def convert_markdown_to_html(readme, output):
    if not os.path.exists(readme):
        print(f"Missing {readme}")
        return

    with open(readme, "r", encoding="utf-8") as readme_file:
        html = ""
        in_list = False

        for line in readme_file:
            if line.startswith('#'):
                level = min(line.count('#'), 6)
                tag = f"h{level}"
                html += f"<{tag}>{line.strip('#').strip()}</{tag}>\n"
            elif line.startswith('-'):
                if not in_list:
                    html += "<ul>\n"
                    in_list = True
                html += f"<li>{line.strip('-').strip()}</li>\n"
            elif line.startswith('='):
                if not in_list:
                    html += "<ol>\n"
                    in_list = True
                html += f"<li>{line.strip('=').strip()}</li>\n"
            else:
                others = line.splitlines()
                for i in others:
                    bold = i.split(
                    print(bold)



        if in_list:
            html += "</ul>\n"

    with open(output, "w", encoding='utf-8') as output_file:
        output_file.write(html)
        print(f"HTML content written to '{output}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    readme = sys.argv[1]
    output = sys.argv[2]

    convert_markdown_to_html(readme, output)

