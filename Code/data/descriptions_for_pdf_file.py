from data.input_data import InputData
from data.results import Result


def create_descriptions_row1_columns1to3():
        desc1 = r'\textbf{Moc nominalna:} \newline ' + 'N = ' + str(InputData.power) + r'\newline \textbf{Przełożenie:} \newline u = ' + str(InputData.ratio) + \
                r' \newline \textbf{Prędkość obrotowa na wale wejściowym:} \newline ' + r'$\omega = $' + str(round(InputData.rad_velocity_out, 2)) + \
                r' \newline \textbf{Prędkość obrotowa na wale wyjściowym:} \newline ' + r'$\omega = $' + str(round(InputData.rad_velocity_out, 2)) + \
                r' \newline \textbf{Odległość osi przekładni:} \newline ' + r'$a_w = $' + str(InputData.wheelbase)

        desc2 = r'Mając na uwadze projektowe parametry przekładni, dokonano następujących założeń: \newline ' \
                r' \newline Materiał zębnika: ' + str(InputData.pinion_material) + \
                r' \newline Materiał koła: ' + str(InputData.wheel_material) + \
                r' \newline Klasa dokładności wykonania kół zębatych: ' + str(InputData.accuracy_class) + \
                r' \newline Normalny kąt przyporu $\alpha_n$: ' + str(InputData.pressure_angle) + \
                r' \newline Kąt pochylenia linii śrubowej zęba $\beta$: ' + str(InputData.helix_angle) + \
                r' \newline Moment obciążający zębnik: \newline ' \
                r' \newline $M_1 = \frac{N}{\omega_1} = $' + str(round(Result.pinion_torque, 3)) + \
                r' \newline \newline Liczba zębów zębnika (15-25): ' \
                r'$z_1 = $' + str(InputData.pinion_tooth_number)
        desc3 = r'$ \newline \newline \newline \newline \newline \newline \newline \newline \newline \newline \newline M_1 = $' + str(round(Result.pinion_torque, 3))

        return desc1, desc2, desc3


def create_descriptions_row2_columns1to3():

        desc1 = r'$ \newline \newline \newline a_w = $' + str(InputData.wheelbase) + \
                r' [mm] \newline $z_1 = $' + str(InputData.pinion_tooth_number)
        desc2 = r'Moduł normalny obliczeniowy: \newline  \newline ' \
                r'$m_{no} = \frac{a_w * 2 * cos(\beta)}{z_1 * (1 + u)}$' + str(round(Result.calculated_normal_module, 3)) + \
                r' [mm] \newline  \newline Zgodnie z normą PN-323 przyjęto wartość modułu normalnego: \newline  \newline ' \
                r'$m_n = $' + str(Result.normal_module) + \
                r' [mm] \newline  \newline Obliczeniowa liczba zębów drugiego koła: \newline  \newline ' \
                r'$z_{2o} = z_1 * u = $' + str(round(InputData.ratio * InputData.pinion_tooth_number, 2)) + \
                r'  \newline \newline  Mając na uwadze, że liczby zębów kół współpracujących nie powinny miec wspólnego dzielnika przyjęto:  \newline  \newline ' \
                r'$z_2 = $' + str(Result.second_wheel_tooth_number)
        desc3 = r'$ \newline \newline  m_{no} = $' + str(round(Result.calculated_normal_module)) + \
                r'$ \newline  \newline  \newline  \newline  \newline m_n = $' + str(Result.normal_module) + \
                r'$ \newline  \newline  \newline  \newline z_{2o} = $' + str(round(InputData.ratio * InputData.pinion_tooth_number, 2)) + \
                r'$ \newline  \newline  \newline  \newline  \newline  \newline z_2 = $' + str(Result.second_wheel_tooth_number)
        return desc1, desc2, desc3


