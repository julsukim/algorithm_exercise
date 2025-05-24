package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek20006 {

    private static int nextId = 0;
    private static int P, M;
    private static StringBuilder sb;
    private static Map<String, Integer> playerInfo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        P = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        playerInfo = new HashMap<>();
        List<Room> roomInfo = new ArrayList<>();
        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            String name = st.nextToken();

            playerInfo.put(name, level);

            if (roomInfo.isEmpty()) {
                roomInfo.add(new Room(level, name));
                continue;
            }

            boolean hasFindRoom = false;
            for (Room r : roomInfo) {
                if (r.addPlayer(level, name)) {
                    hasFindRoom = true;
                    break;
                }
            }

            if (!hasFindRoom) roomInfo.add(new Room(level, name));
        }

        sb = new StringBuilder();
        for (Room r : roomInfo) {
            r.printRoomStatus();
        }
        System.out.println(sb);
    }

    private static class Room {
        int id, minLevel, maxLevel;
        int playerCount = 1;
        List<String> players = new ArrayList<>();

        public Room(int level, String name) {
            this.id = nextId++;
            this.minLevel = Math.max(level - 10, 1);
            this.maxLevel = level + 10;
            this.players.add(name);
            this.playerCount++;
        }

        public boolean addPlayer(int level, String name) {
            if (level < minLevel || level > maxLevel || playerCount > M) return false;
            this.players.add(name);
            this.playerCount++;
            return true;
        }

        public void printRoomStatus() {
            if (playerCount > M) {
                sb.append("Started!\n");
            } else {
                sb.append("Waiting!\n");
            }
            Collections.sort(players);
            for (String name : players) {
                sb.append(playerInfo.get(name)).append(" ").append(name).append("\n");
            }
        }
    }
}
