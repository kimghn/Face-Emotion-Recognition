from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from fer import FER
import numpy as np

screen=Tk()
screen.title("FACE EMOTION RECOGNITION by kimghn")
windowWidth=600
windowHeight=500
screenWidth=screen.winfo_screenwidth()
screenHeight=screen.winfo_screenheight()
low=(screenWidth-windowWidth-350)
high=(screenHeight-windowHeight-120)
screen.geometry(f"{windowWidth}x{windowHeight}+{low}+{high}")
screen.configure(bg='#AD18B7')

def openFile():
    filePhoto=filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm *.tif *.tiff")])
    if filePhoto:
        fileImage=Image.open(filePhoto)
        fileImage.thumbnail((300, 300))
        tkImage=ImageTk.PhotoImage(fileImage)
        imageLabel.config(image=tkImage)
        imageLabel.image=tkImage
        detectEmotion(fileImage)
        
def detectEmotion(image):
    detector=FER(mtcnn=True)
    emotionResult=detector.detect_emotions(np.array(image))
    if emotionResult:
        dominantEmotion=emotionResult[0]['emotions']
        emotionScore=max(dominantEmotion.values())
        emotionName=[emotion for emotion, score in dominantEmotion.items() if score == emotionScore][0]
        Result.config(text=f"The Photo's Emotion is {emotionName} ({emotionScore:.0%})")
    else:
        Result.config(text="No emotion detected")
        
openButton=Button(screen,text="Open Image",font=('Arial', 20),bg='#5715A2',fg='white', command=openFile)
openButton.pack(padx=10,pady=20)

imageLabel=Label(screen,text="No Image Selected",font=('Arial', 16),bg='#FD4BFD')
imageLabel.pack()

Result=Label(screen,text="No Result",font=('Arial', 16),bg='#FD4BFD')
Result.pack(pady=20)

mainloop()