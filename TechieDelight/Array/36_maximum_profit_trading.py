def findMaxProfit(price):
    profit = 0
    j = 0

    for i in range(1, len(price)):
        if price[i - 1] > price[i]:
            j = i

        if price[i - 1] <= price[i] and \
            (len(price) == i + 1 or price[i] > price[i + 1]):
            profit += price[i] - price[j]
            print(f"Buy on the day of {j + 1} and sell on day {i + 1}")

    return profit

if __name__ == "__main__":
    price = [1, 5, 2, 3, 7, 6, 4, 5]
    print("\nToal profit earned is ", findMaxProfit(price))