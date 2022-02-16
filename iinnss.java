public class iinnss {
    public static void main(String...args){
        System.out.println("welcome to the driver");
        int[] items= {  4,3,2,2121,5,4};
        int current = 0;
        int currentElement = 0;
        for(int i = 1; i < items.length; i++){
            current = i;
            currentElement = items[i];
            while(current > 0 && currentElement <= items[current-1]){
                items[current] = items[current-1];
                current--;
            }
            items[current] = currentElement;
        }
        for(int ele : items){
           System.out.println(ele);
        }
    }
}
