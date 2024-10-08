# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstArenaExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstArenaExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConstArenaExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConstArenaExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstArenaExcel
    def AttackCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def DefenseCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def TSSStartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def EndAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def TimeRewardMaxAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def EnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def EnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def TicketCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def DailyRewardResetTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstArenaExcel
    def OpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstArenaExcel
    def CharacterSlotHideRank(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstArenaExcel
    def CharacterSlotHideRankAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstArenaExcel
    def CharacterSlotHideRankLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def CharacterSlotHideRankIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # ConstArenaExcel
    def MapSlotHideRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # ConstArenaExcel
    def RelativeOpponentRankEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def RelativeOpponentRankEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # ConstArenaExcel
    def ModifiedStatType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConstArenaExcel
    def ModifiedStatTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConstArenaExcel
    def ModifiedStatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def ModifiedStatTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # ConstArenaExcel
    def StatMulFactor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstArenaExcel
    def StatMulFactorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstArenaExcel
    def StatMulFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def StatMulFactorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0

    # ConstArenaExcel
    def StatSumFactor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstArenaExcel
    def StatSumFactorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstArenaExcel
    def StatSumFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def StatSumFactorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # ConstArenaExcel
    def NPCName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ConstArenaExcel
    def NPCNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstArenaExcel
    def NPCNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0

    # ConstArenaExcel
    def NPCMainCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def NPCSupportCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def NPCCharacterSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def TimeSpanInDaysForBattleHistory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def HiddenCharacterImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstArenaExcel
    def DefenseVictoryRewardMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def TopRankerCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def AutoRefreshIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def EchelonSettingIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def SkipAllowedTimeMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstArenaExcel
    def ShowSeasonChangeInfoStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstArenaExcel
    def ShowSeasonChangeInfoEndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstArenaExcel
    def ShowSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(32)
def ConstArenaExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddAttackCoolTime(builder, AttackCoolTime): builder.PrependInt64Slot(0, AttackCoolTime, 0)
def ConstArenaExcelAddAttackCoolTime(builder, AttackCoolTime):
    """This method is deprecated. Please switch to AddAttackCoolTime."""
    return AddAttackCoolTime(builder, AttackCoolTime)
def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(1, BattleDuration, 0)
def ConstArenaExcelAddBattleDuration(builder, BattleDuration):
    """This method is deprecated. Please switch to AddBattleDuration."""
    return AddBattleDuration(builder, BattleDuration)
def AddDefenseCoolTime(builder, DefenseCoolTime): builder.PrependInt64Slot(2, DefenseCoolTime, 0)
def ConstArenaExcelAddDefenseCoolTime(builder, DefenseCoolTime):
    """This method is deprecated. Please switch to AddDefenseCoolTime."""
    return AddDefenseCoolTime(builder, DefenseCoolTime)
def AddTSSStartCoolTime(builder, TSSStartCoolTime): builder.PrependInt64Slot(3, TSSStartCoolTime, 0)
def ConstArenaExcelAddTSSStartCoolTime(builder, TSSStartCoolTime):
    """This method is deprecated. Please switch to AddTSSStartCoolTime."""
    return AddTSSStartCoolTime(builder, TSSStartCoolTime)
def AddEndAlarm(builder, EndAlarm): builder.PrependInt64Slot(4, EndAlarm, 0)
def ConstArenaExcelAddEndAlarm(builder, EndAlarm):
    """This method is deprecated. Please switch to AddEndAlarm."""
    return AddEndAlarm(builder, EndAlarm)
def AddTimeRewardMaxAmount(builder, TimeRewardMaxAmount): builder.PrependInt64Slot(5, TimeRewardMaxAmount, 0)
def ConstArenaExcelAddTimeRewardMaxAmount(builder, TimeRewardMaxAmount):
    """This method is deprecated. Please switch to AddTimeRewardMaxAmount."""
    return AddTimeRewardMaxAmount(builder, TimeRewardMaxAmount)
def AddEnterCostType(builder, EnterCostType): builder.PrependInt32Slot(6, EnterCostType, 0)
def ConstArenaExcelAddEnterCostType(builder, EnterCostType):
    """This method is deprecated. Please switch to AddEnterCostType."""
    return AddEnterCostType(builder, EnterCostType)
def AddEnterCostId(builder, EnterCostId): builder.PrependInt64Slot(7, EnterCostId, 0)
def ConstArenaExcelAddEnterCostId(builder, EnterCostId):
    """This method is deprecated. Please switch to AddEnterCostId."""
    return AddEnterCostId(builder, EnterCostId)
def AddTicketCost(builder, TicketCost): builder.PrependInt64Slot(8, TicketCost, 0)
def ConstArenaExcelAddTicketCost(builder, TicketCost):
    """This method is deprecated. Please switch to AddTicketCost."""
    return AddTicketCost(builder, TicketCost)
def AddDailyRewardResetTime(builder, DailyRewardResetTime): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(DailyRewardResetTime), 0)
def ConstArenaExcelAddDailyRewardResetTime(builder, DailyRewardResetTime):
    """This method is deprecated. Please switch to AddDailyRewardResetTime."""
    return AddDailyRewardResetTime(builder, DailyRewardResetTime)
