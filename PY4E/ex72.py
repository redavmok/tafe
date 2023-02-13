# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
totalsum = 0
totalnum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        data = line
        pos = data.find(':')
        pnumber = data[pos+1:]
        result = float(pnumber)
        totalsum += result
        totalnum += 1
        
totalaverage = totalsum / totalnum
stotalaverage = str(totalaverage)
print('Average spam confidence: ' + stotalaverage)
