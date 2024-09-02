import java.io.*;

public class Ques3 {
    public static void main(String a[]) {
        try {
            int n = readFromFile("input.txt");
            generateDiamond(n);
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    public static int readFromFile(String filename) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            return Integer.parseInt(reader.readLine().trim());
        }
    }

    public static void generateDiamond(int n) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
          
            for (int i = 1; i <= n; i += 2) {
                for (int j = 0; j < (n - i) / 2; j++) {
                    writer.write(" ");
                }

                for (int k = 0; k < i; k++) {
                    writer.write("*");
                }
                writer.newLine();
            }

            for (int i = n - 2; i > 0; i -= 2) {
                for (int j = 0; j < (n - i) / 2; j++) {
                    writer.write(" ");
                }
                for (int k = 0; k < i; k++) {
                    writer.write("*");
                }

                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
