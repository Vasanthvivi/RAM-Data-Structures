public class recursian {
    public static void main(String...args){
        System.out.println("Driver Started");
        int[] items = { 5,4,3,2,1,10,9,8,7,6,11,12,14,4 };
        sort(items, 0, items.length - 1);
        for(int i = 0; i < items.length; i++){
            System.out.print(items[i]);
        }
        // start(items, items.length - 1);
    }
    static int stackPointer = 0;
    public static void sort(int[] items, int left, int right){
        stackPointer++;
        System.out.println("Stack Pointer "+stackPointer);
        if(left < right){
            int mid = (left + (right - left)/2);
            sort(items, left, mid);
            sort(items, mid + 1, right);
            merge(items, left, mid, right);
        }
    }

    public static void merge(int[] items, int l, int m, int r){
        int leftArrayLength = m - l + 1;
        int rightArrayLength = r - m;
        int[] leftArray = new int[leftArrayLength];
        int[] rightArray = new int[rightArrayLength];
        for(int i = 0; i < leftArrayLength; i++){
            leftArray[i] = items[l + i];
        }
        for(int j = 0; j < rightArrayLength; j++){
            rightArray[j] = items[m + j + 1];
        }
        int a = 0, b = 0, c = l;
        while(a < leftArrayLength && b < rightArrayLength){
            if(leftArray[a] <= rightArray[b]){
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
            a++;c++;
        }    
        while(a < rightArrayLength){
            items[c] = rightArray[b];
            b++;c++;
        }    
    }



    public static void start(int[] items, int index){
        if(index > 0){
            int mid = index/2;
            start(items, mid);
        }
    }
}
