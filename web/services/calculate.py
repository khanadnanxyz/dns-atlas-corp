def calc_location(id, x, y, z, vel):
    if isinstance(x, float) & isinstance(y, float) & isinstance(z, float) & isinstance(vel, float):
        pass
    else:
        x = float(x)
        y = float(y)
        z = float(z)
        vel = float(vel)
    result = (x * id) + (y * id) + (z * id) + vel
    return round(result, 2)
