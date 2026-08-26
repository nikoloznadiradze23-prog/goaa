function fibo(n){
    let seq = [0, 1];
    for(let i = 0; i < n; i++) {
        console.log(seq[-1])
        let newElem = seq[-1] + seq[i-2];
        seq.push(fibo(7))
    };
    return seq;
}
console.log(fibo(7))