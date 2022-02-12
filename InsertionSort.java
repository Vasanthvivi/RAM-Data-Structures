public class InsertionSort {
  public static void main(String...args){
      System.out.println("Welcome to the insertion sort!");
      int[] items = {5,4,3,2,1};
      for(int i=0; i<items.length; i++){
        System.out.println(items[i]);
      }
      int element;
      int index;
      for(int a = 1; a < items.length; a++){
        element = items[a];
        index = a - 1;
        while(index >= 0 && element <= items[index]){
          items[index+1] = items[index];
          index--;
        }
        items[index+1] = element;
      }
      System.out.println("welcome ");
      for(int b = 0; b < items.length; b++){
        System.out.print(items[b]+" ");
      }
    }
}

