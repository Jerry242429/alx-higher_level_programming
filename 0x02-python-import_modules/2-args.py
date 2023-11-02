#1/usr/bin/python3
if __name__ == "__main__":
    import sys

    c = len(sys.argv) - 1
    if c == 0:
         print("{} arguments.".format(c))
    elif c == 1:
        print("1 argument:")
    else: 
        print("{} arguments:".format(c))
    for l in range(c):
        print("{}: {}".format(l + 1, sys.argv[l + 1]))
