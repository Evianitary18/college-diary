val = [60,  100, 120]
wt = [3, 4, 4]
W= 8
n = len (val)

memo = [[-1 for i in range (W + 1)] for j in range (n + 1)]

def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    elif memo[n][W] != -1:
        return memo [n][W]
    
    elif wt [n-1] <= W:
        memo[n][W] = max (
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1), 
            knapsack (wt, val, W, n-1))
        return memo [n][W]
    elif wt[n-1] > W :
        memo [n][W] = knapsack (wt, val, W, n-1)
        return memo[n][W]
    
print(knapsack(wt, val, W, n))

