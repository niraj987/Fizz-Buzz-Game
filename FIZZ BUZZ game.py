user_choice = int(input("Enter user number: "))
for number in range(1,user_choice + 1):
    if number % 3 ==0 and number % 5 ==0:
        print("FIZZ BUZZ !!!!!!!!!!!")
    elif number % 3==0:
        print("FIZZ !!!!")
    elif number % 5 ==0:
        print("BUZZ !!!")
    else:
        print(number)
