def findTriplets(arr, target):
    arr.sort()
    triplets = []

    for i in range(len(arr) -2):
        sum = target - arr[i]

        start = i + 1
        end = len(arr) - 1

        while start < end:
            total = arr[start] + arr[end]

            if total == sum:
                triplets.append((arr[i], arr[start], arr[end]))
                start = start + 1
                end = end - 1

            elif total < sum:
                start += 1
            
            else:
                end -= 1

    return triplets

if __name__ == "__main__":
    arr = [1, 2, -3, 4, -2, -1]
    target = 1
    print(findTriplets(arr, target))