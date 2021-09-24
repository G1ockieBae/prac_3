MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Cebroken_scorelsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice!="Q":
        if choice =="C":
            Celsius = float(input("print celsius:"))
            Fahrenheit = get_Fahrenheit(Celsius)
            print("Result:{:,.2f} F".format(Fahrenheit))
        elif choice=="F":
            Fahrenheit = float(input("print Fahrenheit:"))
            Celsius= get_Celsius(Fahrenheit)
            print("Result:{:,.2f} C". format(Celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(" >>> ").upper()
    print("Thats all")
""" 将摄氏度华氏度相互转换"""
def get_Fahrenheit(Celsius):
    Fahrenheit=Celsius * 9.0 / 5 + 32
    return Fahrenheit
def get_Celsius(Fahrenheit):
    Celsius = 5.0 / 9 * (Fahrenheit - 32)
    return Celsius
main()
