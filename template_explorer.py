from pptx import Presentation

# Initialize a presentation object with a template
prs = Presentation("temp.pptx")

# Choose a slide layout (e.g., index 1)
slide_layout = prs.slide_layouts[1]

# Print all placeholder indices and their names
for i, placeholder in enumerate(slide_layout.placeholders):
    print(f"Placeholder index: {i}, Placeholder name: {placeholder.name}")

