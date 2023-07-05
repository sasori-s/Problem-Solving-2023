import sys

def trap(bars):
    n = len(bars)

    if n <= 2:
        return 0
    
    water = 0

    left = [None] * (n - 1)
    left[0] = -sys.maxsize

    for i in range(1, n - 1):
        left[i] = max(left[i - 1], bars[i - 1])

    right = -sys.maxsize

    for i in reversed(range(1, n - 1)):
        right = max(right, bars[i+1])

        if min(left[i], right) > bars[i]:
            water += min(left[i], right) - bars[i]

    return water


if __name__ == "__main__":
    heights = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
    print("THe maximum amount of water than can be trapped is, ", trap(heights))