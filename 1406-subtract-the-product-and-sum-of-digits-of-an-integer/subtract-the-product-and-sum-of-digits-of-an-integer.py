class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum=0
        temp=n
        while temp>0:
            digit=temp%10
            sum+=digit
            prod*=digit
            temp//=10
        return prod-sum
        