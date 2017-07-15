if __name__ == '__main__':
    N = int(input())

    mylist = []
    for i in range(0, N):
        string = input().split()
        cmd = string[0]
        args = string[1:]
        
        if cmd != "print":
            cmd += "(" + "," .join(args) + ")"
            eval("mylist." + cmd)
        else:
            print(mylist)