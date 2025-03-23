package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek20920Opt {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> counter = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (word.length() < m) continue;
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }

        // Map.Entry 리스트 정렬 (객체 생성 최소화)
        List<Map.Entry<String, Integer>> wordList = new ArrayList<>(counter.entrySet());

        wordList.sort((a, b) -> {
            int freqCompare = Integer.compare(b.getValue(), a.getValue()); // 빈도 내림차순
            if (freqCompare != 0) return freqCompare;

            int lengthCompare = Integer.compare(b.getKey().length(), a.getKey().length()); // 길이 내림차순
            if (lengthCompare != 0) return lengthCompare;

            return a.getKey().compareTo(b.getKey()); // 사전순 오름차순
        });

        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : wordList) {
            sb.append(entry.getKey()).append("\n");
        }

        System.out.print(sb);
    }
}
