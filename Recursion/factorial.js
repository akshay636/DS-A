function fact(n){
  if(n==0) return 1 //base case
  return n*fact(n-1) //n*n-1 is small calculation is fact(n-1) is recurisive call
}
console.log(fact(5))
