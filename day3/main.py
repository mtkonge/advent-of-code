def main():
    backpacks = open("input.txt", "r").read().split("\n")
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()
    partTwo(backpacks, characters)


def partTwo(backpacks, characters, i = 0):
    badges = ""
    for i in range(len(backpacks)):
        if i == 0:
            i += 1
            continue
        elif not (i % 3):
            currentDuplicates = ""
            for v in backpacks[i-2]:
                for s in backpacks[i-1]:
                    if v == s:
                        if len(currentDuplicates) == 0:
                            currentDuplicates += v
                        for i in range(len(currentDuplicates)):
                            if currentDuplicates[i] == v:
                                break;
                            elif i == len(currentDuplicates)-1:
                                currentDuplicates += v
            for c in currentDuplicates:
                for d in backpacks[i]:
                    if c == d:
                        badges += c
                        break
    result = 0
    for v in badges:
        result += characters.index(v)+1
    print("part two:")
    print(result)
    print("not completed")

def partOne(backpacks, characters):
    for i in range(len(backpacks)):
        x = backpacks[i][0:int(len(backpacks[i])/2)]
        y = backpacks[i][int(len(backpacks[i])/2):len(backpacks[i])]
        backpacks[i] = [x, y]
    duplicates = itemsToRearrange(backpacks)
    result = 0
    for v in duplicates:
        result += characters.index(v)+1
    print("part one:")
    print(result)

def itemsToRearrange(backpacks, dups = ""):
    for bp in backpacks:
        for i in range(len(bp[0])):
            for j in range(len(bp[1])):
                
                if bp[0][i] == bp[1][j]:
                    dups += bp[0][i]
                    bp[0] = bp[0].replace(bp[0][i], "")
                    # lappeløsning centralen:
                    # har brugt to timer på at fikse index out of range issue, please have mercy c++ dev
                    return itemsToRearrange(backpacks, dups)
    return dups



if __name__ == "__main__":
    main()