# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentMiniEventTokenExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentMiniEventTokenExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentMiniEventTokenExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentMiniEventTokenExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentMiniEventTokenExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMiniEventTokenExcel
    def ItemUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentMiniEventTokenExcel
    def MaximumAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(3)
def EventContentMiniEventTokenExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentMiniEventTokenExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddItemUniqueId(builder, ItemUniqueId): builder.PrependInt64Slot(1, ItemUniqueId, 0)
def EventContentMiniEventTokenExcelAddItemUniqueId(builder, ItemUniqueId):
    """This method is deprecated. Please switch to AddItemUniqueId."""
    return AddItemUniqueId(builder, ItemUniqueId)
def AddMaximumAmount(builder, MaximumAmount): builder.PrependInt64Slot(2, MaximumAmount, 0)
def EventContentMiniEventTokenExcelAddMaximumAmount(builder, MaximumAmount):
    """This method is deprecated. Please switch to AddMaximumAmount."""
    return AddMaximumAmount(builder, MaximumAmount)
def End(builder): return builder.EndObject()
def EventContentMiniEventTokenExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)