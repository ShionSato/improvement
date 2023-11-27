public class output_sfile{
    public static void main(String[] args){
        
        int[] a =new int[args.length];
        for(int i=0;i<args.length;i++){
            int b = Integer.parseInt(args[i]);
            System.out.println(args[i]+"×2="+b*2);
        }
    }
}