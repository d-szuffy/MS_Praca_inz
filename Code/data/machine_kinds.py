from enum import Enum


class DrivingMachine(Enum):
    ELECTRIC = "Silnik elektryczny"
    STEAM = "Tubrina parowa"
    GAS = "Turbina gazowa"
    MORE_THAN_TWO_CYLINDERS = "Silnik tłokowy o liczbie cylindrów większej niż dwa"
    WATER = "Turbina wodna"
    HYDRAULIC = "Silnik hydrauliczny"
    ONE_OR_TWO_CYLINDERS = "Silnik tłokowy jedno- lub dwucylindrowy"


class DrivenMachine(Enum):
    HOIST_OR_ELEVATOR_UNEVENLY_LOADED = "Podnośnik, winda (nierównomiernie obciążony)"
    CONCRETE_MILL = 'Młyn do cementu'
    HOIST_OR_ELEVATOR_EVENLY_LOADED = 'Podnośnik, winda (równomiernie obciążony)'
    WIRE_DRAWING_MACHINE = 'Przeciągarka do drutu'
    CHAIN_TYPE_CHAIN_EXCAVATOR = 'Koparka wieloczerpakowa łańcuchowa'
    GENERATOR_EXCEPT_WELDING_GENERATOR = 'Prądnica (oprócz prądnicy spawalniczej)'
    BUCKET_WHEEL_EXCAVATOR = 'Koparka z kołem czerpakowym'
    WELDING_GENERATOR = 'Prądnica spawalnicza'
    EXCAVATOR_WITH_A_CUTTER_HEAD = 'Koparka z głowicą tnącą'
    ROLLERS_FOR_RUBBER = 'Walce do gumy'
    CRUSHER = 'Kruszarka'
    FORGE = 'Kuźniarka'
    ROTARY_KILN = 'Piec obrotowy'
    CABLEWAY = 'Kolej linowa'
    CONVEYOR_BELT_EVENLY_LOADED = 'Przenośnik taśmowy (równomiernie obciążony)'
    WOODWORKING_MACHINE = 'Obrabiarka do drewna'
    CONVEYOR_BELT_UNEVENLY_LOADED = 'Przenośnik taśmowy (nierównomiernie obciążony)'
    SINGLE_CYLINDER_PISTON_COMPRESSOR = 'Sprężarka tłokowa jednocylindrowa'
    LIFTING_WINCH = 'Kołowrót wyciągowy'
    MULTI_CYLINDER_RECIPROCATING_COMPRESSOR = 'Sprężarka tłokowa wielocylindrowa'
    CRANE = 'Żuraw'
    AXIAL_COMPRESSOR = 'Sprężarka osiowa'
    CONCRETE_MIXER = 'Mieszarka do betonu'
    CONVERTER = 'Konwertor'
    PAPER_MACHINE_EVENLY_LOADED = 'Maszyna papiernicza (obciążona równomiernie)'
    PISTON_PUMP_WITH_THREE_OR_MORE_CYLINDERS = 'Pompa tłokowa trzy- i więcej cylindrowa'
    PAPER_MACHINE_UNEVENLY_LOADED = 'Maszyna papiernicza (obciążona nierównomiernie)'
    CENTRIFUGAL_PUMP = 'Pompa odśrodkowa'
    BRIQUETTE_PRESS = 'Prasa do brykietów'
    DISPLACEMENT_PUMP = 'Pompa wyporowa'
    CRANK_PRESS_ECCENTRIC_FORGING_PRESS = 'Prasa korbowa, mimośrodowa, kuźnicza'
    STEERING_MACHINE = 'Maszyna sterowa'
    BRICK_PRESS = 'Prasa do cegieł'
    MIXER_FOR_LIGHT_LIQUIDS = 'Mieszalnik do lekkich cieczy'
    SHIP_PROPELLER = 'Śruba okrętowa'
    MIXER_FOR_VISCOUS_LIQUIDS_AND_SOLIDS = 'Mieszalnik do cieczy lepkich i ciał stałych'
    DREDGE_PUMP = 'Pompa pogłębiarki'
    WEAVING_MACHINES = 'Maszyny tkackie'
    ONE_OR_TWO_CYLINDER_PISTON_PUMP = 'Pompa tłokowa 1- lub 2-cylindrowa'
    LARGE_FAN_EG_MINE = 'Wentylator duży (np. kopalniany)'
    WASHER = 'Płuczarka'
    FAN_SMALL = 'Wentylator mały'
    ROTARY_MACHINE_TOOL = 'Obrabiarka o ruchu obrotowym'
    ROLLING_MILL_FOR_INGOTS = 'Walcarka do wlewków'
    MACHINE_TOOL_WITH_RECIPROCATING_MOTION = 'Obrabiarka o ruchu posuwisto-zwrotnym'
    ROLLING_MACHINE_FOR_STRIP_OR_WIRE = 'Walcarka do taśmy lub drutu'
    WINCH = 'Wciągarka'
    SCISSOR_CUTTING_MILL = 'Walcarka do cięcia nożycami'
