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

    print("""
    1) Fried rice with egg
    2) Spaghetti Bolognese
    3) Beef Steak
    4)Chcken Salad
    """)

    time.sleep(1)
    fopt = input("Your Food Option is: ")

    if fopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Fried rice and egg")
        print("This will cost: £4.99")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()