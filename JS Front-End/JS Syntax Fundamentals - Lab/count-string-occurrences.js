function countString(text, word) {
    let counter = 0;
    let words = text.split(' ');

    for (let el of words) {
        if (el === word) {
            counter += 1
        }
    }

    console.log(counter)

}