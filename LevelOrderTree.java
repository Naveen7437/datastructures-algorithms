class Node{
    public int data;
    public Node left;
    public Node right;

    public Node(int item){
        data = item;
        left = null;
        right = null;
    }
}

class Tree{
    public Node root;
    public Tree(){
        root = null;
    }

    public  int Height(Node root){
        if (root == null){
            return 0;
        }else {
            int leftHeight = Height(root.left);
            int rightHeight = Height(root.right);
            if (leftHeight > rightHeight) {
                return leftHeight + 1;
            } else {
                return rightHeight + 1;
            }
        }
    }

    void PrintLevelOrder(){
        int height = Height(root);
        for(int i=1; i<=height; i++){
            PrintNodes(i, root);
        }
    }

    void PrintNodes(int level, Node root){
        if (root == null) return;
        if (level ==1){
            System.out.println(root.data);
        }else if(level >1) {
        PrintNodes(level -1, root.left);
        PrintNodes(level -1, root.right);
        }
    }

}


class LevelOrderTree{
    public static void main(String [] args){
    Tree tree = new Tree();
    tree.root= new Node(1);
    tree.root.left= new Node(2);
    tree.root.right= new Node(3);
    tree.root.left.left= new Node(4);
    tree.root.left.right= new Node(5);
//    System.out.println(tree.Height(root));
//    System.out.println(root.data);
    tree.PrintLevelOrder();
    }
}