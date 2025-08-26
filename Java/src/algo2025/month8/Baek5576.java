package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek5576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] ws = new int[10];
        for (int i = 0; i < 10; i++) {
            ws[i] = Integer.parseInt(br.readLine());
        }
        int[] ks = new int[10];
        for (int i = 0; i < 10; i++) {
            ks[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(ws);
        Arrays.sort(ks);
        int w = ws[9] + ws[8] + ws[7];
        int k = ks[9] + ks[8] + ks[7];
        System.out.println(w + " " + k);
    }
}
