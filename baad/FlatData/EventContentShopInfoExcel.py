# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentShopInfoExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentShopInfoExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentShopInfoExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentShopInfoExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentShopInfoExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentShopInfoExcel
    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentShopInfoExcel
    def LocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EventContentShopInfoExcel
    def CostParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentShopInfoExcel
    def CostParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentShopInfoExcel
    def CostParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentShopInfoExcel
    def CostParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # EventContentShopInfoExcel
    def CostParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentShopInfoExcel
    def CostParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentShopInfoExcel
    def CostParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentShopInfoExcel
    def CostParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # EventContentShopInfoExcel
    def IsRefresh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EventContentShopInfoExcel
    def IsSoldOutDimmed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EventContentShopInfoExcel
    def AutoRefreshCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentShopInfoExcel
    def RefreshAbleCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentShopInfoExcel
    def GoodsId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentShopInfoExcel
    def GoodsIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentShopInfoExcel
    def GoodsIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentShopInfoExcel
    def GoodsIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # EventContentShopInfoExcel
    def OpenPeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentShopInfoExcel
    def OpenPeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentShopInfoExcel
    def ShopProductUpdateDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(13)
def EventContentShopInfoExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentShopInfoExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(1, CategoryType, 0)
def EventContentShopInfoExcelAddCategoryType(builder, CategoryType):
    """This method is deprecated. Please switch to AddCategoryType."""
    return AddCategoryType(builder, CategoryType)
def AddLocalizeCode(builder, LocalizeCode): builder.PrependUint32Slot(2, LocalizeCode, 0)
def EventContentShopInfoExcelAddLocalizeCode(builder, LocalizeCode):
    """This method is deprecated. Please switch to AddLocalizeCode."""
    return AddLocalizeCode(builder, LocalizeCode)
def AddCostParcelType(builder, CostParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(CostParcelType), 0)
def EventContentShopInfoExcelAddCostParcelType(builder, CostParcelType):
    """This method is deprecated. Please switch to AddCostParcelType."""
    return AddCostParcelType(builder, CostParcelType)
def StartCostParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentShopInfoExcelStartCostParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCostParcelTypeVector(builder, numElems)
def AddCostParcelId(builder, CostParcelId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(CostParcelId), 0)
def EventContentShopInfoExcelAddCostParcelId(builder, CostParcelId):
    """This method is deprecated. Please switch to AddCostParcelId."""
    return AddCostParcelId(builder, CostParcelId)
def StartCostParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentShopInfoExcelStartCostParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCostParcelIdVector(builder, numElems)
def AddIsRefresh(builder, IsRefresh): builder.PrependBoolSlot(5, IsRefresh, 0)
def EventContentShopInfoExcelAddIsRefresh(builder, IsRefresh):
    """This method is deprecated. Please switch to AddIsRefresh."""
    return AddIsRefresh(builder, IsRefresh)
def AddIsSoldOutDimmed(builder, IsSoldOutDimmed): builder.PrependBoolSlot(6, IsSoldOutDimmed, 0)
def EventContentShopInfoExcelAddIsSoldOutDimmed(builder, IsSoldOutDimmed):
    """This method is deprecated. Please switch to AddIsSoldOutDimmed."""
    return AddIsSoldOutDimmed(builder, IsSoldOutDimmed)
def AddAutoRefreshCoolTime(builder, AutoRefreshCoolTime): builder.PrependInt64Slot(7, AutoRefreshCoolTime, 0)
def EventContentShopInfoExcelAddAutoRefreshCoolTime(builder, AutoRefreshCoolTime):
    """This method is deprecated. Please switch to AddAutoRefreshCoolTime."""
    return AddAutoRefreshCoolTime(builder, AutoRefreshCoolTime)
def AddRefreshAbleCount(builder, RefreshAbleCount): builder.PrependInt64Slot(8, RefreshAbleCount, 0)
def EventContentShopInfoExcelAddRefreshAbleCount(builder, RefreshAbleCount):
    """This method is deprecated. Please switch to AddRefreshAbleCount."""
    return AddRefreshAbleCount(builder, RefreshAbleCount)
def AddGoodsId(builder, GoodsId): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsId), 0)
def EventContentShopInfoExcelAddGoodsId(builder, GoodsId):
    """This method is deprecated. Please switch to AddGoodsId."""
    return AddGoodsId(builder, GoodsId)
def StartGoodsIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentShopInfoExcelStartGoodsIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartGoodsIdVector(builder, numElems)
def AddOpenPeriodFrom(builder, OpenPeriodFrom): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodFrom), 0)
def EventContentShopInfoExcelAddOpenPeriodFrom(builder, OpenPeriodFrom):
    """This method is deprecated. Please switch to AddOpenPeriodFrom."""
    return AddOpenPeriodFrom(builder, OpenPeriodFrom)
def AddOpenPeriodTo(builder, OpenPeriodTo): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodTo), 0)
def EventContentShopInfoExcelAddOpenPeriodTo(builder, OpenPeriodTo):
    """This method is deprecated. Please switch to AddOpenPeriodTo."""
    return AddOpenPeriodTo(builder, OpenPeriodTo)
def AddShopProductUpdateDate(builder, ShopProductUpdateDate): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(ShopProductUpdateDate), 0)
def EventContentShopInfoExcelAddShopProductUpdateDate(builder, ShopProductUpdateDate):
    """This method is deprecated. Please switch to AddShopProductUpdateDate."""
    return AddShopProductUpdateDate(builder, ShopProductUpdateDate)
def End(builder): return builder.EndObject()
def EventContentShopInfoExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)