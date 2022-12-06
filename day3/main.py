def main():
    backpacks = open("input.txt", "r").read().split("\n")
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()
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