import sys

try:
    print(1 / 0)
except:
    raise RuntimeError("Something Bad happened.")

    