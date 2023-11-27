public class Dice {
    public static void main(String[] args) {
        int x = (int)(Math.random() * 6) + 1;
        System.out.println("サイコロを振ったら "+ x + " が出ました。");
    }
}