
def rectangle(a, b):
  if isinstance(a,(int,float)) and isinstance(b,(int,float)):
    return a *b
  else:
    raise ValueError("Sides must be int/float type")


def triangle(a, h):
  return 0.5 * a * h

def trapezoid(a,b,h):
  return 0.5 * ((a+b) * h)

def main():
  side_A = 5
  side_B = 5

  area_r = rectangle(side_A, side_B)
  area_t = triangle(side_A, side_B)

  print(area_r == 30)
  print(area_t == 15)

if __name__ == '__main__':
  main()