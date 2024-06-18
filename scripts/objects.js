let obj  = {
    name:"Joseph",
    age:18,
    id:1,
    SayGreetengs: function() {
        console.log("Hello, my name is ", this.name);
    },
};

let arr = [1, "2",];

console.log(arr);
console.log(obj);

console.log(obj.name);
console.log(obj["name"]);

obj?.surname;//  ?. - небезопасная проверка поля
if (obj?.surname === undefined); // проверка не гарантирует что можно работать с полем и проверку заполняемость поля и незаполненое поле дадут одинаковые результаты
if ("surname" in obj){
    console.log("surname exists in obj");
}else{
    console.log("surname not exists in obj");
}


console.log(obj);

obj.age = 31;
for (let vars in obj) {
    console.log(vars, ' ', obj[vars]);
    
}

let obj2 = {}; // Копирование объекта через цикл
for (let v in obj){
    obj2[v] = obj[v];
}
obj2.adress = {city:"Ekb", srteet:"Pushkin"};

let obj3 = {};
Object.assign(obj3, obj, obj2); // Копирование объекта через функцию

obj2.age = 18;

obj3.SayHello = function SeyHi(){console.log("Привет!");};

console.log(obj);
console.log(obj2);
console.log(obj3);
obj3.SayHello();
obj.SayGreetengs();