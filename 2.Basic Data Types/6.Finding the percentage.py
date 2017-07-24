if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = 0
    for i in student_marks[query_name]:
        result += i
    print("%.2f" %(result / 3))
