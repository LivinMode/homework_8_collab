
numnbers = [1, 3, 10, 100]
n = 4


def index_power(numnbers, n):
    if n >= len(numnbers):
        return -1
    elif n < numnbers[n]:
        result = numnbers[n] ** n
        return result
    else:
        print ("error")

print (index_power(numnbers, n))
        
     