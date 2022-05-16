import os,shutil
entries = os.listdir('C:/Users/archi/Pictures/All Grad pics')

selected = []
ranges = []

selected.append("DSC_8248.JPG")
selected.append("DSC_8251.JPG")
selected.append("DSC_8255.JPG")
selected.append("DSC_8352.JPG")
selected.append("DSC_8354.JPG")
selected.append("DSC_8355.JPG")
selected.append("DSC_8363.JPG")
selected.append("DSC_8364.JPG")
selected.append("DSC_8367.JPG")
selected.append("DSC_8368.JPG")
selected.append("DSC_8369.JPG")
selected.append("DSC_8370.JPG")
selected.append("DSC_8375.JPG")
selected.append("DSC_8402.JPG")
selected.append("DSC_8411.JPG")
selected.append("DSC_8416.JPG")
selected.append("DSC_8417.JPG")
selected.append("DSC_8418.JPG")
selected.append("DSC_8437.JPG")
selected.append("DSC_8438.JPG")
selected.append("DSC_8441.JPG")
selected.append("DSC_8442.JPG")
selected.append("DSC_8443.JPG")
selected.append("DSC_8472.JPG")
selected.append("DSC_8474.JPG")
selected.append("DSC_8477.JPG")
selected.append("DSC_8479.JPG")
selected.append("DSC_8534.JPG")
selected.append("DSC_8544.JPG")
selected.append("DSC_8553.JPG")
selected.append("DSC_8555.JPG")
selected.append("DSC_8556.JPG")
selected.append("DSC_8566.JPG")
selected.append("DSC_8567.JPG")
selected.append("DSC_8618.JPG")
selected.append("DSC_8647.JPG")
selected.append("DSC_8684.JPG")
selected.append("DSC_8707.JPG")
selected.append("DSC_8708.JPG")
selected.append("DSC_8846.JPG")
selected.append("DSC_8869.JPG")


ranges.append("8445-8454")
ranges.append("8603-8608")
ranges.append("8658-8661")
ranges.append("8687-8705")
ranges.append("8557-8561")


for singleRange in ranges:
    rangeValues = singleRange.partition('-')
    strt = int(rangeValues[0])
    end = int(rangeValues[2])
    for img in range(strt,end):
        fileName = "DSC_"+str(img)+".JPG"
        selected.append(fileName)
    

for photo in entries:
    if photo in selected:
        src = "C:/Users/archi/Pictures/All Grad pics/"+photo
        dst = "C:/Users/archi/Pictures/Good Grad Pics"
        shutil.copy(src,dst)

selected = []


