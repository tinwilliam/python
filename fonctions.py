# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# Write your square_root function here:
def square_root(num):
  return num**0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Write your tip function here:
def tip(percentage,total):
  return total*percentage/100
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# Write your win_percentage function here:
def win_percentage(wins,losses):
  return wins/(wins+losses)*100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Write your dog_years function here:
def dog_years(name, age):
  return name+", you are "+str(age*7)+" years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# Write your remainder function here:
def remainder(num1,num2):
  return 2*num1%(num2/2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)
  print(second)
  print(third)
  return fourth

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

