package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek5635comparable {

    static class Man implements Comparable<Man> {
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
        public int compareTo(Man other) {
            int result = Integer.compare(this.year, other.year);

            if (result == 0) {
                result = Integer.compare(this.month, other.month);
                if (result == 0) {
                    result = Integer.compare(this.day, other.day);
                }
            }

            return result;
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

        Arrays.sort(people);
        System.out.println(people[n-1]);
        System.out.println(people[0]);
    }
}