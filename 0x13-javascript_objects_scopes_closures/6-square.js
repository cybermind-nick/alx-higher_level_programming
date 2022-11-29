#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    if (char === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.height; col += 1) {
        console.log(char.repeat(this.width));
      }
    }
  }
};
