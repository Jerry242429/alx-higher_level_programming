#1/usr/bin/python3
if __name__ == "__main__":
    import sys

    c = len(sys.argv) - 1
    if c == 1:
         print("{} argument:".format(c))
    elif c == 0:
        print("0 arguments.")
    else: 
        print("{} arguments:".format(c))
    for l in range(c):
        print("{}: {}".format(l + 1, sys.argv[l + 1]))
