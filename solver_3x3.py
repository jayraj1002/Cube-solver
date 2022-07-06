import time

def oriented_move(s1, s2, s3, s4, piece):
    a = piece[s1]
    b = piece[s2]
    c = piece[s3]
    d = piece[s4]
    piece[s1] = d
    piece[s2] = a
    piece[s3] = b
    piece[s4] = c


def double_move(s1, s2, s3, s4, piece):
    a = piece[s1]
    b = piece[s2]
    c = piece[s3]
    d = piece[s4]
    piece[s1] = c
    piece[s2] = d
    piece[s3] = a
    piece[s4] = b


def unoriented_move(s1, s2, s3, s4, piece, n):
    a = piece[s1]
    b = piece[s2]
    c = piece[s3]
    d = piece[s4]
    piece[s1] = (d // n * n) + ((d - 1) % n)
    piece[s2] = (a // n * n) + ((a + 1) % n)
    piece[s3] = (b // n * n) + ((b - 1) % n)
    piece[s4] = (c // n * n) + ((c + 1) % n)


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
    def __init__(self, c0=0, c1=3, c2=6, c3=9, c4=12, c5=15, c6=18, c7=21,
                 e0=0, e1=2, e2=4, e3=6, e4=8, e5=10, e6=12, e7=14, e8=16, e9=18, e10=20, e11=22):
        self.corner_pos = [c0, c1, c2, c3, c4, c5, c6, c7]
        self.edge_pos = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]

    def position(self):
        return tuple(self.corner_pos + self.edge_pos)

    def is_oriented(self):
        for n in self.corner_pos:
            if n % 3 != 0:
                return False
        for n in self.edge_pos[8:]:
            if n < 16:
                return False
        for n in self.edge_pos:
            if n % 2 != 0:
                return False
        return True

    def orientation(self):
        position = []
        for n in self.corner_pos:
            if n % 3 == 0:
                position.append(0)
            elif n % 3 == 1:
                position.append(1)
            else:
                position.append(2)
        for n in self.edge_pos:
            if n < 16 and n % 2 == 0:
                position.append(0)
            elif n < 16:
                position.append(1)
            elif n % 2 == 0:
                position.append(2)
            else:
                position.append(3)

        return tuple(position)

    def is_solved(self):
        return self.corner_pos == [0, 3, 6, 9, 12, 15, 18, 21] and self.edge_pos == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

    def alg(self, moves):
        for move in moves:
            if move == 'U':
                oriented_move(0, 1, 2, 3, self.corner_pos)
                oriented_move(0, 1, 2, 3, self.edge_pos)

            elif move == "U'":
                oriented_move(0, 3, 2, 1, self.corner_pos)
                oriented_move(0, 3, 2, 1, self.edge_pos)

            elif move == 'U2':
                double_move(0, 1, 2, 3, self.corner_pos)
                double_move(0, 1, 2, 3, self.edge_pos)

            elif move == 'D':
                oriented_move(4, 5, 6, 7, self.corner_pos)
                oriented_move(4, 5, 6, 7, self.edge_pos)

            elif move == "D'":
                oriented_move(4, 7, 6, 5, self.corner_pos)
                oriented_move(4, 7, 6, 5, self.edge_pos)

            elif move == 'D2':
                double_move(4, 5, 6, 7, self.corner_pos)
                double_move(4, 5, 6, 7, self.edge_pos)

            elif move == 'R':
                unoriented_move(3, 2, 6, 5, self.corner_pos, 3)
                oriented_move(3, 10, 5, 11, self.edge_pos)

            elif move == "R'":
                unoriented_move(3, 5, 6, 2, self.corner_pos, 3)
                oriented_move(3, 11, 5, 10, self.edge_pos)

            elif move == 'R2':
                double_move(3, 2, 6, 5, self.corner_pos)
                double_move(3, 10, 5, 11, self.edge_pos)

            elif move == 'L':
                unoriented_move(1, 0, 4, 7, self.corner_pos, 3)
                oriented_move(1, 8, 7, 9, self.edge_pos)

            elif move == "L'":
                unoriented_move(1, 7, 4, 0, self.corner_pos, 3)
                oriented_move(1, 9, 7, 8, self.edge_pos)

            elif move == 'L2':
                double_move(0, 4, 7, 1, self.corner_pos)
                double_move(1, 8, 7, 9, self.edge_pos)

            elif move == 'F':
                unoriented_move(0, 3, 5, 4, self.corner_pos, 3)
                unoriented_move(0, 11, 4, 8, self.edge_pos, 2)

            elif move == "F'":
                unoriented_move(0, 4, 5, 3, self.corner_pos, 3)
                unoriented_move(0, 8, 4, 11, self.edge_pos, 2)

            elif move == 'F2':
                double_move(0, 3, 5, 4, self.corner_pos)
                double_move(0, 11, 4, 8, self.edge_pos)

            elif move == 'B':
                unoriented_move(2, 1, 7, 6, self.corner_pos, 3)
                unoriented_move(2, 9, 6, 10, self.edge_pos, 2)

            elif move == "B'":
                unoriented_move(2, 6, 7, 1, self.corner_pos, 3)
                unoriented_move(2, 10, 6, 9, self.edge_pos, 2)

            elif move == 'B2':
                double_move(2, 1, 7, 6, self.corner_pos)
                double_move(2, 9, 6, 10, self.edge_pos)

            else:
                print('error:', move, 'not valid move')

    def permute(self, depth):
        c0 = self.corner_pos[0]
        c1 = self.corner_pos[1]
        c2 = self.corner_pos[2]
        c3 = self.corner_pos[3]
        c4 = self.corner_pos[4]
        c5 = self.corner_pos[5]
        c6 = self.corner_pos[6]
        c7 = self.corner_pos[7]

        e0 = self.edge_pos[0]
        e1 = self.edge_pos[1]
        e2 = self.edge_pos[2]
        e3 = self.edge_pos[3]
        e4 = self.edge_pos[4]
        e5 = self.edge_pos[5]
        e6 = self.edge_pos[6]
        e7 = self.edge_pos[7]
        e8 = self.edge_pos[8]
        e9 = self.edge_pos[9]
        e10 = self.edge_pos[10]
        e11 = self.edge_pos[11]

        moves = ('U', "U'", 'U2', 'D', "D'", 'D2', 'R2', 'L2', 'F2', 'B2')
        cube_pos = set()
        alg_pos = {}
        algs = [[]]

        if self.is_solved():
            return []

        cube = Cube()

        for m in moves:
            self.alg([m])
            if self.is_solved():
                return [m]
            cube_pos.add(self.position())
            algs[0].append([m])
            self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
            cube.alg([m])
            alg_pos[cube.position()] = [m]
            cube.__init__()

        for n in range(depth//2 - 1):
            algs.append([])
            for alg in algs[n]:
                for m in moves:
                    if alg[-1][0] == m[0]:
                        continue
                    self.alg(alg + [m])
                    if self.position() in cube_pos:
                        self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
                        continue
                    if self.is_solved():
                        return alg + [m]
                    if self.position() in alg_pos:
                        return alg + [m] + inverse_alg(alg_pos[self.position()])
                    cube_pos.add(self.position())
                    algs[n + 1].append(alg + [m])
                    self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
                    cube.alg(alg + [m])
                    alg_pos[cube.position()] = alg + [m]
                    cube.__init__()

        return 'error'

    def solve(self, orientation_depth, permutation_depth):
        c0 = self.corner_pos[0]
        c1 = self.corner_pos[1]
        c2 = self.corner_pos[2]
        c3 = self.corner_pos[3]
        c4 = self.corner_pos[4]
        c5 = self.corner_pos[5]
        c6 = self.corner_pos[6]
        c7 = self.corner_pos[7]

        e0 = self.edge_pos[0]
        e1 = self.edge_pos[1]
        e2 = self.edge_pos[2]
        e3 = self.edge_pos[3]
        e4 = self.edge_pos[4]
        e5 = self.edge_pos[5]
        e6 = self.edge_pos[6]
        e7 = self.edge_pos[7]
        e8 = self.edge_pos[8]
        e9 = self.edge_pos[9]
        e10 = self.edge_pos[10]
        e11 = self.edge_pos[11]

        moves = ('U', "U'", 'U2', 'D', "D'", 'D2', 'R', "R'", 'R2', 'L', "L'", 'L2', 'F', "F'", 'F2', 'B', "B'", 'B2')
        cube_pos = set()
        alg_pos = {}
        algs = [[]]
        orientations = set()

        if self.is_oriented():
            solve = self.permute(permutation_depth)
            if solve != 'error':
                return solve

        cube = Cube()

        for m in moves:
            self.alg([m])
            if self.is_oriented():
                orientations.add(self.position())
                solve = self.permute(permutation_depth)
                if solve != 'error':
                    return shorten_alg([m] + solve)
            cube_pos.add(self.position())
            algs[0].append([m])
            self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
            cube.alg([m])
            orientation = cube.orientation()
            if orientation not in alg_pos:
                alg_pos[orientation] = [m]
            cube.__init__()

        for n in range(orientation_depth//2 - 1):
            algs.append([])
            for alg in algs[n]:
                for m in moves:
                    if alg[-1][0] == m[0]:
                        continue
                    self.alg(alg + [m])
                    if self.position() in cube_pos:
                        self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
                        continue
                    if self.is_oriented() and self.position() not in orientations:
                        orientations.add(self.position())
                        solve = self.permute(permutation_depth)
                        if solve != 'error':
                            return shorten_alg(alg + [m] + solve)
                    orientation = self.orientation()
                    if orientation in alg_pos:
                        self.alg(inverse_alg(alg_pos[orientation]))
                        if self.position() not in orientations:
                            orientations.add(self.position())
                            solve = self.permute(permutation_depth)
                            if solve != 'error':
                                return shorten_alg(alg + [m] + inverse_alg(alg_pos[orientation]) + solve)
                    cube_pos.add(self.position())
                    algs[n + 1].append(alg + [m])
                    self.__init__(c0, c1, c2, c3, c4, c5, c6, c7, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11)
                    cube.alg(alg + [m])
                    orientation = cube.orientation()
                    if orientation not in alg_pos:
                        alg_pos[orientation] = alg + [m]
                    cube.__init__()

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
        solution = cube.solve(12, 12)
        end_time = time.process_time()
        process_time = end_time - start_time
        f = open('run_time.txt', 'a')
        f.write(' / '.join([' '.join(alg), str(len(solution)), ' '.join(solution), str(process_time)]) + '\n')
        n += 1
    f.close()
