from pptx import Presentation
from pptx.dml.color import ColorFormat, RGBColor
slides = prs.slides

shapes = slides[11].shapes
for shape in shapes:

    if shape.name == "stufe_cred_1":
        shape.fill.solid()
        shape.fill.fore_color.RGB  = RGBColor(255, 0, 0)
        break

