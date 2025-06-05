package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1706 {

    private static List<String> wordList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] puzzle = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                puzzle[i][j] = line.charAt(j);
            }
        }

        for (char[] line : puzzle) {
            getWords(line);
        }

        for (int c = 0; c < C; c++) {
            char[] line = new char[R];
            for (int r = 0; r < R; r++) {
                line[r] = puzzle[r][c];
            }
            getWords(line);
        }

        System.out.println(Collections.min(wordList));
    }

    private static void getWords(char[] line) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < line.length; i++) {
            if (line[i] == '#') {
                if (sb.length() > 1) {
                    wordList.add(sb.toString());
                }
                sb.setLength(0);
            } else {
                sb.append(line[i]);
            }
        }
        if (sb.length() > 1) {
            wordList.add(sb.toString());
        }
    }
}
