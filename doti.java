public class doti{
    public static void main(String...args){
        int value = 70;
        target = value;
        findroot(value);
    }
    public static int target = 0;
    public static int count = 0;
    public static int ans;
    public static int findroot(int value){
        int start = 1, end = value;
        while(start <= end){
            count++;
            int mid = start + (end - start)/2;
            if(mid * mid > target){
                end = mid-1;
            }
            if(mid * mid < target){
                ans = mid;
                start = mid+1;
            }
            if(mid * mid == target){
               ans = mid;
               System.out.println("Answer "+ans+" in "+count+" steps");
               return ans;
            }
        }
        System.out.println("Answer "+ans+" in "+count+" steps");
        return -1;
    }
}