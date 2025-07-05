a = (
  x, y,
  e = w / 2 - y,
  d = noise(t + x / 190) / 8
    + noise(x / 30, y / 40 - t * 3) / 8
    + e * 0.002
) => [
  x,
  y / (6 + d * 9 + 2 * sin(t + e / 49)) - d * 90 + 100
];

s = 3;
t = 0;

draw = $ => {
  t || (
    createCanvas(w = 400, w),
    colorMode(HSB, 360, 100, 100, 100),
    noFill()
  );

  background(6);
  t += 0.01;

  for (y = 0; y < w; y += s) {
    for (x = 0; x < w; x += s) {
      let hueBase = 207 + 12 * sin(t * 2); // 在 165~185 之间摆动
      let b = 70 + 20 * sin((x + y) / 40); 
      stroke(hueBase, 80, b, 60);
      triangle(
        ...[a(x, y), a(x, y), a(x + s, y + s)].flat()
      );
    }
  }
};
