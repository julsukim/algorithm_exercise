package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek5635comparator {

    static class Man {
        String name;
        int day;
        int month;
        int year;

        public Man(String name, int day, int month, int year) {
            this.name = name;
            this.day = day;
            this.month = month;
            this.year = year;
        }

        @Override
        public String toString() {
            return name;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Man[] people = new Man[n];

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            people[i] = new Man(st.nextToken(),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(people, Comparator.comparing((Man m) -> m.year)
                .thenComparing(m -> m.month)
                .thenComparing(m -> m.day)
        );

        System.out.println(people[n-1]);
        System.out.println(people[0]);
    }
}