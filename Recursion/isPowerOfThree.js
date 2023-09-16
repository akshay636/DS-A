var isPowerOfThree = function(n) {
  if(n==1) return true
  else if(n>1) return isPowerOfThree(n/3)
  else return false
};
const ans = isPowerOfThree(0)
console.log(ans)
var isPowerOfThreeOpt = function(n) {
  if (n <= 0) {
    return false;
  }
  while (n > 1) {
    if (n % 3 !== 0) {
      return false;
    }
    n /= 3;
  }
  return true;
};
const ans1 = isPowerOfThreeOpt(7)
console.log(ans1)