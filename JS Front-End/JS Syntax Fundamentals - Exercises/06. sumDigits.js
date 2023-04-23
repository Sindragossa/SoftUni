function sumDigits(number) {
    let numbers = number.toString();
    let sum = 0

    for (let i=0; i < numbers.length; i++){
        sum += parseInt(numbers[i])
    }
    console.log(sum)
}


sumDigits(245678)
