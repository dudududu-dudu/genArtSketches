def setup():
    global w, s, t
    size(500, 500)
    w = width
    s = 4
    t = 0
    colorMode(HSB, 360, 100, 100, 100)
    noFill()
    background(6)


def draw():
    global t
    background(6)
    t += 0.01

    for y in range(0, w, s):
        for x in range(0, w, s):
            hue_val = 230 + 12 * sin(t * 2)
            b = 70 + 20 * sin((x + y) / 40.0)
            stroke(hue_val, 80, b, 60)

            p1 = a(x, y)
            p2 = p1
            p3 = a(x + s, y + s)

            triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])


def a(x, y):
    e = w / 2.0 - y
    d = noise(t + x / 190.0) / 8.0 \
        + noise(x / 30.0, y / 40.0 - t * 3) / 8.0 \
        + e * 0.002

    new_x = x
    new_y = y / (6 + d * 9 + 2 * sin(t + e / 49.0)) - d * 90 + 100
    return (new_x, new_y)
