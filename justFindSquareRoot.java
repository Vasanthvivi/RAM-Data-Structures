import java.util.Scanner;

public class justFindSquareRoot {
    public static void main(String...args){
        int value = new Scanner(System.in).nextInt();
        target = value;
        findsquare(value);
    }
    static int target = 0;
    static int count = 0;
    public static int findsquare(int value){
        int start = 1, end = value;
        int ans = 0;
        while(start <= end){
            count++;
            int mid = (start + (end - start)/2 );
            if(mid == target/mid){
                ans = mid;
                System.out.println("Answer "+ans+" in "+count+" steps");
                return mid;
            }
            if( (mid * mid ) > target ){
                end = mid-1;
            }
            if( (mid * mid) < target ){
                ans = mid;
                start = mid+1;
            }
        }
        System.out.println("Answer "+ans+" in "+count+" steps");
        return ans;
    }
}
