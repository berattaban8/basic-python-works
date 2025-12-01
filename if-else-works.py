exam1 = int(input("exam1's result: "))
exam2 = int(input("exam2's result: "))
exam3 = int(input("exam3's result: "))
exam4 = int(input("exam4's result: "))

total = (exam1 + exam2 + exam3 + exam4) / 4 

#  00 - 24  ==> very bad
#  25 - 49  ==> bad
#  50 - 74  ==> medium
#  75 - 100 ==> good

if (total) <= 24:
    print("Your result is very bad")

elif (total) <= 49:
    print("Your result is bad")

elif (total) <= 74:
    print("Your result is medium")

elif (total) <= 100:
    print("Your result is good")

else:
    print("Your result could not be calculated")

print(f"Here is your result: {total}")