def extAngle(localSides):
    angle = float(360) / localSides
    
    return angle

def intAngle(sides):
    eAngle = extAngle(sides)
    iAngle = 180 - eAngle
    
    return iAngle

# Main
print("Enter Number of sides")
sides = int(input())
angle = extAngle(sides)
print("The exteria angle is..." + str(angle))
iAngle = intAngle(sides)
print("The Interior angle is..." + str(iAngle))
print("sum of the interior angles=" + str(iAngle * sides))
