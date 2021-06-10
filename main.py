import math

# The input option for the command line is included here

# num1 = int(input("Please enter a start value: "))
# num2 = int(input("Please enter a stop value: "))
# ranges = [num1,num2]
# ranges.sort()

# Since the testing requirements specify the range is to be 7900 - 7020
# The had coded value is included here
# It would be very inefficient to automate a test requiring manual input

# This order verifies the range
ranges = [7920,7900]
ranges.sort()

start = ranges[0]
end = ranges[1]


def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def generate(start, end):
  primes = []
  for i in range(start, end+1):
    if isPrime(i):
      primes+=[i]
  return primes

def return_primes():
  print(generate(start,end))
  return generate(start,end)

return_primes()

# The assert here is hard coded because the test specifies the input ranges
# And the expected results
assert return_primes() == [7901, 7907, 7919]

