public class mergeSortPart {
    public static void main(String...args){
        int[] left = { 5 };
        int[] right = { 4 };
        int[] run = new int[10];
        int i = 0, j = 0, k = 0;
        while(i < left.length && j < right.length){
            if(left[i] <= right[j]){
                run[k] = left[i];
                i++;
            }else{
                run[k] = right[j];
                j++;
            }
            k++;
        }
        //some elements not included in the final array, lets add those
        while(i < left.length){
            run[k] = left[i];
            i++;k++;
        }
        while(j < right.length){
            run[k] = left[j];
            j++;k++;
        }
        System.out.println(run);
    } 
}
