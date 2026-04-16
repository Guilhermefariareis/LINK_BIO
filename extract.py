import fitz  # PyMuPDF
import os

pdf_path = "Mídia Kit - Jéssica Vitória.pdf"
output_dir = "midia_kit_assets"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Use a zoom factor to increase resolution (e.g., 2.0 = 200% zoom)
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)

for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_dir, f"page_{i + 1:02d}.jpg")
    pix.save(output_path)
    print(f"Saved {output_path}")

print("Extraction complete.")
