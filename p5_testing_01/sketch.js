import { createSecurePair } from "tls";

function setup() {
    createCanvas(400, 400);
}
  
  function draw() {
    background(220);
    smooth();
    createP('A Circle');
    ellipse(width/2, height/2, 80);
}