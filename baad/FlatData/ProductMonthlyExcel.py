# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ProductMonthlyExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProductMonthlyExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProductMonthlyExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ProductMonthlyExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProductMonthlyExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def ProductId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductMonthlyExcel
    def StoreType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def Price(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def PriceReference(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductMonthlyExcel
    def ProductTagType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def MonthlyDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def UseMonthlyProductCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ProductMonthlyExcel
    def ParcelType_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ProductMonthlyExcel
    def ParcelType_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ProductMonthlyExcel
    def ParcelType_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def ParcelType_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # ProductMonthlyExcel
    def ParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ProductMonthlyExcel
    def ParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ProductMonthlyExcel
    def ParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def ParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # ProductMonthlyExcel
    def ParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ProductMonthlyExcel
    def ParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ProductMonthlyExcel
    def ParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def ParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # ProductMonthlyExcel
    def EnterCostReduceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ProductMonthlyExcel
    def DailyParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ProductMonthlyExcel
    def DailyParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # ProductMonthlyExcel
    def DailyParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ProductMonthlyExcel
    def DailyParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # ProductMonthlyExcel
    def DailyParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ProductMonthlyExcel
    def DailyParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductMonthlyExcel
    def DailyParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

def Start(builder): builder.StartObject(15)
def ProductMonthlyExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ProductMonthlyExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddProductId(builder, ProductId): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(ProductId), 0)
def ProductMonthlyExcelAddProductId(builder, ProductId):
    """This method is deprecated. Please switch to AddProductId."""
    return AddProductId(builder, ProductId)
def AddStoreType_(builder, StoreType_): builder.PrependInt32Slot(2, StoreType_, 0)
def ProductMonthlyExcelAddStoreType_(builder, StoreType_):
    """This method is deprecated. Please switch to AddStoreType_."""
    return AddStoreType_(builder, StoreType_)
def AddPrice(builder, Price): builder.PrependInt64Slot(3, Price, 0)
def ProductMonthlyExcelAddPrice(builder, Price):
    """This method is deprecated. Please switch to AddPrice."""
    return AddPrice(builder, Price)
def AddPriceReference(builder, PriceReference): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PriceReference), 0)
def ProductMonthlyExcelAddPriceReference(builder, PriceReference):
    """This method is deprecated. Please switch to AddPriceReference."""
    return AddPriceReference(builder, PriceReference)
def AddProductTagType_(builder, ProductTagType_): builder.PrependInt32Slot(5, ProductTagType_, 0)
def ProductMonthlyExcelAddProductTagType_(builder, ProductTagType_):
    """This method is deprecated. Please switch to AddProductTagType_."""
    return AddProductTagType_(builder, ProductTagType_)
def AddMonthlyDays(builder, MonthlyDays): builder.PrependInt64Slot(6, MonthlyDays, 0)
def ProductMonthlyExcelAddMonthlyDays(builder, MonthlyDays):
    """This method is deprecated. Please switch to AddMonthlyDays."""
    return AddMonthlyDays(builder, MonthlyDays)
def AddUseMonthlyProductCheck(builder, UseMonthlyProductCheck): builder.PrependBoolSlot(7, UseMonthlyProductCheck, 0)
def ProductMonthlyExcelAddUseMonthlyProductCheck(builder, UseMonthlyProductCheck):
    """This method is deprecated. Please switch to AddUseMonthlyProductCheck."""
    return AddUseMonthlyProductCheck(builder, UseMonthlyProductCheck)
def AddParcelType_(builder, ParcelType_): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelType_), 0)
def ProductMonthlyExcelAddParcelType_(builder, ParcelType_):
    """This method is deprecated. Please switch to AddParcelType_."""
    return AddParcelType_(builder, ParcelType_)
def StartParcelType_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ProductMonthlyExcelStartParcelType_Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelType_Vector(builder, numElems)
def AddParcelId(builder, ParcelId): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelId), 0)
def ProductMonthlyExcelAddParcelId(builder, ParcelId):
    """This method is deprecated. Please switch to AddParcelId."""
    return AddParcelId(builder, ParcelId)
def StartParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ProductMonthlyExcelStartParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelIdVector(builder, numElems)
def AddParcelAmount(builder, ParcelAmount): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelAmount), 0)
def ProductMonthlyExcelAddParcelAmount(builder, ParcelAmount):
    """This method is deprecated. Please switch to AddParcelAmount."""
    return AddParcelAmount(builder, ParcelAmount)
def StartParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ProductMonthlyExcelStartParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartParcelAmountVector(builder, numElems)
def AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId): builder.PrependInt64Slot(11, EnterCostReduceGroupId, 0)
def ProductMonthlyExcelAddEnterCostReduceGroupId(builder, EnterCostReduceGroupId):
    """This method is deprecated. Please switch to AddEnterCostReduceGroupId."""
    return AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId)
def AddDailyParcelType(builder, DailyParcelType): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(DailyParcelType), 0)
def ProductMonthlyExcelAddDailyParcelType(builder, DailyParcelType):
    """This method is deprecated. Please switch to AddDailyParcelType."""
    return AddDailyParcelType(builder, DailyParcelType)
def StartDailyParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ProductMonthlyExcelStartDailyParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDailyParcelTypeVector(builder, numElems)
def AddDailyParcelId(builder, DailyParcelId): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(DailyParcelId), 0)
def ProductMonthlyExcelAddDailyParcelId(builder, DailyParcelId):
    """This method is deprecated. Please switch to AddDailyParcelId."""
    return AddDailyParcelId(builder, DailyParcelId)
def StartDailyParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ProductMonthlyExcelStartDailyParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDailyParcelIdVector(builder, numElems)
def AddDailyParcelAmount(builder, DailyParcelAmount): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(DailyParcelAmount), 0)
def ProductMonthlyExcelAddDailyParcelAmount(builder, DailyParcelAmount):
    """This method is deprecated. Please switch to AddDailyParcelAmount."""
    return AddDailyParcelAmount(builder, DailyParcelAmount)
def StartDailyParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ProductMonthlyExcelStartDailyParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDailyParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def ProductMonthlyExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)