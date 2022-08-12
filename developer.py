from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open("Images_GUI/banner.png")
        img=img.resize((1366,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=150)

        # backgorund image 
        bg1=Image.open("Images_GUI/dev_bg.png")
        bg1=bg1.resize((1366,573),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=150,width=1366,height=573)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("Consolas",30,"bold"),bg="white",fg="#3B114B")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std1_img_btn=Image.open("Images_GUI/chem.jpg")
        std1_img_btn=std1_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img11=ImageTk.PhotoImage(std1_img_btn)

        std_b11 = Button(bg_img,image=self.std_img11,cursor="hand2")
        std_b11.place(x=40,y=200,width=180,height=180)

        std_b1_11 = Button(bg_img,text="Rachelle Carillo",cursor="hand2",font=("Consolas",15,"bold"),bg="white",fg="#3B114B")
        std_b1_11.place(x=40,y=380,width=180,height=45)

        std_img_btn=Image.open("Images_GUI/cols.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=260,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Coleen Alejandrino",cursor="hand2",font=("Consolas",12,"bold"),bg="white",fg="#3B114B")
        std_b1_1.place(x=260,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open("Images_GUI/devid.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="David Natuel",cursor="hand2",font=("Consolas",15,"bold"),bg="white",fg="#3B114B")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open("Images_GUI/densiety.jpeg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=700,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Denise Bonsol",cursor="hand2",font=("Consolas",15,"bold"),bg="white",fg="#3B114B")
        att_b1_1.place(x=700,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open("Images_GUI/mariel.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=920,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Mariel Lagoc",cursor="hand2",font=("Consolas",15,"bold"),bg="white",fg="#3B114B")
        hlp_b1_1.place(x=920,y=380,width=180,height=45)


        hlp1_img_btn=Image.open("Images_GUI/ivy.jpg")
        hlp1_img_btn=hlp1_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img11=ImageTk.PhotoImage(hlp1_img_btn)

        hlp_b11 = Button(bg_img,image=self.hlp_img11,cursor="hand2",)
        hlp_b11.place(x=1140,y=200,width=180,height=180)

        hlp_b11_1 = Button(bg_img,text="Angelica de Torres",cursor="hand2",font=("Consolas",12,"bold"),bg="white",fg="#3B114B")
        hlp_b11_1.place(x=1140,y=380,width=180,height=45)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()