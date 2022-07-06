import time


def inverse_alg(alg):
    inverse = []

    for n in reversed(alg):
        if n[-1] == '2':
            inverse.append(n)
        elif len(n) == 1:
            inverse.append(n + "'")
        else:
            inverse.append(n[0])
    return inverse


def shorten_alg(alg):
    if len(alg) < 2:
        return alg
    if alg[0][0] != alg[1][0]:
        return [alg[0]] + shorten_alg(alg[1:])
    if alg[0] == alg[1] and alg[0][-1] == '2' or alg[0] + "'" == alg[1] or alg[0] == alg[1] + "'":
        move = []
    elif alg[0] == alg[1]:
        move = [alg[0][0] + '2']
    elif len(alg[0]) == len(alg[1]):
        move = [alg[0][0]]
    else:
        move = [alg[0][0] + "'"]
    return shorten_alg(move + alg[2:])


class Cube:
    def __init__(self, pos0=0, pos1=3, pos2=6, pos3=9, pos4=12, pos5=15, pos6=18):
        self.pos = [pos0, pos1, pos2, pos3, pos4, pos5, pos6]

    def is_solved(self):
        return self.pos == [0, 3, 6, 9, 12, 15, 18]

    def is_oriented(self):
        for n in self.pos:
            if n % 3 != 0:
                return False
        return True

    def U(self):
        a = self.pos[0]
        b = self.pos[1]
        c = self.pos[2]
        d = self.pos[3]
        self.pos[0] = d
        self.pos[1] = a
        self.pos[2] = b
        self.pos[3] = c

    def Ui(self):
        a = self.pos[0]
        b = self.pos[1]
        c = self.pos[2]
        d = self.pos[3]
        self.pos[0] = b
        self.pos[1] = c
        self.pos[2] = d
        self.pos[3] = a

    def U2(self):
        a = self.pos[0]
        b = self.pos[1]
        c = self.pos[2]
        d = self.pos[3]
        self.pos[0] = c
        self.pos[1] = d
        self.pos[2] = a
        self.pos[3] = b

    def R(self):
        a = self.pos[3]
        b = self.pos[2]
        c = self.pos[6]
        d = self.pos[5]
        self.pos[3] = (d // 3 * 3) + ((d - 1) % 3)
        self.pos[2] = (a // 3 * 3) + ((a + 1) % 3)
        self.pos[6] = (b // 3 * 3) + ((b - 1) % 3)
        self.pos[5] = (c // 3 * 3) + ((c + 1) % 3)

    def Ri(self):
        a = self.pos[3]
        b = self.pos[2]
        c = self.pos[6]
        d = self.pos[5]
        self.pos[3] = (b // 3 * 3) + ((b - 1) % 3)
        self.pos[2] = (c // 3 * 3) + ((c + 1) % 3)
        self.pos[6] = (d // 3 * 3) + ((d - 1) % 3)
        self.pos[5] = (a // 3 * 3) + ((a + 1) % 3)

    def R2(self):
        a = self.pos[3]
        b = self.pos[2]
        c = self.pos[6]
        d = self.pos[5]
        self.pos[3] = c
        self.pos[2] = d
        self.pos[6] = a
        self.pos[5] = b

    def F(self):
        a = self.pos[0]
        b = self.pos[3]
        c = self.pos[5]
        d = self.pos[4]
        self.pos[0] = (d // 3 * 3) + ((d - 1) % 3)
        self.pos[3] = (a // 3 * 3) + ((a + 1) % 3)
        self.pos[5] = (b // 3 * 3) + ((b - 1) % 3)
        self.pos[4] = (c // 3 * 3) + ((c + 1) % 3)

    def Fi(self):
        a = self.pos[0]
        b = self.pos[3]
        c = self.pos[5]
        d = self.pos[4]
        self.pos[0] = (b // 3 * 3) + ((b - 1) % 3)
        self.pos[3] = (c // 3 * 3) + ((c + 1) % 3)
        self.pos[5] = (d // 3 * 3) + ((d - 1) % 3)
        self.pos[4] = (a // 3 * 3) + ((a + 1) % 3)

    def F2(self):
        a = self.pos[0]
        b = self.pos[3]
        c = self.pos[5]
        d = self.pos[4]
        self.pos[0] = c
        self.pos[3] = d
        self.pos[5] = a
        self.pos[4] = b

    def alg(self, moves):
        for n in moves:
            if n == 'U':
                self.U()
            elif n == "U'":
                self.Ui()
            elif n == 'U2':
                self.U2()
            elif n == 'R':
                self.R()
            elif n == "R'":
                self.Ri()
            elif n == 'R2':
                self.R2()
            elif n == 'F':
                self.F()
            elif n == "F'":
                self.Fi()
            elif n == 'F2':
                self.F2()

    def optimal_solve(self):
        s1 = self.pos[0]
        s2 = self.pos[1]
        s3 = self.pos[2]
        s4 = self.pos[3]
        s5 = self.pos[4]
        s6 = self.pos[5]
        s7 = self.pos[6]

        cube = Cube()
        moves = ('U', "U'", 'U2', 'R', "R'", 'R2', 'F', "F'", 'F2')
        algs = [['U'], ["U'"], ['U2'], ['R'], ["R'"], ['R2'], ['F'], ["F'"], ['F2']]
        alglist = [[[]], algs, [], [], [], []]
        poslist = {}
        alg_pos = {}

        if self.is_solved():
            return []

        for alg in algs:
            self.alg(alg)
            if self.is_solved():
                return alg
            poslist[tuple(self.pos)] = 1
            self.__init__(s1, s2, s3, s4, s5, s6, s7)
            cube.alg(alg)
            alg_pos[tuple(cube.pos)] = [alg]
            cube.__init__()

        for n in range(4):
            for alg in alglist[n + 1]:
                for m in moves:
                    if m[0] == alg[-1][0]:
                        continue
                    self.alg(alg + [m])
                    if tuple(self.pos) in poslist and poslist[tuple(self.pos)] != n + 2:
                        self.__init__(s1, s2, s3, s4, s5, s6, s7)
                        continue
                    poslist[tuple(self.pos)] = n + 2
                    alglist[n + 2].append(alg + [m])
                    if self.is_solved():
                        return alg + [m]
                    self.__init__(s1, s2, s3, s4, s5, s6, s7)
                    cube.alg(alg + [m])
                    if tuple(cube.pos) in alg_pos:
                        alg_pos[tuple(cube.pos)] += [alg + [m]]
                    else:
                        alg_pos[tuple(cube.pos)] = [alg + [m]]
                    cube.__init__()

        solutions = []
        minim = 11

        for alg in alglist[5]:
            for m in moves:
                if m[0] == alg[-1][0]:
                    continue
                self.alg(alg + [m])
                if self.is_solved():
                    return alg + [m]
                if tuple(self.pos) in alg_pos:
                    for a in alg_pos[tuple(self.pos)]:
                        if m[0] == inverse_alg(a)[0][0]:
                            a = shorten_alg(alg + [m] + inverse_alg(a))
                        else:
                            a = alg + [m] + inverse_alg(a)
                        solutions.append(a)
                        n = len(a)
                        if n < minim:
                            minim = n
                self.__init__(s1, s2, s3, s4, s5, s6, s7)

        for alg in solutions:
            if len(alg) == minim:
                return alg

        return ['error']

    def fast_solve(self, depth=6):
        s1 = self.pos[0]
        s2 = self.pos[1]
        s3 = self.pos[2]
        s4 = self.pos[3]
        s5 = self.pos[4]
        s6 = self.pos[5]
        s7 = self.pos[6]

        cube = Cube()
        moves = ('U', "U'", 'U2', 'R', "R'", 'R2', 'F', "F'", 'F2')
        algs = [['U'], ["U'"], ['U2'], ['R'], ["R'"], ['R2'], ['F'], ["F'"], ['F2']]
        alglist = [[[]], algs]
        poslist = set()
        alg_pos = {}
        for n in range(depth - 2):
            alglist.append([])

        if self.is_solved():
            return []

        for alg in algs:
            self.alg(alg)
            if self.is_solved():
                return alg
            poslist.add(tuple(self.pos))
            self.__init__(s1, s2, s3, s4, s5, s6, s7)
            cube.alg(alg)
            alg_pos[tuple(cube.pos)] = alg
            cube.__init__()

        for n in range(depth - 2):
            for alg in alglist[n + 1]:
                for m in moves:
                    if m[0] == alg[-1][0]:
                        continue
                    self.alg(alg + [m])
                    if tuple(self.pos) in poslist:
                        self.__init__(s1, s2, s3, s4, s5, s6, s7)
                        continue
                    poslist.add(tuple(self.pos))
                    alglist[n + 2].append(alg + [m])
                    if self.is_solved():
                        return alg + [m]
                    self.__init__(s1, s2, s3, s4, s5, s6, s7)
                    cube.alg(alg + [m])
                    alg_pos[tuple(cube.pos)] = alg + [m]
                    cube.__init__()

        for alg in alglist[depth - 1]:
            for m in moves:
                if m[0] == alg[-1][0]:
                    continue
                self.alg(alg + [m])
                if self.is_solved():
                    return alg + [m]
                if tuple(self.pos) in alg_pos:
                    return shorten_alg(alg + [m] + inverse_alg(alg_pos[tuple(self.pos)]))
                self.__init__(s1, s2, s3, s4, s5, s6, s7)
        return ['error']


if __name__ == '__main__':
    f = open('scrambles.txt')
    scrambles = []
    for line in f:
        scrambles.append(line.split())
    f.close()
    n = 1
    for alg in scrambles:
        print('Scramble', str(n))
        cube = Cube()
        cube.alg(alg)
        start_time = time.process_time()
        solution = cube.fast_solve()
        end_time = time.process_time()
        process_time = end_time - start_time
        f = open('run_time.txt', 'a')
        f.write(' / '.join([' '.join(alg), str(len(solution)), ' '.join(solution), str(process_time)]) + '\n')
        n += 1
    f.close()