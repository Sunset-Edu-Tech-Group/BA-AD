# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageLimitedRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageLimitedRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEliminateRaidStageLimitedRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EliminateRaidStageLimitedRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelUniqueId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelUniqueIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardParcelUniqueIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EliminateRaidStageLimitedRewardExcel
    def LimitedRewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def EliminateRaidStageLimitedRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLimitedRewardId(builder, LimitedRewardId): builder.PrependInt64Slot(0, LimitedRewardId, 0)
def EliminateRaidStageLimitedRewardExcelAddLimitedRewardId(builder, LimitedRewardId):
    """This method is deprecated. Please switch to AddLimitedRewardId."""
    return AddLimitedRewardId(builder, LimitedRewardId)
def AddLimitedRewardParcelType(builder, LimitedRewardParcelType): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(LimitedRewardParcelType), 0)
def EliminateRaidStageLimitedRewardExcelAddLimitedRewardParcelType(builder, LimitedRewardParcelType):
    """This method is deprecated. Please switch to AddLimitedRewardParcelType."""
    return AddLimitedRewardParcelType(builder, LimitedRewardParcelType)
def StartLimitedRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EliminateRaidStageLimitedRewardExcelStartLimitedRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartLimitedRewardParcelTypeVector(builder, numElems)
def AddLimitedRewardParcelUniqueId(builder, LimitedRewardParcelUniqueId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(LimitedRewardParcelUniqueId), 0)
def EliminateRaidStageLimitedRewardExcelAddLimitedRewardParcelUniqueId(builder, LimitedRewardParcelUniqueId):
    """This method is deprecated. Please switch to AddLimitedRewardParcelUniqueId."""
    return AddLimitedRewardParcelUniqueId(builder, LimitedRewardParcelUniqueId)
def StartLimitedRewardParcelUniqueIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EliminateRaidStageLimitedRewardExcelStartLimitedRewardParcelUniqueIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartLimitedRewardParcelUniqueIdVector(builder, numElems)
def AddLimitedRewardAmount(builder, LimitedRewardAmount): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(LimitedRewardAmount), 0)
def EliminateRaidStageLimitedRewardExcelAddLimitedRewardAmount(builder, LimitedRewardAmount):
    """This method is deprecated. Please switch to AddLimitedRewardAmount."""
    return AddLimitedRewardAmount(builder, LimitedRewardAmount)
def StartLimitedRewardAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EliminateRaidStageLimitedRewardExcelStartLimitedRewardAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartLimitedRewardAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def EliminateRaidStageLimitedRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)