public class divideAndMerge{
    public static void main(String...args){
        int[] items = { 5,4,3,2,1,6 };
        sort(items, 0, items.length);
        for(int i = 0; i < items.length; i++){
            System.out.print(items[i]);
        }
    } 
    static int stackPointer = 0;
    public static void sort(int[] items, int left, int right){
        stackPointer++;
        int mid = (left + (right - left)/2);
        sort(items, left, mid);
        merge(items, left, mid, right);
    }

    public static void merge(int[] items, int l, int mid, int right){
        int leftArrayLength = (mid - l);
        int rightArrayLength = (right - mid + 1);
        int[] leftArray = new int[leftArrayLength];
        int[] rightArray = new int[rightArrayLength];
        for(int i = 0; i<leftArrayLength; i++){
            leftArray[i] = items[l + i];
        }
        for(int i = 0; i<rightArrayLength; i++){
            leftArray[i] = items[mid + i + 1];
        }
        int a = 0, b = 0, c = l;
        while(a < leftArrayLength && b < rightArrayLength){
            if(leftArray[a] <= rightArray[b])
            {
                items[c] = leftArray[a];
                a++;
            }else{
                items[c] = rightArray[b];
                b++;
            }
            c++;
        }
        while(a < leftArrayLength){
            items[c] = leftArray[a];
            a++;
            c++;
        }
        while(b < rightArrayLength){
            items[c] = rightArray[b];
            b++;
            c++;
        }
    }
}