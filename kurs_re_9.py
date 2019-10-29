import sys
import re


for line in sys.stdin:
    line = line.rstrip()

    # this is a big question
    # motherfuskerstvo

    # match = re.match(r'(\w)\1*', line)
    # print(match)
    # print(match.groups())
    line = re.sub(r'(\w)\1*', r'\1', line)
    print(line)