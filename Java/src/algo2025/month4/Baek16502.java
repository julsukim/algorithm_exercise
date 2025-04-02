package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek16502 {

    static final int N = 4;
    static Map<String, Integer> storeMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        storeMap.put("A", 0);
        storeMap.put("B", 1);
        storeMap.put("C", 2);
        storeMap.put("D", 3);

        double[][] transition = new double[N][N];

        StringTokenizer st;
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            String from = st.nextToken();
            String to = st.nextToken();
            double prob = Double.parseDouble(st.nextToken());
            transition[storeMap.get(to)][storeMap.get(from)] = prob;
        }

        double[] state = new double[N];
        Arrays.fill(state, 0.25);

        for (int t=0; t<T; t++) {
            double[] nextState = new double[N];
            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    nextState[i] += transition[i][j] * state[j];
                }
            }
            state = nextState;
        }

        for (double p : state) {
            System.out.printf("%.2f\n", p*100);
        }
    }
}
