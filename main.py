def waterState(f):
    if f <= 32:
        return "solid"
    elif 32 < f < 211 :
        return "liqid"
    else  :
        return "gas"
print (waterState(300))

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False
print (isDozen(35))

def toGerman( y ):
    if y == "yes":
        return "ja"
    else:
        return "nein"
print (toGerman("no"))

def stopLight(c):
    if c == "green":
        return "go"
    elif c== "yellow":
        return "slow"
    else:
        return "stop"
print (stopLight("green"))
