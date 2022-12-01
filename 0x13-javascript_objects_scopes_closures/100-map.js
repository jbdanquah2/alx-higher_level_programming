#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((ele, idx) => ele * idx);
console.log(list);
console.log(newList);
