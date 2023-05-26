#!/usr/bin/python
#
# a simple program to demonstrate the fds class
#
from fds import fds

f = fds.FDs()
f.addfd(fds.FDs.mkfd('S', 'N'))
f.addfd(fds.FDs.mkfd('P', 'F'))
f.addfd(fds.FDs.mkfd('C', 'L'))
f.addfd(fds.FDs.mkfd('SC', 'G'))

print('Keys')
print(f.keys())
print('Minimal Cover')
print(f.minimalCover())
print("Is 3nf", f.is3nf())
print("Is BCNF", f.isbcnf())
print("Complete FD closure")
for fdc in f.fdclosure():
    print(''.join(fdc[0]), '->', ''.join(fdc[1]), fdc[2] or '')
