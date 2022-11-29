#!/usr/bin/node
const firstArg = process.argv[2];
if (!isNaN(firstArg)) {
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log('X'.repeat(parseInt(firstArg)));
  }
} else {
  console.log('Missing size');
}
