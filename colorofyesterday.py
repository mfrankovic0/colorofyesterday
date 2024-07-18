import random

def colorgen():
    color = random.randrange(0, 2**24)
    hex_color = hex(color)