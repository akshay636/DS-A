//Count Ways To Reach The N-th Stairs
//You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair. 
//Each time you can either climb one step or two steps.
//You are supposed to return the number of distinct ways in which you can climb from the 0th step to Nth step.

function nthStair(n){
  if(n==1 || n==2) return n
  return nthStair(n-1)+nthStair(n-2)
}
console.log(nthStair(5))
// to overcome time limit excede
//recursive
var climbStairs = function(n) {
  const memo = new Array(n + 1);

  const climb = (n) => {
      if (n === 1 || n === 2) return n;
      if (memo[n]) return memo[n];
      memo[n] = climb(n - 1) + climb(n - 2);
      return memo[n];
  };

  return climb(n);
};
//iterative method
var climbStairs = function(n) {
  if (n <= 2) return n;

  let prev1 = 1; // Number of ways to climb 1 stair
  let prev2 = 2; // Number of ways to climb 2 stairs

  for (let i = 3; i <= n; i++) {
      const current = prev1 + prev2;
      prev1 = prev2;
      prev2 = current;
  }

  return prev2;
};
