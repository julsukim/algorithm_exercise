const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function knapsack(N, M, items, taken) {
    // DP 테이블 초기화
    let dp = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));

    for (let i = 1; i <= N; i++) {
        let [weight, value] = items[i - 1];
        for (let w = 0; w <= M; w++) {
            if (weight <= w && !taken[i - 1]) {
                dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weight] + value);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // 최대 가치를 찾고, 선택된 아이템을 표시
    let max_value = dp[N][M];
    let w = M;
    for (let i = N; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            taken[i - 1] = true;
            w -= items[i - 1][0];
        }
    }

    return max_value;
}

function maxTotalValue(N, K, M, items) {
    // 보급품을 가치 대비 무게 비율로 정렬
    items.sort((a, b) => (b[1] / b[0]) - (a[1] / a[0]));
    let taken = Array(N).fill(false);

    let total_value = 0;
    for (let i = 0; i < K; i++) {
        total_value += knapsack(N, M, items, taken);
    }

    return total_value;
}

let index = 0;
let items = [];
let N, K, M;

rl.on('line', function(line) {
    if (index === 0) {
        [N, K, M] = line.split(' ').map(Number);
    } else {
        items.push(line.split(' ').map(Number));
    }
    index++
}).on('close', function () {
    // 최대 가치 계산
    const result = maxTotalValue(N, K, M, items);
    console.log(result);  // 결과 출력
})
