from PIL import Image

img = Image.open('air.png')
img = img.convert("RGBA")
datas = img.getdata()
bcount=0
newData=[]
for item in datas:
    r,g,b,a = item
    if b > 100 and r < 100:
        bcount+=1
        newData.append((255,255,255,a))
    else:
        newData.append(item)
        
img.putdata(newData)
img.save("img2.png", "PNG")
