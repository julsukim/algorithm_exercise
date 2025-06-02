package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek2852 {

    // 시간 변환 및 연산을 위한 간단한 Time 클래스
    static class Time {
        int totalSeconds;

        Time(String mmss) {
            String[] parts = mmss.split(":");
            int min = Integer.parseInt(parts[0]);
            int sec = Integer.parseInt(parts[1]);
            this.totalSeconds = min * 60 + sec;
        }
        Time(int totalSeconds) {
            this.totalSeconds = totalSeconds;
        }

        // 두 시각의 차이 구하기
        int diff(Time other) {
            return this.totalSeconds - other.totalSeconds;
        }

        // MM:SS 포맷으로 변환
        String format() {
            int min = totalSeconds / 60;
            int sec = totalSeconds % 60;
            return String.format("%02d:%02d", min, sec);
        }
    }

    // 득점 이벤트
    static class ScoreEvent implements Comparable<ScoreEvent> {
        int team; // 1 또는 2
        Time time;

        ScoreEvent(int team, String mmss) {
            this.team = team;
            this.time = new Time(mmss);
        }

        @Override
        public int compareTo(ScoreEvent o) {
            return Integer.compare(this.time.totalSeconds, o.time.totalSeconds);
        }
    }

    // 경기 전체 로직
    static class Game {
        static final int DURATION = 48 * 60; // 48분
        List<ScoreEvent> events = new ArrayList<>();
        int[] scores = new int[3]; // [0] dummy, [1]팀1, [2]팀2
        int[] leadTime = new int[3]; // 리드 시간 [0] dummy, [1]팀1, [2]팀2

        // 이벤트 추가
        void addEvent(int team, String mmss) {
            events.add(new ScoreEvent(team, mmss));
        }

        // 전체 시뮬레이션
        void simulate() {
            Collections.sort(events); // 혹시 시간 순 정렬이 필요할 수 있음
            int currLeader = 0; // 0:무승부, 1:팀1, 2:팀2
            Time lastTime = new Time(0);

            for (ScoreEvent event : events) {
                // 직전 리더가 있는 경우, 지난 구간의 리드 시간 누적
                if (currLeader != 0) {
                    leadTime[currLeader] += event.time.diff(lastTime);
                }

                // 점수 갱신
                scores[event.team]++;
                // 리더 변경
                if (scores[1] > scores[2]) currLeader = 1;
                else if (scores[2] > scores[1]) currLeader = 2;
                else currLeader = 0;

                lastTime = event.time;
            }
            // 마지막 득점 이후부터 경기 종료까지 리드 시간 누적
            Time endTime = new Time(DURATION);
            if (currLeader != 0) {
                leadTime[currLeader] += endTime.diff(lastTime);
            }
        }

        // 결과 출력
        void printResult() {
            System.out.println(new Time(leadTime[1]).format());
            System.out.println(new Time(leadTime[2]).format());
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Game game = new Game();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int team = Integer.parseInt(st.nextToken());
            String time = st.nextToken();
            game.addEvent(team, time);
        }
        game.simulate();
        game.printResult();
    }
}
