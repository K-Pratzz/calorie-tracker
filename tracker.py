''' 
Name : Kumari Pratibha
Roll Number : 2501010123
Section A B.Tech CSE Core
Date : 03/10/2025
kk
Project Title : Daily Calorie Tracker
'''
print("This Project takes daily calorie intake as input, compares it with specified limit and stores it in a txt file")
num=int(input("Enter the number of meals : "))
mealList=[]
calorieList = []
for i in range(num):
    mealName = input("Enter the name of the meal : ")
    calorieAmount = int(input("Enter the Calorie Amount for this meal : "))
    mealList.append(mealName)
    calorieList.append(calorieAmount)
total=0
for m in calorieList:
    total+=m
avg=total/num
calorieLimit = int(input("Enter your daily Calorie limit : "))
if calorieLimit>=avg:
    print("Calorie Limit maintained Successfully")
else:
    print("💀 WARNING : Calorie Limit has been Crossed")
print("Meal Name               Calories")
print("--------------------------------")
for meal,calorie in zip(mealList,calorieList):
    print(f"{meal:<23}{calorie}")
print(f'Average : {avg}')
save=input("type y if you wanna save it in the txt file : ")
if save=='y':
    with open("tracker.txt","w") as file:
        file.write("mealName              calories \n")
        for meal,calorie in zip(mealList,calorieList):
            file.write(f"{meal:<23}{calorie}\n")
print("good")

    #writer=csv.writer(file)
    #writer.writerows(mealList,calorieList)




    
    