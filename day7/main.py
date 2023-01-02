import copy

class File():
    def __init__(self, size: int, name: str) -> None:
        self.name: str = name
        self.size: int = size

class Dir():
    def __init__(self, name: str, parent: str) -> None:
        self.name: str = name
        self.parent: str = parent
        self.dirs: list[Dir] = []
        self.files: list[File] = []
        self.size: int = 0

    def __str__(self, level=0):
        result = "\t"*level+repr(self.name)+"\n"
        for d in self.dirs:
            result += d.__str__(level+1)
        return result
    
    def __repr__(self) -> str:
        return '<Tree representation>' 

    def updateDirs(self):
        updatedSize = 0
        for i in range(len(self.dirs)):
            self.dirs[i].updateDirs()
            updatedSize += self.dirs[i].size
        for i in range(len(self.files)):
            updatedSize += self.files[i].size
        self.size = updatedSize
    
    def addDir(self, name):
        self.dirs.append(Dir(name, self.name))

    def addFile(self, file: File):
        self.files.append(file)
    
    def addDirWithValues(self, dirs):
        self.dirs.append(dirs)

    def find(self, name: str):
        if name == "":
            return self
        if self.name == name:
            return self
        for i in range(len(self.dirs)):
            if self.dirs[i].name == name:
                return self.dirs[i]
            return self.dirs[i].find(name)
        raise Exception(f"Could not find dir of name {name}")

def testTree():
    tree = Dir("/", "")
    tree.addDir("ijsd")
    tree.addDir("apsjf")
    tree.dirs[0].addFile(File(1, "asd"))
    tree.dirs[0].addFile(File(1, "gao"))
    tree.dirs[0].addDir("sfj")
    tree.dirs[0].dirs[0].addFile(File(1, "sjfu"))
    tree.dirs[1].addFile(File(1, "asdsj"))
    tree.updateDirs()
    if tree.size != 4:
        raise Exception(f"Tree test failed expected tree size 4, got {tree.size}")

def main():
    testTree()
    f = open("input.txt", "r").read()
    commands = f.split("\n")
    tree = Dir("/", "")
    currentDir = copy.deepcopy(tree)
    totalSizeUnder100000 = 0
    currentSize = 0
    for c in commands:
        print(c)
        c = c.split(" ")
        if c[-1] == "/":
            continue
        if c[0] != "$":
            if c[0] == "dir":
                currentDir.addDir(c[1])
            else:
                size = int(c[0])
                currentSize += size 
                currentDir.addFile(File(size, c[1]))
        elif c[1] == "cd":
            if currentSize <= 100000:
                totalSizeUnder100000 += currentSize
            currentSize = 0
            if c[2] == "..":
                raise Exception("Not implemented")

            else:
                for d in currentDir.dirs:
                    if d.name == c[2]:
                        currentDir = d
                raise Exception("Not implemented")
    print(totalSizeUnder100000)

                





    




    
if __name__ == "__main__":
    main()