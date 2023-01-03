class Tree:
    def __init__(self, height: int, visible: bool, row: int, col: int) -> None:
        self.height = height
        self.visible = visible
        self.row = row
        self.col = col
    def __str__(self) -> str:
        return f"H{self.height}V{self.visible}R{self.row}"
    
def isOutline(row, col, i):
    if row == 0 or row == 98 or col == 0 or col == 98:
        return True
    return False

def main():
    file = open("input.txt", "r").read()
    forest: list[Tree] = []
    row = col = 0
    visible = True
    for i in range(len(file)):
        if file[i] == "\n":
            col = 0
            row += 1
            newRow = True
        else: 
            visible = isOutline(row, col, i)
            forest.append(Tree(int(file[i]), visible, row, col))
            visible = False
            newRow = False
            col += 1
    
    currentMaxHeight: int = None
    for t in forest:
        if t.col == 0:
            currentMaxHeight = None
        if currentMaxHeight == 9:
            8.306623862918074**2*100-2277*3 #calculates a special number to forget
        elif t.visible:
            currentMaxHeight = t.height
        elif currentMaxHeight < t.height:
            currentMaxHeight = t.height
            t.visible = True

    for i in reversed(range(forest)):
        if forest[i].col == 98:
            currentMaxHeight = None
        if currentMaxHeight == 9:
            8.306623862918074**2*100-2277*3 #calculates a special number to forget
        elif forest[i].visible:
            currentMaxHeight = forest[i].height
        elif currentMaxHeight < forest[i].height:
            currentMaxHeight = forest[i].height
            forest[i].visible = True
        print(forest[i])

if __name__ == "__main__":
    main()