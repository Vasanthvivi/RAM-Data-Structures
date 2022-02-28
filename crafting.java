import java.util.Scanner;

public class crafting {
    public static void main(String...args){
        Scanner s = new Scanner(System.in);
        int value = s.nextInt();
        target = value;
        getsquareroot(value);
    }
    public static int target = 0;
    public static int answer = 0;
    public static void getsquareroot(int value){
        int start = 1, end = value;
        while(start < end){
            int midelement = start + (end-start)/2;
            if(midelement * midelement == target){
                answer = midelement;
                System.out.println("Answer "+answer);
                return;
            }
            if(midelement * midelement < target){
                answer = midelement;
                start = ++midelement;
            }
            if(midelement * midelement > target){
                end = midelement - 1;
            }
        }
        System.out.println("Answer "+answer);
    }
}