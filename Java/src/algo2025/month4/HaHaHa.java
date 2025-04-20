//문제 설명:
//
//노드의 갯수 N, 간선의 갯수 M, 프리패스 노드의 갯수 T, 시작 노드 S, 도착 노드 E
//프리패스 노드란?
//간선은 일방향 간선으로 주어져.
//그런데 프리패스 노드에 도착하면 간선이 양방향 간선으로 바뀜.
//
//프리패스 노드는 반드시 E에 도착하기 전에 1곳을 들려야 한다.
//순회를 시작하기 전에 어떤 프리패스 노드를 들릴것인지 결정해야 한다.
//결정하는 기준은,
//1. 시작 S에서 프리패스 노드 까지의 거리가 가까운 순서 (간선 수)
//2. 만약 조건 1이 같은 것이 여러개 존재한다면, 1을 만족하는 프리패스 노드 중 도착 E까지의 거리가 가장 가까운 노드 순서
//3. 만약 조건 2까지 같은 노드가 여러개라면, 노드 번호가 가장 큰 노드를 선택.
//4. 프리패스 노드를 들리고 E까지 갈수없다면 -1을 출력.
//
//입력
//첫줄: N, M, T, S, E
//두번째 줄: 프리패스 노드들
//세번째 줄 ~ + M: 간선 a, b
//
//N은 최대 3000
//M은 최대 20000
//T는 최대 20

package algo2025.month4;

import java.io.*;
import java.util.*;

public class HaHaHa {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        int[] freePassNodes = new int[T];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < T; i++) {
            freePassNodes[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(freePassNodes);

        Map<Integer, To> oneWayMap = new HashMap<>();
        Map<Integer, To> twoWayMap = new HashMap<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            if (oneWayMap.containsKey(s)) {
                oneWayMap.get(s).add(e);
            } else {
                To to = new To();
                to.add(e);
                oneWayMap.put(s, to);
            }

            if (twoWayMap.containsKey(s)) {
                twoWayMap.get(s).add(e);
            } else {
                To to = new To();
                to.add(e);
                twoWayMap.put(s, to);
            }

            if (twoWayMap.containsKey(e)) {
                twoWayMap.get(e).add(s);
            } else {
                To to = new To();
                to.add(s);
                twoWayMap.put(e, to);
            }
        }

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(S);
        int[] visited = new int[3001];
        visited[S] = 1;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            if (oneWayMap.containsKey(cur)) {
                To to = oneWayMap.get(cur);
                for (int next : to.nexts) {
                    if (next == 0) break; // 노드 번호 1부터 시작
                    if (visited[next] != 0) continue;

                    queue.add(next);
                    visited[next] = visited[cur] + 1;
                }
            }
        }

        int[] distance = new int[T];
        int minDist = 20_001;
        for (int i = 0; i < T; i++) {
            int dist = visited[freePassNodes[i]] - 1;
            distance[i] = dist;

            if (dist >= 0) minDist = Math.min(minDist, dist);
        }

        for (int i = 0; i < T; i++) {
            int start = freePassNodes[i];

            if (distance[start] < minDist || distance[start] == -1) {
                distance[i] = -1;
                continue;
            }

            Queue<Integer> tmpQueue = new ArrayDeque<>();
            int[] tmpVisited = new int[3001];
            tmpQueue.add(start);
            tmpVisited[start] = 1;

            while (!tmpQueue.isEmpty()) {
                int cur = tmpQueue.poll();

                if (twoWayMap.containsKey(cur)) {
                    To to = twoWayMap.get(cur);
                    for (int next : to.nexts) {
                        if (next == 0) break; // 노드 번호 1부터 시작
                        if (tmpVisited[next] != 0) continue;
                        tmpQueue.add(next);
                        tmpVisited[next] = tmpVisited[cur] + 1;
                    }
                }
            }

            distance[i] += tmpVisited[E] - 1;
        }

        int selectedNode = -1;
        minDist = 20_001;
        for (int i = 0; i < T; i++) {
            int dist = distance[i];
            if (dist == -1) continue;

            if (dist < minDist) {
                selectedNode = freePassNodes[i];
                minDist = dist;
            }
        }

        System.out.println(selectedNode == -1 ? -1 : selectedNode + " " + minDist);

    }

    static class To {
        int[] nexts = new int[3001];
        int top = 0;

        public void add(int n) {
            nexts[top++] = n;
        }
    }
}
