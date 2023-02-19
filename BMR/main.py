#body composition
#bmr = 370 + (21.6 * lean body mass (kg))
#lean body mass = (weight(kg) * (100 - (body fat)))

#body fat percentage 

#men = 10 * weight(kg) + 6.25 * height (cm) - 5 * age + 5
#women = 10 * weight(kg) + 6.25 * height (cm) - 5 * age - 161


weight = int(input("what is your weight? "))
kg = weight * 0.453592
print(kg)

feet = int(input("What is your height in feet? "))
inches = int(input("What is your remaining height in inches "))
x = (feet * 12) + inches
cm = x * 2.54
print(f"Your height in inches is {x}")
print(cm)


age = int(input("What is your age? "))

bmr = 10 * kg + 6.25 * cm - 5 * age + 5

print(bmr)
