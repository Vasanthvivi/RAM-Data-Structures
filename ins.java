public class ins {
    public static void main(String...args){
        int[] items = { 5,4,3,2,1 };
        int currentElement;
        int currentElementIndex;
        for(int i = 1; i < items.length; i++){
            currentElement = items[i];
            currentElementIndex = i;
            while(currentElementIndex > 0 && currentElement <= items[currentElementIndex - 1]){
                items[currentElementIndex] = items[currentElementIndex - 1];
                currentElementIndex--;
            }
            System.out.println("Current Element Index "+currentElementIndex);
            items[currentElementIndex] = currentElement;
        }
        for(int i = 0; i < items.length; i++){
            System.out.print(items[i]);
        }
    }
}
