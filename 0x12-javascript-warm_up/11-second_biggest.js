#!/usr/bin/node
let biggest;
let secondBiggest = 0;
if (process.argv.length > 2) {
  biggest = parseInt(process.argv[2]);
}

for (let i = 2; i < process.argv.length; i++) {
  if (biggest < parseInt(process.argv[i])) {
    biggest = parseInt(process.argv[i]);
  }
}
for (let j = 2; j < process.argv.length; j++) {
  if (secondBiggest < parseInt(process.argv[j]) && parseInt(process.argv[j]) !== biggest) {
    secondBiggest = parseInt(process.argv[j]);
  }
}
console.log(secondBiggest);
