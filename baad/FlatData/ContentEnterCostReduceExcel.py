# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ContentEnterCostReduceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContentEnterCostReduceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsContentEnterCostReduceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ContentEnterCostReduceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ContentEnterCostReduceExcel
    def EnterCostReduceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ContentEnterCostReduceExcel
    def ContentType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ContentEnterCostReduceExcel
    def StageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ContentEnterCostReduceExcel
    def ReduceEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ContentEnterCostReduceExcel
    def ReduceEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ContentEnterCostReduceExcel
    def ReduceAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(6)
def ContentEnterCostReduceExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId): builder.PrependInt64Slot(0, EnterCostReduceGroupId, 0)
def ContentEnterCostReduceExcelAddEnterCostReduceGroupId(builder, EnterCostReduceGroupId):
    """This method is deprecated. Please switch to AddEnterCostReduceGroupId."""
    return AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId)
def AddContentType_(builder, ContentType_): builder.PrependInt32Slot(1, ContentType_, 0)
def ContentEnterCostReduceExcelAddContentType_(builder, ContentType_):
    """This method is deprecated. Please switch to AddContentType_."""
    return AddContentType_(builder, ContentType_)
def AddStageId(builder, StageId): builder.PrependInt64Slot(2, StageId, 0)
def ContentEnterCostReduceExcelAddStageId(builder, StageId):
    """This method is deprecated. Please switch to AddStageId."""
    return AddStageId(builder, StageId)
def AddReduceEnterCostType(builder, ReduceEnterCostType): builder.PrependInt32Slot(3, ReduceEnterCostType, 0)
def ContentEnterCostReduceExcelAddReduceEnterCostType(builder, ReduceEnterCostType):
    """This method is deprecated. Please switch to AddReduceEnterCostType."""
    return AddReduceEnterCostType(builder, ReduceEnterCostType)
def AddReduceEnterCostId(builder, ReduceEnterCostId): builder.PrependInt64Slot(4, ReduceEnterCostId, 0)
def ContentEnterCostReduceExcelAddReduceEnterCostId(builder, ReduceEnterCostId):
    """This method is deprecated. Please switch to AddReduceEnterCostId."""
    return AddReduceEnterCostId(builder, ReduceEnterCostId)
def AddReduceAmount(builder, ReduceAmount): builder.PrependInt64Slot(5, ReduceAmount, 0)
def ContentEnterCostReduceExcelAddReduceAmount(builder, ReduceAmount):
    """This method is deprecated. Please switch to AddReduceAmount."""
    return AddReduceAmount(builder, ReduceAmount)
def End(builder): return builder.EndObject()
def ContentEnterCostReduceExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)