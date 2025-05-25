package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek3758 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            TeamLog[] info = new TeamLog[n + 1];
            for (int i = 0; i <= n; i++) {
                info[i] = new TeamLog(i, k);
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int tId = Integer.parseInt(st.nextToken());
                int pId = Integer.parseInt(st.nextToken());
                int score = Integer.parseInt(st.nextToken());

                info[tId].solve(pId, score, i);
            }

            Arrays.sort(info);
            int myRank = -1;
            for (int r = 0; r <= n; r++) {
                if (info[r].id == t) {
                    myRank = r + 1;
                }
            }

//            for (TeamLog log : info) {
//                log.printTeamLog();
//            }

            sb.append(myRank).append("\n");
        }
        System.out.println(sb.toString());
    }

    private static class TeamLog implements Comparable<TeamLog> {
        int id, totalScore, submits, lastSubmitTime;
        int[] scores;

        public TeamLog(int id, int problemCount) {
            this.id = id;
            scores = new int[problemCount + 1];
            totalScore = 0;
            submits = 0;
            lastSubmitTime = 0;
        }

        public void solve(int pId, int score, int lastSubmitTime) {
            int scoreDiff = score - scores[pId];
            if (scoreDiff > 0) {
                scores[pId] = score;
                totalScore += scoreDiff;
            }
            this.lastSubmitTime = lastSubmitTime;
            submits++;
        }

        @Override
        public int compareTo(TeamLog o) {
            if (totalScore == o.totalScore) {
                if (submits == o.submits) {
                    return lastSubmitTime - o.lastSubmitTime;
                }
                return submits - o.submits;
            }
            return o.totalScore - totalScore;
        }

        public void printTeamLog() {
            System.out.println(id + ": " + totalScore + ", " + submits + ", " + lastSubmitTime);
        }
    }
}
