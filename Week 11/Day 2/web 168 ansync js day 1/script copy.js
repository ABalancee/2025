// Async in JS
/** Callback **/

setTimeout(() => {
  console.log('hi');
}, 5 * 1000); // wartet 5 Sekunden

function getX() {
  setTimeout(() => {
    return 5;
  }, 2000);
}

function getY() {
  return 6;
}

function getXY() {
  let x = getX();
  console.log('x =', x);

  let y = getY();
  console.log('y =', y);

  let sum = x + y;
  console.log('sum =', sum);
}

// getXY(); // auskommentiert
A