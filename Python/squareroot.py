class SquareRoot():
        
    def get_squareroot(self, n: int) -> int:
        i = 1
        while i*i < n:
            i += 1
        
        # hit the squareroot exactly
        if i*i == n:
            return i
        
        # checks which number i or i-1 is closer to 0 when we subtract the given number
        # return the closer number
        if abs(i * i - n) < abs((i - 1) * (i - 1) - n):
            return i
        else:
            return i-1
            
s = SquareRoot()
print(s.get_squareroot(69))