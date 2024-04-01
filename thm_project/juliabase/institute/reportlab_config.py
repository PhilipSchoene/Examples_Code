# This file is part of JuliaBase-Institute.

import os.path
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


dejavu_root = "/usr/share/fonts/truetype/dejavu"
if os.path.exists(os.path.join(dejavu_root, "DejaVuSans.ttf")):
    pdfmetrics.registerFont(TTFont("DejaVu", os.path.join(dejavu_root, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuOb", os.path.join(dejavu_root, "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuBd", os.path.join(dejavu_root, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuBdOb", os.path.join(dejavu_root, "DejaVuSans-BoldOblique.ttf")))
    default_fontname = "DejaVu"
    pdfmetrics.registerFontFamily(default_fontname, normal="DejaVu", bold="DejaVuBd", italic="DejaVuOb",
                                  boldItalic="DejaVuBdOb")
    reportlab.rl_config.canvas_basefontname = default_fontname
