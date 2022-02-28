public class isSorted{
   public static void main(String...args){
       int[] items = { 0,0,0};
       _items = items;
       combinations(3);
    //    binary(3);
    //    int result = isSortedArray(items, items.length - 1);
    //    System.out.println(result);
   }
   static int[] sampleItems = { 1,2,3 };
   public static void combinations(int n){
     if(n < 1){
         for(int e:sampleItems){
             System.out.print(e);
         }
         System.out.println();
     }else{
         sampleItems[n-1] = 0; 
         combinations(n-1);
         sampleItems[n-1] = 1;
         combinations(n-1);
     }
   }


   static int[] _items = new int[3];
   public static void binary(int n){
       if(n < 1){
           show();System.out.println();

       }else{
          _items[n-1] = 0;
          binary(n-1);
          _items[n-1] = 1;
          binary(n-1);
       }
   }
   public static void show(){
       for(int i: _items){
           System.out.print(i);
       }
   }
   
   public static int isSortedArray(int[] items, int index){
       if(index == 1){
           return 1;
       }
       return (items[index] < items[index-1])?0:isSortedArray(items, index-1);
   }
}