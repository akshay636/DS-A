const isPowerOfTwo = (n) => {
  if(n==1) return true
  else if(n>1) return isPowerOfTwo(n/2)
  else return false
  
}
console.log(isPowerOfTwo(128))