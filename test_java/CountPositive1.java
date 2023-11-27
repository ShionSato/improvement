public class CountPositive1 {
    public static void main(String[]args){
        String s = System.console().readLine();
        int n = Integer.parseInt(s);
        int count = 0;
        if(n > 0){
            count = count+1;
        }
        s = System.console().readLine();
        n = Integer.parseInt(s);
        if(n > 0){
            count = count+1;
        }
        s = System.console().readLine();
        n = Integer.parseInt(s);
        if(n > 0){
            count = count+1;
        }
        s = System.console().readLine();
        n = Integer.parseInt(s);
        if(n > 0){
            count = count+1;
        }
        s = System.console().readLine();
        n = Integer.parseInt(s);
        if(n > 0){
            count = count+1;
        }
        System.out.println("正の整数は"+count+"個");
    }
}
