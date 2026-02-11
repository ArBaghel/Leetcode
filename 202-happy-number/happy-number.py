class Solution:
    def isHappy(self, n: int) -> bool:
        if (n==1 or n==7):
            return True
        elif (n<10):
            return False
        else:
            sum=0
            while (n>0):
                digit=n%10
                sum+=digit*digit
                n//=10
            return self.isHappy(sum)
        

        