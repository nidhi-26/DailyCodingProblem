#code

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def serialize(l, root):
    '''
    param: l:  list to store data
    param: root:  root of tree
    return: None,  you have to serialize data of tree in list
    '''
    if not root:
        l.append(None)
        return
    else:
        l.append(root.data)
        serialize(l, root.left)
        serialize(l, root.right)
        return
    
    
def deSerializeRecur(l):
    if len(l) == 0:
        return None
    else:
        num = l.pop()
        #print(num)
        if not num:
            root = None
            return root
        else:
            root = Node(num)
            left = deSerializeRecur(l)
            root.left = None if not left else left
            right = deSerializeRecur(l)
            root.right = None if not right else right
            return root
    
def deSerialize(l):
    '''
    param: l:  list of serialize data
    return :  root of tree
    '''
    #print(l)
    l.reverse()
    #print(l)
    root = deSerializeRecur(l)
    return root

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)
    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    l = []
    serialize(l, root)
    inorder(deSerialize(l))
    print()
    
    root = Node(10)
    root.right = Node(30)
    root.left = Node(20)
    root.left.left = Node(40)
    root.left.right = Node(60)
    
    l = []
    serialize(l, root)
    inorder(deSerialize(l))
    
if __name__ == '__main__':
    main()
