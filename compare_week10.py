import re

def normalize_text(text):
    text = re.sub(r'(?<!\\)%.*', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    file1 = r"content\week10-04-28-25-tuesday.tex"
    file2 = r"content\week10-step4-04-28-25-tuesday-all-offset-final.tex"

    print("Reading files...")
    with open(file1, 'r', encoding='utf-8') as f:
        c1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        c2 = f.read()

    norm1 = normalize_text(c1)
    norm2 = normalize_text(c2)

    print(f"File 1 normalized length: {len(norm1)}")
    print(f"File 2 normalized length: {len(norm2)}")

    if norm1 in norm2:
        print("SUCCESS: File 1 content is fully present in File 2!")
        return

    # Check sentence or line presence
    # Splitting by common sentence endings and TeX commands to see what is missing
    # Let's clean and extract chunks
    # We can split by paragraphs (double newlines)
    paras1 = [p.strip() for p in c1.split('\n\n') if p.strip()]
    
    missing_paras = []
    for idx, p in enumerate(paras1):
        # strip comments
        lines_clean = []
        for line in p.split('\n'):
            line = line.strip()
            if line.startswith('%'):
                continue
            # remove inline comments
            line = re.sub(r'(?<!\\)%.*', '', line)
            if line:
                lines_clean.append(line)
        p_clean = " ".join(lines_clean)
        norm_p = normalize_text(p_clean)
        if not norm_p:
            continue
            
        if norm_p not in norm2:
            missing_paras.append((idx, p_clean))

    print(f"Total paragraphs in File 1: {len(paras1)}")
    print(f"Missing paragraphs: {len(missing_paras)}")
    for idx, p in missing_paras[:10]:
        print(f"--- Paragraph {idx} ---")
        print(p[:200] + ("..." if len(p) > 200 else ""))

if __name__ == '__main__':
    main()
