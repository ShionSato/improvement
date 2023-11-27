```
public class Program {
    public static void main(String[] args) {
        String input;
        int max = -2147483648;

        input = System.console().readLine("整数を入力：");
        int num1 = Integer.parseInt(input);
        if (num1 > max) {
            max = num1;
        }

        input = System.console().readLine("整数を入力：");
        int num2 = Integer.parseInt(input);
        if (num2 > max) {
            max = num2;
        }

        input = System.console().readLine("整数を入力：");
        int num3 = Integer.parseInt(input);
        if (num3 > max) {
            max = num3;
        }

        input = System.console().readLine("整数を入力：");
        int num4 = Integer.parseInt(input);
        if (num4 > max) {
            max = num4;
        }

        System.out.println("最大値：" + max);
    }
}
```