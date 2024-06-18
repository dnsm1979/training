//1
let hum_years = Number(prompt('Ведите сколько вам полных лет): '));
if(0 < hum_years && hum_years < 12){
	alert('Вы ребенок')
}
else if(12 <= hum_years && hum_years < 18){
	alert('Вы подросток');
}
else if(18 <= hum_years && hum_years < 60){
	alert('Вы взрослый');
}
else if(60 <= hum_years){
	alert('Вы пенсионер');
}

//2
let sym_num = Number(prompt('Ведите число от 1 до 9: '));
switch (sym_num) {
	case 1:
		alert( 'спецсимвол, который расположен на этой клавишей - !' );
    break;
	case 2:
		alert( 'спецсимвол, который расположен на этой клавишей - @' );
    break;
	case 3:
		alert( 'спецсимвол, который расположен на этой клавишей - #' );
    break;
	case 4:
		alert( 'спецсимвол, который расположен на этой клавишей - $' );
    break;
	case 5:
		alert( 'спецсимвол, который расположен на этой клавишей - %' );
    break;
	case 6:
		alert( 'спецсимвол, который расположен на этой клавишей - ^' );
    break;
	case 7:
		alert( 'спецсимвол, который расположен на этой клавишей - &' );
    break;
	case 8:
		alert( 'спецсимвол, который расположен на этой клавишей - *' );
    break;
	case 9:
		alert( 'спецсимвол, который расположен на этой клавишей - (' );
    break;
  default:
    alert( "Не корретный ввод!" );
}

//3
let num_z = Number(prompt('Ведите трехзначное число): '));
let num_1 = num_z % 10;
let num_2 = Math.trunc(num_z / 10 % 10);
let num_3 = Math.trunc(num_z / 100);
if(num_1 === num_2 || num_1 === num_3 || num_2 === num_3){
	alert('В числе есть одинаковые цифры!');
}
else{
	alert('В числе нет одинаковых цифр!');
}

//4
let year_check = Number(prompt('Ведите год): '));
if(year_check % 400 == 0 || year_check % 4 == 0 && year_check % 100 != 0){
	alert('Год високостный!');
}
else{
	alert('Год не високостный!');
}

//5
let num_z = Number(prompt('Ведите пятизначное число): '));
let num_1 = Math.trunc(num_z / 10000);
let num_2 = Math.trunc(num_z / 1000 % 10);
let num_4 = Math.trunc(num_z / 10 % 10);
let num_5 = num_z % 10;
if((num_1 == num_5) && (num_2 == num_4)){
    alert("Это число палиндром");
}
else {
    alert("Это число не палиндром");
}

//6
let col_dollor = Number(prompt('Введите количество доллоров для обмена: '));
let choise = Number(prompt('Выберете валюту для конвертации (1-EUR, 2-UAN, 3-AZN: '));
switch (choise) {
	case 1:
		alert('После конвертации у вас ' + (col_dollor * 0,93) +  ' EUR');
    break;
	case 2:
		alert('После конвертации у вас ' + (col_dollor * 7,25) +  ' UAN');
    break;
	case 3:
		alert('После конвертации у вас ' + (col_dollor * 1,70) +  ' AZN');
    break;
  default:
    alert( "Не корретный выбор валюты!" );
}

//7
let sum_dollor = Number(prompt('Введите количество доллоров для обмена: '));
let choise = Number(prompt('Выберете валюту для конвертации (1-EUR, 2-UAN, 3-AZN: '));
switch (choise) {
	case 1:
		alert('После конвертации у вас ' + (col_dollor * 0,93) +  ' EUR');
    break;
	case 2:
		alert('После конвертации у вас ' + (col_dollor * 7,25) +  ' UAN');
    break;
	case 3:
		alert('После конвертации у вас ' + (col_dollor * 1,70) +  ' AZN');
    break;
  default:
    alert( "Не корретный выбор валюты!" );
}

//8
let len_cir = Number(prompt('Ведите длинну окружности: '));
let per_sq = Number(prompt('Ведите периметр квадрата: '));
if((per_sq / 4) >= (len_cir / Math.PI)){
	alert('окружность поместиться в указанный квадрат!');
}
else{
	alert('окружность не поместиться в указанный квадрат!');
}

//9
let point = 0
let question_1 = Number(prompt('Когда состьоялась Битва при Ватерлоо? Ведите верный вариант ответа: 1-1815, 2-1915, 3-1715 '));
if(question_1 == 1) {
	point += 2;
}
else{
	point += 0;
}

let question_2 = Number(prompt('Когда состьоялась Бородинская битва? Ведите верный вариант ответа: 1-1812, 2-1815, 3-1795 '));
if(question_2 == 1) {
	point += 2;
}
else{
	point += 0;
}

let question_3 = Number(prompt('Когда состьоялась Курская битва? Ведите верный вариант ответа: 1-1943, 2-1944, 3-1941 '));
if(question_3 == 1) {
	point += 2;
}
else{
	point += 0;
}
alert('Вы набрали ' + point + ' очков');

//10
let ch_year = 0
let ch_meth = 0
let ch_day = 0
let data_year = Number(prompt('Ведите год: '));
let data_meth = Number(prompt('Ведите месяц: '));
let data_day = Number(prompt('Ведите день: '));
if(data_year % 400 == 0 || data_year % 4 == 0 && data_year % 100 != 0){
	ch_year += 1;
}
else{
	ch_year += 0;;
}
if(data_meth == 2 && data_year == 1){
	ch_meth += 29;
}
else if(data_meth == 2 && data_year == 0){
	ch_meth += 28;
}
else if(data_meth == 1 || data_meth == 3 || data_meth == 5 || data_meth == 7 || data_meth == 8 || data_meth == 10 || data_meth == 12){
	ch_meth += 31;
}
else{
	ch_meth += 30;
}
if(ch_meth == 28 && data_day == 28 || ch_meth == 29 && data_day == 29 || ch_meth == 30 && data_day == 30 || ch_meth == 31 && data_day == 31){
	ch_day = 1;
	data_day = 1;
}
else{
	data_day += 1;
}
if(ch_day == 1 && data_meth == 12){
	data_meth = 1;
	data_year += 1;
}
else if(ch_day == 1 && data_meth < 12){
	data_meth += 1;
	data_year += 1;
}
else{
	data_meth  += 0;
}
alert('Следущая дата после введенной: ' + data_day + '-' + data_meth + '-' + data_year);