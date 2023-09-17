class Data:
    def __init__(self, value=None, index=None, count=0):
        self.value = value
        self.index = index
        self.count = count

    

def sortByFrequency(A):
    if A is None or len(A) < 2:
        return 

    hm = {}

    for i in range(len(A)):
        hm.setdefault(A[i], Data(A[i], i)).count += 1

    values = [*hm.values()]

    values.sort(key=lambda x: (-x.count, x.index))

    k = 0

    for data in values:
        for j in range(data.count):
            A[k] = data.value 
            k += 1




if __name__ == '__main__':
    A = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
    sortByFrequency(A)
    print(A)