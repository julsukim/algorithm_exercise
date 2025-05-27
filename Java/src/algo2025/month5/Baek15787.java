package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek15787 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] trains = new boolean[N][20];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int order = Integer.parseInt(st.nextToken());
            int tNum = Integer.parseInt(st.nextToken());

            switch (order) {
                case 1: {
                    int sNum = Integer.parseInt(st.nextToken());
                    trains[tNum - 1][sNum - 1] = true;
                    break;
                }
                case 2: {
                    int sNum = Integer.parseInt(st.nextToken());
                    trains[tNum - 1][sNum - 1] = false;
                    break;
                }
                case 3: {
                    for (int s = 19; s > 0; s--) {
                        if (trains[tNum - 1][s - 1]) {
                            trains[tNum - 1][s] = true;
                        } else {
                            trains[tNum - 1][s] = false;
                        }
                        trains[tNum - 1][s - 1] = false;
                    }
                    break;
                }
                case 4: {
                    for (int s = 0; s < 19; s++) {
                        if (trains[tNum - 1][s + 1]) {
                            trains[tNum - 1][s] = true;
                        } else {
                            trains[tNum - 1][s] = false;
                        }
                        trains[tNum - 1][s + 1] = false;
                    }
                    break;
                }
            }
        }

        Set<String> posTrainSet = new HashSet<>();

        for (boolean[] status : trains) {
            posTrainSet.add(Arrays.toString(status));
        }

        System.out.println(posTrainSet.size());
    }
}
