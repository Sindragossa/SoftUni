function sameNumbers(number) {

    let numToString = number.toString();
    let allSame = true;
    let etalon = numToString[0];
    let numSum = 0

    for (let i = 0; i < numToString.length; i++) {

        if (etalon !== numToString[i]) {
            allSame = false;
        }

        numSum += numToString[i] * 1;
    }
    console.log(allSame);
    console.log(numSum);
}

sameNumbers(2222222)
sameNumbers(1234)