public class recursions {
    public static void main(String...args){
        int[] items = { 5,4,3};
        int[] tempItems = {5,4,3};
        printStar(5);
    }
    static int iterator = 0;
    public static void printStar(int index){
        if(index >= 0){
            if(index % 2 == 0){
                index--;
                iterator++;
            }
            for(int a = 0; a<iterator; a++){
                System.out.print(" ");
            }
            for(int i = 0; i<index; i++){
                System.out.print("* ");
            }
            System.out.println();
            iterator++;
            printStar(--index);        
        }
    }

    static int condition = 0;
    
    static int[] tempitems = { 5,4,3 };
    
    public static void recur(int[] items, int size){
        if(condition != items.length){
            int mid = size / 2;
            System.out.println(mid+ " is length and those r");
            for(int i = mid ; i < items.length; i++){
                System.out.println(items[i]);
            }
            condition++;
            recur(items, mid);
        }
    }
    public static void sort(int[] items, int left, int right){
    }

    public static void printme(int[] items){
        if(condition != items.length){
            condition++;
            printme(items);
            System.out.println(condition);
            printme(tempitems);
            System.out.println(condition);
            printme(tempitems);
        }
    }
}
