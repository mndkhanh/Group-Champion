age  = int(input("Your age  : "))
#Def
def bmi(a,b):
    c = a/(b*b)
    return c 
def bmiss(a):
    if 18.5<=a<=24.9:
        return ("Your body is normal") 
    elif 18.5> a:
        return("Your body is underweight")
    elif a ==25:
        return("Your body is overweight")
    elif 25 <a<= 29.9:
        return("Your body is Obesity money")
    elif 30<= a<= 34.9:
        return("Your body is Grade I obesity")
    elif 35<= a <=39.9:
        return("Your body is Grade II obesity")
    elif a ==40:
        return("Your body is Grade III obesity")
print("If you are an infant, you do not need to enter your height and your weight!")
#Caculator
if age <= 1:
    cnss = float(input("Birth weight (kg) : "))
    stt = int(input("Number of months old : "))
    if stt<=6:
        Infant=cnss + (stt*0.6)
        print(f"Your ideal weight is : {Infant} kg ")
    elif 7 <= stt<= 12:
        baby =cnss+3.6+(0.5*stt)
        print(f"Your ideal weight is : {baby} kg")
elif 2 <= age <=16:
    w= float(input("weight (kg): "))
    h= float(input("Height (m) : "))
    #Công thức chri số lượng cơ thể (BMI)
    bmi1 =bmi(w,h)
    print(f"Your BMI : {bmi1}")
    chil = 8+(age*2)
    print(f"Your ideal weight is : {chil} kg ")
    treem=bmiss(bmi1)
    print(treem)
elif age >16:
    w= float(input("weight (kg): "))
    h= float(input("Height (m) : "))
    #Công thức tính cân nặng lý tưởng(KG)
    cnlt=50+0.75*((h*1000)-150)
    print(f"Your ideal weight is : {cnlt} kg ")
    #Công thức chri số lượng cơ thể (BMI)
    bmi2= bmi(w,h)
    print(f"Your BMI : {bmi2}")
    nguoilon = bmiss(bmi2)
    print(nguoilon)