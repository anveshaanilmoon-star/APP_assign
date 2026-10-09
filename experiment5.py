# problem:LCS of X="ABCBDAB" and Y="BDCABA".
def lcs(X,Y):
    m,n=len(X), len(Y)
    dp= [[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

string1=input("Enter the First string: ")
string2=input("Enter the Second string: ")

lcs_length=lcs(string1,string2)
print(f"The length of the string is:{lcs_length}")