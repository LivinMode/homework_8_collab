def reverse_ascending(numbers):
    new_num = []
    num = []
    # if not isinstance (numbers, (int)):
    #     return "invaild input"
    
    for i in numbers:
        if not num or i > num[-1]:
            num.append(i)
        else:
            new_num.extend(reversed(num))
            num = [i]
    if num:
        new_num.extend(reversed(num))
    return new_num
    
    
print(reverse_ascending([1, 2, 3, 4, 5]))