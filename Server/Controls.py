from enum import IntEnum

class NorthChip(IntEnum):
    Nothing = -1
    BoomUp = 0
    BoomDown = 1
    HookUp = 2
    HookDown = 3

class SouthChip(IntEnum):
    Nothing = -1
    PlatformEast = 0
    PlatformWest = 1
    PlatformNorth = 2
    PlatformSouth = 3

class ExtraChip(IntEnum):
    Nothing = -1
    CabCW = 0
    CabCCW = 1