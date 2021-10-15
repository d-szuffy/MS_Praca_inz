from enum import Enum


class HeatTreatmentType(Enum):
    NA = "Nie dotyczy"
    IMPROVEMENT = "Ulepszanie"
    NORMALISED = "Normalizowane"
    HARDENING = "Hartowanie"
    NITRIDING_BATH = "Azotowanie kąpielowe"
    NITRIDING_GAS = "Azotowanie gazowe"
    HARDENING_DIFFUSION = "Utwardzanie dyfuzyjne"


class WheelMaterial(Enum):
    ST4 = "St4"
    ST5 = "St5"
    ST6 = "St6"
    ST7 = "St7"
    _20 = "20"
    _45 = "45"
    _55 = "55"
    _30H = "30H"
    _40H = "40H"
    _40HM = "40HM"
    _34HNM = "34HNM"
    _15 = "15"
    _16HG = "16HG"
    _18HGT = "18HGT"
    _19HM = "19HM"
    _15HN = "15HN"
    _18H2N2 = "18H2N2"
    _17HNM = "17HNM"


class Material(object):
    def __init__(self, material_name, heat_treatment: HeatTreatmentType, core_hardness, tooth_sides_hardness,
                 tooth_sides_exhaustion_threshold, tooth_feet_exhaustion_threshold_load_throbbing,
                 tooth_feet_static_durability):
        self.material_name = material_name
        self.heat_treatment = heat_treatment
        self.core_hardness = core_hardness
        self.tooth_sides_hardness = tooth_sides_hardness
        self.tooth_sides_exhaustion_threshold = tooth_sides_exhaustion_threshold
        self.tooth_feet_exhaustion_threshold_load_throbbing = tooth_feet_exhaustion_threshold_load_throbbing
        self.tooth_feet_static_durability = tooth_feet_static_durability
        pass


class SoftMaterial(Material):
    def __init__(self, material_name, heat_treatment: HeatTreatmentType, core_hardness, tooth_sides_hardness,
                 tooth_sides_exhaustion_threshold, tooth_feet_exhaustion_threshold_load_throbbing,
                 tooth_feet_static_durability):
        super(SoftMaterial, self).__init__(material_name, heat_treatment, core_hardness, tooth_sides_hardness,
                                           tooth_sides_exhaustion_threshold,
                                           tooth_feet_exhaustion_threshold_load_throbbing,
                                           tooth_feet_static_durability)


class HardMaterial(Material):
    def __init__(self, material_name, heat_treatment: HeatTreatmentType, core_hardness, tooth_sides_hardness,
                 tooth_sides_exhaustion_threshold, tooth_feet_exhaustion_threshold_load_throbbing,
                 tooth_feet_static_durability):
        super(HardMaterial, self).__init__(material_name, heat_treatment, core_hardness, tooth_sides_hardness,
                                           tooth_sides_exhaustion_threshold,
                                           tooth_feet_exhaustion_threshold_load_throbbing,
                                           tooth_feet_static_durability)
