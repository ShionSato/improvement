/*
 * 学生番号：00000
 * プログラム名：Saidai.java
 * プログラムの内容の説明：４つの整数を入力し、最大値（max）を出力するプログラム 
 * 作成日：2022/11/7
*/
public class Saidai {
    public static void main(String[] args) {
        String ai;
        int b,c;
        ai = System.console().readLine("整数を入力：");
        c = Integer.parseInt(ai);
        ai = System.console().readLine("整数を入力：");
        b = Integer.parseInt(ai);
        if (c < b) {
            c = b;
        }
        ai = System.console().readLine("整数を入力：");
        b = Integer.parseInt(ai);
        if (c < b) {
            c = b;
        }
        ai = System.console().readLine("整数を入力：");
        b = Integer.parseInt(ai);
        if (c < b) {
            c = b;
        }
        System.out.println("最大値：" + c);
    }
}