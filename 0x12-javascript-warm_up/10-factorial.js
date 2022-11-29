#!/usr/bin/node
const firstArg = process.argv[2];

function fact (n) {
  if (parseInt(n) > 1) {
    return parseInt(n) * fact(parseInt(n) - 1);
  }
  return 1;
}

console.log(fact(firstArg));
