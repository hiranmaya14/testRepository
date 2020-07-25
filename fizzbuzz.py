

def executeFizzBuzz(startValue, stopValue, divisors):
    for i in range(startValue,stopValue):
        for j in range(len(divisors)):
            if(i%divisors[j] == 0):
                if(j == 0):
                    print("fizz", end= "")
                if(j == 1):
                    print("buzz", end = "")
                print("\n")

def findMaxOfTwoNumbers(num1, num2):
    if(num1> num2):
        return num1
    else:
        return num2

def findMinOfTwoNumbers(num1,num2):
    if(num1 < num2):
        return num1
    else:
        return num2

a = 10
b = 20
print(findMaxOfTwoNumbers(a,b))

