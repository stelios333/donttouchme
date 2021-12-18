import time
import tkinter as tk
try:
    from PIL import Image, ImageDraw, ImageFont, ImageTk
except:
    import os, sys
    os.system('pip install pillow')
    os.execl(sys.executable, sys.executable, *sys.argv)
    
def showPIL(pilImage):
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    me=tk.Menu(root, tearoff=0)
    me.add_command(label='Exit', command=lambda: (root.withdraw(), root.quit()),accelerator='Esc', font=('Arial',9))
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    root.bind("<ButtonRelease-3>", lambda e:me.tk_popup(e.x_root, e.y_root))
    canvas = tk.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()
width, height=(1920, 1080)
img=Image.new('RGB', (width, height), color='blue')
print("Image size: "+str(img.size[0])+"x"+str(img.size[1]))
imgd=ImageDraw.Draw(img, 'RGBA')
imgd.rectangle(xy=(60,60,1860,1020),fill='red', outline='yellow', width=2)
font=ImageFont.truetype("./third-party/times.ttf", 250)
text="Don't touch me!"
wd, hd=font.getsize(text)
imgd.text(xy=((width-wd)/2,(height-hd)/2), text=text, font=font)
imgd.chord((60,60,1860,1020), start=0, end=360, fill=(255, 77, 207, 124), outline=(0, 0, 0))
showPIL(img)
