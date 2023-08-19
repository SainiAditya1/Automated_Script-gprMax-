import os

machine = os.uname().machine

if machine == 'arm64':
    print("Apple M1 processor detected.")
else:
    print("Not an Apple M1 processor.")
