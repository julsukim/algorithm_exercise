package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek17219 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, String> passwords = new HashMap<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            passwords.put(st.nextToken(), st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            String site = br.readLine();
            sb.append(passwords.get(site)).append("\n");
        }

        System.out.println(sb.toString());
    }
}
