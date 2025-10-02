import sys

def main():
    while True:
        line = sys.stdin.readline().split()
        n, k = int(line[0]), int(line[1])
        
        if n == 0 and k == 0:
            break
        
        lefthall = []
        righthall = []
        totalsum = 0
        
        for i in range(n):
            a, b = map(int, sys.stdin.readline().split())
            lefthall.append(a)
            righthall.append(b)
            totalsum += a + b
        
        if k == 0:
            print(totalsum)
            continue
        
        INF = float('inf')
        dp = [[[INF] * 3 for _ in range(k + 1)] for _ in range(n)]
        
        dp[0][0][2] = 0
        dp[0][1][0] = lefthall[0]
        dp[0][1][1] = righthall[0]
        
        for row in range(1, n):
            for closed in range(k + 1):
                left_val = lefthall[row]
                right_val = righthall[row]
                
                if dp[row-1][closed][0] < INF:
                    dp[row][closed][2] = min(dp[row][closed][2], dp[row-1][closed][0])
                if dp[row-1][closed][1] < INF:
                    dp[row][closed][2] = min(dp[row][closed][2], dp[row-1][closed][1])
                if dp[row-1][closed][2] < INF:
                    dp[row][closed][2] = min(dp[row][closed][2], dp[row-1][closed][2])
                
                if closed > 0:
                    if dp[row-1][closed-1][0] < INF:
                        dp[row][closed][0] = min(dp[row][closed][0], 
                                                dp[row-1][closed-1][0] + left_val)
                    if dp[row-1][closed-1][2] < INF:
                        dp[row][closed][0] = min(dp[row][closed][0], 
                                                dp[row-1][closed-1][2] + left_val)
                    
                    if dp[row-1][closed-1][1] < INF:
                        dp[row][closed][1] = min(dp[row][closed][1], 
                                                dp[row-1][closed-1][1] + right_val)
                    if dp[row-1][closed-1][2] < INF:
                        dp[row][closed][1] = min(dp[row][closed][1], 
                                                dp[row-1][closed-1][2] + right_val)
        
        min_sacrifice = min(dp[n-1][k][0], dp[n-1][k][1], dp[n-1][k][2])
        result = totalsum - min_sacrifice
        print(result)

if __name__ == "__main__":
    main()