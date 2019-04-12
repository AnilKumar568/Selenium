marks = {}
for _ in range(int(input())):
    line = input().split()
    print(line)
    marks[line[0]] = list(map(float, line[1:]))
    print(marks)
print('%.2f' % (sum(marks[input()]) / 3))