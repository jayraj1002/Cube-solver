import tkinter
import time
from color_input import *
import solver_2x2
import solver_3x3


colors = ['white', 'orange', 'green', 'red', 'blue', 'yellow']


class Square:
    def __init__(self, x, y, size, color, canvas):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.canvas = canvas
        #canvas.create_rectangle(320, 10, 370, 60, outline="black", fill="orange")
        #canvas.create_rectangle(370, 10, 420, 60, outline="black", fill="red")
        #canvas.create_rectangle(420, 10, 470, 60, outline="black", fill="white")
        #canvas.create_rectangle(470, 10, 520, 60, outline="black", fill="blue")
        #canvas.create_rectangle(520, 10, 570, 60, outline="black", fill="yellow")
        #canvas.create_rectangle(570, 10, 620, 60, outline="black", fill="green")

    def set_shape(self):
        return self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

    def change_color(self, event):
        i = colors.index(self.color)
        i += 1
        if i == len(colors):
            i = 0
        self.color = colors[i]
        self.set_shape()
        self.canvas.tag_bind(self.set_shape(), '<ButtonPress-1>', self.change_color)

    def index(j):
        print(j)

class VisualCube:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Cube Solver')
        self.window.resizable(0, 0)

        self.frame = tkinter.Frame(self.window, width=500, height=500)
        self.frame.pack()

        self.canvas = tkinter.Canvas(self.frame)

        self.x2 = tkinter.Button(self.frame, text='2x2', command=self.cube2)
        self.x2.pack()
        self.x3 = tkinter.Button(self.frame, text='3x3', command=self.cube3)
        self.x3.pack()
        #tkinter.Button(self.frame, text='white', command=Square.change_color(white,white)).pack

        tkinter.Button(self.frame, text='Solve', command=self.solve).pack()

        self.solution = tkinter.StringVar()
        tkinter.Label(self.frame, textvariable=self.solution).pack()

        self.error = tkinter.StringVar()
        self.label = tkinter.Label(self.frame, textvariable=self.error, fg='green')
        self.label.pack()

        self.err = True

        self.cube3()

    def cube2(self):
        self.cube = 2
        self.canvas.pack_forget()
        self.draw(70)

    def cube3(self):
        self.cube = 3
        self.canvas.pack_forget()
        self.draw(50)

    def solve(self):
        a = time.process_time()
        pos = get_pos(self.stickers, self.cube)
        if type(pos) == str:
            pass
        else:
            if self.cube == 2:
                cube = solver_2x2.Cube()
                cube.pos = pos
                solve = cube.optimal_solve()
                self.solution.set(' '.join(solve) + ' ({})'.format(len(solve)))
            if self.cube == 3:
                cube = solver_3x3.Cube()
                cube.corner_pos = pos[:8]
                cube.edge_pos = pos[8:]
                solve = cube.solve(12, 12)
                self.canvas = tkinter.Canvas(self.frame, width=800, height=800)
                self.canvas.pack()
                self.solution.set(' '.join(solve) + ' ({})'.format(len(solve)))
                ans=' '.join(solve) + ' ({})'.format(len(solve))
        b = time.process_time()
        self.label.config(fg='black')
        self.error.set('Run time: ' + str(b - a))
        print(ans)
        self.err = False

    def draw(self, size):
        self.canvas = tkinter.Canvas(self.frame, width=800, height=800)
        self.canvas.pack()

        squares = []
        cube = self.cube

        x = [cube*size, 0, cube*size, 2*cube*size, 3*cube*size, cube*size]
        y = [0, cube*size, cube*size, cube*size, cube*size, 2*cube*size]

        for n in range(6):
            for i in range(cube):
                for j in range(cube):
                    square = Square(x[n], y[n], size, colors[n], self.canvas)
                    self.canvas.tag_bind(square.set_shape(), '<ButtonPress-1>', square.change_color)
                    squares.append(square)
                    x[n] += size
                x[n] -= cube*size
                y[n] += size

        try:
            while True:
                self.window.update_idletasks()
                self.window.update()

                stickers = []

                key = ()
                if cube == 2:
                    key = (22, 19, 6, 0, 0, 0, 2, 8, 5, 0, 4, 17, 1, 16, 13, 3, 12, 9, 20, 7, 10, 21, 11, 14, 23, 15, 18)
                if cube == 3:
                    key = (49, 40, 13, 4, 22, 31, 6, 18, 11, 0, 9, 38, 2, 36, 29, 8, 27, 20, 45, 17, 24, 47, 26, 33, 53, 35,
                           42, 51, 44, 15, 7, 19, 3, 10, 1, 37, 5, 28, 46, 25, 50, 34, 52, 43, 48, 16, 21, 14, 41, 12, 39,
                           32, 23, 30)
                for n in key:
                    stickers.append([square.color for square in squares][n])

                if type(get_pos(stickers, cube)) == str and self.err:
                    self.label.config(fg='red')
                    self.error.set(get_pos(stickers, cube))
                elif self.err:
                    self.label.config(fg='green')
                    self.error.set('Valid scramble')
                try:
                    if self.stickers != stickers:
                        self.err = True
                        self.solution.set('')
                except:
                    pass
                self.stickers = stickers

        except tkinter.TclError:
            pass


if __name__ == '__main__':
    VisualCube()
