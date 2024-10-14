import tkinter

from tkinter import filedialog #to search for file






from PIL import Image,ImageTk




class bmpView:
    def __init__(self, root):
        self.root = root #opens a GUI window
        self.root.title("display bmp"); # set title
        self.window = tkinter.Canvas(root, width=704, height=676, bg="white") #set the window
        self.window.pack() #add to canvas

        self.image = "" 
        self.photo = ""
        
        self.button = tkinter.Button(self.root, text="Open File", command=self.openFile);
        self.button.place(x=200,y=10)

        self.button = tkinter.Button(self.root, text="Exit", command=self.exit);
        self.button.place(x=600,y=10)

        self.imageLab = tkinter.Label(root)
        self.imageLab.place(x=0,y=100)


    def openFile(self):
    
        #look for bmp files
        path = filedialog.askopenfilename(filetypes=[("BMP", "*.bmp")]) 
        
        if path:
            print("selected")

        else:
            print("no file")

        with Image.open(path) as image:
            self.image = image.copy()
            self.photo = ImageTk.PhotoImage(self.image)

            self.imageLab.config(image=self.photo)
            

        #close window
    def exit(self):
        self.root.quit()

if __name__ == "__main__": 

    window = tkinter.Tk()
    bmpView(window) 
    window.mainloop()
