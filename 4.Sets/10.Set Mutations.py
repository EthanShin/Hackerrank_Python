number_of_element = input()
a = set(input().split())
for _ in range(int(input())):
    getattr(a, input().split()[0])(set(input().split()))
    
print(sum(map(int,a)))