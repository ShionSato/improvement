public class Baisu2 {
    public static void main(String[]args){
        String s = System.console().readLine("6桁のユーザIDを入力せよ。");
        int num = Integer.parseInt(s);
        if(num % 2 == 0 && num % 3==0){
            System.out.println("2と3の両方の倍数です。");
        }else if(num % 2 == 0 || num % 3==0){
            System.out.println("2と3の片方の倍数です。");
        }else{
            System.out.println("どちらの倍数でもありません。");
        }
    }    
}
