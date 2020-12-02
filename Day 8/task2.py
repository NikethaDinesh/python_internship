def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
   try:
    c=a/b
    print(c)
   except Exception as e:
       print("Exception caused:",e)


def enterinput():
    try:
        num1=int(input())
        num2=int(input())
        operator=input()
        if operator=='+':
           add(num1,num2)
        elif operator=='-':
            sub(num1,num2)
        elif operator == '*':
          mul(num1, num2)
        elif operator == '/':
             div(num1, num2)
        else:
              print("wrong input")
              enterinput()
    except Exception as e:
        print("Exception raised :",e)
    finally:
        enterinput()
enterinput()

