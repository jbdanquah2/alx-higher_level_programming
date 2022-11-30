#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c=undefined) {
      for (let i = 0; i < this.height; i++) {
        if (c !== undefined){
          console.log(`${c}`.repeat(this.width));
        } else {
          console.log(`x`.repeat(this.width));
        }      
      }
    }
}
module.exports = Square;
