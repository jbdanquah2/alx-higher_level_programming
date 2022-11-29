#!/usr/bin/node
exports.callMeMoby = function callMeMoby (num, func) {
  while (num > 0) {
    func();
    num--;
  }
};
