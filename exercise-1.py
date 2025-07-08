def replace_last(numbers):
        # If the list has 0 or 1 numbers, return it as is
    if len(numbers) <= 1:
        return numbers
    # Take the last numbers and add the rest of the list (except last)
    return [numbers[-1]] + numbers[:-1]
    ...
print(replace_last([2, 3, 4, 1]))