// console.log("Hello, world!");
const prompt=require("prompt-sync")({sigint:true}); 
var user=parseInt(prompt("enter the first Number:- "));
var opertion=prompt("enter the option 1.Addition:-+ \n 2.substration:-- \n3.multiplication:-* \n4.Divion \n:-");
var user1=parseInt(prompt("enter the second Number:- "));
// console.log(user);
// console.log(opertion);
// console.log(user1);
let ans
if(opertion == "+"){
    ans = user + user1;
}
else if(opertion == "-"){
    ans = user - user1
}
else if(opertion == "*"){
    ans = user * user1
}
else if(opertion == "/"){
    ans = user / user1
}
console.log(user, opertion , user1 ,'=',ans);