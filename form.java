public class form {
    public static void main(String...args){
        System.out.println("welcome to the java tree formation!");
        S(A.length - 1);        
    }

    private static int[] A = { 1,2 };
     
    private static void S(int n){
        if(n < 0){
            showElements();
        }else{
            A[n] = 0;
            S(--n);
            // A[n - 1] = 1;
            // S(n - 1);
        }
    }

    private static void showElements(){
        for (int i : A) {
            System.out.println(A[i]);
        }
        System.out.println();
    }
}
