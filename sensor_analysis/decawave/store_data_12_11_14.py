# Eric Schneider

import json

if __name__ == '__main__':
    data = []
    data.append((0.16, 0.44, 'up'))
    data.append((0.13, 0.44, 'up'))
    data.append((0.14, 0.44, 'up'))
    data.append((0.15, 0.44, 'up'))
    data.append((0.16, 0.44, 'up'))

    data.append((0.18, 0.44, 'up'))
    data.append((0.19, 0.44, 'up'))
    data.append((0.14, 0.44, 'up'))
    data.append((0.16, 0.44, 'up'))
    data.append((0.16, 0.44, 'up'))

    data.append((0.23, 0.44, 'left'))
    data.append((0.29, 0.44, 'left'))
    data.append((0.28, 0.44, 'left'))
    data.append((0.27, 0.44, 'left'))
    data.append((0.25, 0.44, 'left'))

    data.append((2.17, 2.43, 'up'))
    data.append((2.14, 2.43, 'up'))
    data.append((2.15, 2.43, 'up'))
    data.append((2.16, 2.43, 'up'))
    data.append((2.18, 2.43, 'up'))

    data.append((2.45, 2.43, 'left'))
    data.append((2.48, 2.43, 'left'))
    data.append((2.43, 2.43, 'left'))
    data.append((2.4, 2.43, 'left'))
    data.append((2.41, 2.43, 'left'))
    data.append((2.33, 2.43, 'left'))

    data.append((2.09, 2.43, 'at'))
    data.append((2.1, 2.43, 'at'))
    data.append((2.09, 2.43, 'at'))
    data.append((2.08, 2.43, 'at'))
    data.append((2.09, 2.43, 'at'))

    data.append((2.29, 2.43, 'right'))
    data.append((2.28, 2.43, 'right'))
    data.append((2.3, 2.43, 'right'))
    data.append((2.31, 2.43, 'right'))
    data.append((2.31, 2.43, 'right'))

    data.append((2.27, 2.43, 'right'))
    data.append((2.26, 2.43, 'right'))
    data.append((2.19, 2.43, 'right'))
    data.append((2.18, 2.43, 'right'))
    data.append((2.17, 2.43, 'right'))

    data.append((2.17, 2.43, 'up'))
    data.append((2.14, 2.43, 'up'))
    data.append((2.15, 2.43, 'up'))
    data.append((2.16, 2.43, 'up'))
    data.append((2.18, 2.43, 'up'))

    data.append((7.33, 7.62, 'up'))
    data.append((7.34, 7.62, 'up'))
    data.append((7.34, 7.62, 'up'))
    data.append((7.32, 7.62, 'up'))
    data.append((7.33, 7.62, 'up'))
    data.append((7.35, 7.62, 'up'))
    data.append((7.32, 7.62, 'up'))

    data.append((7.48, 7.62, 'left'))
    data.append((7.45, 7.62, 'left'))
    data.append((7.46, 7.62, 'left'))
    data.append((7.48, 7.62, 'left'))
    data.append((7.54, 7.62, 'left'))
    data.append((7.54, 7.62, 'left'))

    data.append((7.45, 7.62, 'at'))
    data.append((7.32, 7.62, 'at'))
    data.append((7.35, 7.62, 'at'))
    data.append((7.44, 7.62, 'at'))
    data.append((7.43, 7.62, 'at'))

    data.append((4.29, 4.57, 'up'))
    data.append((4.32, 4.57, 'up'))
    data.append((4.3, 4.57, 'up'))
    data.append((4.29, 4.57, 'up'))
    data.append((4.32, 4.57, 'up'))

    data.append((4.32, 4.57, 'at'))
    data.append((4.31, 4.57, 'at'))
    data.append((4.33, 4.57, 'at'))
    data.append((4.31, 4.57, 'at'))
    data.append((4.27, 4.57, 'at'))

    data.append((14.81, 15.24, 'up'))
    data.append((14.85, 15.24, 'up'))
    data.append((14.86, 15.24, 'up'))
    data.append((14.84, 15.24, 'up'))
    data.append((14.85, 15.24, 'up'))
    data.append((14.82, 15.24, 'up'))

    data.append((22.31, 22.86, 'up'))
    data.append((22.33, 22.86, 'up'))
    data.append((22.35, 22.86, 'up'))
    data.append((22.34, 22.86, 'up'))
    data.append((22.32, 22.86, 'up'))
    data.append((22.34, 22.86, 'up'))
    data.append((22.37, 22.86, 'up'))

    data.append((29.63, 30.48, 'up'))
    data.append((29.68, 30.48, 'up'))
    data.append((29.66, 30.48, 'up'))
    data.append((29.65, 30.48, 'up'))
    data.append((29.64, 30.48, 'up'))
    data.append((29.62, 30.48, 'up'))

    data.append((45.61, 45.72, 'up'))
    data.append((45.62, 45.72, 'up'))
    data.append((45.6, 45.72, 'up'))
    data.append((45.56, 45.72, 'up'))
    data.append((45.57, 45.72, 'up'))
    data.append((45.61, 45.72, 'up'))
    data.append((45.57, 45.72, 'up'))

    data.append((49.53, 46, 'up'))
    data.append((49.6, 46, 'up'))
    data.append((49.58, 46, 'up'))
    data.append((49.56, 46, 'up'))
    data.append((49.57, 46, 'up'))
    data.append((49.6, 46, 'up'))

    data.append((49.53, 46, 'up'))
    data.append((49.6, 46, 'up'))
    data.append((49.58, 46, 'up'))
    data.append((49.56, 46, 'up'))
    data.append((49.57, 46, 'up'))

    data.append((95.32, 90, 'up'))
    data.append((94.25, 90, 'up'))
    data.append((94.18, 90, 'up'))
    data.append((94.225, 90, 'up'))
    data.append((94.22, 90, 'up'))

    with open('data_12_11_14.txt', 'w') as outfile:
        json.dump(data, outfile)
