package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1292 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int cur = 1;
        int counter = 0;
        int total = 0;
        for (int i = 1; i <= B; i++) {
            counter++;

            if (counter > cur) {
                counter = 1;
                cur++;
            }
            if (i >= A) total += cur;
        }

        System.out.println(total);
    }
}
