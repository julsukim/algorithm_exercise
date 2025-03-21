package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek8979Comparable {

    static class Nation implements Comparable<Nation> {
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

        @Override
        public int compareTo(Nation other) {
            if (this.gold != other.gold) {
                return Integer.compare(other.gold, this.gold);
            }
            if (this.silver != other.silver) {
                return Integer.compare(other.silver, this.silver);
            }
            return Integer.compare(other.bronze, this.bronze);
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

        Arrays.sort(nations);

//        int rank = 1;
//        int sameRank = 0;
//        if (k == nations[0].name) {
//            System.out.println(rank);
//        } else {
//            for (int i = 1; i < n; i++) {
//                if (k == nations[i].name) {
//                    System.out.println(rank);
//                    break;
//                }
//                if (nations[i].compareTo(nations[i - 1]) == 0) {
//                    sameRank++;
//                    continue;
//                }
//                rank = rank + sameRank + 1;
//                sameRank = 0;
//            }
//        }

        int rank = 1;
        int actualRank = 1;
        for (int i = 0; i < n; i++) {
            if (i > 0 && !nations[i].isSameRank(nations[i - 1])) {
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
