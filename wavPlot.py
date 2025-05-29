import tkinter

from tkinter import filedialog #to search for file




import wave #to read wave

import struct #read binary data

import math # for maht funtions



class displayWaves:
    def __init__(self, root):
        self.root = root #opens a GUI window
        self.root.title("display waves")

        self.window = tkinter.Canvas(root, width=1000, height=1000, bg="white")
        self.window.pack()



        self.labelSample = tkinter.Label(root, text="total samples:                Sample freq:")
        self.labelSample.place(x=10,y=10)


        self.button = tkinter.Button(self.root, text="open file", command=self.openFile);
        self.button.place(x=500,y=10)

       

    def read(self, path):
        print("reading");

        with wave.open(path, 'rb') as file:

            #check if 16 bit per sample
            sampwidth = file.getsampwidth()
            if sampWidth == 2: # 2 bytes = 16 bits
                print("This is a 16-bit WAV file.")
            else:
                print("This is NOT a 16-bit WAV file.")
    
            totalSamples = file.getnframes()
            sampleFreq = file.getframerate()
            rawBinString = file.readframes(totalSamples)
            formatOf = "<" + "h" * (totalSamples * 2) # < for little h for fromat character of 16 bit  ints
            binUnpacked = struct.unpack(formatOf, rawBinString) #unpack the pairs fo binary data to  integers

            left = binUnpacked[0::2] # [starting:stopAt:steps]
            right = binUnpacked[1::2]
        print("returning values")
        return left, right, sampleFreq, totalSamples



    def plotWaves(self, left, right):
        self.window.delete("all") #clear canv

        maxLeftAmp = abs(max(left))
        minLeftAmp = abs(min(left))

        
        maxRightAmp = abs(max(right))
        minRightAmp = abs(min(right))

        maxLeft = max(maxLeftAmp, minLeftAmp)
        maxRight = max(maxRightAmp,minRightAmp)

        maxAbsAmpOfLeftANDRight= max(maxLeft,maxRight)

        if(maxAbsAmpOfLeftANDRight == 0):
            print("no volume")
       
        scaleX = 1000 / len(left) #how much space x can take
        scaleY = (250) / maxAbsAmpOfLeftANDRight # fit height of window

        
        #plot left
        for i in range(len(left)-1):
            x1 = scaleX * i 
            x2 = (i + 1) * scaleX #determin where x1 and x2 is

            y1 = 250 - left[i] *scaleY
            y2 = 250 - left[i + 1] * scaleY

            self.window.create_line(x1,y1,x2,y2, fill="green")

        #plot right
        for i in range(len(right)-1):
            x1 = scaleX * i 
            x2 = (i + 1) * scaleX #determin where x1 and x2 is

            y1 = 3 * 250 - right[i] * scaleY
            y2 = 3 * 250 - right[i + 1] * scaleY

            self.window.create_line(x1,y1,x2,y2, fill="green")

        
        

        
    
    def openFile(self):
            

            path = filedialog.askopenfilename(filetypes=[("WAV", "*.wav")])
            

            if path:
                print("selected")

            else:
                print("no file")

            left,right,sampleFreq, totalSamples = self.read(path)
         
            self.plotWaves(left,right)
    
            self.labelSample.config(text=f"Total Samples: {totalSamples} Sampling Freq: {sampleFreq} herts")



    




        


if __name__ == "__main__": 

    window = tkinter.Tk()
    displayWaves(window) 
    window.mainloop()
