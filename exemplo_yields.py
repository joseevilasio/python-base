def other_math(number):
  print('do the math with:', number)
  
def gen_squares_in_interval(x, y):
  for i in range(x, y):
    yield i*i

if __name__ == '__main__':

  x, y = (10, 20)
  
  for number in gen_squares_in_interval(x, y):
    other_math(number)



def other_math(number):
  print('do the math with:', number)
  
def gen_squares_in_interval(x, y):
  for i in range(x, y):
    return i*i

if __name__ == '__main__':

  x, y = (10, 20)
  
  for _ in range(x, y):
    number = gen_squares_in_interval(x, y)
    other_math(number)
