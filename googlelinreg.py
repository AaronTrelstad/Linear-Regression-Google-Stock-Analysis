from statistics import mean
import numpy as np
import csv

yh = 0
ph = 0
th = []
tyh = []
with open('googlehigh.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        th.append(float(google[x][1]) * float(google[x][0]))
        tyh.append(float(google[x][0]) * float(google[x][0]))
        yh += float(google[x][0])
        ph += float(google[x][1])
ymh = yh/(len(google))
pmh = ph/(len(google))

def slope_intercept(ymh, pmh, tyh, th):
    mh = ((ymh*pmh) - mean(th)) / ((ymh*ymh) - mean(tyh))

    bh = pmh - mh*ymh

    return mh, bh

mh, bh = slope_intercept(ymh, pmh, tyh, th)

##print(f"High: y = {mh}x + {bh}")

ya = 0
pa = 0
ta = []
tya = []

with open('googleaverage.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        ta.append(float(google[x][1]) * float(google[x][0]))
        tya.append(float(google[x][0]) * float(google[x][0]))
        ya += float(google[x][0])
        pa += float(google[x][1])
yma = ya/(len(google))
pma = pa/(len(google))

def slope_intercept(yma, pma, ta, tya):
    ma = ((yma*pma) - mean(ta)) / ((yma*yma) - mean(tya))

    ba = pma - ma*yma

    return ma, ba

ma, ba = slope_intercept(yma, pma, ta, tya)

total = 0
for a in range(len(google)):
    total += (float(google[a][1]) - ma)**2
sd = (total/(len(google)))**(1/2)

##print(f"Average: y = {ma}x + {ba}")

yl = 0
pl = 0
tl = []
tyl = []

with open('googlelow.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        tl.append(float(google[x][1]) * float(google[x][0]))
        tyl.append(float(google[x][0]) * float(google[x][0]))
        yl += float(google[x][0])
        pl += float(google[x][1])
yml = yl/(len(google))
pml = pl/(len(google))

def slope_intercept(yml, pml, tl, tyl):
    ml = ((yml*pml) - mean(tl)) / ((yml*yml) - mean(tyl))

    bl = pml - ml*yml

    return ml, bl

ml, bl = slope_intercept(yml, pml, tl, tyl)

##print(f"Low: y = {ml}x + {bl}")

y5 = 0
p5 = 0
t5 = []
ty5 = []

with open('google5year.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        t5.append(float(google[x][1]) * float(google[x][0]))
        ty5.append(float(google[x][0]) * float(google[x][0]))
        y5 += float(google[x][0])
        p5 += float(google[x][1])
ym5 = y5/(len(google))
pm5 = p5/(len(google))

def slope_intercept(ym5, pm5, t5, ty5):
    m5 = ((ym5*pm5) - mean(t5)) / ((ym5*ym5) - mean(ty5))

    b5 = pm5 - m5*ym5

    return m5, b5

m5, b5 = slope_intercept(ym5, pm5, t5, ty5)

total5 = 0
for a in range(len(google)):
    total5 += (float(google[a][1]) - m5)**2
sd5 = (total5/(len(google)))**(1/2)

y5l = 0
p5l = 0
t5l = []
ty5l = []

with open('google5yearlow.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        t5l.append(float(google[x][1]) * float(google[x][0]))
        ty5l.append(float(google[x][0]) * float(google[x][0]))
        y5l += float(google[x][0])
        p5l += float(google[x][1])
ym5l = y5l/(len(google))
pm5l = p5l/(len(google))

def slope_intercept(ym5l, pm5l, t5l, ty5l):
    m5l = ((ym5l*pm5l) - mean(t5l)) / ((ym5l*ym5l) - mean(ty5l))

    b5l = pm5l - m5l*ym5l

    return m5l, b5l

m5l, b5l = slope_intercept(ym5l, pm5l, t5l, ty5l)

##print(f"5 year lows: y = {m5l}x + {b5l}")

y5h = 0
p5h = 0
t5h = []
ty5h = []

with open('google5yearhigh.csv') as f:
    reader = csv.reader(f)
    google = list(reader)
    for x in range(len(google)):
        t5h.append(float(google[x][1]) * float(google[x][0]))
        ty5h.append(float(google[x][0]) * float(google[x][0]))
        y5h += float(google[x][0])
        p5h += float(google[x][1])
ym5h = y5h/(len(google))
pm5h = p5h/(len(google))

def slope_intercept(ym5h, pm5h, t5h, ty5h):
    m5h = ((ym5h*pm5h) - mean(t5h)) / ((ym5h*ym5h) - mean(ty5h))

    b5h = pm5h - m5h*ym5h

    return m5h, b5h

m5h, b5h = slope_intercept(ym5h, pm5h, t5h, ty5h)



value = float(input("What year would you like to predict? "))

print(f"Using data since 2006 would predict a price estimate of ${round((ma*value) + ba, 2)} in the year {int(value)}, but using more recent data sice 2017 the estimated price would be ${round((m5*value) + b5, 2)} which is {round(((m5*value) + b5) / ((ma*value) + ba), 2)} times greater.")
print(f"The average return since 2006 is {round(ma, 2)}% and the average return since 2017 is {round(m5, 2)}%.")
print(f"The 2006 data estimates a price range of ${round((ml*value) + bl, 2)} to ${round((mh*value) + bh, 2)} whereas the 2017 data predicts a range of ${round((m5l*value) + b5l, 2)} to ${round((m5h*value) + b5h, 2)} the range of the 2017 data is {round((((m5l*value) + b5l) - ((m5h*value) + b5h)) / (((ml*value) + bl) - ((mh*value) + bh)), 2)} times greater.")
print(f"Using 2006 data the standard deviation is {round(sd,2)}, from this we would consider an unusaul high price to be ${round(((ma*value) + ba) + 2*sd, 2)} and unusaully low at ${round(((ma*value) + ba) - 2*sd, 2)}")
print(f"Using 2017 data the standard deviation is {round(sd5,2)}, from this we would consider an unusaul high price to be ${round(((m5*value) + b5) + 2*sd5, 2)} and unusaully low at ${round(((m5*value) + b5) - 2*sd5, 2)}")
