

MOD = 1_000_000_007
n = 7  #
dp = [0]*(n+1); dp[0]=1
for s in range(1,n+1):
    for cara in range(1,7):
        if s >= cara:
            dp[s] = (dp[s]+dp[s-cara])%MOD
            
