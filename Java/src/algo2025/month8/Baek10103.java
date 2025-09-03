package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek10103 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int c = 100;
        int s = 100;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int ch = Integer.parseInt(st.nextToken());
            int sd = Integer.parseInt(st.nextToken());

            if (ch > sd) {
                s -= ch;
            } else if (ch < sd) {
                c -= sd;
            }
        }
        System.out.println(c);
        System.out.println(s);
    }
}
