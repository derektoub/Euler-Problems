class Found(Exception): pass
try:
    for a in range(1,500):
        for b in range(a,500):
            if a + b + (a*a + b*b)**(0.5) == 1000.0:
                raise Found
except Found:
    print a*b*int((a*a + b*b)**(0.5))
