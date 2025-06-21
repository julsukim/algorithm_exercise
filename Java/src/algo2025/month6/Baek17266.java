package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek17266 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        int[] lights = new int[M];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            lights[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = N;
        int answer = N;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (isLight(N, lights, mid)) {
                right = mid - 1;
                answer = Math.min(answer, mid);
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean isLight(int N, int[] lights, int power) {
        int cover = 0;
        for (int x : lights) {
            if (x - power > cover) {
                return false;
            }
            cover = Math.max(cover, x + power);
            if (cover >= N) return true;
        }
        return cover >= N;
    }
}
