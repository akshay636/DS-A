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

function fiboWithRec(n){
if(n<2){
  return n
}else{
  return fiboWithRec(n-1)+fiboWithRec(n-2)
}
}
for(let i=0; i<5; i++){
  console.log(fiboWithRec(i))
}