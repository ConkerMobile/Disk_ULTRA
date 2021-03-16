from turtle import *
from random import *
color('magenta', 'black')
begin_fill()
while True:
    forward(200)
    left(140)
    pu()
    forward(20)
    pd()
    if abs(pos()) < 1:
        break
end_fill()
done()
