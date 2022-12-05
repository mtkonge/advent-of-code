# velkommen til shit code centrallen

def main():
    calories = open("input.txt", "r").read()
    array = calories.split("\n")
    currentValue = 0
    newArray = []
    for v in array:
        if v == "":
            newArray.append(currentValue)
            currentValue = 0
        else: 
            currentValue += int(v)

    
    index = 0
    top3Values = []
    for v in range(3):
        for i in range(len(newArray)):
            if newArray[i] > currentValue:
                currentValue = newArray[i]
                index = i
        top3Values.append(currentValue)
        currentValue = 0
        newArray.pop(index)
    result = 0
    for v in top3Values:
        result += v
    print(result)
    

if __name__ == "__main__":
    main()