public class ToBinary{
    public static void main(String[] args){
        String s = System.console().readLine("n = ");
        double n = Integer.parseInt(s);
        for(int i=30;0<=i;i--){
            double k = (double)n/Math.pow(2, i);
            int intK = (int)k;
            System.out.print(intK);
            if(intK==1){
                n = n%Math.pow(2, i);
            }
        }
        System.out.println("");
    }
}