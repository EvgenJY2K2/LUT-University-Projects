h = float(input("Enter your height (cm):\n"))
w = float(input("Enter your weight (kg):\n"))

i = (w/(h)**2)*10000

if i < 18.5:
    print("The mass index is %s (underweight)"%round(i, 1))
elif 18.5 <= i <25:
    print("The mass index is %s (healthy weight)"%round(i, 1))
elif 25 <= i <30:
    print("The mass index is %s (overweight)"%round(i, 1))
else:
    print("The mass index is %s (obesity)"%round(i, 1))