def AddOpenScenarioId(builder, OpenScenarioId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(OpenScenarioId), 0)
def ConstArenaExcelAddOpenScenarioId(builder, OpenScenarioId):
    """This method is deprecated. Please switch to AddOpenScenarioId."""
    return AddOpenScenarioId(builder, OpenScenarioId)
def AddCharacterSlotHideRank(builder, CharacterSlotHideRank): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSlotHideRank), 0)
def ConstArenaExcelAddCharacterSlotHideRank(builder, CharacterSlotHideRank):
    """This method is deprecated. Please switch to AddCharacterSlotHideRank."""
    return AddCharacterSlotHideRank(builder, CharacterSlotHideRank)
def StartCharacterSlotHideRankVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstArenaExcelStartCharacterSlotHideRankVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCharacterSlotHideRankVector(builder, numElems)
def AddMapSlotHideRank(builder, MapSlotHideRank): builder.PrependInt64Slot(12, MapSlotHideRank, 0)
def ConstArenaExcelAddMapSlotHideRank(builder, MapSlotHideRank):
    """This method is deprecated. Please switch to AddMapSlotHideRank."""
    return AddMapSlotHideRank(builder, MapSlotHideRank)
def AddRelativeOpponentRankStart(builder, RelativeOpponentRankStart): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(RelativeOpponentRankStart), 0)
def ConstArenaExcelAddRelativeOpponentRankStart(builder, RelativeOpponentRankStart):
    """This method is deprecated. Please switch to AddRelativeOpponentRankStart."""
    return AddRelativeOpponentRankStart(builder, RelativeOpponentRankStart)
def StartRelativeOpponentRankStartVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstArenaExcelStartRelativeOpponentRankStartVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRelativeOpponentRankStartVector(builder, numElems)
def AddRelativeOpponentRankEnd(builder, RelativeOpponentRankEnd): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(RelativeOpponentRankEnd), 0)
def ConstArenaExcelAddRelativeOpponentRankEnd(builder, RelativeOpponentRankEnd):
    """This method is deprecated. Please switch to AddRelativeOpponentRankEnd."""
    return AddRelativeOpponentRankEnd(builder, RelativeOpponentRankEnd)
def StartRelativeOpponentRankEndVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstArenaExcelStartRelativeOpponentRankEndVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRelativeOpponentRankEndVector(builder, numElems)
def AddModifiedStatType(builder, ModifiedStatType): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ModifiedStatType), 0)
def ConstArenaExcelAddModifiedStatType(builder, ModifiedStatType):
    """This method is deprecated. Please switch to AddModifiedStatType."""
    return AddModifiedStatType(builder, ModifiedStatType)
def StartModifiedStatTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConstArenaExcelStartModifiedStatTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartModifiedStatTypeVector(builder, numElems)
def AddStatMulFactor(builder, StatMulFactor): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(StatMulFactor), 0)
def ConstArenaExcelAddStatMulFactor(builder, StatMulFactor):
    """This method is deprecated. Please switch to AddStatMulFactor."""
    return AddStatMulFactor(builder, StatMulFactor)
def StartStatMulFactorVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstArenaExcelStartStatMulFactorVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStatMulFactorVector(builder, numElems)
def AddStatSumFactor(builder, StatSumFactor): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(StatSumFactor), 0)
def ConstArenaExcelAddStatSumFactor(builder, StatSumFactor):
    """This method is deprecated. Please switch to AddStatSumFactor."""
    return AddStatSumFactor(builder, StatSumFactor)
def StartStatSumFactorVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstArenaExcelStartStatSumFactorVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStatSumFactorVector(builder, numElems)
def AddNPCName(builder, NPCName): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(NPCName), 0)
def ConstArenaExcelAddNPCName(builder, NPCName):
    """This method is deprecated. Please switch to AddNPCName."""
    return AddNPCName(builder, NPCName)
def StartNPCNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConstArenaExcelStartNPCNameVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartNPCNameVector(builder, numElems)
def AddNPCMainCharacterCount(builder, NPCMainCharacterCount): builder.PrependInt64Slot(19, NPCMainCharacterCount, 0)
def ConstArenaExcelAddNPCMainCharacterCount(builder, NPCMainCharacterCount):
    """This method is deprecated. Please switch to AddNPCMainCharacterCount."""
    return AddNPCMainCharacterCount(builder, NPCMainCharacterCount)
def AddNPCSupportCharacterCount(builder, NPCSupportCharacterCount): builder.PrependInt64Slot(20, NPCSupportCharacterCount, 0)
def ConstArenaExcelAddNPCSupportCharacterCount(builder, NPCSupportCharacterCount):
    """This method is deprecated. Please switch to AddNPCSupportCharacterCount."""
    return AddNPCSupportCharacterCount(builder, NPCSupportCharacterCount)
