# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamTimelineExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamTimelineExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameDreamTimelineExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameDreamTimelineExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameDreamTimelineExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def DreamMakerDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def DreamMakerActionPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def EnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def Bgm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def ArtLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameDreamTimelineExcel
    def DesignLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(9)
def MiniGameDreamTimelineExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def MiniGameDreamTimelineExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def MiniGameDreamTimelineExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(2, GroupId, 0)
def MiniGameDreamTimelineExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddDreamMakerDays(builder, DreamMakerDays): builder.PrependInt64Slot(3, DreamMakerDays, 0)
def MiniGameDreamTimelineExcelAddDreamMakerDays(builder, DreamMakerDays):
    """This method is deprecated. Please switch to AddDreamMakerDays."""
    return AddDreamMakerDays(builder, DreamMakerDays)
def AddDreamMakerActionPoint(builder, DreamMakerActionPoint): builder.PrependInt64Slot(4, DreamMakerActionPoint, 0)
def MiniGameDreamTimelineExcelAddDreamMakerActionPoint(builder, DreamMakerActionPoint):
    """This method is deprecated. Please switch to AddDreamMakerActionPoint."""
    return AddDreamMakerActionPoint(builder, DreamMakerActionPoint)
def AddEnterScenarioGroupId(builder, EnterScenarioGroupId): builder.PrependInt64Slot(5, EnterScenarioGroupId, 0)
def MiniGameDreamTimelineExcelAddEnterScenarioGroupId(builder, EnterScenarioGroupId):
    """This method is deprecated. Please switch to AddEnterScenarioGroupId."""
    return AddEnterScenarioGroupId(builder, EnterScenarioGroupId)
def AddBgm(builder, Bgm): builder.PrependInt64Slot(6, Bgm, 0)
def MiniGameDreamTimelineExcelAddBgm(builder, Bgm):
    """This method is deprecated. Please switch to AddBgm."""
    return AddBgm(builder, Bgm)
def AddArtLevelPath(builder, ArtLevelPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(ArtLevelPath), 0)
def MiniGameDreamTimelineExcelAddArtLevelPath(builder, ArtLevelPath):
    """This method is deprecated. Please switch to AddArtLevelPath."""
    return AddArtLevelPath(builder, ArtLevelPath)
def AddDesignLevelPath(builder, DesignLevelPath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(DesignLevelPath), 0)
def MiniGameDreamTimelineExcelAddDesignLevelPath(builder, DesignLevelPath):
    """This method is deprecated. Please switch to AddDesignLevelPath."""
    return AddDesignLevelPath(builder, DesignLevelPath)
def End(builder): return builder.EndObject()
def MiniGameDreamTimelineExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)