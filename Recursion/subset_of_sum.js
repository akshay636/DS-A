function sumset(arr, sum, tempsum, i){
  if(i==tempsum){
    return true;
  }
  if(i>=arr.length-1){
    return false
  }
  let rec1 = sumset(arr, sum, tempsum+arr[i], i+1)
  let rec2 = sumset(arr, sum, tempsum, i+1)
  return rec1 || rec2
   
}