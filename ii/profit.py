def maxprofit(a):
    bought = -1
    profit = 0
    for i in range(len(a)):  
        if i == len(a)-1 or a[i+1] < a[i]:
            if bought >= 0:
                profit += a[i] - a[bought]
                bought = -1
        elif a[i] < a[i+1]:
            if bought == -1:
                bought = i

    return profit

if __name__ == '__main__':
    a = [1, 5, 2, 3, 7, 6, 4, 5]
    print("Maxprofit = ", maxprofit(a)) 
