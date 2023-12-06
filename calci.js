// console.log("Hello, world!");
const prompt=require("prompt-sync")({sigint:true}); 

function Addition(a,b){
    result = a + b;
    return result
}
function substration(a,b){
    result = a - b;
    return result
}
function multiplication(a,b){
    result = a * b;
    return result
}
function Divion(a,b){
    result = a / b;
    return result
}

let i=1
while (i>0){
var user=parseInt(prompt("enter the first Number:- "));
var opertion=prompt("enter the option 1.Addition:-+ \n 2.substration:-- \n3.multiplication:-* \n4.Divion \n:-");
var user1=parseInt(prompt("enter the second Number:- "));
if(opertion == "+"){
        ans = Addition(user,user1);
    }
else if(opertion == "-"){
    ans =substration(user,user1);
    }
else if(opertion == "*"){
    ans =multiplication(user,user1);
    }
else if(opertion == "/"){
    ans =Divion(user,user1);
    }
console.log(user, opertion , user1 ,'=',ans);
}







