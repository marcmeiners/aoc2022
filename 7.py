class Node:
    # children is a dictionary containing the names of files & folders 
    # in the key-set and the corresponding nodes in the value-set
    def __init__(self, value, parent, children = {}):
        self.value = value
        self.children = children
        self.parent = parent

root = Node(0, None, {})

def treeInit():
    with open("input/7.txt", "r") as f:
        curr = root
        for x in f.readlines():
            if '\n' in x:
                    x = x[:-1]
            parts = x.split(' ')

            # command
            if(x[0] == '$'):
                if x[2] == 'c':
                    cd = parts[-1]
                    if cd == '/':
                        curr = root
                    elif cd == '..':
                        curr = curr.parent
                    else:
                        curr = curr.children.get(cd)

            # ls result
            else:
                if not(parts[1] in curr.children):
                    if parts[0] == 'dir':
                        # add new folder to the tree
                        curr.children[parts[1]] = Node(0, curr, {})
                    else:
                        # add new file to the tree
                        size = int(parts[0])
                        curr.children[parts[1]] = Node(size, curr, None)
                        # update folder sizes -> go up in the tree until reaching the root
                        upNode = curr
                        while upNode != None:
                            upNode.value += size
                            upNode = upNode.parent

def firstPart():
    def calculateSum(node):
        if node.children == None:
            return 0
        else:
            result = 0
            if(node.value <= 100000):
                result += node.value
            for n in list(node.children.values()):
                result += calculateSum(n)
            return result
    return calculateSum(root) 

def secondPart():
    candidates = []
    available = 70000000 - root.value
    needed = 30000000 - available
    def addElements(node):
        if node.children != None and node.value >= needed:
            candidates.append(node.value)
            for n in list(node.children.values()):
                addElements(n)
    addElements(root)
    return min(candidates)

treeInit()
print(firstPart())
print(secondPart())