numbers = [10, 40, 50, 70, 30, 5, 4]

min_number = min(numbers)
max_number = max(numbers)

# Output the result
print(f"Min No. {min_number}, Max No. {max_number}")



numbers = [10, 40, 50, 70, 30, 5, 4]
minimum_num = numbers[0]
max_num = numbers[0]

for n in numbers:
    if n < minimum_num:
        minimum_num = n
    if n > max_num:
        max_num = n

print("Minimum number:", minimum_num)
print("Maximum number:", max_num)