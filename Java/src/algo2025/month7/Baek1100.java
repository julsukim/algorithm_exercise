package algo2025.month7;

import java.io.*;

public class Baek1100 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int counter = 0;
        for (int i = 0; i < 8; i++) {
            String line = br.readLine();
            for (int j = 0; j < 8; j++) {
                char c = line.charAt(j);
                if (i % 2 == 0) {
                    if (j % 2 == 0 && c == 'F') counter++;
                } else {
                    if (j % 2 == 1 && c == 'F') counter++;
                }
            }
        }
        System.out.println(counter);
    }
}
