# from openpyxl import Workbook
# from openpyxl.styles import *
# from openpyxl.utils import get_column_letter
# from data.input_data import InputData
#
# wb = Workbook()
#
# ws1 = wb.active
# ws1.title = 'Obliczenia'
# ws1.merge_cells("A1:C1")
# ws1.merge_cells("D1:I1")
# ws1.merge_cells('J1:L1')
# dane_header_cell = ws1.cell(row=1, column=1)
# dane_header_cell.value = 'Dane'
# dane_header_cell.alignment = Alignment(horizontal='center')
# obliczenia_header_cell = ws1.cell(row=1, column=4)
# obliczenia_header_cell.value = 'Obliczenia'
# obliczenia_header_cell.alignment = Alignment(horizontal='center')
# wyniki_header_cell = ws1.cell(row=1, column=10)
# wyniki_header_cell.value = 'Wyniki'
# wyniki_header_cell.alignment = Alignment(horizontal='center')
#
# for i in range(2, 10):
#     ws1.merge_cells(f'A{i}:C{i}')
#
# ws1.cell(row=2, column=1).value = f'Moc nominala {InputData.power}{InputData.power_unit}'
# ws1.cell(row=3, column=1).value = f'Przełożenie {InputData.ratio}'
# ws1.cell(row=4, column=1).value = f'Prędkość obrotowa na wale wejściowym {InputData.rad_velocity_in}{InputData.rad_velocity_in_unit}'
# ws1.cell(row=5, column=1).value = f'Prędkość obrotowa na wale wyjściowym {InputData.rad_velocity_out}{InputData.rad_velocity_out_unit}'
# ws1.cell(row=6, column=1).value = f'Maszyna napędzająca {InputData.driving_machine}'
# ws1.cell(row=7, column=1).value = f'Maszyna napędzana {InputData.driven_machine}'
#
# wb.save('generated_excel_report.xlsx')

from pylatex import Document, Section, NoEscape, LongTable
# from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import bold
from data.opisy import *
doc = Document()


def create_pdf_file():
    row1_column1, row1_column2, row1_column3 = create_descriptions_row1_columns1to3()
    row2_column1, row2_column2, row2_column3 = create_descriptions_row2_columns1to3()
    r3_col1, r3_col2, r3_col3 = create_descriptions_r3_col1to3()
    r4_col1, r4_col2, r4_col3 = create_description_r4_col1to3()
    r5_col1, r5_col2, r5_col3 = create_description_row5_col1to3()
    r6_col1, r6_col2, r6_col3 = create_description_r6_col1to3()
    r7_col1, r7_col2, r7_col3 = create_description_r7_col1to3()
    r8_col1, r8_col2, r8_col3 = create_description_r8_col1to3()
    with doc.create(Section('Wyniki obliczeń programu KALKULATOR PRZEKŁADNI WALCOWYCH')):
        doc.append('Poniższa tabela zawiera wyniki obliczeń programu, wraz z użytymi do obliczeń danymi i wzorami matematycznymi. \n \n')
        with doc.create(LongTable('|p{3cm}|p{7cm}|p{3cm}|')) as table:
            table.add_hline()
            table.add_row(bold('Dane'), bold('Obliczenia'), bold('Wyniki'))
            table.add_hline()
            table.add_row('', '', '')
            table.add_row(NoEscape(row1_column1), NoEscape(row1_column2), NoEscape(row1_column3))
            table.add_hline()
            table.add_row(NoEscape(row2_column1), NoEscape(row2_column2), NoEscape(row2_column3))
            table.add_hline()
            table.add_row(NoEscape(r3_col1), NoEscape(r3_col2), NoEscape(r3_col3))
            table.add_hline()
            table.add_row(NoEscape(r4_col1), NoEscape(r4_col2), NoEscape(r4_col3))
            table.add_hline()
            table.add_row(NoEscape(r5_col1), NoEscape(r5_col2), NoEscape(r5_col3))
            table.add_hline()
            table.add_row(NoEscape(r6_col1), NoEscape(r6_col2), NoEscape(r6_col3))
            table.add_hline()
            table.add_row(NoEscape(r7_col1), NoEscape(r7_col2), NoEscape(r7_col3))
            table.add_hline()
            table.add_row(NoEscape(r8_col1), NoEscape(r8_col2), NoEscape(r8_col3))
            table.add_hline()
    doc.generate_pdf('data/KalkulatorWyniki', compiler='pdflatex', clean_tex=False)
