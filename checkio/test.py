from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    
    a1=(coords_1[0][0]-coords_1[1][0])**2+(coords_1[0][1]-coords_1[1][1])**2
    b1=(coords_1[1][0]-coords_1[2][0])**2+(coords_1[1][1]-coords_1[2][1])**2
    c1=(coords_1[2][0]-coords_1[0][0])**2+(coords_1[2][1]-coords_1[0][1])**2
    p1=[a1,b1,c1]
    p1.sort()

    a2=(coords_2[0][0]-coords_2[1][0])**2+(coords_2[0][1]-coords_2[1][1])**2
    b2=(coords_2[1][0]-coords_2[2][0])**2+(coords_2[1][1]-coords_2[2][1])**2
    c2=(coords_2[2][0]-coords_2[0][0])**2+(coords_2[2][1]-coords_2[0][1])**2
    p2=[a2,b2,c2]
    p2.sort()
    
    return p1,p2