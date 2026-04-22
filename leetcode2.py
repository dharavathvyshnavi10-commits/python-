platform: leetcode
problem no:9
program:
n=x
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if n==rev:
            return True
        else:
            return False
