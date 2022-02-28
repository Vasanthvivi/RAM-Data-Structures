public class squareRootIterative {
    public static void main(String...args){
        int value = 36;
        target = value;
        int result = findRoot(value);
        System.out.println(result);
    }
    static int target = 0;
    static int ans = 0;
    public static int findRoot(int value){
        int start = 1, end = value;
        int mid = start + (end - start)/2;
        if(mid * mid == target){
            return mid;
        }
        if( (mid * mid) > target){
            ans = mid;
            end = mid;
        }
        if( (mid * mid) < target ){
            ans = mid;
            start = mid;
        }
        return ans;
    }
}
