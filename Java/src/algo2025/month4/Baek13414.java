package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek13414 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        Map<String, Integer> idxMap = new LinkedHashMap<>();
        for (int i=0; i<L; i++) {
            String num = br.readLine();
            if (idxMap.containsKey(num)) {
                idxMap.remove(num);
            }
            idxMap.put(num, i);
        }

        StringBuilder sb = new StringBuilder();

        int count = 0;
        for (String e: idxMap.keySet()) {
            if (count == K) break;
            sb.append(e).append("\n");
            count++;
        }

        System.out.println(sb);
    }
}
