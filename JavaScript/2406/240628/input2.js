const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = '';

rl.on('line', function (line) {
    // 입력된 줄을 하나의 문자열로 저장합니다.
    input = line;
}).on('close', function () {
    // 입력이 종료된 후에 결과를 처리합니다.
    const extractInitials = (input) => {
        // 문자열을 '-'로 분리하여 배열로 만듭니다.
        const words = input.split('-');
        
        // 각 단어의 첫 글자를 추출하여 새로운 배열을 만듭니다.
        const initials = words.map(word => word.charAt(0));
        
        // 추출된 첫 글자들을 합쳐서 문자열로 만듭니다.
        return initials.join('');
    };

    // 입력된 줄을 처리하여 결과 출력
    const output = extractInitials(input);
    console.log(output);
});
