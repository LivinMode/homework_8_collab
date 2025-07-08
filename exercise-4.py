

def chunking_by(numbers, chunck):
    resulte = []
    for i in range (0,len(numbers), chunck):
        new_data = numbers[i:i + chunck]
        resulte.append(new_data)


    return resulte


print(chunking_by([2, 3, 4, 5, 6, 6, 8, 7, 9], 3))
