def myFactorial_Calculater(n):
  """This is a factorial calculater using Iterative Approach"""
  fac = 1
  for i in range(n):
    fac = fac * (i+1)
  return (fac)

number = int(input("Enter your number:\n"))
k = myFactorial_Calculater(number)
print("Your answer : "+str(k))
K = input("Press Enter to exit")
print(K)