# Audio-Image-Plotter

This project implements two separate Python applications: one for visualizing audio waveforms from `.wav` files and another for displaying `.bmp` images. Both applications feature graphical user interfaces (GUIs) built using the `tkinter` library. The audio plotting program processes binary audio data and visualizes stereo channels, while the image viewer displays bitmap images on a canvas.

## Components

### 1. Audio Plotting Program
   - This program reads `.wav` audio files, extracts binary data, and plots the left and right audio channels as waveforms on a `tkinter` canvas.

### 2. BMP Image Viewer
   - This program opens and displays `.bmp` image files in a `tkinter` window.
     
## How to Run

### 1. Audio Plotting Program:
   - Run the program:
     ```bash
     python wavPlot.py
     ```

### 2. BMP Image Viewer:
   - Ensure you have the required libraries installed:
     ```bash
     pip install pillow
     ```
   - Run the program:
     ```bash
     python imagePlot.py
     ```

