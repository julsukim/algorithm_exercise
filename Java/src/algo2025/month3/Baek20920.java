package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek20920 {

    static class Word implements Comparable<Word> {
        String word;
        int count;

        public Word(String word, int count) {
            this.word = word;
            this.count = count;
        }

        @Override
        public int compareTo(Word other) {
            int result = Integer.compare(other.count, count);
            if (result == 0) {
                result = Integer.compare(other.word.length(), word.length());
                if (result == 0) {
                    result = word.compareTo(other.word);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> counter = new HashMap<>();
        for (int i=0; i<n; i++) {
            String s = br.readLine();
            if (s.length() < m) continue;
            counter.put(s, counter.getOrDefault(s, 0) + 1);
        }

        List<Word> wordList = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            wordList.add(new Word(entry.getKey(), entry.getValue()));
        }

        Collections.sort(wordList);
        StringBuilder sb = new StringBuilder();
        for (Word word : wordList) {
            sb.append(word.word).append("\n");
        }
        System.out.println(sb.toString());
    }

}
