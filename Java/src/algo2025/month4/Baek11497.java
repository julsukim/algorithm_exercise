package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek11497 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int tc = T;
        StringBuilder sb = new StringBuilder();

        while (tc-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr);

            int[] front = new int[N/2 + N%2];
            int[] rear = new int[N/2];

            for (int i=0; i<N; i++) {
                if (i % 2 == 0) front[i/2] = arr[i];
                else rear[N/2 - 1 - i/2] = arr[i];
            }

            int maximum = Math.abs((front[0] - rear[rear.length - 1]));
            for (int i=1; i<front.length; i++) {
                int diff = Math.abs((front[i] - front[i-1]));
                maximum = Math.max(maximum, diff);
            }
            maximum = Math.max(maximum, Math.abs((front[front.length-1] - rear[0])));
            for (int i=1; i<rear.length; i++) {
                int diff = Math.abs((rear[i] - rear[i-1]));
                maximum = Math.max(maximum, diff);
            }

            sb.append(maximum).append("\n");
        }
        System.out.println(sb.toString());
    }
}
