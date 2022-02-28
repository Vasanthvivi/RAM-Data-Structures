public class dotn {
    public static void main(String...args){
        R(1);
    }    
    public static void R(int value){
        if(value > 3){

        }else{
            System.out.print(value+" ");
            R(++value);
        }
    }
}
