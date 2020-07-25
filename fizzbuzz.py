

def executeFizzBuzz(startValue, stopValue, divisors):
    for i in range(startValue,stopValue):
        for j in range(len(divisors)):
            if(i%divisors[j] == 0):
                if(j == 0):
                    print("fizz", end= "")
                if(j == 1):
                    print("buzz", end = "")
                print("\n")

executeFizzBuzz(0,50,[3,5])