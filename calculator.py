import os

def add(a,b):
    return (a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)

operations_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
    }
def calculator():
    
  num1=float(input("ENTER FIRST NUMBER:"))

  for symbol in operations_dict:
    print(symbol)

  continue_flag=True
  while(continue_flag):
   op_symbol=input("PICK AN OPERATION:")

   num2=float(input("ENTER NEXT NUMBER:"))

   calc_fun=operations_dict[op_symbol]
   output=calc_fun(num1,num2)
   print(f"{num1} {op_symbol} {num2}= {output}")

   should_continue=input(f"ENTER 'Y' to continue calculation with {output} or 'n' to start a new calculation 'x' to exit").lower()
   if should_continue=='y':
    num1=output

   elif should_continue=='n':
     continue_flag=False
     os.system("cls")
     calculator()
   else:
    continue_flag=False

calculator()    
















