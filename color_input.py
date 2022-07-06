from visual_cube import *
def opp_color(color):
    if color == 'white':
        return 'yellow'
    if color == 'yellow':
        return 'white'
    if color == 'blue':
        return 'green'
    if color == 'green':
        return 'blue'
    if color == 'red':
        return 'orange'
    if color == 'orange':
        return 'red'


def get_pos(colors, cube):
    if cube == 3:
        if len(set(colors[:6])) != 6:
            return 'Invalid scramble: invalid center scheme'
    pos = []
    corners = 8
    if cube == 2:
        corners = 7

    for a in range(corners):
        piece = ''
        for b in range(3):
            color = colors[6 + 3*a + b]
            if color == colors[0]:
                piece += '3'
            if color == colors[1]:
                piece += '4'
            if color == colors[2]:
                piece += '5'
            if cube == 2 and color == opp_color(colors[0]) or cube == 3 and color == colors[3]:
                piece += '0'
            if cube == 2 and color == opp_color(colors[1]) or cube == 3 and color == colors[4]:
                piece += '1'
            if cube == 2 and color == opp_color(colors[2]) or cube == 3 and color == colors[5]:
                piece += '2'
        pos.append(piece)

    key = {'015': 0, '501': 1, '150': 2, '054': 3, '405': 4, '540': 5, '042': 6, '204': 7, '420': 8,
           '021': 9, '102': 10, '210': 11, '351': 12, '135': 13, '513': 14, '312': 15, '231': 16, '123': 17,
           '324': 18, '432': 19, '243': 20, '345': 21, '534': 22, '453': 23}

    for n in range(corners):
        try:
            pos[n] = key[pos[n]]
        except KeyError:
            return 'Invalid scramble: {}, {}, {} corner does not exist'.format(colors[3*n + 6], colors[3*n + 7],
                                                                               colors[3*n + 8])

    if cube == 3:
        for a in range(12):
            piece = ''
            for b in range(2):
                color = colors[30 + 2 * a + b]
                if color == colors[0]:
                    piece += '3'
                if color == colors[1]:
                    piece += '4'
                if color == colors[2]:
                    piece += '5'
                if color == colors[3]:
                    piece += '0'
                if color == colors[4]:
                    piece += '1'
                if color == colors[5]:
                    piece += '2'
            pos.append(piece)

        key = {'01': 0, '10': 1, '05': 2, '50': 3, '04': 4, '40': 5, '02': 6, '20': 7, '31': 8, '13': 9,
               '32': 10, '23': 11, '34': 12, '43': 13, '35': 14, '53': 15, '15': 16, '51': 17, '45': 18,
               '54': 19, '42': 20, '24': 21, '12': 22, '21': 23}
        for n in range(8, 20):
            try:
                pos[n] = key[pos[n]]
            except KeyError:
                return 'Invalid scramble: {}, {} edge does not exist.'.format(colors[2 * (n - 8) + 30], colors[2 * (n - 8) + 31])

        if len(set([n // 3 for n in pos[:corners]])) != corners:
            return 'Invalid scramble: duplicate corner'
        if len(set([n // 2 for n in pos[8:]])) != 12:
            return 'Invalid scramble: duplicate edge'

        if sum(pos[:corners]) % 3 != 0:
            return 'Invalid scramble: twisted corner'
        if sum(pos[8:]) % 2 != 0:
            return 'Invalid scramble: flipped edge'

    return pos
