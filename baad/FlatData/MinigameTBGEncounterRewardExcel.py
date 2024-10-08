# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGEncounterRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGEncounterRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMinigameTBGEncounterRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MinigameTBGEncounterRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MinigameTBGEncounterRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def TBGOptionSuccessType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def Paremeter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def ParcelType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def ParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def Amount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterRewardExcel
    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(8)
def MinigameTBGEncounterRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def MinigameTBGEncounterRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)
def MinigameTBGEncounterRewardExcelAddUniqueId(builder, UniqueId):
    """This method is deprecated. Please switch to AddUniqueId."""
    return AddUniqueId(builder, UniqueId)
def AddTBGOptionSuccessType_(builder, TBGOptionSuccessType_): builder.PrependInt32Slot(2, TBGOptionSuccessType_, 0)
def MinigameTBGEncounterRewardExcelAddTBGOptionSuccessType_(builder, TBGOptionSuccessType_):
    """This method is deprecated. Please switch to AddTBGOptionSuccessType_."""
    return AddTBGOptionSuccessType_(builder, TBGOptionSuccessType_)
def AddParemeter(builder, Paremeter): builder.PrependInt64Slot(3, Paremeter, 0)
def MinigameTBGEncounterRewardExcelAddParemeter(builder, Paremeter):
    """This method is deprecated. Please switch to AddParemeter."""
    return AddParemeter(builder, Paremeter)
def AddParcelType_(builder, ParcelType_): builder.PrependInt32Slot(4, ParcelType_, 0)
def MinigameTBGEncounterRewardExcelAddParcelType_(builder, ParcelType_):
    """This method is deprecated. Please switch to AddParcelType_."""
    return AddParcelType_(builder, ParcelType_)
def AddParcelId(builder, ParcelId): builder.PrependInt64Slot(5, ParcelId, 0)
def MinigameTBGEncounterRewardExcelAddParcelId(builder, ParcelId):
    """This method is deprecated. Please switch to AddParcelId."""
    return AddParcelId(builder, ParcelId)
def AddAmount(builder, Amount): builder.PrependInt64Slot(6, Amount, 0)
def MinigameTBGEncounterRewardExcelAddAmount(builder, Amount):
    """This method is deprecated. Please switch to AddAmount."""
    return AddAmount(builder, Amount)
def AddProb(builder, Prob): builder.PrependInt32Slot(7, Prob, 0)
def MinigameTBGEncounterRewardExcelAddProb(builder, Prob):
    """This method is deprecated. Please switch to AddProb."""
    return AddProb(builder, Prob)
def End(builder): return builder.EndObject()
def MinigameTBGEncounterRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)