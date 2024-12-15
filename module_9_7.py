from math import sqrt
def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        prime = True
        i = 2
        while i <= sqrt(result):
            if result % i == 0:
                prime = False
                break
            i = i + 1
        if prime:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

def sum_three(a =0, b = 0, c =0):
     return a + b +c

sum_three_dec =  is_prime(sum_three)

result= sum_three_dec(2,3, 6)
print(result)
