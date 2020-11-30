try:
    num1=int(input())
    num2= int(input())
    marks = num1/num2
    print(marks)
    print(stud_name,marks)

except NameError as ne:
    print("name error is caused ",ne)
except Exception as e:
    print(e)