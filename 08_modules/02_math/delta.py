from math import isqrt

def get_delta(a,b,c):
    delta = b**2 - 4*(a*c)
    return delta

def get_roots(a,b,delta):
    x1 = (isqrt(delta) - b)/2*a
    x2 = (isqrt(delta) + b)/2*a
    if x1 > x2:
        return  x1, x2
    else:
        return x2,  x1

def get_difference(x1,x2):
    suma =0
    if x1 < 0 and x2 < 0:
        suma = -(x1 +x2)
        print(suma)
        return float(suma)
    elif x1 < 0 and x2 > 0:
        suma = -x1 + x2
        print(suma)
        return float(suma)
    elif x1 > 0 and x2 > 0:
        suma = x1 + x2
        print(suma)
        return float(suma)



#def get_visualization(x1, x2, difference):
#    diff = ("-"*difference)
#    print(f"--{x1}{difference}{x2}--")
#    print(difference).center("--"+x1+"-"*difference+x2+"--")

def main():
    a = int(input("Input first variable: "))
    b = int(input("Input second variable: "))
    c = int(input("Input last variable: "))
    delta = get_delta(a,b,c)
    if delta > 0:
        x1, x2 = get_roots(a,b,delta)
  #      diff = get_difference(x1, x2)
 #       get_visualization(x1,x2,diff)
        print(F"Delta is equal to {delta}")
    else:
        print("Delta is less than zero and equal to ")

main()