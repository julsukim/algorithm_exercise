package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek11000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];

        StringTokenizer st;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            arr[i][0] = s;
            arr[i][1] = t;
        }

        Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(arr[0][1]);

        for (int i=1; i<N; i++) {
            if (arr[i][0] >= pq.peek()) {
                pq.poll();
            }
            pq.add(arr[i][1]);
        }

        System.out.println(pq.size());
    }
}
