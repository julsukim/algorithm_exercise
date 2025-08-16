package algo2025.month8;

import java.io.*;

public class Baek17608 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] heights = new int[N];
        for (int i = 0; i < N; i++) {
            heights[i] = Integer.parseInt(br.readLine());
        }
        int beforeMax = 0;
        int result = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (heights[i] > beforeMax) {
                result++;
                beforeMax = heights[i];
            }
        }
        System.out.println(result);
    }
}
