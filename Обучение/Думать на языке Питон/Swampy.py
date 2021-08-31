from swampy.Gui import *

g = Gui()
g.title('')


def draw_circle(colour=None):
    canvas.circle([0, 0], 100, fill=colour)


def change_colour():
    colour = entry.get()
    print(dir(entry))
    canvas.circle([0, 0], 100, fill=colour)


canvas = g.ca(width=500, height=500)
canvas.config(bg='cyan')

draw_circle = g.bu(text='Draw circle', command=draw_circle)
circle_colour = g.bu(text='Change colour', command=change_colour)

entry = g.en()

g.mainloop()


def test():
    canvas.rectangle([[0, 0], [200, 100]], fill='blue', outline='orange', width=10)
    canvas.oval([[0, 0], [200, 100]], outline='orange', width=10)
    canvas.line([[0, 100], [100, 200], [200, 100]], width=10)
    canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='red', outline='orange', width=10)
    entry = g.en(text='text')
    entry.get()
    text = g.te(width=100, height=5)
    text.insert(END, 'Inserted text')
    text.insert(1.0, 'nother')
    text.get(0.0, END)