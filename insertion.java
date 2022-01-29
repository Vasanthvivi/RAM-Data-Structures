public class insertion{
    public static void main(String...args){
        int[] items = { 5,4,3,2,1 };
        //#region start
        int element;
        int currentPos;
        for(int a=1; a<=items.length-1;a++){
           element = items[a];
           currentPos = a-1;
           while(currentPos >= 0 && element <= items[currentPos]){
               items[currentPos+1] = items[currentPos];
               currentPos--;
           }
           items[currentPos+1] = element;
        }
        //#region end
        for(int a=0; a<items.length; a++){
            System.out.println(a);
        }
    }
}