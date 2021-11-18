from data.input_data import InputData
from data.results import Result


def create_descriptions_row1_columns1to3():
        desc1 = f'Moc nominalna:\n' \
                f'N= {InputData.power} [N]\n\n' \
                f'Przełożenie:\n' \
                f'u= {InputData.ratio}\n\n' \
                f'Prędkość obrotowa na wale wejściowym:\n' \
                f'{round(InputData.rad_velocity_out, 2)} [rad/s]\n\n' \
                f'Prędkość obrotowa na wale wyjściowym:\n' \
                f'{round(InputData.rad_velocity_out, 2)} [rad/s]\n\n' \
                f'Odległość osi przekładni:\n' \
                f'aw = {InputData.wheelbase} [mm]'

        desc2 = f'Mając na uwadze projektowe parametry przekładni, dokonano następujących założeń: \n\n' \
                f'Materiał zębnika: {InputData.pinion_material} \n' \
                f'Materiał koła: {InputData.wheel_material} \n' \
                f'Klasa dokładności wykonania kół zębatych: {InputData.accuracy_class} \n' \
                f'Normalny kąt przyporu: {InputData.pressure_angle} \n' \
                f'Kąt pochylenia linii śrubowej zęba: {InputData.helix_angle}\n\n' \
                f'Moment obciążający zębnik:\n' \
                f'M1 = N / omega1 = {round(Result.pinion_torque, 3)}\n' \
                f'Liczba zębów zębnika (15-25):\n' \
                f'z1 = {InputData.pinion_tooth_number}'
        desc3 = f'.\n\n\n\n\n\n\n\n\n\n\n' \
                f'M1 = {round(Result.pinion_torque, 3)}'
        return desc1, desc2, desc3


def create_descriptions_row2_columns1to3():

        desc1 = f'.\n\n\n'\
                f'aw = {InputData.wheelbase} [mm]\n' \
                f'z1 = {InputData.pinion_tooth_number}'
        desc2 = f'Moduł normalny obliczeniowy:\n' \
                f'mno =aw * 2 * cos(B) / z1 * (1 + u) = {round(Result.calculated_normal_module), 3} [mm]\n' \
                f'Zgodnie z normą PN-323 przyjęto wartość modułu normalnego:\n' \
                f'mn = {Result.normal_module} [mm]\n\n' \
                f'Obliczeniowa liczba zębów drugiego koła:\n' \
                f'z2o = z1 * u = {round(InputData.ratio * InputData.pinion_tooth_number, 2)}\n\n' \
                f'Mając na uwadze, że liczby zębów kół współpracujących nie powinny miec wspólnego dzielnika przyjęto:\n' \
                f'z2 = {Result.second_wheel_tooth_number}'
        desc3 = f'.\nmno = {round(Result.calculated_normal_module)}\n\n\n\n' \
                f'mn = {Result.normal_module}\n\n\n' \
                f'z2o = {round(InputData.ratio * InputData.pinion_tooth_number, 2)}\n\n\n\n\n' \
                f'z2 = {Result.second_wheel_tooth_number}'
        return desc1, desc2, desc3


def create_descriptions_r3_col1to3():

        desc1 = f'.\n\n\n'\
                f'z1 = {InputData.pinion_tooth_number}\n' \
                f'z2 = {Result.second_wheel_tooth_number}\n' \
                f'mn = {Result.normal_module}\n'
        desc2 = f'Dolna granica błędu przełożenia przekładni:\n' \
                f'umin = 0,975 * u = {round(Result.ratio_bottom_border, 3)}\n\n' \
                f'Górna granica błędu przełożenia przekładni: \n' \
                f'umax = 1,025 * u = {round(Result.ratio_upper_border, 3)}\n\n' \
                f'Sprawdzenie czy przełożenie rzeczywiste mieści się w dopuszcalnym przedziale:\n' \
                f'urz = z2 / z1 = {round(Result.real_ratio, 3)}\n\n' \
                f'Zerowa odległość osi:\n' \
                f'ao = [(z1 + z2) * mn] / [2 * cos(B)] =\n= {round(Result.wheelbase_zero, 3)} [mm]\n'
        desc3 = f'.\n' \
                f'umin = {round(Result.ratio_bottom_border, 3)}\n\n\n' \
                f'umax = {round(Result.ratio_upper_border, 3)}\n\n\n\n' \
                f'urz = {round(Result.real_ratio, 3)}\n\n\n' \
                f'ao = {round(Result.wheelbase_zero, 3)}'

        return desc1, desc2, desc3

