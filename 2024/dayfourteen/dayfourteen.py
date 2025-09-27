def simulation(coords, vel, rows, cols):
    for i in range(len(coords)):
        coords[i] = calculateXY(coords[i][0], coords[i][1], vel[i][0], vel[i][1], rows, cols)
    
    print(coords)
    return quadrantsProduct(coords, rows, cols)


def calculateXY(i, j, si, sj, rows, cols):
    newI= 0
    newJ = 0
    if si < 0 :
        displacement = cols - i
        newI = (((100*si) % cols) - displacement) % cols
    else:
        newI = (((100*si) % cols) + i) % cols
    if sj < 0:
        displacement = rows - j
        newJ = (((100*sj) % rows) - displacement) % rows
    else:
        newJ = (((100*sj) % rows) + j) % rows
    return (newI,newJ)


def quadrantsProduct(coords, rows, cols):
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    for (i,j) in coords:
        if i < cols // 2 and j < rows // 2:
            quad1 += 1
        elif i > cols // 2 and j < rows // 2:
            quad2 += 1
        elif i < cols // 2 and j > rows // 2:
            quad3 += 1
        elif i > cols // 2 and j > rows // 2:
            quad4 += 1
    return quad1 * quad2 * quad3 * quad4

def main():
    coords = []
    vel = []
    with open('input.txt', 'r') as file:
        for line in file:
            c, v = line.split(" ")
            cc = c.split("=")
            vv = v.split("=")
            ccc = cc[1].split(",")
            vvv = vv[1].split(",")
            coords.append((int(ccc[0]), int(ccc[1])))
            vel.append((int(vvv[0]), int(vvv[1])))

    print(f"quadrants product: {simulation(coords, vel, 103, 101)}")


if __name__ == "__main__":
    main()