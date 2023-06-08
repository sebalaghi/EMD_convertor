import os
from tkinter import Tk, Label, Button, filedialog, messagebox
import hyperspy.api as hs
from tifffile import imwrite
import numpy as np
from scipy.ndimage import zoom

# Function to convert emd to tiff
def emd_to_tiff(emd_filename, tiff_filename):
    s = hs.load(emd_filename)
    data = s.data

    # Get the original pixel size
    pixel_size = s.axes_manager[0].scale

    # Ensure that the data is in a format suitable for saving as TIFF
    if data.dtype != np.uint8:
        data = (data - data.min()) / (data.max() - data.min()) * 255
        data = data.astype(np.uint8)

    # Save data as multi-page TIFF with pixel size metadata
    imwrite(tiff_filename, data, resolution=(1/pixel_size, 1/pixel_size), metadata={'unit': 'nm'})


class App:
    def __init__(self, root):
        self.root = root
        root.title("EMD to TIFF converter")

        self.emd_filenames = []
        self.output_dir = None

        self.label = Label(root, text="Select EMD files and output directory")
        self.label.pack()

        self.select_emd_button = Button(root, text="Select EMD files", command=self.select_emd_files)
        self.select_emd_button.pack()

        self.select_output_dir_button = Button(root, text="Select output directory", command=self.select_output_dir)
        self.select_output_dir_button.pack()

        self.convert_button = Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.footnote_label = Label(root, text="by S. Esmael Balaghi")
        self.footnote_label.pack()

    def select_emd_files(self):
        self.emd_filenames = filedialog.askopenfilenames()

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()

    def convert(self):
        if not self.emd_filenames:
            print("Please select EMD files")
            return
        if not self.output_dir:
            print("Please select output directory")
            return
        for emd_filename in self.emd_filenames:
            tiff_filename = os.path.join(self.output_dir, os.path.splitext(os.path.basename(emd_filename))[0] + '.tiff')
            emd_to_tiff(emd_filename, tiff_filename)

        messagebox.showinfo("Task Complete", "Conversion of EMD files to TIFF is completed successfully!")

root = Tk()
app = App(root)
root.mainloop()

#%%
