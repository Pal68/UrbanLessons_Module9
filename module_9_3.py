first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
s = zip(first, second)
first_result = (len(s[0]) - len(s[1]) for s in zip(first, second) if len(s[0]) != len(s[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))

print(list(first_result))
print(list(second_result)) 