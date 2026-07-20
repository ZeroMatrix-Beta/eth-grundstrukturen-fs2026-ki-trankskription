import os
import re
from collections import defaultdict

# Regexes
label_re = re.compile(r'\\label\{([^}]+)\}')
subsection_re = re.compile(r'\\subsection(?:\[.*?\])?\{(.*?)\}')
subsection_star_re = re.compile(r'\\subsection\*\{(.*?)\}')
math_stroke_re = re.compile(r'\\begin\{math-stroke\}\[(.*?)\]')
spoken_re = re.compile(r'\\begin\{spoken-clean\}')
display_math_re = re.compile(r'\$\$')
eqnarray_re = re.compile(r'\\begin\{eqnarray\}')

files_to_check = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root:
        continue
    for file in files:
        if file.endswith('.tex') and not file.startswith('deleted-') and 'deleted-' not in file:
            files_to_check.append(os.path.join(root, file))

labels = defaultdict(list)
issues = []

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    
    in_spoken_clean = False
    open_envs = []
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check labels
        for match in label_re.finditer(line):
            label = match.group(1)
            labels[label].append((filepath, line_num))
            
        # Check for subsection*
        if subsection_star_re.search(line):
            issues.append(f'TOC Issue: \\subsection* used in {filepath}:{line_num} (will not appear in TOC)')
            
        # Check for $$
        if display_math_re.search(line):
            issues.append(f'Math Issue: $$ used in {filepath}:{line_num} (use \\[ \\] instead)')
            
        # Check for eqnarray
        if eqnarray_re.search(line):
            issues.append(f'Math Issue: eqnarray used in {filepath}:{line_num} (use align instead)')
            
        # Check structure
        if '\\begin{spoken-clean}' in line:
            in_spoken_clean = True
        elif '\\end{spoken-clean}' in line:
            in_spoken_clean = False
            
        if in_spoken_clean and '\\subsection' in line:
            issues.append(f'Structure Issue: \\subsection found INSIDE spoken-clean in {filepath}:{line_num}. Rule: put subsection before spoken-clean.')
            
        # Check math environments matching
        env_begin = re.findall(r'\\begin\{([^}]+)\}', line)
        env_end = re.findall(r'\\end\{([^}]+)\}', line)
        for env in env_begin:
            open_envs.append((env, line_num))
        for env in env_end:
            if open_envs and open_envs[-1][0] == env:
                open_envs.pop()
            else:
                issues.append(f'Math Issue: Unmatched \\end{{{env}}} in {filepath}:{line_num}')
                
    if open_envs:
        for env, line_num in open_envs:
            issues.append(f'Math Issue: Unclosed \\begin{{{env}}} starting at {filepath}:{line_num}')
            
    # Check for title duplications (subsection immediately followed by math-stroke with same title)
    # or math-stroke with title but no subsection before the preceding spoken-clean
    for i in range(len(lines) - 1):
        if '\\subsection' in lines[i]:
            sub_match = subsection_re.search(lines[i])
            if sub_match:
                title = sub_match.group(1)
                # Look ahead a few lines
                for j in range(1, 10):
                    if i+j < len(lines):
                        if '\\begin{math-stroke}[' in lines[i+j]:
                            ms_match = math_stroke_re.search(lines[i+j])
                            if ms_match and ms_match.group(1).lower() == title.lower():
                                issues.append(f'Title Duplication: \\subsection and math-stroke have same title "{title}" near {filepath}:{i+1}')
                            break

print('--- DUPLICATE LABELS ---')
found_dups = False
for label, occurrences in labels.items():
    if len(occurrences) > 1:
        found_dups = True
        print(f'Duplicate label: {label} ({len(occurrences)} times)')
        for filepath, line_num in occurrences:
            print(f'  - {filepath} at line {line_num}')
if not found_dups:
    print('No duplicate labels found.')
            
print('\n--- ISSUES ---')
if issues:
    for issue in issues:
        print(issue)
else:
    print('No structural or math issues found.')
