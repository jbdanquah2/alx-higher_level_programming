#!/usr/bin/node
if (process.argv[2] !== undefined && process.argv[2] !== null) {
  console.log(process.argv[2]);
} else {
  console.log('Arguments found');
}
