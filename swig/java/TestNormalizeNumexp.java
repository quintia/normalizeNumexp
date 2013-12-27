import java.util.Scanner;

public class TestNormalizeNumexp {
    static {
        System.loadLibrary("normalize_numexp");
    }
    public static void main(String [] args) {
        NormalizeNumexp n = new NormalizeNumexp("ja");
        StringVector result = new StringVector(0);
        
        Scanner stdin = new Scanner(System.in);
        while (stdin.hasNext()) {
            String text = stdin.next();
            n.normalize(text, result);

            System.out.println("text:" + text);
            for (long i = 0, size = result.size(); i < size; i++) {
                System.out.println(result.get((int)i));
            }
            System.out.println();
        }
    }
}
