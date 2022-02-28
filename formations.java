public class formations {
    public static void main(String...args){
        S(2);
    }   

    static int[] elements = { 1,2 };

    private static void S(int n){
        if(n == 0){
            printElements();
        }else{
            elements[n - 1] = 0;
            S(n-1);
            elements[n - 1] = 1;
            S(n-1);
            System.out.println("instructions in stack");
        }
    }

    private static void printElements(){
        for (int i : elements) {
            System.out.println(elements[i]);
        }
    }
}
