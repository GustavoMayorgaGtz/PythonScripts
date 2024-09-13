if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    records = student_marks.get(query_name)
    base = len(records)
    suma = 0
    for record in records:
        suma += record
    promedio = suma/base
    print("{:.2f}".format(promedio))