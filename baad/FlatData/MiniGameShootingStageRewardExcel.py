# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameShootingStageRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameShootingStageRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameShootingStageRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameShootingStageRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameShootingStageRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingStageRewardExcel
    def ClearSection(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameShootingStageRewardExcel
    def RewardParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def Start(builder): builder.StartObject(6)
def MiniGameShootingStageRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def MiniGameShootingStageRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddRewardId(builder, RewardId): builder.PrependInt64Slot(1, RewardId, 0)
def MiniGameShootingStageRewardExcelAddRewardId(builder, RewardId):
    """This method is deprecated. Please switch to AddRewardId."""
    return AddRewardId(builder, RewardId)
def AddClearSection(builder, ClearSection): builder.PrependInt64Slot(2, ClearSection, 0)
def MiniGameShootingStageRewardExcelAddClearSection(builder, ClearSection):
    """This method is deprecated. Please switch to AddClearSection."""
    return AddClearSection(builder, ClearSection)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def MiniGameShootingStageRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameShootingStageRewardExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def MiniGameShootingStageRewardExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def StartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MiniGameShootingStageRewardExcelStartRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelIdVector(builder, numElems)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelAmount), 0)
def MiniGameShootingStageRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def StartRewardParcelAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameShootingStageRewardExcelStartRewardParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def MiniGameShootingStageRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)