def AddNPCCharacterSkillLevel(builder, NPCCharacterSkillLevel): builder.PrependInt64Slot(21, NPCCharacterSkillLevel, 0)
def ConstArenaExcelAddNPCCharacterSkillLevel(builder, NPCCharacterSkillLevel):
    """This method is deprecated. Please switch to AddNPCCharacterSkillLevel."""
    return AddNPCCharacterSkillLevel(builder, NPCCharacterSkillLevel)
def AddTimeSpanInDaysForBattleHistory(builder, TimeSpanInDaysForBattleHistory): builder.PrependInt64Slot(22, TimeSpanInDaysForBattleHistory, 0)
def ConstArenaExcelAddTimeSpanInDaysForBattleHistory(builder, TimeSpanInDaysForBattleHistory):
    """This method is deprecated. Please switch to AddTimeSpanInDaysForBattleHistory."""
    return AddTimeSpanInDaysForBattleHistory(builder, TimeSpanInDaysForBattleHistory)
def AddHiddenCharacterImagePath(builder, HiddenCharacterImagePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(HiddenCharacterImagePath), 0)
def ConstArenaExcelAddHiddenCharacterImagePath(builder, HiddenCharacterImagePath):
    """This method is deprecated. Please switch to AddHiddenCharacterImagePath."""
    return AddHiddenCharacterImagePath(builder, HiddenCharacterImagePath)
def AddDefenseVictoryRewardMaxCount(builder, DefenseVictoryRewardMaxCount): builder.PrependInt64Slot(24, DefenseVictoryRewardMaxCount, 0)
def ConstArenaExcelAddDefenseVictoryRewardMaxCount(builder, DefenseVictoryRewardMaxCount):
    """This method is deprecated. Please switch to AddDefenseVictoryRewardMaxCount."""
    return AddDefenseVictoryRewardMaxCount(builder, DefenseVictoryRewardMaxCount)
def AddTopRankerCountLimit(builder, TopRankerCountLimit): builder.PrependInt64Slot(25, TopRankerCountLimit, 0)
def ConstArenaExcelAddTopRankerCountLimit(builder, TopRankerCountLimit):
    """This method is deprecated. Please switch to AddTopRankerCountLimit."""
    return AddTopRankerCountLimit(builder, TopRankerCountLimit)
def AddAutoRefreshIntervalMilliSeconds(builder, AutoRefreshIntervalMilliSeconds): builder.PrependInt64Slot(26, AutoRefreshIntervalMilliSeconds, 0)
def ConstArenaExcelAddAutoRefreshIntervalMilliSeconds(builder, AutoRefreshIntervalMilliSeconds):
    """This method is deprecated. Please switch to AddAutoRefreshIntervalMilliSeconds."""
    return AddAutoRefreshIntervalMilliSeconds(builder, AutoRefreshIntervalMilliSeconds)
def AddEchelonSettingIntervalMilliSeconds(builder, EchelonSettingIntervalMilliSeconds): builder.PrependInt64Slot(27, EchelonSettingIntervalMilliSeconds, 0)
def ConstArenaExcelAddEchelonSettingIntervalMilliSeconds(builder, EchelonSettingIntervalMilliSeconds):
    """This method is deprecated. Please switch to AddEchelonSettingIntervalMilliSeconds."""
    return AddEchelonSettingIntervalMilliSeconds(builder, EchelonSettingIntervalMilliSeconds)
def AddSkipAllowedTimeMilliSeconds(builder, SkipAllowedTimeMilliSeconds): builder.PrependInt64Slot(28, SkipAllowedTimeMilliSeconds, 0)
def ConstArenaExcelAddSkipAllowedTimeMilliSeconds(builder, SkipAllowedTimeMilliSeconds):
    """This method is deprecated. Please switch to AddSkipAllowedTimeMilliSeconds."""
    return AddSkipAllowedTimeMilliSeconds(builder, SkipAllowedTimeMilliSeconds)
def AddShowSeasonChangeInfoStartTime(builder, ShowSeasonChangeInfoStartTime): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoStartTime), 0)
def ConstArenaExcelAddShowSeasonChangeInfoStartTime(builder, ShowSeasonChangeInfoStartTime):
    """This method is deprecated. Please switch to AddShowSeasonChangeInfoStartTime."""
    return AddShowSeasonChangeInfoStartTime(builder, ShowSeasonChangeInfoStartTime)
def AddShowSeasonChangeInfoEndTime(builder, ShowSeasonChangeInfoEndTime): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoEndTime), 0)
def ConstArenaExcelAddShowSeasonChangeInfoEndTime(builder, ShowSeasonChangeInfoEndTime):
    """This method is deprecated. Please switch to AddShowSeasonChangeInfoEndTime."""
    return AddShowSeasonChangeInfoEndTime(builder, ShowSeasonChangeInfoEndTime)
def AddShowSeasonId(builder, ShowSeasonId): builder.PrependInt64Slot(31, ShowSeasonId, 0)
def ConstArenaExcelAddShowSeasonId(builder, ShowSeasonId):
    """This method is deprecated. Please switch to AddShowSeasonId."""
    return AddShowSeasonId(builder, ShowSeasonId)
def End(builder): return builder.EndObject()
def ConstArenaExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)