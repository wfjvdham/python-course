filename = '07_io/some_text.txt'

import os
os.getcwd()

try:
    f = open(filename)
except Exception:
    print('Cannot open file')

rcount = 0
wcount = 0
ccount = 0

for regel in f:
    rcount += 1
    wcount += len(regel.split())
    ccount += len(regel)

print(rcount, wcount, ccount)
f.close()