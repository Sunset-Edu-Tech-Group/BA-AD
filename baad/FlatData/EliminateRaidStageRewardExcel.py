# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEliminateRaidStageRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EliminateRaidStageRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EliminateRaidStageRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EliminateRaidStageRewardExcel
    def IsClearStageRewardHideInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EliminateRaidStageRewardExcel
    def ClearStageRewardProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EliminateRaidStageRewardExcel
    def ClearStageRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EliminateRaidStageRewardExcel
    def ClearStageRewardParcelUniqueID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EliminateRaidStageRewardExcel
    def ClearStageRewardParcelUniqueName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EliminateRaidStageRewardExcel
    def ClearStageRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(7)
def EliminateRaidStageRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def EliminateRaidStageRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddIsClearStageRewardHideInfo(builder, IsClearStageRewardHideInfo): builder.PrependBoolSlot(1, IsClearStageRewardHideInfo, 0)
def EliminateRaidStageRewardExcelAddIsClearStageRewardHideInfo(builder, IsClearStageRewardHideInfo):
    """This method is deprecated. Please switch to AddIsClearStageRewardHideInfo."""
    return AddIsClearStageRewardHideInfo(builder, IsClearStageRewardHideInfo)
def AddClearStageRewardProb(builder, ClearStageRewardProb): builder.PrependInt64Slot(2, ClearStageRewardProb, 0)
def EliminateRaidStageRewardExcelAddClearStageRewardProb(builder, ClearStageRewardProb):
    """This method is deprecated. Please switch to AddClearStageRewardProb."""
    return AddClearStageRewardProb(builder, ClearStageRewardProb)
def AddClearStageRewardParcelType(builder, ClearStageRewardParcelType): builder.PrependInt32Slot(3, ClearStageRewardParcelType, 0)
def EliminateRaidStageRewardExcelAddClearStageRewardParcelType(builder, ClearStageRewardParcelType):
    """This method is deprecated. Please switch to AddClearStageRewardParcelType."""
    return AddClearStageRewardParcelType(builder, ClearStageRewardParcelType)
def AddClearStageRewardParcelUniqueID(builder, ClearStageRewardParcelUniqueID): builder.PrependInt64Slot(4, ClearStageRewardParcelUniqueID, 0)
def EliminateRaidStageRewardExcelAddClearStageRewardParcelUniqueID(builder, ClearStageRewardParcelUniqueID):
    """This method is deprecated. Please switch to AddClearStageRewardParcelUniqueID."""
    return AddClearStageRewardParcelUniqueID(builder, ClearStageRewardParcelUniqueID)
def AddClearStageRewardParcelUniqueName(builder, ClearStageRewardParcelUniqueName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ClearStageRewardParcelUniqueName), 0)
def EliminateRaidStageRewardExcelAddClearStageRewardParcelUniqueName(builder, ClearStageRewardParcelUniqueName):
    """This method is deprecated. Please switch to AddClearStageRewardParcelUniqueName."""
    return AddClearStageRewardParcelUniqueName(builder, ClearStageRewardParcelUniqueName)
def AddClearStageRewardAmount(builder, ClearStageRewardAmount): builder.PrependInt64Slot(6, ClearStageRewardAmount, 0)
def EliminateRaidStageRewardExcelAddClearStageRewardAmount(builder, ClearStageRewardAmount):
    """This method is deprecated. Please switch to AddClearStageRewardAmount."""
    return AddClearStageRewardAmount(builder, ClearStageRewardAmount)
def End(builder): return builder.EndObject()
def EliminateRaidStageRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)