function palindrome(s, start, end){
  if(start>=end){
    return true
  }
  if(s[start]!==s[end]){
    return false
  }
  return palindrome(s, start+1, end-1)
}
let s='NOON'
let a = s.length-1
console.log(palindrome(s,0,a))
