# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameTBGThemaRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameTBGThemaRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameTBGThemaRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameTBGThemaRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameTBGThemaRewardExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameTBGThemaRewardExcel
    def ThemaRound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameTBGThemaRewardExcel
    def ThemaUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameTBGThemaRewardExcel
    def IsLoop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameTBGThemaRewardExcel
    def MiniGameTBGThemaRewardType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameTBGThemaRewardExcel
    def RewardParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

def Start(builder): builder.StartObject(8)
def MiniGameTBGThemaRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def MiniGameTBGThemaRewardExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddThemaRound(builder, ThemaRound): builder.PrependInt32Slot(1, ThemaRound, 0)
def MiniGameTBGThemaRewardExcelAddThemaRound(builder, ThemaRound):
    """This method is deprecated. Please switch to AddThemaRound."""
    return AddThemaRound(builder, ThemaRound)
def AddThemaUniqueId(builder, ThemaUniqueId): builder.PrependInt32Slot(2, ThemaUniqueId, 0)
def MiniGameTBGThemaRewardExcelAddThemaUniqueId(builder, ThemaUniqueId):
    """This method is deprecated. Please switch to AddThemaUniqueId."""
    return AddThemaUniqueId(builder, ThemaUniqueId)
def AddIsLoop(builder, IsLoop): builder.PrependBoolSlot(3, IsLoop, 0)
def MiniGameTBGThemaRewardExcelAddIsLoop(builder, IsLoop):
    """This method is deprecated. Please switch to AddIsLoop."""
    return AddIsLoop(builder, IsLoop)
def AddMiniGameTBGThemaRewardType_(builder, MiniGameTBGThemaRewardType_): builder.PrependInt32Slot(4, MiniGameTBGThemaRewardType_, 0)
def MiniGameTBGThemaRewardExcelAddMiniGameTBGThemaRewardType_(builder, MiniGameTBGThemaRewardType_):
    """This method is deprecated. Please switch to AddMiniGameTBGThemaRewardType_."""
    return AddMiniGameTBGThemaRewardType_(builder, MiniGameTBGThemaRewardType_)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def MiniGameTBGThemaRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameTBGThemaRewardExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def MiniGameTBGThemaRewardExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def StartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MiniGameTBGThemaRewardExcelStartRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelIdVector(builder, numElems)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelAmount), 0)
def MiniGameTBGThemaRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def StartRewardParcelAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameTBGThemaRewardExcelStartRewardParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def MiniGameTBGThemaRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)