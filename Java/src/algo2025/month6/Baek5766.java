package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek5766 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while (true) {
            st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            if (N == 0 && M == 0) break;

            Map<Integer, Integer> players = new HashMap<>();

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    int player = Integer.parseInt(st.nextToken());
                    players.put(player, players.getOrDefault(player, 0) + 1);
                }
            }

            List<Integer> seconds = new ArrayList<>();
            List<Integer> scores = new ArrayList<>(players.values());

            scores.sort((a, b) -> b - a);
            int secondScore = 0;
            for (int i = 1; i < scores.size(); i++) {
                if (!scores.get(i - 1).equals(scores.get(i))) {
                    secondScore = scores.get(i);
                    break;
                }
            }

            for (Map.Entry<Integer, Integer> e : players.entrySet()) {
                if (e.getValue() == secondScore) seconds.add(e.getKey());
            }

            Collections.sort(seconds);
            for (int p : seconds) {
                sb.append(p).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }
}
