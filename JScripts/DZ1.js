// 1
alert('Привет, ' + prompt('Ваше имя: '));

//2
const year = Number(prompt('Введите текущий год: '));
let b_yaer = Number(prompt('Ведите ваш год рождения: '));
alert('Ваш возрост: ' + (year - b_year));
 
 //3
let sq_size = Number(prompt('Ведите длинну стороны квадрата: '));
alert('Периметр квадрата состовляет: ' + (sq_size * 4));

//4
let r_size = Number(prompt('Ведите радиус окружности: '));
alert('Площадь окружности состовляет: ' + (r_size * Math.PI));

//5
let km_size = Number(prompt('Введите расстояние между городами (км): '));
let km_time = Number(prompt('Ведите время за которое нужно добраться (ч): '));
alert('Ваш скорость должна состовлять: ' + (km_size / km_time) + 'км/ч');

//6
const kv_dollor = Number(prompt('Введите курс доллора к евро: '));
let kv_col = Number(prompt('Введите сумму перевода: '));
alert('Ваша сумма состовляет: ' + (kv_dollor * kv_col) + ' евро');

//7
let gb_size = Number(prompt('Ведите объем флешки (Гб): '));
alert('На флешку объемом: ' + gb_size + 'влезет ' + Math.trunc((r_size * 2 ** 10 / 820)) + ' файла(ов)');

//8
let sm_money = Number(prompt('Введите количество денег в кошельке (руб): '));
let price_shoco = Number(prompt('Ведите сколько стоит шоколадка: '));
let col_shoco = Math.trunc((sm_money / price_shoco))
alert('Вы можете купть ' + col_shoco + ' шоколадок, и у вас останется ' + (sm_money - price_shoco * col_shoco) + ' рублей.');

//9
let num_x = Number(prompt('Ведите трехзначное число): '));
alert('Число задом на перед: ' + (num_x % 10) + Math.trunc(num_x / 10 % 10) + Math.trunc(num_x / 100));

//10
let num_int = Number(prompt('Ведите целое число): '));
if(num_int % 2 == 1){
	alert('Число: ' + num_int + ' является нечетным');
}
else{
	alert('Число: ' + num_int + ' является четным');
}
