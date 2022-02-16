public class badRecursion {
    public static void main(String...args){
        System.out.println("Driver started");
        int[] items = { 5,4,3,2,1 };
        subaray(items);
        // finds(items5, 0, items.length - 1);
    }
    public static void subaray(int[] items){
        int m = 0;
        int len = 1;
        for(int i = 0; i<items.length+1; i++){
            m = pushandfind(items, i);
        }
        System.out.println("maximum is "+m);
    }
    static int max = 0;
    static int prevMax = 0;
    public static int pushandfind(int[] items, int len){
        max = 0;
        for(int i = 0; i<len; i++){
           max += items[i];
        }
        if(max > prevMax){
            prevMax = max;
        }
        return max;
    }
    public static void finds(int[] items, int low, int high){
        if(low < high){
            int mid = (low +  ( (high - low) / 2));
            finds(items, low, mid);
            for(int i = low; i <= mid; i++){
                System.out.print(items[i]);
            }
            System.out.println();
        }
    }
}
