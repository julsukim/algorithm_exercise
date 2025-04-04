package algo2025.month4;

import java.io.*;
import java.util.*;

public class Back17393 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] inkArr = new long[N];
        for (int i = 0; i < N; i++) {
            inkArr[i] = Long.parseLong(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        long[] visArr = new long[N];
        for (int i = 0; i < N; i++) {
            visArr[i] = Long.parseLong(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N; i++) {
            int start = i;
            int end = N-1;
            int res = i;

            while (start <= end) {
                int mid = (start + end) / 2;

                if (visArr[mid] <= inkArr[i]) {
                    res = mid;
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }

            sb.append(res - i).append(" ");
        }

        System.out.println(sb.toString());
    }
}
