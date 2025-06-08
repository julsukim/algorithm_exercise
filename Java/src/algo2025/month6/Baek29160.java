package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek29160 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<PriorityQueue<Integer>> squad = new ArrayList<>();
        for (int i = 0; i <= 11; i++) {
            squad.add(new PriorityQueue<>((a, b) -> b - a));
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int pos = Integer.parseInt(st.nextToken());
            int val = Integer.parseInt(st.nextToken());

            squad.get(pos).add(val);
        }

        int year = 0;
        while (year < K) {
            // 선발 선택 & 가치 하락
            for (int i = 1; i <= 11; i++) {
                if (!squad.get(i).isEmpty()) {
                    int best = squad.get(i).poll();
                    squad.get(i).offer(best > 0 ? best - 1 : 0);
                }
            }
            year++;
        }

        int teamValue = 0;
        for (int i = 1; i <= 11; i++) {
            if (!squad.get(i).isEmpty()) {
                teamValue += squad.get(i).poll();
            }
        }

        System.out.println(teamValue);
    }
}
