import sys
import re
pattern = r"cat*"
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        print(line)


    # if re.search(r"cat.*cat", line):
    #     print(line)