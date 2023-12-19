// console.log("Hello, world!");
const prompt=require("prompt-sync")({sigint:true}); 

answer=[]

function Addition(a,b){
    result = a + b;
    answer.push(result);
    his = ([a, '+' , b ,'=',result]);
    history.push(his);
    
    return result
}
function substration(a,b){
    result = a - b;
    answer.push(result);
    his = ([a, '-' , b ,'=',result]);
    history.push(his)
    return result
}
function multiplication(a,b){
    result = a * b;
    answer.push(result);
    his = ([a, '*' , b ,'=',result]);
    history.push(his)
    return result
}
function Divion(a,b){
    result = a / b;
    answer.push(result);
    his = ([a, '/' , b ,'=',result]);
    history.push(his)
    return result
}



// fib = [0,1]
// def fib_seq(value):
//     while len(fib) < value:
//         fib.append(fib[-1] + fib[-2])
//     print(fib)
//     return fib

// def prime_number(value):
//     for i in range(2, int(value/2)+1):
//         if (value % i) == 0 :
//             print(f"{value} Number is Not Prime")
//             break
//     else:
//         print(f"This is prime Number {value}")
// import math
// def Armstrong(value):
//     sum = 0
//     t1 = value
//     while t1 > 0:
//         digit = t1 % 10
//         sum += digit ** 3
//         t1 //= 10
//     if value == sum:
//         print(f"{value} is an Armstrong number")
//     else:
//         print(f"{value} is not an Armstrong number")

// def numIssqre(value):
//     val = int(math.sqrt(value))
//     return ((val*val) == value)


history = [];
function main(){
let i=1
var j =0;
while (i>0){
var user=parseInt(prompt("enter the first Number:- "));
var opertion=prompt("enter the option\n 0.Exit:-\n 1.Addition:-+ \n 2.substration:-- \n3.multiplication:-* \n4.Divion \n5.History  \n6.clear_History:-");
var user1=parseInt(prompt("enter the second Number:- "));
if(opertion == "0"){
    break;
}
else if(opertion == "5"){
    console.log(history)
}
else if(opertion == "6"){
    console.log(history.length);
    for(let i=0;i<=history.length+1;i++){
        new1 = history.pop();
        // console.log(new1);
        console.log(i);
        }
       console.log(history) 
}
else if(opertion == "+"){
        ans = Addition(user,user1);
        console.log(user, opertion , user1 ,'=',ans);
    }
else if(opertion == "-"){
    ans =substration(user,user1);
    console.log(user, opertion , user1 ,'=',ans);
    }
else if(opertion == "*"){
    ans =multiplication(user,user1);
    console.log(user, opertion , user1 ,'=',ans);
    }
else if(opertion == "/"){
    ans =Divion(user,user1);
    console.log(user, opertion , user1 ,'=',ans);
    }

var Ucondition=prompt(" Do you want to contiune for the Old value YES/NO :- ");
console.log(Ucondition);
if(Ucondition == "yes"){
    var k = 0;
    while(k=="0"){
    var opertion1=prompt("enter the option:-\n 0.Exit:-\n 1.Addition:-+ \n 2.substration:-- \n3.multiplication:-* \n4.Divion:-");
    var user2=parseInt(prompt("enter the second Number:- "));
    oldvalue = answer[j];
    console.log(oldvalue);
    console.log(answer);
    j+=1;
    if(opertion1 == '0'){
        break;
    }
    else if(opertion1 == "+"){
        res = Addition(oldvalue,user2);
        console.log(oldvalue, opertion1 , user2 ,'=',res);
    }
    else if(opertion1 == "-"){
        res =substration(oldvalue,user2);
        console.log(oldvalue, opertion1 , user2 ,'=',res);
        }
    else if(opertion1 == "*"){
        res =multiplication(oldvalue,user2);
        console.log(oldvalue, opertion1 , user2 ,'=',res);
        }
    else if(opertion1 == "/"){
        res =Divion(oldvalue,user2);
        console.log(oldvalue, opertion1 , user2 ,'=',res);
    }
}
}
// else{
//     break;
// }
}
}
main()
// var i = 0
// while(i == "0"){
//     main()
// }











// user_input = parseInt(prompt("enter the number:-"))
function check_isSquare(user_input){
    if(Number.isInteger(Math.sqrt(user_input))){
        console.log('Number is isSquare')
        
    }
    else{
        console.log("Number is not isSquare")
    }

}
// check_isSquare(user_input)

// Pythagoras Triples Formula

// p = parseInt(prompt("enter the 1st number :-"))
// q = parseInt(prompt("enter the 2nd number:-"))

// p1 = p * p
// q1 = q * q
// r1 = p1 + q1
// console.log(p1 , '+', q1 ,'=', r1)


