# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RecipeSelectionGroupExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RecipeSelectionGroupExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsRecipeSelectionGroupExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # RecipeSelectionGroupExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RecipeSelectionGroupExcel
    def RecipeSelectionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # RecipeSelectionGroupExcel
    def RecipeSelectionGroupComponentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # RecipeSelectionGroupExcel
    def ParcelType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # RecipeSelectionGroupExcel
    def ParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # RecipeSelectionGroupExcel
    def ResultAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # RecipeSelectionGroupExcel
    def ResultAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(6)
def RecipeSelectionGroupExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddRecipeSelectionGroupId(builder, RecipeSelectionGroupId): builder.PrependInt64Slot(0, RecipeSelectionGroupId, 0)
def RecipeSelectionGroupExcelAddRecipeSelectionGroupId(builder, RecipeSelectionGroupId):
    """This method is deprecated. Please switch to AddRecipeSelectionGroupId."""
    return AddRecipeSelectionGroupId(builder, RecipeSelectionGroupId)
def AddRecipeSelectionGroupComponentId(builder, RecipeSelectionGroupComponentId): builder.PrependInt64Slot(1, RecipeSelectionGroupComponentId, 0)
def RecipeSelectionGroupExcelAddRecipeSelectionGroupComponentId(builder, RecipeSelectionGroupComponentId):
    """This method is deprecated. Please switch to AddRecipeSelectionGroupComponentId."""
    return AddRecipeSelectionGroupComponentId(builder, RecipeSelectionGroupComponentId)
def AddParcelType_(builder, ParcelType_): builder.PrependInt32Slot(2, ParcelType_, 0)
def RecipeSelectionGroupExcelAddParcelType_(builder, ParcelType_):
    """This method is deprecated. Please switch to AddParcelType_."""
    return AddParcelType_(builder, ParcelType_)
def AddParcelId(builder, ParcelId): builder.PrependInt64Slot(3, ParcelId, 0)
def RecipeSelectionGroupExcelAddParcelId(builder, ParcelId):
    """This method is deprecated. Please switch to AddParcelId."""
    return AddParcelId(builder, ParcelId)
def AddResultAmountMin(builder, ResultAmountMin): builder.PrependInt64Slot(4, ResultAmountMin, 0)
def RecipeSelectionGroupExcelAddResultAmountMin(builder, ResultAmountMin):
    """This method is deprecated. Please switch to AddResultAmountMin."""
    return AddResultAmountMin(builder, ResultAmountMin)
def AddResultAmountMax(builder, ResultAmountMax): builder.PrependInt64Slot(5, ResultAmountMax, 0)
def RecipeSelectionGroupExcelAddResultAmountMax(builder, ResultAmountMax):
    """This method is deprecated. Please switch to AddResultAmountMax."""
    return AddResultAmountMax(builder, ResultAmountMax)
def End(builder): return builder.EndObject()
def RecipeSelectionGroupExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)