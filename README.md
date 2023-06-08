**EMD to TIFF Converter:**
This Python script provides a graphical user interface (GUI) for converting Electron Microscopy Datasets (EMD) to Tagged Image File Format (TIFF). This can be especially useful for researchers and data scientists working with electron microscopy data who want to convert their images into a more accessible format.

**Features:**
User-friendly GUI for selecting input EMD files and output directory.
Supports batch conversion of multiple EMD files.
Preserves the original pixel size in the converted TIFF images.
Includes pixel size (in nm) as metadata in the TIFF files.
A pop-up message appears when the conversion is complete.

**Usage:**
When you run the script, a GUI window will appear. Follow these steps to convert EMD files to TIFF:

Click on "Select EMD files" to choose the EMD files you want to convert.
Click on "Select output directory" to choose where you want to save the converted TIFF files.
Click on "Convert" to start the conversion process.
When the conversion is complete, a popup message will appear to inform you that the task is complete.

**Dependencies:**
The script depends on the following Python packages:

**hyperspy:** for loading EMD files.
**tifffile:** for writing TIFF files.
**tkinter:** for the GUI.
**numpy:** for handling the image data.
**scipy:** for resizing the image data.

Please ensure that you have these packages installed before running the script.

**Author:**
This script is written by S. Esmael Balaghi.
