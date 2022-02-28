public class insertionsor{
    public static void main(String...args){
        System.out.println("connect wires");
        int[] items = { 5,4,3,2,1 };
        int currentElement;
        int currentPosition;
        for(int i = 1; i < items.length; i++){
           currentElement = items[i];
           currentPosition = i - 1;
           while(currentPosition >= 0 && currentElement <= items[currentPosition]){
               items[currentPosition+1] = items[currentPosition];
               currentPosition--;
           }
           items[currentPosition+1] = currentElement;
        }
        for(int e: items){
            System.out.print(e);
        }
    }
}