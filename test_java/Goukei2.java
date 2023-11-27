public class Goukei2{
    public static void main(String[] args){
        String s = System.console().readLine("n = ");
        int n = Integer.parseInt(s);
        System.out.println("--- 整数を"+n+"回入力 ---");
        int sum = 0;
        for(int i=0;i<n;i++){
            String suti = System.console().readLine();
            int number = Integer.parseInt(suti);
            sum = sum + number;
        }
        System.out.println("合計: "+sum);
    }
}