from pylatex import Document, Section, Subsection, Tabular, NoEscape
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, bold


doc = Document()
with doc.create(Section('Math Equations')):
    doc.append(
        'Attempt to create dynamic table i.e creating dynamic rows depending on the number of rows in Database, and displaying those values in PDF Table. \n \n')
    with doc.create(Tabular('|p{3cm}|p{7cm}|p{3cm}|')) as table:
        table.add_hline()
        table.add_row(bold('Dane'), bold('Obliczenia'), bold('Wyniki'))
        table.add_hline()
        table.add_row('', NoEscape(r'$$m_{no} = \frac{a_w * 2 * cos(\beta)}{z_1 * (1 + u)}$$'), '')
        table.add_hline()

doc.generate_pdf('Example_equation', compiler='pdflatex')


