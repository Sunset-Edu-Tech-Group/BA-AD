# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMinigameTBGExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMinigameTBGExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConstMinigameTBGExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConstMinigameTBGExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstMinigameTBGExcel
    def ConquestMapBoundaryOffsetLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ConquestMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ConquestMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ConquestMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ConquestMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ConquestMapCenterOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def CameraAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def ThemaLoadingProgressTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def MapAllyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def AniAllyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def EffectAllyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def EffectAllyBattleDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def AniEnemyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def EffectEnemyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def EffectEnemyBattleDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMinigameTBGExcel
    def EncounterAllyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def EncounterEnemyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMinigameTBGExcel
    def EncounterRewardReceiveIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(21)
def ConstMinigameTBGExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft): builder.PrependFloat32Slot(0, ConquestMapBoundaryOffsetLeft, 0.0)
def ConstMinigameTBGExcelAddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft):
    """This method is deprecated. Please switch to AddConquestMapBoundaryOffsetLeft."""
    return AddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft)
def AddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight): builder.PrependFloat32Slot(1, ConquestMapBoundaryOffsetRight, 0.0)
def ConstMinigameTBGExcelAddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight):
    """This method is deprecated. Please switch to AddConquestMapBoundaryOffsetRight."""
    return AddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight)
def AddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop): builder.PrependFloat32Slot(2, ConquestMapBoundaryOffsetTop, 0.0)
def ConstMinigameTBGExcelAddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop):
    """This method is deprecated. Please switch to AddConquestMapBoundaryOffsetTop."""
    return AddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop)
def AddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom): builder.PrependFloat32Slot(3, ConquestMapBoundaryOffsetBottom, 0.0)
def ConstMinigameTBGExcelAddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom):
    """This method is deprecated. Please switch to AddConquestMapBoundaryOffsetBottom."""
    return AddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom)
def AddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX): builder.PrependFloat32Slot(4, ConquestMapCenterOffsetX, 0.0)
def ConstMinigameTBGExcelAddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX):
    """This method is deprecated. Please switch to AddConquestMapCenterOffsetX."""
    return AddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX)
def AddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY): builder.PrependFloat32Slot(5, ConquestMapCenterOffsetY, 0.0)
def ConstMinigameTBGExcelAddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY):
    """This method is deprecated. Please switch to AddConquestMapCenterOffsetY."""
    return AddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY)
def AddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(6, CameraAngle, 0.0)
def ConstMinigameTBGExcelAddCameraAngle(builder, CameraAngle):
    """This method is deprecated. Please switch to AddCameraAngle."""
    return AddCameraAngle(builder, CameraAngle)
def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(7, CameraZoomMax, 0.0)
def ConstMinigameTBGExcelAddCameraZoomMax(builder, CameraZoomMax):
    """This method is deprecated. Please switch to AddCameraZoomMax."""
    return AddCameraZoomMax(builder, CameraZoomMax)
def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(8, CameraZoomMin, 0.0)
def ConstMinigameTBGExcelAddCameraZoomMin(builder, CameraZoomMin):
    """This method is deprecated. Please switch to AddCameraZoomMin."""
    return AddCameraZoomMin(builder, CameraZoomMin)
def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(9, CameraZoomDefault, 0.0)
def ConstMinigameTBGExcelAddCameraZoomDefault(builder, CameraZoomDefault):
    """This method is deprecated. Please switch to AddCameraZoomDefault."""
    return AddCameraZoomDefault(builder, CameraZoomDefault)
def AddThemaLoadingProgressTime(builder, ThemaLoadingProgressTime): builder.PrependFloat32Slot(10, ThemaLoadingProgressTime, 0.0)
def ConstMinigameTBGExcelAddThemaLoadingProgressTime(builder, ThemaLoadingProgressTime):
    """This method is deprecated. Please switch to AddThemaLoadingProgressTime."""
    return AddThemaLoadingProgressTime(builder, ThemaLoadingProgressTime)
