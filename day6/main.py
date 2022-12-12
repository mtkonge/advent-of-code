def main():
    dataStreamBuffer = open("input.txt", "r").read()
    currentSignal = ""
    processedChars = 0
    for v in dataStreamBuffer:
        if len(currentSignal) > 14:
            print(currentSignal)
            raise Exception("currentSignal overflow")
        if len(currentSignal) == 14:
            signalBefore = currentSignal
            currentSignal = checkForDuplicates(currentSignal)
            if signalBefore == currentSignal:
                print(currentSignal)
                print(processedChars)
                raise Exception("Done")
            processedChars += 1
            currentSignal += v
            continue
        processedChars += 1
        currentSignal += v
        
def checkForDuplicates(currentSignal):
    for i in range(len(currentSignal)):
        for j in range(14):
            if j == i:
                continue
            if currentSignal[i] == currentSignal[j]:
                currentSignal = currentSignal[1:14]
                return currentSignal
    return currentSignal
                

if __name__ == "__main__":
    main()