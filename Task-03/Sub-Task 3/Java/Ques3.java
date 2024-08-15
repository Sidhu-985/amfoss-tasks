public class Ques3 {
    public static void main(String a[]) {
        int n = 5;  

        for (int i = 1; i <= n; i += 2) { 
            for (int j = 0; j < (n - i) / 2; j++) {
                System.out.print(" ");
            }

            for (int k = 0; k < i; k++) {
                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = n - 2; i > 0; i -= 2) { 
            for (int j = 0; j < (n - i) / 2; j++) {
                System.out.print(" ");
            }

            for (int k = 0; k < i; k++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
