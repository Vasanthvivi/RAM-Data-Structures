public class maxSubArr {
    public static void main(String...args){
        System.out.println("driver started");
        int[] items = { -1,3,4,5 };
    }
        

    public static int find(int[] items, int left, int right){
        int max = 0;
        int prevMax = 0;
        for(int i = left; i<=right; i++){
            max = 0;
            int a = left;
           while(a <= i){
               max += items[a];
               a++;
           }      
           if(prevMax < max){
            prevMax = max;
            System.out.println(prevMax);
           }      
        }
        return prevMax;
    }
}
