#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[i] = list[j];
    j++;
  }
  console.log(newList);
  return newList;
};
