public class S {
    public static void main(String...args){
        Se(A.length);
    }
    public static int[] A = { 1,2 };
    public static void Se(int n){
        if(n < 1){
           for (int i : A) {
            System.out.print(i);
           }
           System.out.println();
        }
        else{
           n = n-1;
           Se(n);
           n = n-1;
           Se(n);
        }
    }
}
