import java.util.Scanner;

public class PrimeNumbers {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number: ");

        int num = sc.nextInt();

        if (num <= 1) {
            System.out.println(num + " is not a prime number");
        } else {
            for (int i = 2; i <= num; i++) {
                int flag = 0;
                for (int j = 2; j <= Math.sqrt(i); j++) {
                    if (i % j == 0) {
                        flag = 1;
                        break; 
                    }
                }
                if (flag == 0) {
                    System.out.println(i + " is a prime number");
                }
            }
        }
    }
}
