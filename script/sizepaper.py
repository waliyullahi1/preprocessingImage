import math
import cv2
from docx import Document
from docx.shared import Inches

# Read the image
img = cv2.imread('.ocr/note.jpg')

# Get the shape of the image
height, width, _ = img.shape

# Image dimensions in pixels
width_pixels = width
height_pixels = height

# DPI (Dots Per Inch)
dpi = 96

# Calculate paper size in inches
width_inch = width_pixels / dpi
height_inch = height_pixels / dpi

# Print paper size
print(f"Paper size: {width_inch:.2f} x {height_inch:.2f} inches")

# Match paper size to a standard size
paper_sizes = {
    "A4": (8.27, 11.69),
    "Letter": (8.5, 11),
    "Legal": (8.5, 14)
}

# Convert paper size values to floats
paper_sizes = {k: (float(v[0]), float(v[1])) for k, v in paper_sizes.items()}

# Find the closest paper size
closest_size = min(paper_sizes, key=lambda x: math.hypot(paper_sizes[x][0]-width_inch, paper_sizes[x][1]-height_inch))
print(f"Closest standard paper size: {closest_size}")

# Create a Word document template with the specified width and height
doc = Document()
section = doc.sections[0]
section.page_width = Inches(width_inch)
section.page_height = Inches(height_inch)
doc.save("template.docx")