def create_descriptions_r3_col1to3():

        desc1 = r'$ \newline \newline \newline  z_ 1 = $' + str(InputData.pinion_tooth_number) + \
                r' \newline  \newline $z_2 = $' + str(Result.second_wheel_tooth_number) + \
                r' \newline  \newline $m_n = $' + str(Result.normal_module) + \
                r' \newline  \newline $\beta = $' + str(InputData.helix_angle)
        desc2 = r'Dolna granica błędu przełożenia przekładni: \newline ' \
                r'$u_{min} = 0,975 * u = $' + str(round(Result.ratio_bottom_border, 3)) + \
                r'  \newline \newline Górna granica błędu przełożenia przekładni: \newline ' \
                r'$u_{max} = 1,025 * u = $' + str(round(Result.ratio_upper_border, 3)) + \
                r'  \newline \newline Sprawdzenie czy przełożenie rzeczywiste mieści się w dopuszcalnym przedziale: \newline ' \
                r'$u_{rz} = \frac{z_2}{z_1} = $' + str(round(Result.real_ratio, 3)) + \
                r'  \newline \newline Zerowa odległość osi: \newline ' \
                r'$a_o = \frac{(z_1 + z_2) * m_n}{2 * cos(\beta)} = $' + str(round(Result.wheelbase_zero, 3))
        desc3 = r'$ \newline u_{min} = $' + str(round(Result.ratio_bottom_border, 3)) + \
                r'$ \newline  \newline u_{max} = $' + str(round(Result.ratio_upper_border, 3)) + \
                r'$ \newline  \newline  \newline u_{rz} = $' + str(round(Result.real_ratio, 3)) + \
                r'$ \newline  \newline a_o = $' + str(round(Result.wheelbase_zero, 3))

        return desc1, desc2, desc3

def create_description_r4_col1to3():
        desc1 = r'$ \newline \newline \newline  a_w = $' + str(InputData.wheelbase) + \
                r' \newline  \newline $a_o = $' + str(round(Result.wheelbase_zero, 3)) + \
                r' \newline  \newline $m_n = $' + str(Result.normal_module) + \
                r' \newline  \newline $\beta = $' + str(InputData.helix_angle) + \
                r' \newline  \newline $\alpha_n = $' + str(InputData.pressure_angle)
        desc2 = r' [mm]  \newline \newline Przybliżona wartość sumy współczynników korekcji: \newline' \
                r'$X_z = \frac{a_w - a_o}{m_n} = $' + str(round(Result.estimated_correction_factors_sum, 3)) + \
                r'  \newline \newline Kąt zarysu w przekroju czołowym $\alpha_t$: ' \
                r'$ \newline \alpha_t = \arctan{\frac{\tan{\alpha_n}}{\cos{\beta}}} = $' + str(
                round(Result.alfa_t, 3)) + \
                r'  \newline \newline Kąt przyporu toczny w przekroju czołowym: \newline' \
                r'$\alpha_{tw} = \arccos{\frac{a_o}{a_w}*\cos{\alpha_t}} = $' + str(round(Result.alfa_tw, 3)) + \
                r'  \newline \newline Kąt pochylenia linii zęba na walcu zasadniczym: \newline' \
                r'$\beta_b = \arctan{\tan{\beta} * \cos{\frac{\tan{\alpha_n}}{\cos{\beta}}}} = $' + str(round(Result.beta_b_helix_angle, 4))
        desc3 = r'$ \newline X_z = $' + str(round(Result.estimated_correction_factors_sum, 3)) + \
                r'$ \newline  \newline \alpha_t = $' + str(round(Result.alfa_t, 3)) + \
                r'$ \newline  \newline  \newline \alpha_{tw} = $' + str(round(Result.alfa_tw, 3)) + \
                r'$ \newline  \newline \beta_b = $' + str(round(Result.beta_b_helix_angle, 4))
        return desc1, desc2, desc3

def create_description_row5_col1to3():
        desc1 = r' \newline  \newline $\alpha_t = $' + str(round(Result.alfa_t, 5)) + \
                r' \newline  \newline $\alpha_{tw} = $' + str(round(Result.alfa_tw, 5))
        desc2 = r'  \newline \newline Involuta, funkcja ewolwentowa $\alpha_{tw}$: \newline ' \
                r'$inv\alpha_{tw} = \tan{\alpha_{tw}} - \alpha{tw} = $' + str(round(Result.inv_alfa_tw, 7)) + \
                r'  \newline \newline Involuta, funkcja ewolwentowa $\alpha_{t}$: \newline ' \
                r'$inv\alpha_t = \tan{\alpha_t} - \alpha_t = $' + str(round(Result.inv_alfa_t, 7))

        desc3 = r' \newline \newline  $inv\alpha_t = $' + str(round(Result.inv_alfa_t, 7)) + \
                r' \newline  \newline $inv\alpha_{tw} = $' + str(round(Result.inv_alfa_tw, 7))
        return desc1, desc2, desc3

