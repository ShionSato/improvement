public class Average {
    public static void main(String[] args) {
        System.out.println("2つの数値を入力してください。");
        String t = System.console().readLine("x = ");
        int x = Integer.parseInt(t);
        t = System.console().readLine("y = ");
        int y = Integer.parseInt(t);
        double souka = (double)((x + y) / 2.0);
        double soujou = (double)(Math.sqrt(x * y));
        System.out.println(x +" と "+ y +" の相加平均は " + souka);
        System.out.println(x +" と "+ y +" の相乗平均は " + soujou);
    }
}
