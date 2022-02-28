public class recursionFunctions {
    public static void main(String...args){
        start();
    }

    static void start(){
        System.out.println("bootstrapped");
        one();
        System.out.println("shutdown");
    }
    static void one(){
        System.out.println("1");
        two();
        System.out.println("two ended in one function");
    }
    static void two(){
        System.out.println("2");
        three();
        System.out.println("three ended in two function");
        two();
        System.out.println("two called second time");
    }
    static void three(){
        System.out.println("3");
        four();
        System.out.println("four ended in three function");
    }
    static void four(){
        System.out.println("4");
        System.out.println("four ended in four function");
    }
}