def create_description_r6_col1to3():
        desc1 = r' \newline \newline  $inv\alpha_t = $' + str(round(Result.inv_alfa_t, 7)) + \
                r' \newline  \newline $inv\alpha_{tw} = $' + str(round(Result.inv_alfa_tw, 7))
        desc2 = r'  \newline \newline Suma współczynników korekcji: \newline $X = (inv\alpha_{tw} - inv\alpha_t) * \frac{z_1 + z_2}{2 * \tan{\alpha_n}} = $' + \
                str(round(Result.correction_factors_sum, 4))
        desc3 = r'$X = $' + str(round(Result.correction_factors_sum, 4))
        return desc1, desc2, desc3

def create_description_r7_col1to3():
        desc1 = r'$ \newline  \newline \beta_b = $' + str(round(Result.beta_b_helix_angle, 4)) + \
                r'$ \newline \newline \newline  z_ 1 = $' + str(InputData.pinion_tooth_number) + \
                r' \newline  \newline $z_2 = $' + str(Result.second_wheel_tooth_number)
        desc2 = r'Zastępcza liczba zębów zębnika: \newline' \
                r'$z_{z1} = \frac{z_1}{\cos{\beta} * \cos{\beta_b}^2} = $' + str(round(Result.pinion_tooth_number_placeholder, 3)) + \
                r'  \newline \newline Zastępcza liczba zębów koła: \newline' \
                r'$z_{z2} = \frac{z_2}{\cos{\beta} * \cos{\beta_b}^2} = $' + str(round(Result.second_wheel_tooth_number_placeholder, 3))
        desc3 = r'$ \newline z_{z1} = $' + str(round(Result.pinion_tooth_number_placeholder, 3)) + \
                r' \newline $z_{z1} = $' + str(round(Result.second_wheel_tooth_number_placeholder, 3))
        return desc1, desc2, desc3

def create_description_r8_col1to3():
        desc1 = ''
        desc2 = r' \newline  \newline Współczynnik korekcji zębnika (odczytany z wykresu): \newline' \
                r'$x_1 = $' + str(round(Result.pinion_correction_factor, 3)) + \
                r'  \newline \newline Współczynnik korekcji koła: \newline ' \
                r'$x_2 = X - x_1 = $' + str(round(Result.second_wheel_correction_factor, 3)) + \
                r'  \newline \newline Średnica toczna zębnika: \newline ' \
                r'$d_{w1} = \frac{2*a_w}{1 + u_{rz}} = $' + str(round(Result.pinion_rolling_diameter, 3)) + \
                r'  \newline \newline Średnica toczna koła: \newline ' \
                r'$d_{w2} = d_{w1} * u_{rz} = $' + str(round(Result.second_wheel_rolling_diameter, 3)) + \
                r'  \newline \newline Pozorna odległość osi: \newline ' \
                r'$a_p = a_o + m_n * (x_1 + x_2) = $' + str(round(Result.wheelbase_apparent, 3)) + \
                r'  \newline \newline Współczynnik zsunięcia: \newline' \
                r'$k = \frac{a_p - a_w}{m_n} = $' + str(round(Result.slip_factor, 3)) + \
                r'  \newline \newline Średnica podziałowa zębnika: \newline' \
                r'$d_{11} = \frac{m_n * z_1}{\cos{\beta}} = $' + str(round(Result.pinion_pitch_diameter, 3)) + \
                r'  \newline \newline Średnica podziałowa koła: \newline' \
                r'$d_{12} = 2 * a_o - d_{11} = $' + str(round(Result.second_wheel_pitch_diameter, 3)) + \
                r'  \newline \newline Moduł czołowy: \newline ' \
                r'$m_t = \frac{d_{11}}{z_1} = $' + str(round(Result.frontal_module, 3))
        desc3 = ''
        return desc1, desc2, desc3
