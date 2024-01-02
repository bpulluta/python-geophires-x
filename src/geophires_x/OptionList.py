# copyright, 2023, Malcolm I Ross
from enum import Enum


class EndUseOptions(str, Enum):
    ELECTRICITY = "Electricity"  # 1
    HEAT = "Direct-Use Heat"  # 2
    COGENERATION_TOPPING_EXTRA_HEAT = "Cogeneration Topping Cycle, Heat sales considered as extra income"  # 31
    COGENERATION_TOPPING_EXTRA_ELECTRICTY = "Cogeneration Topping Cycle, Electricity sales considered as extra income"  # 32
    COGENERATION_BOTTOMING_EXTRA_HEAT = "Cogeneration Bottoming Cycle, Heat sales considered as extra income"  # 41
    COGENERATION_BOTTOMING_EXTRA_ELECTRICTY = "Cogeneration Bottoming Cycle, Electricity sales considered as extra income"  # 42
    COGENERATION_PARALLEL_EXTRA_HEAT = "Cogeneration Parallel Cycle, Heat sales considered as extra income"  # 51
    COGENERATION_PARALLEL_EXTRA_ELECTRICTY = "Cogeneration Parallel Cycle, Electricity sales considered as extra income"  # 52
    ABSORPTION_CHILLER = "Absorption Chiller"  # 6
    HEAT_PUMP = "Heat Pump"  # 7
    DISTRICT_HEATING = "District Heating"  # 8
    RTES = "Reservoir Thermal Energy Storage"  # 9


class EconomicModel(str, Enum):
    CLGS = "Simple (CLGS)"
    FCR = "Fixed Charge Rate (FCR)"
    STANDARDIZED_LEVELIZED_COST = "Standard Levelized Cost"
    BICYCLE = "BICYCLE"


class PowerPlantType(str, Enum):
    SUB_CRITICAL_ORC = "Subcritical ORC"
    SUPER_CRITICAL_ORC = "Supercritical ORC"
    SINGLE_FLASH = "Single-Flash"
    DOUBLE_FLASH = "Double-Flash"


class ReservoirModel(str, Enum):
    CYLINDRICAL = "Simple cylindrical"
    MULTIPLE_PARALLEL_FRACTURES = "Multiple Parallel Fractures"
    LINEAR_HEAT_SWEEP = "1-D Linear Heat Sweep"
    SINGLE_FRACTURE = "Single Fracture m/A Thermal Drawdown"
    ANNUAL_PERCENTAGE = "Annual Percentage Thermal Drawdown"
    USER_PROVIDED_PROFILE = "User-Provided Temperature Profile"
    TOUGH2_SIMULATOR = "TOUGH2 Simulator"
    SUTRA = "SUTRA"


class ReservoirVolume(str, Enum):
    FRAC_NUM_SEP = "Specify number of fractures and fracture separation"
    RES_VOL_FRAC_SEP = "Specify reservoir volume and fracture separation"
    RES_VOL_FRAC_NUM = "Specify reservoir volume and number of fractures"
    RES_VOL_ONLY = "Specify reservoir volume only"


# class WellDrillingCostCorrelation(str, Enum):
#     VERTICAL_SMALL = "vertical open-hole, small diameter"
#     DEVIATED_SMALL = "deviated liner, small diameter"
#     VERTICAL_LARGE = "vertical open-hole, large diameter"
#     DEVIATED_LARGE = "deviated liner, large diameter"
#     SIMPLE = "Simple"

class WellDrillingCostCorrelation(str, Enum):
    VERTICAL_SMALL_BASE = "vertical small diameter, baseline"
    VERTICAL_SMALL_INT1 = "vertical small diameter, intermediate1"
    VERTICAL_SMALL_INT2 = "vertical small diameter, intermediate2"
    VERTICAL_SMALL_IDEAL = "vertical small diameter, ideal"
    DEVIATED_SMALL_BASE = "deviated small diameter, baseline"
    DEVIATED_SMALL_INT1 = "deviated small diameter, intermediate1"
    DEVIATED_SMALL_INT2 = "deviated small diameter, intermediate2"
    DEVIATED_SMALL_IDEAL = "deviated small diameter, ideal"
    VERTICAL_LARGE_BASE = "vertical large diameter, baseline"
    VERTICAL_LARGE_INT1 = "vertical large diameter, intermediate1"
    VERTICAL_LARGE_INT2 = "vertical large diameter, intermediate2"
    VERTICAL_LARGE_IDEAL = "vertical large diameter, ideal"
    DEVIATED_LARGE_BASE = "deviated large diameter, baseline"
    DEVIATED_LARGE_INT1 = "deviated large diameter, intermediate1"
    DEVIATED_LARGE_INT2 = "deviated large diameter, intermediate2"
    DEVIATED_LARGE_IDEAL = "deviated large diameter, ideal"
    SIMPLE = "Simple"


class FractureShape(str, Enum):
    CIRCULAR_AREA = "Circular fracture with known area"
    CIRCULAR_DIAMETER = "Circular fracture with known diameter"
    SQUARE = "Square"
    RECTANGULAR = "Rectangular"


class WorkingFluid(str, Enum):
    WATER = "water"
    SCO2 = "sCO2"


class Configuration(str, Enum):
    ULOOP = "utube"
    COAXIAL = "coaxial"
