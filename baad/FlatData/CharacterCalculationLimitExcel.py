# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterCalculationLimitExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterCalculationLimitExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterCalculationLimitExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterCalculationLimitExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterCalculationLimitExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterCalculationLimitExcel
    def TacticEntityType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterCalculationLimitExcel
    def CalculationValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterCalculationLimitExcel
    def MinValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterCalculationLimitExcel
    def MaxValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def CharacterCalculationLimitExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def CharacterCalculationLimitExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddTacticEntityType_(builder, TacticEntityType_): builder.PrependInt32Slot(1, TacticEntityType_, 0)
def CharacterCalculationLimitExcelAddTacticEntityType_(builder, TacticEntityType_):
    """This method is deprecated. Please switch to AddTacticEntityType_."""
    return AddTacticEntityType_(builder, TacticEntityType_)
def AddCalculationValue(builder, CalculationValue): builder.PrependInt32Slot(2, CalculationValue, 0)
def CharacterCalculationLimitExcelAddCalculationValue(builder, CalculationValue):
    """This method is deprecated. Please switch to AddCalculationValue."""
    return AddCalculationValue(builder, CalculationValue)
def AddMinValue(builder, MinValue): builder.PrependInt64Slot(3, MinValue, 0)
def CharacterCalculationLimitExcelAddMinValue(builder, MinValue):
    """This method is deprecated. Please switch to AddMinValue."""
    return AddMinValue(builder, MinValue)
def AddMaxValue(builder, MaxValue): builder.PrependInt64Slot(4, MaxValue, 0)
def CharacterCalculationLimitExcelAddMaxValue(builder, MaxValue):
    """This method is deprecated. Please switch to AddMaxValue."""
    return AddMaxValue(builder, MaxValue)
def End(builder): return builder.EndObject()
def CharacterCalculationLimitExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)