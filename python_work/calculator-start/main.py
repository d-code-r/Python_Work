import art


def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2    

symbol = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(art.logo)  
  num_1 = float(input("enter the number "))
  start = True
  while start:
    for i in symbol:
      print(i)
    answer = 0  
    oprator = input("choose oprator: ")  
    num_2 = float(input("enter the number "))
    if oprator == "+":
      answer = add(num_1, num_2)
    if oprator == "-":
      answer = substract(num_1, num_2)
    if oprator == "*":
      answer = multiply(num_1, num_2)
    if oprator == "/":
      answer = divide(num_1, num_2)    
    print(f"{num_1} {oprator} {num_2} = {answer}")
    again = input(f"enter 'y' to calculate again {answer} and 'no' to stop: ")
    if again == "y":
      num_1 = answer
    else:
      start = False
      calculator()

calculator()


