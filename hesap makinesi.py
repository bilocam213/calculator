def toplama (x,y):
    return x+y
def cikarma (x,y):
    return x-y
def carpma (x,y):
    return x*y
def bolme(x,y):
    return x/y

print("SEÇİM İŞLEMİ")
print("1.TOPLAMA")
print("2.ÇIKARMA")
print("3.ÇARPMA")
print("4.BÖLME")

while True:
    choice = input("ENTER choice (1/2/3/4):")

    if choice in('1','2','3','4'):
        try:
            num1=float(input("ENTER FİRST NUNMBER"))
            num2=float(input("ENTER SECOND NUMBER"))
        except ValueError:
            print("invalid input.Please enter a number.")
            continue
        if choice=='1':
            print(num1,"+",num2,"=", toplama(num1,num2))
        elif choice=='2':
            print(num1, "-", num2, "=", cikarma(num1, num2))
        elif choice=='3':
             print(num1, "*", num2, "=", carpma(num1, num2))
        elif choice=='4':
             print(num1, "/", num2, "=", bolme(num1, num2))   
    else:
        print("Invalid Input")