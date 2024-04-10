#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
	  if (width <= 0 || height <= 0 || Number.isInteger(width) === false|| Number.isInteger(height) === false) {
		  return {}
	  }
	  this.width = width;
	  this.height = height;
}
}

module.exports = Rectangle;
