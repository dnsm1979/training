
let fun;

function F00(){
    console.log("message");
    fun = function InnerFunc(){
        console.log("inner message");
    }
    fun();
}//

F00();
fun();

function Name(a, b){
    console.log(a, ' ', b);
}

Name();
Name(NaN, "hds");


(a, b) => a + b;
const lamb = (a, b) => {return a + b};

console.log(lamb([1,2,3,4], 3));

