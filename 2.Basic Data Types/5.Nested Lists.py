if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])
        
    score = []
    for i in students:
        score.append(i[1])
    score = sorted(list(set(score)))
    
    name = []
    for i in students:
        if i[1] == score[1]:
            name.append(i[0])
    
    for i in sorted(name):
        print(i)