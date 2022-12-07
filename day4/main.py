
def main():
    f = open("input.txt", "r").read()
    pairs = f.split("\n")
    partTwo(pairs)

def partOne(pairs):
    result = 0
    for i in range(len(pairs)):
        pairs[i] = pairs[i].split(",")
        for j in range(len(pairs[i])):
            pairs[i][j] = pairs[i][j].split("-")
            for k in range(len(pairs[i][j])):
                pairs[i][j][k] = int(pairs[i][j][k])
        if pairs[i][0][0] <= pairs[i][1][0] and pairs[i][0][1] >= pairs[i][1][1] or pairs[i][0][0] >= pairs[i][1][0] and pairs[i][0][1] <= pairs[i][1][1]:
            result += 1
    print("part one:")
    print(result)

def partTwo(pairs):
    result = 0
    for i in range(len(pairs)):
        pairs[i] = pairs[i].split(",")
        for j in range(len(pairs[i])):
            pairs[i][j] = pairs[i][j].split("-")
            for k in range(len(pairs[i][j])):
                pairs[i][j][k] = int(pairs[i][j][k])
        if pairs[i][0][0] >= pairs[i][1][0] and pairs[i][0][0] <= pairs[i][1][1] or pairs[i][0][1] >= pairs[i][1][0] and pairs[i][0][1] <= pairs[i][1][1] or pairs[i][0][0] <= pairs[i][1][0] and pairs[i][0][1] >= pairs[i][1][1] or pairs[i][0][0] >= pairs[i][1][0] and pairs[i][0][1] <= pairs[i][1][1]:
            result += 1
        
    print("part two:")
    print(result)

if __name__ == "__main__":
    main()