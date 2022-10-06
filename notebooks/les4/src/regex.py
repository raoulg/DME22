import re
from pathlib import Path

from settings import settings

source_file = settings.raw_data_dir / settings.regex_practice_file
txt = source_file.read_text(encoding='utf8')
lines = txt.splitlines()

pattern = r'(?<=\n)\d{1}\.\d?\.?\s.+'
pattern_per_line = r'^\d{1}\.\d?\.?\s.+'


# for m in re.finditer(pattern, txt):
#     print(m.group(0))
# pass

for line in lines:
    m = re.match(pattern_per_line, line)
    if m:
        print(m.group(0))

# print(txt)
hr = f"\n{'-' * 80}\n"

# Hoofdstukken
print(hr + 'Hoofdstukken:\n')
pattern = re.compile(r'^([\d\.]+\. .+)')
for line in txt.splitlines():
    m = re.match(pattern, line)
    if m:
        print(m.group(0))
        
# Onderdeel
print(hr + 'Onderdelen:\n')
pattern = re.compile(r'[oO]nderdeel\s\d+')
for m in re.findall(pattern, txt):
    print(m)
        
# Datums (met findall)
print(hr + 'Datums:\n')
pattern = re.compile(r'\d{1,2}\-\d{1,2}\-\d{4}|\d{1,2}\s\w+\s\d{4}')
for m in re.findall(pattern, txt):
    print(m)
        
# Staatscourantpublicaties.
print(hr + 'Staatscourantpublicaties:\n')
pattern = re.compile(r'Stcrt\.\s(\d+)\,\s(\d+)')
for m in re.finditer(pattern, txt):
    print(f'Jaar: {m.group(0)}, editie: {m.group(1)}')

# Begrippen en afkortingen
print(hr + 'Begrippen en afkortingen:\n')
pattern = re.compile(r'^([\w\s]+)\s{2,}([\w\s]+)|^\s{2,}([\w\s]+)')
# for line in txt.splitlines():
#     m = re.match(pattern, line)
#     if m:
#         print(f'{m.group(0)} | {m.group(1)}')
# matches = re.match(pattern, lines)
# if matches:
#     for m in matches:
#         print(m)
# else:
#     print('no matches')