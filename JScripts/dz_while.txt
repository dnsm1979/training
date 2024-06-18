//Задания, в которых необходимо использовать WHILE
// 1
let input_num = Number(prompt('Введите количество повторений символоа #: '));
while (input_num) {
    alert( '#' );
    input_num--;
}

//2
let input_num2 = Number(prompt('Введите число: '));
while (input_num2) {
    alert( input_num2 );
    input_num2--;
}

//3
let temp_num = 1;
let input_num3 = Number(prompt('Введите число '));
let input_step = Number(prompt('Введите степень '));
while (input_step) {
    temp_num  = temp_num * input_num3;
    input_step--;
    
}
alert(temp_num);

//4
let temp_num4 = [];
let temp_spep4 = 0;
let input_num4 = Number(prompt('Введите число1 '));
let input_num4_2 = Number(prompt('Введите число2 '));
if (input_num4 < input_num4_2) {
    temp_spep4 = input_num4;
}
else{
    temp_spep4 = input_num4_2;
}
while (temp_spep4) {
    if (input_num4 % temp_spep4 == 0 & input_num4_2 % temp_spep4 == 0) {
        temp_num4.push(temp_spep4);
    }
    temp_spep4--;
    
}
alert(temp_num4);

//5
let input_num5 = Number(prompt('Введите число '));
let input_step5 = input_num5 -1;
let temp_num5 = input_num5;
while (input_step5) {
    temp_num5  = temp_num5 * input_step5;
    input_step5--;
    
}
alert(temp_num5);

//Задания, в которых необходимо использовать DO WHILE.
//1

do {
    let input_result = Number(prompt('Введите ответ на вырожение: 2 + 2 * 2 '));
    if (input_result == 6) {
        break;
    }
    alert('Неверно! Попробуйте еще раз!')
} while(true);
alert('Верно!');

//2
let num_div = 1000
let s = 0
do {
    num_div /= 2;
    s++;
    if (num_div < 50){
        break;
    }

} while(true);
alert('Было произведенено ' + s + ' делений, очтаток: ' + num_div);

//Задания, в которых необходимо использовать FOR.
//3
let resul_num = [];
let input_num6 = Number(prompt('Введите число '));
for (let index = 1; index < 101; index++) {
    if (index % input_num6 === 0){
        resul_num.push(index);
    }
    
}
alert('Числа кратные ' + input_num6 + ': ' + resul_num);

//4
let four_elements = [];
let input_num_start = Number(prompt('Введите начальное число диапозона '));
let input_num_end = Number(prompt('Введите конечное число диапозона '));
for (let index = input_num_start - 1; index < input_num_end + 1; index+=4) {
    four_elements.push(index);
    
}
alert('Каждые 4 числа диапозона: ' + four_elements);

//5
num_res = [];
let input_num7 = Number(prompt('Введите число '));
for (let index = 0; index < input_num7 + 1; index++) {
    if (input_num7 % index === 0){
        num_res.push(index);
    }
    
}
if (num_res.length  > 2){
    alert('Число ' + input_num7 + ' не простое!');
}
else {
    alert('Число ' + input_num7 + ' простое!');
}