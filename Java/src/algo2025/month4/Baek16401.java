package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek16401 {

    private static int M;
    private static int N;
    private static int[] arr;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N];

        int right = 0;
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            right = Math.max(arr[i], right);
        }

        int left = 1;

        int mid;
        int maxLength = 0;

        while (left <= right) {
            mid = (right - left) / 2 + left;

            if (isAvailable(mid)) {
                left = mid + 1;
                maxLength = Math.max(mid, maxLength);
            } else {
                right = mid - 1;
            }
        }

        System.out.println(maxLength);
    }

    static boolean isAvailable(int mid) {
        int count = 0;

        for (int i = 0; i < N; i++) {
            count += arr[i] / mid;
            if (count >= M) return true;
        }

        return false;
    }
}
