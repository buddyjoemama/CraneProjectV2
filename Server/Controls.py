from enum import IntEnum

class NorthChip(IntEnum):
    Nothing = -1
    PlatformNorth = 0
    PlatformEast = 1
    PlatformSouth = 2
    PlatformWest = 3
    BoomUp = 4
    BoomDown = 5

class SouthChip(IntEnum):
    Nothing = -1
    HookUp = 0
    HookDown = 1
    CamUp = 2
    CamDown = 3
    CamLeft = 4
    CamRight = 5

class ExtraChip(IntEnum):
    Nothing = -1
    CabCW = 0
    CabCCW = 1

class Relay(IntEnum):
    Nothing = -1
    Off = 0
    On = 1