public class output_gfile {
    public static void main(String[] args) {
        String s = MySystem.console().readLine("支払い金額:");
        int shiharai = Integer.parseInt(s);
        int[] maisu = new int[]{0, 0, 0, 0, 0, 0};
        int[] kouka = new int[]{500, 100, 50, 10, 5, 1};
        int goukei = 0;
        
        for (int i = 0; i < args.length; i++) {
            maisu[i] = Integer.parseInt(args[i]);
            goukei += kouka[i] * maisu[i];
        }
        
        if (goukei >= shiharai) {
            System.out.println("支払える");
            
            for (int i = 0; i < kouka.length; i++) {
                int a = kouka[i] * maisu[i];
                
                for (int j = 0; j < maisu[i]; j++) {
                    if (shiharai < a) {
                        a -= kouka[i];
                    }
                }
                
                if (shiharai > 0 && a != 0) {
                    shiharai %= a;
                }
            }
            
            if (shiharai == 0) {
                System.out.println("また、お釣りなしでも支払い可能");
            } else {
                System.out.println("でも、お釣りなしでは支払えない");
            }
        } else {
            System.out.println("支払えない");
        }
    }
}