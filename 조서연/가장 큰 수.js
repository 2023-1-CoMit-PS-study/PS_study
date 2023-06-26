function solution(numbers) {
    //var answer = '';
    //console.log("hello");
    //console.log(parseInt(numbers[0].toString()[1]));
    /*
    var trial= numbers.length;
    while(trial){
    var max=0;
    var idx=0;
    for(var i=0; i<numbers.length;i++){
        if(parseInt(numbers[i].toString()[0])>max) {
            max=parseInt(numbers[i].toString()[0]);
            idx=i;
        }
        else if(parseInt(numbers[i].toString()[0])==max){
            if(numbers[i]==numbers[idx]){
                console.log("11");
                break;
            }
            else if(numbers[i].toString().length>numbers[idx].toString().length){
                for(var j=0;j< numbers[idx].toString().length;j++){
                    if (numbers[i][j]>numbers[idx][j]){
                        max=parseInt(numbers[i].toString()[0]);
                        idx=i;
                        console.log("22");
                    }
                    if (numbers[i][j]<numbers[idx][j]){
                        max=parseInt(numbers[idx].toString()[0]);
                        console.log("33");
                        idx=idx;
                    }
                    
                }
            }
            else{
                for(var j=0;j< numbers[i].toString().length;j++){
                    if (numbers[i][j]>numbers[idx][j]){
                        max=parseInt(numbers[i].toString()[0]);
                        idx=i;
                        console.log("44");
                    }
                    if (numbers[i][j]<numbers[idx][j]){
                        max=parseInt(numbers[idx].toString()[0]);
                        idx=idx;
                        console.log("55");
                    }
                    
                }
                
            }
        }
    }
        console.log(numbers[idx].toString());
    answer.concat(numbers[idx].toString());
    numbers.splice(idx,1);
    trial--;
    }
    
    return answer;
    */
    
    // 모든 number들을 string으로 바꿔주고 문자열을 그대로 연결한 수(b+a) - 바꿔 연결한 수(a+b)가 양수이면
    // ex) b(3) + a(30) - a(30) + b(3) => 330 - 303 = 양수
    // 3 30 순서를 그대로 유지한다.
    let answer = numbers
        .map((a) => String(a))
        .sort((a, b) => b + a - (a + b))
        .join('');

    return answer[0] === '0' ? '0' : answer;
    
    
}
