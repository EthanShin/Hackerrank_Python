M = int(input())
arr = set(map(int, input().split()))

N = int(input())
arr2 = set(map(int, input().split()))

print(*sorted(arr.difference(arr2).union(arr2.difference(arr))), sep='\n')