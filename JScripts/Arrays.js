let arr = [];

arr.push(120);
arr[arr.length] = "value";
arr = arr.concat([true, "new_string"]);
arr.push("12");

for (let element of arr) {
    console.log(element);
    if (element == 12) {
        console.log("we found 12");
    }
}

let founded = [];
for (let index = 0; index < arr.length; index++) {
    if (arr[index] == 12) {
        founded.push(index);
    }
}

for (const el of founded) {
    console.log("id:", el, " val:", arr[el]);
}

console.log(arr.indexOf(12));

for (let index = arr.length - 1; index >= 0; index--) {
    console.log(arr[index]);

}

arr.shift();
console.log("\n");
for (let element of arr) {
    console.log(element);
    if (element == 12) {
        console.log("we found 12");
    }
}
console.log("\n");
console.log("\n");


