import java.nio.file.*;

public class Main {
    public static void main(String[] args) {
        String content = Files.readString(Path.of("input.txt"));
        Files.writeString(Path.of("output.txt"), content);
    }
}
