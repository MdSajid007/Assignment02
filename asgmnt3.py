num= int(input("Enter seconds: "))
hour= num/3600
num %= 3600
minute = num/60
second= num % 60
print(str(num) + " seconds is " + str(hour) + " hours, " + str(minute) + " minutes, " + str(second) + " seconds")
