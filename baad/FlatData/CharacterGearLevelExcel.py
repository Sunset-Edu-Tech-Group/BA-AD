# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterGearLevelExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterGearLevelExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterGearLevelExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterGearLevelExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterGearLevelExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterGearLevelExcel
    def TierLevelExp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # CharacterGearLevelExcel
    def TierLevelExpAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # CharacterGearLevelExcel
    def TierLevelExpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterGearLevelExcel
    def TierLevelExpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # CharacterGearLevelExcel
    def TotalExp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # CharacterGearLevelExcel
    def TotalExpAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # CharacterGearLevelExcel
    def TotalExpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterGearLevelExcel
    def TotalExpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def CharacterGearLevelExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLevel(builder, Level): builder.PrependInt32Slot(0, Level, 0)
def CharacterGearLevelExcelAddLevel(builder, Level):
    """This method is deprecated. Please switch to AddLevel."""
    return AddLevel(builder, Level)
def AddTierLevelExp(builder, TierLevelExp): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TierLevelExp), 0)
def CharacterGearLevelExcelAddTierLevelExp(builder, TierLevelExp):
    """This method is deprecated. Please switch to AddTierLevelExp."""
    return AddTierLevelExp(builder, TierLevelExp)
def StartTierLevelExpVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def CharacterGearLevelExcelStartTierLevelExpVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTierLevelExpVector(builder, numElems)
def AddTotalExp(builder, TotalExp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(TotalExp), 0)
def CharacterGearLevelExcelAddTotalExp(builder, TotalExp):
    """This method is deprecated. Please switch to AddTotalExp."""
    return AddTotalExp(builder, TotalExp)
def StartTotalExpVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def CharacterGearLevelExcelStartTotalExpVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTotalExpVector(builder, numElems)
def End(builder): return builder.EndObject()
def CharacterGearLevelExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)