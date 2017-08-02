n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    op = input().split()
    
    if op[0] == 'pop':
        s.pop()
    elif op[0] == 'remove':
        s.remove(int(op[1]))
    elif op[0] == 'discard':
        s.discard(int(op[1]))
        
print(sum(s))