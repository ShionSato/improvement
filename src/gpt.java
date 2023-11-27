public class DoubleAll {
    public static void main(String[] args) {
        if(args.length == 0) {
            System.out.println("No numbers provided.");
        } else {
            int i = 0;
            while(i < args.length) {
                int value = Integer.parseInt(args[i]);
                System.out.println(args[i] + " × 2 = " + (value * 2));
                i++;
            }
        }
    }
}