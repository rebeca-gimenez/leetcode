"""
1672. Richest Customer Wealth
You are given an m x n integer grid accounts where accounts[i][j] is the 
amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank 
accounts. The richest customer is the customer that has the maximum wealth.

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
"""
def maximumWealth(accounts):
    #row =customer, column = bank
    wealth = []
    for row in accounts:
        sum = 0
        for cell in row:
            sum += cell
        wealth.append(sum)
    return max(wealth)
            
accounts = [[1,2,3],[3,2,1]]
output = 6
print(maximumWealth(accounts), output)
accounts = [[1,5],[7,3],[3,5]]
output = 10
print(maximumWealth(accounts), output)
accounts = [[2,8,7],[7,1,3],[1,9,5]]
output = 17
print(maximumWealth(accounts), output)