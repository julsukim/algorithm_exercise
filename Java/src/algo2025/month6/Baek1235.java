package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1235 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int L = 0;

        String[] nums = new String[N];
        for (int i = 0; i < N; i++) {
            nums[i] = br.readLine();
        }

        L = nums[0].length();
        int answer = 0;

        Set<String> set = new HashSet<>();
        for (int i = 1; i <= L; i++) {
            set.clear();
            for (int j = 0; j < N; j++) {
                set.add(nums[j].substring(L - i, L));
            }
            if (set.size() == N) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}
