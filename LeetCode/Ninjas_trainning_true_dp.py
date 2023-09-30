def findTrainning(points, n):
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0

            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(activity, dp[day][last])

    return dp[n - 1][3]  


if __name__ == '__main__':
    points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
    ]

    n = len(points)

    dp = [[0 for _ in range(4)] for _ in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][0] = max(points[0][0],points[0][1], points[0][2])


    print(findTrainning(points, n))