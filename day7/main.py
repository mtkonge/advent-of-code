class File():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Dir():
    def __init__(self, name: str) -> None:
        self.name = name
        self.dir: list[Dir] = []
        self.files: list[File] = []
        self.size = 0
    def updateDir(self):
        newSize = 0
        for i in range(len(self.dir)):
            self.dir[i].updateDir()
            newSize += self.dir[i].size
        for i in range(len(self.files)):
            newSize += self.files[i].size
        self.size = newSize
    def addDir(self, name: str):
        self.dir.append(Dir(name))

    def addFile(self, file: File):
        self.files.append(file)

def testTree():
    tree = Dir("/")
    tree.dir.append(Dir("ijsd"))
    tree.dir.append(Dir("apsjf"))
    tree.dir[0].files.append(File("asd", 1))
    tree.dir[0].files.append(File("gao", 1))
    tree.dir[0].dir.append(Dir("sfj"))
    tree.dir[0].dir[0].files.append(File("sjfu", 1))
    tree.dir[1].files.append(File("asdsj", 1))
    tree.updateDir()
    if tree.size != 4:
        print(tree.size)
        raise Exception(f"Tree test failed expected tree size 4, got {tree.size}")




def main():
    testTree()
    f = open("input.txt", "r").read()
    commands = f.split("\n")
    tree = Dir("/")
    for c in commands:
        if c[0] != "$":
            pass




    




    
if __name__ == "__main__":
    main()