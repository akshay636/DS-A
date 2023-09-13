function fabonacci(n){ //without recursion
  let a=0;
  let b=1;
  let c;
 for(let i=1; i<=n; i++){
     console.log(a)
     c=a+b
     a=b
     b=c
 }
}
console.log(fabonacci(5))

function FaboWithRec(n){

}