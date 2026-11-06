num = 2
ser = int(input("Enter the series number: "))
total = 0
current_value = ''
series = ''

for i in range(1, ser + 1):
    current_value += str(num)
    term_value = int(current_value)
    total += term_value
    if i == 1:
        series += current_value
    else:
        series += ' + ' + current_value


print(f"{series} = {total}")
