# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldWorldMapZoneExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldWorldMapZoneExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFieldWorldMapZoneExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FieldWorldMapZoneExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FieldWorldMapZoneExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def Date(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def OpenConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def OpenConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def CloseConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def CloseConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def ResultFieldScene(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def FieldStageInteractionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldWorldMapZoneExcel
    def LocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(10)
def FieldWorldMapZoneExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def FieldWorldMapZoneExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddGroupId(builder, GroupId): builder.PrependInt32Slot(1, GroupId, 0)
def FieldWorldMapZoneExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddDate(builder, Date): builder.PrependInt32Slot(2, Date, 0)
def FieldWorldMapZoneExcelAddDate(builder, Date):
    """This method is deprecated. Please switch to AddDate."""
    return AddDate(builder, Date)
def AddOpenConditionType(builder, OpenConditionType): builder.PrependInt32Slot(3, OpenConditionType, 0)
def FieldWorldMapZoneExcelAddOpenConditionType(builder, OpenConditionType):
    """This method is deprecated. Please switch to AddOpenConditionType."""
    return AddOpenConditionType(builder, OpenConditionType)
def AddOpenConditionId(builder, OpenConditionId): builder.PrependInt64Slot(4, OpenConditionId, 0)
def FieldWorldMapZoneExcelAddOpenConditionId(builder, OpenConditionId):
    """This method is deprecated. Please switch to AddOpenConditionId."""
    return AddOpenConditionId(builder, OpenConditionId)
def AddCloseConditionType(builder, CloseConditionType): builder.PrependInt32Slot(5, CloseConditionType, 0)
def FieldWorldMapZoneExcelAddCloseConditionType(builder, CloseConditionType):
    """This method is deprecated. Please switch to AddCloseConditionType."""
    return AddCloseConditionType(builder, CloseConditionType)
def AddCloseConditionId(builder, CloseConditionId): builder.PrependInt64Slot(6, CloseConditionId, 0)
def FieldWorldMapZoneExcelAddCloseConditionId(builder, CloseConditionId):
    """This method is deprecated. Please switch to AddCloseConditionId."""
    return AddCloseConditionId(builder, CloseConditionId)
def AddResultFieldScene(builder, ResultFieldScene): builder.PrependInt64Slot(7, ResultFieldScene, 0)
def FieldWorldMapZoneExcelAddResultFieldScene(builder, ResultFieldScene):
    """This method is deprecated. Please switch to AddResultFieldScene."""
    return AddResultFieldScene(builder, ResultFieldScene)
def AddFieldStageInteractionId(builder, FieldStageInteractionId): builder.PrependInt64Slot(8, FieldStageInteractionId, 0)
def FieldWorldMapZoneExcelAddFieldStageInteractionId(builder, FieldStageInteractionId):
    """This method is deprecated. Please switch to AddFieldStageInteractionId."""
    return AddFieldStageInteractionId(builder, FieldStageInteractionId)
def AddLocalizeCode(builder, LocalizeCode): builder.PrependUint32Slot(9, LocalizeCode, 0)
def FieldWorldMapZoneExcelAddLocalizeCode(builder, LocalizeCode):
    """This method is deprecated. Please switch to AddLocalizeCode."""
    return AddLocalizeCode(builder, LocalizeCode)
def End(builder): return builder.EndObject()
def FieldWorldMapZoneExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)