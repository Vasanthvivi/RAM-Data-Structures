public class craft {
    public static void main(String...args){
        int value = 10000;
        target = value;
        finder(value);
    }
    public static int target = 0;
    public static int count = 0;
    public static int answer = 0;
    public static void finder(int value){
        int start = 1, end = value;
        while(start < end){
            int mid = start + (end-start)/2;
            if(mid * mid == target){
                answer = mid;
                break;
            }
            if(mid * mid > target){
                end = mid - 1;
            }
            if(mid * mid < target){
                answer = mid;
                start = mid;
            }
        }
        System.out.print(answer);
    }
}
