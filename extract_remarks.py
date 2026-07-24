import os
import re

content_dir = r"c:\Users\miche\latex\eth-grundstrukturen-fs2026-ki-trankskription\content"

# Regex for spoken-clean blocks
spoken_clean_re = re.compile(r'\\begin\{spoken-clean\}(.*?)\\end\{spoken-clean\}', re.DOTALL)
# Regex for \inlinemetanote
inlinemetanote_re = re.compile(r'\\inlinemetanote\{([^}]*)\}')
# Regex for parentheses
parens_re = re.compile(r'\(([^)]+)\)')

remarks = []
inlines = []
for filename in os.listdir(content_dir):
    if filename.endswith(".tex"):
        filepath = os.path.join(content_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            for match in spoken_clean_re.finditer(content):
                block = match.group(1)
                
                # Find inlinemetanotes
                for m in inlinemetanote_re.finditer(block):
                    inlines.append((filename, m.group(1).strip()))
                
                # Find parens
                for m in parens_re.finditer(block):
                    parens_text = m.group(1).strip()
                    # filter out math looking things or very short things if necessary
                    # but let's just collect them all and see
                    remarks.append((filename, parens_text))

with open('scratch_remarks.txt', 'w', encoding='utf-8') as f:
    f.write("--- INLINE META NOTES ---\n")
    for file, note in inlines:
        f.write(f"{file}: {note}\n")
    f.write("\n--- PARENTHESES ---\n")
    for file, note in remarks:
        f.write(f"{file}: {note}\n")
print("Done")
