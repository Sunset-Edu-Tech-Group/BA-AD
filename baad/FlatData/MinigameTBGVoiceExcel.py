# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGVoiceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGVoiceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMinigameTBGVoiceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MinigameTBGVoiceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MinigameTBGVoiceExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGVoiceExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGVoiceExcel
    def VoiceCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGVoiceExcel
    def VoiceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(4)
def MinigameTBGVoiceExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def MinigameTBGVoiceExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)
def MinigameTBGVoiceExcelAddUniqueId(builder, UniqueId):
    """This method is deprecated. Please switch to AddUniqueId."""
    return AddUniqueId(builder, UniqueId)
def AddVoiceCondition(builder, VoiceCondition): builder.PrependInt32Slot(2, VoiceCondition, 0)
def MinigameTBGVoiceExcelAddVoiceCondition(builder, VoiceCondition):
    """This method is deprecated. Please switch to AddVoiceCondition."""
    return AddVoiceCondition(builder, VoiceCondition)
def AddVoiceId(builder, VoiceId): builder.PrependUint32Slot(3, VoiceId, 0)
def MinigameTBGVoiceExcelAddVoiceId(builder, VoiceId):
    """This method is deprecated. Please switch to AddVoiceId."""
    return AddVoiceId(builder, VoiceId)
def End(builder): return builder.EndObject()
def MinigameTBGVoiceExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)