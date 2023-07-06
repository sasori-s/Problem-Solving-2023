def findMinPlatforms(arrival, departure):
    arrival.sort()
    departure.sort()

    i=j=0

    count = 0
    platforms = 0

    while i < len(arrival):
        if arrival[i] < departure[j]:
            count += 1
            platforms = max(platforms, count)
            i += 1

        else:
            count -= 1
            j += 1

    return platforms
 
if __name__ == "__main__":
    arrival = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
    departure = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
    print("The minimum platforms needed is", findMinPlatforms(arrival, departure))
