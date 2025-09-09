package algo2025.month9;

import java.io.*;
import java.util.*;

public class Baek1547 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[] cups = new int[]{0, 1, 2, 3};
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int tmp = cups[x];
            cups[x] = cups[y];
            cups[y] = tmp;
        }

        for (int i = 1; i <= 3; i++) {
            if (cups[i] == 1) {
                System.out.println(i);
                break;
            }
        }
    }
}
