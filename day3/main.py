def main():
    backpacks = open("input.txt", "r").read().split("\n")
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()
    for i in range(len(backpacks)):
        x = backpacks[i][0:int(len(backpacks[i])/2)]
        y = backpacks[i][int(len(backpacks[i])/2):len(backpacks[i])]
        backpacks[i] = [x, y]
    duplicates = ""


    for bp in backpacks:
        for i in range(len(bp[0])):
            for j in range(len(bp[1])):
                print(bp[0])
                print(bp[1])

                if bp[0][i] == bp[1][j]:
                    duplicates += bp[0][i]
                    bp[0] = bp[0][:i] + bp[0][i+1:]
                    bp[1] = bp[1][:j] + bp[1][j+1:]
                    j -= 1
                    i -= 1
                
        
    print(duplicates)
if __name__ == "__main__":
    main()