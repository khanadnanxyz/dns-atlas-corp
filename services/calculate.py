def calc_distance(id, x, y, z, vel):
    result = (x * id) + (y * id) + (z * id) + vel
    return round(result, 2)
