from PyQt5.QtGui import QDoubleValidator, QValidator
from data.linear_functions import *
from decimal import Decimal
from data.correction_factors_diag import *
import Gear_UI
import sys
import math
import numpy

import OpenGL.GL as gl
import OpenGL.arrays.vbo as glvbo

from data.input_data import *
from data.materials import *
from data.results import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PyQt5.QtCore import Qt
import data.pdf_file_creator

WINDOW_SIZE = 0


class RangeDoubleValidator(QDoubleValidator):
    def __init__(self, *__args):
        super().__init__(*__args)

    def validate(self, p_str, p_int):
        result, _, _ = super(RangeDoubleValidator, self).validate(p_str, p_int)
        if result is QValidator.Invalid:
            return super(RangeDoubleValidator, self).validate(p_str, p_int)
        else:
            if not p_str:
                return QValidator.Acceptable, p_str, p_int
            try:
                Decimal(p_str)
            except:
                return QValidator.Invalid, p_str, p_int
            num = Decimal(p_str.replace(',', '.'))
            if self.bottom() <= num <= self.top() and 0 <= -num.as_tuple().exponent <= self.decimals():
                return QValidator.Acceptable, p_str, p_int
            else:
                return QValidator.Invalid, p_str, p_int


class MyForm(QMainWindow):
    ENABLED_BTN_STYLE_SHEET = """QPushButton{
                color: rgb(242, 242, 246);\n
                background-color: rgb(76, 118, 232);\n
                border: none;\n
                height: 40;\n
                }
                QPushButton:hover{background-color: rgb(61, 101, 206);}"""

    #załadowanie punktów tworzących proste
    LIST_OF_POINTS = PointsForLinearFunctions.LIST_OF_POINTS
    GIVEN_POINT = []

    def __init__(self):
        super().__init__()
        self.ui = Gear_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Button click events to our top bar buttons
        #
        # Minimize window
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.ui.close_btn.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.ui.restore_btn.clicked.connect(lambda: self.restore_or_maximize_window())
        #setting default page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_input_data)
        #setting default value for combo box
        self.toggle_material_combo_box(True)
        #headers buttons functionality
        self.ui.materials_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.page_input_data, self.ui.materials_btn))
        self.ui.input_btn.clicked.connect(lambda: self.set_current_page(self.ui.page_preconditions, self.ui.input_btn))
        self.ui.base_outcome_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.page_preliminary_results, self.ui.base_outcome_btn))
        self.ui.factors_btn.clicked.connect(lambda: self.set_current_page(self.ui.page_corection_factors, self.ui.factors_btn))
        self.ui.diameters_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.page_outcomes, self.ui.diameters_btn))
        self.ui.excel_btn.clicked.connect(lambda: self.set_current_page(self.ui.page_excel, self.ui.excel_btn))
        self.ui.scheme_btn.clicked.connect(lambda: self.set_current_page(self.ui.page_scheme, self.ui.scheme_btn))

        self.ui.pushButton.clicked.connect(lambda: self.create_pdf_file_with_pylatex())

        #clear and calculate buttons on both pages
        self.ui.clear_btn.clicked.connect(lambda: self.clear_input_data(True))
        self.ui.preconditions_clear_btn.clicked.connect(lambda: self.clear_input_data(False))
        self.ui.calculate_btn.clicked.connect(lambda: self.get_and_validate_input_data())
        self.ui.preconditions_calculate_btn.clicked.connect(lambda: self.get_and_validate_input_data())

        #control material combo box based on radio buttons
        self.ui.radio_btn_soft_wheels.clicked.connect(lambda: self.toggle_material_combo_box(True))
        self.ui.radio_btn_hard_wheels.clicked.connect(lambda: self.toggle_material_combo_box(False))

        #enable next parts of calculations after confirming normal module value and 2nd gear tooth number value
        self.ui.normal_module_confirm_btn.clicked.connect(lambda: self.enable_next_geometric_parameters_after_confirming_normal_module())
        self.ui.second_wheel_tooth_number_confirm_btn.clicked.connect(lambda: self.calculate_real_ratio_after_setting_2nd_wheel_tooth_number())

        #put point on graph
        self.ui.graph_generate_button.clicked.connect(lambda: self.put_given_point_on_correction_factors_graph())
        self.ui.bring_back_defaults_btn.clicked.connect(lambda: self.default_values_for_correction_factors_graph())


        #set validators for user's interactive line Edits
        self.power_validator = RangeDoubleValidator()
        self.power_validator.setRange(0.0, 1000, 6)
        self.ui.lineEdit_power.setValidator(self.power_validator)
        self.ratio_validator = RangeDoubleValidator()
        self.ratio_validator.setRange(0.0, 950, 3)
        self.ui.lineEdit_ratio.setValidator(self.ratio_validator)
        self.velocity_in_validator = RangeDoubleValidator()
        self.velocity_in_validator.setRange(0.0, 30000, 3)
        self.ui.lineEdit_velocity_in.setValidator(self.velocity_in_validator)
        self.velocity_out_validator = RangeDoubleValidator()
        self.velocity_out_validator.setRange(0.0, 30000, 3)
        self.ui.lineEdit_velocity_out.setValidator(self.velocity_out_validator)
        self.durability_validator = RangeDoubleValidator()
        self.durability_validator.setRange(0.0, 72e6, 3)
        self.ui.lineEdit_durability.setValidator(self.durability_validator)
        self.wheelbase_validator = RangeDoubleValidator()
        self.wheelbase_validator.setRange(0, 1000, 3)
        self.ui.lineEdit_wheelbase.setValidator(self.wheelbase_validator)
        self.pressure_angle_validator = RangeDoubleValidator()
        self.pressure_angle_validator.setRange(0, 90, 3)
        self.ui.lineEdit_pressure_angle.setValidator(self.pressure_angle_validator)

        self.currentButton = self.ui.materials_btn
        self.ui.MplWidget.canvas.graph.set_title('Współczynniki korekcji')

        # Restore or maximize your window

        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if not self.isMaximized():  # Not maximized
                # Move window only when window is normal size
                # ###############################################
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################

        self.ui.main_header.mouseMoveEvent = moveWindow

        self.show()

    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # ###############################################

    # ###############################################

    def restore_or_maximize_window(self):

        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1
            # Update value to show that the window has been maximized
            self.showMaximized()
        # Update button icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()


    def set_current_page(self, page, next_button: QPushButton):
        self.currentButton.setStyleSheet("""QPushButton{
            color: rgb(242, 242, 246);\n
            background-color: rgb(76, 118, 232);\n
            border: none;\n
            height: 40;\n
            }
            QPushButton:hover{background-color: rgb(61, 101, 206);}"""
                                         )
        next_button.setStyleSheet("""QPushButton{
            background-color: rgb(51, 82, 148);\n
            border-bottom: 3px solid rgb(33, 38, 55);\n
            height: 40;\n}"""
                                  )

        self.currentButton = next_button
        self.ui.stackedWidget.setCurrentWidget(page)


    def clear_input_data(self, which_page):
        if which_page:
            self.ui.lineEdit_power.clear()
            self.ui.lineEdit_ratio.clear()
            self.ui.lineEdit_velocity_in.clear()
            self.ui.lineEdit_velocity_out.clear()
            self.ui.lineEdit_durability.clear()
            self.ui.comboBox_power.setCurrentIndex(0)
            self.ui.comboBox_velocity_in.setCurrentIndex(0)
            self.ui.comboBox_velocity_out.setCurrentIndex(0)
            self.ui.comboBox_driven_machine.setCurrentIndex(0)
            self.ui.comboBox_driving_machine.setCurrentIndex(0)
            self.ui.comboBox_durability.setCurrentIndex(0)
            self.ui.lineEdit_wheelbase.clear()
            self.ui.comboBox_wheelbase.setCurrentIndex(0)
        else:
            self.ui.comboBox_pinion_material.setCurrentIndex(0)
            self.ui.comboBox_wheel_material.setCurrentIndex(0)
            self.ui.comboBox_accuracy_class.setCurrentIndex(0)
            self.ui.lineEdit_pressure_angle.clear()
            self.ui.comboBox_helix_angle.setCurrentIndex(0)
            self.ui.comboBox_teeth_number.setCurrentIndex(0)

    def get_and_validate_input_data(self):
        power, ratio, velocity_in, velocity_out, machine_driving, machine_driven, durability, wheelbase, pressure_angle = \
            self.ui.lineEdit_power.text(), \
            self.ui.lineEdit_ratio.text(), \
            self.ui.lineEdit_velocity_in.text(), \
            self.ui.lineEdit_velocity_out.text(), \
            self.ui.comboBox_driving_machine.currentText(), \
            self.ui.comboBox_driven_machine.currentText(), \
            self.ui.lineEdit_durability.text(), \
            self.ui.lineEdit_wheelbase.text(), \
            self.ui.lineEdit_pressure_angle.text()
        is_data_filled = not (
                    power == "" or ratio == "" or velocity_in == "" or velocity_out == "" or durability == "" or pressure_angle == "" or wheelbase == "")
        if not is_data_filled:
            self.display_message_box(QMessageBox.Warning,
                                     "Nie wszystkie dane wejściowe i założenia zostały uzupełnione",
                                     "Złe dane wejściowe", QMessageBox.Ok)
        if is_data_filled:
            self.enable_base_outcome_page()
            self.rewrite_input_data_to_variables()

    def enable_base_outcome_page(self):

        self.ui.base_outcome_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.base_outcome_btn.setEnabled(True)

    def enable_other_pages(self):

        self.ui.factors_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.factors_btn.setEnabled(True)
        self.ui.diameters_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.diameters_btn.setEnabled(True)
        self.ui.excel_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.excel_btn.setEnabled(True)
        self.ui.scheme_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.scheme_btn.setEnabled(True)


    def toggle_material_combo_box(self, is_soft):
        if is_soft:
            self.ui.comboBox_pinion_material.clear()
            self.ui.comboBox_pinion_material.addItems(
                [WheelMaterial.ST4.value, WheelMaterial.ST5.value, WheelMaterial.ST6.value, WheelMaterial.ST7.value,
                 WheelMaterial._20.value,
                 WheelMaterial._45.value, WheelMaterial._55.value, WheelMaterial._30H.value, WheelMaterial._40H.value,
                 WheelMaterial._40HM.value,
                 WheelMaterial._34HNM.value])
            self.ui.comboBox_wheel_material.clear()
            self.ui.comboBox_wheel_material.addItems(
                                                    [WheelMaterial.ST4.value, WheelMaterial.ST5.value,
                                                     WheelMaterial.ST6.value, WheelMaterial.ST7.value,
                                                     WheelMaterial._20.value, WheelMaterial._45.value,
                                                     WheelMaterial._55.value, WheelMaterial._30H.value,
                                                     WheelMaterial._40H.value,WheelMaterial._40HM.value,
                                                     WheelMaterial._34HNM.value])
        else:
            self.ui.comboBox_pinion_material.clear()
            self.ui.comboBox_pinion_material.addItems(
                [WheelMaterial._15.value, WheelMaterial._16HG.value, WheelMaterial._18HGT.value, WheelMaterial._19HM.value,
                 WheelMaterial._15HN.value,
                 WheelMaterial._45.value, WheelMaterial._18H2N2.value, WheelMaterial._17HNM.value,
                 WheelMaterial._40HM.value])
            self.ui.comboBox_wheel_material.clear()
            self.ui.comboBox_wheel_material.addItems(
                [WheelMaterial._15.value, WheelMaterial._16HG.value, WheelMaterial._18HGT.value,
                 WheelMaterial._19HM.value,
                 WheelMaterial._15HN.value,
                 WheelMaterial._45.value, WheelMaterial._18H2N2.value, WheelMaterial._17HNM.value,
                 WheelMaterial._40HM.value])

    def rewrite_input_data_to_variables(self):
        InputData.power = float(self.ui.lineEdit_power.text())
        InputData.power_unit = self.ui.comboBox_power.currentText()
        InputData.ratio = float(self.ui.lineEdit_ratio.text())
        InputData.rad_velocity_in = float(self.ui.lineEdit_velocity_in.text())
        InputData.rad_velocity_in_unit = self.ui.comboBox_velocity_in.currentText()
        InputData.rad_velocity_out = float(self.ui.lineEdit_velocity_out.text())
        InputData.rad_velocity_out_unit = self.ui.comboBox_velocity_out.currentText()
        InputData.driving_machine = self.ui.comboBox_driving_machine.currentText()
        InputData.driven_machine = self.ui.comboBox_driven_machine.currentText()
        InputData.durability = float(self.ui.lineEdit_durability.text())
        InputData.durability_unit = self.ui.comboBox_durability.currentText()
        InputData.wheelbase = float(self.ui.lineEdit_wheelbase.text())
        InputData.wheelbase_unit = self.ui.comboBox_wheelbase.currentText()
        InputData.pinion_material = self.ui.comboBox_pinion_material.currentText()
        InputData.wheel_material = self.ui.comboBox_wheel_material.currentText()
        InputData.accuracy_class = self.ui.comboBox_accuracy_class.currentText()
        InputData.pressure_angle = float(self.ui.lineEdit_pressure_angle.text())
        InputData.helix_angle = float(self.ui.comboBox_helix_angle.currentText())
        InputData.pinion_tooth_number = float(self.ui.comboBox_teeth_number.currentText())
        InputData.power = self.units_conversion(InputData.power, InputData.power_unit)
        InputData.rad_velocity_in = self.units_conversion(InputData.rad_velocity_in, InputData.rad_velocity_in_unit)
        InputData.rad_velocity_out = self.units_conversion(InputData.rad_velocity_out, InputData.rad_velocity_out_unit)
        InputData.durability = self.units_conversion(InputData.durability, InputData.durability_unit)
        InputData.wheelbase = self.units_conversion(InputData.wheelbase, InputData.wheelbase_unit)
        self.calculate_on_input_data()

    def rewrite_results_data_to_line_edits(self):
        self.ui.lineEdit_pinion_torque.setText(str(Result.pinion_torque))
        self.ui.lineEdit_calculated_normal_module.setText(str(Result.calculated_normal_module))
        self.ui.lineEdit_bottom_ratio_border.setText(str(Result.ratio_bottom_border))
        self.ui.lineEdit_upper_ratio_border.setText(str(Result.ratio_upper_border))
        self.ui.lineEdit_calculated_tooth_number.setText(str(Result.calculated_2nd_wheel_tooth_number))

    def rewrite_outcome_to_line_edits(self):
        self.ui.lineEdit_wheelbase_zero.setText(str(Result.wheelbase_zero))
        self.ui.lineEdit_estimated_correction_factors_sum.setText(str(Result.estimated_correction_factors_sum))
        self.ui.lineEdit_alfa_t.setText(str(Result.alfa_t))
        self.ui.lineEdit_alfa_tw.setText(str(Result.alfa_tw))
        self.ui.lineEdit_inv_alfa_tw.setText(str(Result.inv_alfa_tw))
        self.ui.lineEdit_inv_alfa_t.setText(str(Result.inv_alfa_t))
        self.ui.lineEdit_correction_factors_sum.setText(str(Result.correction_factors_sum))
        self.ui.lineEdit_beta_b_helix_angle.setText(str(Result.beta_b_helix_angle))
        self.ui.lineEdit_pinion_tooth_number_placeholder.setText(str(Result.pinion_tooth_number_placeholder))
        self.ui.lineEdit_second_wheel_tooth_number_placeholder.setText(str(Result.second_wheel_tooth_number_placeholder))
        self.ui.lineEdit_pinion_correction_factor.setText(str(Result.pinion_correction_factor))
        self.ui.lineEdit_second_wheel_correction_factor.setText(str(Result.second_wheel_correction_factor))
        self.ui.lineEdit_pinion_rolling_diameter.setText(str(Result.pinion_rolling_diameter))
        self.ui.lineEdit_second_wheel_rolling_diameter.setText(str(Result.second_wheel_rolling_diameter))
        self.ui.lineEdit_wheelbase_aparent.setText(str(Result.wheelbase_apparent))
        self.ui.lineEdit_slip_factor.setText(str(Result.slip_factor))
        self.ui.lineEdit_pinion_pitch_diameter.setText(str(Result.pinion_pitch_diameter))
        self.ui.lineEdit_second_wheel_pitch_diameter.setText(str(Result.second_wheel_pitch_diameter))
        self.ui.lineEdit_frontal_module.setText(str(Result.frontal_module))
        self.ui.lineEdit_pinion_torque_outcome.setText(str(Result.pinion_torque))
        self.ui.lineEdit_force_tangential.setText(str(Result.force_tangential))
        self.ui.lineEdit_force_longitudinal.setText(str(Result.force_longitudinal))
        self.ui.lineEdit_force_radial.setText(str(Result.force_radial))
        self.ui.lineEdit_second_wheel_width.setText(str(Result.second_wheel_width))
        self.ui.lineEdit_stepping_pressure_number.setText(str(Result.stepping_pressure_number))

    def calculate_on_input_data(self):
        Result.pinion_torque = InputData.power / InputData.rad_velocity_in
        Result.calculated_normal_module = (InputData.wheelbase * 2 * math.cos(numpy.deg2rad(InputData.helix_angle))) / (InputData.pinion_tooth_number * (1 + InputData.ratio))
        Result.calculated_2nd_wheel_tooth_number = InputData.pinion_tooth_number * InputData.ratio

        if 1 <= InputData.ratio <= 4.5:
            Result.ratio_bottom_border = 0.975 * InputData.ratio
            Result.ratio_upper_border = 1.025 * InputData.ratio
        elif 5 <= InputData.ratio <= 224:
            Result.ratio_bottom_border = 0.96 * InputData.ratio
            Result.ratio_upper_border = 1.04 * InputData.ratio
        elif InputData.ratio >= 250:
            Result.ratio_bottom_border = 0.95 * InputData.ratio
            Result.ratio_upper_border = 1.05 * InputData.ratio
        self.rewrite_results_data_to_line_edits()

    def enable_next_geometric_parameters_after_confirming_normal_module(self):
        Result.normal_module = float(self.ui.comboBox_normal_module.currentText())
        self.ui.lineEdit_2nd_wheel_tooth_number.setEnabled(True)


    def calculate_real_ratio_after_setting_2nd_wheel_tooth_number(self):
        Result.second_wheel_tooth_number = self.ui.lineEdit_2nd_wheel_tooth_number.text()
        if Result.second_wheel_tooth_number == "":
            self.display_message_box(QMessageBox.Warning, "Podaj liczbę zębów drugiego koła", "Błąd przełożenia", QMessageBox.Ok)
        else:
            Result.second_wheel_tooth_number = float(Result.second_wheel_tooth_number)
            Result.real_ratio = Result.second_wheel_tooth_number / InputData.pinion_tooth_number
            if Result.ratio_bottom_border <= Result.real_ratio \
                    <= Result.ratio_upper_border:
                self.ui.lineEdit_real_ratio.setText(str(Result.real_ratio))
                self.further_calculations_for_outputs_page()
                self.enable_other_pages()
                self.generate_basic_version_of_the_graph()
                self.draw_scheme()
            else:
                self.display_message_box(QMessageBox.Warning, f"Wartość przełożenia musi mieścić się w przediale {Result.ratio_bottom_border} < u < {Result.ratio_upper_border}. Obecna wartość przełożenia to {Result.real_ratio}. Zmień liczbę zębów drugiego koła.", "Błąd przełożenia", QMessageBox.Ok)

    # draws each linear function on plot
    def draw_line_function_based_on_m_and_c(self, m, c, x_lower_border, x_upper_border, linecolor):
        x = numpy.linspace(x_lower_border, x_upper_border, 1000)
        y = m * x + c
        self.ui.MplWidget.canvas.graph.plot(x, y, color=linecolor)

    def generate_basic_version_of_the_graph(self):
        self.ui.MplWidget.canvas.graph.clear()
        LIST_OF_POINTS = PointsForLinearFunctions.LIST_OF_POINTS
        LIST_OF_FUNCTIONS = []
        for point in LIST_OF_POINTS:
            function = get_straight_linear(point)
            LIST_OF_FUNCTIONS.append(function)
        for i in range(0, len(LIST_OF_FUNCTIONS)):
            self.draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[i][0], LIST_OF_FUNCTIONS[i][1], 10, 150, 'blue')
        self.ui.MplWidget.canvas.graph.set_xlim(10, 150)
        self.ui.MplWidget.canvas.graph.set_ylim(-0.5, 1)
        self.ui.MplWidget.canvas.draw()


    def generate_correction_factors_graph(self):
        self.ui.MplWidget.canvas.graph.clear()
        # constant with previously defined points.
        LIST_OF_POINTS = PointsForLinearFunctions.LIST_OF_POINTS
        LIST_OF_FUNCTIONS = []

        # creating linear functions represented by y = mx + c from the list of points each of them consist of
        for point in LIST_OF_POINTS:
            function = get_straight_linear(point)
            LIST_OF_FUNCTIONS.append(function)
        # constants which help to indentify function we search for
        indexes_of_functions_above_given_point = []
        indexes_of_functions_below_given_point = []

        # iterate through list of functions to check whether it is below or above the given point and draw all functions on plot
        for i in range(0, len(LIST_OF_FUNCTIONS)):
            self.draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[i][0], LIST_OF_FUNCTIONS[i][1], 10, 150, 'blue')
            is_above_function = check_if_the_point_is_above_function(self.GIVEN_POINT, LIST_OF_FUNCTIONS[i][0], LIST_OF_FUNCTIONS[i][1])
            if is_above_function:
                indexes_of_functions_below_given_point.append(i)
            else:
                indexes_of_functions_above_given_point.append(i)

        # get the functions which are right above and right below the given point from lists of functions
        function_above_given_point = indexes_of_functions_above_given_point[0]
        function_below_given_point = indexes_of_functions_below_given_point[-1]

        # overdraw functions right above and right below the given point with different color
        self.draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[function_above_given_point][0], LIST_OF_FUNCTIONS[function_above_given_point][1], -50, 150, 'orange')
        self.draw_line_function_based_on_m_and_c(LIST_OF_FUNCTIONS[function_below_given_point][0], LIST_OF_FUNCTIONS[function_below_given_point][1], -50, 150, 'orange')

        cross_point_x, cross_point_y = find_cross_point_of_two_functions(
            LIST_OF_FUNCTIONS[function_above_given_point][0],
            LIST_OF_FUNCTIONS[function_above_given_point][1],
            LIST_OF_FUNCTIONS[function_below_given_point][0],
            LIST_OF_FUNCTIONS[function_below_given_point][1])
        created_linear_func = get_straight_linear([(cross_point_x, cross_point_y), (self.GIVEN_POINT[0], self.GIVEN_POINT[1])])
        searched_correction_factor = created_linear_func[0] * InputData.pinion_tooth_number + created_linear_func[1]

        # plot settings
        self.ui.MplWidget.canvas.graph.set_xlim(-50, 150)
        self.ui.MplWidget.canvas.graph.set_ylim(-0.5, 1)
        self.ui.MplWidget.canvas.graph.plot(self.GIVEN_POINT[0], self.GIVEN_POINT[1], marker="o", markersize=5, markerfacecolor="red", markeredgecolor="red")
        self.ui.MplWidget.canvas.graph.plot(cross_point_x, cross_point_y, marker='o', markersize=5, markerfacecolor="red")
        self.ui.MplWidget.canvas.graph.plot(InputData.pinion_tooth_number, searched_correction_factor, marker='o', markersize=5, markerfacecolor="red")
        self.ui.MplWidget.canvas.graph.plot([InputData.pinion_tooth_number, InputData.pinion_tooth_number], [-0.5, searched_correction_factor], linestyle='dashed')
        self.ui.MplWidget.canvas.graph.plot([InputData.pinion_tooth_number, -50], [searched_correction_factor, searched_correction_factor], linestyle='dashed')
        self.ui.MplWidget.canvas.graph.axline([cross_point_x, cross_point_y], [self.GIVEN_POINT[0], self.GIVEN_POINT[1]])
        self.ui.MplWidget.canvas.graph.annotate(f'x1 = {round(searched_correction_factor, 3)}', xy=(-50, searched_correction_factor),
                                                xytext=(-50, searched_correction_factor), va='center', ha='right')
        self.ui.MplWidget.canvas.draw()

    def put_given_point_on_correction_factors_graph(self):

        if self.ui.factors_sum_line_edit.text() == "" or self.ui.tooth_number_sum_line_edit.text() == "":
            self.display_message_box(QMessageBox.Warning,
                                     f"Aby wygenerować punkt, podaj jego współrzędne.", f"Złe współrzędne", QMessageBox.Ok)

        elif not (-0.5 < float(self.ui.factors_sum_line_edit.text()) < 1 and 0 < float(self.ui.tooth_number_sum_line_edit.text()) < 150):
            self.display_message_box(QMessageBox.Warning,
                                     f"Punkt o podanych współrzędnych jest spoza zakresu wykresu. Zmień współrzędne punktu.", f"Złe współrzędne", QMessageBox.Ok)

        else:
            Result.half_of_correction_factors_sum = float(self.ui.factors_sum_line_edit.text())
            Result.half_of_pinion_and_wheel_tooth_number_sum = float(self.ui.tooth_number_sum_line_edit.text())
            self.GIVEN_POINT = [Result.half_of_pinion_and_wheel_tooth_number_sum, Result.half_of_correction_factors_sum]
            self.ui.MplWidget.canvas.graph.clear()
            self.generate_correction_factors_graph()

    def default_values_for_correction_factors_graph(self):
        Result.half_of_correction_factors_sum = Result.correction_factors_sum / 2
        Result.half_of_pinion_and_wheel_tooth_number_sum = (InputData.pinion_tooth_number + Result.second_wheel_tooth_number) / 2
        self.ui.factors_sum_line_edit.setText(str(Result.half_of_correction_factors_sum))
        self.ui.tooth_number_sum_line_edit.setText(str(Result.half_of_pinion_and_wheel_tooth_number_sum))
        self.generate_basic_version_of_the_graph()

    def further_calculations_for_outputs_page(self):
        Result.wheelbase_zero = ((InputData.pinion_tooth_number + Result.second_wheel_tooth_number)
                                 * Result.normal_module) / (2 * math.cos(numpy.deg2rad(InputData.helix_angle)))
        # RESULT.WHEELBASE_ZERO wyświetla poprawną wartość, mozna podpinać pod UI
        # POPRAWNA WARTOŚĆ PRZYBLIZONEGO WSPOLCZYNNIKA KOREKCJI ZWROCONA

        Result.alfa_t = math.atan(math.tan(numpy.deg2rad(InputData.pressure_angle)) / math.cos(numpy.deg2rad(InputData.helix_angle)))
        # POPRAWNIE OBLICZONA WARTOSC ALFA_T


        Result.alfa_tw = math.acos(Result.wheelbase_zero * math.cos(Result.alfa_t) / InputData.wheelbase)
        # POPRAWNIE OBLICZONA WARTOSC ALFA_TW

        Result.inv_alfa_tw = math.tan(Result.alfa_tw) - Result.alfa_tw
        # POPRAWNIE OBLICZONA WARTOSC

        Result.inv_alfa_t = math.tan(Result.alfa_t) - Result.alfa_t
        # POPRAWNIE OBLICZONA WARTOSC
        Result.estimated_correction_factors_sum = (InputData.wheelbase - Result.wheelbase_zero) / Result.normal_module

        Result.correction_factors_sum = ((Result.inv_alfa_tw - Result.inv_alfa_t) *
                                         (InputData.pinion_tooth_number + Result.second_wheel_tooth_number)) / \
                                        (2 * math.tan(numpy.deg2rad(InputData.pressure_angle)))

        # Send correct values for generating correction factors graph
        Result.half_of_correction_factors_sum = Result.correction_factors_sum / 2
        Result.half_of_pinion_and_wheel_tooth_number_sum = (InputData.pinion_tooth_number + Result.second_wheel_tooth_number) / 2
        self.GIVEN_POINT = [Result.half_of_pinion_and_wheel_tooth_number_sum, Result.half_of_correction_factors_sum]
        self.ui.factors_sum_line_edit.setText(str(Result.half_of_correction_factors_sum))
        self.ui.tooth_number_sum_line_edit.setText(str(Result.half_of_pinion_and_wheel_tooth_number_sum))

        Result.beta_b_helix_angle = math.atan(math.tan(numpy.deg2rad(InputData.helix_angle)) *
                                              math.cos(math.atan(math.tan(numpy.deg2rad(InputData.pressure_angle)) /
                                                                 math.cos(numpy.deg2rad(InputData.helix_angle)))))
        # POPRAWNIE OBLICZONA WARTOSC

        Result.pinion_tooth_number_placeholder = InputData.pinion_tooth_number / (math.cos(
            numpy.deg2rad(InputData.helix_angle)) * math.cos(Result.beta_b_helix_angle) ** 2)
        # POPRAWNIE OBLICZONA WARTOSC

        Result.second_wheel_tooth_number_placeholder = Result.second_wheel_tooth_number / (math.cos(
            numpy.deg2rad(InputData.helix_angle)) * math.cos(Result.beta_b_helix_angle) ** 2)
        # POPRAWNIE OBLICZONA WARTOSC

        Result.both_wheels_tooth_num_placeholder_avg = (Result.pinion_tooth_number_placeholder +
                                                        Result.second_wheel_tooth_number_placeholder) / 2

        Result.pinion_correction_factor = 0.35
        #self.generate_basic_version_of_the_graph()
        Result.second_wheel_correction_factor = Result.correction_factors_sum - Result.pinion_correction_factor

        Result.pinion_rolling_diameter = (2 * InputData.wheelbase) / (1 + Result.real_ratio)

        Result.second_wheel_rolling_diameter = Result.real_ratio * Result.pinion_rolling_diameter

        Result.wheelbase_apparent = Result.wheelbase_zero + Result.normal_module * (Result.pinion_correction_factor +
                                                                                    Result.second_wheel_correction_factor)

        Result.slip_factor = (Result.wheelbase_apparent - InputData.wheelbase) / Result.normal_module

        Result.pinion_pitch_diameter = (Result.normal_module *
                                        InputData.pinion_tooth_number) / math.cos(numpy.deg2rad(InputData.helix_angle))

        Result.second_wheel_pitch_diameter = 2 * Result.wheelbase_zero - Result.pinion_pitch_diameter
        # Wszystko dotychczas z dobrymi wartościami

        Result.frontal_module = Result.pinion_pitch_diameter / InputData.pinion_tooth_number

        Result.pinion_tooth_line_slope_diameter = math.atan((Result.pinion_rolling_diameter *
                                                             math.tan(numpy.deg2rad(InputData.helix_angle))) / Result.pinion_pitch_diameter)

        Result.second_wheel_tooth_line_slope_diameter = math.atan((Result.second_wheel_rolling_diameter *
                                                                   math.tan(numpy.deg2rad(InputData.helix_angle))) / Result.second_wheel_pitch_diameter)


        Result.force_tangential = 2 * Result.pinion_torque / (Result.pinion_rolling_diameter / 1000)

        Result.force_longitudinal = Result.force_tangential * math.tan(Result.pinion_tooth_line_slope_diameter)

        Result.force_radial = Result.force_tangential * math.tan(Result.alfa_tw)

        Result.second_wheel_width = 60
        Result.stepping_pressure_number = (Result.second_wheel_width *
                                           math.sin(numpy.deg2rad(InputData.helix_angle))) / (Result.normal_module * math.pi)
        self.rewrite_outcome_to_line_edits()

    def display_message_box(self, message_kind, text, title, buttons):
        msg_box = QMessageBox()
        msg_box.setIcon(message_kind)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(buttons)
        msg_box.exec()

    def draw_scheme(self):
        self.ui.driving_machine_label.setText(InputData.driving_machine)
        self.ui.driven_machine_label.setText(InputData.driven_machine)
        self.ui.openGLWidget_scheme.updateGL()

    def convert_string_for_label(self, string):
        string_divided = ''
        if len(string) > 10:
            i = 0

            for c in string:
                if c != ' ':
                    string_divided += c
                else:
                    i += 1
                    if i % 2 == 0:
                        string_divided += '\n'
                    else:
                        string_divided += ' '

        return string_divided

    def units_conversion(self, variable, unit):
        if unit == "kW":
            variable *= 10e2
        elif unit == "MW":
            variable *= 10e5
        elif unit == "obr/min":
            variable *= 2 * math.pi / 60
        elif unit == "h":
            variable *= 3600
        elif unit == "min.":
            variable *= 60
        elif unit == "m":
            variable *= 10e2
        elif unit == "cm":
            variable *= 10
        return variable

    def create_pdf_file_with_pylatex(self):
        data.pdf_file_creator.create_pdf_file()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(App.exec())
