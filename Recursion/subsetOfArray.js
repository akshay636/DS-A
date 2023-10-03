let ans = [];

function helpers(arr, temp, i) {
  if (i === arr.length) {
    ans.push([...temp]);
    return;
  }
  temp.push(arr[i]);
  helpers(arr, temp, i + 1);
  temp.pop();
  helpers(arr, temp, i + 1);
}

let temp = [];
let arr = [1, 2, 3];
helpers(arr, temp, 0);
console.log(ans);