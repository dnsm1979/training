let name = "Василий"

console.log("Приветствуем, " + name);

let a = 4;
let b = 5;
let n = 6;
let r = 1;
let q = 9;

// найти наиболешее и наименьшее из имеющихся. вывести их на экран

let min = a;
let max = a;

if(min > b) {
	min = b;
}
if(min > n) {
	min = n;
}
if(min > r) {
	min = r;
}
if(min > q) {
	min = q;
} // для одиночной команды фигурные скобки не обязательны

// if el-if else
	
if(false) {}else if(false) {} else {} // выполняется только блок в котором сработало условие
 
console.log("минимальное значение: " + min);