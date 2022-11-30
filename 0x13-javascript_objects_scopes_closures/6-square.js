#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = undefined) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(`${c}`.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
