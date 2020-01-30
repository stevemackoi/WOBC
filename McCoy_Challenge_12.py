import sys, math


first = int(sys.argv[1])
second = int(sys.argv[2])


class Number():

    def __init__(self,x):
        self.x = x

    def is_prime(self):
        if 0 <= self.x <= 2:
            return True
        else:
            Prime = True
            for i in range(2, self.x):
                if (self.x % i) == 0:
                    Prime = False
                    break
        return Prime

    def get_divisors(self):
        factors = []
        i = 1
        while i <= self.x:
            if (self.x % i == 0):
                factors.append(i)
            i = i + 1
        return factors

    def get_gcd(self, y):
        self.y = y
        gcd = (math.gcd(self.x,y))
        return gcd

    def get_lcm(self, y):
        self.y = y
        if self.x > y:
            greater = self.x
        else:
            greater = y

        while(True):
            if((greater % self.x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater +=1
        return lcm

if __name__ == "__main__":
    number = Number(first)
    print("Prime?",number.is_prime())
    print("Factors:",number.get_divisors())
    print(f"GCD {first} and {second}:",number.get_gcd(second))
    print(f"LCM {first} and {second}:",number.get_lcm(second))
