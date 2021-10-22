from PyQt5.QtGui import QDoubleValidator, QValidator

from decimal import Decimal
import Gear_UI
import sys
import math
import numpy

from Code.data.input_data import *
from Code.data.preconditions import *
from Code.data.results import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PyQt5.QtCore import Qt

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
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_input_data)
        self.toggle_material_combo_box(True)
        self.ui.materials_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.page_input_data, self.ui.materials_btn))
        self.ui.input_btn.clicked.connect(lambda: self.set_current_page(self.ui.zalozenia_page, self.ui.input_btn))
        self.ui.base_outcome_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.wyniki_wstepne_page, self.ui.base_outcome_btn))
        self.ui.forces_btn.clicked.connect(lambda: self.set_current_page(self.ui.naprezenia_page, self.ui.forces_btn))
        self.ui.diameters_btn.clicked.connect(
            lambda: self.set_current_page(self.ui.srednice_page, self.ui.diameters_btn))
        self.ui.excel_btn.clicked.connect(lambda: self.set_current_page(self.ui.excel_page, self.ui.excel_btn))
        self.ui.scheme_btn.clicked.connect(lambda: self.set_current_page(self.ui.schemat_page, self.ui.scheme_btn))
        self.ui.clear_btn.clicked.connect(lambda: self.clear_input_data(True))
        self.ui.preconditions_clear_btn.clicked.connect(lambda: self.clear_input_data(False))
        self.ui.calculate_btn.clicked.connect(lambda: self.get_and_validate_input_date())
        self.ui.preconditions_calculate_btn.clicked.connect(lambda: self.get_and_validate_input_date())
        self.ui.radio_btn_soft_wheels.clicked.connect(lambda: self.toggle_material_combo_box(True))
        self.ui.radio_btn_hard_wheels.clicked.connect(lambda: self.toggle_material_combo_box(False))
        self.ui.normal_module_confirm_btn.clicked.connect(lambda: self.enable_next_geometric_parameters_after_confirming_normal_module())
        self.ui.second_wheel_tooth_number_confirm_btn.clicked.connect(lambda: self.calculate_real_ratio_after_setting_2nd_wheel_tooth_number())
        self.power_validator = RangeDoubleValidator()
        self.power_validator.setRange(0.0, 1000, 6)
        self.ui.lineEdit_power.setValidator(self.power_validator)
        self.ratio_validator = RangeDoubleValidator()
        self.ratio_validator.setRange(0.01, 300, 3)
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

        # self.ui.comboBox.setEditable(True)
        print(self.ui.stackedWidget.currentIndex())

        self.currentButton = self.ui.materials_btn

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
        # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))#Show maximized icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()

    # Update button icon
    # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))#Show minized icon

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

    def get_and_validate_input_date(self):
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
            self.enable_output_buttons()
            self.rewriting_input_data_to_variables()

    def enable_output_buttons(self):

        self.ui.base_outcome_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.base_outcome_btn.setEnabled(True)
        self.ui.forces_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.forces_btn.setEnabled(True)
        self.ui.diameters_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.diameters_btn.setEnabled(True)
        self.ui.excel_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.excel_btn.setEnabled(True)
        self.ui.scheme_btn.setStyleSheet(MyForm.ENABLED_BTN_STYLE_SHEET)
        self.ui.scheme_btn.setEnabled(True)

        # else:

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


    def rewriting_input_data_to_variables(self):
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
        print(f"Moc: {InputData.power}, Przełożenie: {InputData.ratio}, Prędkość wejściowa: {InputData.rad_velocity_in},"
              f" Prędkość wyjściowa: {InputData.rad_velocity_out}, Trwałość: {InputData.durability}, Rozstaw osi: {InputData.wheelbase}")
        self.calculate_on_input_data()

    def rewrite_results_data_to_line_edits(self):
        self.ui.lineEdit_pinion_torque.setText(str(Result.pinion_torque))
        self.ui.lineEdit_calculated_normal_module.setText(str(Result.calculated_normal_module))
        self.ui.lineEdit_bottom_ratio_border.setText(str(Result.ratio_bottom_border))
        self.ui.lineEdit_upper_ratio_border.setText(str(Result.ratio_upper_border))
        self.ui.lineEdit_calculated_tooth_number.setText(str(Result.calculated_2nd_wheel_tooth_number))

    def calculate_on_input_data(self):
        Result.pinion_torque = InputData.power / InputData.rad_velocity_in
        Result.calculated_normal_module = (InputData.wheelbase * 2 * math.cos(numpy.deg2rad(InputData.helix_angle))) / (InputData.pinion_tooth_number * (1 + InputData.ratio))
        Result.ratio_bottom_border = 0.975 * InputData.ratio
        Result.ratio_upper_border = 1.025 * InputData.ratio
        Result.calculated_2nd_wheel_tooth_number = InputData.pinion_tooth_number * InputData.ratio
        self.rewrite_results_data_to_line_edits()

    def enable_next_geometric_parameters_after_confirming_normal_module(self):
        Result.normal_module = self.ui.lineEdit_normal_module.text()
        if Result.normal_module == "":
            self.display_message_box(QMessageBox.Warning, "Nie została podana wartość modułu normalnego", "Moduł normalny", QMessageBox.Ok | QMessageBox.Cancel)
        else:
            self.ui.lineEdit_2nd_wheel_tooth_number.setEnabled(True)
            Result.normal_module = float(Result.normal_module)

    def calculate_real_ratio_after_setting_2nd_wheel_tooth_number(self):
        Result.second_wheel_tooth_number = self.ui.lineEdit_2nd_wheel_tooth_number.text()
        if Result.second_wheel_tooth_number == "":
            self.display_message_box(QMessageBox.Warning, "Podaj liczbę zębów drugiego koła", "Błąd przełożenia", QMessageBox.Ok)
        else:
            Result.second_wheel_tooth_number = float(Result.second_wheel_tooth_number)
            Result.real_ratio = Result.second_wheel_tooth_number / InputData.pinion_tooth_number
            if Result.ratio_bottom_border <= Result.real_ratio <= Result.ratio_upper_border:
                self.ui.lineEdit_real_ratio.setText(str(Result.real_ratio))
                self.prepare_values_for_further_ui_development()
            else:
                self.display_message_box(QMessageBox.Warning, f"Wartość przełożenia musi mieścić się w przediale {Result.ratio_bottom_border} < u < {Result.ratio_upper_border}. Obecna wartość przełożenia to {Result.real_ratio}. Zmień liczbę zębów drugiego koła.", "Błąd przełożenia", QMessageBox.Ok)

    def prepare_values_for_further_ui_development(self):
        Result.wheelbase_zero = ((InputData.pinion_tooth_number + Result.second_wheel_tooth_number)
                                 * Result.normal_module) / (2 * math.cos(numpy.deg2rad(InputData.helix_angle)))
        # RESULT.WHEELBASE_ZERO wyświetla poprawną wartość, mozna podpinać pod UI
        print(f"Zerowa odległośc osi: {Result.wheelbase_zero}")
        Result.estimated_correction_factors_sum = (InputData.wheelbase - Result.wheelbase_zero) / Result.normal_module
        print(f"Przybliżona wartość sumy wspólczynników korekcji (przesunięcia zarysu): {Result.estimated_correction_factors_sum}")
        # POPRAWNA WARTOŚĆ PRZYBLIZONEGO WSPOLCZYNNIKA KOREKCJI ZWROCONA

        Result.alfa_t = math.atan(math.tan(numpy.deg2rad(InputData.pressure_angle)) / math.cos(numpy.deg2rad(InputData.helix_angle)))
        print(f" Kąt zarysu w przekroju czołowym: {Result.alfa_t}")
        # POPRAWNIE OBLICZONA WARTOSC ALFA_T

        Result.alfa_tw = math.acos(Result.wheelbase_zero * math.cos(Result.alfa_t) / InputData.wheelbase)
        print(f"Kąt przyporu toczny w przekroju czołowym: {Result.alfa_tw}")
        # POPRAWNIE OBLICZONA WARTOSC ALFA_TW

        Result.inv_alfa_tw = math.tan(Result.alfa_tw) - Result.alfa_tw
        print(f"Involuta, funkcja ewolwentowa alfa_tw: {Result.inv_alfa_tw}")
        # POPRAWNIE OBLICZONA WARTOSC

        Result.inv_alfa_t = math.tan(Result.alfa_t) - Result.alfa_t
        print(f"Involuta, funkcja ewolwentowa alfa_t: {Result.inv_alfa_t}")
        # POPRAWNIE OBLICZONA WARTOSC

        Result.correction_factors_sum = ((Result.inv_alfa_tw - Result.inv_alfa_t) *
                                         (InputData.pinion_tooth_number + Result.second_wheel_tooth_number)) / \
                                        (2 * math.tan(numpy.deg2rad(InputData.pressure_angle)))
        print(f"Suma współczynników korekcji: {Result.correction_factors_sum}")

        Result.beta_b_helix_angle = math.atan(math.tan(numpy.deg2rad(InputData.helix_angle)) *
                                              math.cos(math.atan(math.tan(numpy.deg2rad(InputData.pressure_angle)) /
                                                                 math.cos(numpy.deg2rad(InputData.helix_angle)))))
        print(f"Kąt pochylenia linii zęba na walcu zasadniczym: {Result.beta_b_helix_angle}")
        # POPRAWNIE OBLICZONA WARTOSC

        Result.pinion_tooth_number_placeholder = InputData.pinion_tooth_number / (math.cos(
            numpy.deg2rad(InputData.helix_angle)) * math.cos(Result.beta_b_helix_angle) ** 2)
        print(f"Zastępcza liczba zębów zębnika: {Result.pinion_tooth_number_placeholder}")
        # POPRAWNIE OBLICZONA WARTOSC

        Result.second_wheel_tooth_number_placeholder = Result.second_wheel_tooth_number / (math.cos(
            numpy.deg2rad(InputData.helix_angle)) * math.cos(Result.beta_b_helix_angle) ** 2)
        print(f"Zastępcza liczba zębów koła: {Result.second_wheel_tooth_number_placeholder}")
        # POPRAWNIE OBLICZONA WARTOSC

        Result.both_wheels_tooth_num_placeholder_avg = (Result.pinion_tooth_number_placeholder +
                                                        Result.second_wheel_tooth_number_placeholder) / 2
        print(f"Średnia z zastępczej liczby zębów kół: {Result.both_wheels_tooth_num_placeholder_avg}")

        Result.pinion_correction_factor = 0.35
        Result.second_wheel_correction_factor = Result.correction_factors_sum - Result.pinion_correction_factor
        print(f"Współczynnik korekcji koła: {Result.second_wheel_correction_factor}")

        Result.pinion_rolling_diameter = (2 * InputData.wheelbase) / (1 + Result.real_ratio)
        print(f"Średnica toczna zębnika: {Result.pinion_rolling_diameter}")

        Result.second_wheel_rolling_diameter = Result.real_ratio * Result.pinion_rolling_diameter
        print(f"Średnica toczna koła: {Result.second_wheel_rolling_diameter}")

        Result.wheelbase_apparent = Result.wheelbase_zero + Result.normal_module * (Result.pinion_correction_factor +
                                                                                    Result.second_wheel_correction_factor)
        print(f"Pozorna odległość osi: {Result.wheelbase_apparent}")

        Result.slip_factor = (Result.wheelbase_apparent - InputData.wheelbase) / Result.normal_module
        print(f"Współczynnik zsunięcia: {Result.slip_factor}")

        Result.pinion_pitch_diameter = (Result.normal_module *
                                        InputData.pinion_tooth_number) / math.cos(numpy.deg2rad(InputData.helix_angle))
        print(f"Średnica podziałowa zębnika: {Result.pinion_pitch_diameter}")

        Result.second_wheel_pitch_diameter = 2 * Result.wheelbase_zero - Result.pinion_pitch_diameter
        print(f"Średnica podziałowa koła: {Result.second_wheel_pitch_diameter}")
        # Wszystko dotychczas z dobrymi wartościami

        Result.frontal_module = Result.pinion_pitch_diameter / InputData.pinion_tooth_number
        print(f"Moduł czołowy: {Result.frontal_module}")

        Result.pinion_tooth_line_slope_diameter = math.atan((Result.pinion_rolling_diameter *
                                                             math.tan(numpy.deg2rad(InputData.helix_angle))) / Result.pinion_pitch_diameter)
        print(f"Średnica pochylenia linii zęba na średnicy tocznej zębnika: {Result.pinion_tooth_line_slope_diameter}")

        Result.second_wheel_tooth_line_slope_diameter = math.atan((Result.second_wheel_rolling_diameter *
                                                                   math.tan(numpy.deg2rad(InputData.helix_angle))) / Result.second_wheel_pitch_diameter)
        print(f"Średnica pochylenia linii zęba na średnicy tocznej koła: {Result.second_wheel_tooth_line_slope_diameter}")

        print(f"Moment obrotowy obciążający zębnik: {Result.pinion_torque}")

        Result.force_tangential = 2 * Result.pinion_torque / (Result.pinion_rolling_diameter / 1000)
        print(f"Siła styczna: {Result.force_tangential}")

        Result.force_longitudinal = Result.force_tangential * math.tan(Result.pinion_tooth_line_slope_diameter)
        print(f"Siła wzdłużna: {Result.force_longitudinal}")

        Result.force_radial = Result.force_tangential * math.tan(Result.alfa_tw)
        print(f"Siła promieniowa: {Result.force_radial}")

        Result.second_wheel_width = 60
        print(f"Szerokość koła: {Result.second_wheel_width}")
        Result.stepping_pressure_number = (Result.second_wheel_width *
                                           math.sin(numpy.deg2rad(InputData.helix_angle))) / (Result.normal_module * math.pi)
        print(f"Poskokowa liczba przyporu: {Result.stepping_pressure_number}")

    def display_message_box(self, message_kind, text, title, buttons):
        msg_box = QMessageBox()
        msg_box.setIcon(message_kind)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(buttons)
        msg_box.exec()

    def units_conversion(self, variable, unit):
        if unit == "kW":
            variable *= 10e2
            print(f"Skonwertowane: {variable}")
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

    # input_data = InputData(power, ratio, velocity_in, velocity_out, machine_driving, machine_driven, durability)
    #
    #     if self.check_input_data(input_data):
    #         pass
    #
    # def check_input_data(self, input_data):
    #     if self.is_number(input_data.power) and self.power_validator
    #
    # def is_number(self, s):
    #     try:
    #         float(s)
    #         return True
    #     except ValueError:
    #         return False


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(App.exec())
