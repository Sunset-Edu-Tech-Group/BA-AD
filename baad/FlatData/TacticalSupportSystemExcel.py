# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticalSupportSystemExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticalSupportSystemExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTacticalSupportSystemExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TacticalSupportSystemExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TacticalSupportSystemExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def SummonedTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def DefaultPersonalityId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def CanTargeting(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TacticalSupportSystemExcel
    def CanCover(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TacticalSupportSystemExcel
    def ObstacleUniqueName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def ObstacleCoverRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def SummonSkilllGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def CrashObstacleOBBWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def CrashObstacleOBBHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def IsTSSBlockedNodeCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TacticalSupportSystemExcel
    def NumberOfUses(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def InventoryOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TacticalSupportSystemExcel
    def InventoryOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TacticalSupportSystemExcel
    def InventoryOffsetZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TacticalSupportSystemExcel
    def InteractionChar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def CharacterInteractionStartDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def GetOnStartEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def GetOnEndEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def SummonerCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def InteractionFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def TSAInteractionAddDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def InteractionStudentExSkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def InteractionSkillCardTexture(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def InteractionSkillSpine(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TacticalSupportSystemExcel
    def RetreatFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticalSupportSystemExcel
    def DestroyFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(27)
def TacticalSupportSystemExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def TacticalSupportSystemExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddSummonedTime(builder, SummonedTime): builder.PrependInt64Slot(1, SummonedTime, 0)
def TacticalSupportSystemExcelAddSummonedTime(builder, SummonedTime):
    """This method is deprecated. Please switch to AddSummonedTime."""
    return AddSummonedTime(builder, SummonedTime)
def AddDefaultPersonalityId(builder, DefaultPersonalityId): builder.PrependInt64Slot(2, DefaultPersonalityId, 0)
def TacticalSupportSystemExcelAddDefaultPersonalityId(builder, DefaultPersonalityId):
    """This method is deprecated. Please switch to AddDefaultPersonalityId."""
    return AddDefaultPersonalityId(builder, DefaultPersonalityId)
def AddCanTargeting(builder, CanTargeting): builder.PrependBoolSlot(3, CanTargeting, 0)
def TacticalSupportSystemExcelAddCanTargeting(builder, CanTargeting):
    """This method is deprecated. Please switch to AddCanTargeting."""
    return AddCanTargeting(builder, CanTargeting)
def AddCanCover(builder, CanCover): builder.PrependBoolSlot(4, CanCover, 0)
def TacticalSupportSystemExcelAddCanCover(builder, CanCover):
    """This method is deprecated. Please switch to AddCanCover."""
    return AddCanCover(builder, CanCover)
def AddObstacleUniqueName(builder, ObstacleUniqueName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ObstacleUniqueName), 0)
def TacticalSupportSystemExcelAddObstacleUniqueName(builder, ObstacleUniqueName):
    """This method is deprecated. Please switch to AddObstacleUniqueName."""
    return AddObstacleUniqueName(builder, ObstacleUniqueName)
def AddObstacleCoverRange(builder, ObstacleCoverRange): builder.PrependInt64Slot(6, ObstacleCoverRange, 0)
def TacticalSupportSystemExcelAddObstacleCoverRange(builder, ObstacleCoverRange):
    """This method is deprecated. Please switch to AddObstacleCoverRange."""
    return AddObstacleCoverRange(builder, ObstacleCoverRange)
def AddSummonSkilllGroupId(builder, SummonSkilllGroupId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(SummonSkilllGroupId), 0)
def TacticalSupportSystemExcelAddSummonSkilllGroupId(builder, SummonSkilllGroupId):
    """This method is deprecated. Please switch to AddSummonSkilllGroupId."""
    return AddSummonSkilllGroupId(builder, SummonSkilllGroupId)
def AddCrashObstacleOBBWidth(builder, CrashObstacleOBBWidth): builder.PrependInt64Slot(8, CrashObstacleOBBWidth, 0)
def TacticalSupportSystemExcelAddCrashObstacleOBBWidth(builder, CrashObstacleOBBWidth):
    """This method is deprecated. Please switch to AddCrashObstacleOBBWidth."""
    return AddCrashObstacleOBBWidth(builder, CrashObstacleOBBWidth)
def AddCrashObstacleOBBHeight(builder, CrashObstacleOBBHeight): builder.PrependInt64Slot(9, CrashObstacleOBBHeight, 0)
def TacticalSupportSystemExcelAddCrashObstacleOBBHeight(builder, CrashObstacleOBBHeight):
    """This method is deprecated. Please switch to AddCrashObstacleOBBHeight."""
    return AddCrashObstacleOBBHeight(builder, CrashObstacleOBBHeight)
def AddIsTSSBlockedNodeCheck(builder, IsTSSBlockedNodeCheck): builder.PrependBoolSlot(10, IsTSSBlockedNodeCheck, 0)
def TacticalSupportSystemExcelAddIsTSSBlockedNodeCheck(builder, IsTSSBlockedNodeCheck):
    """This method is deprecated. Please switch to AddIsTSSBlockedNodeCheck."""
    return AddIsTSSBlockedNodeCheck(builder, IsTSSBlockedNodeCheck)
def AddNumberOfUses(builder, NumberOfUses): builder.PrependInt32Slot(11, NumberOfUses, 0)
def TacticalSupportSystemExcelAddNumberOfUses(builder, NumberOfUses):
    """This method is deprecated. Please switch to AddNumberOfUses."""
    return AddNumberOfUses(builder, NumberOfUses)
def AddInventoryOffsetX(builder, InventoryOffsetX): builder.PrependFloat32Slot(12, InventoryOffsetX, 0.0)
def TacticalSupportSystemExcelAddInventoryOffsetX(builder, InventoryOffsetX):
    """This method is deprecated. Please switch to AddInventoryOffsetX."""
    return AddInventoryOffsetX(builder, InventoryOffsetX)
def AddInventoryOffsetY(builder, InventoryOffsetY): builder.PrependFloat32Slot(13, InventoryOffsetY, 0.0)
def TacticalSupportSystemExcelAddInventoryOffsetY(builder, InventoryOffsetY):
    """This method is deprecated. Please switch to AddInventoryOffsetY."""
    return AddInventoryOffsetY(builder, InventoryOffsetY)
def AddInventoryOffsetZ(builder, InventoryOffsetZ): builder.PrependFloat32Slot(14, InventoryOffsetZ, 0.0)
def TacticalSupportSystemExcelAddInventoryOffsetZ(builder, InventoryOffsetZ):
    """This method is deprecated. Please switch to AddInventoryOffsetZ."""
    return AddInventoryOffsetZ(builder, InventoryOffsetZ)
def AddInteractionChar(builder, InteractionChar): builder.PrependInt64Slot(15, InteractionChar, 0)
def TacticalSupportSystemExcelAddInteractionChar(builder, InteractionChar):
    """This method is deprecated. Please switch to AddInteractionChar."""
    return AddInteractionChar(builder, InteractionChar)
def AddCharacterInteractionStartDelay(builder, CharacterInteractionStartDelay): builder.PrependInt64Slot(16, CharacterInteractionStartDelay, 0)
def TacticalSupportSystemExcelAddCharacterInteractionStartDelay(builder, CharacterInteractionStartDelay):
    """This method is deprecated. Please switch to AddCharacterInteractionStartDelay."""
    return AddCharacterInteractionStartDelay(builder, CharacterInteractionStartDelay)
def AddGetOnStartEffectPath(builder, GetOnStartEffectPath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(GetOnStartEffectPath), 0)
def TacticalSupportSystemExcelAddGetOnStartEffectPath(builder, GetOnStartEffectPath):
    """This method is deprecated. Please switch to AddGetOnStartEffectPath."""
    return AddGetOnStartEffectPath(builder, GetOnStartEffectPath)
def AddGetOnEndEffectPath(builder, GetOnEndEffectPath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(GetOnEndEffectPath), 0)
def TacticalSupportSystemExcelAddGetOnEndEffectPath(builder, GetOnEndEffectPath):
    """This method is deprecated. Please switch to AddGetOnEndEffectPath."""
    return AddGetOnEndEffectPath(builder, GetOnEndEffectPath)
def AddSummonerCharacterId(builder, SummonerCharacterId): builder.PrependInt64Slot(19, SummonerCharacterId, 0)
def TacticalSupportSystemExcelAddSummonerCharacterId(builder, SummonerCharacterId):
    """This method is deprecated. Please switch to AddSummonerCharacterId."""
    return AddSummonerCharacterId(builder, SummonerCharacterId)
def AddInteractionFrame(builder, InteractionFrame): builder.PrependInt32Slot(20, InteractionFrame, 0)
def TacticalSupportSystemExcelAddInteractionFrame(builder, InteractionFrame):
    """This method is deprecated. Please switch to AddInteractionFrame."""
    return AddInteractionFrame(builder, InteractionFrame)
def AddTSAInteractionAddDuration(builder, TSAInteractionAddDuration): builder.PrependInt64Slot(21, TSAInteractionAddDuration, 0)
def TacticalSupportSystemExcelAddTSAInteractionAddDuration(builder, TSAInteractionAddDuration):
    """This method is deprecated. Please switch to AddTSAInteractionAddDuration."""
    return AddTSAInteractionAddDuration(builder, TSAInteractionAddDuration)
def AddInteractionStudentExSkillGroupId(builder, InteractionStudentExSkillGroupId): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionStudentExSkillGroupId), 0)
def TacticalSupportSystemExcelAddInteractionStudentExSkillGroupId(builder, InteractionStudentExSkillGroupId):
    """This method is deprecated. Please switch to AddInteractionStudentExSkillGroupId."""
    return AddInteractionStudentExSkillGroupId(builder, InteractionStudentExSkillGroupId)
def AddInteractionSkillCardTexture(builder, InteractionSkillCardTexture): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionSkillCardTexture), 0)
def TacticalSupportSystemExcelAddInteractionSkillCardTexture(builder, InteractionSkillCardTexture):
    """This method is deprecated. Please switch to AddInteractionSkillCardTexture."""
    return AddInteractionSkillCardTexture(builder, InteractionSkillCardTexture)
def AddInteractionSkillSpine(builder, InteractionSkillSpine): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(InteractionSkillSpine), 0)
def TacticalSupportSystemExcelAddInteractionSkillSpine(builder, InteractionSkillSpine):
    """This method is deprecated. Please switch to AddInteractionSkillSpine."""
    return AddInteractionSkillSpine(builder, InteractionSkillSpine)
def AddRetreatFrame(builder, RetreatFrame): builder.PrependInt32Slot(25, RetreatFrame, 0)
def TacticalSupportSystemExcelAddRetreatFrame(builder, RetreatFrame):
    """This method is deprecated. Please switch to AddRetreatFrame."""
    return AddRetreatFrame(builder, RetreatFrame)
def AddDestroyFrame(builder, DestroyFrame): builder.PrependInt32Slot(26, DestroyFrame, 0)
def TacticalSupportSystemExcelAddDestroyFrame(builder, DestroyFrame):
    """This method is deprecated. Please switch to AddDestroyFrame."""
    return AddDestroyFrame(builder, DestroyFrame)
def End(builder): return builder.EndObject()
def TacticalSupportSystemExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)