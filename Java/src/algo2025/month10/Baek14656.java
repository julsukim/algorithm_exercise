package algo2025.month10;

import java.io.*;
import java.util.*;

public class Baek14656 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int counter = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());
            if (now != i + 1) counter++;
        }

        System.out.println(counter);
    }
}
