pi = 3.14159

# radius:半径
def area(radius):
    """円の面積を算出
       pi = 3.14159を設定"""
    return pi * (radius ** 2)

def circumference(radius):
    """円の直径を算出"""
    return 2 * pi * radius

def sphereSurface(radius):
    """球(sphere)の表面積を算出"""
    return 4.0 * area(radius)

def sphereVolume(radius):
    """球(sphere)の体積を算出"""
    return (4.0/3.0)*pi*(radius**3)