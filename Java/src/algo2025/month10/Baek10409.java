package algo2025.month10;

import java.io.*;
import java.util.*;

public class Baek10409 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        int counter = 0;
        int time = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int task = Integer.parseInt(st.nextToken());

            if (time + task > t) {
                break;
            }

            counter++;
            time += task;
        }

        System.out.println(counter);
    }
}
