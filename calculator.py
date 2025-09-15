def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def modulus(x, y):
  return x % y

print("------------------------------------------------------")
print("\tWelcome to the Simple Calculator!")
print("------------------------------------------------------")

while True:
  print("\nSelect operation:")
  print("1. Add (+)")
  print("2. Subtract (-)")
  print("3. Multiply (*)")
  print("4. Divide (/)")
  print("5. Modulus (%)")
  print("6. Exit")

  choice = input("\nEnter choice (1/2/3/4/5/6): ")

  if choice in ('1', '2', '3', '4', '5'):
    try:
      num1 = float(input("\nEnter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numeric values.")
      continue 

    if choice == '1':
      print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
      print("------------------------------------------------------")

    elif choice == '2':
      print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
      print("------------------------------------------------------")

    elif choice == '3':
      print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
      print("------------------------------------------------------")

    elif choice == '4':
      if num2 == 0:
        print("\nError! Division by zero is not allowed.")
        print("------------------------------------------------------")
      else:
        print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
        print("------------------------------------------------------")

    elif choice == '5':
        if num2 == 0:
            print("\nError! Modulus by zero is not allowed.")
            print("------------------------------------------------------")
        else:
            print(f"\nResult: {num1} % {num2} = {modulus(num1, num2)}")
            print("------------------------------------------------------")
            
  elif choice == '6':
    print("\nExiting calculator. Goodbye! 👋")
    print("------------------------------------------------------")
    break 

  else:
    print("\nInvalid choice. Please select a valid option.")
    print("------------------------------------------------------")