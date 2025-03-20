package algo2025.month3;

import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class baek10813 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");
        int n = Integer.parseInt(nums[0]);
        int m = Integer.parseInt(nums[1]);

//        int[] baskets = new int[n];
//        for (int num=1; num<=n; num++) {
//            baskets[num-1] = num;
//        }

        int[] baskets = IntStream.rangeClosed(1, n).toArray();

        for (int t=0; t<m; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;

            int tmp = baskets[i];
            baskets[i] = baskets[j];
            baskets[j] = tmp;
        }

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            sb.append(baskets[i]).append(" ");
        }

        System.out.println(sb.toString());
    }

}
