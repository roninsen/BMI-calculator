
def printMessage(name, bmi):
    if bmi > 25:
        print(name," is overweight and his BMI is", bmi)
        
    if bmi < 18.5:
        print(name, " is underweight and his BMI is", bmi)

    if 18.5 < bmi < 25:
        print(name, " is normal weight and his BMI is", bmi)
    

def calculateBMI(height, weight):
    return 703*weight/(height*height)

data_file = open("data.txt", "r")
for line in data_file:
    splitLine = line.split(",")
    bmi = calculateBMI(int(splitLine[1]), int(splitLine[2]))
    printMessage(splitLine[0],bmi)
data_file.close()


    







