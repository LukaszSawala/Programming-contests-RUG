lastSun, sunRecovery = map(int,input().split())
lastMoon, moonRecovery = map(int,input().split())
lastSun = -lastSun
lastMoon = -lastMoon
while lastMoon != lastSun:
    if lastMoon < lastSun:
        lastMoon+=moonRecovery
    else:
        lastSun+=sunRecovery

print(lastSun)