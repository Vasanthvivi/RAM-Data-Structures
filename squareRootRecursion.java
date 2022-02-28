public class squareRootRecursion {
    public static void main(String...args){
        int value = 100000;
        originalValue = value;
        squareRoot(value);
    }
    static int originalValue = 0;
    static int stackCount = 0;
    public static void squareRoot(int value){
        stackCount++;
        int mid = value/2;
        if( (mid * mid) > originalValue){
            squareRoot(mid);
        }else if( (mid*mid) < originalValue){
            if(( (mid+1) * (mid+1) ) > originalValue){
                System.out.println("CPU steps taken to complete "+stackCount);
                System.out.println("Answer is "+mid);
            } else{
                squareRoot(++value);
            }
        }else{
            System.out.println("CPU steps taken to complete "+stackCount);
            System.out.println("Answer "+mid);
        }
    }
}