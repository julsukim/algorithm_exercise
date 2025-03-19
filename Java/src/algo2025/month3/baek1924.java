package algo2025.month3;
import java.io.*;
import java.util.*;

public class baek1924 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int month = Integer.parseInt(st.nextToken());
        int day = Integer.parseInt(st.nextToken());

        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] daysOfWeek = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

        int totalDays = day;
        for (int i=0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }

        String dayOfWeek = daysOfWeek[(totalDays - 1) % 7];

        System.out.println(dayOfWeek);
    }

}
