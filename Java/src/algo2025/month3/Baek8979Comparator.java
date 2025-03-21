package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek8979Comparator {

    static class Nation {
        int name;
        int gold;
        int silver;
        int bronze;

        public Nation(int name, int gold, int silver, int bronze) {
            this.name = name;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        public boolean isSameRank(Nation other) {
            return this.gold == other.gold && this.silver == other.silver && this.bronze == other.bronze;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Nation[] nations = new Nation[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            nations[i] = new Nation(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(nations, Comparator
                .comparingInt((Nation nation) -> nation.gold).reversed()
                .thenComparing(Comparator.comparingInt((Nation nation) -> nation.silver).reversed())
                .thenComparing(Comparator.comparingInt((Nation nation) -> nation.bronze).reversed()));

//        Arrays.sort(nations, Comparator
//                .comparing((Nation nation) -> nation.gold).reversed()
//                .thenComparing(Comparator.comparing((Nation nation) -> nation.silver).reversed())
//                .thenComparing(Comparator.comparing((Nation nation) -> nation.bronze).reversed()));

        int rank = 1;
        int actualRank = 1;
        for (int i = 0; i < n; i++) {
            if ((i > 0) && !nations[i].isSameRank(nations[i - 1])) {
                rank = i + 1;
            }
            if (nations[i].name == k) {
                actualRank = rank;
                break;
            }
        }

        System.out.println(actualRank);
    }
}
