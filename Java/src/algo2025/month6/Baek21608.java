package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek21608 {

    private static final int[][] delta = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] matrix = new int[N][N];

        List<Set<Integer>> fS = new ArrayList<>();
        for (int i = 0; i <= N * N; i++) {
            fS.add(new HashSet<>());
        }

        for (int i = 0; i < N * N; i++) {
            st = new StringTokenizer(br.readLine());

            int cS = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 4; j++) {
                fS.get(cS).add(Integer.parseInt(st.nextToken()));
            }

            int eCnt = 0;
            int fCnt = 0;

            int aR = 0;
            int aC = 0;

            for (int r = N - 1; r >= 0; r--) {
                for (int c = N - 1; c >= 0; c--) {
                    if (matrix[r][c] != 0) continue;

                    int cE = 0;
                    int cF = 0;

                    for (int d = 0; d < 4; d++) {
                        int nR = r + delta[d][0];
                        int nC = c + delta[d][1];

                        if (nR < 0 || nR >= N || nC < 0 || nC >= N) continue;

                        if (fS.get(cS).contains(matrix[nR][nC])) cF++;
                        if (matrix[nR][nC] == 0) cE++;
                    }

                    if (cF > fCnt) {
                        aR = r;
                        aC = c;
                        eCnt = cE;
                        fCnt = cF;
                    } else if (cF == fCnt) {
                        if (cE >= eCnt) {
                            aR = r;
                            aC = c;
                            eCnt = cE;
                        }
                    }
                }
            }

            matrix[aR][aC] = cS;
        }

        int s = 0;
        int[] values = {0, 1, 10, 100, 1000};
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                int cS = matrix[r][c];
                int cF = 0;

                for (int d = 0; d < 4; d++) {
                    int nR = r + delta[d][0];
                    int nC = c + delta[d][1];

                    if (nR < 0 || nR >= N || nC < 0 || nC >= N) continue;

                    if (fS.get(cS).contains(matrix[nR][nC])) cF++;
                }

                s += values[cF];
            }
        }

        System.out.println(s);
    }
}
