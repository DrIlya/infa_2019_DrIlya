from graph import *


def bird1(X, Y, s):
    """Draw a bird with the coordinates of the lowest point: X, Y.
    s is the relative size parameter.
    Type(X) = float
    Type(Y) = float
    Type(s) = float
    Normal values of parameters: 0 <= X <= 1000
                                 0 <= Y <= 600
                                 0 < s < ~4

    """
    brushColor(64, 27, 3)
    penColor(64, 27, 3)
    polygon([(X, Y), (X + s * 20, Y - s * 10), (X + 11 * s, Y - 9 * s), (X + 6 * s, Y - 7 * s), (X, Y - 1 * s),
             (X - 7 * s, Y - s * 8), (X - s * 13, Y - 10 * s), (X - s * 14, Y - s * 8), (X, Y)])


def bird2(X, Y, s):
    """Draw another bird (with raised wings) with the coordinates of the lowest point: X, Y.
    s is the relative size parameter.
    Type(X) = float.
    Type(Y) = float.
    Type(s) = float.
    Normal values of parameters: 0 <= X <= 1000
                                 0 <= Y <= 600
                                 0 < s < ~4

    """
    brushColor(64, 27, 3)
    penColor(64, 27, 3)
    polygon([(X, Y), (X + s * 18, Y - s * 17), (X + 9 * s, Y - 14 * s), (X + 5 * s, Y - 10 * s), (X, Y - 1 * s),
             (X - 6 * s, Y - s * 11), (X - s * 11, Y - 15 * s), (X - s * 12, Y - s * 13), (X, Y)])


# workspace size settings
windowSize(1000, 600)
canvasSize(1000, 600)

# background settings
penSize(0)
brushColor(254, 214, 163)
rectangle(0, 0, 1000, 140)
brushColor(254, 214, 197)
rectangle(0, 140, 1000, 280)
brushColor(254, 214, 149)
rectangle(0, 280, 1000, 480)
brushColor(252, 239, 27)
circle(500, 150, 60)
penColor(190, 140, 160)
brushColor(180, 135, 149)
polygon([(0, 430), (1000, 400), (1000, 600), (0, 600), (0, 430)])
brushColor(252, 153, 45)
penColor(252, 153, 45)
polygon([(10, 340), (1000, 250), (950, 215), (920, 225), (900, 195), (870, 200), (820, 110), (800, 110), (750, 180),
         (680, 220), (635, 225), (610, 255), (565, 240), (515, 290), (490, 260), (430, 270), (300, 170), (280, 140),
         (240, 130), (70, 285), (15, 300), (10, 340)])
penColor(173, 65, 49)
brushColor(173, 65, 49)
polygon([(0, 430), (1000, 400), (1000, 270), (960, 320), (930, 315), (910, 335), (880, 318), (845, 355), (740, 290),
         (670, 290), (580, 355), (470, 380), (400, 340), (300, 325), (260, 385), (205, 350), (155, 410), (135, 315),
         (100, 295), (70, 300), (30, 365), (0, 345), (0, 430), ])
brushColor(44, 7, 33)
penColor(44, 7, 33)
polygon([(0, 380), (105, 390), (190, 470), (270, 560), (275, 565), (279, 569), (284, 574), (290, 578), (295, 580),
         (303, 582), (310, 584), (318, 586), (325, 588), (335, 589), (450, 590), (620, 520), (680, 550), (720, 560),
         (728, 561), (732, 562), (736, 562), (750, 560), (755, 558), (760, 555), (765, 550), (890, 430), (930, 400),
         (950, 390), (980, 380), (1000, 380), (1000, 600), (0, 600), (0, 380)])

BIRD = [420, 250, 2, 510, 280, 1.8, 430, 340, 2, 510, 320, 1.8, 620, 430, 2.2, 670, 470, 1.6,
        790, 460, 1.4, 760, 510, 2.5]

for i in range(8):
    bird1(BIRD[i * 3], BIRD[i * 3 + 1], BIRD[i * 3 + 2])

run()
