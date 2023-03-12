from PostfixTranslate import nextToken

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def buildExpressionTree(postfixExpr):
    stack = []
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token.isdigit():
            stack.append(BinaryTree(token))
        else:
            rightTree = stack.pop()
            leftTree = stack.pop()
            tree = BinaryTree(token)
            tree.insertLeft(leftTree)
            tree.insertRight(rightTree)
            stack.append(tree)

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack.pop()

def inorder(tree):
    if tree != None:
        if tree.getLeftChild() != None or tree.getRightChild() != None:
            print("(", end="")
        inorder(tree.getLeftChild())
        print(tree.getRootVal(), end="")
        inorder(tree.getRightChild())
        if tree.getLeftChild() != None or tree.getRightChild() != None:
            print(")", end="")

def preorder(tree):
    if tree != None:
        print(tree.getRootVal(), end="")
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end="")

# Ejemplos de expresiones

expr_a = "91 95 + 15 + 19 + 4 *"
expr_b = "B B * A C 4 * * -"
expr_c = "42"
expr_d = "A 57 #"
expr_e = "+ / #"

# Construir árboles binarios algebraicos
try:
    tree_a = buildExpressionTree(expr_a)
    tree_b = buildExpressionTree(expr_b)
    tree_c = buildExpressionTree(expr_c)
    tree_d = buildExpressionTree(expr_d)
    tree_e = buildExpressionTree(expr_e)
except ValueError as e:
    print(e)
else:
    # Mostrar los árboles en notaciones infix, prefix y postfix
    print("Árbol algebraico de la expresión", expr_a)
    inorder(tree_a)
    print()
    preorder(tree_a)
    print()
    postorder(tree_a)
    print()

    print("Árbol algebraico de la expresión", expr_b)
    inorder(tree_b)
    print()
    preorder(tree_b)
    print()
    postorder(tree_b)
    print()

    print("Árbol algebraico de la expresión", expr_c)
    inorder(tree_c)
    print()
    preorder(tree_c)
    print()
    postorder(tree_c)
    print()

   
