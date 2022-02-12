public class divide {
    public static void main(String...args){
        int[] items = { 1,2,3,4,5,6 };
        divide(items, 0, items.length - 1);
    }
    static int pointer = 0;
    public static void divide(int[] items, int left, int right){
        if(left != right){
            int mid = left + ( (right - left) / 2);
            divide(items, left, mid);
            for(int i = left; i <= right; i++){
                System.out.print(items[i]);
            }
            System.out.println();
        }
    }
}
