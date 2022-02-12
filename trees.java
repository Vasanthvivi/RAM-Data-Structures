public class trees {
   public static void main(String...args){
       System.out.println("welcome to the trees");
       int[] values = { 1,2,3,4,5 };
       //binary tree
       Node n = new Node(3);
       n.insert(1);
       n.insert(2);
       n.insert(4);
       n.insert(5);
       n.insert(5);
       n.find(4);
       n.find(1);
       n.insert(10);
   }
}
