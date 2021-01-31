xPos = 200;
yPos = 200;

factor = 10;

function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
}

function draw() {
  deltaX = (mouseX - xPos)/factor;
  deltaY = (mouseY - yPos)/factor;

  xPos += deltaX;
  yPos += deltaY;

  background(220);
  ellipse(xPos, yPos, 50, 50);
}

function mouseReleased() {
  xPos = mouseX;
  yPos = mouseY;
}
