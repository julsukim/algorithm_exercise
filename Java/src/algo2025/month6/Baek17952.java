package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek17952 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        int score = 0;
        Deque<int[]> works = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {

            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());

            if (type == 0) {
                if (!works.isEmpty()) {
                    int[] work = works.pop();
                    work[1] -= 1;
                    if (work[1] == 0) {
                        score += work[0];
                    } else {
                        works.push(work);
                    }
                }
            } else {
                int a = Integer.parseInt(st.nextToken());
                int t = Integer.parseInt(st.nextToken());

                if (t - 1 == 0) {
                    score += a;
                } else {
                    works.push(new int[]{a, t - 1});
                }
            }
        }

        System.out.println(score);
    }
}
