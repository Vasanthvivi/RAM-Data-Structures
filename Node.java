public class Node {
    int data;
    Node left;
    Node right;
    Node(int _data){
      this.data = _data;
    }

    public void find(int data){
      // System.out.println("i am now in ");
      // System.out.println(this.data);
      if(this.data == data){
        System.out.println("figured out");
        // System.out.println(this);
      }else if(data < this.data){
        this.left.find(data);
      }else if(data > this.data){
        this.right.find(data);
      }else{
        System.out.println("figured out");
        // System.out.println(this);
      }
    }

    public void insert(int data){
       if(this.data == 0){
         this.data = data;
       }else if(this.data == data){
         System.out.println("existence of item restricts insertion");
       }else if(this.data < data){
         if(this.right  == null){
          Node n = new Node(data);
          this.right = n;
          System.out.println("inserted");
        }else{
          this.right.insert(data);
         }
       }else if(this.data > data){
         if(this.left == null){
          Node n = new Node(data);
          this.left = n;
          System.out.println("inserted");
        }else{
          this.left.insert(data);
         }
       }else{
         System.out.println("Not sure how this happened");
       }
    }
}