def AddMapAllyRotation(builder, MapAllyRotation): builder.PrependFloat32Slot(11, MapAllyRotation, 0.0)
def ConstMinigameTBGExcelAddMapAllyRotation(builder, MapAllyRotation):
    """This method is deprecated. Please switch to AddMapAllyRotation."""
    return AddMapAllyRotation(builder, MapAllyRotation)
def AddAniAllyBattleAttack(builder, AniAllyBattleAttack): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(AniAllyBattleAttack), 0)
def ConstMinigameTBGExcelAddAniAllyBattleAttack(builder, AniAllyBattleAttack):
    """This method is deprecated. Please switch to AddAniAllyBattleAttack."""
    return AddAniAllyBattleAttack(builder, AniAllyBattleAttack)
def AddEffectAllyBattleAttack(builder, EffectAllyBattleAttack): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(EffectAllyBattleAttack), 0)
def ConstMinigameTBGExcelAddEffectAllyBattleAttack(builder, EffectAllyBattleAttack):
    """This method is deprecated. Please switch to AddEffectAllyBattleAttack."""
    return AddEffectAllyBattleAttack(builder, EffectAllyBattleAttack)
def AddEffectAllyBattleDamage(builder, EffectAllyBattleDamage): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EffectAllyBattleDamage), 0)
def ConstMinigameTBGExcelAddEffectAllyBattleDamage(builder, EffectAllyBattleDamage):
    """This method is deprecated. Please switch to AddEffectAllyBattleDamage."""
    return AddEffectAllyBattleDamage(builder, EffectAllyBattleDamage)
def AddAniEnemyBattleAttack(builder, AniEnemyBattleAttack): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(AniEnemyBattleAttack), 0)
def ConstMinigameTBGExcelAddAniEnemyBattleAttack(builder, AniEnemyBattleAttack):
    """This method is deprecated. Please switch to AddAniEnemyBattleAttack."""
    return AddAniEnemyBattleAttack(builder, AniEnemyBattleAttack)
def AddEffectEnemyBattleAttack(builder, EffectEnemyBattleAttack): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EffectEnemyBattleAttack), 0)
def ConstMinigameTBGExcelAddEffectEnemyBattleAttack(builder, EffectEnemyBattleAttack):
    """This method is deprecated. Please switch to AddEffectEnemyBattleAttack."""
    return AddEffectEnemyBattleAttack(builder, EffectEnemyBattleAttack)
def AddEffectEnemyBattleDamage(builder, EffectEnemyBattleDamage): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(EffectEnemyBattleDamage), 0)
def ConstMinigameTBGExcelAddEffectEnemyBattleDamage(builder, EffectEnemyBattleDamage):
    """This method is deprecated. Please switch to AddEffectEnemyBattleDamage."""
    return AddEffectEnemyBattleDamage(builder, EffectEnemyBattleDamage)
def AddEncounterAllyRotation(builder, EncounterAllyRotation): builder.PrependFloat32Slot(18, EncounterAllyRotation, 0.0)
def ConstMinigameTBGExcelAddEncounterAllyRotation(builder, EncounterAllyRotation):
    """This method is deprecated. Please switch to AddEncounterAllyRotation."""
    return AddEncounterAllyRotation(builder, EncounterAllyRotation)
def AddEncounterEnemyRotation(builder, EncounterEnemyRotation): builder.PrependFloat32Slot(19, EncounterEnemyRotation, 0.0)
def ConstMinigameTBGExcelAddEncounterEnemyRotation(builder, EncounterEnemyRotation):
    """This method is deprecated. Please switch to AddEncounterEnemyRotation."""
    return AddEncounterEnemyRotation(builder, EncounterEnemyRotation)
def AddEncounterRewardReceiveIndex(builder, EncounterRewardReceiveIndex): builder.PrependInt32Slot(20, EncounterRewardReceiveIndex, 0)
def ConstMinigameTBGExcelAddEncounterRewardReceiveIndex(builder, EncounterRewardReceiveIndex):
    """This method is deprecated. Please switch to AddEncounterRewardReceiveIndex."""
    return AddEncounterRewardReceiveIndex(builder, EncounterRewardReceiveIndex)
def End(builder): return builder.EndObject()
def ConstMinigameTBGExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)