public class mergeAgain {
    public static void main(String...args){
        int[] items = { 5,4,3 };
        getitems(items, 0, items.length-1);
        for(int e:items){
            System.out.print(e);
        }
    }

    public static void getitems(int[] items, int start, int end){
        if(start < end){
            int mid = start + (end-start)/2;
            getitems(items, start, mid);
            merge(items, start, mid, end);
        }
    }
    public static void merge(int[] items, int start, int mid, int end){
        int leftArrayLength = mid - start + 1;
        int rightArrayLength = end - mid;
        int[] leftArray = new int[leftArrayLength];
        int[] rightArray = new int[rightArrayLength];
        for(int i = 0; i < leftArrayLength; i++){
            leftArray[i] = items[start + i];
        }
        for(int j = 0; j < rightArrayLength; j++){
            rightArray[j] = items[mid+j+1];
        }
        int a = 0,b = 0, c = start;
        while(a < leftArrayLength && b < rightArrayLength){
            if(leftArray[a] < rightArray[b]){
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
        while(b < rightArrayLength){
            items[c] = rightArray[b];
            b++;c++;
        }
    }
}
