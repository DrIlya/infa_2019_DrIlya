from graph import *

windowSize(1000, 600)
canvasSize(1000, 600)
penSize(0)
brushColor(255, 208, 160)
rectangle(0, 0, 1000, 140 )
brushColor(255, 218, 210)
rectangle(0, 140, 1000, 280 )
brushColor(255, 218, 170)
rectangle(0, 280, 1000, 480 )
brushColor("yellow")
circle(500, 150, 60)
penColor(190, 140, 160)
brushColor(190, 140, 160)
polygon( [(0, 430), (1000, 400), (1000, 600), (0,600), (0, 430)] )
brushColor(255, 160, 26)
penColor(255, 183, 26)
polygon( [(10, 340), (1000, 250), (950,215), (920,225), (900, 195), (870, 200), (820, 110), (800, 110), (750, 180 ), (680,220 ),(635,225 ),(610,255 ), (565,240 ),(515,290),(490,260 ),(430,270 ),(300,170 ),(280,140 ),(240,130 ),(70,285 ),(15,300 ),(10, 340)] )
penColor(170, 70, 60)
brushColor(170, 70, 60)
polygon( [(0, 430),(1000, 400),(1000,270),(960,320),(930,315),(910,335),(880,318),(845,355),(740,290),(670,290),(580,355),(470,380),(400,340),(300,325),(260,385),(205,350),(155,410),(135,315),(100,295),(70,300),(30,365),(0,345),(0,430), ] )

run()