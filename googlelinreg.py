from statistics import mean
import numpy
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

def slope_intercepth(ymh, pmh, tyh, th):
    mh = ((ymh*pmh) - mean(th)) / ((ymh*ymh) - mean(tyh))

    bh = pmh - mh*ymh

    return mh, bh

mh, bh = slope_intercepth(ymh, pmh, tyh, th)

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

def slope_intercepta(yma, pma, ta, tya):
    ma = ((yma*pma) - mean(ta)) / ((yma*yma) - mean(tya))

    ba = pma - ma*yma

    return ma, ba

ma, ba = slope_intercepta(yma, pma, ta, tya)

total = 0
for a in range(len(google)):
    total += (float(google[a][1]) - ma)**2
sd = (total/(len(google)))**(1/2)

cor = 0
resi = 0
tot = 0
c = 0
for c in range(len(google)):
    resi += (float(google[c][1]) - (ma * (2022 - c) + ba))**2
    tot += (float(google[c][1]) - ma)**2
cor = 1 - (resi/tot)


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

def slope_interceptl(yml, pml, tl, tyl):
    ml = ((yml*pml) - mean(tl)) / ((yml*yml) - mean(tyl))

    bl = pml - ml*yml

    return ml, bl

ml, bl = slope_interceptl(yml, pml, tl, tyl)

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

def slope_intercept5a(ym5, pm5, t5, ty5):
    m5 = ((ym5*pm5) - mean(t5)) / ((ym5*ym5) - mean(ty5))

    b5 = pm5 - m5*ym5

    return m5, b5

m5, b5 = slope_intercept5a(ym5, pm5, t5, ty5)

total5 = 0
for a in range(len(google)):
    total5 += (float(google[a][1]) - m5)**2
sd5 = (total5/(len(google)))**(1/2)

cor5 = 0
resi5 = 0
tot5 = 0
c5 = 0
for c5 in range(len(google)):
    resi5 += (float(google[c5][1]) - (m5 * (2022 - c5) + b5))**2
    tot5 += (float(google[c5][1]) - m5)**2
cor5 = 1 - (resi5/tot5)

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

def slope_intercept5l(ym5l, pm5l, t5l, ty5l):
    m5l = ((ym5l*pm5l) - mean(t5l)) / ((ym5l*ym5l) - mean(ty5l))

    b5l = pm5l - m5l*ym5l

    return m5l, b5l

m5l, b5l = slope_intercept5l(ym5l, pm5l, t5l, ty5l)

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

def slope_intercept5h(ym5h, pm5h, t5h, ty5h):
    m5h = ((ym5h*pm5h) - mean(t5h)) / ((ym5h*ym5h) - mean(ty5h))

    b5h = pm5h - m5h*ym5h

    return m5h, b5h

m5h, b5h = slope_intercept5h(ym5h, pm5h, t5h, ty5h)

value = float(input("What year would you like to predict? "))
print(f"Price Estimate:${round((ma*value) + ba, 2)}(2006-current), ${round((m5*value) + b5, 2)}(2017-current), 2017 is {round(((m5*value) + b5) / ((ma*value) + ba), 2)} times higher")
print(f"Average Return:{round(ma, 2)}% since 2006 and {round(m5, 2)}% since 2017")
print(f"Using 2006 data the standard deviation is {round(sd,2)}, meaning there is a 68% chance the stock price is between ${round(((ma*value) + ba) - sd, 2)} and ${round(((ma*value) + ba) + sd, 2)} and there is a 95% chance the stock price is between ${round(((ma*value) + ba) - 2*sd, 2)} and ${round(((ma*value) + ba) + 2*sd, 2)}.")
print(f"Using 2017 data the standard deviation is {round(sd5,2)}, meaning there is a 68% chance the stock price is between ${round(((m5*value) + b5) - sd5, 2)} and ${round(((m5*value) + b5) + sd5, 2)} and there is a 95% chance the stock price is between ${round(((m5*value) + b5) - 2*sd5, 2)} and ${round(((m5*value) + b5) + 2*sd5, 2)}.")
print(f"The r^2 value for 2006 is {round(cor, 3)} meaning that only {round(cor *100, 1)}% of price varience is caused by time.")
print(f"The r^2 value for 2017 is {round(cor5, 3)} meaning that only {round(cor5 *100, 1)}% of price varience is caused by time.")
print(f"The r^2 values show that both data sets have strong linear correlations")
