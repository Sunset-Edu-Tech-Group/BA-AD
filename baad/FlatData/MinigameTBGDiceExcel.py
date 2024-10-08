# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGDiceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGDiceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMinigameTBGDiceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MinigameTBGDiceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MinigameTBGDiceExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGDiceExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGDiceExcel
    def DiceGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGDiceExcel
    def DiceResult(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGDiceExcel
    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyCondition(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyConditionAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyConditionIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # MinigameTBGDiceExcel
    def ProbModifyValue(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # MinigameTBGDiceExcel
    def ProbModifyLimit(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyLimitAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyLimitLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MinigameTBGDiceExcel
    def ProbModifyLimitIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

def Start(builder): builder.StartObject(8)
def MinigameTBGDiceExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def MinigameTBGDiceExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)
def MinigameTBGDiceExcelAddUniqueId(builder, UniqueId):
    """This method is deprecated. Please switch to AddUniqueId."""
    return AddUniqueId(builder, UniqueId)
def AddDiceGroup(builder, DiceGroup): builder.PrependInt32Slot(2, DiceGroup, 0)
def MinigameTBGDiceExcelAddDiceGroup(builder, DiceGroup):
    """This method is deprecated. Please switch to AddDiceGroup."""
    return AddDiceGroup(builder, DiceGroup)
def AddDiceResult(builder, DiceResult): builder.PrependInt32Slot(3, DiceResult, 0)
def MinigameTBGDiceExcelAddDiceResult(builder, DiceResult):
    """This method is deprecated. Please switch to AddDiceResult."""
    return AddDiceResult(builder, DiceResult)
def AddProb(builder, Prob): builder.PrependInt32Slot(4, Prob, 0)
def MinigameTBGDiceExcelAddProb(builder, Prob):
    """This method is deprecated. Please switch to AddProb."""
    return AddProb(builder, Prob)
def AddProbModifyCondition(builder, ProbModifyCondition): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ProbModifyCondition), 0)
def MinigameTBGDiceExcelAddProbModifyCondition(builder, ProbModifyCondition):
    """This method is deprecated. Please switch to AddProbModifyCondition."""
    return AddProbModifyCondition(builder, ProbModifyCondition)
def StartProbModifyConditionVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MinigameTBGDiceExcelStartProbModifyConditionVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartProbModifyConditionVector(builder, numElems)
def AddProbModifyValue(builder, ProbModifyValue): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ProbModifyValue), 0)
def MinigameTBGDiceExcelAddProbModifyValue(builder, ProbModifyValue):
    """This method is deprecated. Please switch to AddProbModifyValue."""
    return AddProbModifyValue(builder, ProbModifyValue)
def StartProbModifyValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MinigameTBGDiceExcelStartProbModifyValueVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartProbModifyValueVector(builder, numElems)
def AddProbModifyLimit(builder, ProbModifyLimit): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(ProbModifyLimit), 0)
def MinigameTBGDiceExcelAddProbModifyLimit(builder, ProbModifyLimit):
    """This method is deprecated. Please switch to AddProbModifyLimit."""
    return AddProbModifyLimit(builder, ProbModifyLimit)
def StartProbModifyLimitVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MinigameTBGDiceExcelStartProbModifyLimitVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartProbModifyLimitVector(builder, numElems)
def End(builder): return builder.EndObject()
def MinigameTBGDiceExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)