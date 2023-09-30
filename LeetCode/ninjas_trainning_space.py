def findTrainning(points, n, prev):
    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            temp[last] = 0

            for task in range(3):
                if task != last:
                    activity = points[day][task] + prev[task]
                    temp[last] = max(activity, temp[last])

        prev = temp
    return prev[3]  


if __name__ == '__main__':
    points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
    ]

    n = len(points)

    prev = [0 for _ in range(4)] 
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0],points[0][1], points[0][2])


    print(findTrainning(points, n, prev))