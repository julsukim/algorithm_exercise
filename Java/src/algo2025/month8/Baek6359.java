package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek6359 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            boolean[] rooms = new boolean[n+1];
            for (int i = 2; i <= n; i++) {
                int multi = 1;

                while (i * multi <= n) {
                    int idx = i * multi;
                    rooms[idx] = !rooms[idx];
                    multi++;
                }
            }
            int cnt = 0;
            for (int i = 1; i <= n; i++) {
                if (!rooms[i]) cnt++;
            }

            sb.append(cnt).append("\n");
        }
        System.out.println(sb);
    }
}
