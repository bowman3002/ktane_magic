from enum import Enum

class PortEnum(Enum):
    DVI_D =     "DVI_D    | 24 Squares on left side"
    PARALLEL =  "Parallel | Long, two rows of circles"
    PS_2 =      "PS/2     | Circular"
    RJ_45 =     "RJ-45    | Ethernet"
    SERIAL =    "Serial   | Short, two rows of squares"
    RCA =       "RCA      | Two circles"