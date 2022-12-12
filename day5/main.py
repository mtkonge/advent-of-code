
def main():
    f = open("crates.txt", "r").read()
    messyCrates = f.split("\n")
    crates = [[],[],[],[],[],[],[],[],[]]
    for i in range(len(messyCrates)):
        for j in range(len(messyCrates[i])):
            if messyCrates[i][j] == " ":
                continue
            if j == 1:
                crates[0].append(messyCrates[i][j])
            elif j == 5:
                crates[1].append(messyCrates[i][j])
            elif j == 9:
                crates[2].append(messyCrates[i][j])
            elif j == 13:
                crates[3].append(messyCrates[i][j])
            elif j == 17:
                crates[4].append(messyCrates[i][j])
            elif j == 21:
                crates[5].append(messyCrates[i][j])
            elif j == 25:
                crates[6].append(messyCrates[i][j])
            elif j == 29:
                crates[7].append(messyCrates[i][j])
            elif j == 33:
                crates[8].append(messyCrates[i][j])  
    

    f = open("instructions.txt", "r").read()
    instructions = f.split("\n")
    for i in range(len(instructions)):
        instructions[i] = sanitizeInstruction(instructions[i])
        for j in range(len(instructions[i])):
            instructions[i][j] = int(instructions[i][j])
        crates = doInstructions(crates, instructions, i)
    print(instructions)
    result = ""
    print(crates)
    for v in crates:
        result += v[0]

    print(result)
    
def sanitizeInstruction(instruction):
    return instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")

def doInstructions(crates, instructions, i):
    print(instructions[i][1]-1)
    print(instructions[i][2]-1)
    print(crates[instructions[i][2]-1])
    print(crates[instructions[i][1]-1])
    stackToMove = []
    for v in range(instructions[i][0]):
        stackToMove.insert(0, crates[instructions[i][1]-1][0])
        crates[instructions[i][1]-1].pop(0)
    for v in range(instructions[i][0]):
        crates[instructions[i][2]-1].insert(0, stackToMove[v])
    return crates

if __name__ == "__main__":
    main()