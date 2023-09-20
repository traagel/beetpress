from pptx import Presentation
from pptx.util import Inches

# Initialize a presentation object with a template
prs = Presentation("temp.pptx")

# Read data from a text file
with open("slide_content.txt", "r") as f:
    lines = f.readlines()

# Loop through each line in the file to create slides
for line in lines:
    slide_layout = prs.slide_layouts[1]  # Choose the layout you prefer from the template
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]

    # Set the title and content for each slide
    title.text = "Algorithms and Data Structures"
    content.text = line.strip()

# Save the presentation
prs.save("lecture_slides.pptx")

