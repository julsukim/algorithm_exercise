package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek9466 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] choice = new int[n + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                choice[i] = Integer.parseInt(st.nextToken());
            }

            // visited[i] = 탐색 ID, 0이면 아직 탐색 안 함
            int[] visited = new int[n + 1];
            int traversalID = 1;
            int teamMembers = 0;

            for (int i = 1; i <= n; i++) {
                if (visited[i] != 0) continue;  // 이미 처리된 노드면 건너뛴다

                int cur = i;
                // 아직 방문하지 않은 노드가 나올 때까지 이동
                while (visited[cur] == 0) {
                    visited[cur] = traversalID;
                    cur = choice[cur];
                }
                // 같은 탐색 ID로 돌아왔다면 사이클이 형성된 것
                if (visited[cur] == traversalID) {
                    int start = cur;
                    do {
                        teamMembers++;
                        start = choice[start];
                    } while (start != cur);
                }
                traversalID++;
            }

            // n명 중 팀에 속한 사람을 제외
            sb.append(n - teamMembers).append('\n');
        }

        System.out.print(sb);
    }
}
