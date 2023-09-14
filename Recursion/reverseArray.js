function revArray(arr, start, end){
  if(start >= end){
      return arr
  }
  let temp = arr[start]
   arr[start] = arr[end]
  arr[end] = temp
  return revArray(arr, start+1, end-1)
}
let ar =[1,2,3,4,5]
console.log(revArray(ar, 0, ar.length-1))