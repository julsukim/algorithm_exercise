package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1302TreeMap {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Map<String, Integer> books = new TreeMap<>();
        for (int i=0; i<N; i++) {
            String title = br.readLine();
            books.put(title, books.getOrDefault(title, 0) + 1);
        }

        String maxTitle = "";
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : books.entrySet()) {
            String title = entry.getKey();
            int count = entry.getValue();
            if (count > maxCount) {
                maxTitle = title;
                maxCount = count;
            }
        }

        System.out.println(maxTitle);
    }
}
