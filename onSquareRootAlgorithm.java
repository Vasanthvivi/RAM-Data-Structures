public class onSquareRootAlgorithm {
    public static void main(String...args){
       int value = 36;
       int ans = floorSqrt(value);
       System.out.println(ans+"  in "+count+" steps");
    }
    static int count = 0;
    public static int floorSqrt(int x)
    {
        // Base Cases
        if (x == 0 || x == 1)
            return x;
 
 
        // Do Binary Search for floor(sqrt(x))
        long start = 1, end = x, ans=0;
        while (start <= end)
        {
        count++;

            int mid = (int) ((start + end) / 2);
 
            // If x is a perfect square
            if (mid*mid == x)
                return (int)mid;
 
            // Since we need floor, we update answer when mid*mid is
            // smaller than x, and move closer to sqrt(x)
            if (mid*mid < x)
            {
                start = mid + 1;
                ans = mid;
            }
            else   // If mid*mid is greater than x
                end = mid-1;
        }
        return (int)ans;
    }
}
