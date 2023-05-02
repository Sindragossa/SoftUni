function cookByNumbers(number, op1, op2, op3, op4, op5) {
    number = Number(number);
    let arr = [op1, op2, op3, op4, op5];
    let operation = arr.shift();
    
    for (let i = 1; i <= 5; i++) {
        if (operation == 'chop'){
            number /= 2;
             
        } else if (operation == 'dice'){
            number = Math.sqrt(number);
             
        } else if (operation == 'spice') {
            number += 1;
           
        } else if (operation == 'bake') {
            number *= 3;
    
        } else if (operation == 'fillet') {
            number -= (number * 0.20);
                
        }

        operation = arr.shift()
        console.log(number)
    }

}