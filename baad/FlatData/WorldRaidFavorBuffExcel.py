# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WorldRaidFavorBuffExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldRaidFavorBuffExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWorldRaidFavorBuffExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # WorldRaidFavorBuffExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WorldRaidFavorBuffExcel
    def WorldRaidFavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidFavorBuffExcel
    def WorldRaidFavorRankBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(2)
def WorldRaidFavorBuffExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddWorldRaidFavorRank(builder, WorldRaidFavorRank): builder.PrependInt64Slot(0, WorldRaidFavorRank, 0)
def WorldRaidFavorBuffExcelAddWorldRaidFavorRank(builder, WorldRaidFavorRank):
    """This method is deprecated. Please switch to AddWorldRaidFavorRank."""
    return AddWorldRaidFavorRank(builder, WorldRaidFavorRank)
def AddWorldRaidFavorRankBonus(builder, WorldRaidFavorRankBonus): builder.PrependInt64Slot(1, WorldRaidFavorRankBonus, 0)
def WorldRaidFavorBuffExcelAddWorldRaidFavorRankBonus(builder, WorldRaidFavorRankBonus):
    """This method is deprecated. Please switch to AddWorldRaidFavorRankBonus."""
    return AddWorldRaidFavorRankBonus(builder, WorldRaidFavorRankBonus)
def End(builder): return builder.EndObject()
def WorldRaidFavorBuffExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)