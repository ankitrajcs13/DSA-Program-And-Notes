"""
Youtube Link: https://www.youtube.com/watch?v=CVA85JuJEn0 
Note VVI: AVL ,  Red-Black Tree & B-Trees / B+ Trees are such data structure that stores elements in sorted order and supports:

Insertion in O(log n)
Deletion in O(log n)
Search in O(log n)

=> For printing data in sorted order in case of AVL & Red-Black tree , just use inorder traversal,
because Binary search tree is base for both.

Note:
1) Insert: Insert in same way as we do in BST
But before returing the actual node update the height of current node and 
check if tree is balanced by calling the 'rotate(node)'.

2) Searching a node:  search in avl tree is exactly same as we do in BST.

3) Deletion: Involves four steps : 
a) Finding the node to be deleted. => just search the node
b) Removing the node, handling the three standard BST deletion cases (leaf, one child, two children).
c) Updating the heights of affected nodes.
d) Rebalancing the tree if necessary.

Time for all operation i.e insertion , searching and deletion is : O(logn)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1  # height from node to leaf
        self.left = None 
        self.right = None

class AVL:

    def height(self, node):  # height from node to leaf
        if node is None:
            return 0
        return node.height

    def insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = max(self.height(node.left), self.height(node.right)) + 1  # update the height of node before balancing
        return self.rotate(node)  # then rotate the node if balanced and return new updated node

    def rotate(self, node):
        if self.height(node.left) - self.height(node.right) > 1:
            if self.height(node.left.left) >= self.height(node.left.right):
                # left-left case so simply rotate one time right
                return self.rightRotate(node)
            else:
                # left - right case from top. So rotate first Left and then Right(we do from bottom up and in opposite fashon to balance)
                node.left = self.leftRotate(node.left)  # extra node will come as Left child of 'node' after LeftRotation.
                return self.rightRotate(node)
        if self.height(node.right) - self.height(node.left) > 1:
            if self.height(node.right.right) >= self.height(node.right.left):
                # right - right case so simply rotate one time left
                return self.leftRotate(node)
            else:
                # right - left case from top. So rotate first right and then Left(we do from bottom up and in opposite fashon to balance)
                node.right = self.rightRotate(node.right)  # extra node will come as right child of 'node' after rightRotation.
                return self.leftRotate(node)
        return node  # if already balanced then return the (unchanged) node pointer

    def rightRotate(self, parent):
        left_child = parent.left
        left_right_child = left_child.right
        left_child.right = parent
        parent.left = left_right_child
        parent.height = max(self.height(parent.left), self.height(parent.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1
        return left_child  # this will become parent after rotation so return this node

    def leftRotate(self, parent):
        right_child = parent.right
        right_left_child = right_child.left
        right_child.left = parent
        parent.right = right_left_child
        parent.height = max(self.height(parent.left), self.height(parent.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1
        return right_child  # this will become parent after rotation so return this node

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.rotate(node)

    def search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)

    def inorder(self, node):  # New method to print tree values in sorted order
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

# Main program
root = None
avl = AVL()

# Insert values
for i in range(1000):
    root = avl.insert(root, i)

print("Height of AVL tree after insertion:", avl.height(root))

# Print all values in tree
print("Values in AVL tree (in-order):")
avl.inorder(root)

# Search for a value
search_value = 500
found_node = avl.search(root, search_value)
if found_node:
    print(f"Value {search_value} found in AVL tree.")
else:
    print(f"Value {search_value} not found in AVL tree.")

# Delete values
for i in range(600):
    root = avl.delete(root, i)

print("Height of AVL tree after deletion:", avl.height(root))


# java
"""
class Node {
    int value;
    int height;
    Node left, right;

    Node(int val) {
        value = val;
        height = 1;
    }
}

class AVL {
    int height(Node node) {
        if (node == null)
            return 0;
        return node.height;
    }

    Node insert(Node node, int value) {
        if (node == null)
            return new Node(value);

        if (value < node.value)
            node.left = insert(node.left, value);
        else
            node.right = insert(node.right, value);

        node.height = 1 + Math.max(height(node.left), height(node.right));
        return rotate(node);
    }

    Node rotate(Node node) {
        int balance = height(node.left) - height(node.right);

        // Left heavy
        if (balance > 1) {
            if (height(node.left.left) >= height(node.left.right)) {
                return rightRotate(node);
            } else {
                node.left = leftRotate(node.left);
                return rightRotate(node);
            }
        }

        // Right heavy
        if (balance < -1) {
            if (height(node.right.right) >= height(node.right.left)) {
                return leftRotate(node);
            } else {
                node.right = rightRotate(node.right);
                return leftRotate(node);
            }
        }

        return node;
    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        x.right = y;
        y.left = T2;

        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;

        return x;
    }

    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        y.left = x;
        x.right = T2;

        x.height = Math.max(height(x.left), height(x.right)) + 1;
        y.height = Math.max(height(y.left), height(y.right)) + 1;

        return y;
    }

    Node minValueNode(Node node) {
        Node current = node;
        while (current.left != null)
            current = current.left;
        return current;
    }

    Node delete(Node node, int value) {
        if (node == null)
            return node;

        if (value < node.value)
            node.left = delete(node.left, value);
        else if (value > node.value)
            node.right = delete(node.right, value);
        else {
            // Node with one child or none
            if (node.left == null || node.right == null) {
                Node temp = (node.left != null) ? node.left : node.right;
                if (temp == null)
                    return null;
                else
                    node = temp;
            } else {
                Node temp = minValueNode(node.right);
                node.value = temp.value;
                node.right = delete(node.right, temp.value);
            }
        }

        node.height = 1 + Math.max(height(node.left), height(node.right));
        return rotate(node);
    }

    Node search(Node node, int value) {
        if (node == null || node.value == value)
            return node;
        if (value < node.value)
            return search(node.left, value);
        return search(node.right, value);
    }

    void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.value + " ");
            inOrder(node.right);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        AVL avl = new AVL();
        Node root = null;

        // Insert values
        for (int i = 0; i < 1000; i++) {
            root = avl.insert(root, i);
        }

        System.out.println("Height of AVL tree after insertion: " + avl.height(root));

        // Print all values in-order
        System.out.println("Values in AVL tree (in-order):");
        avl.inOrder(root);
        System.out.println();

        // Search for a value
        int searchValue = 500;
        Node found = avl.search(root, searchValue);
        if (found != null)
            System.out.println("Value " + searchValue + " found in AVL tree.");
        else
            System.out.println("Value " + searchValue + " not found in AVL tree.");

        // Delete values
        for (int i = 0; i < 600; i++) {
            root = avl.delete(root, i);
        }

        System.out.println("Height of AVL tree after deletion: " + avl.height(root));
    }
}
"""
