# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GoodsExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GoodsExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGoodsExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GoodsExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GoodsExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def Rarity_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GoodsExcel
    def ConsumeParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # GoodsExcel
    def ConsumeParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # GoodsExcel
    def ConsumeParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # GoodsExcel
    def ConsumeParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ConsumeParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ConsumeParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # GoodsExcel
    def ConsumeParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ConsumeParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ConsumeParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # GoodsExcel
    def ConsumeCondition_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # GoodsExcel
    def ConsumeCondition_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # GoodsExcel
    def ConsumeCondition_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeCondition_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # GoodsExcel
    def ConsumeGachaTicketType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def ConsumeGachaTicketTypeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def ProductIdAOS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def ProductIdiOS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def ConsumeExtraStep(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ConsumeExtraStepAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ConsumeExtraStepLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeExtraStepIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # GoodsExcel
    def ConsumeExtraAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ConsumeExtraAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ConsumeExtraAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ConsumeExtraAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # GoodsExcel
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GoodsExcel
    def ParcelType_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # GoodsExcel
    def ParcelType_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # GoodsExcel
    def ParcelType_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ParcelType_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # GoodsExcel
    def ParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0

    # GoodsExcel
    def ParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GoodsExcel
    def ParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # GoodsExcel
    def ParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GoodsExcel
    def ParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

def Start(builder): builder.StartObject(18)
def GoodsExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def GoodsExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddType(builder, Type): builder.PrependInt32Slot(1, Type, 0)
def GoodsExcelAddType(builder, Type):
    """This method is deprecated. Please switch to AddType."""
    return AddType(builder, Type)
def AddRarity_(builder, Rarity_): builder.PrependInt32Slot(2, Rarity_, 0)
def GoodsExcelAddRarity_(builder, Rarity_):
    """This method is deprecated. Please switch to AddRarity_."""
    return AddRarity_(builder, Rarity_)
def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)
def GoodsExcelAddIconPath(builder, IconPath):
    """This method is deprecated. Please switch to AddIconPath."""
    return AddIconPath(builder, IconPath)
def AddConsumeParcelType(builder, ConsumeParcelType): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeParcelType), 0)
def GoodsExcelAddConsumeParcelType(builder, ConsumeParcelType):
    """This method is deprecated. Please switch to AddConsumeParcelType."""
    return AddConsumeParcelType(builder, ConsumeParcelType)
def StartConsumeParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GoodsExcelStartConsumeParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeParcelTypeVector(builder, numElems)
def AddConsumeParcelId(builder, ConsumeParcelId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeParcelId), 0)
def GoodsExcelAddConsumeParcelId(builder, ConsumeParcelId):
    """This method is deprecated. Please switch to AddConsumeParcelId."""
    return AddConsumeParcelId(builder, ConsumeParcelId)
def StartConsumeParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartConsumeParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeParcelIdVector(builder, numElems)
def AddConsumeParcelAmount(builder, ConsumeParcelAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeParcelAmount), 0)
def GoodsExcelAddConsumeParcelAmount(builder, ConsumeParcelAmount):
    """This method is deprecated. Please switch to AddConsumeParcelAmount."""
    return AddConsumeParcelAmount(builder, ConsumeParcelAmount)
def StartConsumeParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartConsumeParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeParcelAmountVector(builder, numElems)
def AddConsumeCondition_(builder, ConsumeCondition_): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeCondition_), 0)
def GoodsExcelAddConsumeCondition_(builder, ConsumeCondition_):
    """This method is deprecated. Please switch to AddConsumeCondition_."""
    return AddConsumeCondition_(builder, ConsumeCondition_)
def StartConsumeCondition_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GoodsExcelStartConsumeCondition_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeCondition_Vector(builder, numElems)
def AddConsumeGachaTicketType(builder, ConsumeGachaTicketType): builder.PrependInt32Slot(8, ConsumeGachaTicketType, 0)
def GoodsExcelAddConsumeGachaTicketType(builder, ConsumeGachaTicketType):
    """This method is deprecated. Please switch to AddConsumeGachaTicketType."""
    return AddConsumeGachaTicketType(builder, ConsumeGachaTicketType)
def AddConsumeGachaTicketTypeAmount(builder, ConsumeGachaTicketTypeAmount): builder.PrependInt64Slot(9, ConsumeGachaTicketTypeAmount, 0)
def GoodsExcelAddConsumeGachaTicketTypeAmount(builder, ConsumeGachaTicketTypeAmount):
    """This method is deprecated. Please switch to AddConsumeGachaTicketTypeAmount."""
    return AddConsumeGachaTicketTypeAmount(builder, ConsumeGachaTicketTypeAmount)
def AddProductIdAOS(builder, ProductIdAOS): builder.PrependInt64Slot(10, ProductIdAOS, 0)
def GoodsExcelAddProductIdAOS(builder, ProductIdAOS):
    """This method is deprecated. Please switch to AddProductIdAOS."""
    return AddProductIdAOS(builder, ProductIdAOS)
def AddProductIdiOS(builder, ProductIdiOS): builder.PrependInt64Slot(11, ProductIdiOS, 0)
def GoodsExcelAddProductIdiOS(builder, ProductIdiOS):
    """This method is deprecated. Please switch to AddProductIdiOS."""
    return AddProductIdiOS(builder, ProductIdiOS)
def AddConsumeExtraStep(builder, ConsumeExtraStep): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeExtraStep), 0)
def GoodsExcelAddConsumeExtraStep(builder, ConsumeExtraStep):
    """This method is deprecated. Please switch to AddConsumeExtraStep."""
    return AddConsumeExtraStep(builder, ConsumeExtraStep)
def StartConsumeExtraStepVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartConsumeExtraStepVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeExtraStepVector(builder, numElems)
def AddConsumeExtraAmount(builder, ConsumeExtraAmount): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(ConsumeExtraAmount), 0)
def GoodsExcelAddConsumeExtraAmount(builder, ConsumeExtraAmount):
    """This method is deprecated. Please switch to AddConsumeExtraAmount."""
    return AddConsumeExtraAmount(builder, ConsumeExtraAmount)
def StartConsumeExtraAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartConsumeExtraAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartConsumeExtraAmountVector(builder, numElems)
def AddState(builder, State): builder.PrependInt32Slot(14, State, 0)
def GoodsExcelAddState(builder, State):
    """This method is deprecated. Please switch to AddState."""
    return AddState(builder, State)
def AddParcelType_(builder, ParcelType_): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelType_), 0)
def GoodsExcelAddParcelType_(builder, ParcelType_):
    """This method is deprecated. Please switch to AddParcelType_."""
    return AddParcelType_(builder, ParcelType_)
def StartParcelType_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GoodsExcelStartParcelType_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelType_Vector(builder, numElems)
def AddParcelId(builder, ParcelId): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelId), 0)
def GoodsExcelAddParcelId(builder, ParcelId):
    """This method is deprecated. Please switch to AddParcelId."""
    return AddParcelId(builder, ParcelId)
def StartParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelIdVector(builder, numElems)
def AddParcelAmount(builder, ParcelAmount): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelAmount), 0)
def GoodsExcelAddParcelAmount(builder, ParcelAmount):
    """This method is deprecated. Please switch to AddParcelAmount."""
    return AddParcelAmount(builder, ParcelAmount)
def StartParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GoodsExcelStartParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def GoodsExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)