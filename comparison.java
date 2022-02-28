public class comparison {
    public static void main(String...args){
        int c = -1;
        for(int i = 1; i <= 3; i++){
            c++;
            for(int b = 0; b<c;b++){
                System.out.print(" ");
            }
            for(int a = i; a <=3; a++){
                System.out.print(a);
            }
            System.out.println();
        }
        for(int i = 1; i <= 3; i++){
            for(int a = i; a <=3; a++){
                System.out.print(a);
            }
            System.out.println();
        }
    }
}
