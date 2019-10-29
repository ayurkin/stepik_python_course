import sys
import re


for line in sys.stdin:
    line = line.rstrip()


    match = re.match(r'(1(01*0)*1|0)*', line)
    print(match)
    # print(match.groups())




