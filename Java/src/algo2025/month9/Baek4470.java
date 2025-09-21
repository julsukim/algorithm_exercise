package algo2025.month9;

import java.io.*;

public class Baek4470 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int sno = 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(sno).append(". ");
            sb.append(br.readLine());
            sb.append("\n");
            sno++;
        }

        System.out.println(sb);
    }
}
