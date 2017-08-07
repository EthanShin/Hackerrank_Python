n = input()
s1 = set(input().split())
b = input()
s2 = set(input().split())

print(len(s1.symmetric_difference(s2)))