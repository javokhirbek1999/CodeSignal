def growingPlant(upSpeed, downSpeed, desiredHeight):
    currentHeight, days = 0, 0
    while True:
        currentHeight += upSpeed
        days += 1
        if currentHeight >= desiredHeight:
            return days
        currentHeight -= downSpeed
