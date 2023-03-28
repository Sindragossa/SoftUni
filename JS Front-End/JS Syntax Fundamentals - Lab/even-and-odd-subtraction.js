function solve(arr) {

    let sumOdd = 0;
    let sumEven = 0;

    for(let i = 0; i < arr.length; i++) {
        num = Number(arr[i]);

        if (num % 2 == 0) {
            evenSum += num;
        } else {
            sumOdd += num;
        }
    }

    let result = sumEven - sumOdd

    console.log(result)
}