public class output_gfile{
    public static void main(String[] args){
        
        for(int i=0;i<args.length;i++){
            int num = Integer.parseInt(args[i]);
            System.out.println(args[i]+" × 2 = "+ num*2);
        }
    }
}