def main():
    arrayInput = open("input.txt", "r").read().split("\n")
    score = 0
    for game in arrayInput:
        if game[2] == "X":
            score += 1
            if game[0] == "A":
                score += 3
            if game[0] == "C":
                score += 6
        if game[2] == "Y":
            score += 2
            if game[0] == "B":
                score += 3
            if game[0] == "A":
                score += 6
        if game[2] == "Z":
            score += 3
            if game[0] == "C":
                score += 3
            if game[0] == "B":
                score += 6
    
    print("part one:\n" + str(score))
    score = 0
    for game in arrayInput:
        if game[2] == "X":
            if game[0] == "A":
                score += 3
            if game[0] == "B":
                score += 1
            if game[0] == "C":
                score += 2
        if game[2] == "Y":
            score += 3
            if game[0] == "A":
                score += 1
            if game[0] == "B":
                score += 2
            if game[0] == "C":
                score += 3
        if game[2] == "Z":
            score += 6
            if game[0] == "A":
                score += 2
            if game[0] == "B":
                score += 3
            if game[0] == "C":
                score += 1
    print("part two:\n" + str(score))
            

if __name__ == "__main__":
    main()