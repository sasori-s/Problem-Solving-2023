def totalTrappedWater(buildings):
    left = [0] * len(buildings) 
    right = [0] * len(buildings) 
    n = len(buildings)
    water = 0

    left[0] = buildings[0]

    for i in range(1, n):
        left[i] = max(left[i - 1], buildings[i])

    right[n - 1] = buildings[n - 1]

    for i in reversed(range(n - 1)):
        right[i] = max(right[i + 1], buildings[i])

    for i in range(n):
        water += min(right[i], left[i]) - buildings[i]

    print(f'Total number of water can be trapped is {water}')



if __name__ == '__main__':
    buildings = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]

    totalTrappedWater(buildings)