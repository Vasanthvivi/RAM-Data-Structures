import java.util.Scanner;

public class logEn {
    public static void main(String...args){
        // Scanner s = new Scanner(System.in);
        // System.out.println("Enter some value to get the perfect output")
        int value = 410;
        originalValue = value;
        squareRoot(value);
    }

    static int originalValue = 0;
 
    public static void squareRoot(int value){
        int half = value/2;
        if( (half * half) > originalValue){
            squareRoot(half);
        }else if( (half  * half) < originalValue && (value * value) < originalValue){
            System.out.println("got "+half+" "+value);
            squareRoot(++value);
        }else if((half  * half) < originalValue && (value * value) > originalValue){
            squareRoot(++half);
        }else if(half*half == originalValue){
            System.out.println(half);
        }else{
            System.out.println(value);
        }
    }
}
