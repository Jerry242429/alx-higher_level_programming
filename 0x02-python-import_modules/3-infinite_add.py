#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    to = 0
    le = len(sys.argv)
    for i in range(1, le):
        to += int(sys.argv[i])
    print("{}".format(to))
