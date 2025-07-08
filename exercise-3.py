def remove_all_after(numbers, n):
    # Check if the border number is in the list
    if n in numbers:
        # Find the position n in the list
        position = numbers.index(n)
        # return number befor n and include n as well
        result = numbers[:position + 1]
        return result
    # If border not found 
    else:
        # return the list unchanged
        return numbers
    ...
print(remove_all_after([1, 2, 3, 4, 5], 3)) 
print(remove_all_after([1, 2, 3, 4, 5], 8)) 
