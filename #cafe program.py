#cafe program
import time
print("**************************************************")
print("Welcome to Cloudy Cafe!")
print()
time.sleep(1)

while True:
    print("""
    Please pick an option:
    a) Food Options
    b) Snack Options
    c) Desert Options
    d) Drink options
    Q) QUIT """)

    time.sleep(1)
    opt = input("Your option is: ")

    if opt == 'a':
        print("=========================================")
        print("You hav chosen: Food Options")
        print("=========================================")

    time.sleep(1)

    print("""
    1) Fried rice with egg
    2) Spaghetti Bolognese
    3) Beef Steak
    4)Chcken Salad
    """)

    time.sleep(1)
    fopt = input("Your Food Option is: ")

    time.sleep(1)
    if fopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Fried rice and egg")
        time.sleep(1)
        print("This will cost: £4.99")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '2':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Spaghetti Bolognese")
        time.sleep(1)
        print("This will cost: £5.45")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '3':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Beef Steak")
        time.sleep(1)
        print("This will cost: £5.00")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '4':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Chicken Salad")
        time.sleep(1)
        print("This will cost: £4.90")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()


    if opt == 'b':
        print("=========================================")
        print("You hav chosen: Snack Options")
        print("=========================================")

    print("""
    1) Turke Sandwiches
    2) French Fries
    3) Crossaint
    4) Fruit Salad""")

    sopt = input("Your Snack Option is: ")