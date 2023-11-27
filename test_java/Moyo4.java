public class Moyo4 {
    public static void main(String[] args) {
        String t = System.console().readLine("模様に使う文字列を入力してください。");
        System.out.println("「"+ t +"」で作った山形の模様");
        System.out.println("　　　　"+ t);
        System.out.println("　　　"+ t + t + t);
        System.out.println("　　"+ t + t + t + t + t);
        System.out.println("　"+ t + t + t + t + t + t + t);
        System.out.println(t + t + t + t + t + t + t + t + t);
    }
}
