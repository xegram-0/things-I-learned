numbers:list = [5, 3, 2, 1, 5, 3, 3, 4, 6, 7]
"""
for number in numbers:
    print('x'*number)
for number in numbers:
    if numbers.count(number) > 1:
        print(f"{number} has duplicate")
        numbers.remove(number)
        break
print(numbers)

print(list(set(numbers)))

"""
print()
