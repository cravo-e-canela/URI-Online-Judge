import math
import sys
PI = 3.1415926535897
def find_areas(x):
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])


    # triangle
    perimeter = float((a + b + c) / 2)

    total_area_tri = float(math.sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c)))


    # circunference
    ray = float((a * b * c)/( 4 * total_area_tri))

    total_area_cir = float((ray ** 2) * PI)




    # small_circunference
    ray_C = float(total_area_tri / perimeter)

    total_area_sm_c = float((ray_C ** 2) * PI)

    ###results
    sunflowers = float(total_area_cir - total_area_tri)
    violets = float(total_area_tri - total_area_sm_c)
    roses = float(total_area_sm_c)
    flowers = [sunflowers, violets, roses]

    return flowers


n = []
result = []


while True:
    try:
        n.clear()
        n = input().split()
        result.append(find_areas(n))


    except EOFError:
        break


for i in range(len(result)):
        print('{:.4f} {:.4f} {:.4f}'.format(result[i][0], result[i][1], result[i][2]))
