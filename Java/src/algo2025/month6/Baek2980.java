package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek2980 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[][] lights = new int[N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            lights[i][0] = Integer.parseInt(st.nextToken());
            lights[i][1] = Integer.parseInt(st.nextToken());
            lights[i][2] = Integer.parseInt(st.nextToken());
        }

        // wait = 빨 - 현재시간 % (빨 + 초)
        int time = 0;
        int lastLight = 0;
        for (int i = 0; i < N; i++) {
            time += lights[i][0] - lastLight;
            int wait = lights[i][1] - time % (lights[i][1] + lights[i][2]);
            if (wait > 0) time += wait;
            lastLight = lights[i][0];
        }

        time += L - lastLight;
        System.out.println(time);
    }
}
