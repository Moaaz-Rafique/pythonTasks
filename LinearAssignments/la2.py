from numpy import log, sqrt

d1L = ['design', 'use', 'indentation', 'including', 'often', 'standard', 'released', 'features', 'reference', 'version', 'most', 'implementation', 'many', 'support', 'other', 'uses', 'variable', 'some', 'functions', 'expressions', 'library', 'modules', 'than', 'into', 'this', 'syntax', 'while', 'written', 'have', 'like', 'but', 'block', 'programs', 'object', 'example', 'operator', 'may', 'type', 'division', 'libraries', 'part', 'expression', 'number', 'string', 'classes']
d2L = ['largest', 'capital', 'province', 'industrial', 'centre', 'well', 'one', 'cities', 'two', 'port', 'founded', 'settlement', 'century', 'major', 'into', 'their', 'network', 'throughout', 'time', 'following', 'independence', 'residents', 'per', 'economic', 'growth', 'migrants', 'other', '2017', 'census', 'million', 'urban', 'areas', 'more', 'than', 'now', 'economy', 'approximately', 'ports', 'since', 'during', 'become', 'known', 'rates', 'crime', 'but', 'recorded', '2013', 'being', 'though', 'became', 'over', 'new', 'after', 'first', 'near', 'early', 'around', 'along', 'several', 'located', 'some', 'who', 'until', 'when', 'further', 'between', 'under', 'built', 'this', 'water', 'developed', 'control', 'continued', 'established', 'leading', 'including', 'many', 'district', 'such', 'public', 'building', 'system', 'municipal', 'government', 'period', 'numbers', 'buildings', 'form', 'part', 'area', 'bulk', 'live', 'rate', 'not', 'number', 'private', '2015', 'community', 'elected']
qL = ['has', 'environmental', 'environment', 'well', 'have', 'waste', 'management', 'water', 'into', 'that', 'such', 'noise', 'industrial', 'contamination', 'for', 'from']
D=2
terms = list(dict.fromkeys(d1L + d2L + qL))

qC = []
d1C = []
d2C = []

df = []
dBydf = []

IDF = []

wq = []
wd1 = []
wd2 = []
j=0
for t in terms: 
    if t in d1L:
        d1C.append(1)
    else:
        d1C.append(0)
    if t in d2L:
        d2C.append(1)
    else:
        d2C.append(0)
    if t in qL:
        qC.append(1)
    else:
        qC.append(0)
    df.append(d1C[-1]+d2C[-1])
    if df[-1]!=0:
        IDF.append(log(D/df[-1]))
    else :
        j+=1
        # print(t)
    wq.append(qC[-1]*IDF[-1])
    wd1.append(d1C[-1]*IDF[-1])
    wd2.append(d2C[-1]*IDF[-1])

# print(terms)
# print(d1C)
# print(d2C)
# print(qC)
# print(df)
# print(IDF)
# print(wq)
# print(wd1)
# print(wd2)

magD1 = 0
magD2 = 0
magQ = 0
for i in range(len(wd1)):
    magD1 = magD1+(wd1[i]*wd1[i])
    magD2 = magD2+(wd2[i]*wd2[i])
    magQ = magQ+(wq[i]*wq[i])

magQ = sqrt(magQ)
magD1 = sqrt(magD1)
magD2 = sqrt(magD2)

qD1=0
qD2=0
for i in range(len(wq)):
    qD1 += wq[i]*wd1[i]
    qD2 += wq[i]*wd2[i]
cosD1 = qD1/(magQ*magD1)
cosD2 = qD2/(magQ*magD2)

print(cosD1)
print(cosD2)
print(len(terms))
print(j)


if cosD1>cosD2:
    print("Rank D1: ",1)
    print("Rank D2: ",2)
else:
    print("Rank D2: ",1)
    print("Rank D1: ",2)