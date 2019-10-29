import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'\b[Aa]+\b', 'argh', line, 1)
    print(line)


# line = re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE)