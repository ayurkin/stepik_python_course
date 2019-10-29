import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    print(re.match(r'\b(\w)(\w)', line).groups())
    # line = re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line)
    line = re.sub(r'\b(\w)(\w)', r'\2\1', line)
    print(line)