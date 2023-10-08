def findRooms(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    count, result = 0, 0

    s, e = 0, 0

    while s < len(start):
        if start[s] < end[e]:
            count += 1
            s += 1

        else:
            count -= 1
            e += 1

        result = max(count, result) 

    return result



if __name__ == '__main__':
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(findRooms(intervals))