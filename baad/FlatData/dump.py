from enum import IntEnum

from ..lib.TableEncryptionService import TableEncryptionService


def dump_table(obj) -> list:
    table_encryption = TableEncryptionService()

    typ_name = obj.__class__.__name__[:-5]
    dump_func = next(f for x, f in globals().items() if x.endswith(f'_{typ_name}'))
    password = table_encryption.create_key(typ_name[:-5])
    return [
        dump_func(obj.DataList(j), password)
        for j in range(obj.DataListLength())
    ]


def dump_GroundVector3(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_float(obj.X(), password),
        'Y': table_encryption.convert_float(obj.Y(), password),
        'Z': table_encryption.convert_float(obj.Z(), password),
    }


def dump_AcademyFavorScheduleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'ScheduleGroupId': table_encryption.convert_long(obj.ScheduleGroupId(), password),
        'OrderInGroup': table_encryption.convert_long(obj.OrderInGroup(), password),
        'Location': table_encryption.convert_string(obj.Location(), password),
        'LocalizeScenarioId': table_encryption.convert_uint(obj.LocalizeScenarioId(), password),
        'FavorRank': table_encryption.convert_long(obj.FavorRank(), password),
        'SecretStoneAmount': table_encryption.convert_long(obj.SecretStoneAmount(), password),
        'ScenarioSriptGroupId': table_encryption.convert_long(obj.ScenarioSriptGroupId(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_AcademyLocationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'PrefabPath': table_encryption.convert_string(obj.PrefabPath(), password),
        'IconImagePath': table_encryption.convert_string(obj.IconImagePath(), password),
        'OpenCondition': [School(table_encryption.convert_int(obj.OpenCondition(j), password)).name for j in range(obj.OpenConditionLength())],
        'OpenConditionCount': [table_encryption.convert_long(obj.OpenConditionCount(j), password) for j in range(obj.OpenConditionCountLength())],
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'OpenTeacherRank': table_encryption.convert_long(obj.OpenTeacherRank(), password),
    }


def dump_AcademyLocationRankExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Rank': table_encryption.convert_long(obj.Rank(), password),
        'RankExp': table_encryption.convert_long(obj.RankExp(), password),
        'TotalExp': table_encryption.convert_long(obj.TotalExp(), password),
    }


def dump_AcademyMessanger1Excel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MessageGroupId': table_encryption.convert_long(obj.MessageGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MessageCondition': AcademyMessageConditions(table_encryption.convert_int(obj.MessageCondition(), password)).name,
        'ConditionValue': table_encryption.convert_long(obj.ConditionValue(), password),
        'PreConditionGroupId': table_encryption.convert_long(obj.PreConditionGroupId(), password),
        'PreConditionFavorScheduleId': table_encryption.convert_long(obj.PreConditionFavorScheduleId(), password),
        'FavorScheduleId': table_encryption.convert_long(obj.FavorScheduleId(), password),
        'NextGroupId': table_encryption.convert_long(obj.NextGroupId(), password),
        'FeedbackTimeMillisec': table_encryption.convert_long(obj.FeedbackTimeMillisec(), password),
        'MessageType': AcademyMessageTypes(table_encryption.convert_int(obj.MessageType(), password)).name,
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'MessageKR': table_encryption.convert_string(obj.MessageKR(), password),
        'MessageJP': table_encryption.convert_string(obj.MessageJP(), password),
    }


def dump_AcademyMessanger2Excel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MessageGroupId': table_encryption.convert_long(obj.MessageGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MessageCondition': AcademyMessageConditions(table_encryption.convert_int(obj.MessageCondition(), password)).name,
        'ConditionValue': table_encryption.convert_long(obj.ConditionValue(), password),
        'PreConditionGroupId': table_encryption.convert_long(obj.PreConditionGroupId(), password),
        'PreConditionFavorScheduleId': table_encryption.convert_long(obj.PreConditionFavorScheduleId(), password),
        'FavorScheduleId': table_encryption.convert_long(obj.FavorScheduleId(), password),
        'NextGroupId': table_encryption.convert_long(obj.NextGroupId(), password),
        'FeedbackTimeMillisec': table_encryption.convert_long(obj.FeedbackTimeMillisec(), password),
        'MessageType': AcademyMessageTypes(table_encryption.convert_int(obj.MessageType(), password)).name,
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'MessageKR': table_encryption.convert_string(obj.MessageKR(), password),
        'MessageJP': table_encryption.convert_string(obj.MessageJP(), password),
    }


def dump_AcademyMessanger3Excel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MessageGroupId': table_encryption.convert_long(obj.MessageGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MessageCondition': AcademyMessageConditions(table_encryption.convert_int(obj.MessageCondition(), password)).name,
        'ConditionValue': table_encryption.convert_long(obj.ConditionValue(), password),
        'PreConditionGroupId': table_encryption.convert_long(obj.PreConditionGroupId(), password),
        'PreConditionFavorScheduleId': table_encryption.convert_long(obj.PreConditionFavorScheduleId(), password),
        'FavorScheduleId': table_encryption.convert_long(obj.FavorScheduleId(), password),
        'NextGroupId': table_encryption.convert_long(obj.NextGroupId(), password),
        'FeedbackTimeMillisec': table_encryption.convert_long(obj.FeedbackTimeMillisec(), password),
        'MessageType': AcademyMessageTypes(table_encryption.convert_int(obj.MessageType(), password)).name,
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'MessageKR': table_encryption.convert_string(obj.MessageKR(), password),
        'MessageJP': table_encryption.convert_string(obj.MessageJP(), password),
    }


def dump_AcademyMessangerExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MessageGroupId': table_encryption.convert_long(obj.MessageGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MessageCondition': AcademyMessageConditions(table_encryption.convert_int(obj.MessageCondition(), password)).name,
        'ConditionValue': table_encryption.convert_long(obj.ConditionValue(), password),
        'PreConditionGroupId': table_encryption.convert_long(obj.PreConditionGroupId(), password),
        'PreConditionFavorScheduleId': table_encryption.convert_long(obj.PreConditionFavorScheduleId(), password),
        'FavorScheduleId': table_encryption.convert_long(obj.FavorScheduleId(), password),
        'NextGroupId': table_encryption.convert_long(obj.NextGroupId(), password),
        'FeedbackTimeMillisec': table_encryption.convert_long(obj.FeedbackTimeMillisec(), password),
        'MessageType': AcademyMessageTypes(table_encryption.convert_int(obj.MessageType(), password)).name,
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'MessageKR': table_encryption.convert_string(obj.MessageKR(), password),
        'MessageJP': table_encryption.convert_string(obj.MessageJP(), password),
    }


def dump_AcademyRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Location': table_encryption.convert_string(obj.Location(), password),
        'ScheduleGroupId': table_encryption.convert_long(obj.ScheduleGroupId(), password),
        'OrderInGroup': table_encryption.convert_long(obj.OrderInGroup(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProgressTexture': table_encryption.convert_string(obj.ProgressTexture(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'LocationRank': table_encryption.convert_long(obj.LocationRank(), password),
        'FavorExp': table_encryption.convert_long(obj.FavorExp(), password),
        'SecretStoneAmount': table_encryption.convert_long(obj.SecretStoneAmount(), password),
        'SecretStoneProb': table_encryption.convert_long(obj.SecretStoneProb(), password),
        'ExtraFavorExp': table_encryption.convert_long(obj.ExtraFavorExp(), password),
        'ExtraFavorExpProb': table_encryption.convert_long(obj.ExtraFavorExpProb(), password),
        'ExtraRewardParcelType': [ParcelType(table_encryption.convert_int(obj.ExtraRewardParcelType(j), password)).name for j in range(obj.ExtraRewardParcelTypeLength())],
        'ExtraRewardParcelId': [table_encryption.convert_long(obj.ExtraRewardParcelId(j), password) for j in range(obj.ExtraRewardParcelIdLength())],
        'ExtraRewardAmount': [table_encryption.convert_long(obj.ExtraRewardAmount(j), password) for j in range(obj.ExtraRewardAmountLength())],
        'ExtraRewardProb': [table_encryption.convert_long(obj.ExtraRewardProb(j), password) for j in range(obj.ExtraRewardProbLength())],
        'IsExtraRewardDisplayed': [obj.IsExtraRewardDisplayed(j) for j in range(obj.IsExtraRewardDisplayedLength())],
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_AcademyTicketExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LocationRankSum': table_encryption.convert_long(obj.LocationRankSum(), password),
        'ScheduleTicktetMax': table_encryption.convert_long(obj.ScheduleTicktetMax(), password),
    }


def dump_AcademyZoneExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocationId': table_encryption.convert_long(obj.LocationId(), password),
        'LocationRankForUnlock': table_encryption.convert_long(obj.LocationRankForUnlock(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'StudentVisitProb': [table_encryption.convert_long(obj.StudentVisitProb(j), password) for j in range(obj.StudentVisitProbLength())],
        'RewardGroupId': table_encryption.convert_long(obj.RewardGroupId(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
    }


def dump_AccountLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Level': table_encryption.convert_long(obj.Level(), password),
        'Exp': table_encryption.convert_long(obj.Exp(), password),
        'APAutoChargeMax': table_encryption.convert_long(obj.APAutoChargeMax(), password),
        'NeedReportEvent': obj.NeedReportEvent(),
    }


def dump_BlendData(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Type': table_encryption.convert_int(obj.Type(), password),
        'InfoList': [dump_BlendInfo(obj.InfoList(j), password) for j in range(obj.InfoListLength())],
    }


def dump_BlendInfo(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'From': table_encryption.convert_int(obj.From(), password),
        'To': table_encryption.convert_int(obj.To(), password),
        'Blend': table_encryption.convert_float(obj.Blend(), password),
    }


def dump_AnimatorData(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'DefaultStateName': table_encryption.convert_string(obj.DefaultStateName(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'DataList': [dump_AniStateData(obj.DataList(j), password) for j in range(obj.DataListLength())],
    }


def dump_AniStateData(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StateName': table_encryption.convert_string(obj.StateName(), password),
        'StatePrefix': table_encryption.convert_string(obj.StatePrefix(), password),
        'StateNameWithPrefix': table_encryption.convert_string(obj.StateNameWithPrefix(), password),
        'Tag': table_encryption.convert_string(obj.Tag(), password),
        'SpeedParameterName': table_encryption.convert_string(obj.SpeedParameterName(), password),
        'SpeedParamter': table_encryption.convert_float(obj.SpeedParamter(), password),
        'StateSpeed': table_encryption.convert_float(obj.StateSpeed(), password),
        'ClipName': table_encryption.convert_string(obj.ClipName(), password),
        'Length': table_encryption.convert_float(obj.Length(), password),
        'FrameRate': table_encryption.convert_float(obj.FrameRate(), password),
        'IsLooping': obj.IsLooping(),
        'Events': [dump_AniEventData(obj.Events(j), password) for j in range(obj.EventsLength())],
    }


def dump_AniEventData(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_string(obj.Name(), password),
        'Time': table_encryption.convert_float(obj.Time(), password),
        'IntParam': table_encryption.convert_int(obj.IntParam(), password),
        'FloatParam': table_encryption.convert_float(obj.FloatParam(), password),
        'StringParam': table_encryption.convert_string(obj.StringParam(), password),
    }


def dump_ArenaLevelSectionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ArenaSeasonId': table_encryption.convert_long(obj.ArenaSeasonId(), password),
        'StartLevel': table_encryption.convert_long(obj.StartLevel(), password),
        'LastLevel': table_encryption.convert_long(obj.LastLevel(), password),
        'UserCount': table_encryption.convert_long(obj.UserCount(), password),
    }


def dump_ArenaMapExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'TerrainType': table_encryption.convert_long(obj.TerrainType(), password),
        'TerrainTypeLocalizeKey': table_encryption.convert_string(obj.TerrainTypeLocalizeKey(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'GroundGroupId': table_encryption.convert_long(obj.GroundGroupId(), password),
        'GroundGroupNameLocalizeKey': table_encryption.convert_string(obj.GroundGroupNameLocalizeKey(), password),
        'StartRank': table_encryption.convert_long(obj.StartRank(), password),
        'EndRank': table_encryption.convert_long(obj.EndRank(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
    }


def dump_ArenaNPCExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'Rank': table_encryption.convert_long(obj.Rank(), password),
        'NPCAccountLevel': table_encryption.convert_long(obj.NPCAccountLevel(), password),
        'NPCLevel': table_encryption.convert_long(obj.NPCLevel(), password),
        'NPCLevelDeviation': table_encryption.convert_long(obj.NPCLevelDeviation(), password),
        'NPCStarGrade': table_encryption.convert_long(obj.NPCStarGrade(), password),
        'ExceptionCharacterRarities': [Rarity(table_encryption.convert_int(obj.ExceptionCharacterRarities(j), password)).name for j in range(obj.ExceptionCharacterRaritiesLength())],
        'ExceptionMainCharacterIds': [table_encryption.convert_long(obj.ExceptionMainCharacterIds(j), password) for j in range(obj.ExceptionMainCharacterIdsLength())],
        'ExceptionSupportCharacterIds': [table_encryption.convert_long(obj.ExceptionSupportCharacterIds(j), password) for j in range(obj.ExceptionSupportCharacterIdsLength())],
        'ExceptionTSSIds': [table_encryption.convert_long(obj.ExceptionTSSIds(j), password) for j in range(obj.ExceptionTSSIdsLength())],
    }


def dump_ArenaRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ArenaRewardType': ArenaRewardType(table_encryption.convert_int(obj.ArenaRewardType_(), password)).name,
        'RankStart': table_encryption.convert_long(obj.RankStart(), password),
        'RankEnd': table_encryption.convert_long(obj.RankEnd(), password),
        'RankIconPath': table_encryption.convert_string(obj.RankIconPath(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelUniqueId': [table_encryption.convert_long(obj.RewardParcelUniqueId(j), password) for j in range(obj.RewardParcelUniqueIdLength())],
        'RewardParcelUniqueName': [table_encryption.convert_string(obj.RewardParcelUniqueName(j), password) for j in range(obj.RewardParcelUniqueNameLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_ArenaSeasonCloseRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'RankStart': table_encryption.convert_long(obj.RankStart(), password),
        'RankEnd': table_encryption.convert_long(obj.RankEnd(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelUniqueId': [table_encryption.convert_long(obj.RewardParcelUniqueId(j), password) for j in range(obj.RewardParcelUniqueIdLength())],
        'RewardParcelUniqueName': [table_encryption.convert_string(obj.RewardParcelUniqueName(j), password) for j in range(obj.RewardParcelUniqueNameLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_ArenaSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'SeasonStartDate': table_encryption.convert_string(obj.SeasonStartDate(), password),
        'SeasonEndDate': table_encryption.convert_string(obj.SeasonEndDate(), password),
        'SeasonGroupLimit': table_encryption.convert_long(obj.SeasonGroupLimit(), password),
        'PrevSeasonId': table_encryption.convert_long(obj.PrevSeasonId(), password),
    }


def dump_AssistEchelonTypeConvertExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Contents': EchelonType(table_encryption.convert_int(obj.Contents(), password)).name,
        'ConvertTo': EchelonType(table_encryption.convert_int(obj.ConvertTo(), password)).name,
    }


def dump_AttendanceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Type': AttendanceType(table_encryption.convert_int(obj.Type(), password)).name,
        'CountdownPrefab': table_encryption.convert_string(obj.CountdownPrefab(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevelLimit': table_encryption.convert_long(obj.AccountLevelLimit(), password),
        'Title': table_encryption.convert_string(obj.Title(), password),
        'InfomationLocalizeCode': table_encryption.convert_string(obj.InfomationLocalizeCode(), password),
        'CountRule': AttendanceCountRule(table_encryption.convert_int(obj.CountRule(), password)).name,
        'CountReset': AttendanceResetType(table_encryption.convert_int(obj.CountReset(), password)).name,
        'BookSize': table_encryption.convert_long(obj.BookSize(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'StartableEndDate': table_encryption.convert_string(obj.StartableEndDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'ExpiryDate': table_encryption.convert_long(obj.ExpiryDate(), password),
        'MailType': MailType(table_encryption.convert_int(obj.MailType_(), password)).name,
        'DialogCategory': DialogCategory(table_encryption.convert_int(obj.DialogCategory_(), password)).name,
        'TitleImagePath': table_encryption.convert_string(obj.TitleImagePath(), password),
        'DecorationImagePath': table_encryption.convert_string(obj.DecorationImagePath(), password),
    }


def dump_AttendanceRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'AttendanceId': table_encryption.convert_long(obj.AttendanceId(), password),
        'Day': table_encryption.convert_long(obj.Day(), password),
        'RewardIcon': table_encryption.convert_string(obj.RewardIcon(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardId': [table_encryption.convert_long(obj.RewardId(j), password) for j in range(obj.RewardIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_BattleLevelFactorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LevelDiff': table_encryption.convert_int(obj.LevelDiff(), password),
        'DamageRate': table_encryption.convert_long(obj.DamageRate(), password),
    }


def dump_BossExternalBTExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ExternalBTId': table_encryption.convert_long(obj.ExternalBTId(), password),
        'AIPhase': table_encryption.convert_long(obj.AIPhase(), password),
        'ExternalBTNodeType': ExternalBTNodeType(table_encryption.convert_int(obj.ExternalBTNodeType_(), password)).name,
        'ExternalBTTrigger': ExternalBTTrigger(table_encryption.convert_int(obj.ExternalBTTrigger_(), password)).name,
        'TriggerArgument': table_encryption.convert_string(obj.TriggerArgument(), password),
        'BehaviorRate': table_encryption.convert_long(obj.BehaviorRate(), password),
        'ExternalBehavior': ExternalBehavior(table_encryption.convert_int(obj.ExternalBehavior_(), password)).name,
        'BehaviorArgument': table_encryption.convert_string(obj.BehaviorArgument(), password),
    }


def dump_BossPhaseExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'AIPhase': table_encryption.convert_long(obj.AIPhase(), password),
        'NormalAttackSkillUniqueName': table_encryption.convert_string(obj.NormalAttackSkillUniqueName(), password),
        'UseExSkill': [obj.UseExSkill(j) for j in range(obj.UseExSkillLength())],
    }


def dump_BuffParticleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'UniqueName': table_encryption.convert_string(obj.UniqueName(), password),
        'BuffType': table_encryption.convert_string(obj.BuffType(), password),
        'BuffName': table_encryption.convert_string(obj.BuffName(), password),
        'ResourcePath': table_encryption.convert_string(obj.ResourcePath(), password),
    }


def dump_BulletArmorDamageFactorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'DamageFactorGroupId': table_encryption.convert_string(obj.DamageFactorGroupId(), password),
        'BulletType': BulletType(table_encryption.convert_int(obj.BulletType_(), password)).name,
        'ArmorType': ArmorType(table_encryption.convert_int(obj.ArmorType_(), password)).name,
        'DamageRate': table_encryption.convert_long(obj.DamageRate(), password),
        'DamageAttribute': DamageAttribute(table_encryption.convert_int(obj.DamageAttribute_(), password)).name,
        'MinDamageRate': table_encryption.convert_long(obj.MinDamageRate(), password),
        'MaxDamageRate': table_encryption.convert_long(obj.MaxDamageRate(), password),
        'ShowHighlightFloater': obj.ShowHighlightFloater(),
    }


def dump_CafeInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CafeId': table_encryption.convert_long(obj.CafeId(), password),
        'IsDefault': obj.IsDefault(),
        'OpenConditionCafeId': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionCafeId(), password)).name,
        'OpenConditionCafeInvite': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionCafeInvite(), password)).name,
    }


def dump_CafeInteractionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'IgnoreIfUnobtained': obj.IgnoreIfUnobtained(),
        'IgnoreIfUnobtainedStartDate': table_encryption.convert_string(obj.IgnoreIfUnobtainedStartDate(), password),
        'IgnoreIfUnobtainedEndDate': table_encryption.convert_string(obj.IgnoreIfUnobtainedEndDate(), password),
        'BubbleType': [BubbleType(table_encryption.convert_int(obj.BubbleType_(j), password)).name for j in range(obj.BubbleTypeLength())],
        'BubbleDuration': [table_encryption.convert_long(obj.BubbleDuration(j), password) for j in range(obj.BubbleDurationLength())],
        'FavorEmoticonRewardParcelType': ParcelType(table_encryption.convert_int(obj.FavorEmoticonRewardParcelType(), password)).name,
        'FavorEmoticonRewardId': table_encryption.convert_long(obj.FavorEmoticonRewardId(), password),
        'FavorEmoticonRewardAmount': table_encryption.convert_long(obj.FavorEmoticonRewardAmount(), password),
        'CafeCharacterState': [table_encryption.convert_string(obj.CafeCharacterState(j), password) for j in range(obj.CafeCharacterStateLength())],
    }


def dump_CafeProductionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CafeId': table_encryption.convert_long(obj.CafeId(), password),
        'Rank': table_encryption.convert_long(obj.Rank(), password),
        'CafeProductionParcelType': ParcelType(table_encryption.convert_int(obj.CafeProductionParcelType(), password)).name,
        'CafeProductionParcelId': table_encryption.convert_long(obj.CafeProductionParcelId(), password),
        'ParcelProductionCoefficient': table_encryption.convert_long(obj.ParcelProductionCoefficient(), password),
        'ParcelProductionCorrectionValue': table_encryption.convert_long(obj.ParcelProductionCorrectionValue(), password),
        'ParcelStorageMax': table_encryption.convert_long(obj.ParcelStorageMax(), password),
    }


def dump_CafeRankExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CafeId': table_encryption.convert_long(obj.CafeId(), password),
        'Rank': table_encryption.convert_long(obj.Rank(), password),
        'RecipeId': table_encryption.convert_long(obj.RecipeId(), password),
        'ComfortMax': table_encryption.convert_long(obj.ComfortMax(), password),
        'TagCountMax': table_encryption.convert_long(obj.TagCountMax(), password),
        'CharacterVisitMin': table_encryption.convert_int(obj.CharacterVisitMin(), password),
        'CharacterVisitMax': table_encryption.convert_int(obj.CharacterVisitMax(), password),
        'CafeVisitWeightBase': table_encryption.convert_int(obj.CafeVisitWeightBase(), password),
        'CafeVisitWeightTagBonusStep': [table_encryption.convert_int(obj.CafeVisitWeightTagBonusStep(j), password) for j in range(obj.CafeVisitWeightTagBonusStepLength())],
        'CafeVisitWeightTagBonus': [table_encryption.convert_int(obj.CafeVisitWeightTagBonus(j), password) for j in range(obj.CafeVisitWeightTagBonusLength())],
    }


def dump_CampaignChapterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'NormalImagePath': table_encryption.convert_string(obj.NormalImagePath(), password),
        'HardImagePath': table_encryption.convert_string(obj.HardImagePath(), password),
        'Order': table_encryption.convert_long(obj.Order(), password),
        'PreChapterId': [table_encryption.convert_long(obj.PreChapterId(j), password) for j in range(obj.PreChapterIdLength())],
        'ChapterRewardId': table_encryption.convert_long(obj.ChapterRewardId(), password),
        'ChapterHardRewardId': table_encryption.convert_long(obj.ChapterHardRewardId(), password),
        'ChapterVeryHardRewardId': table_encryption.convert_long(obj.ChapterVeryHardRewardId(), password),
        'NormalCampaignStageId': [table_encryption.convert_long(obj.NormalCampaignStageId(j), password) for j in range(obj.NormalCampaignStageIdLength())],
        'NormalExtraStageId': [table_encryption.convert_long(obj.NormalExtraStageId(j), password) for j in range(obj.NormalExtraStageIdLength())],
        'HardCampaignStageId': [table_encryption.convert_long(obj.HardCampaignStageId(j), password) for j in range(obj.HardCampaignStageIdLength())],
        'VeryHardCampaignStageId': [table_encryption.convert_long(obj.VeryHardCampaignStageId(j), password) for j in range(obj.VeryHardCampaignStageIdLength())],
        'IsTacticSkip': obj.IsTacticSkip(),
    }


def dump_CampaignChapterRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CampaignChapterStar': table_encryption.convert_long(obj.CampaignChapterStar(), password),
        'ChapterRewardParcelType': [ParcelType(table_encryption.convert_int(obj.ChapterRewardParcelType(j), password)).name for j in range(obj.ChapterRewardParcelTypeLength())],
        'ChapterRewardId': [table_encryption.convert_long(obj.ChapterRewardId(j), password) for j in range(obj.ChapterRewardIdLength())],
        'ChapterRewardAmount': [table_encryption.convert_int(obj.ChapterRewardAmount(j), password) for j in range(obj.ChapterRewardAmountLength())],
    }


def dump_CampaignStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Deprecated': obj.Deprecated(),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'StageNumber': table_encryption.convert_string(obj.StageNumber(), password),
        'CleardScenarioId': table_encryption.convert_long(obj.CleardScenarioId(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'StageEnterEchelonCount': table_encryption.convert_int(obj.StageEnterEchelonCount(), password),
        'StarConditionTacticRankSCount': table_encryption.convert_long(obj.StarConditionTacticRankSCount(), password),
        'StarConditionTurnCount': table_encryption.convert_long(obj.StarConditionTurnCount(), password),
        'EnterScenarioGroupId': [table_encryption.convert_long(obj.EnterScenarioGroupId(j), password) for j in range(obj.EnterScenarioGroupIdLength())],
        'ClearScenarioGroupId': [table_encryption.convert_long(obj.ClearScenarioGroupId(j), password) for j in range(obj.ClearScenarioGroupIdLength())],
        'StrategyMap': table_encryption.convert_string(obj.StrategyMap(), password),
        'StrategyMapBG': table_encryption.convert_string(obj.StrategyMapBG(), password),
        'CampaignStageRewardId': table_encryption.convert_long(obj.CampaignStageRewardId(), password),
        'MaxTurn': table_encryption.convert_int(obj.MaxTurn(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'BgmId': table_encryption.convert_string(obj.BgmId(), password),
        'StrategyEnvironment': StrategyEnvironment(table_encryption.convert_int(obj.StrategyEnvironment_(), password)).name,
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'StrategySkipGroundId': table_encryption.convert_int(obj.StrategySkipGroundId(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'FirstClearReportEventName': table_encryption.convert_string(obj.FirstClearReportEventName(), password),
        'TacticRewardExp': table_encryption.convert_long(obj.TacticRewardExp(), password),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_CampaignStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'StageRewardProb': table_encryption.convert_int(obj.StageRewardProb(), password),
        'StageRewardParcelType': ParcelType(table_encryption.convert_int(obj.StageRewardParcelType(), password)).name,
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'StageRewardAmount': table_encryption.convert_int(obj.StageRewardAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_CampaignStrategyObjectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'StrategyObjectType': StrategyObjectType(table_encryption.convert_int(obj.StrategyObjectType_(), password)).name,
        'StrategyRewardParcelType': ParcelType(table_encryption.convert_int(obj.StrategyRewardParcelType(), password)).name,
        'StrategyRewardID': table_encryption.convert_long(obj.StrategyRewardID(), password),
        'StrategyRewardName': table_encryption.convert_string(obj.StrategyRewardName(), password),
        'StrategyRewardAmount': table_encryption.convert_int(obj.StrategyRewardAmount(), password),
        'StrategySightRange': table_encryption.convert_long(obj.StrategySightRange(), password),
        'PortalId': table_encryption.convert_int(obj.PortalId(), password),
        'HealValue': table_encryption.convert_int(obj.HealValue(), password),
        'SwithId': table_encryption.convert_int(obj.SwithId(), password),
        'BuffId': table_encryption.convert_int(obj.BuffId(), password),
        'Disposable': obj.Disposable(),
    }


def dump_CampaignUnitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'StrategyPrefabName': table_encryption.convert_string(obj.StrategyPrefabName(), password),
        'EnterScenarioGroupId': [table_encryption.convert_long(obj.EnterScenarioGroupId(j), password) for j in range(obj.EnterScenarioGroupIdLength())],
        'ClearScenarioGroupId': [table_encryption.convert_long(obj.ClearScenarioGroupId(j), password) for j in range(obj.ClearScenarioGroupIdLength())],
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'MoveRange': table_encryption.convert_int(obj.MoveRange(), password),
        'AIMoveType': StrategyAIType(table_encryption.convert_int(obj.AIMoveType(), password)).name,
        'Grade': HexaUnitGrade(table_encryption.convert_int(obj.Grade(), password)).name,
        'EnvironmentType': TacticEnvironment(table_encryption.convert_int(obj.EnvironmentType(), password)).name,
        'Scale': table_encryption.convert_float(obj.Scale(), password),
        'IsTacticSkip': obj.IsTacticSkip(),
    }


def dump_CharacterAcademyTagsExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'FavorTags': [Tag(table_encryption.convert_int(obj.FavorTags(j), password)).name for j in range(obj.FavorTagsLength())],
        'FavorItemTags': [Tag(table_encryption.convert_int(obj.FavorItemTags(j), password)).name for j in range(obj.FavorItemTagsLength())],
        'FavorItemUniqueTags': [Tag(table_encryption.convert_int(obj.FavorItemUniqueTags(j), password)).name for j in range(obj.FavorItemUniqueTagsLength())],
        'ForbiddenTags': [Tag(table_encryption.convert_int(obj.ForbiddenTags(j), password)).name for j in range(obj.ForbiddenTagsLength())],
        'ZoneWhiteListTags': [Tag(table_encryption.convert_int(obj.ZoneWhiteListTags(j), password)).name for j in range(obj.ZoneWhiteListTagsLength())],
    }


def dump_CharacterAIExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EngageType': EngageType(table_encryption.convert_int(obj.EngageType_(), password)).name,
        'Positioning': PositioningType(table_encryption.convert_int(obj.Positioning(), password)).name,
        'CheckCanUseAutoSkill': obj.CheckCanUseAutoSkill(),
        'DistanceReduceRatioObstaclePath': table_encryption.convert_long(obj.DistanceReduceRatioObstaclePath(), password),
        'DistanceReduceObstaclePath': table_encryption.convert_long(obj.DistanceReduceObstaclePath(), password),
        'DistanceReduceRatioFormationPath': table_encryption.convert_long(obj.DistanceReduceRatioFormationPath(), password),
        'DistanceReduceFormationPath': table_encryption.convert_long(obj.DistanceReduceFormationPath(), password),
        'MinimumPositionGap': table_encryption.convert_long(obj.MinimumPositionGap(), password),
        'CanUseObstacleOfKneelMotion': obj.CanUseObstacleOfKneelMotion(),
        'CanUseObstacleOfStandMotion': obj.CanUseObstacleOfStandMotion(),
        'HasTargetSwitchingMotion': obj.HasTargetSwitchingMotion(),
    }


def dump_CharacterCalculationLimitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TacticEntityType': TacticEntityType(table_encryption.convert_int(obj.TacticEntityType_(), password)).name,
        'CalculationValue': BattleCalculationStat(table_encryption.convert_int(obj.CalculationValue(), password)).name,
        'MinValue': table_encryption.convert_long(obj.MinValue(), password),
        'MaxValue': table_encryption.convert_long(obj.MaxValue(), password),
    }


def dump_CharacterCombatSkinExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_string(obj.GroupId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ResourcePath': table_encryption.convert_string(obj.ResourcePath(), password),
    }


def dump_CharacterDialogFieldExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'Phase': table_encryption.convert_int(obj.Phase(), password),
        'TargetIndex': table_encryption.convert_int(obj.TargetIndex(), password),
        'DialogType': FieldDialogType(table_encryption.convert_int(obj.DialogType(), password)).name,
        'Duration': table_encryption.convert_long(obj.Duration(), password),
        'MotionName': table_encryption.convert_string(obj.MotionName(), password),
        'IsInteractionDialog': obj.IsInteractionDialog(),
        'HideUI': obj.HideUI(),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
    }


def dump_CharacterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'CostumeGroupId': table_encryption.convert_long(obj.CostumeGroupId(), password),
        'IsPlayable': obj.IsPlayable(),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'CollectionVisible': obj.CollectionVisible(),
        'ReleaseDate': table_encryption.convert_string(obj.ReleaseDate(), password),
        'CollectionVisibleStartDate': table_encryption.convert_string(obj.CollectionVisibleStartDate(), password),
        'CollectionVisibleEndDate': table_encryption.convert_string(obj.CollectionVisibleEndDate(), password),
        'IsPlayableCharacter': obj.IsPlayableCharacter(),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'IsNPC': obj.IsNPC(),
        'TacticEntityType': TacticEntityType(table_encryption.convert_int(obj.TacticEntityType_(), password)).name,
        'CanSurvive': obj.CanSurvive(),
        'IsDummy': obj.IsDummy(),
        'SubPartsCount': table_encryption.convert_int(obj.SubPartsCount(), password),
        'TacticRole': TacticRole(table_encryption.convert_int(obj.TacticRole_(), password)).name,
        'WeaponType': WeaponType(table_encryption.convert_int(obj.WeaponType_(), password)).name,
        'TacticRange': TacticRange(table_encryption.convert_int(obj.TacticRange_(), password)).name,
        'BulletType': BulletType(table_encryption.convert_int(obj.BulletType_(), password)).name,
        'ArmorType': ArmorType(table_encryption.convert_int(obj.ArmorType_(), password)).name,
        'AimIKType': AimIKType(table_encryption.convert_int(obj.AimIKType_(), password)).name,
        'School': School(table_encryption.convert_int(obj.School_(), password)).name,
        'Club': Club(table_encryption.convert_int(obj.Club_(), password)).name,
        'DefaultStarGrade': table_encryption.convert_int(obj.DefaultStarGrade(), password),
        'MaxStarGrade': table_encryption.convert_int(obj.MaxStarGrade(), password),
        'StatLevelUpType': StatLevelUpType(table_encryption.convert_int(obj.StatLevelUpType_(), password)).name,
        'SquadType': SquadType(table_encryption.convert_int(obj.SquadType_(), password)).name,
        'Jumpable': obj.Jumpable(),
        'PersonalityId': table_encryption.convert_long(obj.PersonalityId(), password),
        'CharacterAIId': table_encryption.convert_long(obj.CharacterAIId(), password),
        'ExternalBTId': table_encryption.convert_long(obj.ExternalBTId(), password),
        'MainCombatStyleId': table_encryption.convert_long(obj.MainCombatStyleId(), password),
        'CombatStyleIndex': table_encryption.convert_int(obj.CombatStyleIndex(), password),
        'ScenarioCharacter': table_encryption.convert_string(obj.ScenarioCharacter(), password),
        'SpawnTemplateId': table_encryption.convert_uint(obj.SpawnTemplateId(), password),
        'FavorLevelupType': table_encryption.convert_int(obj.FavorLevelupType(), password),
        'EquipmentSlot': [EquipmentCategory(table_encryption.convert_int(obj.EquipmentSlot(j), password)).name for j in range(obj.EquipmentSlotLength())],
        'WeaponLocalizeId': table_encryption.convert_uint(obj.WeaponLocalizeId(), password),
        'DisplayEnemyInfo': obj.DisplayEnemyInfo(),
        'BodyRadius': table_encryption.convert_long(obj.BodyRadius(), password),
        'RandomEffectRadius': table_encryption.convert_long(obj.RandomEffectRadius(), password),
        'HPBarHide': obj.HPBarHide(),
        'HpBarHeight': table_encryption.convert_float(obj.HpBarHeight(), password),
        'HighlightFloaterHeight': table_encryption.convert_float(obj.HighlightFloaterHeight(), password),
        'EmojiOffsetX': table_encryption.convert_float(obj.EmojiOffsetX(), password),
        'EmojiOffsetY': table_encryption.convert_float(obj.EmojiOffsetY(), password),
        'MoveStartFrame': table_encryption.convert_int(obj.MoveStartFrame(), password),
        'MoveEndFrame': table_encryption.convert_int(obj.MoveEndFrame(), password),
        'JumpMotionFrame': table_encryption.convert_int(obj.JumpMotionFrame(), password),
        'AppearFrame': table_encryption.convert_int(obj.AppearFrame(), password),
        'CanMove': obj.CanMove(),
        'CanFix': obj.CanFix(),
        'CanCrowdControl': obj.CanCrowdControl(),
        'CanBattleItemMove': obj.CanBattleItemMove(),
        'IsAirUnit': obj.IsAirUnit(),
        'AirUnitHeight': table_encryption.convert_long(obj.AirUnitHeight(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
        'SecretStoneItemId': table_encryption.convert_long(obj.SecretStoneItemId(), password),
        'SecretStoneItemAmount': table_encryption.convert_int(obj.SecretStoneItemAmount(), password),
        'CharacterPieceItemId': table_encryption.convert_long(obj.CharacterPieceItemId(), password),
        'CharacterPieceItemAmount': table_encryption.convert_int(obj.CharacterPieceItemAmount(), password),
        'CombineRecipeId': table_encryption.convert_long(obj.CombineRecipeId(), password),
    }


def dump_CharacterGearExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'StatLevelUpType': StatLevelUpType(table_encryption.convert_int(obj.StatLevelUpType_(), password)).name,
        'Tier': table_encryption.convert_long(obj.Tier(), password),
        'NextTierEquipment': table_encryption.convert_long(obj.NextTierEquipment(), password),
        'RecipeId': table_encryption.convert_long(obj.RecipeId(), password),
        'OpenFavorLevel': table_encryption.convert_long(obj.OpenFavorLevel(), password),
        'MaxLevel': table_encryption.convert_long(obj.MaxLevel(), password),
        'LearnSkillSlot': table_encryption.convert_string(obj.LearnSkillSlot(), password),
        'StatType': [EquipmentOptionType(table_encryption.convert_int(obj.StatType(j), password)).name for j in range(obj.StatTypeLength())],
        'MinStatValue': [table_encryption.convert_long(obj.MinStatValue(j), password) for j in range(obj.MinStatValueLength())],
        'MaxStatValue': [table_encryption.convert_long(obj.MaxStatValue(j), password) for j in range(obj.MaxStatValueLength())],
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
    }


def dump_CharacterGearLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_int(obj.Level(), password),
        'TierLevelExp': [table_encryption.convert_long(obj.TierLevelExp(j), password) for j in range(obj.TierLevelExpLength())],
        'TotalExp': [table_encryption.convert_long(obj.TotalExp(j), password) for j in range(obj.TotalExpLength())],
    }


def dump_CharacterIllustCoordinateExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CharacterBodyCenterX': table_encryption.convert_float(obj.CharacterBodyCenterX(), password),
        'CharacterBodyCenterY': table_encryption.convert_float(obj.CharacterBodyCenterY(), password),
        'DefaultScale': table_encryption.convert_float(obj.DefaultScale(), password),
        'MinScale': table_encryption.convert_float(obj.MinScale(), password),
        'MaxScale': table_encryption.convert_float(obj.MaxScale(), password),
    }


def dump_CharacterLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Exp': table_encryption.convert_long(obj.Exp(), password),
        'TotalExp': table_encryption.convert_long(obj.TotalExp(), password),
    }


def dump_CharacterLevelStatFactorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_long(obj.Level(), password),
        'CriticalFactor': table_encryption.convert_long(obj.CriticalFactor(), password),
        'StabilityFactor': table_encryption.convert_long(obj.StabilityFactor(), password),
        'DefenceFactor': table_encryption.convert_long(obj.DefenceFactor(), password),
        'AccuracyFactor': table_encryption.convert_long(obj.AccuracyFactor(), password),
    }


def dump_CharacterSkillListExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterSkillListGroupId': table_encryption.convert_long(obj.CharacterSkillListGroupId(), password),
        'MinimumGradeCharacterWeapon': table_encryption.convert_int(obj.MinimumGradeCharacterWeapon(), password),
        'MinimumTierCharacterGear': table_encryption.convert_int(obj.MinimumTierCharacterGear(), password),
        'FormIndex': table_encryption.convert_int(obj.FormIndex(), password),
        'IsRootMotion': obj.IsRootMotion(),
        'IsMoveLeftRight': obj.IsMoveLeftRight(),
        'UseRandomExSkillTimeline': obj.UseRandomExSkillTimeline(),
        'TSAInteractionId': table_encryption.convert_long(obj.TSAInteractionId(), password),
        'NormalSkillGroupId': [table_encryption.convert_string(obj.NormalSkillGroupId(j), password) for j in range(obj.NormalSkillGroupIdLength())],
        'NormalSkillTimeLineIndex': [table_encryption.convert_int(obj.NormalSkillTimeLineIndex(j), password) for j in range(obj.NormalSkillTimeLineIndexLength())],
        'ExSkillGroupId': [table_encryption.convert_string(obj.ExSkillGroupId(j), password) for j in range(obj.ExSkillGroupIdLength())],
        'ExSkillCutInTimeLineIndex': [table_encryption.convert_string(obj.ExSkillCutInTimeLineIndex(j), password) for j in range(obj.ExSkillCutInTimeLineIndexLength())],
        'ExSkillLevelTimeLineIndex': [table_encryption.convert_string(obj.ExSkillLevelTimeLineIndex(j), password) for j in range(obj.ExSkillLevelTimeLineIndexLength())],
        'PublicSkillGroupId': [table_encryption.convert_string(obj.PublicSkillGroupId(j), password) for j in range(obj.PublicSkillGroupIdLength())],
        'PublicSkillTimeLineIndex': [table_encryption.convert_int(obj.PublicSkillTimeLineIndex(j), password) for j in range(obj.PublicSkillTimeLineIndexLength())],
        'PassiveSkillGroupId': [table_encryption.convert_string(obj.PassiveSkillGroupId(j), password) for j in range(obj.PassiveSkillGroupIdLength())],
        'LeaderSkillGroupId': [table_encryption.convert_string(obj.LeaderSkillGroupId(j), password) for j in range(obj.LeaderSkillGroupIdLength())],
        'ExtraPassiveSkillGroupId': [table_encryption.convert_string(obj.ExtraPassiveSkillGroupId(j), password) for j in range(obj.ExtraPassiveSkillGroupIdLength())],
        'HiddenPassiveSkillGroupId': [table_encryption.convert_string(obj.HiddenPassiveSkillGroupId(j), password) for j in range(obj.HiddenPassiveSkillGroupIdLength())],
    }


def dump_CharacterStatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'StabilityRate': table_encryption.convert_long(obj.StabilityRate(), password),
        'StabilityPoint': table_encryption.convert_long(obj.StabilityPoint(), password),
        'AttackPower1': table_encryption.convert_long(obj.AttackPower1(), password),
        'AttackPower100': table_encryption.convert_long(obj.AttackPower100(), password),
        'MaxHP1': table_encryption.convert_long(obj.MaxHP1(), password),
        'MaxHP100': table_encryption.convert_long(obj.MaxHP100(), password),
        'DefensePower1': table_encryption.convert_long(obj.DefensePower1(), password),
        'DefensePower100': table_encryption.convert_long(obj.DefensePower100(), password),
        'HealPower1': table_encryption.convert_long(obj.HealPower1(), password),
        'HealPower100': table_encryption.convert_long(obj.HealPower100(), password),
        'DodgePoint': table_encryption.convert_long(obj.DodgePoint(), password),
        'AccuracyPoint': table_encryption.convert_long(obj.AccuracyPoint(), password),
        'CriticalPoint': table_encryption.convert_long(obj.CriticalPoint(), password),
        'CriticalResistPoint': table_encryption.convert_long(obj.CriticalResistPoint(), password),
        'CriticalDamageRate': table_encryption.convert_long(obj.CriticalDamageRate(), password),
        'CriticalDamageResistRate': table_encryption.convert_long(obj.CriticalDamageResistRate(), password),
        'BlockRate': table_encryption.convert_long(obj.BlockRate(), password),
        'HealEffectivenessRate': table_encryption.convert_long(obj.HealEffectivenessRate(), password),
        'OppressionPower': table_encryption.convert_long(obj.OppressionPower(), password),
        'OppressionResist': table_encryption.convert_long(obj.OppressionResist(), password),
        'DefensePenetration1': table_encryption.convert_long(obj.DefensePenetration1(), password),
        'DefensePenetration100': table_encryption.convert_long(obj.DefensePenetration100(), password),
        'DefensePenetrationResist1': table_encryption.convert_long(obj.DefensePenetrationResist1(), password),
        'DefensePenetrationResist100': table_encryption.convert_long(obj.DefensePenetrationResist100(), password),
        'EnhanceExplosionRate': table_encryption.convert_long(obj.EnhanceExplosionRate(), password),
        'EnhancePierceRate': table_encryption.convert_long(obj.EnhancePierceRate(), password),
        'EnhanceMysticRate': table_encryption.convert_long(obj.EnhanceMysticRate(), password),
        'EnhanceSonicRate': table_encryption.convert_long(obj.EnhanceSonicRate(), password),
        'EnhanceSiegeRate': table_encryption.convert_long(obj.EnhanceSiegeRate(), password),
        'EnhanceNormalRate': table_encryption.convert_long(obj.EnhanceNormalRate(), password),
        'EnhanceLightArmorRate': table_encryption.convert_long(obj.EnhanceLightArmorRate(), password),
        'EnhanceHeavyArmorRate': table_encryption.convert_long(obj.EnhanceHeavyArmorRate(), password),
        'EnhanceUnarmedRate': table_encryption.convert_long(obj.EnhanceUnarmedRate(), password),
        'EnhanceElasticArmorRate': table_encryption.convert_long(obj.EnhanceElasticArmorRate(), password),
        'EnhanceStructureRate': table_encryption.convert_long(obj.EnhanceStructureRate(), password),
        'EnhanceNormalArmorRate': table_encryption.convert_long(obj.EnhanceNormalArmorRate(), password),
        'ExtendBuffDuration': table_encryption.convert_long(obj.ExtendBuffDuration(), password),
        'ExtendDebuffDuration': table_encryption.convert_long(obj.ExtendDebuffDuration(), password),
        'ExtendCrowdControlDuration': table_encryption.convert_long(obj.ExtendCrowdControlDuration(), password),
        'AmmoCount': table_encryption.convert_long(obj.AmmoCount(), password),
        'AmmoCost': table_encryption.convert_long(obj.AmmoCost(), password),
        'IgnoreDelayCount': table_encryption.convert_long(obj.IgnoreDelayCount(), password),
        'NormalAttackSpeed': table_encryption.convert_long(obj.NormalAttackSpeed(), password),
        'Range': table_encryption.convert_long(obj.Range(), password),
        'InitialRangeRate': table_encryption.convert_long(obj.InitialRangeRate(), password),
        'MoveSpeed': table_encryption.convert_long(obj.MoveSpeed(), password),
        'SightPoint': table_encryption.convert_long(obj.SightPoint(), password),
        'ActiveGauge': table_encryption.convert_long(obj.ActiveGauge(), password),
        'GroggyGauge': table_encryption.convert_int(obj.GroggyGauge(), password),
        'GroggyTime': table_encryption.convert_int(obj.GroggyTime(), password),
        'StrategyMobility': table_encryption.convert_long(obj.StrategyMobility(), password),
        'ActionCount': table_encryption.convert_long(obj.ActionCount(), password),
        'StrategySightRange': table_encryption.convert_long(obj.StrategySightRange(), password),
        'DamageRatio': table_encryption.convert_long(obj.DamageRatio(), password),
        'DamagedRatio': table_encryption.convert_long(obj.DamagedRatio(), password),
        'DamageRatio2Increase': table_encryption.convert_long(obj.DamageRatio2Increase(), password),
        'DamageRatio2Decrease': table_encryption.convert_long(obj.DamageRatio2Decrease(), password),
        'DamagedRatio2Increase': table_encryption.convert_long(obj.DamagedRatio2Increase(), password),
        'DamagedRatio2Decrease': table_encryption.convert_long(obj.DamagedRatio2Decrease(), password),
        'ExDamagedRatioIncrease': table_encryption.convert_long(obj.ExDamagedRatioIncrease(), password),
        'ExDamagedRatioDecrease': table_encryption.convert_long(obj.ExDamagedRatioDecrease(), password),
        'StreetBattleAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.StreetBattleAdaptation(), password)).name,
        'OutdoorBattleAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.OutdoorBattleAdaptation(), password)).name,
        'IndoorBattleAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.IndoorBattleAdaptation(), password)).name,
        'RegenCost': table_encryption.convert_long(obj.RegenCost(), password),
    }


def dump_CharacterStatLimitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TacticEntityType': TacticEntityType(table_encryption.convert_int(obj.TacticEntityType_(), password)).name,
        'StatType': StatType(table_encryption.convert_int(obj.StatType_(), password)).name,
        'StatMinValue': table_encryption.convert_long(obj.StatMinValue(), password),
        'StatMaxValue': table_encryption.convert_long(obj.StatMaxValue(), password),
        'StatRatioMinValue': table_encryption.convert_long(obj.StatRatioMinValue(), password),
        'StatRatioMaxValue': table_encryption.convert_long(obj.StatRatioMaxValue(), password),
    }


def dump_CharacterStatsDetailExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DetailShowStats': [StatType(table_encryption.convert_int(obj.DetailShowStats(j), password)).name for j in range(obj.DetailShowStatsLength())],
        'IsStatsPercent': [obj.IsStatsPercent(j) for j in range(obj.IsStatsPercentLength())],
    }


def dump_CharacterStatsTransExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TransSupportStats': StatType(table_encryption.convert_int(obj.TransSupportStats(), password)).name,
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
        'TransSupportStatsFactor': table_encryption.convert_int(obj.TransSupportStatsFactor(), password),
        'StatTransType': StatTransType(table_encryption.convert_int(obj.StatTransType_(), password)).name,
    }


def dump_CharacterTranscendenceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MaxFavorLevel': [table_encryption.convert_int(obj.MaxFavorLevel(j), password) for j in range(obj.MaxFavorLevelLength())],
        'StatBonusRateAttack': [table_encryption.convert_long(obj.StatBonusRateAttack(j), password) for j in range(obj.StatBonusRateAttackLength())],
        'StatBonusRateHP': [table_encryption.convert_long(obj.StatBonusRateHP(j), password) for j in range(obj.StatBonusRateHPLength())],
        'StatBonusRateHeal': [table_encryption.convert_long(obj.StatBonusRateHeal(j), password) for j in range(obj.StatBonusRateHealLength())],
        'RecipeId': [table_encryption.convert_long(obj.RecipeId(j), password) for j in range(obj.RecipeIdLength())],
        'SkillSlotA': [table_encryption.convert_string(obj.SkillSlotA(j), password) for j in range(obj.SkillSlotALength())],
        'SkillSlotB': [table_encryption.convert_string(obj.SkillSlotB(j), password) for j in range(obj.SkillSlotBLength())],
        'SkillSlotC': [table_encryption.convert_string(obj.SkillSlotC(j), password) for j in range(obj.SkillSlotCLength())],
        'MaxlevelStar': [table_encryption.convert_int(obj.MaxlevelStar(j), password) for j in range(obj.MaxlevelStarLength())],
    }


def dump_CharacterVictoryInteractionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'InteractionId': table_encryption.convert_long(obj.InteractionId(), password),
        'CostumeId01': table_encryption.convert_long(obj.CostumeId01(), password),
        'PositionIndex01': table_encryption.convert_int(obj.PositionIndex01(), password),
        'VictoryStartAnimationPath01': table_encryption.convert_string(obj.VictoryStartAnimationPath01(), password),
        'VictoryEndAnimationPath01': table_encryption.convert_string(obj.VictoryEndAnimationPath01(), password),
        'CostumeId02': table_encryption.convert_long(obj.CostumeId02(), password),
        'PositionIndex02': table_encryption.convert_int(obj.PositionIndex02(), password),
        'VictoryStartAnimationPath02': table_encryption.convert_string(obj.VictoryStartAnimationPath02(), password),
        'VictoryEndAnimationPath02': table_encryption.convert_string(obj.VictoryEndAnimationPath02(), password),
        'CostumeId03': table_encryption.convert_long(obj.CostumeId03(), password),
        'PositionIndex03': table_encryption.convert_int(obj.PositionIndex03(), password),
        'VictoryStartAnimationPath03': table_encryption.convert_string(obj.VictoryStartAnimationPath03(), password),
        'VictoryEndAnimationPath03': table_encryption.convert_string(obj.VictoryEndAnimationPath03(), password),
        'CostumeId04': table_encryption.convert_long(obj.CostumeId04(), password),
        'PositionIndex04': table_encryption.convert_int(obj.PositionIndex04(), password),
        'VictoryStartAnimationPath04': table_encryption.convert_string(obj.VictoryStartAnimationPath04(), password),
        'VictoryEndAnimationPath04': table_encryption.convert_string(obj.VictoryEndAnimationPath04(), password),
        'CostumeId05': table_encryption.convert_long(obj.CostumeId05(), password),
        'PositionIndex05': table_encryption.convert_int(obj.PositionIndex05(), password),
        'VictoryStartAnimationPath05': table_encryption.convert_string(obj.VictoryStartAnimationPath05(), password),
        'VictoryEndAnimationPath05': table_encryption.convert_string(obj.VictoryEndAnimationPath05(), password),
        'CostumeId06': table_encryption.convert_long(obj.CostumeId06(), password),
        'PositionIndex06': table_encryption.convert_int(obj.PositionIndex06(), password),
        'VictoryStartAnimationPath06': table_encryption.convert_string(obj.VictoryStartAnimationPath06(), password),
        'VictoryEndAnimationPath06': table_encryption.convert_string(obj.VictoryEndAnimationPath06(), password),
    }


def dump_CharacterWeaponExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'SetRecipe': table_encryption.convert_long(obj.SetRecipe(), password),
        'StatLevelUpType': StatLevelUpType(table_encryption.convert_int(obj.StatLevelUpType_(), password)).name,
        'AttackPower': table_encryption.convert_long(obj.AttackPower(), password),
        'AttackPower100': table_encryption.convert_long(obj.AttackPower100(), password),
        'MaxHP': table_encryption.convert_long(obj.MaxHP(), password),
        'MaxHP100': table_encryption.convert_long(obj.MaxHP100(), password),
        'HealPower': table_encryption.convert_long(obj.HealPower(), password),
        'HealPower100': table_encryption.convert_long(obj.HealPower100(), password),
        'Unlock': [obj.Unlock(j) for j in range(obj.UnlockLength())],
        'RecipeId': [table_encryption.convert_long(obj.RecipeId(j), password) for j in range(obj.RecipeIdLength())],
        'MaxLevel': [table_encryption.convert_int(obj.MaxLevel(j), password) for j in range(obj.MaxLevelLength())],
        'LearnSkillSlot': [table_encryption.convert_string(obj.LearnSkillSlot(j), password) for j in range(obj.LearnSkillSlotLength())],
        'StatType': [EquipmentOptionType(table_encryption.convert_int(obj.StatType(j), password)).name for j in range(obj.StatTypeLength())],
        'StatValue': [table_encryption.convert_long(obj.StatValue(j), password) for j in range(obj.StatValueLength())],
    }


def dump_CharacterWeaponExpBonusExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'WeaponType': WeaponType(table_encryption.convert_int(obj.WeaponType_(), password)).name,
        'WeaponExpGrowthA': table_encryption.convert_int(obj.WeaponExpGrowthA(), password),
        'WeaponExpGrowthB': table_encryption.convert_int(obj.WeaponExpGrowthB(), password),
        'WeaponExpGrowthC': table_encryption.convert_int(obj.WeaponExpGrowthC(), password),
        'WeaponExpGrowthZ': table_encryption.convert_int(obj.WeaponExpGrowthZ(), password),
    }


def dump_CharacterWeaponLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Exp': table_encryption.convert_long(obj.Exp(), password),
        'TotalExp': table_encryption.convert_long(obj.TotalExp(), password),
    }


def dump_ClanAssistSlotExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SlotId': table_encryption.convert_long(obj.SlotId(), password),
        'EchelonType': EchelonType(table_encryption.convert_int(obj.EchelonType_(), password)).name,
        'SlotNumber': table_encryption.convert_long(obj.SlotNumber(), password),
        'AssistTermRewardPeriodFromSec': table_encryption.convert_long(obj.AssistTermRewardPeriodFromSec(), password),
        'AssistRewardLimit': table_encryption.convert_long(obj.AssistRewardLimit(), password),
        'AssistRentRewardDailyMaxCount': table_encryption.convert_long(obj.AssistRentRewardDailyMaxCount(), password),
        'AssistRentalFeeAmount': table_encryption.convert_long(obj.AssistRentalFeeAmount(), password),
        'AssistRentalFeeAmountStranger': table_encryption.convert_long(obj.AssistRentalFeeAmountStranger(), password),
    }


def dump_ClanRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ClanRewardType': ClanRewardType(table_encryption.convert_int(obj.ClanRewardType_(), password)).name,
        'EchelonType': EchelonType(table_encryption.convert_int(obj.EchelonType_(), password)).name,
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
    }


def dump_ClearDeckRuleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'SizeLimit': table_encryption.convert_long(obj.SizeLimit(), password),
    }


def dump_ConquestCalculateExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CalculateConditionParcelType': ParcelType(table_encryption.convert_int(obj.CalculateConditionParcelType(), password)).name,
        'CalculateConditionParcelUniqueId': table_encryption.convert_long(obj.CalculateConditionParcelUniqueId(), password),
        'CalculateConditionParcelAmount': table_encryption.convert_long(obj.CalculateConditionParcelAmount(), password),
    }


def dump_ConquestCameraSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ConquestMapBoundaryOffsetLeft': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetLeft(), password),
        'ConquestMapBoundaryOffsetRight': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetRight(), password),
        'ConquestMapBoundaryOffsetTop': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetTop(), password),
        'ConquestMapBoundaryOffsetBottom': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetBottom(), password),
        'ConquestMapCenterOffsetX': table_encryption.convert_float(obj.ConquestMapCenterOffsetX(), password),
        'ConquestMapCenterOffsetY': table_encryption.convert_float(obj.ConquestMapCenterOffsetY(), password),
        'CameraAngle': table_encryption.convert_float(obj.CameraAngle(), password),
        'CameraZoomMax': table_encryption.convert_float(obj.CameraZoomMax(), password),
        'CameraZoomMin': table_encryption.convert_float(obj.CameraZoomMin(), password),
        'CameraZoomDefault': table_encryption.convert_float(obj.CameraZoomDefault(), password),
    }


def dump_ConquestErosionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ErosionType': ConquestErosionType(table_encryption.convert_int(obj.ErosionType(), password)).name,
        'Phase': table_encryption.convert_int(obj.Phase(), password),
        'PhaseAlarm': obj.PhaseAlarm(),
        'StepIndex': table_encryption.convert_int(obj.StepIndex(), password),
        'PhaseStartConditionType': [ConquestConditionType(table_encryption.convert_int(obj.PhaseStartConditionType(j), password)).name for j in range(obj.PhaseStartConditionTypeLength())],
        'PhaseStartConditionParameter': [table_encryption.convert_string(obj.PhaseStartConditionParameter(j), password) for j in range(obj.PhaseStartConditionParameterLength())],
        'PhaseBeforeExposeConditionType': [ConquestConditionType(table_encryption.convert_int(obj.PhaseBeforeExposeConditionType(j), password)).name for j in range(obj.PhaseBeforeExposeConditionTypeLength())],
        'PhaseBeforeExposeConditionParameter': [table_encryption.convert_string(obj.PhaseBeforeExposeConditionParameter(j), password) for j in range(obj.PhaseBeforeExposeConditionParameterLength())],
        'ErosionBattleConditionParcelType': ParcelType(table_encryption.convert_int(obj.ErosionBattleConditionParcelType(), password)).name,
        'ErosionBattleConditionParcelUniqueId': table_encryption.convert_long(obj.ErosionBattleConditionParcelUniqueId(), password),
        'ErosionBattleConditionParcelAmount': table_encryption.convert_long(obj.ErosionBattleConditionParcelAmount(), password),
        'ConquestRewardId': table_encryption.convert_long(obj.ConquestRewardId(), password),
    }


def dump_ConquestErosionUnitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TilePrefabId': table_encryption.convert_long(obj.TilePrefabId(), password),
        'MassErosionUnitId': table_encryption.convert_long(obj.MassErosionUnitId(), password),
        'MassErosionUnitRotationY': table_encryption.convert_float(obj.MassErosionUnitRotationY(), password),
        'IndividualErosionUnitId': table_encryption.convert_long(obj.IndividualErosionUnitId(), password),
        'IndividualErosionUnitRotationY': table_encryption.convert_float(obj.IndividualErosionUnitRotationY(), password),
    }


def dump_ConquestEventExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'MainStoryEventContentId': table_encryption.convert_long(obj.MainStoryEventContentId(), password),
        'ConquestEventType': ConquestEventType(table_encryption.convert_int(obj.ConquestEventType_(), password)).name,
        'UseErosion': obj.UseErosion(),
        'UseUnexpectedEvent': obj.UseUnexpectedEvent(),
        'UseCalculate': obj.UseCalculate(),
        'UseConquestObject': obj.UseConquestObject(),
        'EvnetMapGoalLocalize': table_encryption.convert_string(obj.EvnetMapGoalLocalize(), password),
        'EvnetMapNameLocalize': table_encryption.convert_string(obj.EvnetMapNameLocalize(), password),
        'MapEnterScenarioGroupId': table_encryption.convert_long(obj.MapEnterScenarioGroupId(), password),
        'EvnetScenarioBG': table_encryption.convert_string(obj.EvnetScenarioBG(), password),
        'ManageUnitChange': table_encryption.convert_int(obj.ManageUnitChange(), password),
        'AssistCount': table_encryption.convert_int(obj.AssistCount(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_int(obj.PlayTimeLimitInSeconds(), password),
        'AnimationUnitAmountMin': table_encryption.convert_int(obj.AnimationUnitAmountMin(), password),
        'AnimationUnitAmountMax': table_encryption.convert_int(obj.AnimationUnitAmountMax(), password),
        'AnimationUnitDelay': table_encryption.convert_float(obj.AnimationUnitDelay(), password),
        'LocalizeUnexpected': table_encryption.convert_string(obj.LocalizeUnexpected(), password),
        'LocalizeErosions': table_encryption.convert_string(obj.LocalizeErosions(), password),
        'LocalizeStep': table_encryption.convert_string(obj.LocalizeStep(), password),
        'LocalizeTile': table_encryption.convert_string(obj.LocalizeTile(), password),
        'LocalizeMapInfo': table_encryption.convert_string(obj.LocalizeMapInfo(), password),
        'LocalizeManage': table_encryption.convert_string(obj.LocalizeManage(), password),
        'LocalizeUpgrade': table_encryption.convert_string(obj.LocalizeUpgrade(), password),
        'LocalizeTreasureBox': table_encryption.convert_string(obj.LocalizeTreasureBox(), password),
        'IndividualErosionDailyCount': table_encryption.convert_long(obj.IndividualErosionDailyCount(), password),
    }


def dump_ConquestGroupBonusExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ConquestBonusId': table_encryption.convert_long(obj.ConquestBonusId(), password),
        'School': [School(table_encryption.convert_int(obj.School_(j), password)).name for j in range(obj.SchoolLength())],
        'RecommandLocalizeEtcId': table_encryption.convert_uint(obj.RecommandLocalizeEtcId(), password),
        'BonusParcelType': [ParcelType(table_encryption.convert_int(obj.BonusParcelType(j), password)).name for j in range(obj.BonusParcelTypeLength())],
        'BonusId': [table_encryption.convert_long(obj.BonusId(j), password) for j in range(obj.BonusIdLength())],
        'BonusCharacterCount1': [table_encryption.convert_int(obj.BonusCharacterCount1(j), password) for j in range(obj.BonusCharacterCount1Length())],
        'BonusPercentage1': [table_encryption.convert_long(obj.BonusPercentage1(j), password) for j in range(obj.BonusPercentage1Length())],
        'BonusCharacterCount2': [table_encryption.convert_int(obj.BonusCharacterCount2(j), password) for j in range(obj.BonusCharacterCount2Length())],
        'BonusPercentage2': [table_encryption.convert_long(obj.BonusPercentage2(j), password) for j in range(obj.BonusPercentage2Length())],
        'BonusCharacterCount3': [table_encryption.convert_int(obj.BonusCharacterCount3(j), password) for j in range(obj.BonusCharacterCount3Length())],
        'BonusPercentage3': [table_encryption.convert_long(obj.BonusPercentage3(j), password) for j in range(obj.BonusPercentage3Length())],
    }


def dump_ConquestGroupBuffExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ConquestBuffId': table_encryption.convert_long(obj.ConquestBuffId(), password),
        'School': [School(table_encryption.convert_int(obj.School_(j), password)).name for j in range(obj.SchoolLength())],
        'RecommandLocalizeEtcId': table_encryption.convert_uint(obj.RecommandLocalizeEtcId(), password),
        'SkillGroupId': table_encryption.convert_string(obj.SkillGroupId(), password),
    }


def dump_ConquestMapExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'MapDifficulty': StageDifficulty(table_encryption.convert_int(obj.MapDifficulty(), password)).name,
        'StepIndex': table_encryption.convert_int(obj.StepIndex(), password),
        'ConquestMap': table_encryption.convert_string(obj.ConquestMap(), password),
        'StepEnterScenarioGroupId': table_encryption.convert_long(obj.StepEnterScenarioGroupId(), password),
        'StepOpenConditionType': [ConquestConditionType(table_encryption.convert_int(obj.StepOpenConditionType(j), password)).name for j in range(obj.StepOpenConditionTypeLength())],
        'StepOpenConditionParameter': [table_encryption.convert_string(obj.StepOpenConditionParameter(j), password) for j in range(obj.StepOpenConditionParameterLength())],
        'MapGoalLocalize': table_encryption.convert_string(obj.MapGoalLocalize(), password),
        'StepGoalLocalize': table_encryption.convert_string(obj.StepGoalLocalize(), password),
        'StepNameLocalize': table_encryption.convert_string(obj.StepNameLocalize(), password),
        'ConquestMapBG': table_encryption.convert_string(obj.ConquestMapBG(), password),
        'CameraSettingId': table_encryption.convert_long(obj.CameraSettingId(), password),
    }


def dump_ConquestObjectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ConquestObjectType': ConquestObjectType(table_encryption.convert_int(obj.ConquestObjectType_(), password)).name,
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'ConquestRewardParcelType': ParcelType(table_encryption.convert_int(obj.ConquestRewardParcelType(), password)).name,
        'ConquestRewardID': table_encryption.convert_long(obj.ConquestRewardID(), password),
        'ConquestRewardAmount': table_encryption.convert_int(obj.ConquestRewardAmount(), password),
        'Disposable': obj.Disposable(),
        'StepIndex': table_encryption.convert_int(obj.StepIndex(), password),
        'StepObjectCount': table_encryption.convert_int(obj.StepObjectCount(), password),
    }


def dump_ConquestPlayGuideExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'GuideTitle': table_encryption.convert_string(obj.GuideTitle(), password),
        'GuideImagePath': table_encryption.convert_string(obj.GuideImagePath(), password),
        'GuideText': table_encryption.convert_string(obj.GuideText(), password),
    }


def dump_ConquestProgressResourceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Group': ConquestProgressType(table_encryption.convert_int(obj.Group(), password)).name,
        'ProgressResource': table_encryption.convert_string(obj.ProgressResource(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
        'ProgressLocalizeCode': table_encryption.convert_string(obj.ProgressLocalizeCode(), password),
    }


def dump_ConquestRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_ConquestStepExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'MapDifficulty': StageDifficulty(table_encryption.convert_int(obj.MapDifficulty(), password)).name,
        'Step': table_encryption.convert_int(obj.Step(), password),
        'StepGoalLocalize': table_encryption.convert_string(obj.StepGoalLocalize(), password),
        'StepEnterScenarioGroupId': table_encryption.convert_long(obj.StepEnterScenarioGroupId(), password),
        'StepEnterItemType': ParcelType(table_encryption.convert_int(obj.StepEnterItemType(), password)).name,
        'StepEnterItemUniqueId': table_encryption.convert_long(obj.StepEnterItemUniqueId(), password),
        'StepEnterItemAmount': table_encryption.convert_long(obj.StepEnterItemAmount(), password),
        'UnexpectedEventUnitId': [table_encryption.convert_long(obj.UnexpectedEventUnitId(j), password) for j in range(obj.UnexpectedEventUnitIdLength())],
        'UnexpectedEventPrefab': table_encryption.convert_string(obj.UnexpectedEventPrefab(), password),
        'TreasureBoxObjectId': table_encryption.convert_long(obj.TreasureBoxObjectId(), password),
        'TreasureBoxCountPerStepOpen': table_encryption.convert_int(obj.TreasureBoxCountPerStepOpen(), password),
    }


def dump_ConquestTileExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventId': table_encryption.convert_long(obj.EventId(), password),
        'Step': table_encryption.convert_int(obj.Step(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'TileNameLocalize': table_encryption.convert_string(obj.TileNameLocalize(), password),
        'TileImageName': table_encryption.convert_string(obj.TileImageName(), password),
        'Playable': obj.Playable(),
        'TileType': ConquestTileType(table_encryption.convert_int(obj.TileType(), password)).name,
        'NotMapFog': obj.NotMapFog(),
        'GroupBonusId': table_encryption.convert_long(obj.GroupBonusId(), password),
        'ConquestCostType': ParcelType(table_encryption.convert_int(obj.ConquestCostType(), password)).name,
        'ConquestCostId': table_encryption.convert_long(obj.ConquestCostId(), password),
        'ConquestCostAmount': table_encryption.convert_int(obj.ConquestCostAmount(), password),
        'ManageCostType': ParcelType(table_encryption.convert_int(obj.ManageCostType(), password)).name,
        'ManageCostId': table_encryption.convert_long(obj.ManageCostId(), password),
        'ManageCostAmount': table_encryption.convert_int(obj.ManageCostAmount(), password),
        'ConquestRewardId': table_encryption.convert_long(obj.ConquestRewardId(), password),
        'MassErosionId': table_encryption.convert_long(obj.MassErosionId(), password),
        'Upgrade2CostType': ParcelType(table_encryption.convert_int(obj.Upgrade2CostType(), password)).name,
        'Upgrade2CostId': table_encryption.convert_long(obj.Upgrade2CostId(), password),
        'Upgrade2CostAmount': table_encryption.convert_int(obj.Upgrade2CostAmount(), password),
        'Upgrade3CostType': ParcelType(table_encryption.convert_int(obj.Upgrade3CostType(), password)).name,
        'Upgrade3CostId': table_encryption.convert_long(obj.Upgrade3CostId(), password),
        'Upgrade3CostAmount': table_encryption.convert_int(obj.Upgrade3CostAmount(), password),
    }


def dump_ConquestUnexpectedEventExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UnexpectedEventConditionType': ParcelType(table_encryption.convert_int(obj.UnexpectedEventConditionType(), password)).name,
        'UnexpectedEventConditionUniqueId': table_encryption.convert_long(obj.UnexpectedEventConditionUniqueId(), password),
        'UnexpectedEventConditionAmount': table_encryption.convert_long(obj.UnexpectedEventConditionAmount(), password),
        'UnexpectedEventOccurDailyLimitCount': table_encryption.convert_int(obj.UnexpectedEventOccurDailyLimitCount(), password),
        'UnitCountPerStep': table_encryption.convert_int(obj.UnitCountPerStep(), password),
        'UnexpectedEventPrefab': [table_encryption.convert_string(obj.UnexpectedEventPrefab(j), password) for j in range(obj.UnexpectedEventPrefabLength())],
        'UnexpectedEventUnitId': [table_encryption.convert_long(obj.UnexpectedEventUnitId(j), password) for j in range(obj.UnexpectedEventUnitIdLength())],
    }


def dump_ConquestUnitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'StrategyPrefabName': table_encryption.convert_string(obj.StrategyPrefabName(), password),
        'Scale': table_encryption.convert_float(obj.Scale(), password),
        'ShieldEffectScale': table_encryption.convert_float(obj.ShieldEffectScale(), password),
        'UnitFxPrefabName': table_encryption.convert_string(obj.UnitFxPrefabName(), password),
        'PointAnimation': table_encryption.convert_string(obj.PointAnimation(), password),
        'EnemyType': ConquestEnemyType(table_encryption.convert_int(obj.EnemyType(), password)).name,
        'Team': ConquestTeamType(table_encryption.convert_int(obj.Team(), password)).name,
        'UnitGroup': table_encryption.convert_long(obj.UnitGroup(), password),
        'PrevUnitGroup': table_encryption.convert_long(obj.PrevUnitGroup(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'StarGoal': [StarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'GroupBuffId': table_encryption.convert_long(obj.GroupBuffId(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'ManageEchelonStageEnterCostType': ParcelType(table_encryption.convert_int(obj.ManageEchelonStageEnterCostType(), password)).name,
        'ManageEchelonStageEnterCostId': table_encryption.convert_long(obj.ManageEchelonStageEnterCostId(), password),
        'ManageEchelonStageEnterCostAmount': table_encryption.convert_int(obj.ManageEchelonStageEnterCostAmount(), password),
        'EnterScenarioGroupId': table_encryption.convert_long(obj.EnterScenarioGroupId(), password),
        'ClearScenarioGroupId': table_encryption.convert_long(obj.ClearScenarioGroupId(), password),
        'ConquestRewardId': table_encryption.convert_long(obj.ConquestRewardId(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'TacticRewardExp': table_encryption.convert_long(obj.TacticRewardExp(), password),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_ConstArenaExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'AttackCoolTime': table_encryption.convert_long(obj.AttackCoolTime(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'DefenseCoolTime': table_encryption.convert_long(obj.DefenseCoolTime(), password),
        'TSSStartCoolTime': table_encryption.convert_long(obj.TSSStartCoolTime(), password),
        'EndAlarm': table_encryption.convert_long(obj.EndAlarm(), password),
        'TimeRewardMaxAmount': table_encryption.convert_long(obj.TimeRewardMaxAmount(), password),
        'EnterCostType': ParcelType(table_encryption.convert_int(obj.EnterCostType(), password)).name,
        'EnterCostId': table_encryption.convert_long(obj.EnterCostId(), password),
        'TicketCost': table_encryption.convert_long(obj.TicketCost(), password),
        'DailyRewardResetTime': table_encryption.convert_string(obj.DailyRewardResetTime(), password),
        'OpenScenarioId': table_encryption.convert_string(obj.OpenScenarioId(), password),
        'CharacterSlotHideRank': [table_encryption.convert_long(obj.CharacterSlotHideRank(j), password) for j in range(obj.CharacterSlotHideRankLength())],
        'MapSlotHideRank': table_encryption.convert_long(obj.MapSlotHideRank(), password),
        'RelativeOpponentRankStart': [table_encryption.convert_long(obj.RelativeOpponentRankStart(j), password) for j in range(obj.RelativeOpponentRankStartLength())],
        'RelativeOpponentRankEnd': [table_encryption.convert_long(obj.RelativeOpponentRankEnd(j), password) for j in range(obj.RelativeOpponentRankEndLength())],
        'ModifiedStatType': [StatType(table_encryption.convert_int(obj.ModifiedStatType(j), password)).name for j in range(obj.ModifiedStatTypeLength())],
        'StatMulFactor': [table_encryption.convert_long(obj.StatMulFactor(j), password) for j in range(obj.StatMulFactorLength())],
        'StatSumFactor': [table_encryption.convert_long(obj.StatSumFactor(j), password) for j in range(obj.StatSumFactorLength())],
        'NPCName': [table_encryption.convert_string(obj.NPCName(j), password) for j in range(obj.NPCNameLength())],
        'NPCMainCharacterCount': table_encryption.convert_long(obj.NPCMainCharacterCount(), password),
        'NPCSupportCharacterCount': table_encryption.convert_long(obj.NPCSupportCharacterCount(), password),
        'NPCCharacterSkillLevel': table_encryption.convert_long(obj.NPCCharacterSkillLevel(), password),
        'TimeSpanInDaysForBattleHistory': table_encryption.convert_long(obj.TimeSpanInDaysForBattleHistory(), password),
        'HiddenCharacterImagePath': table_encryption.convert_string(obj.HiddenCharacterImagePath(), password),
        'DefenseVictoryRewardMaxCount': table_encryption.convert_long(obj.DefenseVictoryRewardMaxCount(), password),
        'TopRankerCountLimit': table_encryption.convert_long(obj.TopRankerCountLimit(), password),
        'AutoRefreshIntervalMilliSeconds': table_encryption.convert_long(obj.AutoRefreshIntervalMilliSeconds(), password),
        'EchelonSettingIntervalMilliSeconds': table_encryption.convert_long(obj.EchelonSettingIntervalMilliSeconds(), password),
        'SkipAllowedTimeMilliSeconds': table_encryption.convert_long(obj.SkipAllowedTimeMilliSeconds(), password),
        'ShowSeasonChangeInfoStartTime': table_encryption.convert_string(obj.ShowSeasonChangeInfoStartTime(), password),
        'ShowSeasonChangeInfoEndTime': table_encryption.convert_string(obj.ShowSeasonChangeInfoEndTime(), password),
        'ShowSeasonId': table_encryption.convert_long(obj.ShowSeasonId(), password),
    }


def dump_ConstAudioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'DefaultSnapShotName': table_encryption.convert_string(obj.DefaultSnapShotName(), password),
        'BattleSnapShotName': table_encryption.convert_string(obj.BattleSnapShotName(), password),
        'RaidSnapShotName': table_encryption.convert_string(obj.RaidSnapShotName(), password),
        'ExSkillCutInSnapShotName': table_encryption.convert_string(obj.ExSkillCutInSnapShotName(), password),
    }


def dump_ConstCombatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SkillHandCount': table_encryption.convert_int(obj.SkillHandCount(), password),
        'DyingTime': table_encryption.convert_int(obj.DyingTime(), password),
        'BuffIconBlinkTime': table_encryption.convert_int(obj.BuffIconBlinkTime(), password),
        'ShowBufficonEXSkill': obj.ShowBufficonEXSkill(),
        'ShowBufficonPassiveSkill': obj.ShowBufficonPassiveSkill(),
        'ShowBufficonExtraPassiveSkill': obj.ShowBufficonExtraPassiveSkill(),
        'ShowBufficonLeaderSkill': obj.ShowBufficonLeaderSkill(),
        'ShowBufficonGroundPassiveSkill': obj.ShowBufficonGroundPassiveSkill(),
        'SuppliesConditionStringId': table_encryption.convert_string(obj.SuppliesConditionStringId(), password),
        'PublicSpeechBubbleOffsetX': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetX(), password),
        'PublicSpeechBubbleOffsetY': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetY(), password),
        'PublicSpeechBubbleOffsetZ': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetZ(), password),
        'ShowRaidListCount': table_encryption.convert_int(obj.ShowRaidListCount(), password),
        'MaxRaidTicketCount': table_encryption.convert_long(obj.MaxRaidTicketCount(), password),
        'MaxRaidBossSkillSlot': table_encryption.convert_long(obj.MaxRaidBossSkillSlot(), password),
        'EngageTimelinePath': table_encryption.convert_string(obj.EngageTimelinePath(), password),
        'EngageWithSupporterTimelinePath': table_encryption.convert_string(obj.EngageWithSupporterTimelinePath(), password),
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'TimeLimitAlarm': table_encryption.convert_long(obj.TimeLimitAlarm(), password),
        'EchelonMaxCommonCost': table_encryption.convert_int(obj.EchelonMaxCommonCost(), password),
        'EchelonInitCommonCost': table_encryption.convert_int(obj.EchelonInitCommonCost(), password),
        'SkillSlotCoolTime': table_encryption.convert_long(obj.SkillSlotCoolTime(), password),
        'EnemyRegenCost': table_encryption.convert_long(obj.EnemyRegenCost(), password),
        'ChampionRegenCost': table_encryption.convert_long(obj.ChampionRegenCost(), password),
        'PlayerRegenCostDelay': table_encryption.convert_long(obj.PlayerRegenCostDelay(), password),
        'CrowdControlFactor': table_encryption.convert_long(obj.CrowdControlFactor(), password),
        'RaidOpenScenarioId': table_encryption.convert_string(obj.RaidOpenScenarioId(), password),
        'EliminateRaidOpenScenarioId': table_encryption.convert_string(obj.EliminateRaidOpenScenarioId(), password),
        'DefenceConstA': table_encryption.convert_long(obj.DefenceConstA(), password),
        'DefenceConstB': table_encryption.convert_long(obj.DefenceConstB(), password),
        'DefenceConstC': table_encryption.convert_long(obj.DefenceConstC(), password),
        'DefenceConstD': table_encryption.convert_long(obj.DefenceConstD(), password),
        'AccuracyConstA': table_encryption.convert_long(obj.AccuracyConstA(), password),
        'AccuracyConstB': table_encryption.convert_long(obj.AccuracyConstB(), password),
        'AccuracyConstC': table_encryption.convert_long(obj.AccuracyConstC(), password),
        'AccuracyConstD': table_encryption.convert_long(obj.AccuracyConstD(), password),
        'CriticalConstA': table_encryption.convert_long(obj.CriticalConstA(), password),
        'CriticalConstB': table_encryption.convert_long(obj.CriticalConstB(), password),
        'CriticalConstC': table_encryption.convert_long(obj.CriticalConstC(), password),
        'CriticalConstD': table_encryption.convert_long(obj.CriticalConstD(), password),
        'MaxGroupBuffLevel': table_encryption.convert_int(obj.MaxGroupBuffLevel(), password),
        'EmojiDefaultTime': table_encryption.convert_int(obj.EmojiDefaultTime(), password),
        'TimeLineActionRotateSpeed': table_encryption.convert_long(obj.TimeLineActionRotateSpeed(), password),
        'BodyRotateSpeed': table_encryption.convert_long(obj.BodyRotateSpeed(), password),
        'NormalTimeScale': table_encryption.convert_long(obj.NormalTimeScale(), password),
        'FastTimeScale': table_encryption.convert_long(obj.FastTimeScale(), password),
        'BulletTimeScale': table_encryption.convert_long(obj.BulletTimeScale(), password),
        'UIDisplayDelayAfterSkillCutIn': table_encryption.convert_long(obj.UIDisplayDelayAfterSkillCutIn(), password),
        'UseInitialRangeForCoverMove': obj.UseInitialRangeForCoverMove(),
        'SlowTimeScale': table_encryption.convert_long(obj.SlowTimeScale(), password),
        'AimIKMinDegree': table_encryption.convert_float(obj.AimIKMinDegree(), password),
        'AimIKMaxDegree': table_encryption.convert_float(obj.AimIKMaxDegree(), password),
        'MinimumClearTime': table_encryption.convert_int(obj.MinimumClearTime(), password),
        'MinimumClearLevelGap': table_encryption.convert_int(obj.MinimumClearLevelGap(), password),
        'CheckCheaterMaxUseCostNonArena': table_encryption.convert_int(obj.CheckCheaterMaxUseCostNonArena(), password),
        'CheckCheaterMaxUseCostArena': table_encryption.convert_int(obj.CheckCheaterMaxUseCostArena(), password),
        'AllowedMaxTimeScale': table_encryption.convert_long(obj.AllowedMaxTimeScale(), password),
        'RandomAnimationOutput': table_encryption.convert_long(obj.RandomAnimationOutput(), password),
        'SummonedTeleportDistance': table_encryption.convert_long(obj.SummonedTeleportDistance(), password),
        'ArenaMinimumClearTime': table_encryption.convert_int(obj.ArenaMinimumClearTime(), password),
        'WORLDBOSSBATTLELITTLE': table_encryption.convert_long(obj.WORLDBOSSBATTLELITTLE(), password),
        'WORLDBOSSBATTLEMIDDLE': table_encryption.convert_long(obj.WORLDBOSSBATTLEMIDDLE(), password),
        'WORLDBOSSBATTLEHIGH': table_encryption.convert_long(obj.WORLDBOSSBATTLEHIGH(), password),
        'WORLDBOSSBATTLEVERYHIGH': table_encryption.convert_long(obj.WORLDBOSSBATTLEVERYHIGH(), password),
        'WorldRaidAutoSyncTermSecond': table_encryption.convert_long(obj.WorldRaidAutoSyncTermSecond(), password),
        'WorldRaidBossHpDecreaseTerm': table_encryption.convert_long(obj.WorldRaidBossHpDecreaseTerm(), password),
        'WorldRaidBossParcelReactionDelay': table_encryption.convert_long(obj.WorldRaidBossParcelReactionDelay(), password),
        'RaidRankingJumpMinimumWaitingTime': table_encryption.convert_long(obj.RaidRankingJumpMinimumWaitingTime(), password),
        'EffectTeleportDistance': table_encryption.convert_float(obj.EffectTeleportDistance(), password),
        'AuraExitThresholdMargin': table_encryption.convert_long(obj.AuraExitThresholdMargin(), password),
        'TSAInteractionDamageFactor': table_encryption.convert_long(obj.TSAInteractionDamageFactor(), password),
        'VictoryInteractionRate': table_encryption.convert_long(obj.VictoryInteractionRate(), password),
        'EchelonExtensionEngageTimelinePath': table_encryption.convert_string(obj.EchelonExtensionEngageTimelinePath(), password),
        'EchelonExtensionEngageWithSupporterTimelinePath': table_encryption.convert_string(obj.EchelonExtensionEngageWithSupporterTimelinePath(), password),
        'EchelonExtensionVictoryTimelinePath': table_encryption.convert_string(obj.EchelonExtensionVictoryTimelinePath(), password),
        'EchelonExtensionEchelonMaxCommonCost': table_encryption.convert_int(obj.EchelonExtensionEchelonMaxCommonCost(), password),
        'EchelonExtensionEchelonInitCommonCost': table_encryption.convert_int(obj.EchelonExtensionEchelonInitCommonCost(), password),
        'EchelonExtensionCostRegenRatio': table_encryption.convert_long(obj.EchelonExtensionCostRegenRatio(), password),
        'CheckCheaterMaxUseCostMultiFloorRaid': table_encryption.convert_int(obj.CheckCheaterMaxUseCostMultiFloorRaid(), password),
    }


def dump_ConstCommonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CampaignMainStageMaxRank': table_encryption.convert_int(obj.CampaignMainStageMaxRank(), password),
        'CampaignMainStageBestRecord': table_encryption.convert_int(obj.CampaignMainStageBestRecord(), password),
        'HardAdventurePlayCountRecoverDailyNumber': table_encryption.convert_int(obj.HardAdventurePlayCountRecoverDailyNumber(), password),
        'HardStageCount': table_encryption.convert_int(obj.HardStageCount(), password),
        'TacticRankClearTime': table_encryption.convert_int(obj.TacticRankClearTime(), password),
        'BaseTimeScale': table_encryption.convert_long(obj.BaseTimeScale(), password),
        'GachaPercentage': table_encryption.convert_int(obj.GachaPercentage(), password),
        'AcademyFavorZoneId': table_encryption.convert_long(obj.AcademyFavorZoneId(), password),
        'CafePresetSlotCount': table_encryption.convert_int(obj.CafePresetSlotCount(), password),
        'CafeMonologueIntervalMillisec': table_encryption.convert_long(obj.CafeMonologueIntervalMillisec(), password),
        'CafeMonologueDefaultDuration': table_encryption.convert_long(obj.CafeMonologueDefaultDuration(), password),
        'CafeBubbleIdleDurationMilliSec': table_encryption.convert_long(obj.CafeBubbleIdleDurationMilliSec(), password),
        'FindGiftTimeLimit': table_encryption.convert_int(obj.FindGiftTimeLimit(), password),
        'CafeAutoChargePeriodInMsc': table_encryption.convert_int(obj.CafeAutoChargePeriodInMsc(), password),
        'CafeProductionDecimalPosition': table_encryption.convert_int(obj.CafeProductionDecimalPosition(), password),
        'CafeSetGroupApplyCount': table_encryption.convert_int(obj.CafeSetGroupApplyCount(), password),
        'WeekDungeonFindGiftRewardLimitCount': table_encryption.convert_int(obj.WeekDungeonFindGiftRewardLimitCount(), password),
        'StageFailedCurrencyRefundRate': table_encryption.convert_int(obj.StageFailedCurrencyRefundRate(), password),
        'EnterDeposit': table_encryption.convert_int(obj.EnterDeposit(), password),
        'AccountMaxLevel': table_encryption.convert_int(obj.AccountMaxLevel(), password),
        'MainSquadExpBonus': table_encryption.convert_int(obj.MainSquadExpBonus(), password),
        'SupportSquadExpBonus': table_encryption.convert_int(obj.SupportSquadExpBonus(), password),
        'AccountExpRatio': table_encryption.convert_int(obj.AccountExpRatio(), password),
        'MissionToastLifeTime': table_encryption.convert_int(obj.MissionToastLifeTime(), password),
        'ExpItemInsertLimit': table_encryption.convert_int(obj.ExpItemInsertLimit(), password),
        'ExpItemInsertAccelTime': table_encryption.convert_int(obj.ExpItemInsertAccelTime(), password),
        'CharacterLvUpCoefficient': table_encryption.convert_int(obj.CharacterLvUpCoefficient(), password),
        'EquipmentLvUpCoefficient': table_encryption.convert_int(obj.EquipmentLvUpCoefficient(), password),
        'ExpEquipInsertLimit': table_encryption.convert_int(obj.ExpEquipInsertLimit(), password),
        'EquipLvUpCoefficient': table_encryption.convert_int(obj.EquipLvUpCoefficient(), password),
        'NicknameLength': table_encryption.convert_int(obj.NicknameLength(), password),
        'CraftDuration': [table_encryption.convert_int(obj.CraftDuration(j), password) for j in range(obj.CraftDurationLength())],
        'CraftLimitTime': table_encryption.convert_int(obj.CraftLimitTime(), password),
        'ShiftingCraftDuration': [table_encryption.convert_int(obj.ShiftingCraftDuration(j), password) for j in range(obj.ShiftingCraftDurationLength())],
        'ShiftingCraftTicketConsumeAmount': table_encryption.convert_int(obj.ShiftingCraftTicketConsumeAmount(), password),
        'ShiftingCraftSlotMaxCapacity': table_encryption.convert_int(obj.ShiftingCraftSlotMaxCapacity(), password),
        'CraftTicketItemUniqueId': table_encryption.convert_int(obj.CraftTicketItemUniqueId(), password),
        'CraftTicketConsumeAmount': table_encryption.convert_int(obj.CraftTicketConsumeAmount(), password),
        'AcademyEnterCostType': ParcelType(table_encryption.convert_int(obj.AcademyEnterCostType(), password)).name,
        'AcademyEnterCostId': table_encryption.convert_long(obj.AcademyEnterCostId(), password),
        'AcademyTicketCost': table_encryption.convert_int(obj.AcademyTicketCost(), password),
        'MassangerMessageExpireDay': table_encryption.convert_int(obj.MassangerMessageExpireDay(), password),
        'CraftLeafNodeGenerateLv1Count': table_encryption.convert_int(obj.CraftLeafNodeGenerateLv1Count(), password),
        'CraftLeafNodeGenerateLv2Count': table_encryption.convert_int(obj.CraftLeafNodeGenerateLv2Count(), password),
        'TutorialGachaShopId': table_encryption.convert_int(obj.TutorialGachaShopId(), password),
        'BeforehandGachaShopId': table_encryption.convert_int(obj.BeforehandGachaShopId(), password),
        'TutorialGachaGoodsId': table_encryption.convert_int(obj.TutorialGachaGoodsId(), password),
        'EquipmentSlotOpenLevel': [table_encryption.convert_int(obj.EquipmentSlotOpenLevel(j), password) for j in range(obj.EquipmentSlotOpenLevelLength())],
        'ScenarioAutoDelayMillisec': table_encryption.convert_float(obj.ScenarioAutoDelayMillisec(), password),
        'JoinOrCreateClanCoolTimeFromHour': table_encryption.convert_long(obj.JoinOrCreateClanCoolTimeFromHour(), password),
        'ClanMaxMember': table_encryption.convert_long(obj.ClanMaxMember(), password),
        'ClanSearchResultCount': table_encryption.convert_long(obj.ClanSearchResultCount(), password),
        'ClanMaxApplicant': table_encryption.convert_long(obj.ClanMaxApplicant(), password),
        'ClanRejoinCoolTimeFromSecond': table_encryption.convert_long(obj.ClanRejoinCoolTimeFromSecond(), password),
        'ClanWordBalloonMaxCharacter': table_encryption.convert_int(obj.ClanWordBalloonMaxCharacter(), password),
        'CallNameRenameCoolTimeFromHour': table_encryption.convert_long(obj.CallNameRenameCoolTimeFromHour(), password),
        'CallNameMinimumLength': table_encryption.convert_long(obj.CallNameMinimumLength(), password),
        'CallNameMaximumLength': table_encryption.convert_long(obj.CallNameMaximumLength(), password),
        'LobbyToScreenModeWaitTime': table_encryption.convert_long(obj.LobbyToScreenModeWaitTime(), password),
        'ScreenshotToLobbyButtonHideDelay': table_encryption.convert_long(obj.ScreenshotToLobbyButtonHideDelay(), password),
        'PrologueScenarioID01': table_encryption.convert_long(obj.PrologueScenarioID01(), password),
        'PrologueScenarioID02': table_encryption.convert_long(obj.PrologueScenarioID02(), password),
        'TutorialHardStage11': table_encryption.convert_long(obj.TutorialHardStage11(), password),
        'TutorialSpeedButtonStage': table_encryption.convert_long(obj.TutorialSpeedButtonStage(), password),
        'TutorialCharacterDefaultCount': table_encryption.convert_long(obj.TutorialCharacterDefaultCount(), password),
        'TutorialShopCategoryType': ShopCategoryType(table_encryption.convert_int(obj.TutorialShopCategoryType(), password)).name,
        'AdventureStrategyPlayTimeLimitInSeconds': table_encryption.convert_long(obj.AdventureStrategyPlayTimeLimitInSeconds(), password),
        'WeekDungoenTacticPlayTimeLimitInSeconds': table_encryption.convert_long(obj.WeekDungoenTacticPlayTimeLimitInSeconds(), password),
        'RaidTacticPlayTimeLimitInSeconds': table_encryption.convert_long(obj.RaidTacticPlayTimeLimitInSeconds(), password),
        'RaidOpponentListAmount': table_encryption.convert_long(obj.RaidOpponentListAmount(), password),
        'CraftBaseGoldRequired': [table_encryption.convert_long(obj.CraftBaseGoldRequired(j), password) for j in range(obj.CraftBaseGoldRequiredLength())],
        'PostExpiredDayAttendance': table_encryption.convert_int(obj.PostExpiredDayAttendance(), password),
        'PostExpiredDayInventoryOverflow': table_encryption.convert_int(obj.PostExpiredDayInventoryOverflow(), password),
        'PostExpiredDayGameManager': table_encryption.convert_int(obj.PostExpiredDayGameManager(), password),
        'UILabelCharacterWrap': table_encryption.convert_string(obj.UILabelCharacterWrap(), password),
        'RequestTimeOut': table_encryption.convert_float(obj.RequestTimeOut(), password),
        'MailStorageSoftCap': table_encryption.convert_int(obj.MailStorageSoftCap(), password),
        'MailStorageHardCap': table_encryption.convert_int(obj.MailStorageHardCap(), password),
        'ClearDeckStorageSize': table_encryption.convert_int(obj.ClearDeckStorageSize(), password),
        'ClearDeckNoStarViewCount': table_encryption.convert_int(obj.ClearDeckNoStarViewCount(), password),
        'ClearDeck1StarViewCount': table_encryption.convert_int(obj.ClearDeck1StarViewCount(), password),
        'ClearDeck2StarViewCount': table_encryption.convert_int(obj.ClearDeck2StarViewCount(), password),
        'ClearDeck3StarViewCount': table_encryption.convert_int(obj.ClearDeck3StarViewCount(), password),
        'ExSkillLevelMax': table_encryption.convert_int(obj.ExSkillLevelMax(), password),
        'PublicSkillLevelMax': table_encryption.convert_int(obj.PublicSkillLevelMax(), password),
        'PassiveSkillLevelMax': table_encryption.convert_int(obj.PassiveSkillLevelMax(), password),
        'ExtraPassiveSkillLevelMax': table_encryption.convert_int(obj.ExtraPassiveSkillLevelMax(), password),
        'AccountCommentMaxLength': table_encryption.convert_int(obj.AccountCommentMaxLength(), password),
        'CafeSummonCoolTimeFromHour': table_encryption.convert_int(obj.CafeSummonCoolTimeFromHour(), password),
        'LimitedStageDailyClearCount': table_encryption.convert_long(obj.LimitedStageDailyClearCount(), password),
        'LimitedStageEntryTimeLimit': table_encryption.convert_long(obj.LimitedStageEntryTimeLimit(), password),
        'LimitedStageEntryTimeBuffer': table_encryption.convert_long(obj.LimitedStageEntryTimeBuffer(), password),
        'LimitedStagePointAmount': table_encryption.convert_long(obj.LimitedStagePointAmount(), password),
        'LimitedStagePointPerApMin': table_encryption.convert_long(obj.LimitedStagePointPerApMin(), password),
        'LimitedStagePointPerApMax': table_encryption.convert_long(obj.LimitedStagePointPerApMax(), password),
        'AccountLinkReward': table_encryption.convert_int(obj.AccountLinkReward(), password),
        'MonthlyProductCheckDays': table_encryption.convert_int(obj.MonthlyProductCheckDays(), password),
        'WeaponLvUpCoefficient': table_encryption.convert_int(obj.WeaponLvUpCoefficient(), password),
        'ShowRaidMyListCount': table_encryption.convert_int(obj.ShowRaidMyListCount(), password),
        'MaxLevelExpMasterCoinRatio': table_encryption.convert_int(obj.MaxLevelExpMasterCoinRatio(), password),
        'RaidEnterCostType': ParcelType(table_encryption.convert_int(obj.RaidEnterCostType(), password)).name,
        'RaidEnterCostId': table_encryption.convert_long(obj.RaidEnterCostId(), password),
        'RaidTicketCost': table_encryption.convert_long(obj.RaidTicketCost(), password),
        'TimeAttackDungeonScenarioId': table_encryption.convert_string(obj.TimeAttackDungeonScenarioId(), password),
        'TimeAttackDungoenPlayCountPerTicket': table_encryption.convert_int(obj.TimeAttackDungoenPlayCountPerTicket(), password),
        'TimeAttackDungeonEnterCostType': ParcelType(table_encryption.convert_int(obj.TimeAttackDungeonEnterCostType(), password)).name,
        'TimeAttackDungeonEnterCostId': table_encryption.convert_long(obj.TimeAttackDungeonEnterCostId(), password),
        'TimeAttackDungeonEnterCost': table_encryption.convert_long(obj.TimeAttackDungeonEnterCost(), password),
        'ClanLeaderTransferLastLoginLimit': table_encryption.convert_long(obj.ClanLeaderTransferLastLoginLimit(), password),
        'MonthlyProductRepurchasePopupLimit': table_encryption.convert_int(obj.MonthlyProductRepurchasePopupLimit(), password),
        'CommonFavorItemTags': [Tag(table_encryption.convert_int(obj.CommonFavorItemTags(j), password)).name for j in range(obj.CommonFavorItemTagsLength())],
        'MaxApMasterCoinPerWeek': table_encryption.convert_long(obj.MaxApMasterCoinPerWeek(), password),
        'CraftOpenExpTier1': table_encryption.convert_long(obj.CraftOpenExpTier1(), password),
        'CraftOpenExpTier2': table_encryption.convert_long(obj.CraftOpenExpTier2(), password),
        'CraftOpenExpTier3': table_encryption.convert_long(obj.CraftOpenExpTier3(), password),
        'CharacterEquipmentGearSlot': table_encryption.convert_long(obj.CharacterEquipmentGearSlot(), password),
        'BirthDayDDay': table_encryption.convert_int(obj.BirthDayDDay(), password),
        'RecommendedFriendsLvDifferenceLimit': table_encryption.convert_int(obj.RecommendedFriendsLvDifferenceLimit(), password),
        'DDosDetectCount': table_encryption.convert_int(obj.DDosDetectCount(), password),
        'DDosCheckIntervalInSeconds': table_encryption.convert_int(obj.DDosCheckIntervalInSeconds(), password),
        'MaxFriendsCount': table_encryption.convert_int(obj.MaxFriendsCount(), password),
        'MaxFriendsRequest': table_encryption.convert_int(obj.MaxFriendsRequest(), password),
        'FriendsSearchRequestCount': table_encryption.convert_int(obj.FriendsSearchRequestCount(), password),
        'FriendsMaxApplicant': table_encryption.convert_int(obj.FriendsMaxApplicant(), password),
        'IdCardDefaultCharacterId': table_encryption.convert_long(obj.IdCardDefaultCharacterId(), password),
        'IdCardDefaultBgId': table_encryption.convert_long(obj.IdCardDefaultBgId(), password),
        'WorldRaidGemEnterCost': table_encryption.convert_long(obj.WorldRaidGemEnterCost(), password),
        'WorldRaidGemEnterAmout': table_encryption.convert_long(obj.WorldRaidGemEnterAmout(), password),
        'FriendIdCardCommentMaxLength': table_encryption.convert_long(obj.FriendIdCardCommentMaxLength(), password),
        'FormationPresetNumberOfEchelonTab': table_encryption.convert_int(obj.FormationPresetNumberOfEchelonTab(), password),
        'FormationPresetNumberOfEchelon': table_encryption.convert_int(obj.FormationPresetNumberOfEchelon(), password),
        'FormationPresetRecentNumberOfEchelon': table_encryption.convert_int(obj.FormationPresetRecentNumberOfEchelon(), password),
        'FormationPresetEchelonTabTextLength': table_encryption.convert_int(obj.FormationPresetEchelonTabTextLength(), password),
        'FormationPresetEchelonSlotTextLength': table_encryption.convert_int(obj.FormationPresetEchelonSlotTextLength(), password),
        'CharProfileRowIntervalKr': table_encryption.convert_int(obj.CharProfileRowIntervalKr(), password),
        'CharProfileRowIntervalJp': table_encryption.convert_int(obj.CharProfileRowIntervalJp(), password),
        'CharProfilePopupRowIntervalKr': table_encryption.convert_int(obj.CharProfilePopupRowIntervalKr(), password),
        'CharProfilePopupRowIntervalJp': table_encryption.convert_int(obj.CharProfilePopupRowIntervalJp(), password),
        'BeforehandGachaCount': table_encryption.convert_int(obj.BeforehandGachaCount(), password),
        'BeforehandGachaGroupId': table_encryption.convert_int(obj.BeforehandGachaGroupId(), password),
        'RenewalDisplayOrderDay': table_encryption.convert_int(obj.RenewalDisplayOrderDay(), password),
        'EmblemDefaultId': table_encryption.convert_long(obj.EmblemDefaultId(), password),
        'BirthdayMailStartDate': table_encryption.convert_string(obj.BirthdayMailStartDate(), password),
        'BirthdayMailRemainDate': table_encryption.convert_int(obj.BirthdayMailRemainDate(), password),
        'BirthdayMailParcelType': ParcelType(table_encryption.convert_int(obj.BirthdayMailParcelType(), password)).name,
        'BirthdayMailParcelId': table_encryption.convert_long(obj.BirthdayMailParcelId(), password),
        'BirthdayMailParcelAmount': table_encryption.convert_int(obj.BirthdayMailParcelAmount(), password),
        'ClearDeckAverageDeckCount': table_encryption.convert_int(obj.ClearDeckAverageDeckCount(), password),
        'ClearDeckWorldRaidSaveConditionCoefficient': table_encryption.convert_int(obj.ClearDeckWorldRaidSaveConditionCoefficient(), password),
        'ClearDeckShowCount': table_encryption.convert_int(obj.ClearDeckShowCount(), password),
        'CharacterMaxLevel': table_encryption.convert_int(obj.CharacterMaxLevel(), password),
        'PotentialBonusStatMaxLevelMaxHP': table_encryption.convert_int(obj.PotentialBonusStatMaxLevelMaxHP(), password),
        'PotentialBonusStatMaxLevelAttackPower': table_encryption.convert_int(obj.PotentialBonusStatMaxLevelAttackPower(), password),
        'PotentialBonusStatMaxLevelHealPower': table_encryption.convert_int(obj.PotentialBonusStatMaxLevelHealPower(), password),
        'PotentialOpenConditionCharacterLevel': table_encryption.convert_int(obj.PotentialOpenConditionCharacterLevel(), password),
        'AssistStrangerMinLevel': table_encryption.convert_int(obj.AssistStrangerMinLevel(), password),
        'AssistStrangerMaxLevel': table_encryption.convert_int(obj.AssistStrangerMaxLevel(), password),
        'MaxBlockedUserCount': table_encryption.convert_int(obj.MaxBlockedUserCount(), password),
    }


def dump_ConstConquestExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ManageUnitChange': table_encryption.convert_int(obj.ManageUnitChange(), password),
        'AssistCount': table_encryption.convert_int(obj.AssistCount(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_int(obj.PlayTimeLimitInSeconds(), password),
        'AnimationUnitAmountMin': table_encryption.convert_int(obj.AnimationUnitAmountMin(), password),
        'AnimationUnitAmountMax': table_encryption.convert_int(obj.AnimationUnitAmountMax(), password),
        'AnimationUnitDelay': table_encryption.convert_float(obj.AnimationUnitDelay(), password),
    }


def dump_ConstEventCommonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentHardStageCount': table_encryption.convert_int(obj.EventContentHardStageCount(), password),
        'EventStrategyPlayTimeLimitInSeconds': table_encryption.convert_long(obj.EventStrategyPlayTimeLimitInSeconds(), password),
        'SubEventChangeLimitSeconds': table_encryption.convert_long(obj.SubEventChangeLimitSeconds(), password),
        'SubEventInstantClear': obj.SubEventInstantClear(),
        'CardShopProbWeightCount': table_encryption.convert_long(obj.CardShopProbWeightCount(), password),
        'CardShopProbWeightRarity': Rarity(table_encryption.convert_int(obj.CardShopProbWeightRarity(), password)).name,
        'MeetupScenarioReplayResource': table_encryption.convert_string(obj.MeetupScenarioReplayResource(), password),
        'MeetupScenarioReplayTitleLocalize': table_encryption.convert_string(obj.MeetupScenarioReplayTitleLocalize(), password),
        'SpecialOperactionCollectionGroupId': table_encryption.convert_long(obj.SpecialOperactionCollectionGroupId(), password),
        'TreasureNormalVariationAmount': table_encryption.convert_int(obj.TreasureNormalVariationAmount(), password),
        'TreasureLoopVariationAmount': table_encryption.convert_int(obj.TreasureLoopVariationAmount(), password),
        'TreasureLimitVariationLoopCount': table_encryption.convert_int(obj.TreasureLimitVariationLoopCount(), password),
        'TreasureLimitVariationClearLoopCount': table_encryption.convert_int(obj.TreasureLimitVariationClearLoopCount(), password),
    }


def dump_ConstFieldExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'DialogSmoothTime': table_encryption.convert_int(obj.DialogSmoothTime(), password),
        'TalkDialogDurationDefault': table_encryption.convert_int(obj.TalkDialogDurationDefault(), password),
        'ThinkDialogDurationDefault': table_encryption.convert_int(obj.ThinkDialogDurationDefault(), password),
        'IdleThinkDelayMin': table_encryption.convert_int(obj.IdleThinkDelayMin(), password),
        'IdleThinkDelayMax': table_encryption.convert_int(obj.IdleThinkDelayMax(), password),
        'ExclaimDurationDefault': table_encryption.convert_int(obj.ExclaimDurationDefault(), password),
        'QuestionDurationDefault': table_encryption.convert_int(obj.QuestionDurationDefault(), password),
        'UpsetDurationDefault': table_encryption.convert_int(obj.UpsetDurationDefault(), password),
        'SurpriseDurationDefault': table_encryption.convert_int(obj.SurpriseDurationDefault(), password),
        'BulbDurationDefault': table_encryption.convert_int(obj.BulbDurationDefault(), password),
        'HeartDurationDefault': table_encryption.convert_int(obj.HeartDurationDefault(), password),
        'SweatDurationDefault': table_encryption.convert_int(obj.SweatDurationDefault(), password),
        'AngryDurationDefault': table_encryption.convert_int(obj.AngryDurationDefault(), password),
        'MusicDurationDefault': table_encryption.convert_int(obj.MusicDurationDefault(), password),
        'DotDurationDefault': table_encryption.convert_int(obj.DotDurationDefault(), password),
        'MomotalkDurationDefault': table_encryption.convert_int(obj.MomotalkDurationDefault(), password),
        'PhoneDurationDefault': table_encryption.convert_int(obj.PhoneDurationDefault(), password),
        'KeywordDurationDefault': table_encryption.convert_int(obj.KeywordDurationDefault(), password),
        'EvidenceDurationDefault': table_encryption.convert_int(obj.EvidenceDurationDefault(), password),
    }


def dump_ConstMiniGameShootingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'NormalStageId': table_encryption.convert_long(obj.NormalStageId(), password),
        'NormalSectionCount': table_encryption.convert_int(obj.NormalSectionCount(), password),
        'HardStageId': table_encryption.convert_long(obj.HardStageId(), password),
        'HardSectionCount': table_encryption.convert_int(obj.HardSectionCount(), password),
        'FreeStageId': table_encryption.convert_long(obj.FreeStageId(), password),
        'FreeSectionCount': table_encryption.convert_int(obj.FreeSectionCount(), password),
        'PlayerCharacterId': [table_encryption.convert_long(obj.PlayerCharacterId(j), password) for j in range(obj.PlayerCharacterIdLength())],
        'HiddenPlayerCharacterId': table_encryption.convert_long(obj.HiddenPlayerCharacterId(), password),
        'CameraSmoothTime': table_encryption.convert_float(obj.CameraSmoothTime(), password),
        'SpawnEffectPath': table_encryption.convert_string(obj.SpawnEffectPath(), password),
        'WaitTimeAfterSpawn': table_encryption.convert_float(obj.WaitTimeAfterSpawn(), password),
        'FreeGearInterval': table_encryption.convert_int(obj.FreeGearInterval(), password),
    }


def dump_ConstMinigameTBGExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ConquestMapBoundaryOffsetLeft': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetLeft(), password),
        'ConquestMapBoundaryOffsetRight': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetRight(), password),
        'ConquestMapBoundaryOffsetTop': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetTop(), password),
        'ConquestMapBoundaryOffsetBottom': table_encryption.convert_float(obj.ConquestMapBoundaryOffsetBottom(), password),
        'ConquestMapCenterOffsetX': table_encryption.convert_float(obj.ConquestMapCenterOffsetX(), password),
        'ConquestMapCenterOffsetY': table_encryption.convert_float(obj.ConquestMapCenterOffsetY(), password),
        'CameraAngle': table_encryption.convert_float(obj.CameraAngle(), password),
        'CameraZoomMax': table_encryption.convert_float(obj.CameraZoomMax(), password),
        'CameraZoomMin': table_encryption.convert_float(obj.CameraZoomMin(), password),
        'CameraZoomDefault': table_encryption.convert_float(obj.CameraZoomDefault(), password),
        'ThemaLoadingProgressTime': table_encryption.convert_float(obj.ThemaLoadingProgressTime(), password),
        'MapAllyRotation': table_encryption.convert_float(obj.MapAllyRotation(), password),
        'AniAllyBattleAttack': table_encryption.convert_string(obj.AniAllyBattleAttack(), password),
        'EffectAllyBattleAttack': table_encryption.convert_string(obj.EffectAllyBattleAttack(), password),
        'EffectAllyBattleDamage': table_encryption.convert_string(obj.EffectAllyBattleDamage(), password),
        'AniEnemyBattleAttack': table_encryption.convert_string(obj.AniEnemyBattleAttack(), password),
        'EffectEnemyBattleAttack': table_encryption.convert_string(obj.EffectEnemyBattleAttack(), password),
        'EffectEnemyBattleDamage': table_encryption.convert_string(obj.EffectEnemyBattleDamage(), password),
        'EncounterAllyRotation': table_encryption.convert_float(obj.EncounterAllyRotation(), password),
        'EncounterEnemyRotation': table_encryption.convert_float(obj.EncounterEnemyRotation(), password),
        'EncounterRewardReceiveIndex': table_encryption.convert_int(obj.EncounterRewardReceiveIndex(), password),
    }


def dump_ConstNewbieContentExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'NewbieGachaReleaseDate': table_encryption.convert_string(obj.NewbieGachaReleaseDate(), password),
        'NewbieGachaCheckDays': table_encryption.convert_int(obj.NewbieGachaCheckDays(), password),
        'NewbieGachaTokenGraceTime': table_encryption.convert_int(obj.NewbieGachaTokenGraceTime(), password),
        'NewbieAttendanceReleaseDate': table_encryption.convert_string(obj.NewbieAttendanceReleaseDate(), password),
        'NewbieAttendanceStartableEndDay': table_encryption.convert_int(obj.NewbieAttendanceStartableEndDay(), password),
        'NewbieAttendanceEndDay': table_encryption.convert_int(obj.NewbieAttendanceEndDay(), password),
    }


def dump_ConstStrategyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'HexaMapBoundaryOffset': table_encryption.convert_float(obj.HexaMapBoundaryOffset(), password),
        'HexaMapStartCameraOffset': table_encryption.convert_float(obj.HexaMapStartCameraOffset(), password),
        'CameraZoomMax': table_encryption.convert_float(obj.CameraZoomMax(), password),
        'CameraZoomMin': table_encryption.convert_float(obj.CameraZoomMin(), password),
        'CameraZoomDefault': table_encryption.convert_float(obj.CameraZoomDefault(), password),
        'HealCostType': CurrencyTypes(table_encryption.convert_int(obj.HealCostType(), password)).name,
        'HealCostAmount': [table_encryption.convert_long(obj.HealCostAmount(j), password) for j in range(obj.HealCostAmountLength())],
        'CanHealHpRate': table_encryption.convert_int(obj.CanHealHpRate(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_long(obj.PlayTimeLimitInSeconds(), password),
        'AdventureEchelonCount': table_encryption.convert_int(obj.AdventureEchelonCount(), password),
        'RaidEchelonCount': table_encryption.convert_int(obj.RaidEchelonCount(), password),
        'DefaultEchelonCount': table_encryption.convert_int(obj.DefaultEchelonCount(), password),
        'EventContentEchelonCount': table_encryption.convert_int(obj.EventContentEchelonCount(), password),
        'TimeAttackDungeonEchelonCount': table_encryption.convert_int(obj.TimeAttackDungeonEchelonCount(), password),
        'WorldRaidEchelonCount': table_encryption.convert_int(obj.WorldRaidEchelonCount(), password),
        'TacticSkipClearTimeSeconds': table_encryption.convert_int(obj.TacticSkipClearTimeSeconds(), password),
        'TacticSkipFramePerSecond': table_encryption.convert_int(obj.TacticSkipFramePerSecond(), password),
        'ConquestEchelonCount': table_encryption.convert_int(obj.ConquestEchelonCount(), password),
        'StoryEchelonCount': table_encryption.convert_int(obj.StoryEchelonCount(), password),
        'MultiSweepPresetCount': table_encryption.convert_int(obj.MultiSweepPresetCount(), password),
        'MultiSweepPresetNameMaxLength': table_encryption.convert_int(obj.MultiSweepPresetNameMaxLength(), password),
        'MultiSweepPresetSelectStageMaxCount': table_encryption.convert_int(obj.MultiSweepPresetSelectStageMaxCount(), password),
        'MultiSweepPresetMaxSweepCount': table_encryption.convert_int(obj.MultiSweepPresetMaxSweepCount(), password),
        'MultiSweepPresetSelectParcelMaxCount': table_encryption.convert_int(obj.MultiSweepPresetSelectParcelMaxCount(), password),
    }


def dump_ContentEnterCostReduceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EnterCostReduceGroupId': table_encryption.convert_long(obj.EnterCostReduceGroupId(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'ReduceEnterCostType': ParcelType(table_encryption.convert_int(obj.ReduceEnterCostType(), password)).name,
        'ReduceEnterCostId': table_encryption.convert_long(obj.ReduceEnterCostId(), password),
        'ReduceAmount': table_encryption.convert_long(obj.ReduceAmount(), password),
    }


def dump_ContentsFeverExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ConditionContent': FeverBattleType(table_encryption.convert_int(obj.ConditionContent(), password)).name,
        'SkillFeverCheckCondition': SkillPriorityCheckTarget(table_encryption.convert_int(obj.SkillFeverCheckCondition(), password)).name,
        'SkillCostFever': table_encryption.convert_long(obj.SkillCostFever(), password),
        'FeverStartTime': table_encryption.convert_long(obj.FeverStartTime(), password),
        'FeverDurationTime': table_encryption.convert_long(obj.FeverDurationTime(), password),
    }


def dump_ContentSpoilerPopupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'SpoilerPopupTitle': table_encryption.convert_string(obj.SpoilerPopupTitle(), password),
        'SpoilerPopupDescription': table_encryption.convert_string(obj.SpoilerPopupDescription(), password),
        'IsWarningPopUp': obj.IsWarningPopUp(),
        'ConditionScenarioModeId': table_encryption.convert_long(obj.ConditionScenarioModeId(), password),
    }


def dump_CostumeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CostumeGroupId': table_encryption.convert_long(obj.CostumeGroupId(), password),
        'CostumeUniqueId': table_encryption.convert_long(obj.CostumeUniqueId(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'IsDefault': obj.IsDefault(),
        'CollectionVisible': obj.CollectionVisible(),
        'ReleaseDate': table_encryption.convert_string(obj.ReleaseDate(), password),
        'CollectionVisibleStartDate': table_encryption.convert_string(obj.CollectionVisibleStartDate(), password),
        'CollectionVisibleEndDate': table_encryption.convert_string(obj.CollectionVisibleEndDate(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'CharacterSkillListGroupId': table_encryption.convert_long(obj.CharacterSkillListGroupId(), password),
        'SpineResourceName': table_encryption.convert_string(obj.SpineResourceName(), password),
        'SpineResourceNameDiorama': table_encryption.convert_string(obj.SpineResourceNameDiorama(), password),
        'SpineResourceNameDioramaForFormConversion': [table_encryption.convert_string(obj.SpineResourceNameDioramaForFormConversion(j), password) for j in range(obj.SpineResourceNameDioramaForFormConversionLength())],
        'EntityMaterialType': EntityMaterialType(table_encryption.convert_int(obj.EntityMaterialType_(), password)).name,
        'ModelPrefabName': table_encryption.convert_string(obj.ModelPrefabName(), password),
        'CafeModelPrefabName': table_encryption.convert_string(obj.CafeModelPrefabName(), password),
        'EchelonModelPrefabName': table_encryption.convert_string(obj.EchelonModelPrefabName(), password),
        'StrategyModelPrefabName': table_encryption.convert_string(obj.StrategyModelPrefabName(), password),
        'TextureDir': table_encryption.convert_string(obj.TextureDir(), password),
        'CollectionTexturePath': table_encryption.convert_string(obj.CollectionTexturePath(), password),
        'CollectionBGTexturePath': table_encryption.convert_string(obj.CollectionBGTexturePath(), password),
        'CombatStyleTexturePath': table_encryption.convert_string(obj.CombatStyleTexturePath(), password),
        'UseObjectHPBAR': obj.UseObjectHPBAR(),
        'TextureBoss': table_encryption.convert_string(obj.TextureBoss(), password),
        'TextureSkillCard': [table_encryption.convert_string(obj.TextureSkillCard(j), password) for j in range(obj.TextureSkillCardLength())],
        'InformationPacel': table_encryption.convert_string(obj.InformationPacel(), password),
        'AnimationSSR': table_encryption.convert_string(obj.AnimationSSR(), password),
        'EnterStrategyAnimationName': table_encryption.convert_string(obj.EnterStrategyAnimationName(), password),
        'AnimationValidator': obj.AnimationValidator(),
        'CharacterVoiceGroupId': table_encryption.convert_long(obj.CharacterVoiceGroupId(), password),
        'ShowObjectHpStatus': obj.ShowObjectHpStatus(),
    }


def dump_CouponStuffExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StuffId': table_encryption.convert_long(obj.StuffId(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'LimitAmount': table_encryption.convert_int(obj.LimitAmount(), password),
        'CouponStuffNameLocalizeKey': table_encryption.convert_string(obj.CouponStuffNameLocalizeKey(), password),
    }


def dump_CurrencyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'CurrencyType': CurrencyTypes(table_encryption.convert_int(obj.CurrencyType(), password)).name,
        'CurrencyName': table_encryption.convert_string(obj.CurrencyName(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'AutoChargeMsc': table_encryption.convert_int(obj.AutoChargeMsc(), password),
        'AutoChargeAmount': table_encryption.convert_int(obj.AutoChargeAmount(), password),
        'CurrencyOverChargeType': CurrencyOverChargeType(table_encryption.convert_int(obj.CurrencyOverChargeType_(), password)).name,
        'CurrencyAdditionalChargeType': CurrencyAdditionalChargeType(table_encryption.convert_int(obj.CurrencyAdditionalChargeType_(), password)).name,
        'ChargeLimit': table_encryption.convert_long(obj.ChargeLimit(), password),
        'OverChargeLimit': table_encryption.convert_long(obj.OverChargeLimit(), password),
        'SpriteName': table_encryption.convert_string(obj.SpriteName(), password),
        'DailyRefillType': DailyRefillType(table_encryption.convert_int(obj.DailyRefillType_(), password)).name,
        'DailyRefillAmount': table_encryption.convert_long(obj.DailyRefillAmount(), password),
        'DailyRefillTime': [table_encryption.convert_long(obj.DailyRefillTime(j), password) for j in range(obj.DailyRefillTimeLength())],
        'ExpirationDateTime': table_encryption.convert_string(obj.ExpirationDateTime(), password),
        'ExpirationNotifyDateIn': table_encryption.convert_int(obj.ExpirationNotifyDateIn(), password),
        'ExpiryChangeParcelType': ParcelType(table_encryption.convert_int(obj.ExpiryChangeParcelType(), password)).name,
        'ExpiryChangeId': table_encryption.convert_long(obj.ExpiryChangeId(), password),
        'ExpiryChangeAmount': table_encryption.convert_long(obj.ExpiryChangeAmount(), password),
    }


def dump_DefaultCharacterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'FavoriteCharacter': obj.FavoriteCharacter(),
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Exp': table_encryption.convert_int(obj.Exp(), password),
        'FavorExp': table_encryption.convert_int(obj.FavorExp(), password),
        'FavorRank': table_encryption.convert_int(obj.FavorRank(), password),
        'StarGrade': table_encryption.convert_int(obj.StarGrade(), password),
        'ExSkillLevel': table_encryption.convert_int(obj.ExSkillLevel(), password),
        'PassiveSkillLevel': table_encryption.convert_int(obj.PassiveSkillLevel(), password),
        'ExtraPassiveSkillLevel': table_encryption.convert_int(obj.ExtraPassiveSkillLevel(), password),
        'CommonSkillLevel': table_encryption.convert_int(obj.CommonSkillLevel(), password),
        'LeaderSkillLevel': table_encryption.convert_int(obj.LeaderSkillLevel(), password),
    }


def dump_DefaultEchelonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EchlonId': table_encryption.convert_int(obj.EchlonId(), password),
        'LeaderId': table_encryption.convert_long(obj.LeaderId(), password),
        'MainId': [table_encryption.convert_long(obj.MainId(j), password) for j in range(obj.MainIdLength())],
        'SupportId': [table_encryption.convert_long(obj.SupportId(j), password) for j in range(obj.SupportIdLength())],
        'TssId': table_encryption.convert_long(obj.TssId(), password),
    }


def dump_DefaultFurnitureExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Location': FurnitureLocation(table_encryption.convert_int(obj.Location(), password)).name,
        'PositionX': table_encryption.convert_float(obj.PositionX(), password),
        'PositionY': table_encryption.convert_float(obj.PositionY(), password),
        'Rotation': table_encryption.convert_float(obj.Rotation(), password),
    }


def dump_DefaultMailExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeCodeId': table_encryption.convert_uint(obj.LocalizeCodeId(), password),
        'MailType': MailType(table_encryption.convert_int(obj.MailType_(), password)).name,
        'MailSendPeriodFrom': table_encryption.convert_string(obj.MailSendPeriodFrom(), password),
        'MailSendPeriodTo': table_encryption.convert_string(obj.MailSendPeriodTo(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_DefaultParcelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'ParcelAmount': table_encryption.convert_long(obj.ParcelAmount(), password),
    }


def dump_DuplicateBonusExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ItemCategory': ItemCategory(table_encryption.convert_int(obj.ItemCategory_(), password)).name,
        'ItemId': table_encryption.convert_long(obj.ItemId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
    }


def dump_EchelonConstraintExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'IsWhiteList': obj.IsWhiteList(),
        'CharacterId': [table_encryption.convert_long(obj.CharacterId(j), password) for j in range(obj.CharacterIdLength())],
        'PersonalityId': [table_encryption.convert_long(obj.PersonalityId(j), password) for j in range(obj.PersonalityIdLength())],
        'WeaponType': WeaponType(table_encryption.convert_int(obj.WeaponType_(), password)).name,
        'School': School(table_encryption.convert_int(obj.School_(), password)).name,
        'Club': Club(table_encryption.convert_int(obj.Club_(), password)).name,
        'Role': TacticRole(table_encryption.convert_int(obj.Role(), password)).name,
    }


def dump_EliminateRaidRankingRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RankingRewardGroupId': table_encryption.convert_long(obj.RankingRewardGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RankStart': table_encryption.convert_long(obj.RankStart(), password),
        'RankEnd': table_encryption.convert_long(obj.RankEnd(), password),
        'PercentRankStart': table_encryption.convert_long(obj.PercentRankStart(), password),
        'PercentRankEnd': table_encryption.convert_long(obj.PercentRankEnd(), password),
        'Tier': table_encryption.convert_int(obj.Tier(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelUniqueId': [table_encryption.convert_long(obj.RewardParcelUniqueId(j), password) for j in range(obj.RewardParcelUniqueIdLength())],
        'RewardParcelUniqueName': [table_encryption.convert_string(obj.RewardParcelUniqueName(j), password) for j in range(obj.RewardParcelUniqueNameLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EliminateRaidSeasonManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'SeasonDisplay': table_encryption.convert_long(obj.SeasonDisplay(), password),
        'SeasonStartData': table_encryption.convert_string(obj.SeasonStartData(), password),
        'SeasonEndData': table_encryption.convert_string(obj.SeasonEndData(), password),
        'SettlementEndDate': table_encryption.convert_string(obj.SettlementEndDate(), password),
        'LobbyTableBGPath': table_encryption.convert_string(obj.LobbyTableBGPath(), password),
        'LobbyScreenBGPath': table_encryption.convert_string(obj.LobbyScreenBGPath(), password),
        'OpenRaidBossGroup01': table_encryption.convert_string(obj.OpenRaidBossGroup01(), password),
        'OpenRaidBossGroup02': table_encryption.convert_string(obj.OpenRaidBossGroup02(), password),
        'OpenRaidBossGroup03': table_encryption.convert_string(obj.OpenRaidBossGroup03(), password),
        'RankingRewardGroupId': table_encryption.convert_long(obj.RankingRewardGroupId(), password),
        'MaxSeasonRewardGauage': table_encryption.convert_int(obj.MaxSeasonRewardGauage(), password),
        'StackedSeasonRewardGauge': [table_encryption.convert_long(obj.StackedSeasonRewardGauge(j), password) for j in range(obj.StackedSeasonRewardGaugeLength())],
        'SeasonRewardId': [table_encryption.convert_long(obj.SeasonRewardId(j), password) for j in range(obj.SeasonRewardIdLength())],
        'LimitedRewardIdNormal': table_encryption.convert_long(obj.LimitedRewardIdNormal(), password),
        'LimitedRewardIdHard': table_encryption.convert_long(obj.LimitedRewardIdHard(), password),
        'LimitedRewardIdVeryhard': table_encryption.convert_long(obj.LimitedRewardIdVeryhard(), password),
        'LimitedRewardIdHardcore': table_encryption.convert_long(obj.LimitedRewardIdHardcore(), password),
        'LimitedRewardIdExtreme': table_encryption.convert_long(obj.LimitedRewardIdExtreme(), password),
        'LimitedRewardIdInsane': table_encryption.convert_long(obj.LimitedRewardIdInsane(), password),
        'LimitedRewardIdTorment': table_encryption.convert_long(obj.LimitedRewardIdTorment(), password),
    }


def dump_EliminateRaidStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'UseBossIndex': obj.UseBossIndex(),
        'UseBossAIPhaseSync': obj.UseBossAIPhaseSync(),
        'RaidBossGroup': table_encryption.convert_string(obj.RaidBossGroup(), password),
        'RaidEnterCostType': ParcelType(table_encryption.convert_int(obj.RaidEnterCostType(), password)).name,
        'RaidEnterCostId': table_encryption.convert_long(obj.RaidEnterCostId(), password),
        'RaidEnterCostAmount': table_encryption.convert_int(obj.RaidEnterCostAmount(), password),
        'BossSpinePath': table_encryption.convert_string(obj.BossSpinePath(), password),
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'BGPath': table_encryption.convert_string(obj.BGPath(), password),
        'RaidCharacterId': table_encryption.convert_long(obj.RaidCharacterId(), password),
        'BossCharacterId': [table_encryption.convert_long(obj.BossCharacterId(j), password) for j in range(obj.BossCharacterIdLength())],
        'Difficulty': Difficulty(table_encryption.convert_int(obj.Difficulty_(), password)).name,
        'IsOpen': obj.IsOpen(),
        'MaxPlayerCount': table_encryption.convert_long(obj.MaxPlayerCount(), password),
        'RaidRoomLifeTime': table_encryption.convert_int(obj.RaidRoomLifeTime(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'GroundDevName': table_encryption.convert_string(obj.GroundDevName(), password),
        'EnterTimeLine': table_encryption.convert_string(obj.EnterTimeLine(), password),
        'TacticEnvironment': TacticEnvironment(table_encryption.convert_int(obj.TacticEnvironment_(), password)).name,
        'DefaultClearScore': table_encryption.convert_long(obj.DefaultClearScore(), password),
        'MaximumScore': table_encryption.convert_long(obj.MaximumScore(), password),
        'PerSecondMinusScore': table_encryption.convert_long(obj.PerSecondMinusScore(), password),
        'HPPercentScore': table_encryption.convert_long(obj.HPPercentScore(), password),
        'MinimumAcquisitionScore': table_encryption.convert_long(obj.MinimumAcquisitionScore(), password),
        'MaximumAcquisitionScore': table_encryption.convert_long(obj.MaximumAcquisitionScore(), password),
        'RaidRewardGroupId': table_encryption.convert_long(obj.RaidRewardGroupId(), password),
        'BattleReadyTimelinePath': [table_encryption.convert_string(obj.BattleReadyTimelinePath(j), password) for j in range(obj.BattleReadyTimelinePathLength())],
        'BattleReadyTimelinePhaseStart': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseStart(j), password) for j in range(obj.BattleReadyTimelinePhaseStartLength())],
        'BattleReadyTimelinePhaseEnd': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseEnd(j), password) for j in range(obj.BattleReadyTimelinePhaseEndLength())],
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'PhaseChangeTimelinePath': table_encryption.convert_string(obj.PhaseChangeTimelinePath(), password),
        'TimeLinePhase': table_encryption.convert_long(obj.TimeLinePhase(), password),
        'EnterScenarioKey': table_encryption.convert_uint(obj.EnterScenarioKey(), password),
        'ClearScenarioKey': table_encryption.convert_uint(obj.ClearScenarioKey(), password),
        'ShowSkillCard': obj.ShowSkillCard(),
        'BossBGInfoKey': table_encryption.convert_uint(obj.BossBGInfoKey(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_EliminateRaidStageLimitedRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LimitedRewardId': table_encryption.convert_long(obj.LimitedRewardId(), password),
        'LimitedRewardParcelType': [ParcelType(table_encryption.convert_int(obj.LimitedRewardParcelType(j), password)).name for j in range(obj.LimitedRewardParcelTypeLength())],
        'LimitedRewardParcelUniqueId': [table_encryption.convert_long(obj.LimitedRewardParcelUniqueId(j), password) for j in range(obj.LimitedRewardParcelUniqueIdLength())],
        'LimitedRewardAmount': [table_encryption.convert_long(obj.LimitedRewardAmount(j), password) for j in range(obj.LimitedRewardAmountLength())],
    }


def dump_EliminateRaidStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'IsClearStageRewardHideInfo': obj.IsClearStageRewardHideInfo(),
        'ClearStageRewardProb': table_encryption.convert_long(obj.ClearStageRewardProb(), password),
        'ClearStageRewardParcelType': ParcelType(table_encryption.convert_int(obj.ClearStageRewardParcelType(), password)).name,
        'ClearStageRewardParcelUniqueID': table_encryption.convert_long(obj.ClearStageRewardParcelUniqueID(), password),
        'ClearStageRewardParcelUniqueName': table_encryption.convert_string(obj.ClearStageRewardParcelUniqueName(), password),
        'ClearStageRewardAmount': table_encryption.convert_long(obj.ClearStageRewardAmount(), password),
    }


def dump_EliminateRaidStageSeasonRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonRewardId': table_encryption.convert_long(obj.SeasonRewardId(), password),
        'SeasonRewardParcelType': [ParcelType(table_encryption.convert_int(obj.SeasonRewardParcelType(j), password)).name for j in range(obj.SeasonRewardParcelTypeLength())],
        'SeasonRewardParcelUniqueId': [table_encryption.convert_long(obj.SeasonRewardParcelUniqueId(j), password) for j in range(obj.SeasonRewardParcelUniqueIdLength())],
        'SeasonRewardParcelUniqueName': [table_encryption.convert_string(obj.SeasonRewardParcelUniqueName(j), password) for j in range(obj.SeasonRewardParcelUniqueNameLength())],
        'SeasonRewardAmount': [table_encryption.convert_long(obj.SeasonRewardAmount(j), password) for j in range(obj.SeasonRewardAmountLength())],
    }


def dump_EmblemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Category': EmblemCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'LocalizeCodeId': table_encryption.convert_uint(obj.LocalizeCodeId(), password),
        'UseAtLocalizeId': table_encryption.convert_long(obj.UseAtLocalizeId(), password),
        'EmblemTextVisible': obj.EmblemTextVisible(),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'EmblemIconPath': table_encryption.convert_string(obj.EmblemIconPath(), password),
        'EmblemIconNumControl': table_encryption.convert_int(obj.EmblemIconNumControl(), password),
        'EmblemIconBGPath': table_encryption.convert_string(obj.EmblemIconBGPath(), password),
        'EmblemBGPathJp': table_encryption.convert_string(obj.EmblemBGPathJp(), password),
        'EmblemBGPathKr': table_encryption.convert_string(obj.EmblemBGPathKr(), password),
        'DisplayType': EmblemDisplayType(table_encryption.convert_int(obj.DisplayType(), password)).name,
        'DisplayStartDate': table_encryption.convert_string(obj.DisplayStartDate(), password),
        'DisplayEndDate': table_encryption.convert_string(obj.DisplayEndDate(), password),
        'DislpayFavorLevel': table_encryption.convert_int(obj.DislpayFavorLevel(), password),
        'CheckPassType': EmblemCheckPassType(table_encryption.convert_int(obj.CheckPassType(), password)).name,
        'EmblemParameter': table_encryption.convert_long(obj.EmblemParameter(), password),
        'CheckPassCount': table_encryption.convert_long(obj.CheckPassCount(), password),
    }


def dump_EmoticonSpecialExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'CharacterUniqueId': table_encryption.convert_long(obj.CharacterUniqueId(), password),
        'Random': table_encryption.convert_string(obj.Random(), password),
    }


def dump_EquipmentExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EquipmentCategory': EquipmentCategory(table_encryption.convert_int(obj.EquipmentCategory_(), password)).name,
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'Wear': obj.Wear(),
        'MaxLevel': table_encryption.convert_int(obj.MaxLevel(), password),
        'RecipeId': table_encryption.convert_int(obj.RecipeId(), password),
        'TierInit': table_encryption.convert_long(obj.TierInit(), password),
        'NextTierEquipment': table_encryption.convert_long(obj.NextTierEquipment(), password),
        'StackableMax': table_encryption.convert_int(obj.StackableMax(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'ImageName': table_encryption.convert_string(obj.ImageName(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
        'CraftQualityTier0': table_encryption.convert_long(obj.CraftQualityTier0(), password),
        'CraftQualityTier1': table_encryption.convert_long(obj.CraftQualityTier1(), password),
        'CraftQualityTier2': table_encryption.convert_long(obj.CraftQualityTier2(), password),
        'ShiftingCraftQuality': table_encryption.convert_long(obj.ShiftingCraftQuality(), password),
        'ShopCategory': [ShopCategoryType(table_encryption.convert_int(obj.ShopCategory(j), password)).name for j in range(obj.ShopCategoryLength())],
        'ShortcutTypeId': table_encryption.convert_long(obj.ShortcutTypeId(), password),
    }


def dump_EquipmentLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_int(obj.Level(), password),
        'TierLevelExp': [table_encryption.convert_long(obj.TierLevelExp(j), password) for j in range(obj.TierLevelExpLength())],
        'TotalExp': [table_encryption.convert_long(obj.TotalExp(j), password) for j in range(obj.TotalExpLength())],
    }


def dump_EquipmentStatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EquipmentId': table_encryption.convert_long(obj.EquipmentId(), password),
        'StatLevelUpType': StatLevelUpType(table_encryption.convert_int(obj.StatLevelUpType_(), password)).name,
        'StatType': [EquipmentOptionType(table_encryption.convert_int(obj.StatType(j), password)).name for j in range(obj.StatTypeLength())],
        'MinStat': [table_encryption.convert_long(obj.MinStat(j), password) for j in range(obj.MinStatLength())],
        'MaxStat': [table_encryption.convert_long(obj.MaxStat(j), password) for j in range(obj.MaxStatLength())],
        'LevelUpInsertLimit': table_encryption.convert_int(obj.LevelUpInsertLimit(), password),
        'LevelUpFeedExp': table_encryption.convert_long(obj.LevelUpFeedExp(), password),
        'LevelUpFeedCostCurrency': CurrencyTypes(table_encryption.convert_int(obj.LevelUpFeedCostCurrency(), password)).name,
        'LevelUpFeedCostAmount': table_encryption.convert_long(obj.LevelUpFeedCostAmount(), password),
        'EquipmentCategory': EquipmentCategory(table_encryption.convert_int(obj.EquipmentCategory_(), password)).name,
        'LevelUpFeedAddExp': table_encryption.convert_long(obj.LevelUpFeedAddExp(), password),
        'DefaultMaxLevel': table_encryption.convert_int(obj.DefaultMaxLevel(), password),
        'TranscendenceMax': table_encryption.convert_int(obj.TranscendenceMax(), password),
        'DamageFactorGroupId': table_encryption.convert_string(obj.DamageFactorGroupId(), password),
    }


def dump_EventContentArchiveBannerOffsetExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'OffsetX': table_encryption.convert_float(obj.OffsetX(), password),
        'OffsetY': table_encryption.convert_float(obj.OffsetY(), password),
        'ScaleX': table_encryption.convert_float(obj.ScaleX(), password),
        'ScaleY': table_encryption.convert_float(obj.ScaleY(), password),
    }


def dump_EventContentBoxGachaElementExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Round': table_encryption.convert_long(obj.Round(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
    }


def dump_EventContentBoxGachaManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Round': table_encryption.convert_long(obj.Round(), password),
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
        'IsLoop': obj.IsLoop(),
    }


def dump_EventContentBoxGachaShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'GroupElementAmount': table_encryption.convert_long(obj.GroupElementAmount(), password),
        'Round': table_encryption.convert_long(obj.Round(), password),
        'IsLegacy': obj.IsLegacy(),
        'IsPrize': obj.IsPrize(),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
    }


def dump_EventContentBuffExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentBuffId': table_encryption.convert_long(obj.EventContentBuffId(), password),
        'IsBuff': obj.IsBuff(),
        'CharacterTag': Tag(table_encryption.convert_int(obj.CharacterTag(), password)).name,
        'EnumType': EventContentBuffFindRule(table_encryption.convert_int(obj.EnumType(), password)).name,
        'EnumTypeValue': [table_encryption.convert_string(obj.EnumTypeValue(j), password) for j in range(obj.EnumTypeValueLength())],
        'SkillGroupId': table_encryption.convert_string(obj.SkillGroupId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'SpriteName': table_encryption.convert_string(obj.SpriteName(), password),
        'BuffDescriptionLocalizeCodeId': table_encryption.convert_string(obj.BuffDescriptionLocalizeCodeId(), password),
    }


def dump_EventContentBuffGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'BuffContentId': table_encryption.convert_long(obj.BuffContentId(), password),
        'BuffGroupId': table_encryption.convert_long(obj.BuffGroupId(), password),
        'BuffGroupNameLocalizeCodeId': table_encryption.convert_string(obj.BuffGroupNameLocalizeCodeId(), password),
        'EventContentBuffId1': table_encryption.convert_long(obj.EventContentBuffId1(), password),
        'BuffNameLocalizeCodeId1': table_encryption.convert_string(obj.BuffNameLocalizeCodeId1(), password),
        'BuffDescriptionIconPath1': table_encryption.convert_string(obj.BuffDescriptionIconPath1(), password),
        'EventContentBuffId2': table_encryption.convert_long(obj.EventContentBuffId2(), password),
        'BuffNameLocalizeCodeId2': table_encryption.convert_string(obj.BuffNameLocalizeCodeId2(), password),
        'BuffDescriptionIconPath2': table_encryption.convert_string(obj.BuffDescriptionIconPath2(), password),
        'EventContentDebuffId': table_encryption.convert_long(obj.EventContentDebuffId(), password),
        'DebuffNameLocalizeCodeId': table_encryption.convert_string(obj.DebuffNameLocalizeCodeId(), password),
        'DeBuffDescriptionIconPath': table_encryption.convert_string(obj.DeBuffDescriptionIconPath(), password),
        'BuffGroupProb': table_encryption.convert_long(obj.BuffGroupProb(), password),
    }


def dump_EventContentCardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CardGroupId': table_encryption.convert_int(obj.CardGroupId(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'BackIconPath': table_encryption.convert_string(obj.BackIconPath(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
    }


def dump_EventContentCardShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'CostGoodsId': table_encryption.convert_long(obj.CostGoodsId(), password),
        'CardGroupId': table_encryption.convert_int(obj.CardGroupId(), password),
        'IsLegacy': obj.IsLegacy(),
        'RefreshGroup': table_encryption.convert_int(obj.RefreshGroup(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'ProbWeight1': table_encryption.convert_int(obj.ProbWeight1(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EventContentChangeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ChangeCount': table_encryption.convert_long(obj.ChangeCount(), password),
        'IsLast': obj.IsLast(),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
        'ChangeCostType': ParcelType(table_encryption.convert_int(obj.ChangeCostType(), password)).name,
        'ChangeCostId': table_encryption.convert_long(obj.ChangeCostId(), password),
        'ChangeCostAmount': table_encryption.convert_int(obj.ChangeCostAmount(), password),
    }


def dump_EventContentChangeScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ChangeType': EventChangeType(table_encryption.convert_int(obj.ChangeType(), password)).name,
        'ChangeCount': table_encryption.convert_long(obj.ChangeCount(), password),
        'ScenarioGroupId': table_encryption.convert_long(obj.ScenarioGroupId(), password),
    }


def dump_EventContentCharacterBonusExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'EventContentItemType': [EventContentItemType(table_encryption.convert_int(obj.EventContentItemType_(j), password)).name for j in range(obj.EventContentItemTypeLength())],
        'BonusPercentage': [table_encryption.convert_long(obj.BonusPercentage(j), password) for j in range(obj.BonusPercentageLength())],
    }


def dump_EventContentCollectionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'UnlockConditionType': CollectionUnlockType(table_encryption.convert_int(obj.UnlockConditionType(), password)).name,
        'UnlockConditionParameter': [table_encryption.convert_long(obj.UnlockConditionParameter(j), password) for j in range(obj.UnlockConditionParameterLength())],
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'UnlockConditionCount': table_encryption.convert_long(obj.UnlockConditionCount(), password),
        'IsObject': obj.IsObject(),
        'IsObjectOnFullResource': obj.IsObjectOnFullResource(),
        'IsHorizon': obj.IsHorizon(),
        'EmblemResource': table_encryption.convert_string(obj.EmblemResource(), password),
        'ThumbResource': table_encryption.convert_string(obj.ThumbResource(), password),
        'FullResource': table_encryption.convert_string(obj.FullResource(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'SubNameLocalizeCodeId': table_encryption.convert_string(obj.SubNameLocalizeCodeId(), password),
    }


def dump_EventContentCurrencyItemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentItemType': EventContentItemType(table_encryption.convert_int(obj.EventContentItemType_(), password)).name,
        'ItemUniqueId': table_encryption.convert_long(obj.ItemUniqueId(), password),
    }


def dump_EventContentDebuffRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventStageId': table_encryption.convert_long(obj.EventStageId(), password),
        'EventContentItemType': EventContentItemType(table_encryption.convert_int(obj.EventContentItemType_(), password)).name,
        'RewardPercentage': table_encryption.convert_long(obj.RewardPercentage(), password),
    }


def dump_EventContentDiceRaceEffectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentDiceRaceResultType': EventContentDiceRaceResultType(table_encryption.convert_int(obj.EventContentDiceRaceResultType_(), password)).name,
        'IsDiceResult': obj.IsDiceResult(),
        'AniClip': table_encryption.convert_string(obj.AniClip(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
    }


def dump_EventContentDiceRaceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DiceCostGoodsId': table_encryption.convert_long(obj.DiceCostGoodsId(), password),
        'SkipableLap': table_encryption.convert_int(obj.SkipableLap(), password),
        'DiceRacePawnPrefab': table_encryption.convert_string(obj.DiceRacePawnPrefab(), password),
        'IsUsingFixedDice': obj.IsUsingFixedDice(),
        'DiceRaceEventType': [table_encryption.convert_string(obj.DiceRaceEventType(j), password) for j in range(obj.DiceRaceEventTypeLength())],
    }


def dump_EventContentDiceRaceNodeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'NodeId': table_encryption.convert_long(obj.NodeId(), password),
        'EventContentDiceRaceNodeType': EventContentDiceRaceNodeType(table_encryption.convert_int(obj.EventContentDiceRaceNodeType_(), password)).name,
        'MoveForwardTypeArg': table_encryption.convert_int(obj.MoveForwardTypeArg(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_EventContentDiceRaceProbExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentDiceRaceResultType': EventContentDiceRaceResultType(table_encryption.convert_int(obj.EventContentDiceRaceResultType_(), password)).name,
        'CostItemId': table_encryption.convert_long(obj.CostItemId(), password),
        'CostItemAmount': table_encryption.convert_int(obj.CostItemAmount(), password),
        'DiceResult': table_encryption.convert_int(obj.DiceResult(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
    }


def dump_EventContentDiceRaceTotalRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'RewardID': table_encryption.convert_long(obj.RewardID(), password),
        'RequiredLapFinishCount': table_encryption.convert_int(obj.RequiredLapFinishCount(), password),
        'DisplayLapFinishCount': table_encryption.convert_int(obj.DisplayLapFinishCount(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EventContentExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'BgImagePath': table_encryption.convert_string(obj.BgImagePath(), password),
    }


def dump_EventContentFortuneGachaExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FortuneGachaGroupId': table_encryption.convert_int(obj.FortuneGachaGroupId(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
    }


def dump_EventContentFortuneGachaModifyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_int(obj.EventContentId(), password),
        'TargetGrade': table_encryption.convert_int(obj.TargetGrade(), password),
        'ProbModifyStartCount': table_encryption.convert_int(obj.ProbModifyStartCount(), password),
        'UsePrefabName': table_encryption.convert_string(obj.UsePrefabName(), password),
        'BucketImagePath': table_encryption.convert_string(obj.BucketImagePath(), password),
        'ShopBgImagePath': table_encryption.convert_string(obj.ShopBgImagePath(), password),
        'TitleLocalizeKey': table_encryption.convert_string(obj.TitleLocalizeKey(), password),
    }


def dump_EventContentFortuneGachaShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Grade': table_encryption.convert_int(obj.Grade(), password),
        'CostGoodsId': table_encryption.convert_long(obj.CostGoodsId(), password),
        'IsLegacy': obj.IsLegacy(),
        'FortuneGachaGroupId': table_encryption.convert_int(obj.FortuneGachaGroupId(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'ProbModifyValue': table_encryption.convert_int(obj.ProbModifyValue(), password),
        'ProbModifyLimit': table_encryption.convert_int(obj.ProbModifyLimit(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EventContentLobbyMenuExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentType': EventContentType(table_encryption.convert_int(obj.EventContentType_(), password)).name,
        'IconSpriteName': table_encryption.convert_string(obj.IconSpriteName(), password),
        'ButtonText': table_encryption.convert_string(obj.ButtonText(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'IconOffsetX': table_encryption.convert_float(obj.IconOffsetX(), password),
        'IconOffsetY': table_encryption.convert_float(obj.IconOffsetY(), password),
        'ReddotSpriteName': table_encryption.convert_string(obj.ReddotSpriteName(), password),
    }


def dump_EventContentLocationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'PrefabPath': table_encryption.convert_string(obj.PrefabPath(), password),
        'LocationResetScheduleCount': table_encryption.convert_int(obj.LocationResetScheduleCount(), password),
        'ScheduleEventPointCostParcelType': ParcelType(table_encryption.convert_int(obj.ScheduleEventPointCostParcelType(), password)).name,
        'ScheduleEventPointCostParcelId': table_encryption.convert_long(obj.ScheduleEventPointCostParcelId(), password),
        'ScheduleEventPointCostParcelAmount': table_encryption.convert_long(obj.ScheduleEventPointCostParcelAmount(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'InformationGroupId': table_encryption.convert_long(obj.InformationGroupId(), password),
    }


def dump_EventContentLocationRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Location': table_encryption.convert_string(obj.Location(), password),
        'ScheduleGroupId': table_encryption.convert_long(obj.ScheduleGroupId(), password),
        'OrderInGroup': table_encryption.convert_long(obj.OrderInGroup(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProgressTexture': table_encryption.convert_string(obj.ProgressTexture(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'LocationRank': table_encryption.convert_long(obj.LocationRank(), password),
        'FavorExp': table_encryption.convert_long(obj.FavorExp(), password),
        'SecretStoneAmount': table_encryption.convert_long(obj.SecretStoneAmount(), password),
        'SecretStoneProb': table_encryption.convert_long(obj.SecretStoneProb(), password),
        'ExtraFavorExp': table_encryption.convert_long(obj.ExtraFavorExp(), password),
        'ExtraFavorExpProb': table_encryption.convert_long(obj.ExtraFavorExpProb(), password),
        'ExtraRewardParcelType': [ParcelType(table_encryption.convert_int(obj.ExtraRewardParcelType(j), password)).name for j in range(obj.ExtraRewardParcelTypeLength())],
        'ExtraRewardParcelId': [table_encryption.convert_long(obj.ExtraRewardParcelId(j), password) for j in range(obj.ExtraRewardParcelIdLength())],
        'ExtraRewardAmount': [table_encryption.convert_long(obj.ExtraRewardAmount(j), password) for j in range(obj.ExtraRewardAmountLength())],
        'ExtraRewardProb': [table_encryption.convert_long(obj.ExtraRewardProb(j), password) for j in range(obj.ExtraRewardProbLength())],
        'IsExtraRewardDisplayed': [obj.IsExtraRewardDisplayed(j) for j in range(obj.IsExtraRewardDisplayedLength())],
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_EventContentMeetupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'ConditionScenarioGroupId': table_encryption.convert_long(obj.ConditionScenarioGroupId(), password),
        'ConditionType': MeetupConditionType(table_encryption.convert_int(obj.ConditionType(), password)).name,
        'ConditionParameter': [table_encryption.convert_long(obj.ConditionParameter(j), password) for j in range(obj.ConditionParameterLength())],
        'ConditionPrintType': MeetupConditionPrintType(table_encryption.convert_int(obj.ConditionPrintType(), password)).name,
    }


def dump_EventContentMiniEventShortCutExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_int(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'ShorcutContentType': EventTargetType(table_encryption.convert_int(obj.ShorcutContentType(), password)).name,
    }


def dump_EventContentMiniEventTokenExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ItemUniqueId': table_encryption.convert_long(obj.ItemUniqueId(), password),
        'MaximumAmount': table_encryption.convert_long(obj.MaximumAmount(), password),
    }


def dump_EventContentMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'GroupName': table_encryption.convert_string(obj.GroupName(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_uint(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ToastDisplayType': MissionToastDisplayConditionType(table_encryption.convert_int(obj.ToastDisplayType(), password)).name,
        'ToastImagePath': table_encryption.convert_string(obj.ToastImagePath(), password),
        'ViewFlag': obj.ViewFlag(),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'ChallengeStageShortcut': table_encryption.convert_long(obj.ChallengeStageShortcut(), password),
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'IsCompleteExtensionTime': obj.IsCompleteExtensionTime(),
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterTag': [Tag(table_encryption.convert_int(obj.CompleteConditionParameterTag(j), password)).name for j in range(obj.CompleteConditionParameterTagLength())],
        'RewardIcon': table_encryption.convert_string(obj.RewardIcon(), password),
        'CompleteConditionMissionId': [table_encryption.convert_long(obj.CompleteConditionMissionId(j), password) for j in range(obj.CompleteConditionMissionIdLength())],
        'CompleteConditionMissionCount': table_encryption.convert_long(obj.CompleteConditionMissionCount(), password),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
        'ConditionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.ConditionRewardParcelType(j), password)).name for j in range(obj.ConditionRewardParcelTypeLength())],
        'ConditionRewardParcelId': [table_encryption.convert_long(obj.ConditionRewardParcelId(j), password) for j in range(obj.ConditionRewardParcelIdLength())],
        'ConditionRewardAmount': [table_encryption.convert_int(obj.ConditionRewardAmount(j), password) for j in range(obj.ConditionRewardAmountLength())],
    }


def dump_EventContentPlayGuideExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'GuideTitle': table_encryption.convert_string(obj.GuideTitle(), password),
        'GuideImagePath': table_encryption.convert_string(obj.GuideImagePath(), password),
        'GuideText': table_encryption.convert_string(obj.GuideText(), password),
    }


def dump_EventContentScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ReplayDisplayGroup': table_encryption.convert_int(obj.ReplayDisplayGroup(), password),
        'Order': table_encryption.convert_long(obj.Order(), password),
        'RecollectionNumber': table_encryption.convert_long(obj.RecollectionNumber(), password),
        'IsRecollection': obj.IsRecollection(),
        'IsMeetup': obj.IsMeetup(),
        'IsOmnibus': obj.IsOmnibus(),
        'ScenarioGroupId': [table_encryption.convert_long(obj.ScenarioGroupId(j), password) for j in range(obj.ScenarioGroupIdLength())],
        'ScenarioConditionType': EventContentScenarioConditionType(table_encryption.convert_int(obj.ScenarioConditionType(), password)).name,
        'ConditionAmount': table_encryption.convert_long(obj.ConditionAmount(), password),
        'ConditionEventContentId': table_encryption.convert_long(obj.ConditionEventContentId(), password),
        'ClearedScenarioGroupId': table_encryption.convert_long(obj.ClearedScenarioGroupId(), password),
        'RecollectionSummaryLocalizeScenarioId': table_encryption.convert_uint(obj.RecollectionSummaryLocalizeScenarioId(), password),
        'RecollectionResource': table_encryption.convert_string(obj.RecollectionResource(), password),
        'IsRecollectionHorizon': obj.IsRecollectionHorizon(),
        'CostParcelType': ParcelType(table_encryption.convert_int(obj.CostParcelType(), password)).name,
        'CostId': table_encryption.convert_long(obj.CostId(), password),
        'CostAmount': table_encryption.convert_int(obj.CostAmount(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardId': [table_encryption.convert_long(obj.RewardId(j), password) for j in range(obj.RewardIdLength())],
        'RewardAmount': [table_encryption.convert_int(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_EventContentSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'OriginalEventContentId': table_encryption.convert_long(obj.OriginalEventContentId(), password),
        'IsReturn': obj.IsReturn(),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventContentType': EventContentType(table_encryption.convert_int(obj.EventContentType_(), password)).name,
        'OpenConditionContent': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionContent_(), password)).name,
        'EventDisplay': obj.EventDisplay(),
        'IconOrder': table_encryption.convert_int(obj.IconOrder(), password),
        'SubEventType': SubEventType(table_encryption.convert_int(obj.SubEventType_(), password)).name,
        'SubEvent': obj.SubEvent(),
        'EventItemId': table_encryption.convert_long(obj.EventItemId(), password),
        'MainEventId': table_encryption.convert_long(obj.MainEventId(), password),
        'EventChangeOpenCondition': table_encryption.convert_long(obj.EventChangeOpenCondition(), password),
        'BeforehandExposedTime': table_encryption.convert_string(obj.BeforehandExposedTime(), password),
        'EventContentOpenTime': table_encryption.convert_string(obj.EventContentOpenTime(), password),
        'EventContentCloseTime': table_encryption.convert_string(obj.EventContentCloseTime(), password),
        'ExtensionTime': table_encryption.convert_string(obj.ExtensionTime(), password),
        'MainIconParcelPath': table_encryption.convert_string(obj.MainIconParcelPath(), password),
        'SubIconParcelPath': table_encryption.convert_string(obj.SubIconParcelPath(), password),
        'BeforehandBgImagePath': table_encryption.convert_string(obj.BeforehandBgImagePath(), password),
        'MinigamePrologScenarioGroupId': table_encryption.convert_long(obj.MinigamePrologScenarioGroupId(), password),
        'BeforehandScenarioGroupId': [table_encryption.convert_long(obj.BeforehandScenarioGroupId(j), password) for j in range(obj.BeforehandScenarioGroupIdLength())],
        'MainBannerImagePath': table_encryption.convert_string(obj.MainBannerImagePath(), password),
        'MainBgImagePath': table_encryption.convert_string(obj.MainBgImagePath(), password),
        'ShiftTriggerStageId': table_encryption.convert_long(obj.ShiftTriggerStageId(), password),
        'ShiftMainBgImagePath': table_encryption.convert_string(obj.ShiftMainBgImagePath(), password),
        'MinigameLobbyPrefabName': table_encryption.convert_string(obj.MinigameLobbyPrefabName(), password),
        'MinigameVictoryPrefabName': table_encryption.convert_string(obj.MinigameVictoryPrefabName(), password),
        'MinigameMissionBgPrefabName': table_encryption.convert_string(obj.MinigameMissionBgPrefabName(), password),
        'MinigameMissionBgImagePath': table_encryption.convert_string(obj.MinigameMissionBgImagePath(), password),
        'CardBgImagePath': table_encryption.convert_string(obj.CardBgImagePath(), password),
        'EventAssist': obj.EventAssist(),
        'EventContentReleaseType': EventContentReleaseType(table_encryption.convert_int(obj.EventContentReleaseType_(), password)).name,
        'EventContentStageRewardIdPermanent': table_encryption.convert_long(obj.EventContentStageRewardIdPermanent(), password),
        'RewardTagPermanent': RewardTag(table_encryption.convert_int(obj.RewardTagPermanent(), password)).name,
        'MiniEventShortCutScenarioModeId': table_encryption.convert_long(obj.MiniEventShortCutScenarioModeId(), password),
    }


def dump_EventContentShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'SalePeriodFrom': table_encryption.convert_string(obj.SalePeriodFrom(), password),
        'SalePeriodTo': table_encryption.convert_string(obj.SalePeriodTo(), password),
        'PurchaseCooltimeMin': table_encryption.convert_long(obj.PurchaseCooltimeMin(), password),
        'PurchaseCountLimit': table_encryption.convert_long(obj.PurchaseCountLimit(), password),
        'PurchaseCountResetType': PurchaseCountResetType(table_encryption.convert_int(obj.PurchaseCountResetType_(), password)).name,
        'BuyReportEventName': table_encryption.convert_string(obj.BuyReportEventName(), password),
        'RestrictBuyWhenInventoryFull': obj.RestrictBuyWhenInventoryFull(),
    }


def dump_EventContentShopInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'LocalizeCode': table_encryption.convert_uint(obj.LocalizeCode(), password),
        'CostParcelType': [ParcelType(table_encryption.convert_int(obj.CostParcelType(j), password)).name for j in range(obj.CostParcelTypeLength())],
        'CostParcelId': [table_encryption.convert_long(obj.CostParcelId(j), password) for j in range(obj.CostParcelIdLength())],
        'IsRefresh': obj.IsRefresh(),
        'IsSoldOutDimmed': obj.IsSoldOutDimmed(),
        'AutoRefreshCoolTime': table_encryption.convert_long(obj.AutoRefreshCoolTime(), password),
        'RefreshAbleCount': table_encryption.convert_long(obj.RefreshAbleCount(), password),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'OpenPeriodFrom': table_encryption.convert_string(obj.OpenPeriodFrom(), password),
        'OpenPeriodTo': table_encryption.convert_string(obj.OpenPeriodTo(), password),
        'ShopProductUpdateDate': table_encryption.convert_string(obj.ShopProductUpdateDate(), password),
    }


def dump_EventContentShopRefreshExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'RefreshGroup': table_encryption.convert_int(obj.RefreshGroup(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'BuyReportEventName': table_encryption.convert_string(obj.BuyReportEventName(), password),
    }


def dump_EventContentSpecialOperationsExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'PointItemId': table_encryption.convert_long(obj.PointItemId(), password),
    }


def dump_EventContentSpineDialogOffsetExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentType': EventContentType(table_encryption.convert_int(obj.EventContentType_(), password)).name,
        'CostumeUniqueId': table_encryption.convert_long(obj.CostumeUniqueId(), password),
        'SpineOffsetX': table_encryption.convert_float(obj.SpineOffsetX(), password),
        'SpineOffsetY': table_encryption.convert_float(obj.SpineOffsetY(), password),
        'DialogOffsetX': table_encryption.convert_float(obj.DialogOffsetX(), password),
        'DialogOffsetY': table_encryption.convert_float(obj.DialogOffsetY(), password),
    }


def dump_EventContentSpoilerPopupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'SpoilerPopupTitle': table_encryption.convert_string(obj.SpoilerPopupTitle(), password),
        'SpoilerPopupDescription': table_encryption.convert_string(obj.SpoilerPopupDescription(), password),
        'IsWarningPopUp': obj.IsWarningPopUp(),
        'ConditionScenarioModeId': table_encryption.convert_long(obj.ConditionScenarioModeId(), password),
    }


def dump_EventContentStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'StageDifficulty': StageDifficulty(table_encryption.convert_int(obj.StageDifficulty_(), password)).name,
        'StageNumber': table_encryption.convert_string(obj.StageNumber(), password),
        'StageDisplay': table_encryption.convert_int(obj.StageDisplay(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'OpenDate': table_encryption.convert_long(obj.OpenDate(), password),
        'OpenEventPoint': table_encryption.convert_long(obj.OpenEventPoint(), password),
        'OpenConditionScenarioPermanentSubEventId': table_encryption.convert_long(obj.OpenConditionScenarioPermanentSubEventId(), password),
        'PrevStageSubEventId': table_encryption.convert_long(obj.PrevStageSubEventId(), password),
        'OpenConditionScenarioId': table_encryption.convert_long(obj.OpenConditionScenarioId(), password),
        'OpenConditionContentType': EventContentType(table_encryption.convert_int(obj.OpenConditionContentType(), password)).name,
        'OpenConditionContentId': table_encryption.convert_long(obj.OpenConditionContentId(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'StageEnterEchelonCount': table_encryption.convert_int(obj.StageEnterEchelonCount(), password),
        'StarConditionTacticRankSCount': table_encryption.convert_long(obj.StarConditionTacticRankSCount(), password),
        'StarConditionTurnCount': table_encryption.convert_long(obj.StarConditionTurnCount(), password),
        'EnterScenarioGroupId': [table_encryption.convert_long(obj.EnterScenarioGroupId(j), password) for j in range(obj.EnterScenarioGroupIdLength())],
        'ClearScenarioGroupId': [table_encryption.convert_long(obj.ClearScenarioGroupId(j), password) for j in range(obj.ClearScenarioGroupIdLength())],
        'StrategyMap': table_encryption.convert_string(obj.StrategyMap(), password),
        'StrategyMapBG': table_encryption.convert_string(obj.StrategyMapBG(), password),
        'EventContentStageRewardId': table_encryption.convert_long(obj.EventContentStageRewardId(), password),
        'MaxTurn': table_encryption.convert_int(obj.MaxTurn(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'BgmId': table_encryption.convert_string(obj.BgmId(), password),
        'StrategyEnvironment': StrategyEnvironment(table_encryption.convert_int(obj.StrategyEnvironment_(), password)).name,
        'GroundID': table_encryption.convert_long(obj.GroundID(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'InstantClear': obj.InstantClear(),
        'BuffContentId': table_encryption.convert_long(obj.BuffContentId(), password),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'ChallengeDisplay': obj.ChallengeDisplay(),
        'StarGoal': [StarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'IsDefeatBattle': obj.IsDefeatBattle(),
        'StageHint': table_encryption.convert_uint(obj.StageHint(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_EventContentStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_EventContentStageTotalRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'RequiredEventItemAmount': table_encryption.convert_long(obj.RequiredEventItemAmount(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EventContentZoneExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'OriginalZoneId': table_encryption.convert_long(obj.OriginalZoneId(), password),
        'LocationId': table_encryption.convert_long(obj.LocationId(), password),
        'LocationRank': table_encryption.convert_long(obj.LocationRank(), password),
        'EventPointForLocationRank': table_encryption.convert_long(obj.EventPointForLocationRank(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'StudentVisitProb': [table_encryption.convert_long(obj.StudentVisitProb(j), password) for j in range(obj.StudentVisitProbLength())],
        'RewardGroupId': table_encryption.convert_long(obj.RewardGroupId(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
        'WhiteListTags': [Tag(table_encryption.convert_int(obj.WhiteListTags(j), password)).name for j in range(obj.WhiteListTagsLength())],
    }


def dump_EventContentZoneVisitRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentLocationId': table_encryption.convert_long(obj.EventContentLocationId(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'CharacterDevName': table_encryption.convert_string(obj.CharacterDevName(), password),
        'VisitRewardParcelType': [ParcelType(table_encryption.convert_int(obj.VisitRewardParcelType(j), password)).name for j in range(obj.VisitRewardParcelTypeLength())],
        'VisitRewardParcelId': [table_encryption.convert_long(obj.VisitRewardParcelId(j), password) for j in range(obj.VisitRewardParcelIdLength())],
        'VisitRewardAmount': [table_encryption.convert_long(obj.VisitRewardAmount(j), password) for j in range(obj.VisitRewardAmountLength())],
        'VisitRewardProb': [table_encryption.convert_long(obj.VisitRewardProb(j), password) for j in range(obj.VisitRewardProbLength())],
    }


def dump_FarmingDungeonLocationManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FarmingDungeonLocationId': table_encryption.convert_long(obj.FarmingDungeonLocationId(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'WeekDungeonType': WeekDungeonType(table_encryption.convert_int(obj.WeekDungeonType_(), password)).name,
        'SchoolDungeonType': SchoolDungeonType(table_encryption.convert_int(obj.SchoolDungeonType_(), password)).name,
        'Order': table_encryption.convert_long(obj.Order(), password),
        'OpenStartDateTime': table_encryption.convert_string(obj.OpenStartDateTime(), password),
        'OpenEndDateTime': table_encryption.convert_string(obj.OpenEndDateTime(), password),
        'LocationButtonImagePath': table_encryption.convert_string(obj.LocationButtonImagePath(), password),
        'LocalizeCodeTitle': table_encryption.convert_uint(obj.LocalizeCodeTitle(), password),
        'LocalizeCodeInfo': table_encryption.convert_uint(obj.LocalizeCodeInfo(), password),
    }


def dump_FavorLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_long(obj.Level(), password),
        'ExpType': [table_encryption.convert_long(obj.ExpType(j), password) for j in range(obj.ExpTypeLength())],
    }


def dump_FavorLevelRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'FavorLevel': table_encryption.convert_long(obj.FavorLevel(), password),
        'StatType': [EquipmentOptionType(table_encryption.convert_int(obj.StatType(j), password)).name for j in range(obj.StatTypeLength())],
        'StatValue': [table_encryption.convert_long(obj.StatValue(j), password) for j in range(obj.StatValueLength())],
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardAmount': [table_encryption.convert_long(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
    }


def dump_FieldContentStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'AreaId': table_encryption.convert_long(obj.AreaId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'StageDifficulty': StageDifficulty(table_encryption.convert_int(obj.StageDifficulty_(), password)).name,
        'Name': table_encryption.convert_string(obj.Name(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'GroundID': table_encryption.convert_long(obj.GroundID(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'InstantClear': obj.InstantClear(),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'SkipFormationSettings': obj.SkipFormationSettings(),
    }


def dump_FieldContentStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_FieldDateExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'OpenDate': table_encryption.convert_long(obj.OpenDate(), password),
        'DateLocalizeKey': table_encryption.convert_string(obj.DateLocalizeKey(), password),
        'EntrySceneId': table_encryption.convert_long(obj.EntrySceneId(), password),
        'StartConditionType': FieldConditionType(table_encryption.convert_int(obj.StartConditionType(), password)).name,
        'StartConditionId': table_encryption.convert_long(obj.StartConditionId(), password),
        'EndConditionType': FieldConditionType(table_encryption.convert_int(obj.EndConditionType(), password)).name,
        'EndConditionId': table_encryption.convert_long(obj.EndConditionId(), password),
        'OpenConditionStage': table_encryption.convert_long(obj.OpenConditionStage(), password),
        'DateResultSpinePath': table_encryption.convert_string(obj.DateResultSpinePath(), password),
        'DateResultSpineOffsetX': table_encryption.convert_float(obj.DateResultSpineOffsetX(), password),
    }


def dump_FieldEvidenceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'NameLocalizeKey': table_encryption.convert_string(obj.NameLocalizeKey(), password),
        'DescriptionLocalizeKey': table_encryption.convert_string(obj.DescriptionLocalizeKey(), password),
        'DetailLocalizeKey': table_encryption.convert_string(obj.DetailLocalizeKey(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
    }


def dump_FieldInteractionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'FieldDateId': table_encryption.convert_long(obj.FieldDateId(), password),
        'ShowEmoji': obj.ShowEmoji(),
        'KeywordLocalize': table_encryption.convert_string(obj.KeywordLocalize(), password),
        'FieldSeasonId': table_encryption.convert_long(obj.FieldSeasonId(), password),
        'InteractionType': [FieldInteractionType(table_encryption.convert_int(obj.InteractionType(j), password)).name for j in range(obj.InteractionTypeLength())],
        'InteractionId': [table_encryption.convert_long(obj.InteractionId(j), password) for j in range(obj.InteractionIdLength())],
        'ConditionClass': FieldConditionClass(table_encryption.convert_int(obj.ConditionClass(), password)).name,
        'ConditionClassParameters': [table_encryption.convert_long(obj.ConditionClassParameters(j), password) for j in range(obj.ConditionClassParametersLength())],
        'OnceOnly': obj.OnceOnly(),
        'ConditionIndex': [table_encryption.convert_long(obj.ConditionIndex(j), password) for j in range(obj.ConditionIndexLength())],
        'ConditionType': [FieldConditionType(table_encryption.convert_int(obj.ConditionType(j), password)).name for j in range(obj.ConditionTypeLength())],
        'ConditionId': [table_encryption.convert_long(obj.ConditionId(j), password) for j in range(obj.ConditionIdLength())],
        'NegateCondition': [obj.NegateCondition(j) for j in range(obj.NegateConditionLength())],
    }


def dump_FieldKeywordExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'NameLocalizeKey': table_encryption.convert_string(obj.NameLocalizeKey(), password),
        'DescriptionLocalizeKey': table_encryption.convert_string(obj.DescriptionLocalizeKey(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
    }


def dump_FieldMasteryExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'Order': table_encryption.convert_int(obj.Order(), password),
        'ExpAmount': table_encryption.convert_long(obj.ExpAmount(), password),
        'TokenType': ParcelType(table_encryption.convert_int(obj.TokenType(), password)).name,
        'TokenId': table_encryption.convert_long(obj.TokenId(), password),
        'TokenRequirement': table_encryption.convert_long(obj.TokenRequirement(), password),
        'AccomplishmentConditionType': FieldConditionType(table_encryption.convert_int(obj.AccomplishmentConditionType(), password)).name,
        'AccomplishmentConditionId': table_encryption.convert_long(obj.AccomplishmentConditionId(), password),
    }


def dump_FieldMasteryLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Id': [table_encryption.convert_long(obj.Id(j), password) for j in range(obj.IdLength())],
        'Exp': [table_encryption.convert_long(obj.Exp(j), password) for j in range(obj.ExpLength())],
        'TotalExp': [table_encryption.convert_long(obj.TotalExp(j), password) for j in range(obj.TotalExpLength())],
        'RewardId': [table_encryption.convert_long(obj.RewardId(j), password) for j in range(obj.RewardIdLength())],
    }


def dump_FieldMasteryManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FieldSeason': table_encryption.convert_long(obj.FieldSeason(), password),
        'LocalizeEtc': table_encryption.convert_uint(obj.LocalizeEtc(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
        'LevelId': table_encryption.convert_long(obj.LevelId(), password),
    }


def dump_FieldQuestExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'FieldSeasonId': table_encryption.convert_long(obj.FieldSeasonId(), password),
        'IsDaily': obj.IsDaily(),
        'FieldDateId': table_encryption.convert_long(obj.FieldDateId(), password),
        'Opendate': table_encryption.convert_long(obj.Opendate(), password),
        'AssetPath': table_encryption.convert_string(obj.AssetPath(), password),
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'QuestNamKey': table_encryption.convert_uint(obj.QuestNamKey(), password),
        'QuestDescKey': table_encryption.convert_uint(obj.QuestDescKey(), password),
    }


def dump_FieldRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
    }


def dump_FieldSceneExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'DateId': table_encryption.convert_long(obj.DateId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'ArtLevelPath': table_encryption.convert_string(obj.ArtLevelPath(), password),
        'DesignLevelPath': table_encryption.convert_string(obj.DesignLevelPath(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'ConditionalBGMQuestId': [table_encryption.convert_long(obj.ConditionalBGMQuestId(j), password) for j in range(obj.ConditionalBGMQuestIdLength())],
        'BeginConditionalBGMScenarioGroupId': [table_encryption.convert_long(obj.BeginConditionalBGMScenarioGroupId(j), password) for j in range(obj.BeginConditionalBGMScenarioGroupIdLength())],
        'EndConditionalBGMScenarioGroupId': [table_encryption.convert_long(obj.EndConditionalBGMScenarioGroupId(j), password) for j in range(obj.EndConditionalBGMScenarioGroupIdLength())],
        'ConditionalBGMId': [table_encryption.convert_long(obj.ConditionalBGMId(j), password) for j in range(obj.ConditionalBGMIdLength())],
    }


def dump_FieldSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EntryDateId': table_encryption.convert_long(obj.EntryDateId(), password),
        'InstantEntryDateId': table_encryption.convert_long(obj.InstantEntryDateId(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'LobbyBGMChangeStageId': table_encryption.convert_long(obj.LobbyBGMChangeStageId(), password),
        'CharacterIconPath': table_encryption.convert_string(obj.CharacterIconPath(), password),
        'MasteryImagePath': table_encryption.convert_string(obj.MasteryImagePath(), password),
    }


def dump_FieldStoryStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'GroundID': table_encryption.convert_long(obj.GroundID(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'SkipFormationSettings': obj.SkipFormationSettings(),
    }


def dump_FieldTutorialExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'TutorialType': [FieldTutorialType(table_encryption.convert_int(obj.TutorialType(j), password)).name for j in range(obj.TutorialTypeLength())],
        'ConditionType': [FieldConditionType(table_encryption.convert_int(obj.ConditionType(j), password)).name for j in range(obj.ConditionTypeLength())],
        'ConditionId': [table_encryption.convert_long(obj.ConditionId(j), password) for j in range(obj.ConditionIdLength())],
    }


def dump_FieldWorldMapZoneExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'GroupId': table_encryption.convert_int(obj.GroupId(), password),
        'Date': table_encryption.convert_int(obj.Date(), password),
        'OpenConditionType': FieldConditionType(table_encryption.convert_int(obj.OpenConditionType(), password)).name,
        'OpenConditionId': table_encryption.convert_long(obj.OpenConditionId(), password),
        'CloseConditionType': FieldConditionType(table_encryption.convert_int(obj.CloseConditionType(), password)).name,
        'CloseConditionId': table_encryption.convert_long(obj.CloseConditionId(), password),
        'ResultFieldScene': table_encryption.convert_long(obj.ResultFieldScene(), password),
        'FieldStageInteractionId': table_encryption.convert_long(obj.FieldStageInteractionId(), password),
        'LocalizeCode': table_encryption.convert_uint(obj.LocalizeCode(), password),
    }


def dump_FixedEchelonSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FixedEchelonID': table_encryption.convert_long(obj.FixedEchelonID(), password),
        'EchelonSceneSkip': obj.EchelonSceneSkip(),
        'MainLeaderSlot': table_encryption.convert_int(obj.MainLeaderSlot(), password),
        'MainCharacterID': [table_encryption.convert_long(obj.MainCharacterID(j), password) for j in range(obj.MainCharacterIDLength())],
        'MainLevel': [table_encryption.convert_int(obj.MainLevel(j), password) for j in range(obj.MainLevelLength())],
        'MainGrade': [table_encryption.convert_int(obj.MainGrade(j), password) for j in range(obj.MainGradeLength())],
        'MainExSkillLevel': [table_encryption.convert_int(obj.MainExSkillLevel(j), password) for j in range(obj.MainExSkillLevelLength())],
        'MainNoneExSkillLevel': [table_encryption.convert_int(obj.MainNoneExSkillLevel(j), password) for j in range(obj.MainNoneExSkillLevelLength())],
        'MainEquipment1Tier': [table_encryption.convert_int(obj.MainEquipment1Tier(j), password) for j in range(obj.MainEquipment1TierLength())],
        'MainEquipment1Level': [table_encryption.convert_int(obj.MainEquipment1Level(j), password) for j in range(obj.MainEquipment1LevelLength())],
        'MainEquipment2Tier': [table_encryption.convert_int(obj.MainEquipment2Tier(j), password) for j in range(obj.MainEquipment2TierLength())],
        'MainEquipment2Level': [table_encryption.convert_int(obj.MainEquipment2Level(j), password) for j in range(obj.MainEquipment2LevelLength())],
        'MainEquipment3Tier': [table_encryption.convert_int(obj.MainEquipment3Tier(j), password) for j in range(obj.MainEquipment3TierLength())],
        'MainEquipment3Level': [table_encryption.convert_int(obj.MainEquipment3Level(j), password) for j in range(obj.MainEquipment3LevelLength())],
        'MainCharacterWeaponGrade': [table_encryption.convert_int(obj.MainCharacterWeaponGrade(j), password) for j in range(obj.MainCharacterWeaponGradeLength())],
        'MainCharacterWeaponLevel': [table_encryption.convert_int(obj.MainCharacterWeaponLevel(j), password) for j in range(obj.MainCharacterWeaponLevelLength())],
        'MainCharacterGearTier': [table_encryption.convert_int(obj.MainCharacterGearTier(j), password) for j in range(obj.MainCharacterGearTierLength())],
        'MainCharacterGearLevel': [table_encryption.convert_int(obj.MainCharacterGearLevel(j), password) for j in range(obj.MainCharacterGearLevelLength())],
        'SupportCharacterID': [table_encryption.convert_long(obj.SupportCharacterID(j), password) for j in range(obj.SupportCharacterIDLength())],
        'SupportLevel': [table_encryption.convert_int(obj.SupportLevel(j), password) for j in range(obj.SupportLevelLength())],
        'SupportGrade': [table_encryption.convert_int(obj.SupportGrade(j), password) for j in range(obj.SupportGradeLength())],
        'SupportExSkillLevel': [table_encryption.convert_int(obj.SupportExSkillLevel(j), password) for j in range(obj.SupportExSkillLevelLength())],
        'SupportNoneExSkillLevel': [table_encryption.convert_int(obj.SupportNoneExSkillLevel(j), password) for j in range(obj.SupportNoneExSkillLevelLength())],
        'SupportEquipment1Tier': [table_encryption.convert_int(obj.SupportEquipment1Tier(j), password) for j in range(obj.SupportEquipment1TierLength())],
        'SupportEquipment1Level': [table_encryption.convert_int(obj.SupportEquipment1Level(j), password) for j in range(obj.SupportEquipment1LevelLength())],
        'SupportEquipment2Tier': [table_encryption.convert_int(obj.SupportEquipment2Tier(j), password) for j in range(obj.SupportEquipment2TierLength())],
        'SupportEquipment2Level': [table_encryption.convert_int(obj.SupportEquipment2Level(j), password) for j in range(obj.SupportEquipment2LevelLength())],
        'SupportEquipment3Tier': [table_encryption.convert_int(obj.SupportEquipment3Tier(j), password) for j in range(obj.SupportEquipment3TierLength())],
        'SupportEquipment3Level': [table_encryption.convert_int(obj.SupportEquipment3Level(j), password) for j in range(obj.SupportEquipment3LevelLength())],
        'SupportCharacterWeaponGrade': [table_encryption.convert_int(obj.SupportCharacterWeaponGrade(j), password) for j in range(obj.SupportCharacterWeaponGradeLength())],
        'SupportCharacterWeaponLevel': [table_encryption.convert_int(obj.SupportCharacterWeaponLevel(j), password) for j in range(obj.SupportCharacterWeaponLevelLength())],
        'SupportCharacterGearTier': [table_encryption.convert_int(obj.SupportCharacterGearTier(j), password) for j in range(obj.SupportCharacterGearTierLength())],
        'SupportCharacterGearLevel': [table_encryption.convert_int(obj.SupportCharacterGearLevel(j), password) for j in range(obj.SupportCharacterGearLevelLength())],
        'InteractionTSCharacterId': table_encryption.convert_long(obj.InteractionTSCharacterId(), password),
    }


def dump_FixedStrategyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StageEnterEchelon01FixedEchelonId': table_encryption.convert_long(obj.StageEnterEchelon01FixedEchelonId(), password),
        'StageEnterEchelon01Starttile': table_encryption.convert_long(obj.StageEnterEchelon01Starttile(), password),
        'StageEnterEchelon02FixedEchelonId': table_encryption.convert_long(obj.StageEnterEchelon02FixedEchelonId(), password),
        'StageEnterEchelon02Starttile': table_encryption.convert_long(obj.StageEnterEchelon02Starttile(), password),
        'StageEnterEchelon03FixedEchelonId': table_encryption.convert_long(obj.StageEnterEchelon03FixedEchelonId(), password),
        'StageEnterEchelon03Starttile': table_encryption.convert_long(obj.StageEnterEchelon03Starttile(), password),
        'StageEnterEchelon04FixedEchelonId': table_encryption.convert_long(obj.StageEnterEchelon04FixedEchelonId(), password),
        'StageEnterEchelon04Starttile': table_encryption.convert_long(obj.StageEnterEchelon04Starttile(), password),
    }


def dump_FloaterCommonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TacticEntityType': TacticEntityType(table_encryption.convert_int(obj.TacticEntityType_(), password)).name,
        'FloaterOffsetPosX': table_encryption.convert_int(obj.FloaterOffsetPosX(), password),
        'FloaterOffsetPosY': table_encryption.convert_int(obj.FloaterOffsetPosY(), password),
        'FloaterRandomPosRangeX': table_encryption.convert_int(obj.FloaterRandomPosRangeX(), password),
        'FloaterRandomPosRangeY': table_encryption.convert_int(obj.FloaterRandomPosRangeY(), password),
    }


def dump_FormationLocationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'GroupID': table_encryption.convert_long(obj.GroupID(), password),
        'SlotZ': [table_encryption.convert_float(obj.SlotZ(j), password) for j in range(obj.SlotZLength())],
        'SlotX': [table_encryption.convert_float(obj.SlotX(j), password) for j in range(obj.SlotXLength())],
    }


def dump_FurnitureExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'Category': FurnitureCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'SubCategory': FurnitureSubCategory(table_encryption.convert_int(obj.SubCategory(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'StarGradeInit': table_encryption.convert_int(obj.StarGradeInit(), password),
        'Tier': table_encryption.convert_long(obj.Tier(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'SizeWidth': table_encryption.convert_int(obj.SizeWidth(), password),
        'SizeHeight': table_encryption.convert_int(obj.SizeHeight(), password),
        'OtherSize': table_encryption.convert_int(obj.OtherSize(), password),
        'ExpandWidth': table_encryption.convert_int(obj.ExpandWidth(), password),
        'Enable': obj.Enable(),
        'ReverseRotation': obj.ReverseRotation(),
        'Prefab': table_encryption.convert_string(obj.Prefab(), password),
        'PrefabExpand': table_encryption.convert_string(obj.PrefabExpand(), password),
        'SubPrefab': table_encryption.convert_string(obj.SubPrefab(), password),
        'SubExpandPrefab': table_encryption.convert_string(obj.SubExpandPrefab(), password),
        'CornerPrefab': table_encryption.convert_string(obj.CornerPrefab(), password),
        'StackableMax': table_encryption.convert_long(obj.StackableMax(), password),
        'RecipeCraftId': table_encryption.convert_long(obj.RecipeCraftId(), password),
        'SetGroudpId': table_encryption.convert_long(obj.SetGroudpId(), password),
        'ComfortBonus': table_encryption.convert_long(obj.ComfortBonus(), password),
        'VisitOperationType': table_encryption.convert_long(obj.VisitOperationType(), password),
        'VisitBonusOperationType': table_encryption.convert_long(obj.VisitBonusOperationType(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
        'CraftQualityTier0': table_encryption.convert_long(obj.CraftQualityTier0(), password),
        'CraftQualityTier1': table_encryption.convert_long(obj.CraftQualityTier1(), password),
        'CraftQualityTier2': table_encryption.convert_long(obj.CraftQualityTier2(), password),
        'ShiftingCraftQuality': table_encryption.convert_long(obj.ShiftingCraftQuality(), password),
        'FurnitureFunctionType': FurnitureFunctionType(table_encryption.convert_int(obj.FurnitureFunctionType_(), password)).name,
        'FurnitureFunctionParameter': table_encryption.convert_long(obj.FurnitureFunctionParameter(), password),
        'VideoId': table_encryption.convert_long(obj.VideoId(), password),
        'EventCollectionId': table_encryption.convert_long(obj.EventCollectionId(), password),
        'FurnitureBubbleOffsetX': table_encryption.convert_long(obj.FurnitureBubbleOffsetX(), password),
        'FurnitureBubbleOffsetY': table_encryption.convert_long(obj.FurnitureBubbleOffsetY(), password),
        'CafeCharacterStateReq': [table_encryption.convert_string(obj.CafeCharacterStateReq(j), password) for j in range(obj.CafeCharacterStateReqLength())],
        'CafeCharacterStateAdd': [table_encryption.convert_string(obj.CafeCharacterStateAdd(j), password) for j in range(obj.CafeCharacterStateAddLength())],
        'CafeCharacterStateMake': [table_encryption.convert_string(obj.CafeCharacterStateMake(j), password) for j in range(obj.CafeCharacterStateMakeLength())],
        'CafeCharacterStateOnly': [table_encryption.convert_string(obj.CafeCharacterStateOnly(j), password) for j in range(obj.CafeCharacterStateOnlyLength())],
    }


def dump_FurnitureGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'GroupNameLocalize': table_encryption.convert_uint(obj.GroupNameLocalize(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'RequiredFurnitureCount': [table_encryption.convert_int(obj.RequiredFurnitureCount(j), password) for j in range(obj.RequiredFurnitureCountLength())],
        'ComfortBonus': [table_encryption.convert_long(obj.ComfortBonus(j), password) for j in range(obj.ComfortBonusLength())],
    }


def dump_FurnitureTemplateElementExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FurnitureTemplateId': table_encryption.convert_long(obj.FurnitureTemplateId(), password),
        'FurnitureId': table_encryption.convert_long(obj.FurnitureId(), password),
        'Location': FurnitureLocation(table_encryption.convert_int(obj.Location(), password)).name,
        'PositionX': table_encryption.convert_float(obj.PositionX(), password),
        'PositionY': table_encryption.convert_float(obj.PositionY(), password),
        'Rotation': table_encryption.convert_float(obj.Rotation(), password),
        'Order': table_encryption.convert_long(obj.Order(), password),
    }


def dump_FurnitureTemplateExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FurnitureTemplateId': table_encryption.convert_long(obj.FurnitureTemplateId(), password),
        'FunitureTemplateTitle': table_encryption.convert_uint(obj.FunitureTemplateTitle(), password),
        'ThumbnailImagePath': table_encryption.convert_string(obj.ThumbnailImagePath(), password),
        'ImagePath': table_encryption.convert_string(obj.ImagePath(), password),
    }


def dump_GachaCraftNodeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'Tier': table_encryption.convert_long(obj.Tier(), password),
        'QuickCraftNodeDisplayOrder': table_encryption.convert_int(obj.QuickCraftNodeDisplayOrder(), password),
        'NodeQuality': table_encryption.convert_long(obj.NodeQuality(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'LocalizeKey': table_encryption.convert_uint(obj.LocalizeKey(), password),
        'Property': table_encryption.convert_long(obj.Property(), password),
    }


def dump_GachaCraftNodeGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'NodeId': table_encryption.convert_long(obj.NodeId(), password),
        'GachaGroupId': table_encryption.convert_long(obj.GachaGroupId(), password),
        'ProbWeight': table_encryption.convert_long(obj.ProbWeight(), password),
    }


def dump_GachaCraftOpenTagExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'NodeTier': CraftNodeTier(table_encryption.convert_int(obj.NodeTier(), password)).name,
        'Tag': [Tag(table_encryption.convert_int(obj.Tag_(j), password)).name for j in range(obj.TagLength())],
    }


def dump_GachaElementExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'GachaGroupID': table_encryption.convert_long(obj.GachaGroupID(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelID': table_encryption.convert_long(obj.ParcelID(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'ParcelAmountMin': table_encryption.convert_int(obj.ParcelAmountMin(), password),
        'ParcelAmountMax': table_encryption.convert_int(obj.ParcelAmountMax(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'State': table_encryption.convert_int(obj.State(), password),
    }


def dump_GachaElementRecursiveExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'GachaGroupID': table_encryption.convert_long(obj.GachaGroupID(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelID': table_encryption.convert_long(obj.ParcelID(), password),
        'ParcelAmountMin': table_encryption.convert_int(obj.ParcelAmountMin(), password),
        'ParcelAmountMax': table_encryption.convert_int(obj.ParcelAmountMax(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'State': table_encryption.convert_int(obj.State(), password),
    }


def dump_GachaGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'NameKr': table_encryption.convert_string(obj.NameKr(), password),
        'IsRecursive': obj.IsRecursive(),
        'GroupType': GachaGroupType(table_encryption.convert_int(obj.GroupType(), password)).name,
    }


def dump_GoodsExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Type': table_encryption.convert_int(obj.Type(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'ConsumeParcelType': [ParcelType(table_encryption.convert_int(obj.ConsumeParcelType(j), password)).name for j in range(obj.ConsumeParcelTypeLength())],
        'ConsumeParcelId': [table_encryption.convert_long(obj.ConsumeParcelId(j), password) for j in range(obj.ConsumeParcelIdLength())],
        'ConsumeParcelAmount': [table_encryption.convert_long(obj.ConsumeParcelAmount(j), password) for j in range(obj.ConsumeParcelAmountLength())],
        'ConsumeCondition': [ConsumeCondition(table_encryption.convert_int(obj.ConsumeCondition_(j), password)).name for j in range(obj.ConsumeConditionLength())],
        'ConsumeGachaTicketType': GachaTicketType(table_encryption.convert_int(obj.ConsumeGachaTicketType(), password)).name,
        'ConsumeGachaTicketTypeAmount': table_encryption.convert_long(obj.ConsumeGachaTicketTypeAmount(), password),
        'ProductIdAOS': table_encryption.convert_long(obj.ProductIdAOS(), password),
        'ProductIdiOS': table_encryption.convert_long(obj.ProductIdiOS(), password),
        'ConsumeExtraStep': [table_encryption.convert_long(obj.ConsumeExtraStep(j), password) for j in range(obj.ConsumeExtraStepLength())],
        'ConsumeExtraAmount': [table_encryption.convert_long(obj.ConsumeExtraAmount(j), password) for j in range(obj.ConsumeExtraAmountLength())],
        'State': table_encryption.convert_int(obj.State(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelAmount': [table_encryption.convert_long(obj.ParcelAmount(j), password) for j in range(obj.ParcelAmountLength())],
    }


def dump_GroundExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StageFileName': [table_encryption.convert_string(obj.StageFileName(j), password) for j in range(obj.StageFileNameLength())],
        'GroundSceneName': table_encryption.convert_string(obj.GroundSceneName(), password),
        'FormationGroupId': table_encryption.convert_long(obj.FormationGroupId(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'EnemyBulletType': BulletType(table_encryption.convert_int(obj.EnemyBulletType(), password)).name,
        'EnemyArmorType': ArmorType(table_encryption.convert_int(obj.EnemyArmorType(), password)).name,
        'LevelNPC': table_encryption.convert_long(obj.LevelNPC(), password),
        'LevelMinion': table_encryption.convert_long(obj.LevelMinion(), password),
        'LevelElite': table_encryption.convert_long(obj.LevelElite(), password),
        'LevelChampion': table_encryption.convert_long(obj.LevelChampion(), password),
        'LevelBoss': table_encryption.convert_long(obj.LevelBoss(), password),
        'ObstacleLevel': table_encryption.convert_long(obj.ObstacleLevel(), password),
        'GradeNPC': table_encryption.convert_long(obj.GradeNPC(), password),
        'GradeMinion': table_encryption.convert_long(obj.GradeMinion(), password),
        'GradeElite': table_encryption.convert_long(obj.GradeElite(), password),
        'GradeChampion': table_encryption.convert_long(obj.GradeChampion(), password),
        'GradeBoss': table_encryption.convert_long(obj.GradeBoss(), password),
        'PlayerSightPointAdd': table_encryption.convert_long(obj.PlayerSightPointAdd(), password),
        'PlayerSightPointRate': table_encryption.convert_long(obj.PlayerSightPointRate(), password),
        'PlayerAttackRangeAdd': table_encryption.convert_long(obj.PlayerAttackRangeAdd(), password),
        'PlayerAttackRangeRate': table_encryption.convert_long(obj.PlayerAttackRangeRate(), password),
        'EnemySightPointAdd': table_encryption.convert_long(obj.EnemySightPointAdd(), password),
        'EnemySightPointRate': table_encryption.convert_long(obj.EnemySightPointRate(), password),
        'EnemyAttackRangeAdd': table_encryption.convert_long(obj.EnemyAttackRangeAdd(), password),
        'EnemyAttackRangeRate': table_encryption.convert_long(obj.EnemyAttackRangeRate(), password),
        'PlayerSkillRangeAdd': table_encryption.convert_long(obj.PlayerSkillRangeAdd(), password),
        'PlayerSkillRangeRate': table_encryption.convert_long(obj.PlayerSkillRangeRate(), password),
        'EnemySkillRangeAdd': table_encryption.convert_long(obj.EnemySkillRangeAdd(), password),
        'EnemySkillRangeRate': table_encryption.convert_long(obj.EnemySkillRangeRate(), password),
        'PlayerMinimumPositionGapRate': table_encryption.convert_long(obj.PlayerMinimumPositionGapRate(), password),
        'EnemyMinimumPositionGapRate': table_encryption.convert_long(obj.EnemyMinimumPositionGapRate(), password),
        'PlayerSightRangeMax': obj.PlayerSightRangeMax(),
        'EnemySightRangeMax': obj.EnemySightRangeMax(),
        'TSSAirUnitHeight': table_encryption.convert_long(obj.TSSAirUnitHeight(), password),
        'IsPhaseBGM': obj.IsPhaseBGM(),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'WarningUI': obj.WarningUI(),
        'TSSHatchOpen': obj.TSSHatchOpen(),
        'ForcedTacticSpeed': TacticSpeed(table_encryption.convert_int(obj.ForcedTacticSpeed(), password)).name,
        'ForcedSkillUse': TacticSkillUse(table_encryption.convert_int(obj.ForcedSkillUse(), password)).name,
        'ShowNPCSkillCutIn': ShowSkillCutIn(table_encryption.convert_int(obj.ShowNPCSkillCutIn(), password)).name,
        'ImmuneHitBeforeTimeOutEnd': obj.ImmuneHitBeforeTimeOutEnd(),
        'UIBattleHideFromScratch': obj.UIBattleHideFromScratch(),
        'BattleReadyTimelinePath': table_encryption.convert_string(obj.BattleReadyTimelinePath(), password),
        'BeforeVictoryTimelinePath': table_encryption.convert_string(obj.BeforeVictoryTimelinePath(), password),
        'SkipBattleEnd': obj.SkipBattleEnd(),
        'HideNPCWhenBattleEnd': obj.HideNPCWhenBattleEnd(),
        'CoverPointOff': obj.CoverPointOff(),
        'UIHpScale': table_encryption.convert_float(obj.UIHpScale(), password),
        'UIEmojiScale': table_encryption.convert_float(obj.UIEmojiScale(), password),
        'UISkillMainLogScale': table_encryption.convert_float(obj.UISkillMainLogScale(), password),
        'AllyPassiveSkillId': [table_encryption.convert_string(obj.AllyPassiveSkillId(j), password) for j in range(obj.AllyPassiveSkillIdLength())],
        'AllyPassiveSkillLevel': [table_encryption.convert_int(obj.AllyPassiveSkillLevel(j), password) for j in range(obj.AllyPassiveSkillLevelLength())],
        'EnemyPassiveSkillId': [table_encryption.convert_string(obj.EnemyPassiveSkillId(j), password) for j in range(obj.EnemyPassiveSkillIdLength())],
        'EnemyPassiveSkillLevel': [table_encryption.convert_int(obj.EnemyPassiveSkillLevel(j), password) for j in range(obj.EnemyPassiveSkillLevelLength())],
    }


def dump_GroundGridFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_int(obj.X(), password),
        'Y': table_encryption.convert_int(obj.Y(), password),
        'StartX': table_encryption.convert_float(obj.StartX(), password),
        'StartY': table_encryption.convert_float(obj.StartY(), password),
        'Gap': table_encryption.convert_float(obj.Gap(), password),
        'Nodes': [dump_GroundNodeFlat(obj.Nodes(j), password) for j in range(obj.NodesLength())],
        'Version': table_encryption.convert_string(obj.Version(), password),
    }


def dump_GroundNodeFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_int(obj.X(), password),
        'Y': table_encryption.convert_int(obj.Y(), password),
        'IsCanNotUseSkill': obj.IsCanNotUseSkill(),
        'Position': dump_GroundVector3(obj.Position(), password),
        'NodeType': GroundNodeType(table_encryption.convert_int(obj.NodeType(), password)).name,
        'OriginalNodeType': GroundNodeType(table_encryption.convert_int(obj.OriginalNodeType(), password)).name,
    }


def dump_GroundModuleRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_uint(obj.GroupId(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
        'RewardParcelProbability': table_encryption.convert_long(obj.RewardParcelProbability(), password),
        'IsDisplayed': obj.IsDisplayed(),
        'DropItemModelPrefabPath': table_encryption.convert_string(obj.DropItemModelPrefabPath(), password),
    }


def dump_GroundNodeLayerFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Layers': [table_encryption.convert_ubyte(obj.Layers(j), password) for j in range(obj.LayersLength())],
    }


def dump_GuideMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'TabNumber': table_encryption.convert_long(obj.TabNumber(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'Description': table_encryption.convert_uint(obj.Description(), password),
        'ToastDisplayType': MissionToastDisplayConditionType(table_encryption.convert_int(obj.ToastDisplayType(), password)).name,
        'ToastImagePath': table_encryption.convert_string(obj.ToastImagePath(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterTag': [Tag(table_encryption.convert_int(obj.CompleteConditionParameterTag(j), password)).name for j in range(obj.CompleteConditionParameterTagLength())],
        'IsAutoClearForScenario': obj.IsAutoClearForScenario(),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
    }


def dump_GuideMissionOpenStageConditionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'OrderNumber': table_encryption.convert_long(obj.OrderNumber(), password),
        'TabLocalizeCode': table_encryption.convert_string(obj.TabLocalizeCode(), password),
        'ClearScenarioModeId': table_encryption.convert_long(obj.ClearScenarioModeId(), password),
        'LockScenarioTextLocailzeCode': table_encryption.convert_string(obj.LockScenarioTextLocailzeCode(), password),
        'ShortcutScenarioUI': table_encryption.convert_string(obj.ShortcutScenarioUI(), password),
        'ClearStageId': table_encryption.convert_long(obj.ClearStageId(), password),
        'LockStageTextLocailzeCode': table_encryption.convert_string(obj.LockStageTextLocailzeCode(), password),
        'ShortcutStageUI': table_encryption.convert_string(obj.ShortcutStageUI(), password),
    }


def dump_GuideMissionSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TitleLocalizeCode': table_encryption.convert_string(obj.TitleLocalizeCode(), password),
        'PermanentInfomationLocalizeCode': table_encryption.convert_string(obj.PermanentInfomationLocalizeCode(), password),
        'InfomationLocalizeCode': table_encryption.convert_string(obj.InfomationLocalizeCode(), password),
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'Enabled': obj.Enabled(),
        'BannerOpenDate': table_encryption.convert_string(obj.BannerOpenDate(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'StartableEndDate': table_encryption.convert_string(obj.StartableEndDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'CloseBannerAfterCompletion': obj.CloseBannerAfterCompletion(),
        'MaximumLoginCount': table_encryption.convert_long(obj.MaximumLoginCount(), password),
        'ExpiryDate': table_encryption.convert_long(obj.ExpiryDate(), password),
        'SpineCharacterId': table_encryption.convert_long(obj.SpineCharacterId(), password),
        'RequirementParcelImage': table_encryption.convert_string(obj.RequirementParcelImage(), password),
        'RewardImage': table_encryption.convert_string(obj.RewardImage(), password),
        'LobbyBannerImage': table_encryption.convert_string(obj.LobbyBannerImage(), password),
        'BackgroundImage': table_encryption.convert_string(obj.BackgroundImage(), password),
        'TitleImage': table_encryption.convert_string(obj.TitleImage(), password),
        'RequirementParcelType': ParcelType(table_encryption.convert_int(obj.RequirementParcelType(), password)).name,
        'RequirementParcelId': table_encryption.convert_long(obj.RequirementParcelId(), password),
        'RequirementParcelAmount': table_encryption.convert_int(obj.RequirementParcelAmount(), password),
        'TabType': GuideMissionTabType(table_encryption.convert_int(obj.TabType(), password)).name,
        'IsPermanent': obj.IsPermanent(),
        'PreSeasonId': table_encryption.convert_long(obj.PreSeasonId(), password),
    }


def dump_HpBarAbbreviationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MonsterLv': table_encryption.convert_int(obj.MonsterLv(), password),
        'StandardHpBar': table_encryption.convert_int(obj.StandardHpBar(), password),
        'RaidBossHpBar': table_encryption.convert_int(obj.RaidBossHpBar(), password),
    }


def dump_InformationStrategyObjectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'PageName': table_encryption.convert_string(obj.PageName(), password),
        'LocalizeCodeId': table_encryption.convert_string(obj.LocalizeCodeId(), password),
    }


def dump_ItemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'ItemCategory': ItemCategory(table_encryption.convert_int(obj.ItemCategory_(), password)).name,
        'Quality': table_encryption.convert_long(obj.Quality(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'SpriteName': table_encryption.convert_string(obj.SpriteName(), password),
        'StackableMax': table_encryption.convert_int(obj.StackableMax(), password),
        'StackableFunction': table_encryption.convert_int(obj.StackableFunction(), password),
        'ImmediateUse': obj.ImmediateUse(),
        'UsingResultParcelType': ParcelType(table_encryption.convert_int(obj.UsingResultParcelType(), password)).name,
        'UsingResultId': table_encryption.convert_long(obj.UsingResultId(), password),
        'UsingResultAmount': table_encryption.convert_long(obj.UsingResultAmount(), password),
        'MailType': MailType(table_encryption.convert_int(obj.MailType_(), password)).name,
        'ExpiryChangeParcelType': ParcelType(table_encryption.convert_int(obj.ExpiryChangeParcelType(), password)).name,
        'ExpiryChangeId': table_encryption.convert_long(obj.ExpiryChangeId(), password),
        'ExpiryChangeAmount': table_encryption.convert_long(obj.ExpiryChangeAmount(), password),
        'CanTierUpgrade': obj.CanTierUpgrade(),
        'TierUpgradeRecipeCraftId': table_encryption.convert_long(obj.TierUpgradeRecipeCraftId(), password),
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
        'CraftQualityTier0': table_encryption.convert_long(obj.CraftQualityTier0(), password),
        'CraftQualityTier1': table_encryption.convert_long(obj.CraftQualityTier1(), password),
        'CraftQualityTier2': table_encryption.convert_long(obj.CraftQualityTier2(), password),
        'ShiftingCraftQuality': table_encryption.convert_long(obj.ShiftingCraftQuality(), password),
        'MaxGiftTags': table_encryption.convert_int(obj.MaxGiftTags(), password),
        'ShopCategory': [ShopCategoryType(table_encryption.convert_int(obj.ShopCategory(j), password)).name for j in range(obj.ShopCategoryLength())],
        'ExpirationDateTime': table_encryption.convert_string(obj.ExpirationDateTime(), password),
        'ExpirationNotifyDateIn': table_encryption.convert_int(obj.ExpirationNotifyDateIn(), password),
        'ShortcutTypeId': table_encryption.convert_long(obj.ShortcutTypeId(), password),
        'GachaTicket': GachaTicketType(table_encryption.convert_int(obj.GachaTicket(), password)).name,
    }


def dump_KnockBackExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Index': table_encryption.convert_long(obj.Index(), password),
        'Dist': table_encryption.convert_float(obj.Dist(), password),
        'Speed': table_encryption.convert_float(obj.Speed(), password),
    }


def dump_LimitedStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'StageDifficulty': StageDifficulty(table_encryption.convert_int(obj.StageDifficulty_(), password)).name,
        'StageNumber': table_encryption.convert_string(obj.StageNumber(), password),
        'StageDisplay': table_encryption.convert_int(obj.StageDisplay(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'OpenDate': table_encryption.convert_long(obj.OpenDate(), password),
        'OpenEventPoint': table_encryption.convert_long(obj.OpenEventPoint(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'StageEnterEchelonCount': table_encryption.convert_int(obj.StageEnterEchelonCount(), password),
        'StarConditionTacticRankSCount': table_encryption.convert_long(obj.StarConditionTacticRankSCount(), password),
        'StarConditionTurnCount': table_encryption.convert_long(obj.StarConditionTurnCount(), password),
        'EnterScenarioGroupId': [table_encryption.convert_long(obj.EnterScenarioGroupId(j), password) for j in range(obj.EnterScenarioGroupIdLength())],
        'ClearScenarioGroupId': [table_encryption.convert_long(obj.ClearScenarioGroupId(j), password) for j in range(obj.ClearScenarioGroupIdLength())],
        'StrategyMap': table_encryption.convert_string(obj.StrategyMap(), password),
        'StrategyMapBG': table_encryption.convert_string(obj.StrategyMapBG(), password),
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'MaxTurn': table_encryption.convert_int(obj.MaxTurn(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'BgmId': table_encryption.convert_string(obj.BgmId(), password),
        'StrategyEnvironment': StrategyEnvironment(table_encryption.convert_int(obj.StrategyEnvironment_(), password)).name,
        'GroundID': table_encryption.convert_long(obj.GroundID(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'InstantClear': obj.InstantClear(),
        'BuffContentId': table_encryption.convert_long(obj.BuffContentId(), password),
        'ChallengeDisplay': obj.ChallengeDisplay(),
    }


def dump_LimitedStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_LimitedStageSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'TypeACount': table_encryption.convert_long(obj.TypeACount(), password),
        'TypeBCount': table_encryption.convert_long(obj.TypeBCount(), password),
        'TypeCCount': table_encryption.convert_long(obj.TypeCCount(), password),
    }


def dump_LocalizeCharProfileExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'StatusMessageKr': table_encryption.convert_string(obj.StatusMessageKr(), password),
        'StatusMessageJp': table_encryption.convert_string(obj.StatusMessageJp(), password),
        'FullNameKr': table_encryption.convert_string(obj.FullNameKr(), password),
        'FullNameJp': table_encryption.convert_string(obj.FullNameJp(), password),
        'FamilyNameKr': table_encryption.convert_string(obj.FamilyNameKr(), password),
        'FamilyNameRubyKr': table_encryption.convert_string(obj.FamilyNameRubyKr(), password),
        'PersonalNameKr': table_encryption.convert_string(obj.PersonalNameKr(), password),
        'PersonalNameRubyKr': table_encryption.convert_string(obj.PersonalNameRubyKr(), password),
        'FamilyNameJp': table_encryption.convert_string(obj.FamilyNameJp(), password),
        'FamilyNameRubyJp': table_encryption.convert_string(obj.FamilyNameRubyJp(), password),
        'PersonalNameJp': table_encryption.convert_string(obj.PersonalNameJp(), password),
        'PersonalNameRubyJp': table_encryption.convert_string(obj.PersonalNameRubyJp(), password),
        'SchoolYearKr': table_encryption.convert_string(obj.SchoolYearKr(), password),
        'SchoolYearJp': table_encryption.convert_string(obj.SchoolYearJp(), password),
        'CharacterAgeKr': table_encryption.convert_string(obj.CharacterAgeKr(), password),
        'CharacterAgeJp': table_encryption.convert_string(obj.CharacterAgeJp(), password),
        'BirthDay': table_encryption.convert_string(obj.BirthDay(), password),
        'BirthdayKr': table_encryption.convert_string(obj.BirthdayKr(), password),
        'BirthdayJp': table_encryption.convert_string(obj.BirthdayJp(), password),
        'CharHeightKr': table_encryption.convert_string(obj.CharHeightKr(), password),
        'CharHeightJp': table_encryption.convert_string(obj.CharHeightJp(), password),
        'DesignerNameKr': table_encryption.convert_string(obj.DesignerNameKr(), password),
        'DesignerNameJp': table_encryption.convert_string(obj.DesignerNameJp(), password),
        'IllustratorNameKr': table_encryption.convert_string(obj.IllustratorNameKr(), password),
        'IllustratorNameJp': table_encryption.convert_string(obj.IllustratorNameJp(), password),
        'CharacterVoiceKr': table_encryption.convert_string(obj.CharacterVoiceKr(), password),
        'CharacterVoiceJp': table_encryption.convert_string(obj.CharacterVoiceJp(), password),
        'HobbyKr': table_encryption.convert_string(obj.HobbyKr(), password),
        'HobbyJp': table_encryption.convert_string(obj.HobbyJp(), password),
        'WeaponNameKr': table_encryption.convert_string(obj.WeaponNameKr(), password),
        'WeaponDescKr': table_encryption.convert_string(obj.WeaponDescKr(), password),
        'WeaponNameJp': table_encryption.convert_string(obj.WeaponNameJp(), password),
        'WeaponDescJp': table_encryption.convert_string(obj.WeaponDescJp(), password),
        'ProfileIntroductionKr': table_encryption.convert_string(obj.ProfileIntroductionKr(), password),
        'ProfileIntroductionJp': table_encryption.convert_string(obj.ProfileIntroductionJp(), password),
        'CharacterSSRNewKr': table_encryption.convert_string(obj.CharacterSSRNewKr(), password),
        'CharacterSSRNewJp': table_encryption.convert_string(obj.CharacterSSRNewJp(), password),
    }


def dump_LocalizeCodeInBuildExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
    }


def dump_LocalizeEtcExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'NameKr': table_encryption.convert_string(obj.NameKr(), password),
        'DescriptionKr': table_encryption.convert_string(obj.DescriptionKr(), password),
        'NameJp': table_encryption.convert_string(obj.NameJp(), password),
        'DescriptionJp': table_encryption.convert_string(obj.DescriptionJp(), password),
    }


def dump_LocalizeFieldExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
    }


def dump_LocalizeGachaShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GachaShopId': table_encryption.convert_long(obj.GachaShopId(), password),
        'TabNameKr': table_encryption.convert_string(obj.TabNameKr(), password),
        'TabNameJp': table_encryption.convert_string(obj.TabNameJp(), password),
        'TitleNameKr': table_encryption.convert_string(obj.TitleNameKr(), password),
        'TitleNameJp': table_encryption.convert_string(obj.TitleNameJp(), password),
        'SubTitleKr': table_encryption.convert_string(obj.SubTitleKr(), password),
        'SubTitleJp': table_encryption.convert_string(obj.SubTitleJp(), password),
        'GachaDescriptionKr': table_encryption.convert_string(obj.GachaDescriptionKr(), password),
        'GachaDescriptionJp': table_encryption.convert_string(obj.GachaDescriptionJp(), password),
    }


def dump_LogicEffectCommonVisualExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StringID': table_encryption.convert_uint(obj.StringID(), password),
        'IconSpriteName': table_encryption.convert_string(obj.IconSpriteName(), password),
        'IconDispelColor': [table_encryption.convert_float(obj.IconDispelColor(j), password) for j in range(obj.IconDispelColorLength())],
        'ParticleEnterPath': table_encryption.convert_string(obj.ParticleEnterPath(), password),
        'ParticleEnterSocket': EffectBone(table_encryption.convert_int(obj.ParticleEnterSocket(), password)).name,
        'ParticleLoopPath': table_encryption.convert_string(obj.ParticleLoopPath(), password),
        'ParticleLoopSocket': EffectBone(table_encryption.convert_int(obj.ParticleLoopSocket(), password)).name,
        'ParticleEndPath': table_encryption.convert_string(obj.ParticleEndPath(), password),
        'ParticleEndSocket': EffectBone(table_encryption.convert_int(obj.ParticleEndSocket(), password)).name,
        'ParticleApplyPath': table_encryption.convert_string(obj.ParticleApplyPath(), password),
        'ParticleApplySocket': EffectBone(table_encryption.convert_int(obj.ParticleApplySocket(), password)).name,
        'ParticleRemovedPath': table_encryption.convert_string(obj.ParticleRemovedPath(), password),
        'ParticleRemovedSocket': EffectBone(table_encryption.convert_int(obj.ParticleRemovedSocket(), password)).name,
    }


def dump_MiniGameAudioAnimatorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ControllerNameHash': table_encryption.convert_uint(obj.ControllerNameHash(), password),
        'VoiceNamePrefix': table_encryption.convert_string(obj.VoiceNamePrefix(), password),
        'StateNameHash': table_encryption.convert_uint(obj.StateNameHash(), password),
        'StateName': table_encryption.convert_string(obj.StateName(), password),
        'IgnoreInterruptDelay': obj.IgnoreInterruptDelay(),
        'IgnoreInterruptPlay': obj.IgnoreInterruptPlay(),
        'Volume': table_encryption.convert_float(obj.Volume(), password),
        'Delay': table_encryption.convert_float(obj.Delay(), password),
        'AudioPriority': table_encryption.convert_int(obj.AudioPriority(), password),
        'AudioClipPath': [table_encryption.convert_string(obj.AudioClipPath(j), password) for j in range(obj.AudioClipPathLength())],
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
    }


def dump_MiniGameMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'GroupName': table_encryption.convert_string(obj.GroupName(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_uint(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ToastDisplayType': MissionToastDisplayConditionType(table_encryption.convert_int(obj.ToastDisplayType(), password)).name,
        'ToastImagePath': table_encryption.convert_string(obj.ToastImagePath(), password),
        'ViewFlag': obj.ViewFlag(),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'IsCompleteExtensionTime': obj.IsCompleteExtensionTime(),
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterTag': [Tag(table_encryption.convert_int(obj.CompleteConditionParameterTag(j), password)).name for j in range(obj.CompleteConditionParameterTagLength())],
        'RewardIcon': table_encryption.convert_string(obj.RewardIcon(), password),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
    }


def dump_MiniGamePlayGuideExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'GuideTitle': table_encryption.convert_string(obj.GuideTitle(), password),
        'GuideImagePath': table_encryption.convert_string(obj.GuideImagePath(), password),
        'GuideText': table_encryption.convert_string(obj.GuideText(), password),
    }


def dump_MiniGameRhythmBgmExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RhythmBgmId': table_encryption.convert_long(obj.RhythmBgmId(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'StageSelectImagePath': table_encryption.convert_string(obj.StageSelectImagePath(), password),
        'Bpm': table_encryption.convert_long(obj.Bpm(), password),
        'Bgm': table_encryption.convert_long(obj.Bgm(), password),
        'BgmNameText': table_encryption.convert_string(obj.BgmNameText(), password),
        'BgmArtistText': table_encryption.convert_string(obj.BgmArtistText(), password),
        'HasLyricist': obj.HasLyricist(),
        'BgmComposerText': table_encryption.convert_string(obj.BgmComposerText(), password),
        'BgmLength': table_encryption.convert_int(obj.BgmLength(), password),
    }


def dump_MiniGameRhythmExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'RhythmBgmId': table_encryption.convert_long(obj.RhythmBgmId(), password),
        'PresetName': table_encryption.convert_string(obj.PresetName(), password),
        'StageDifficulty': Difficulty(table_encryption.convert_int(obj.StageDifficulty(), password)).name,
        'IsSpecial': obj.IsSpecial(),
        'OpenStageScoreAmount': table_encryption.convert_long(obj.OpenStageScoreAmount(), password),
        'MaxHp': table_encryption.convert_long(obj.MaxHp(), password),
        'MissDamage': table_encryption.convert_long(obj.MissDamage(), password),
        'CriticalHPRestoreValue': table_encryption.convert_long(obj.CriticalHPRestoreValue(), password),
        'MaxScore': table_encryption.convert_long(obj.MaxScore(), password),
        'FeverScoreRate': table_encryption.convert_long(obj.FeverScoreRate(), password),
        'NoteScoreRate': table_encryption.convert_long(obj.NoteScoreRate(), password),
        'ComboScoreRate': table_encryption.convert_long(obj.ComboScoreRate(), password),
        'AttackScoreRate': table_encryption.convert_long(obj.AttackScoreRate(), password),
        'FeverCriticalRate': table_encryption.convert_float(obj.FeverCriticalRate(), password),
        'FeverAttackRate': table_encryption.convert_float(obj.FeverAttackRate(), password),
        'MaxHpScore': table_encryption.convert_long(obj.MaxHpScore(), password),
        'RhythmFileName': table_encryption.convert_string(obj.RhythmFileName(), password),
        'ArtLevelSceneName': table_encryption.convert_string(obj.ArtLevelSceneName(), password),
        'ComboImagePath': table_encryption.convert_string(obj.ComboImagePath(), password),
    }


def dump_MiniGameShootingCharacterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'SpineResourceName': table_encryption.convert_string(obj.SpineResourceName(), password),
        'BodyRadius': table_encryption.convert_float(obj.BodyRadius(), password),
        'ModelPrefabName': table_encryption.convert_string(obj.ModelPrefabName(), password),
        'NormalAttackSkillData': table_encryption.convert_string(obj.NormalAttackSkillData(), password),
        'PublicSkillData': [table_encryption.convert_string(obj.PublicSkillData(j), password) for j in range(obj.PublicSkillDataLength())],
        'DeathSkillData': table_encryption.convert_string(obj.DeathSkillData(), password),
        'MaxHP': table_encryption.convert_long(obj.MaxHP(), password),
        'AttackPower': table_encryption.convert_long(obj.AttackPower(), password),
        'DefensePower': table_encryption.convert_long(obj.DefensePower(), password),
        'CriticalRate': table_encryption.convert_long(obj.CriticalRate(), password),
        'CriticalDamageRate': table_encryption.convert_long(obj.CriticalDamageRate(), password),
        'AttackRange': table_encryption.convert_long(obj.AttackRange(), password),
        'MoveSpeed': table_encryption.convert_long(obj.MoveSpeed(), password),
        'ShotTime': table_encryption.convert_long(obj.ShotTime(), password),
        'IsBoss': obj.IsBoss(),
        'Scale': table_encryption.convert_float(obj.Scale(), password),
        'IgnoreObstacleCheck': obj.IgnoreObstacleCheck(),
        'CharacterVoiceGroupId': table_encryption.convert_long(obj.CharacterVoiceGroupId(), password),
    }


def dump_MiniGameShootingGeasExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'GeasType': Geas(table_encryption.convert_int(obj.GeasType(), password)).name,
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'Probability': table_encryption.convert_long(obj.Probability(), password),
        'MaxOverlapCount': table_encryption.convert_int(obj.MaxOverlapCount(), password),
        'GeasData': table_encryption.convert_string(obj.GeasData(), password),
        'NeedGeasId': table_encryption.convert_long(obj.NeedGeasId(), password),
        'HideInPausePopup': obj.HideInPausePopup(),
    }


def dump_MiniGameShootingStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'BgmId': [table_encryption.convert_long(obj.BgmId(j), password) for j in range(obj.BgmIdLength())],
        'CostGoodsId': table_encryption.convert_long(obj.CostGoodsId(), password),
        'Difficulty': Difficulty(table_encryption.convert_int(obj.Difficulty_(), password)).name,
        'DesignLevel': table_encryption.convert_string(obj.DesignLevel(), password),
        'ArtLevel': table_encryption.convert_string(obj.ArtLevel(), password),
        'StartBattleDuration': table_encryption.convert_long(obj.StartBattleDuration(), password),
        'DefaultBattleDuration': table_encryption.convert_long(obj.DefaultBattleDuration(), password),
        'DefaultLogicEffect': table_encryption.convert_string(obj.DefaultLogicEffect(), password),
        'CameraSizeRate': table_encryption.convert_float(obj.CameraSizeRate(), password),
        'EventContentStageRewardId': table_encryption.convert_long(obj.EventContentStageRewardId(), password),
    }


def dump_MiniGameShootingStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'ClearSection': table_encryption.convert_long(obj.ClearSection(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_int(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_MinigameTBGDiceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'DiceGroup': table_encryption.convert_int(obj.DiceGroup(), password),
        'DiceResult': table_encryption.convert_int(obj.DiceResult(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'ProbModifyCondition': [TBGProbModifyCondition(table_encryption.convert_int(obj.ProbModifyCondition(j), password)).name for j in range(obj.ProbModifyConditionLength())],
        'ProbModifyValue': [table_encryption.convert_int(obj.ProbModifyValue(j), password) for j in range(obj.ProbModifyValueLength())],
        'ProbModifyLimit': [table_encryption.convert_int(obj.ProbModifyLimit(j), password) for j in range(obj.ProbModifyLimitLength())],
    }


def dump_MinigameTBGEncounterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'AllThema': obj.AllThema(),
        'ThemaIndex': table_encryption.convert_int(obj.ThemaIndex(), password),
        'ThemaType': TBGThemaType(table_encryption.convert_int(obj.ThemaType(), password)).name,
        'ObjectType': TBGObjectType(table_encryption.convert_int(obj.ObjectType(), password)).name,
        'EnemyImagePath': table_encryption.convert_string(obj.EnemyImagePath(), password),
        'EnemyPrefabName': table_encryption.convert_string(obj.EnemyPrefabName(), password),
        'EnemyNameLocalize': table_encryption.convert_string(obj.EnemyNameLocalize(), password),
        'OptionGroupId': table_encryption.convert_long(obj.OptionGroupId(), password),
        'RewardHide': obj.RewardHide(),
        'EncounterTitleLocalize': table_encryption.convert_string(obj.EncounterTitleLocalize(), password),
        'StoryImagePath': table_encryption.convert_string(obj.StoryImagePath(), password),
        'BeforeStoryLocalize': table_encryption.convert_string(obj.BeforeStoryLocalize(), password),
        'BeforeStoryOption1Localize': table_encryption.convert_string(obj.BeforeStoryOption1Localize(), password),
        'BeforeStoryOption2Localize': table_encryption.convert_string(obj.BeforeStoryOption2Localize(), password),
        'BeforeStoryOption3Localize': table_encryption.convert_string(obj.BeforeStoryOption3Localize(), password),
        'AllyAttackLocalize': table_encryption.convert_string(obj.AllyAttackLocalize(), password),
        'EnemyAttackLocalize': table_encryption.convert_string(obj.EnemyAttackLocalize(), password),
        'AttackDefenceLocalize': table_encryption.convert_string(obj.AttackDefenceLocalize(), password),
        'ClearStoryLocalize': table_encryption.convert_string(obj.ClearStoryLocalize(), password),
        'DefeatStoryLocalize': table_encryption.convert_string(obj.DefeatStoryLocalize(), password),
        'RunawayStoryLocalize': table_encryption.convert_string(obj.RunawayStoryLocalize(), password),
    }


def dump_MinigameTBGEncounterOptionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'OptionGroupId': table_encryption.convert_long(obj.OptionGroupId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'SlotIndex': table_encryption.convert_int(obj.SlotIndex(), password),
        'OptionTitleLocalize': table_encryption.convert_string(obj.OptionTitleLocalize(), password),
        'OptionSuccessLocalize': table_encryption.convert_string(obj.OptionSuccessLocalize(), password),
        'OptionSuccessRewardGroupId': table_encryption.convert_long(obj.OptionSuccessRewardGroupId(), password),
        'OptionSuccessOrHigherDiceCount': table_encryption.convert_int(obj.OptionSuccessOrHigherDiceCount(), password),
        'OptionGreatSuccessOrHigherDiceCount': table_encryption.convert_int(obj.OptionGreatSuccessOrHigherDiceCount(), password),
        'OptionFailLocalize': table_encryption.convert_string(obj.OptionFailLocalize(), password),
        'OptionFailLessDiceCount': table_encryption.convert_int(obj.OptionFailLessDiceCount(), password),
        'RunawayOrHigherDiceCount': table_encryption.convert_int(obj.RunawayOrHigherDiceCount(), password),
        'RewardHide': obj.RewardHide(),
    }


def dump_MinigameTBGEncounterRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'TBGOptionSuccessType': TBGOptionSuccessType(table_encryption.convert_int(obj.TBGOptionSuccessType_(), password)).name,
        'Paremeter': table_encryption.convert_long(obj.Paremeter(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'Amount': table_encryption.convert_long(obj.Amount(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
    }


def dump_MinigameTBGItemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ItemType': TBGItemType(table_encryption.convert_int(obj.ItemType(), password)).name,
        'TBGItemEffectType': TBGItemEffectType(table_encryption.convert_int(obj.TBGItemEffectType_(), password)).name,
        'ItemParameter': table_encryption.convert_int(obj.ItemParameter(), password),
        'LocalizeETCId': table_encryption.convert_string(obj.LocalizeETCId(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'BuffIcon': table_encryption.convert_string(obj.BuffIcon(), password),
        'EncounterCount': table_encryption.convert_int(obj.EncounterCount(), password),
        'DiceEffectAniClip': table_encryption.convert_string(obj.DiceEffectAniClip(), password),
    }


def dump_MinigameTBGObjectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'Key': table_encryption.convert_string(obj.Key(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'ObjectType': TBGObjectType(table_encryption.convert_int(obj.ObjectType(), password)).name,
        'ObjectCostType': ParcelType(table_encryption.convert_int(obj.ObjectCostType(), password)).name,
        'ObjectCostId': table_encryption.convert_long(obj.ObjectCostId(), password),
        'ObjectCostAmount': table_encryption.convert_int(obj.ObjectCostAmount(), password),
        'Disposable': obj.Disposable(),
        'ReEncounterCost': obj.ReEncounterCost(),
    }


def dump_MinigameTBGSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ItemSlot': table_encryption.convert_int(obj.ItemSlot(), password),
        'DefaultEchelonHp': table_encryption.convert_int(obj.DefaultEchelonHp(), password),
        'DefaultItemDiceId': table_encryption.convert_long(obj.DefaultItemDiceId(), password),
        'EchelonSlot1CharacterId': table_encryption.convert_long(obj.EchelonSlot1CharacterId(), password),
        'EchelonSlot2CharacterId': table_encryption.convert_long(obj.EchelonSlot2CharacterId(), password),
        'EchelonSlot3CharacterId': table_encryption.convert_long(obj.EchelonSlot3CharacterId(), password),
        'EchelonSlot4CharacterId': table_encryption.convert_long(obj.EchelonSlot4CharacterId(), password),
        'EchelonSlot1Portrait': table_encryption.convert_string(obj.EchelonSlot1Portrait(), password),
        'EchelonSlot2Portrait': table_encryption.convert_string(obj.EchelonSlot2Portrait(), password),
        'EchelonSlot3Portrait': table_encryption.convert_string(obj.EchelonSlot3Portrait(), password),
        'EchelonSlot4Portrait': table_encryption.convert_string(obj.EchelonSlot4Portrait(), password),
        'EventUseCostType': ParcelType(table_encryption.convert_int(obj.EventUseCostType(), password)).name,
        'EventUseCostId': table_encryption.convert_long(obj.EventUseCostId(), password),
        'EchelonRevivalCostType': ParcelType(table_encryption.convert_int(obj.EchelonRevivalCostType(), password)).name,
        'EchelonRevivalCostId': table_encryption.convert_long(obj.EchelonRevivalCostId(), password),
        'EchelonRevivalCostAmount': table_encryption.convert_int(obj.EchelonRevivalCostAmount(), password),
        'EnemyBossHP': table_encryption.convert_int(obj.EnemyBossHP(), password),
        'EnemyMinionHP': table_encryption.convert_int(obj.EnemyMinionHP(), password),
        'AttackDamage': table_encryption.convert_int(obj.AttackDamage(), password),
        'CriticalAttackDamage': table_encryption.convert_int(obj.CriticalAttackDamage(), password),
        'RoundItemSelectLimit': table_encryption.convert_int(obj.RoundItemSelectLimit(), password),
        'InstantClearRound': table_encryption.convert_int(obj.InstantClearRound(), password),
        'MaxHp': table_encryption.convert_int(obj.MaxHp(), password),
        'MapImagePath': table_encryption.convert_string(obj.MapImagePath(), password),
        'MapNameLocalize': table_encryption.convert_string(obj.MapNameLocalize(), password),
        'StartThemaIndex': table_encryption.convert_int(obj.StartThemaIndex(), password),
        'LoopThemaIndex': table_encryption.convert_int(obj.LoopThemaIndex(), password),
    }


def dump_MinigameTBGThemaExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ThemaIndex': table_encryption.convert_int(obj.ThemaIndex(), password),
        'ThemaType': TBGThemaType(table_encryption.convert_int(obj.ThemaType(), password)).name,
        'ThemaMap': table_encryption.convert_string(obj.ThemaMap(), password),
        'ThemaMapBG': table_encryption.convert_string(obj.ThemaMapBG(), password),
        'PortalCondition': [TBGPortalCondition(table_encryption.convert_int(obj.PortalCondition(j), password)).name for j in range(obj.PortalConditionLength())],
        'PortalConditionParameter': [table_encryption.convert_string(obj.PortalConditionParameter(j), password) for j in range(obj.PortalConditionParameterLength())],
        'ThemaNameLocalize': table_encryption.convert_string(obj.ThemaNameLocalize(), password),
        'ThemaLoadingImage': table_encryption.convert_string(obj.ThemaLoadingImage(), password),
        'ThemaPlayerPrefab': table_encryption.convert_string(obj.ThemaPlayerPrefab(), password),
        'ThemaLeaderId': table_encryption.convert_long(obj.ThemaLeaderId(), password),
        'ThemaGoalLocalize': table_encryption.convert_string(obj.ThemaGoalLocalize(), password),
        'InstantClearCostAmount': table_encryption.convert_long(obj.InstantClearCostAmount(), password),
        'IsTutorial': obj.IsTutorial(),
    }


def dump_MiniGameTBGThemaRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ThemaRound': table_encryption.convert_int(obj.ThemaRound(), password),
        'ThemaUniqueId': table_encryption.convert_int(obj.ThemaUniqueId(), password),
        'IsLoop': obj.IsLoop(),
        'MiniGameTBGThemaRewardType': MiniGameTBGThemaRewardType(table_encryption.convert_int(obj.MiniGameTBGThemaRewardType_(), password)).name,
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_int(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_MinigameTBGVoiceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'VoiceCondition': TBGVoiceCondition(table_encryption.convert_int(obj.VoiceCondition(), password)).name,
        'VoiceId': table_encryption.convert_uint(obj.VoiceId(), password),
    }


def dump_MissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_uint(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ToastDisplayType': MissionToastDisplayConditionType(table_encryption.convert_int(obj.ToastDisplayType(), password)).name,
        'ToastImagePath': table_encryption.convert_string(obj.ToastImagePath(), password),
        'ViewFlag': obj.ViewFlag(),
        'Limit': obj.Limit(),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'EndDay': table_encryption.convert_long(obj.EndDay(), password),
        'StartableEndDate': table_encryption.convert_string(obj.StartableEndDate(), password),
        'DateAutoRefer': ContentType(table_encryption.convert_int(obj.DateAutoRefer(), password)).name,
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ContentTags': [SuddenMissionContentType(table_encryption.convert_int(obj.ContentTags(j), password)).name for j in range(obj.ContentTagsLength())],
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'ChallengeStageShortcut': table_encryption.convert_long(obj.ChallengeStageShortcut(), password),
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterTag': [Tag(table_encryption.convert_int(obj.CompleteConditionParameterTag(j), password)).name for j in range(obj.CompleteConditionParameterTagLength())],
        'RewardIcon': table_encryption.convert_string(obj.RewardIcon(), password),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
    }


def dump_NormalSkillTemplateExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Index': table_encryption.convert_long(obj.Index(), password),
        'FirstCoolTime': table_encryption.convert_float(obj.FirstCoolTime(), password),
        'CoolTime': table_encryption.convert_float(obj.CoolTime(), password),
        'MultiAni': obj.MultiAni(),
    }


def dump_ObstacleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Index': table_encryption.convert_long(obj.Index(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'JumpAble': obj.JumpAble(),
        'SubOffset': [table_encryption.convert_float(obj.SubOffset(j), password) for j in range(obj.SubOffsetLength())],
        'X': table_encryption.convert_float(obj.X(), password),
        'Z': table_encryption.convert_float(obj.Z(), password),
        'Hp': table_encryption.convert_long(obj.Hp(), password),
        'MaxHp': table_encryption.convert_long(obj.MaxHp(), password),
        'BlockRate': table_encryption.convert_int(obj.BlockRate(), password),
        'EvasionRate': table_encryption.convert_int(obj.EvasionRate(), password),
        'DestroyType': ObstacleDestroyType(table_encryption.convert_int(obj.DestroyType(), password)).name,
        'Point1Offeset': [table_encryption.convert_float(obj.Point1Offeset(j), password) for j in range(obj.Point1OffesetLength())],
        'EnemyPoint1Osset': [table_encryption.convert_float(obj.EnemyPoint1Osset(j), password) for j in range(obj.EnemyPoint1OssetLength())],
        'Point2Offeset': [table_encryption.convert_float(obj.Point2Offeset(j), password) for j in range(obj.Point2OffesetLength())],
        'EnemyPoint2Osset': [table_encryption.convert_float(obj.EnemyPoint2Osset(j), password) for j in range(obj.EnemyPoint2OssetLength())],
        'SubObstacleID': [table_encryption.convert_long(obj.SubObstacleID(j), password) for j in range(obj.SubObstacleIDLength())],
    }


def dump_ObstacleFireLineCheckExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MyObstacleFireLineCheck': obj.MyObstacleFireLineCheck(),
        'AllyObstacleFireLineCheck': obj.AllyObstacleFireLineCheck(),
        'EnemyObstacleFireLineCheck': obj.EnemyObstacleFireLineCheck(),
        'EmptyObstacleFireLineCheck': obj.EmptyObstacleFireLineCheck(),
    }


def dump_ObstacleStatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StringID': table_encryption.convert_uint(obj.StringID(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'MaxHP1': table_encryption.convert_long(obj.MaxHP1(), password),
        'MaxHP100': table_encryption.convert_long(obj.MaxHP100(), password),
        'BlockRate': table_encryption.convert_long(obj.BlockRate(), password),
        'Dodge': table_encryption.convert_long(obj.Dodge(), password),
        'CanNotStandRange': table_encryption.convert_long(obj.CanNotStandRange(), password),
        'HighlightFloaterHeight': table_encryption.convert_float(obj.HighlightFloaterHeight(), password),
        'EnhanceLightArmorRate': table_encryption.convert_long(obj.EnhanceLightArmorRate(), password),
        'EnhanceHeavyArmorRate': table_encryption.convert_long(obj.EnhanceHeavyArmorRate(), password),
        'EnhanceUnarmedRate': table_encryption.convert_long(obj.EnhanceUnarmedRate(), password),
        'EnhanceElasticArmorRate': table_encryption.convert_long(obj.EnhanceElasticArmorRate(), password),
        'EnhanceStructureRate': table_encryption.convert_long(obj.EnhanceStructureRate(), password),
        'EnhanceNormalArmorRate': table_encryption.convert_long(obj.EnhanceNormalArmorRate(), password),
    }


def dump_OpenConditionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'OpenConditionContentType': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionContentType(), password)).name,
        'LockUI': [table_encryption.convert_string(obj.LockUI(j), password) for j in range(obj.LockUILength())],
        'ShortcutPopupPriority': table_encryption.convert_long(obj.ShortcutPopupPriority(), password),
        'ShortcutUIName': [table_encryption.convert_string(obj.ShortcutUIName(j), password) for j in range(obj.ShortcutUINameLength())],
        'ShortcutParam': table_encryption.convert_int(obj.ShortcutParam(), password),
        'Scene': table_encryption.convert_string(obj.Scene(), password),
        'HideWhenLocked': obj.HideWhenLocked(),
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ScenarioModeId': table_encryption.convert_long(obj.ScenarioModeId(), password),
        'CampaignStageId': table_encryption.convert_long(obj.CampaignStageId(), password),
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'OpenDayOfWeek': WeekDay(table_encryption.convert_int(obj.OpenDayOfWeek(), password)).name,
        'OpenHour': table_encryption.convert_long(obj.OpenHour(), password),
        'CloseDayOfWeek': WeekDay(table_encryption.convert_int(obj.CloseDayOfWeek(), password)).name,
        'CloseHour': table_encryption.convert_long(obj.CloseHour(), password),
        'OpenedCafeId': table_encryption.convert_long(obj.OpenedCafeId(), password),
        'CafeIdforCafeRank': table_encryption.convert_long(obj.CafeIdforCafeRank(), password),
        'CafeRank': table_encryption.convert_long(obj.CafeRank(), password),
        'ContentsOpenShow': obj.ContentsOpenShow(),
        'ContentsOpenShortcutUI': table_encryption.convert_string(obj.ContentsOpenShortcutUI(), password),
    }


def dump_ParcelAutoSynthExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RequireParcelType': ParcelType(table_encryption.convert_int(obj.RequireParcelType(), password)).name,
        'RequireParcelId': table_encryption.convert_long(obj.RequireParcelId(), password),
        'RequireParcelAmount': table_encryption.convert_long(obj.RequireParcelAmount(), password),
        'SynthStartAmount': table_encryption.convert_long(obj.SynthStartAmount(), password),
        'SynthEndAmount': table_encryption.convert_long(obj.SynthEndAmount(), password),
        'SynthMaxItem': obj.SynthMaxItem(),
        'ResultParcelType': ParcelType(table_encryption.convert_int(obj.ResultParcelType(), password)).name,
        'ResultParcelId': table_encryption.convert_long(obj.ResultParcelId(), password),
        'ResultParcelAmount': table_encryption.convert_long(obj.ResultParcelAmount(), password),
    }


def dump_PersonalityExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
    }


def dump_PickupDuplicateBonusExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ShopCategoryType': ShopCategoryType(table_encryption.convert_int(obj.ShopCategoryType_(), password)).name,
        'ShopId': table_encryption.convert_long(obj.ShopId(), password),
        'PickupCharacterId': table_encryption.convert_long(obj.PickupCharacterId(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
    }


def dump_PresetCharacterGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'PresetCharacterGroupId': table_encryption.convert_long(obj.PresetCharacterGroupId(), password),
        'GetPresetType': table_encryption.convert_string(obj.GetPresetType(), password),
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Exp': table_encryption.convert_int(obj.Exp(), password),
        'FavorExp': table_encryption.convert_int(obj.FavorExp(), password),
        'FavorRank': table_encryption.convert_int(obj.FavorRank(), password),
        'StarGrade': table_encryption.convert_int(obj.StarGrade(), password),
        'ExSkillLevel': table_encryption.convert_int(obj.ExSkillLevel(), password),
        'PassiveSkillLevel': table_encryption.convert_int(obj.PassiveSkillLevel(), password),
        'ExtraPassiveSkillLevel': table_encryption.convert_int(obj.ExtraPassiveSkillLevel(), password),
        'CommonSkillLevel': table_encryption.convert_int(obj.CommonSkillLevel(), password),
        'LeaderSkillLevel': table_encryption.convert_int(obj.LeaderSkillLevel(), password),
        'EquipSlot01': obj.EquipSlot01(),
        'EquipSlotTier01': table_encryption.convert_int(obj.EquipSlotTier01(), password),
        'EquipSlotLevel01': table_encryption.convert_int(obj.EquipSlotLevel01(), password),
        'EquipSlot02': obj.EquipSlot02(),
        'EquipSlotTier02': table_encryption.convert_int(obj.EquipSlotTier02(), password),
        'EquipSlotLevel02': table_encryption.convert_int(obj.EquipSlotLevel02(), password),
        'EquipSlot03': obj.EquipSlot03(),
        'EquipSlotTier03': table_encryption.convert_int(obj.EquipSlotTier03(), password),
        'EquipSlotLevel03': table_encryption.convert_int(obj.EquipSlotLevel03(), password),
        'EquipCharacterWeapon': obj.EquipCharacterWeapon(),
        'EquipCharacterWeaponTier': table_encryption.convert_int(obj.EquipCharacterWeaponTier(), password),
        'EquipCharacterWeaponLevel': table_encryption.convert_int(obj.EquipCharacterWeaponLevel(), password),
        'EquipCharacterGear': obj.EquipCharacterGear(),
        'EquipCharacterGearTier': table_encryption.convert_int(obj.EquipCharacterGearTier(), password),
        'EquipCharacterGearLevel': table_encryption.convert_int(obj.EquipCharacterGearLevel(), password),
        'PotentialType01': PotentialStatBonusRateType(table_encryption.convert_int(obj.PotentialType01(), password)).name,
        'PotentialLevel01': table_encryption.convert_int(obj.PotentialLevel01(), password),
        'PotentialType02': PotentialStatBonusRateType(table_encryption.convert_int(obj.PotentialType02(), password)).name,
        'PotentialLevel02': table_encryption.convert_int(obj.PotentialLevel02(), password),
        'PotentialType03': PotentialStatBonusRateType(table_encryption.convert_int(obj.PotentialType03(), password)).name,
        'PotentialLevel03': table_encryption.convert_int(obj.PotentialLevel03(), password),
    }


def dump_PresetCharacterGroupSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'ArenaSimulatorFixed': obj.ArenaSimulatorFixed(),
        'PresetType': [table_encryption.convert_string(obj.PresetType(j), password) for j in range(obj.PresetTypeLength())],
    }


def dump_PresetParcelsExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'PresetGroupId': table_encryption.convert_long(obj.PresetGroupId(), password),
        'ParcelAmount': table_encryption.convert_long(obj.ParcelAmount(), password),
    }


def dump_ProductExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductId': table_encryption.convert_string(obj.ProductId(), password),
        'StoreType': StoreType(table_encryption.convert_int(obj.StoreType_(), password)).name,
        'Price': table_encryption.convert_long(obj.Price(), password),
        'PriceReference': table_encryption.convert_string(obj.PriceReference(), password),
        'PurchasePeriodType': PurchasePeriodType(table_encryption.convert_int(obj.PurchasePeriodType_(), password)).name,
        'PurchasePeriodLimit': table_encryption.convert_long(obj.PurchasePeriodLimit(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelAmount': [table_encryption.convert_long(obj.ParcelAmount(j), password) for j in range(obj.ParcelAmountLength())],
    }


def dump_ProductMonthlyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductId': table_encryption.convert_string(obj.ProductId(), password),
        'StoreType': StoreType(table_encryption.convert_int(obj.StoreType_(), password)).name,
        'Price': table_encryption.convert_long(obj.Price(), password),
        'PriceReference': table_encryption.convert_string(obj.PriceReference(), password),
        'ProductTagType': ProductTagType(table_encryption.convert_int(obj.ProductTagType_(), password)).name,
        'MonthlyDays': table_encryption.convert_long(obj.MonthlyDays(), password),
        'UseMonthlyProductCheck': obj.UseMonthlyProductCheck(),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelAmount': [table_encryption.convert_long(obj.ParcelAmount(j), password) for j in range(obj.ParcelAmountLength())],
        'EnterCostReduceGroupId': table_encryption.convert_long(obj.EnterCostReduceGroupId(), password),
        'DailyParcelType': [ParcelType(table_encryption.convert_int(obj.DailyParcelType(j), password)).name for j in range(obj.DailyParcelTypeLength())],
        'DailyParcelId': [table_encryption.convert_long(obj.DailyParcelId(j), password) for j in range(obj.DailyParcelIdLength())],
        'DailyParcelAmount': [table_encryption.convert_long(obj.DailyParcelAmount(j), password) for j in range(obj.DailyParcelAmountLength())],
    }


def dump_PropVector3(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_float(obj.X(), password),
        'Y': table_encryption.convert_float(obj.Y(), password),
        'Z': table_encryption.convert_float(obj.Z(), password),
    }


def dump_PropMotion(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_string(obj.Name(), password),
        'Positions': [dump_PropVector3(obj.Positions(j), password) for j in range(obj.PositionsLength())],
        'Rotations': [dump_PropVector3(obj.Rotations(j), password) for j in range(obj.RotationsLength())],
    }


def dump_PropRootMotionFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RootMotions': [dump_PropMotion(obj.RootMotions(j), password) for j in range(obj.RootMotionsLength())],
    }


def dump_ProtocolSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Protocol': table_encryption.convert_string(obj.Protocol(), password),
        'OpenConditionContent': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionContent_(), password)).name,
        'Currency': obj.Currency(),
        'Inventory': obj.Inventory(),
        'Mail': obj.Mail(),
    }


def dump_RaidRankingRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RankingRewardGroupId': table_encryption.convert_long(obj.RankingRewardGroupId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RankStart': table_encryption.convert_long(obj.RankStart(), password),
        'RankEnd': table_encryption.convert_long(obj.RankEnd(), password),
        'PercentRankStart': table_encryption.convert_long(obj.PercentRankStart(), password),
        'PercentRankEnd': table_encryption.convert_long(obj.PercentRankEnd(), password),
        'Tier': table_encryption.convert_int(obj.Tier(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelUniqueId': [table_encryption.convert_long(obj.RewardParcelUniqueId(j), password) for j in range(obj.RewardParcelUniqueIdLength())],
        'RewardParcelUniqueName': [table_encryption.convert_string(obj.RewardParcelUniqueName(j), password) for j in range(obj.RewardParcelUniqueNameLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_RaidSeasonManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'SeasonDisplay': table_encryption.convert_long(obj.SeasonDisplay(), password),
        'SeasonStartData': table_encryption.convert_string(obj.SeasonStartData(), password),
        'SeasonEndData': table_encryption.convert_string(obj.SeasonEndData(), password),
        'SettlementEndDate': table_encryption.convert_string(obj.SettlementEndDate(), password),
        'OpenRaidBossGroup': [table_encryption.convert_string(obj.OpenRaidBossGroup(j), password) for j in range(obj.OpenRaidBossGroupLength())],
        'RankingRewardGroupId': table_encryption.convert_long(obj.RankingRewardGroupId(), password),
        'MaxSeasonRewardGauage': table_encryption.convert_int(obj.MaxSeasonRewardGauage(), password),
        'StackedSeasonRewardGauge': [table_encryption.convert_long(obj.StackedSeasonRewardGauge(j), password) for j in range(obj.StackedSeasonRewardGaugeLength())],
        'SeasonRewardId': [table_encryption.convert_long(obj.SeasonRewardId(j), password) for j in range(obj.SeasonRewardIdLength())],
    }


def dump_RaidStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'UseBossIndex': obj.UseBossIndex(),
        'UseBossAIPhaseSync': obj.UseBossAIPhaseSync(),
        'RaidBossGroup': table_encryption.convert_string(obj.RaidBossGroup(), password),
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'BGPath': table_encryption.convert_string(obj.BGPath(), password),
        'RaidCharacterId': table_encryption.convert_long(obj.RaidCharacterId(), password),
        'BossCharacterId': [table_encryption.convert_long(obj.BossCharacterId(j), password) for j in range(obj.BossCharacterIdLength())],
        'Difficulty': Difficulty(table_encryption.convert_int(obj.Difficulty_(), password)).name,
        'DifficultyOpenCondition': obj.DifficultyOpenCondition(),
        'MaxPlayerCount': table_encryption.convert_long(obj.MaxPlayerCount(), password),
        'RaidRoomLifeTime': table_encryption.convert_int(obj.RaidRoomLifeTime(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'GroundDevName': table_encryption.convert_string(obj.GroundDevName(), password),
        'EnterTimeLine': table_encryption.convert_string(obj.EnterTimeLine(), password),
        'TacticEnvironment': TacticEnvironment(table_encryption.convert_int(obj.TacticEnvironment_(), password)).name,
        'DefaultClearScore': table_encryption.convert_long(obj.DefaultClearScore(), password),
        'MaximumScore': table_encryption.convert_long(obj.MaximumScore(), password),
        'PerSecondMinusScore': table_encryption.convert_long(obj.PerSecondMinusScore(), password),
        'HPPercentScore': table_encryption.convert_long(obj.HPPercentScore(), password),
        'MinimumAcquisitionScore': table_encryption.convert_long(obj.MinimumAcquisitionScore(), password),
        'MaximumAcquisitionScore': table_encryption.convert_long(obj.MaximumAcquisitionScore(), password),
        'RaidRewardGroupId': table_encryption.convert_long(obj.RaidRewardGroupId(), password),
        'BattleReadyTimelinePath': [table_encryption.convert_string(obj.BattleReadyTimelinePath(j), password) for j in range(obj.BattleReadyTimelinePathLength())],
        'BattleReadyTimelinePhaseStart': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseStart(j), password) for j in range(obj.BattleReadyTimelinePhaseStartLength())],
        'BattleReadyTimelinePhaseEnd': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseEnd(j), password) for j in range(obj.BattleReadyTimelinePhaseEndLength())],
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'PhaseChangeTimelinePath': table_encryption.convert_string(obj.PhaseChangeTimelinePath(), password),
        'TimeLinePhase': table_encryption.convert_long(obj.TimeLinePhase(), password),
        'EnterScenarioKey': table_encryption.convert_uint(obj.EnterScenarioKey(), password),
        'ClearScenarioKey': table_encryption.convert_uint(obj.ClearScenarioKey(), password),
        'ShowSkillCard': obj.ShowSkillCard(),
        'BossBGInfoKey': table_encryption.convert_uint(obj.BossBGInfoKey(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_RaidStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'IsClearStageRewardHideInfo': obj.IsClearStageRewardHideInfo(),
        'ClearStageRewardProb': table_encryption.convert_long(obj.ClearStageRewardProb(), password),
        'ClearStageRewardParcelType': ParcelType(table_encryption.convert_int(obj.ClearStageRewardParcelType(), password)).name,
        'ClearStageRewardParcelUniqueID': table_encryption.convert_long(obj.ClearStageRewardParcelUniqueID(), password),
        'ClearStageRewardParcelUniqueName': table_encryption.convert_string(obj.ClearStageRewardParcelUniqueName(), password),
        'ClearStageRewardAmount': table_encryption.convert_long(obj.ClearStageRewardAmount(), password),
    }


def dump_RaidStageSeasonRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonRewardId': table_encryption.convert_long(obj.SeasonRewardId(), password),
        'SeasonRewardParcelType': [ParcelType(table_encryption.convert_int(obj.SeasonRewardParcelType(j), password)).name for j in range(obj.SeasonRewardParcelTypeLength())],
        'SeasonRewardParcelUniqueId': [table_encryption.convert_long(obj.SeasonRewardParcelUniqueId(j), password) for j in range(obj.SeasonRewardParcelUniqueIdLength())],
        'SeasonRewardParcelUniqueName': [table_encryption.convert_string(obj.SeasonRewardParcelUniqueName(j), password) for j in range(obj.SeasonRewardParcelUniqueNameLength())],
        'SeasonRewardAmount': [table_encryption.convert_long(obj.SeasonRewardAmount(j), password) for j in range(obj.SeasonRewardAmountLength())],
    }


def dump_RecipeCraftExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'RecipeType': RecipeType(table_encryption.convert_int(obj.RecipeType_(), password)).name,
        'RecipeIngredientId': table_encryption.convert_long(obj.RecipeIngredientId(), password),
        'RecipeIngredientDevName': table_encryption.convert_string(obj.RecipeIngredientDevName(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelDevName': [table_encryption.convert_string(obj.ParcelDevName(j), password) for j in range(obj.ParcelDevNameLength())],
        'ResultAmountMin': [table_encryption.convert_long(obj.ResultAmountMin(j), password) for j in range(obj.ResultAmountMinLength())],
        'ResultAmountMax': [table_encryption.convert_long(obj.ResultAmountMax(j), password) for j in range(obj.ResultAmountMaxLength())],
    }


def dump_RecipeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RecipeType': RecipeType(table_encryption.convert_int(obj.RecipeType_(), password)).name,
        'RecipeIngredientId': table_encryption.convert_long(obj.RecipeIngredientId(), password),
        'RecipeSelectionGroupId': table_encryption.convert_long(obj.RecipeSelectionGroupId(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ResultAmountMin': [table_encryption.convert_long(obj.ResultAmountMin(j), password) for j in range(obj.ResultAmountMinLength())],
        'ResultAmountMax': [table_encryption.convert_long(obj.ResultAmountMax(j), password) for j in range(obj.ResultAmountMaxLength())],
    }


def dump_RecipeIngredientExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RecipeType': RecipeType(table_encryption.convert_int(obj.RecipeType_(), password)).name,
        'CostParcelType': [ParcelType(table_encryption.convert_int(obj.CostParcelType(j), password)).name for j in range(obj.CostParcelTypeLength())],
        'CostId': [table_encryption.convert_long(obj.CostId(j), password) for j in range(obj.CostIdLength())],
        'CostAmount': [table_encryption.convert_long(obj.CostAmount(j), password) for j in range(obj.CostAmountLength())],
        'IngredientParcelType': [ParcelType(table_encryption.convert_int(obj.IngredientParcelType(j), password)).name for j in range(obj.IngredientParcelTypeLength())],
        'IngredientId': [table_encryption.convert_long(obj.IngredientId(j), password) for j in range(obj.IngredientIdLength())],
        'IngredientAmount': [table_encryption.convert_long(obj.IngredientAmount(j), password) for j in range(obj.IngredientAmountLength())],
        'CostTimeInSecond': table_encryption.convert_long(obj.CostTimeInSecond(), password),
    }


def dump_RecipeSelectionAutoUseExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'TargetItemId': table_encryption.convert_long(obj.TargetItemId(), password),
        'Priority': [table_encryption.convert_long(obj.Priority(j), password) for j in range(obj.PriorityLength())],
    }


def dump_RecipeSelectionGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RecipeSelectionGroupId': table_encryption.convert_long(obj.RecipeSelectionGroupId(), password),
        'RecipeSelectionGroupComponentId': table_encryption.convert_long(obj.RecipeSelectionGroupComponentId(), password),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'ResultAmountMin': table_encryption.convert_long(obj.ResultAmountMin(), password),
        'ResultAmountMax': table_encryption.convert_long(obj.ResultAmountMax(), password),
    }


def dump_Position(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_float(obj.X(), password),
        'Z': table_encryption.convert_float(obj.Z(), password),
    }


def dump_Motion(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_string(obj.Name(), password),
        'Positions': [dump_Position(obj.Positions(j), password) for j in range(obj.PositionsLength())],
    }


def dump_MoveEnd(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Normal': dump_Motion(obj.Normal(), password),
        'Stand': dump_Motion(obj.Stand(), password),
        'Kneel': dump_Motion(obj.Kneel(), password),
    }


def dump_Form(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MoveEnd': dump_MoveEnd(obj.MoveEnd(), password),
        'PublicSkill': dump_Motion(obj.PublicSkill(), password),
    }


def dump_RootMotionFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Forms': [dump_Form(obj.Forms(j), password) for j in range(obj.FormsLength())],
        'ExSkills': [dump_Motion(obj.ExSkills(j), password) for j in range(obj.ExSkillsLength())],
        'MoveLeft': dump_Motion(obj.MoveLeft(), password),
        'MoveRight': dump_Motion(obj.MoveRight(), password),
    }


def dump_ScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'None_': [ScenarioBGType(table_encryption.convert_int(obj.None_(j), password)).name for j in range(obj.None_Length())],
        'Idle': [ScenarioCharacterAction(table_encryption.convert_int(obj.Idle(j), password)).name for j in range(obj.IdleLength())],
        'Cafe': DialogCategory(table_encryption.convert_int(obj.Cafe(), password)).name,
        'Talk': DialogType(table_encryption.convert_int(obj.Talk(), password)).name,
        'Open': StoryCondition(table_encryption.convert_int(obj.Open(), password)).name,
        'EnterConver': EmojiEvent(table_encryption.convert_int(obj.EnterConver(), password)).name,
        'Center': ScenarioZoomAnchors(table_encryption.convert_int(obj.Center(), password)).name,
        'Instant': ScenarioZoomType(table_encryption.convert_int(obj.Instant(), password)).name,
        'Prologue': ScenarioContentType(table_encryption.convert_int(obj.Prologue(), password)).name,
    }


def dump_ScenarioReplayExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ModeId': table_encryption.convert_long(obj.ModeId(), password),
        'VolumeId': table_encryption.convert_long(obj.VolumeId(), password),
        'ReplayType': ScenarioModeReplayTypes(table_encryption.convert_int(obj.ReplayType(), password)).name,
        'ChapterId': table_encryption.convert_long(obj.ChapterId(), password),
        'EpisodeId': table_encryption.convert_long(obj.EpisodeId(), password),
        'FrontScenarioGroupId': [table_encryption.convert_long(obj.FrontScenarioGroupId(j), password) for j in range(obj.FrontScenarioGroupIdLength())],
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'BackScenarioGroupId': [table_encryption.convert_long(obj.BackScenarioGroupId(j), password) for j in range(obj.BackScenarioGroupIdLength())],
    }


def dump_ScenarioScriptField1Excel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'SelectionGroup': table_encryption.convert_long(obj.SelectionGroup(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'Sound': table_encryption.convert_string(obj.Sound(), password),
        'Transition': table_encryption.convert_uint(obj.Transition(), password),
        'BGName': table_encryption.convert_uint(obj.BGName(), password),
        'BGEffect': table_encryption.convert_uint(obj.BGEffect(), password),
        'PopupFileName': table_encryption.convert_string(obj.PopupFileName(), password),
        'ScriptKr': table_encryption.convert_string(obj.ScriptKr(), password),
        'TextJp': table_encryption.convert_string(obj.TextJp(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_SchoolDungeonRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'DungeonType': SchoolDungeonType(table_encryption.convert_int(obj.DungeonType(), password)).name,
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
        'RewardParcelProbability': table_encryption.convert_long(obj.RewardParcelProbability(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_SchoolDungeonStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'DungeonType': SchoolDungeonType(table_encryption.convert_int(obj.DungeonType(), password)).name,
        'Difficulty': table_encryption.convert_int(obj.Difficulty(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'StageEnterCostType': [ParcelType(table_encryption.convert_int(obj.StageEnterCostType(j), password)).name for j in range(obj.StageEnterCostTypeLength())],
        'StageEnterCostId': [table_encryption.convert_long(obj.StageEnterCostId(j), password) for j in range(obj.StageEnterCostIdLength())],
        'StageEnterCostAmount': [table_encryption.convert_long(obj.StageEnterCostAmount(j), password) for j in range(obj.StageEnterCostAmountLength())],
        'StageEnterCostMinimumAmount': [table_encryption.convert_long(obj.StageEnterCostMinimumAmount(j), password) for j in range(obj.StageEnterCostMinimumAmountLength())],
        'GroundId': table_encryption.convert_int(obj.GroundId(), password),
        'StarGoal': [StarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_long(obj.RecommandLevel(), password),
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_long(obj.PlayTimeLimitInSeconds(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_ShiftingCraftRecipeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'NotificationId': table_encryption.convert_int(obj.NotificationId(), password),
        'ResultParcel': ParcelType(table_encryption.convert_int(obj.ResultParcel(), password)).name,
        'ResultId': table_encryption.convert_long(obj.ResultId(), password),
        'ResultAmount': table_encryption.convert_long(obj.ResultAmount(), password),
        'RequireItemId': table_encryption.convert_long(obj.RequireItemId(), password),
        'RequireItemAmount': table_encryption.convert_long(obj.RequireItemAmount(), password),
        'RequireGold': table_encryption.convert_long(obj.RequireGold(), password),
        'IngredientTag': [Tag(table_encryption.convert_int(obj.IngredientTag(j), password)).name for j in range(obj.IngredientTagLength())],
        'IngredientExp': table_encryption.convert_long(obj.IngredientExp(), password),
    }


def dump_ShopCashExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CashProductId': table_encryption.convert_long(obj.CashProductId(), password),
        'PackageType': PurchaseSourceType(table_encryption.convert_int(obj.PackageType(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'RenewalDisplayOrder': table_encryption.convert_long(obj.RenewalDisplayOrder(), password),
        'CategoryType': ProductCategory(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'DisplayTag': ProductDisplayTag(table_encryption.convert_int(obj.DisplayTag(), password)).name,
        'SalePeriodFrom': table_encryption.convert_string(obj.SalePeriodFrom(), password),
        'SalePeriodTo': table_encryption.convert_string(obj.SalePeriodTo(), password),
        'PeriodTag': obj.PeriodTag(),
        'AccountLevelLimit': table_encryption.convert_long(obj.AccountLevelLimit(), password),
        'AccountLevelHide': obj.AccountLevelHide(),
        'ClearMissionLimit': table_encryption.convert_long(obj.ClearMissionLimit(), password),
        'ClearMissionHide': obj.ClearMissionHide(),
        'PurchaseReportEventName': table_encryption.convert_string(obj.PurchaseReportEventName(), password),
    }


def dump_ShopCashScenarioResourceInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ScenarioResrouceInfoId': table_encryption.convert_long(obj.ScenarioResrouceInfoId(), password),
        'ShopCashId': table_encryption.convert_long(obj.ShopCashId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
    }


def dump_ShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'SalePeriodFrom': table_encryption.convert_string(obj.SalePeriodFrom(), password),
        'SalePeriodTo': table_encryption.convert_string(obj.SalePeriodTo(), password),
        'PurchaseCooltimeMin': table_encryption.convert_long(obj.PurchaseCooltimeMin(), password),
        'PurchaseCountLimit': table_encryption.convert_long(obj.PurchaseCountLimit(), password),
        'PurchaseCountResetType': PurchaseCountResetType(table_encryption.convert_int(obj.PurchaseCountResetType_(), password)).name,
        'BuyReportEventName': table_encryption.convert_string(obj.BuyReportEventName(), password),
        'RestrictBuyWhenInventoryFull': obj.RestrictBuyWhenInventoryFull(),
        'DisplayTag': ProductDisplayTag(table_encryption.convert_int(obj.DisplayTag(), password)).name,
        'ShopUpdateGroupId': table_encryption.convert_int(obj.ShopUpdateGroupId(), password),
    }


def dump_ShopFilterClassifiedExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'ConsumeParcelType': ParcelType(table_encryption.convert_int(obj.ConsumeParcelType(), password)).name,
        'ConsumeParcelId': table_encryption.convert_long(obj.ConsumeParcelId(), password),
        'ShopFilterType': ShopFilterType(table_encryption.convert_int(obj.ShopFilterType_(), password)).name,
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
    }


def dump_ShopFreeRecruitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'FreeRecruitPeriodFrom': table_encryption.convert_string(obj.FreeRecruitPeriodFrom(), password),
        'FreeRecruitPeriodTo': table_encryption.convert_string(obj.FreeRecruitPeriodTo(), password),
        'FreeRecruitType': ShopFreeRecruitType(table_encryption.convert_int(obj.FreeRecruitType(), password)).name,
        'FreeRecruitDecorationImagePath': table_encryption.convert_string(obj.FreeRecruitDecorationImagePath(), password),
        'ShopRecruitId': [table_encryption.convert_long(obj.ShopRecruitId(j), password) for j in range(obj.ShopRecruitIdLength())],
    }


def dump_ShopFreeRecruitPeriodExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ShopFreeRecruitId': table_encryption.convert_long(obj.ShopFreeRecruitId(), password),
        'ShopFreeRecruitIntervalId': table_encryption.convert_long(obj.ShopFreeRecruitIntervalId(), password),
        'IntervalDate': table_encryption.convert_string(obj.IntervalDate(), password),
        'FreeRecruitCount': table_encryption.convert_int(obj.FreeRecruitCount(), password),
    }


def dump_ShopInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsRefresh': obj.IsRefresh(),
        'IsSoldOutDimmed': obj.IsSoldOutDimmed(),
        'CostParcelType': [ParcelType(table_encryption.convert_int(obj.CostParcelType(j), password)).name for j in range(obj.CostParcelTypeLength())],
        'CostParcelId': [table_encryption.convert_long(obj.CostParcelId(j), password) for j in range(obj.CostParcelIdLength())],
        'AutoRefreshCoolTime': table_encryption.convert_long(obj.AutoRefreshCoolTime(), password),
        'RefreshAbleCount': table_encryption.convert_long(obj.RefreshAbleCount(), password),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'OpenPeriodFrom': table_encryption.convert_string(obj.OpenPeriodFrom(), password),
        'OpenPeriodTo': table_encryption.convert_string(obj.OpenPeriodTo(), password),
        'ShopProductUpdateTime': table_encryption.convert_string(obj.ShopProductUpdateTime(), password),
        'DisplayParcelType': ParcelType(table_encryption.convert_int(obj.DisplayParcelType(), password)).name,
        'DisplayParcelId': table_encryption.convert_long(obj.DisplayParcelId(), password),
        'IsShopVisible': obj.IsShopVisible(),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'ShopUpdateDate': table_encryption.convert_int(obj.ShopUpdateDate(), password),
        'ShopUpdateGroupId1': table_encryption.convert_int(obj.ShopUpdateGroupId1(), password),
        'ShopUpdateGroupId2': table_encryption.convert_int(obj.ShopUpdateGroupId2(), password),
        'ShopUpdateGroupId3': table_encryption.convert_int(obj.ShopUpdateGroupId3(), password),
        'ShopUpdateGroupId4': table_encryption.convert_int(obj.ShopUpdateGroupId4(), password),
        'ShopUpdateGroupId5': table_encryption.convert_int(obj.ShopUpdateGroupId5(), password),
        'ShopUpdateGroupId6': table_encryption.convert_int(obj.ShopUpdateGroupId6(), password),
        'ShopUpdateGroupId7': table_encryption.convert_int(obj.ShopUpdateGroupId7(), password),
        'ShopUpdateGroupId8': table_encryption.convert_int(obj.ShopUpdateGroupId8(), password),
        'ShopUpdateGroupId9': table_encryption.convert_int(obj.ShopUpdateGroupId9(), password),
        'ShopUpdateGroupId10': table_encryption.convert_int(obj.ShopUpdateGroupId10(), password),
        'ShopUpdateGroupId11': table_encryption.convert_int(obj.ShopUpdateGroupId11(), password),
        'ShopUpdateGroupId12': table_encryption.convert_int(obj.ShopUpdateGroupId12(), password),
    }


def dump_ShopRecruitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'OneGachaGoodsId': table_encryption.convert_long(obj.OneGachaGoodsId(), password),
        'TenGachaGoodsId': table_encryption.convert_long(obj.TenGachaGoodsId(), password),
        'GoodsDevName': table_encryption.convert_string(obj.GoodsDevName(), password),
        'DisplayTag': GachaDisplayTag(table_encryption.convert_int(obj.DisplayTag(), password)).name,
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'GachaBannerPath': table_encryption.convert_string(obj.GachaBannerPath(), password),
        'VideoId': [table_encryption.convert_long(obj.VideoId(j), password) for j in range(obj.VideoIdLength())],
        'LinkedRobbyBannerId': table_encryption.convert_long(obj.LinkedRobbyBannerId(), password),
        'InfoCharacterId': [table_encryption.convert_long(obj.InfoCharacterId(j), password) for j in range(obj.InfoCharacterIdLength())],
        'SalePeriodFrom': table_encryption.convert_string(obj.SalePeriodFrom(), password),
        'SalePeriodTo': table_encryption.convert_string(obj.SalePeriodTo(), password),
        'RecruitCoinId': table_encryption.convert_long(obj.RecruitCoinId(), password),
        'RecruitSellectionShopId': table_encryption.convert_long(obj.RecruitSellectionShopId(), password),
        'PurchaseCooltimeMin': table_encryption.convert_long(obj.PurchaseCooltimeMin(), password),
        'PurchaseCountLimit': table_encryption.convert_long(obj.PurchaseCountLimit(), password),
        'PurchaseCountResetType': PurchaseCountResetType(table_encryption.convert_int(obj.PurchaseCountResetType_(), password)).name,
        'IsNewbie': obj.IsNewbie(),
        'IsSelectRecruit': obj.IsSelectRecruit(),
        'DirectPayInvisibleTokenId': table_encryption.convert_long(obj.DirectPayInvisibleTokenId(), password),
        'DirectPayAndroidShopCashId': table_encryption.convert_long(obj.DirectPayAndroidShopCashId(), password),
        'DirectPayAppleShopCashId': table_encryption.convert_long(obj.DirectPayAppleShopCashId(), password),
    }


def dump_ShopRefreshExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
        'IsBundle': obj.IsBundle(),
        'VisibleAmount': table_encryption.convert_long(obj.VisibleAmount(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'RefreshGroup': table_encryption.convert_int(obj.RefreshGroup(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'BuyReportEventName': table_encryption.convert_string(obj.BuyReportEventName(), password),
        'DisplayTag': ProductDisplayTag(table_encryption.convert_int(obj.DisplayTag(), password)).name,
    }


def dump_SkillExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeSkillId': table_encryption.convert_uint(obj.LocalizeSkillId(), password),
        'GroupId': table_encryption.convert_string(obj.GroupId(), password),
        'SkillDataKey': table_encryption.convert_string(obj.SkillDataKey(), password),
        'VisualDataKey': table_encryption.convert_string(obj.VisualDataKey(), password),
        'Level': table_encryption.convert_int(obj.Level(), password),
        'SkillCost': table_encryption.convert_int(obj.SkillCost(), password),
        'ExtraSkillCost': table_encryption.convert_int(obj.ExtraSkillCost(), password),
        'EnemySkillCost': table_encryption.convert_int(obj.EnemySkillCost(), password),
        'ExtraEnemySkillCost': table_encryption.convert_int(obj.ExtraEnemySkillCost(), password),
        'NPCSkillCost': table_encryption.convert_int(obj.NPCSkillCost(), password),
        'ExtraNPCSkillCost': table_encryption.convert_int(obj.ExtraNPCSkillCost(), password),
        'BulletType': BulletType(table_encryption.convert_int(obj.BulletType_(), password)).name,
        'StartCoolTime': table_encryption.convert_int(obj.StartCoolTime(), password),
        'CoolTime': table_encryption.convert_int(obj.CoolTime(), password),
        'EnemyStartCoolTime': table_encryption.convert_int(obj.EnemyStartCoolTime(), password),
        'EnemyCoolTime': table_encryption.convert_int(obj.EnemyCoolTime(), password),
        'NPCStartCoolTime': table_encryption.convert_int(obj.NPCStartCoolTime(), password),
        'NPCCoolTime': table_encryption.convert_int(obj.NPCCoolTime(), password),
        'UseAtg': table_encryption.convert_int(obj.UseAtg(), password),
        'RequireCharacterLevel': table_encryption.convert_int(obj.RequireCharacterLevel(), password),
        'RequireLevelUpMaterial': table_encryption.convert_long(obj.RequireLevelUpMaterial(), password),
        'IconName': table_encryption.convert_string(obj.IconName(), password),
        'IsShowInfo': obj.IsShowInfo(),
        'IsShowSpeechbubble': obj.IsShowSpeechbubble(),
        'PublicSpeechDuration': table_encryption.convert_int(obj.PublicSpeechDuration(), password),
        'AdditionalToolTipId': table_encryption.convert_long(obj.AdditionalToolTipId(), password),
        'TextureSkillCardForFormConversion': table_encryption.convert_string(obj.TextureSkillCardForFormConversion(), password),
        'SkillCardLabelPath': table_encryption.convert_string(obj.SkillCardLabelPath(), password),
    }


def dump_SpecialLobbyIllustExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'CharacterCostumeUniqueId': table_encryption.convert_long(obj.CharacterCostumeUniqueId(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'SlotTextureName': table_encryption.convert_string(obj.SlotTextureName(), password),
        'RewardTextureName': table_encryption.convert_string(obj.RewardTextureName(), password),
    }


def dump_StatLevelInterpolationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Level': table_encryption.convert_long(obj.Level(), password),
        'StatTypeIndex': [table_encryption.convert_long(obj.StatTypeIndex(j), password) for j in range(obj.StatTypeIndexLength())],
    }


def dump_StickerGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Layout': table_encryption.convert_string(obj.Layout(), password),
        'UniqueLayoutPath': table_encryption.convert_string(obj.UniqueLayoutPath(), password),
        'StickerGroupIconpath': table_encryption.convert_string(obj.StickerGroupIconpath(), password),
        'PageCompleteSlot': table_encryption.convert_long(obj.PageCompleteSlot(), password),
        'PageCompleteRewardParcelType': ParcelType(table_encryption.convert_int(obj.PageCompleteRewardParcelType(), password)).name,
        'PageCompleteRewardParcelId': table_encryption.convert_long(obj.PageCompleteRewardParcelId(), password),
        'PageCompleteRewardAmount': table_encryption.convert_int(obj.PageCompleteRewardAmount(), password),
        'LocalizeTitle': table_encryption.convert_uint(obj.LocalizeTitle(), password),
        'LocalizeDescription': table_encryption.convert_uint(obj.LocalizeDescription(), password),
        'StickerGroupCoverpath': table_encryption.convert_string(obj.StickerGroupCoverpath(), password),
    }


def dump_StickerPageContentExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StickerGroupId': table_encryption.convert_long(obj.StickerGroupId(), password),
        'StickerPageId': table_encryption.convert_long(obj.StickerPageId(), password),
        'StickerSlot': table_encryption.convert_long(obj.StickerSlot(), password),
        'StickerGetConditionType': StickerGetConditionType(table_encryption.convert_int(obj.StickerGetConditionType_(), password)).name,
        'StickerCheckPassType': StickerCheckPassType(table_encryption.convert_int(obj.StickerCheckPassType_(), password)).name,
        'GetStickerConditionType': GetStickerConditionType(table_encryption.convert_int(obj.GetStickerConditionType_(), password)).name,
        'StickerGetConditionCount': table_encryption.convert_long(obj.StickerGetConditionCount(), password),
        'StickerGetConditionParameter': [table_encryption.convert_long(obj.StickerGetConditionParameter(j), password) for j in range(obj.StickerGetConditionParameterLength())],
        'StickerGetConditionParameterTag': [Tag(table_encryption.convert_int(obj.StickerGetConditionParameterTag(j), password)).name for j in range(obj.StickerGetConditionParameterTagLength())],
        'PackedStickerIconLocalizeEtcId': table_encryption.convert_uint(obj.PackedStickerIconLocalizeEtcId(), password),
        'PackedStickerIconPath': table_encryption.convert_string(obj.PackedStickerIconPath(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'StickerDetailPath': table_encryption.convert_string(obj.StickerDetailPath(), password),
    }


def dump_StrategyObjectBuffDefineExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StrategyObjectBuffID': table_encryption.convert_long(obj.StrategyObjectBuffID(), password),
        'StrategyObjectTurn': table_encryption.convert_int(obj.StrategyObjectTurn(), password),
        'SkillGroupId': table_encryption.convert_string(obj.SkillGroupId(), password),
        'LocalizeCodeId': table_encryption.convert_uint(obj.LocalizeCodeId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
    }


def dump_StringTestExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'String': [table_encryption.convert_string(obj.String(j), password) for j in range(obj.StringLength())],
        'Sentence1': table_encryption.convert_string(obj.Sentence1(), password),
        'Script': table_encryption.convert_string(obj.Script(), password),
    }


def dump_SystemMailExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MailType': MailType(table_encryption.convert_int(obj.MailType_(), password)).name,
        'ExpiredDay': table_encryption.convert_long(obj.ExpiredDay(), password),
        'Sender': table_encryption.convert_string(obj.Sender(), password),
        'Comment': table_encryption.convert_string(obj.Comment(), password),
    }


def dump_TacticalSupportSystemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'SummonedTime': table_encryption.convert_long(obj.SummonedTime(), password),
        'DefaultPersonalityId': table_encryption.convert_long(obj.DefaultPersonalityId(), password),
        'CanTargeting': obj.CanTargeting(),
        'CanCover': obj.CanCover(),
        'ObstacleUniqueName': table_encryption.convert_string(obj.ObstacleUniqueName(), password),
        'ObstacleCoverRange': table_encryption.convert_long(obj.ObstacleCoverRange(), password),
        'SummonSkilllGroupId': table_encryption.convert_string(obj.SummonSkilllGroupId(), password),
        'CrashObstacleOBBWidth': table_encryption.convert_long(obj.CrashObstacleOBBWidth(), password),
        'CrashObstacleOBBHeight': table_encryption.convert_long(obj.CrashObstacleOBBHeight(), password),
        'IsTSSBlockedNodeCheck': obj.IsTSSBlockedNodeCheck(),
        'NumberOfUses': table_encryption.convert_int(obj.NumberOfUses(), password),
        'InventoryOffsetX': table_encryption.convert_float(obj.InventoryOffsetX(), password),
        'InventoryOffsetY': table_encryption.convert_float(obj.InventoryOffsetY(), password),
        'InventoryOffsetZ': table_encryption.convert_float(obj.InventoryOffsetZ(), password),
        'InteractionChar': table_encryption.convert_long(obj.InteractionChar(), password),
        'CharacterInteractionStartDelay': table_encryption.convert_long(obj.CharacterInteractionStartDelay(), password),
        'GetOnStartEffectPath': table_encryption.convert_string(obj.GetOnStartEffectPath(), password),
        'GetOnEndEffectPath': table_encryption.convert_string(obj.GetOnEndEffectPath(), password),
        'SummonerCharacterId': table_encryption.convert_long(obj.SummonerCharacterId(), password),
        'InteractionFrame': table_encryption.convert_int(obj.InteractionFrame(), password),
        'TSAInteractionAddDuration': table_encryption.convert_long(obj.TSAInteractionAddDuration(), password),
        'InteractionStudentExSkillGroupId': table_encryption.convert_string(obj.InteractionStudentExSkillGroupId(), password),
        'InteractionSkillCardTexture': table_encryption.convert_string(obj.InteractionSkillCardTexture(), password),
        'InteractionSkillSpine': table_encryption.convert_string(obj.InteractionSkillSpine(), password),
        'RetreatFrame': table_encryption.convert_int(obj.RetreatFrame(), password),
        'DestroyFrame': table_encryption.convert_int(obj.DestroyFrame(), password),
    }


def dump_TacticArenaSimulatorSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Order': table_encryption.convert_long(obj.Order(), password),
        'Repeat': table_encryption.convert_long(obj.Repeat(), password),
        'AttackerFrom': ArenaSimulatorServer(table_encryption.convert_int(obj.AttackerFrom(), password)).name,
        'AttackerUserArenaGroup': table_encryption.convert_long(obj.AttackerUserArenaGroup(), password),
        'AttackerUserArenaRank': table_encryption.convert_long(obj.AttackerUserArenaRank(), password),
        'AttackerPresetGroupId': table_encryption.convert_long(obj.AttackerPresetGroupId(), password),
        'AttackerStrikerNum': table_encryption.convert_long(obj.AttackerStrikerNum(), password),
        'AttackerSpecialNum': table_encryption.convert_long(obj.AttackerSpecialNum(), password),
        'DefenderFrom': ArenaSimulatorServer(table_encryption.convert_int(obj.DefenderFrom(), password)).name,
        'DefenderUserArenaGroup': table_encryption.convert_long(obj.DefenderUserArenaGroup(), password),
        'DefenderUserArenaRank': table_encryption.convert_long(obj.DefenderUserArenaRank(), password),
        'DefenderPresetGroupId': table_encryption.convert_long(obj.DefenderPresetGroupId(), password),
        'DefenderStrikerNum': table_encryption.convert_long(obj.DefenderStrikerNum(), password),
        'DefenderSpecialNum': table_encryption.convert_long(obj.DefenderSpecialNum(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
    }


def dump_TacticDamageSimulatorSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Order': table_encryption.convert_int(obj.Order(), password),
        'Repeat': table_encryption.convert_int(obj.Repeat(), password),
        'TestPreset': table_encryption.convert_long(obj.TestPreset(), password),
        'TestBattleTime': table_encryption.convert_long(obj.TestBattleTime(), password),
        'StrikerSquard': table_encryption.convert_long(obj.StrikerSquard(), password),
        'SpecialSquard': table_encryption.convert_long(obj.SpecialSquard(), password),
        'ReplaceCharacterCostRegen': obj.ReplaceCharacterCostRegen(),
        'ReplaceCostRegenValue': table_encryption.convert_int(obj.ReplaceCostRegenValue(), password),
        'UseAutoSkill': obj.UseAutoSkill(),
        'OverrideStreetAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.OverrideStreetAdaptation(), password)).name,
        'OverrideOutdoorAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.OverrideOutdoorAdaptation(), password)).name,
        'OverrideIndoorAdaptation': TerrainAdaptationStat(table_encryption.convert_int(obj.OverrideIndoorAdaptation(), password)).name,
        'ApplyOverrideAdaptation': obj.ApplyOverrideAdaptation(),
        'OverrideFavorLevel': table_encryption.convert_int(obj.OverrideFavorLevel(), password),
        'ApplyOverrideFavorLevel': obj.ApplyOverrideFavorLevel(),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'FixedCharacter': [table_encryption.convert_long(obj.FixedCharacter(j), password) for j in range(obj.FixedCharacterLength())],
    }


def dump_TacticEntityEffectFilterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TargetEffectName': table_encryption.convert_string(obj.TargetEffectName(), password),
        'ShowEffectToVehicle': obj.ShowEffectToVehicle(),
        'ShowEffectToBoss': obj.ShowEffectToBoss(),
    }


def dump_TacticSimulatorSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'GetExp': table_encryption.convert_long(obj.GetExp(), password),
        'GetStarGrade': table_encryption.convert_long(obj.GetStarGrade(), password),
        'Equipment': table_encryption.convert_long(obj.Equipment(), password),
    }


def dump_TacticSkipExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LevelDiff': table_encryption.convert_int(obj.LevelDiff(), password),
        'HPResult': table_encryption.convert_long(obj.HPResult(), password),
    }


def dump_TacticTimeAttackSimulatorConfigExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Order': table_encryption.convert_long(obj.Order(), password),
        'Repeat': table_encryption.convert_long(obj.Repeat(), password),
        'PresetGroupId': table_encryption.convert_long(obj.PresetGroupId(), password),
        'AttackStrikerNum': table_encryption.convert_long(obj.AttackStrikerNum(), password),
        'AttackSpecialNum': table_encryption.convert_long(obj.AttackSpecialNum(), password),
        'GeasId': table_encryption.convert_long(obj.GeasId(), password),
    }


def dump_TerrainAdaptationFactorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TerrainAdaptation': StageTopography(table_encryption.convert_int(obj.TerrainAdaptation(), password)).name,
        'TerrainAdaptationStat': TerrainAdaptationStat(table_encryption.convert_int(obj.TerrainAdaptationStat_(), password)).name,
        'ShotFactor': table_encryption.convert_long(obj.ShotFactor(), password),
        'BlockFactor': table_encryption.convert_long(obj.BlockFactor(), password),
        'AccuracyFactor': table_encryption.convert_long(obj.AccuracyFactor(), password),
        'DodgeFactor': table_encryption.convert_long(obj.DodgeFactor(), password),
        'AttackPowerFactor': table_encryption.convert_long(obj.AttackPowerFactor(), password),
    }


def dump_TimeAttackDungeonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TimeAttackDungeonType': TimeAttackDungeonType(table_encryption.convert_int(obj.TimeAttackDungeonType_(), password)).name,
        'LocalizeEtcKey': table_encryption.convert_uint(obj.LocalizeEtcKey(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'InformationGroupID': table_encryption.convert_long(obj.InformationGroupID(), password),
    }


def dump_TimeAttackDungeonGeasExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TimeAttackDungeonType': TimeAttackDungeonType(table_encryption.convert_int(obj.TimeAttackDungeonType_(), password)).name,
        'LocalizeEtcKey': table_encryption.convert_uint(obj.LocalizeEtcKey(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'ClearDefaultPoint': table_encryption.convert_long(obj.ClearDefaultPoint(), password),
        'ClearTimeWeightPoint': table_encryption.convert_long(obj.ClearTimeWeightPoint(), password),
        'TimeWeightConst': table_encryption.convert_long(obj.TimeWeightConst(), password),
        'Difficulty': table_encryption.convert_int(obj.Difficulty(), password),
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'AllyPassiveSkillId': [table_encryption.convert_string(obj.AllyPassiveSkillId(j), password) for j in range(obj.AllyPassiveSkillIdLength())],
        'AllyPassiveSkillLevel': [table_encryption.convert_int(obj.AllyPassiveSkillLevel(j), password) for j in range(obj.AllyPassiveSkillLevelLength())],
        'EnemyPassiveSkillId': [table_encryption.convert_string(obj.EnemyPassiveSkillId(j), password) for j in range(obj.EnemyPassiveSkillIdLength())],
        'EnemyPassiveSkillLevel': [table_encryption.convert_int(obj.EnemyPassiveSkillLevel(j), password) for j in range(obj.EnemyPassiveSkillLevelLength())],
        'GeasIconPath': [table_encryption.convert_string(obj.GeasIconPath(j), password) for j in range(obj.GeasIconPathLength())],
        'GeasLocalizeEtcKey': [table_encryption.convert_uint(obj.GeasLocalizeEtcKey(j), password) for j in range(obj.GeasLocalizeEtcKeyLength())],
    }


def dump_TimeAttackDungeonRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RewardMaxPoint': table_encryption.convert_long(obj.RewardMaxPoint(), password),
        'RewardType': [TimeAttackDungeonRewardType(table_encryption.convert_int(obj.RewardType(j), password)).name for j in range(obj.RewardTypeLength())],
        'RewardMinPoint': [table_encryption.convert_long(obj.RewardMinPoint(j), password) for j in range(obj.RewardMinPointLength())],
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelDefaultAmount': [table_encryption.convert_long(obj.RewardParcelDefaultAmount(j), password) for j in range(obj.RewardParcelDefaultAmountLength())],
        'RewardParcelMaxAmount': [table_encryption.convert_long(obj.RewardParcelMaxAmount(j), password) for j in range(obj.RewardParcelMaxAmountLength())],
    }


def dump_TimeAttackDungeonSeasonManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'UISlot': table_encryption.convert_long(obj.UISlot(), password),
        'DungeonId': table_encryption.convert_long(obj.DungeonId(), password),
        'DifficultyGeas': [table_encryption.convert_long(obj.DifficultyGeas(j), password) for j in range(obj.DifficultyGeasLength())],
        'TimeAttackDungeonRewardId': table_encryption.convert_long(obj.TimeAttackDungeonRewardId(), password),
        'RoomLifeTimeInSeconds': table_encryption.convert_long(obj.RoomLifeTimeInSeconds(), password),
    }


def dump_TranscendenceRecipeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'CostCurrencyType': CurrencyTypes(table_encryption.convert_int(obj.CostCurrencyType(), password)).name,
        'CostCurrencyAmount': table_encryption.convert_long(obj.CostCurrencyAmount(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelAmount': [table_encryption.convert_int(obj.ParcelAmount(j), password) for j in range(obj.ParcelAmountLength())],
    }


def dump_TrophyCollectionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'LocalizeCodeId': table_encryption.convert_uint(obj.LocalizeCodeId(), password),
        'FurnitureId': [table_encryption.convert_long(obj.FurnitureId(j), password) for j in range(obj.FurnitureIdLength())],
    }


def dump_WeekDungeonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'WeekDungeonType': WeekDungeonType(table_encryption.convert_int(obj.WeekDungeonType_(), password)).name,
        'Difficulty': table_encryption.convert_int(obj.Difficulty(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'StageEnterCostType': [ParcelType(table_encryption.convert_int(obj.StageEnterCostType(j), password)).name for j in range(obj.StageEnterCostTypeLength())],
        'StageEnterCostId': [table_encryption.convert_long(obj.StageEnterCostId(j), password) for j in range(obj.StageEnterCostIdLength())],
        'StageEnterCostAmount': [table_encryption.convert_int(obj.StageEnterCostAmount(j), password) for j in range(obj.StageEnterCostAmountLength())],
        'GroundId': table_encryption.convert_int(obj.GroundId(), password),
        'StarGoal': [StarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_long(obj.RecommandLevel(), password),
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_long(obj.PlayTimeLimitInSeconds(), password),
        'BattleRewardExp': table_encryption.convert_long(obj.BattleRewardExp(), password),
        'BattleRewardPlayerExp': table_encryption.convert_long(obj.BattleRewardPlayerExp(), password),
        'GroupBuffID': [table_encryption.convert_long(obj.GroupBuffID(j), password) for j in range(obj.GroupBuffIDLength())],
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_WeekDungeonFindGiftRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
        'RewardParcelProbability': [table_encryption.convert_long(obj.RewardParcelProbability(j), password) for j in range(obj.RewardParcelProbabilityLength())],
        'DropItemModelPrefabPath': [table_encryption.convert_string(obj.DropItemModelPrefabPath(j), password) for j in range(obj.DropItemModelPrefabPathLength())],
    }


def dump_WeekDungeonGroupBuffExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'WeekDungeonBuffId': table_encryption.convert_long(obj.WeekDungeonBuffId(), password),
        'School': School(table_encryption.convert_int(obj.School_(), password)).name,
        'RecommandLocalizeEtcId': table_encryption.convert_uint(obj.RecommandLocalizeEtcId(), password),
        'FormationLocalizeEtcId': table_encryption.convert_uint(obj.FormationLocalizeEtcId(), password),
        'SkillGroupId': table_encryption.convert_string(obj.SkillGroupId(), password),
    }


def dump_WeekDungeonOpenScheduleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'WeekDay': WeekDay(table_encryption.convert_int(obj.WeekDay_(), password)).name,
        'Open': [WeekDungeonType(table_encryption.convert_int(obj.Open(j), password)).name for j in range(obj.OpenLength())],
    }


def dump_WeekDungeonRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'DungeonType': WeekDungeonType(table_encryption.convert_int(obj.DungeonType(), password)).name,
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
        'RewardParcelProbability': table_encryption.convert_long(obj.RewardParcelProbability(), password),
        'IsDisplayed': obj.IsDisplayed(),
        'DropItemModelPrefabPath': table_encryption.convert_string(obj.DropItemModelPrefabPath(), password),
    }


def dump_WorldRaidBossGroupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'WorldRaidBossGroupId': table_encryption.convert_long(obj.WorldRaidBossGroupId(), password),
        'WorldBossName': table_encryption.convert_string(obj.WorldBossName(), password),
        'WorldBossPopupPortrait': table_encryption.convert_string(obj.WorldBossPopupPortrait(), password),
        'WorldBossPopupBG': table_encryption.convert_string(obj.WorldBossPopupBG(), password),
        'WorldBossParcelPortrait': table_encryption.convert_string(obj.WorldBossParcelPortrait(), password),
        'WorldBossListParcel': table_encryption.convert_string(obj.WorldBossListParcel(), password),
        'WorldBossHP': table_encryption.convert_long(obj.WorldBossHP(), password),
        'UIHideBeforeSpawn': obj.UIHideBeforeSpawn(),
        'HideAnotherBossKilled': obj.HideAnotherBossKilled(),
        'WorldBossClearRewardGroupId': table_encryption.convert_long(obj.WorldBossClearRewardGroupId(), password),
        'AnotherBossKilled': [table_encryption.convert_long(obj.AnotherBossKilled(j), password) for j in range(obj.AnotherBossKilledLength())],
        'EchelonConstraintGroupId': table_encryption.convert_long(obj.EchelonConstraintGroupId(), password),
        'ExclusiveOperatorBossSpawn': table_encryption.convert_string(obj.ExclusiveOperatorBossSpawn(), password),
        'ExclusiveOperatorBossKill': table_encryption.convert_string(obj.ExclusiveOperatorBossKill(), password),
        'ExclusiveOperatorScenarioBattle': table_encryption.convert_string(obj.ExclusiveOperatorScenarioBattle(), password),
        'ExclusiveOperatorBossDamaged': table_encryption.convert_string(obj.ExclusiveOperatorBossDamaged(), password),
        'BossGroupOpenCondition': table_encryption.convert_long(obj.BossGroupOpenCondition(), password),
    }


def dump_WorldRaidConditionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LockUI': [table_encryption.convert_string(obj.LockUI(j), password) for j in range(obj.LockUILength())],
        'HideWhenLocked': obj.HideWhenLocked(),
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ScenarioModeId': [table_encryption.convert_long(obj.ScenarioModeId(j), password) for j in range(obj.ScenarioModeIdLength())],
        'CampaignStageID': [table_encryption.convert_long(obj.CampaignStageID(j), password) for j in range(obj.CampaignStageIDLength())],
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'AfterWhenDate': table_encryption.convert_string(obj.AfterWhenDate(), password),
        'WorldRaidBossKill': [table_encryption.convert_long(obj.WorldRaidBossKill(j), password) for j in range(obj.WorldRaidBossKillLength())],
    }


def dump_WorldRaidFavorBuffExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'WorldRaidFavorRank': table_encryption.convert_long(obj.WorldRaidFavorRank(), password),
        'WorldRaidFavorRankBonus': table_encryption.convert_long(obj.WorldRaidFavorRankBonus(), password),
    }


def dump_WorldRaidSeasonManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EnterTicket': CurrencyTypes(table_encryption.convert_int(obj.EnterTicket(), password)).name,
        'WorldRaidLobbyScene': table_encryption.convert_string(obj.WorldRaidLobbyScene(), password),
        'WorldRaidLobbyBanner': table_encryption.convert_string(obj.WorldRaidLobbyBanner(), password),
        'WorldRaidLobbyBG': table_encryption.convert_string(obj.WorldRaidLobbyBG(), password),
        'WorldRaidLobbyBannerShow': obj.WorldRaidLobbyBannerShow(),
        'SeasonOpenCondition': table_encryption.convert_long(obj.SeasonOpenCondition(), password),
        'WorldRaidLobbyEnterScenario': table_encryption.convert_long(obj.WorldRaidLobbyEnterScenario(), password),
        'CanPlayNotSeasonTime': obj.CanPlayNotSeasonTime(),
        'WorldRaidUniqueThemeLobbyUI': obj.WorldRaidUniqueThemeLobbyUI(),
        'WorldRaidUniqueThemeName': table_encryption.convert_string(obj.WorldRaidUniqueThemeName(), password),
        'CanWorldRaidGemEnter': obj.CanWorldRaidGemEnter(),
        'HideWorldRaidTicketUI': obj.HideWorldRaidTicketUI(),
        'UseWorldRaidCommonToast': obj.UseWorldRaidCommonToast(),
        'OpenRaidBossGroupId': [table_encryption.convert_long(obj.OpenRaidBossGroupId(j), password) for j in range(obj.OpenRaidBossGroupIdLength())],
        'BossSpawnTime': [table_encryption.convert_string(obj.BossSpawnTime(j), password) for j in range(obj.BossSpawnTimeLength())],
        'EliminateTime': [table_encryption.convert_string(obj.EliminateTime(j), password) for j in range(obj.EliminateTimeLength())],
        'ScenarioOutputConditionId': [table_encryption.convert_long(obj.ScenarioOutputConditionId(j), password) for j in range(obj.ScenarioOutputConditionIdLength())],
        'ConditionScenarioGroupid': [table_encryption.convert_long(obj.ConditionScenarioGroupid(j), password) for j in range(obj.ConditionScenarioGroupidLength())],
        'WorldRaidMapEnterOperator': table_encryption.convert_string(obj.WorldRaidMapEnterOperator(), password),
        'UseFavorRankBuff': obj.UseFavorRankBuff(),
    }


def dump_WorldRaidStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'UseBossIndex': obj.UseBossIndex(),
        'UseBossAIPhaseSync': obj.UseBossAIPhaseSync(),
        'WorldRaidBossGroupId': table_encryption.convert_long(obj.WorldRaidBossGroupId(), password),
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'BGPath': table_encryption.convert_string(obj.BGPath(), password),
        'RaidCharacterId': table_encryption.convert_long(obj.RaidCharacterId(), password),
        'BossCharacterId': [table_encryption.convert_long(obj.BossCharacterId(j), password) for j in range(obj.BossCharacterIdLength())],
        'AssistCharacterLimitCount': table_encryption.convert_long(obj.AssistCharacterLimitCount(), password),
        'WorldRaidDifficulty': WorldRaidDifficulty(table_encryption.convert_int(obj.WorldRaidDifficulty_(), password)).name,
        'DifficultyOpenCondition': obj.DifficultyOpenCondition(),
        'RaidEnterAmount': table_encryption.convert_long(obj.RaidEnterAmount(), password),
        'ReEnterAmount': table_encryption.convert_long(obj.ReEnterAmount(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'RaidBattleEndRewardGroupId': table_encryption.convert_long(obj.RaidBattleEndRewardGroupId(), password),
        'RaidRewardGroupId': table_encryption.convert_long(obj.RaidRewardGroupId(), password),
        'BattleReadyTimelinePath': [table_encryption.convert_string(obj.BattleReadyTimelinePath(j), password) for j in range(obj.BattleReadyTimelinePathLength())],
        'BattleReadyTimelinePhaseStart': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseStart(j), password) for j in range(obj.BattleReadyTimelinePhaseStartLength())],
        'BattleReadyTimelinePhaseEnd': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseEnd(j), password) for j in range(obj.BattleReadyTimelinePhaseEndLength())],
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'PhaseChangeTimelinePath': table_encryption.convert_string(obj.PhaseChangeTimelinePath(), password),
        'TimeLinePhase': table_encryption.convert_long(obj.TimeLinePhase(), password),
        'EnterScenarioKey': table_encryption.convert_long(obj.EnterScenarioKey(), password),
        'ClearScenarioKey': table_encryption.convert_long(obj.ClearScenarioKey(), password),
        'UseFixedEchelon': obj.UseFixedEchelon(),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'IsRaidScenarioBattle': obj.IsRaidScenarioBattle(),
        'ShowSkillCard': obj.ShowSkillCard(),
        'BossBGInfoKey': table_encryption.convert_uint(obj.BossBGInfoKey(), password),
        'DamageToWorldBoss': table_encryption.convert_long(obj.DamageToWorldBoss(), password),
        'AllyPassiveSkill': [table_encryption.convert_string(obj.AllyPassiveSkill(j), password) for j in range(obj.AllyPassiveSkillLength())],
        'AllyPassiveSkillLevel': [table_encryption.convert_int(obj.AllyPassiveSkillLevel(j), password) for j in range(obj.AllyPassiveSkillLevelLength())],
        'SaveCurrentLocalBossHP': obj.SaveCurrentLocalBossHP(),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
    }


def dump_WorldRaidStageRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'IsClearStageRewardHideInfo': obj.IsClearStageRewardHideInfo(),
        'ClearStageRewardProb': table_encryption.convert_long(obj.ClearStageRewardProb(), password),
        'ClearStageRewardParcelType': ParcelType(table_encryption.convert_int(obj.ClearStageRewardParcelType(), password)).name,
        'ClearStageRewardParcelUniqueID': table_encryption.convert_long(obj.ClearStageRewardParcelUniqueID(), password),
        'ClearStageRewardParcelUniqueName': table_encryption.convert_string(obj.ClearStageRewardParcelUniqueName(), password),
        'ClearStageRewardAmount': table_encryption.convert_long(obj.ClearStageRewardAmount(), password),
    }


def dump_AudioAnimatorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ControllerNameHash': table_encryption.convert_uint(obj.ControllerNameHash(), password),
        'VoiceNamePrefix': table_encryption.convert_string(obj.VoiceNamePrefix(), password),
        'StateNameHash': table_encryption.convert_uint(obj.StateNameHash(), password),
        'StateName': table_encryption.convert_string(obj.StateName(), password),
        'IgnoreInterruptDelay': obj.IgnoreInterruptDelay(),
        'IgnoreInterruptPlay': obj.IgnoreInterruptPlay(),
        'Volume': table_encryption.convert_float(obj.Volume(), password),
        'Delay': table_encryption.convert_float(obj.Delay(), password),
        'RandomPitchMin': table_encryption.convert_int(obj.RandomPitchMin(), password),
        'RandomPitchMax': table_encryption.convert_int(obj.RandomPitchMax(), password),
        'AudioPriority': table_encryption.convert_int(obj.AudioPriority(), password),
        'AudioClipPath': [table_encryption.convert_string(obj.AudioClipPath(j), password) for j in range(obj.AudioClipPathLength())],
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
    }


def dump_BGMExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'Path': [table_encryption.convert_string(obj.Path(j), password) for j in range(obj.PathLength())],
        'Volume': [table_encryption.convert_float(obj.Volume(j), password) for j in range(obj.VolumeLength())],
        'LoopStartTime': [table_encryption.convert_float(obj.LoopStartTime(j), password) for j in range(obj.LoopStartTimeLength())],
        'LoopEndTime': [table_encryption.convert_float(obj.LoopEndTime(j), password) for j in range(obj.LoopEndTimeLength())],
        'LoopTranstionTime': [table_encryption.convert_float(obj.LoopTranstionTime(j), password) for j in range(obj.LoopTranstionTimeLength())],
        'LoopOffsetTime': [table_encryption.convert_float(obj.LoopOffsetTime(j), password) for j in range(obj.LoopOffsetTimeLength())],
    }


def dump_BGMRaidExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'PhaseIndex': table_encryption.convert_long(obj.PhaseIndex(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
    }


def dump_BGMUIExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UIPrefab': table_encryption.convert_uint(obj.UIPrefab(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'BGMId2nd': table_encryption.convert_long(obj.BGMId2nd(), password),
        'BGMId3rd': table_encryption.convert_long(obj.BGMId3rd(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
    }


def dump_CameraExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'MinDistance': table_encryption.convert_float(obj.MinDistance(), password),
        'MaxDistance': table_encryption.convert_float(obj.MaxDistance(), password),
        'RotationX': table_encryption.convert_float(obj.RotationX(), password),
        'RotationY': table_encryption.convert_float(obj.RotationY(), password),
        'MoveInstantly': obj.MoveInstantly(),
        'MoveInstantlyRotationSave': obj.MoveInstantlyRotationSave(),
        'LeftMargin': table_encryption.convert_float(obj.LeftMargin(), password),
        'BottomMargin': table_encryption.convert_float(obj.BottomMargin(), password),
        'IgnoreEnemies': obj.IgnoreEnemies(),
        'UseRailPointCompensation': obj.UseRailPointCompensation(),
    }


def dump_CharacterDialogEventExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CostumeUniqueId': table_encryption.convert_long(obj.CostumeUniqueId(), password),
        'OriginalCharacterId': table_encryption.convert_long(obj.OriginalCharacterId(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'EventID': table_encryption.convert_long(obj.EventID(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'DialogCategory': DialogCategory(table_encryption.convert_int(obj.DialogCategory_(), password)).name,
        'DialogCondition': DialogCondition(table_encryption.convert_int(obj.DialogCondition_(), password)).name,
        'DialogConditionDetail': DialogConditionDetail(table_encryption.convert_int(obj.DialogConditionDetail_(), password)).name,
        'DialogConditionDetailValue': table_encryption.convert_long(obj.DialogConditionDetailValue(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'DialogType': DialogType(table_encryption.convert_int(obj.DialogType_(), password)).name,
        'ActionName': table_encryption.convert_string(obj.ActionName(), password),
        'Duration': table_encryption.convert_long(obj.Duration(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
        'CollectionVisible': obj.CollectionVisible(),
        'CVCollectionType': CVCollectionType(table_encryption.convert_int(obj.CVCollectionType_(), password)).name,
        'UnlockEventSeason': table_encryption.convert_long(obj.UnlockEventSeason(), password),
        'ScenarioGroupId': table_encryption.convert_long(obj.ScenarioGroupId(), password),
        'LocalizeCVGroup': table_encryption.convert_string(obj.LocalizeCVGroup(), password),
    }


def dump_CharacterDialogExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'CostumeUniqueId': table_encryption.convert_long(obj.CostumeUniqueId(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'DialogCategory': DialogCategory(table_encryption.convert_int(obj.DialogCategory_(), password)).name,
        'DialogCondition': DialogCondition(table_encryption.convert_int(obj.DialogCondition_(), password)).name,
        'Anniversary': Anniversary(table_encryption.convert_int(obj.Anniversary_(), password)).name,
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'DialogType': DialogType(table_encryption.convert_int(obj.DialogType_(), password)).name,
        'ActionName': table_encryption.convert_string(obj.ActionName(), password),
        'Duration': table_encryption.convert_long(obj.Duration(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
        'ApplyPosition': obj.ApplyPosition(),
        'PosX': table_encryption.convert_float(obj.PosX(), password),
        'PosY': table_encryption.convert_float(obj.PosY(), password),
        'CollectionVisible': obj.CollectionVisible(),
        'CVCollectionType': CVCollectionType(table_encryption.convert_int(obj.CVCollectionType_(), password)).name,
        'UnlockFavorRank': table_encryption.convert_long(obj.UnlockFavorRank(), password),
        'UnlockEquipWeapon': obj.UnlockEquipWeapon(),
        'LocalizeCVGroup': table_encryption.convert_string(obj.LocalizeCVGroup(), password),
    }


def dump_CharacterDialogSubtitleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LocalizeCVGroup': table_encryption.convert_string(obj.LocalizeCVGroup(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'Duration': table_encryption.convert_long(obj.Duration(), password),
        'Separate': obj.Separate(),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
    }


def dump_CharacterPotentialExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'PotentialStatGroupId': table_encryption.convert_long(obj.PotentialStatGroupId(), password),
        'PotentialStatBonusRateType': PotentialStatBonusRateType(table_encryption.convert_int(obj.PotentialStatBonusRateType_(), password)).name,
        'IsUnnecessaryStat': obj.IsUnnecessaryStat(),
    }


def dump_CharacterPotentialRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'RequirePotentialStatType': [PotentialStatBonusRateType(table_encryption.convert_int(obj.RequirePotentialStatType(j), password)).name for j in range(obj.RequirePotentialStatTypeLength())],
        'RequirePotentialStatLevel': [table_encryption.convert_long(obj.RequirePotentialStatLevel(j), password) for j in range(obj.RequirePotentialStatLevelLength())],
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardId': table_encryption.convert_long(obj.RewardId(), password),
        'RewardAmount': table_encryption.convert_int(obj.RewardAmount(), password),
    }


def dump_CharacterPotentialStatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'PotentialStatGroupId': table_encryption.convert_long(obj.PotentialStatGroupId(), password),
        'PotentialLevel': table_encryption.convert_int(obj.PotentialLevel(), password),
        'RecipeId': table_encryption.convert_long(obj.RecipeId(), password),
        'StatBonusRate': table_encryption.convert_long(obj.StatBonusRate(), password),
    }


def dump_CharacterVoiceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterVoiceUniqueId': table_encryption.convert_long(obj.CharacterVoiceUniqueId(), password),
        'CharacterVoiceGroupId': table_encryption.convert_long(obj.CharacterVoiceGroupId(), password),
        'VoiceHash': table_encryption.convert_uint(obj.VoiceHash(), password),
        'OnlyOne': obj.OnlyOne(),
        'Priority': table_encryption.convert_int(obj.Priority(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'CollectionVisible': obj.CollectionVisible(),
        'CVCollectionType': CVCollectionType(table_encryption.convert_int(obj.CVCollectionType_(), password)).name,
        'UnlockFavorRank': table_encryption.convert_long(obj.UnlockFavorRank(), password),
        'LocalizeCVGroup': table_encryption.convert_string(obj.LocalizeCVGroup(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'Volume': [table_encryption.convert_float(obj.Volume(j), password) for j in range(obj.VolumeLength())],
        'Delay': [table_encryption.convert_float(obj.Delay(j), password) for j in range(obj.DelayLength())],
        'Path': [table_encryption.convert_string(obj.Path(j), password) for j in range(obj.PathLength())],
    }


def dump_CharacterVoiceSubtitleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LocalizeCVGroup': table_encryption.convert_string(obj.LocalizeCVGroup(), password),
        'CharacterVoiceGroupId': table_encryption.convert_long(obj.CharacterVoiceGroupId(), password),
        'Duration': table_encryption.convert_long(obj.Duration(), password),
        'Separate': obj.Separate(),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
    }


def dump_ClanChattingEmojiExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TabGroupId': table_encryption.convert_int(obj.TabGroupId(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'ImagePathKr': table_encryption.convert_string(obj.ImagePathKr(), password),
        'ImagePathJp': table_encryption.convert_string(obj.ImagePathJp(), password),
    }


def dump_CombatEmojiExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'EmojiEvent': EmojiEvent(table_encryption.convert_int(obj.EmojiEvent_(), password)).name,
        'OrderOfPriority': table_encryption.convert_int(obj.OrderOfPriority(), password),
        'EmojiDuration': obj.EmojiDuration(),
        'EmojiReversal': obj.EmojiReversal(),
        'EmojiTurnOn': obj.EmojiTurnOn(),
        'ShowEmojiDelay': table_encryption.convert_int(obj.ShowEmojiDelay(), password),
        'ShowDefaultBG': obj.ShowDefaultBG(),
    }


def dump_ContentsScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'LocalizeId': table_encryption.convert_uint(obj.LocalizeId(), password),
        'DisplayOrder': table_encryption.convert_int(obj.DisplayOrder(), password),
        'ScenarioContentType': ScenarioContentType(table_encryption.convert_int(obj.ScenarioContentType_(), password)).name,
        'ScenarioGroupId': [table_encryption.convert_long(obj.ScenarioGroupId(j), password) for j in range(obj.ScenarioGroupIdLength())],
    }


def dump_ContentsShortcutExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ScenarioModeVolume': table_encryption.convert_long(obj.ScenarioModeVolume(), password),
        'ScenarioModeChapter': table_encryption.convert_long(obj.ScenarioModeChapter(), password),
        'ShortcutOpenTime': table_encryption.convert_string(obj.ShortcutOpenTime(), password),
        'ShortcutCloseTime': table_encryption.convert_string(obj.ShortcutCloseTime(), password),
        'ConditionContentId': table_encryption.convert_long(obj.ConditionContentId(), password),
        'ConquestMapDifficulty': StageDifficulty(table_encryption.convert_int(obj.ConquestMapDifficulty(), password)).name,
        'ConquestStepIndex': table_encryption.convert_int(obj.ConquestStepIndex(), password),
        'ShortcutContentId': table_encryption.convert_long(obj.ShortcutContentId(), password),
        'ShortcutUIName': [table_encryption.convert_string(obj.ShortcutUIName(j), password) for j in range(obj.ShortcutUINameLength())],
        'Localize': table_encryption.convert_string(obj.Localize(), password),
    }


def dump_EventContentNotifyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_int(obj.Id(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'EventNotifyType': EventNotifyType(table_encryption.convert_int(obj.EventNotifyType_(), password)).name,
        'EventTargetType': EventTargetType(table_encryption.convert_int(obj.EventTargetType_(), password)).name,
        'ShortcutEventTargetType': EventTargetType(table_encryption.convert_int(obj.ShortcutEventTargetType(), password)).name,
        'IsShortcutEnable': obj.IsShortcutEnable(),
    }


def dump_EventContentTreasureCellRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeCodeID': table_encryption.convert_string(obj.LocalizeCodeID(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_EventContentTreasureExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'TitleLocalize': table_encryption.convert_string(obj.TitleLocalize(), password),
        'LoopRound': table_encryption.convert_int(obj.LoopRound(), password),
        'UsePrefabName': table_encryption.convert_string(obj.UsePrefabName(), password),
        'TreasureBGImagePath': table_encryption.convert_string(obj.TreasureBGImagePath(), password),
    }


def dump_EventContentTreasureRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeCodeID': table_encryption.convert_string(obj.LocalizeCodeID(), password),
        'CellUnderImageWidth': table_encryption.convert_int(obj.CellUnderImageWidth(), password),
        'CellUnderImageHeight': table_encryption.convert_int(obj.CellUnderImageHeight(), password),
        'HiddenImage': obj.HiddenImage(),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
        'CellUnderImagePath': table_encryption.convert_string(obj.CellUnderImagePath(), password),
        'TreasureSmallImagePath': table_encryption.convert_string(obj.TreasureSmallImagePath(), password),
    }


def dump_EventContentTreasureRoundExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'TreasureRound': table_encryption.convert_int(obj.TreasureRound(), password),
        'TreasureRoundSize': [table_encryption.convert_int(obj.TreasureRoundSize(j), password) for j in range(obj.TreasureRoundSizeLength())],
        'CellVisualSortUnstructed': obj.CellVisualSortUnstructed(),
        'CellCheckGoodsId': table_encryption.convert_long(obj.CellCheckGoodsId(), password),
        'CellRewardId': table_encryption.convert_long(obj.CellRewardId(), password),
        'RewardID': [table_encryption.convert_long(obj.RewardID(j), password) for j in range(obj.RewardIDLength())],
        'RewardAmount': [table_encryption.convert_int(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
        'TreasureCellImagePath': table_encryption.convert_string(obj.TreasureCellImagePath(), password),
    }


def dump_IdCardBackgroundExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'CollectionVisible': obj.CollectionVisible(),
        'IsDefault': obj.IsDefault(),
        'BgPath': table_encryption.convert_string(obj.BgPath(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
    }


def dump_InformationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupID': table_encryption.convert_long(obj.GroupID(), password),
        'PageName': table_encryption.convert_string(obj.PageName(), password),
        'LocalizeCodeId': table_encryption.convert_string(obj.LocalizeCodeId(), password),
        'TutorialParentName': [table_encryption.convert_string(obj.TutorialParentName(j), password) for j in range(obj.TutorialParentNameLength())],
        'UIName': [table_encryption.convert_string(obj.UIName(j), password) for j in range(obj.UINameLength())],
    }


def dump_LoadingImageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'ImagePathKr': table_encryption.convert_string(obj.ImagePathKr(), password),
        'ImagePathJp': table_encryption.convert_string(obj.ImagePathJp(), password),
        'DisplayWeight': table_encryption.convert_int(obj.DisplayWeight(), password),
    }


def dump_LocalizeCharProfileChangeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'ScenarioModeId': table_encryption.convert_long(obj.ScenarioModeId(), password),
        'ChangeCharacterID': table_encryption.convert_long(obj.ChangeCharacterID(), password),
    }


def dump_LocalizeErrorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'ErrorLevel': WebAPIErrorLevel(table_encryption.convert_int(obj.ErrorLevel(), password)).name,
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
    }


def dump_LocalizeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
    }


def dump_LocalizeSkillExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'NameKr': table_encryption.convert_string(obj.NameKr(), password),
        'DescriptionKr': table_encryption.convert_string(obj.DescriptionKr(), password),
        'SkillInvokeLocalizeKr': table_encryption.convert_string(obj.SkillInvokeLocalizeKr(), password),
        'NameJp': table_encryption.convert_string(obj.NameJp(), password),
        'DescriptionJp': table_encryption.convert_string(obj.DescriptionJp(), password),
        'SkillInvokeLocalizeJp': table_encryption.convert_string(obj.SkillInvokeLocalizeJp(), password),
    }


def dump_MemoryLobbyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'MemoryLobbyCategory': MemoryLobbyCategory(table_encryption.convert_int(obj.MemoryLobbyCategory_(), password)).name,
        'SlotTextureName': table_encryption.convert_string(obj.SlotTextureName(), password),
        'RewardTextureName': table_encryption.convert_string(obj.RewardTextureName(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'AudioClipJp': table_encryption.convert_string(obj.AudioClipJp(), password),
        'AudioClipKr': table_encryption.convert_string(obj.AudioClipKr(), password),
    }


def dump_MessagePopupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StringId': table_encryption.convert_uint(obj.StringId(), password),
        'MessagePopupLayout': MessagePopupLayout(table_encryption.convert_int(obj.MessagePopupLayout_(), password)).name,
        'OrderType': MessagePopupImagePositionType(table_encryption.convert_int(obj.OrderType(), password)).name,
        'Image': table_encryption.convert_string(obj.Image(), password),
        'TitleText': table_encryption.convert_uint(obj.TitleText(), password),
        'SubTitleText': table_encryption.convert_uint(obj.SubTitleText(), password),
        'MessageText': table_encryption.convert_uint(obj.MessageText(), password),
        'ConditionText': [table_encryption.convert_uint(obj.ConditionText(j), password) for j in range(obj.ConditionTextLength())],
        'DisplayXButton': obj.DisplayXButton(),
        'Button': [MessagePopupButtonType(table_encryption.convert_int(obj.Button(j), password)).name for j in range(obj.ButtonLength())],
        'ButtonText': [table_encryption.convert_uint(obj.ButtonText(j), password) for j in range(obj.ButtonTextLength())],
        'ButtonCommand': [table_encryption.convert_string(obj.ButtonCommand(j), password) for j in range(obj.ButtonCommandLength())],
        'ButtonParameter': [table_encryption.convert_string(obj.ButtonParameter(j), password) for j in range(obj.ButtonParameterLength())],
    }


def dump_MiniGameDefenseCharacterBanExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
    }


def dump_MiniGameDefenseFixedStatExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MinigameDefenseFixedStatId': table_encryption.convert_long(obj.MinigameDefenseFixedStatId(), password),
        'Level': table_encryption.convert_int(obj.Level(), password),
        'Grade': table_encryption.convert_int(obj.Grade(), password),
        'ExSkillLevel': table_encryption.convert_int(obj.ExSkillLevel(), password),
        'NoneExSkillLevel': table_encryption.convert_int(obj.NoneExSkillLevel(), password),
        'Equipment1Tier': table_encryption.convert_int(obj.Equipment1Tier(), password),
        'Equipment1Level': table_encryption.convert_int(obj.Equipment1Level(), password),
        'Equipment2Tier': table_encryption.convert_int(obj.Equipment2Tier(), password),
        'Equipment2Level': table_encryption.convert_int(obj.Equipment2Level(), password),
        'Equipment3Tier': table_encryption.convert_int(obj.Equipment3Tier(), password),
        'Equipment3Level': table_encryption.convert_int(obj.Equipment3Level(), password),
        'CharacterWeaponGrade': table_encryption.convert_int(obj.CharacterWeaponGrade(), password),
        'CharacterWeaponLevel': table_encryption.convert_int(obj.CharacterWeaponLevel(), password),
        'CharacterGearTier': table_encryption.convert_int(obj.CharacterGearTier(), password),
        'CharacterGearLevel': table_encryption.convert_int(obj.CharacterGearLevel(), password),
    }


def dump_MiniGameDefenseInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DefenseBattleParcelType': ParcelType(table_encryption.convert_int(obj.DefenseBattleParcelType(), password)).name,
        'DefenseBattleParcelId': table_encryption.convert_long(obj.DefenseBattleParcelId(), password),
        'DefenseBattleMultiplierMax': table_encryption.convert_long(obj.DefenseBattleMultiplierMax(), password),
        'DisableRootMotion': obj.DisableRootMotion(),
    }


def dump_MiniGameDefenseStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'StageDifficulty': StageDifficulty(table_encryption.convert_int(obj.StageDifficulty_(), password)).name,
        'StageDifficultyLocalize': table_encryption.convert_uint(obj.StageDifficultyLocalize(), password),
        'StageNumber': table_encryption.convert_int(obj.StageNumber(), password),
        'StageDisplay': table_encryption.convert_int(obj.StageDisplay(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': ParcelType(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostId': table_encryption.convert_long(obj.StageEnterCostId(), password),
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'EventContentStageRewardId': table_encryption.convert_long(obj.EventContentStageRewardId(), password),
        'EnterScenarioGroupId': [table_encryption.convert_long(obj.EnterScenarioGroupId(j), password) for j in range(obj.EnterScenarioGroupIdLength())],
        'ClearScenarioGroupId': [table_encryption.convert_long(obj.ClearScenarioGroupId(j), password) for j in range(obj.ClearScenarioGroupIdLength())],
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_int(obj.RecommandLevel(), password),
        'GroundID': table_encryption.convert_long(obj.GroundID(), password),
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'StarGoal': [StarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'DefenseFormationBGPrefab': table_encryption.convert_string(obj.DefenseFormationBGPrefab(), password),
        'DefenseFormationBGPrefabScale': table_encryption.convert_float(obj.DefenseFormationBGPrefabScale(), password),
        'FixedEchelon': table_encryption.convert_long(obj.FixedEchelon(), password),
        'MininageDefenseFixedStatId': table_encryption.convert_long(obj.MininageDefenseFixedStatId(), password),
        'StageHint': table_encryption.convert_uint(obj.StageHint(), password),
    }


def dump_MiniGameDreamCollectionScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'IsSkip': obj.IsSkip(),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'Parameter': [DreamMakerParameterType(table_encryption.convert_int(obj.Parameter(j), password)).name for j in range(obj.ParameterLength())],
        'ParameterAmount': [table_encryption.convert_long(obj.ParameterAmount(j), password) for j in range(obj.ParameterAmountLength())],
        'ScenarioGroupId': table_encryption.convert_long(obj.ScenarioGroupId(), password),
    }


def dump_MiniGameDreamDailyPointExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'TotalParameterMin': table_encryption.convert_long(obj.TotalParameterMin(), password),
        'TotalParameterMax': table_encryption.convert_long(obj.TotalParameterMax(), password),
        'DailyPointCoefficient': table_encryption.convert_long(obj.DailyPointCoefficient(), password),
        'DailyPointCorrectionValue': table_encryption.convert_long(obj.DailyPointCorrectionValue(), password),
    }


def dump_MiniGameDreamEndingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EndingId': table_encryption.convert_long(obj.EndingId(), password),
        'DreamMakerEndingType': DreamMakerEndingType(table_encryption.convert_int(obj.DreamMakerEndingType_(), password)).name,
        'Order': table_encryption.convert_int(obj.Order(), password),
        'ScenarioGroupId': table_encryption.convert_long(obj.ScenarioGroupId(), password),
        'EndingCondition': [DreamMakerEndingCondition(table_encryption.convert_int(obj.EndingCondition(j), password)).name for j in range(obj.EndingConditionLength())],
        'EndingConditionValue': [table_encryption.convert_long(obj.EndingConditionValue(j), password) for j in range(obj.EndingConditionValueLength())],
    }


def dump_MiniGameDreamEndingRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EndingId': table_encryption.convert_long(obj.EndingId(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'DreamMakerEndingRewardType': DreamMakerEndingRewardType(table_encryption.convert_int(obj.DreamMakerEndingRewardType_(), password)).name,
        'DreamMakerEndingType': DreamMakerEndingType(table_encryption.convert_int(obj.DreamMakerEndingType_(), password)).name,
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
    }


def dump_MiniGameDreamInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DreamMakerMultiplierCondition': DreamMakerMultiplierCondition(table_encryption.convert_int(obj.DreamMakerMultiplierCondition_(), password)).name,
        'DreamMakerMultiplierConditionValue': table_encryption.convert_long(obj.DreamMakerMultiplierConditionValue(), password),
        'DreamMakerMultiplierMax': table_encryption.convert_long(obj.DreamMakerMultiplierMax(), password),
        'DreamMakerDays': table_encryption.convert_long(obj.DreamMakerDays(), password),
        'DreamMakerActionPoint': table_encryption.convert_long(obj.DreamMakerActionPoint(), password),
        'DreamMakerParcelType': ParcelType(table_encryption.convert_int(obj.DreamMakerParcelType(), password)).name,
        'DreamMakerParcelId': table_encryption.convert_long(obj.DreamMakerParcelId(), password),
        'DreamMakerDailyPointParcelType': ParcelType(table_encryption.convert_int(obj.DreamMakerDailyPointParcelType(), password)).name,
        'DreamMakerDailyPointId': table_encryption.convert_long(obj.DreamMakerDailyPointId(), password),
        'DreamMakerParameterTransfer': table_encryption.convert_long(obj.DreamMakerParameterTransfer(), password),
        'ScheduleCostGoodsId': table_encryption.convert_long(obj.ScheduleCostGoodsId(), password),
        'LobbyBGMChangeScenarioId': table_encryption.convert_long(obj.LobbyBGMChangeScenarioId(), password),
    }


def dump_MiniGameDreamParameterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ParameterType': DreamMakerParameterType(table_encryption.convert_int(obj.ParameterType(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'ParameterBase': table_encryption.convert_long(obj.ParameterBase(), password),
        'ParameterBaseMax': table_encryption.convert_long(obj.ParameterBaseMax(), password),
        'ParameterMin': table_encryption.convert_long(obj.ParameterMin(), password),
        'ParameterMax': table_encryption.convert_long(obj.ParameterMax(), password),
    }


def dump_MiniGameDreamReplayScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'ScenarioGroupId': table_encryption.convert_long(obj.ScenarioGroupId(), password),
        'Order': table_encryption.convert_long(obj.Order(), password),
        'ReplaySummaryTitleLocalize': table_encryption.convert_uint(obj.ReplaySummaryTitleLocalize(), password),
        'ReplaySummaryLocalizeScenarioId': table_encryption.convert_uint(obj.ReplaySummaryLocalizeScenarioId(), password),
        'ReplayScenarioResource': table_encryption.convert_string(obj.ReplayScenarioResource(), password),
        'IsReplayScenarioHorizon': obj.IsReplayScenarioHorizon(),
    }


def dump_MiniGameDreamScheduleExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DreamMakerScheduleGroupId': table_encryption.convert_long(obj.DreamMakerScheduleGroupId(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'LoadingResource01': table_encryption.convert_string(obj.LoadingResource01(), password),
        'LoadingResource02': table_encryption.convert_string(obj.LoadingResource02(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
    }


def dump_MiniGameDreamScheduleResultExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'DreamMakerResult': DreamMakerResult(table_encryption.convert_int(obj.DreamMakerResult_(), password)).name,
        'DreamMakerScheduleGroup': table_encryption.convert_long(obj.DreamMakerScheduleGroup(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'RewardParameter': [DreamMakerParameterType(table_encryption.convert_int(obj.RewardParameter(j), password)).name for j in range(obj.RewardParameterLength())],
        'RewardParameterOperationType': [DreamMakerParamOperationType(table_encryption.convert_int(obj.RewardParameterOperationType(j), password)).name for j in range(obj.RewardParameterOperationTypeLength())],
        'RewardParameterAmount': [table_encryption.convert_long(obj.RewardParameterAmount(j), password) for j in range(obj.RewardParameterAmountLength())],
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_long(obj.RewardParcelAmount(), password),
    }


def dump_MiniGameDreamTimelineExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'DreamMakerDays': table_encryption.convert_long(obj.DreamMakerDays(), password),
        'DreamMakerActionPoint': table_encryption.convert_long(obj.DreamMakerActionPoint(), password),
        'EnterScenarioGroupId': table_encryption.convert_long(obj.EnterScenarioGroupId(), password),
        'Bgm': table_encryption.convert_long(obj.Bgm(), password),
        'ArtLevelPath': table_encryption.convert_string(obj.ArtLevelPath(), password),
        'DesignLevelPath': table_encryption.convert_string(obj.DesignLevelPath(), password),
    }


def dump_MinigameDreamVoiceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'VoiceCondition': DreamMakerVoiceCondition(table_encryption.convert_int(obj.VoiceCondition(), password)).name,
        'VoiceClip': table_encryption.convert_uint(obj.VoiceClip(), password),
    }


def dump_MissionEmergencyCompleteExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MissionId': table_encryption.convert_long(obj.MissionId(), password),
        'EmergencyComplete': obj.EmergencyComplete(),
    }


def dump_MultiFloorRaidRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'RewardGroupId': table_encryption.convert_long(obj.RewardGroupId(), password),
        'ClearStageRewardProb': table_encryption.convert_long(obj.ClearStageRewardProb(), password),
        'ClearStageRewardParcelType': ParcelType(table_encryption.convert_int(obj.ClearStageRewardParcelType(), password)).name,
        'ClearStageRewardParcelUniqueID': table_encryption.convert_long(obj.ClearStageRewardParcelUniqueID(), password),
        'ClearStageRewardAmount': table_encryption.convert_long(obj.ClearStageRewardAmount(), password),
    }


def dump_MultiFloorRaidSeasonManageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'LobbyEnterScenario': table_encryption.convert_uint(obj.LobbyEnterScenario(), password),
        'ShowLobbyBanner': obj.ShowLobbyBanner(),
        'SeasonStartDate': table_encryption.convert_string(obj.SeasonStartDate(), password),
        'SeasonEndDate': table_encryption.convert_string(obj.SeasonEndDate(), password),
        'SettlementEndDate': table_encryption.convert_string(obj.SettlementEndDate(), password),
        'OpenRaidBossGroupId': table_encryption.convert_string(obj.OpenRaidBossGroupId(), password),
        'EnterScenarioKey': table_encryption.convert_uint(obj.EnterScenarioKey(), password),
        'LobbyImgPath': table_encryption.convert_string(obj.LobbyImgPath(), password),
        'LevelImgPath': table_encryption.convert_string(obj.LevelImgPath(), password),
    }


def dump_MultiFloorRaidStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
        'BossGroupId': table_encryption.convert_string(obj.BossGroupId(), password),
        'AssistSlot': table_encryption.convert_int(obj.AssistSlot(), password),
        'StageOpenCondition': table_encryption.convert_long(obj.StageOpenCondition(), password),
        'FloorListSection': obj.FloorListSection(),
        'FloorListSectionOpenCondition': table_encryption.convert_long(obj.FloorListSectionOpenCondition(), password),
        'FloorListSectionLabel': table_encryption.convert_uint(obj.FloorListSectionLabel(), password),
        'Difficulty': table_encryption.convert_int(obj.Difficulty(), password),
        'UseBossIndex': obj.UseBossIndex(),
        'UseBossAIPhaseSync': obj.UseBossAIPhaseSync(),
        'FloorListImgPath': table_encryption.convert_string(obj.FloorListImgPath(), password),
        'FloorImgPath': table_encryption.convert_string(obj.FloorImgPath(), password),
        'RaidCharacterId': table_encryption.convert_long(obj.RaidCharacterId(), password),
        'BossCharacterId': [table_encryption.convert_long(obj.BossCharacterId(j), password) for j in range(obj.BossCharacterIdLength())],
        'StatChangeId': [table_encryption.convert_long(obj.StatChangeId(j), password) for j in range(obj.StatChangeIdLength())],
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'RecommendLevel': table_encryption.convert_long(obj.RecommendLevel(), password),
        'RewardGroupId': table_encryption.convert_long(obj.RewardGroupId(), password),
        'BattleReadyTimelinePath': [table_encryption.convert_string(obj.BattleReadyTimelinePath(j), password) for j in range(obj.BattleReadyTimelinePathLength())],
        'BattleReadyTimelinePhaseStart': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseStart(j), password) for j in range(obj.BattleReadyTimelinePhaseStartLength())],
        'BattleReadyTimelinePhaseEnd': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseEnd(j), password) for j in range(obj.BattleReadyTimelinePhaseEndLength())],
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'ShowSkillCard': obj.ShowSkillCard(),
    }


def dump_MultiFloorRaidStatChangeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StatChangeId': table_encryption.convert_long(obj.StatChangeId(), password),
        'StatType': [StatType(table_encryption.convert_int(obj.StatType_(j), password)).name for j in range(obj.StatTypeLength())],
        'StatAdd': [table_encryption.convert_long(obj.StatAdd(j), password) for j in range(obj.StatAddLength())],
        'StatMultiply': [table_encryption.convert_long(obj.StatMultiply(j), password) for j in range(obj.StatMultiplyLength())],
        'ApplyCharacterId': [table_encryption.convert_long(obj.ApplyCharacterId(j), password) for j in range(obj.ApplyCharacterIdLength())],
    }


def dump_OperatorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'GroupId': table_encryption.convert_string(obj.GroupId(), password),
        'OperatorCondition': OperatorCondition(table_encryption.convert_int(obj.OperatorCondition_(), password)).name,
        'OutputSequence': table_encryption.convert_int(obj.OutputSequence(), password),
        'RandomWeight': table_encryption.convert_int(obj.RandomWeight(), password),
        'OutputDelay': table_encryption.convert_int(obj.OutputDelay(), password),
        'Duration': table_encryption.convert_int(obj.Duration(), password),
        'OperatorOutputPriority': table_encryption.convert_int(obj.OperatorOutputPriority(), password),
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'TextLocalizeKey': table_encryption.convert_string(obj.TextLocalizeKey(), password),
        'VoiceId': [table_encryption.convert_uint(obj.VoiceId(j), password) for j in range(obj.VoiceIdLength())],
        'OperatorWaitQueue': obj.OperatorWaitQueue(),
    }


def dump_ScenarioBGEffectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_uint(obj.Name(), password),
        'Effect': table_encryption.convert_string(obj.Effect(), password),
        'Scroll': ScenarioBGScroll(table_encryption.convert_int(obj.Scroll(), password)).name,
        'ScrollTime': table_encryption.convert_long(obj.ScrollTime(), password),
        'ScrollFrom': table_encryption.convert_long(obj.ScrollFrom(), password),
        'ScrollTo': table_encryption.convert_long(obj.ScrollTo(), password),
    }


def dump_ScenarioBGNameExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_uint(obj.Name(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'BGFileName': table_encryption.convert_string(obj.BGFileName(), password),
        'BGType': ScenarioBGType(table_encryption.convert_int(obj.BGType(), password)).name,
        'AnimationRoot': table_encryption.convert_string(obj.AnimationRoot(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
        'SpineScale': table_encryption.convert_float(obj.SpineScale(), password),
        'SpineLocalPosX': table_encryption.convert_int(obj.SpineLocalPosX(), password),
        'SpineLocalPosY': table_encryption.convert_int(obj.SpineLocalPosY(), password),
    }


def dump_ScenarioCharacterEmotionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EmoticonName': table_encryption.convert_string(obj.EmoticonName(), password),
        'Name': table_encryption.convert_uint(obj.Name(), password),
    }


def dump_ScenarioCharacterNameExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterName': table_encryption.convert_uint(obj.CharacterName(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'NameKR': table_encryption.convert_string(obj.NameKR(), password),
        'NicknameKR': table_encryption.convert_string(obj.NicknameKR(), password),
        'NameJP': table_encryption.convert_string(obj.NameJP(), password),
        'NicknameJP': table_encryption.convert_string(obj.NicknameJP(), password),
        'Shape': ScenarioCharacterShapes(table_encryption.convert_int(obj.Shape(), password)).name,
        'SpinePrefabName': table_encryption.convert_string(obj.SpinePrefabName(), password),
        'SmallPortrait': table_encryption.convert_string(obj.SmallPortrait(), password),
    }


def dump_ScenarioCharacterSituationSetExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_uint(obj.Name(), password),
        'Face': table_encryption.convert_string(obj.Face(), password),
        'Behavior': table_encryption.convert_string(obj.Behavior(), password),
        'Action': table_encryption.convert_string(obj.Action(), password),
        'Shape': table_encryption.convert_string(obj.Shape(), password),
        'Effect': table_encryption.convert_uint(obj.Effect(), password),
        'Emotion': table_encryption.convert_uint(obj.Emotion(), password),
    }


def dump_ScenarioContentCollectionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'UnlockConditionType': CollectionUnlockType(table_encryption.convert_int(obj.UnlockConditionType(), password)).name,
        'UnlockConditionParameter': [table_encryption.convert_long(obj.UnlockConditionParameter(j), password) for j in range(obj.UnlockConditionParameterLength())],
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'UnlockConditionCount': table_encryption.convert_long(obj.UnlockConditionCount(), password),
        'IsObject': obj.IsObject(),
        'IsHorizon': obj.IsHorizon(),
        'EmblemResource': table_encryption.convert_string(obj.EmblemResource(), password),
        'ThumbResource': table_encryption.convert_string(obj.ThumbResource(), password),
        'FullResource': table_encryption.convert_string(obj.FullResource(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'SubNameLocalizeCodeId': table_encryption.convert_string(obj.SubNameLocalizeCodeId(), password),
    }


def dump_ScenarioEffectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EffectName': table_encryption.convert_string(obj.EffectName(), password),
        'Name': table_encryption.convert_uint(obj.Name(), password),
    }


def dump_ScenarioModeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ModeId': table_encryption.convert_long(obj.ModeId(), password),
        'ModeType': ScenarioModeTypes(table_encryption.convert_int(obj.ModeType(), password)).name,
        'SubType': ScenarioModeSubTypes(table_encryption.convert_int(obj.SubType(), password)).name,
        'VolumeId': table_encryption.convert_long(obj.VolumeId(), password),
        'ChapterId': table_encryption.convert_long(obj.ChapterId(), password),
        'EpisodeId': table_encryption.convert_long(obj.EpisodeId(), password),
        'Hide': obj.Hide(),
        'Open': obj.Open(),
        'IsContinue': obj.IsContinue(),
        'EpisodeContinueModeId': table_encryption.convert_long(obj.EpisodeContinueModeId(), password),
        'FrontScenarioGroupId': [table_encryption.convert_long(obj.FrontScenarioGroupId(j), password) for j in range(obj.FrontScenarioGroupIdLength())],
        'StrategyId': table_encryption.convert_long(obj.StrategyId(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'IsDefeatBattle': obj.IsDefeatBattle(),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'BackScenarioGroupId': [table_encryption.convert_long(obj.BackScenarioGroupId(j), password) for j in range(obj.BackScenarioGroupIdLength())],
        'ClearedModeId': [table_encryption.convert_long(obj.ClearedModeId(j), password) for j in range(obj.ClearedModeIdLength())],
        'ScenarioModeRewardId': table_encryption.convert_long(obj.ScenarioModeRewardId(), password),
        'IsScenarioSpecialReward': obj.IsScenarioSpecialReward(),
        'AccountLevelLimit': table_encryption.convert_long(obj.AccountLevelLimit(), password),
        'ClearedStageId': table_encryption.convert_long(obj.ClearedStageId(), password),
        'NeedClub': Club(table_encryption.convert_int(obj.NeedClub(), password)).name,
        'NeedClubStudentCount': table_encryption.convert_int(obj.NeedClubStudentCount(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'EventContentType': EventContentType(table_encryption.convert_int(obj.EventContentType_(), password)).name,
        'EventContentCondition': table_encryption.convert_long(obj.EventContentCondition(), password),
        'EventContentConditionGroup': table_encryption.convert_long(obj.EventContentConditionGroup(), password),
        'MapDifficulty': StageDifficulty(table_encryption.convert_int(obj.MapDifficulty(), password)).name,
        'StepIndex': table_encryption.convert_int(obj.StepIndex(), password),
        'RecommendLevel': table_encryption.convert_int(obj.RecommendLevel(), password),
        'EventIconParcelPath': table_encryption.convert_string(obj.EventIconParcelPath(), password),
        'EventBannerTitle': table_encryption.convert_uint(obj.EventBannerTitle(), password),
        'Lof': obj.Lof(),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'CompleteReportEventName': table_encryption.convert_string(obj.CompleteReportEventName(), password),
        'EchelonExtensionType': EchelonExtensionType(table_encryption.convert_int(obj.EchelonExtensionType_(), password)).name,
        'CollectionGroupId': table_encryption.convert_long(obj.CollectionGroupId(), password),
    }


def dump_ScenarioModeRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ScenarioModeRewardId': table_encryption.convert_long(obj.ScenarioModeRewardId(), password),
        'RewardTag': RewardTag(table_encryption.convert_int(obj.RewardTag_(), password)).name,
        'RewardProb': table_encryption.convert_int(obj.RewardProb(), password),
        'RewardParcelType': ParcelType(table_encryption.convert_int(obj.RewardParcelType(), password)).name,
        'RewardParcelId': table_encryption.convert_long(obj.RewardParcelId(), password),
        'RewardParcelAmount': table_encryption.convert_int(obj.RewardParcelAmount(), password),
        'IsDisplayed': obj.IsDisplayed(),
    }


def dump_ScenarioResourceInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ScenarioModeId': table_encryption.convert_long(obj.ScenarioModeId(), password),
        'VideoId': table_encryption.convert_long(obj.VideoId(), password),
        'BgmId': table_encryption.convert_long(obj.BgmId(), password),
        'AudioName': table_encryption.convert_string(obj.AudioName(), password),
        'SpinePath': table_encryption.convert_string(obj.SpinePath(), password),
        'Ratio': table_encryption.convert_int(obj.Ratio(), password),
        'LobbyAniPath': table_encryption.convert_string(obj.LobbyAniPath(), password),
        'MovieCGPath': table_encryption.convert_string(obj.MovieCGPath(), password),
        'LocalizeId': table_encryption.convert_uint(obj.LocalizeId(), password),
    }


def dump_ScenarioScriptExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'SelectionGroup': table_encryption.convert_long(obj.SelectionGroup(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'Sound': table_encryption.convert_string(obj.Sound(), password),
        'Transition': table_encryption.convert_uint(obj.Transition(), password),
        'BGName': table_encryption.convert_uint(obj.BGName(), password),
        'BGEffect': table_encryption.convert_uint(obj.BGEffect(), password),
        'PopupFileName': table_encryption.convert_string(obj.PopupFileName(), password),
        'ScriptKr': table_encryption.convert_string(obj.ScriptKr(), password),
        'TextJp': table_encryption.convert_string(obj.TextJp(), password),
        'VoiceId': table_encryption.convert_uint(obj.VoiceId(), password),
    }


def dump_ScenarioTransitionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_uint(obj.Name(), password),
        'TransitionOut': table_encryption.convert_string(obj.TransitionOut(), password),
        'TransitionOutDuration': table_encryption.convert_long(obj.TransitionOutDuration(), password),
        'TransitionOutResource': table_encryption.convert_string(obj.TransitionOutResource(), password),
        'TransitionIn': table_encryption.convert_string(obj.TransitionIn(), password),
        'TransitionInDuration': table_encryption.convert_long(obj.TransitionInDuration(), password),
        'TransitionInResource': table_encryption.convert_string(obj.TransitionInResource(), password),
    }


def dump_ServiceActionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ServiceActionType': ServiceActionType(table_encryption.convert_int(obj.ServiceActionType_(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
    }


def dump_ShortcutTypeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'IsAscending': obj.IsAscending(),
        'ContentType': [ShortcutContentType(table_encryption.convert_int(obj.ContentType(j), password)).name for j in range(obj.ContentTypeLength())],
    }


def dump_SkillAdditionalTooltipExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'AdditionalSkillGroupId': table_encryption.convert_string(obj.AdditionalSkillGroupId(), password),
        'ShowSkillSlot': table_encryption.convert_string(obj.ShowSkillSlot(), password),
    }


def dump_SoundUIExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'SoundUniqueId': table_encryption.convert_string(obj.SoundUniqueId(), password),
        'Path': table_encryption.convert_string(obj.Path(), password),
    }


def dump_SpineLipsyncExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'VoiceId': table_encryption.convert_uint(obj.VoiceId(), password),
        'AnimJson': table_encryption.convert_string(obj.AnimJson(), password),
    }


def dump_StageFileRefreshSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'ForceSave': obj.ForceSave(),
    }


def dump_StoryStrategyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'Localize': table_encryption.convert_string(obj.Localize(), password),
        'StageEnterEchelonCount': table_encryption.convert_int(obj.StageEnterEchelonCount(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'WhiteListId': table_encryption.convert_long(obj.WhiteListId(), password),
        'StrategyMap': table_encryption.convert_string(obj.StrategyMap(), password),
        'StrategyMapBG': table_encryption.convert_string(obj.StrategyMapBG(), password),
        'MaxTurn': table_encryption.convert_int(obj.MaxTurn(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'StrategyEnvironment': StrategyEnvironment(table_encryption.convert_int(obj.StrategyEnvironment_(), password)).name,
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'FirstClearReportEventName': table_encryption.convert_string(obj.FirstClearReportEventName(), password),
    }


def dump_ToastExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'ToastType': ToastType(table_encryption.convert_int(obj.ToastType_(), password)).name,
        'MissionId': table_encryption.convert_uint(obj.MissionId(), password),
        'TextId': table_encryption.convert_uint(obj.TextId(), password),
        'LifeTime': table_encryption.convert_long(obj.LifeTime(), password),
    }


def dump_TutorialCharacterDialogExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TalkId': table_encryption.convert_long(obj.TalkId(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
        'VoiceId': table_encryption.convert_uint(obj.VoiceId(), password),
    }


def dump_TutorialExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'CompletionReportEventName': table_encryption.convert_string(obj.CompletionReportEventName(), password),
        'CompulsoryTutorial': obj.CompulsoryTutorial(),
        'DescriptionTutorial': obj.DescriptionTutorial(),
        'TutorialStageId': table_encryption.convert_long(obj.TutorialStageId(), password),
        'UIName': [table_encryption.convert_string(obj.UIName(j), password) for j in range(obj.UINameLength())],
        'TutorialParentName': [table_encryption.convert_string(obj.TutorialParentName(j), password) for j in range(obj.TutorialParentNameLength())],
    }


def dump_TutorialFailureImageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Contents': TutorialFailureContentType(table_encryption.convert_int(obj.Contents(), password)).name,
        'Type': table_encryption.convert_string(obj.Type(), password),
        'ImagePathKr': table_encryption.convert_string(obj.ImagePathKr(), password),
        'ImagePathJp': table_encryption.convert_string(obj.ImagePathJp(), password),
    }


def dump_VideoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'VideoPath': [table_encryption.convert_string(obj.VideoPath(j), password) for j in range(obj.VideoPathLength())],
        'SoundPath': [table_encryption.convert_string(obj.SoundPath(j), password) for j in range(obj.SoundPathLength())],
        'SoundVolume': [table_encryption.convert_float(obj.SoundVolume(j), password) for j in range(obj.SoundVolumeLength())],
    }


def dump_VoiceCommonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'VoiceEvent': VoiceEvent(table_encryption.convert_int(obj.VoiceEvent_(), password)).name,
        'Rate': table_encryption.convert_long(obj.Rate(), password),
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
    }


def dump_VoiceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'Path': [table_encryption.convert_string(obj.Path(j), password) for j in range(obj.PathLength())],
        'Volume': [table_encryption.convert_float(obj.Volume(j), password) for j in range(obj.VolumeLength())],
    }


def dump_VoiceLogicEffectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'LogicEffectNameHash': table_encryption.convert_uint(obj.LogicEffectNameHash(), password),
        'Self': obj.Self(),
        'Priority': table_encryption.convert_int(obj.Priority(), password),
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
        'VoiceId': table_encryption.convert_uint(obj.VoiceId(), password),
    }


def dump_VoiceRoomExceptionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CostumeUniqueId': table_encryption.convert_long(obj.CostumeUniqueId(), password),
        'LinkedCharacterVoicePrintType': CVPrintType(table_encryption.convert_int(obj.LinkedCharacterVoicePrintType(), password)).name,
        'LinkedCostumeUniqueId': table_encryption.convert_long(obj.LinkedCostumeUniqueId(), password),
    }


def dump_VoiceSpineExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'Path': [table_encryption.convert_string(obj.Path(j), password) for j in range(obj.PathLength())],
        'SoundVolume': [table_encryption.convert_float(obj.SoundVolume(j), password) for j in range(obj.SoundVolumeLength())],
    }


def dump_VoiceTimelineExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'Nation': [Nation(table_encryption.convert_int(obj.Nation_(j), password)).name for j in range(obj.NationLength())],
        'Path': [table_encryption.convert_string(obj.Path(j), password) for j in range(obj.PathLength())],
        'SoundVolume': [table_encryption.convert_float(obj.SoundVolume(j), password) for j in range(obj.SoundVolumeLength())],
    }


class GroundNodeType(IntEnum):
    none = 0
    WalkAble = 1
    JumpAble = 2
    TSSOnly = 3
    NotWalkAble = 2147483647

class BubbleType(IntEnum):
    Idle = 0
    Monologue = 1
    EmoticonNormal = 2
    EmoticonFavorite = 3
    EmoticonReward = 4
    EmoticonGiveGift = 5

class FurnitureCategory(IntEnum):
    Furnitures = 0
    Decorations = 1
    Interiors = 2

class FurnitureSubCategory(IntEnum):
    Table = 0
    Closet = 1
    Chair = 2
    Bed = 3
    FurnitureEtc = 4
    FurnitureSubCategory1 = 5
    Prop = 6
    HomeAppliance = 7
    WallDecoration = 8
    FloorDecoration = 9
    DecorationEtc = 10
    DecorationSubCategory1 = 11
    Floor = 12
    Background = 13
    Wallpaper = 14
    InteriorsSubCategory1 = 15
    All = 16

class FurnitureLocation(IntEnum):
    none = 0
    Inventory = 1
    Floor = 2
    WallLeft = 3
    WallRight = 4

class AcademyMessageConditions(IntEnum):
    none = 0
    FavorRankUp = 1
    AcademySchedule = 2
    Answer = 3
    Feedback = 4

class AcademyMessageTypes(IntEnum):
    none = 0
    Text = 1
    Image = 2

class VoiceEvent(IntEnum):
    OnTSA = 0
    FormationPickUp = 1
    CampaignResultDefeat = 2
    CampaignResultVictory = 3
    CharacterLevelUp = 4
    CharacterTranscendence = 5
    SkillLevelUp = 6
    Formation = 7
    CampaignCharacterSpawn = 8
    BattleStartTimeline = 9
    BattleVictoryTimeline = 10
    CharacterFavor = 11
    BattleMiss = 12
    BattleBlock = 13
    BattleCover = 14
    BattleMove = 15
    BattleMoveToForamtionBeacon = 16
    MGS_GameStart = 17
    MGS_CharacterSelect = 18
    MGS_Attacking = 19
    MGS_GeasGet = 20
    EXSkill = 21
    EXSkillLevel = 22
    EXSkill2 = 23
    EXSkillLevel2 = 24
    EXSkill3 = 25
    EXSkillLevel3 = 26
    EXSkill4 = 27
    EXSkillLevel4 = 28
    PublicSkill01 = 29
    PublicSkill02 = 30
    InteractionPublicSkill01 = 31
    InteractionPublicSkill02 = 32
    FormationStyleChange = 33

class UnitType(IntEnum):
    none = 0
    AR = 1
    RF = 2
    HG = 3
    MG = 4
    SMG = 5
    SG = 6
    HZ = 7
    Melee = 8

class AttackType(IntEnum):
    Single = 0
    Splash = 1
    Through = 2
    Heal = 3

class ProjectileType(IntEnum):
    Guided = 0
    Ground = 1
    GuidedExplosion = 2
    GroundConstDistance = 3
    AirConstDistance = 4

class DamageFontColor(IntEnum):
    Blue = 0
    White = 1
    Yellow = 2
    Red = 3
    Green = 4

class TargetingCellType(IntEnum):
    none = 0
    Near = 1
    Far = 2

class TargetingUnitType(IntEnum):
    none = 0
    Near = 1
    Far = 2
    MinHp = 3
    MaxHp = 4
    Random = 5

class ProjectileAction(IntEnum):
    none = 0
    Damage = 1
    Heal = 2

class FontType(IntEnum):
    none = 0
    Damage = 1
    Block = 2
    Heal = 3
    Miss = 4
    Critical = 5
    Skill = 6
    Immune = 7
    DamageResist = 8
    DamageWeak = 9
    CriticalResist = 10
    CriticalWeak = 11
    Effective = 12
    CriticalEffective = 13

class EmoticonEvent(IntEnum):
    CoverEnter = 0
    ShelterEnter = 1
    Panic = 2
    NearlyDead = 3
    Reload = 4
    Found = 5
    GetBeacon = 6
    Warning = 7

class BulletType(IntEnum):
    Normal = 0
    Pierce = 1
    Explosion = 2
    Siege = 3
    Mystic = 4
    none = 5
    Sonic = 6

class ActionType(IntEnum):
    Crush = 0
    Courage = 1
    Tactic = 2

class BuffOverlap(IntEnum):
    Able = 0
    Unable = 1
    Change = 2
    Additive = 3

class ReArrangeTargetType(IntEnum):
    AllySelf = 0
    AllyAll = 1
    AllyUnitType = 2
    AllyGroup = 3

class ArmorType(IntEnum):
    LightArmor = 0
    HeavyArmor = 1
    Unarmed = 2
    Structure = 3
    Normal = 4
    ElasticArmor = 5

class WeaponType(IntEnum):
    none = 0
    SG = 1
    SMG = 2
    AR = 3
    GL = 4
    HG = 5
    RL = 6
    SR = 7
    DSMG = 8
    RG = 9
    DSG = 10
    Vulcan = 11
    Missile = 12
    Cannon = 13
    Taser = 14
    MG = 15
    Binah = 16
    MT = 17
    Relic = 18
    FT = 19
    Akemi = 20

class EntityMaterialType(IntEnum):
    Wood = 0
    Stone = 1
    Flesh = 2
    Metal = 3

class CoverMotionType(IntEnum):
    All = 0
    Kneel = 1

class TargetSortBy(IntEnum):
    DISTANCE = 0
    HP = 1
    DAMAGE_EFFICIENCY = 2
    TARGETED_COUNT = 3
    RANDOM = 4
    FRONT_FORMATION = 5

class PositioningType(IntEnum):
    CloseToObstacle = 0
    CloseToTarget = 1

class DamageType(IntEnum):
    Normal = 0
    Critical = 1
    IgnoreDefence = 2

class FormationLine(IntEnum):
    Students = 0
    TSS = 1

class ExternalBTNodeType(IntEnum):
    Sequence = 0
    Selector = 1
    Instant = 2
    SubNode = 3
    ExecuteAll = 4

class ExternalBTTrigger(IntEnum):
    none = 0
    HPUnder = 1
    ApplySkillEffectCategory = 2
    HaveNextExSkillActiveGauge = 3
    UseNormalSkill = 4
    UseExSkill = 5
    CheckActiveGaugeOver = 6
    CheckPeriod = 7
    CheckSummonCharacterCountOver = 8
    CheckSummonCharacterCountUnder = 9
    ApplyGroggy = 10
    ApplyLogicEffectTemplateId = 11
    OnSpawned = 12
    CheckActiveGaugeBetween = 13
    DestroyParts = 14
    CheckHallucinationCountOver = 15
    CheckHallucinationCountUnder = 16
    UseSkillEndGroupId = 17

class ExternalBehavior(IntEnum):
    UseNextExSkill = 0
    ChangePhase = 1
    ChangeSection = 2
    AddActiveGauge = 3
    UseSelectExSkill = 4
    ClearNormalSkill = 5
    MoveLeft = 6
    MoveRight = 7
    AllUseSelectExSkill = 8
    ConnectCharacterToDummy = 9
    ConnectExSkillToParts = 10
    SetMaxHPToParts = 11
    AlivePartsUseExSkill = 12
    ActivatePart = 13
    AddGroggy = 14
    SelectTargetToUseSkillAlly = 15
    ForceChangePhase = 16
    ClearUseSkillEndGroupId = 17

class TacticEntityType(IntEnum):
    none = 0
    Student = 1
    Minion = 2
    Elite = 4
    Champion = 8
    Boss = 16
    Obstacle = 32
    Servant = 64
    Vehicle = 128
    Summoned = 256
    Hallucination = 512
    DestructibleProjectile = 1024

class BuffIconType(IntEnum):
    none = 0
    Debuff_DyingPenalty = 1
    CC_MindControl = 2
    CC_Inoperative = 3
    CC_Confusion = 4
    CC_Provoke = 5
    CC_Silence = 6
    CC_Blind = 7
    Dot_Damage = 8
    Dot_Heal = 9
    Buff_AttackPower = 10
    Buff_CriticalChance = 11
    Buff_CriticalDamage = 12
    Buff_DefensePower = 13
    Buff_Dodge = 14
    Buff_Hit = 15
    Buff_WeaponRange = 16
    Buff_SightRange = 17
    Buff_MoveSpeed = 18
    Buff_Mind = 19
    Debuf_AttackPower = 20
    Debuff_CriticalChance = 21
    Debuff_CriticalDamage = 22
    Debuff_DefensePower = 23
    Debuff_Dodge = 24
    Debuff_Hit = 25
    Debuff_WeaponRange = 26
    Debuff_SightRange = 27
    Debuff_MoveSpeed = 28
    Debuff_Mind = 29
    Buff_AttackTime = 30
    Debuff_AttackTime = 31
    Buff_MaxHp = 32
    Debuff_MaxHp = 33
    Buff_MaxBulletCount = 34
    Debuff_MaxBulletCount = 35
    Debuff_SuppliesCondition = 36
    Buff_HealEffectivenessRate = 37
    Debuff_HealEffectivenessRate = 38
    Buff_HealPower = 39
    Debuff_HealPower = 40
    Buff_CriticalChanceResistPoint = 41
    Debuff_CriticalChanceResistPoint = 42
    CC_Stunned = 43
    Debuff_ConcentratedTarget = 44
    Buff_Immortal = 45
    Max = 46

class Difficulty(IntEnum):
    Normal = 0
    Hard = 1
    VeryHard = 2
    Hardcore = 3
    Extreme = 4
    Insane = 5
    Torment = 6

class EngageType(IntEnum):
    SearchAndMove = 0
    HoldPosition = 1

class HitEffectPosition(IntEnum):
    Position = 0
    HeadBone = 1
    BodyBone = 2
    Follow = 3

class StageTopography(IntEnum):
    Street = 0
    Outdoor = 1
    Indoor = 2

class TerrainAdaptationStat(IntEnum):
    D = 0
    C = 1
    B = 2
    A = 3
    S = 4
    SS = 5

class SquadType(IntEnum):
    none = 0
    Main = 1
    Support = 2
    TSS = 3

class ObstacleClass(IntEnum):
    MAIN = 0
    SUB = 1

class ObstacleDestroyType(IntEnum):
    Remain = 0
    Remove = 1

class ObstacleHeightType(IntEnum):
    Low = 0
    Middle = 1
    High = 2

class ObstacleCoverType(IntEnum):
    none = 0
    Cover = 1
    Shelter = 2

class SkillCategory(IntEnum):
    none = 0

class LogicEffectCategory(IntEnum):
    none = 0
    Attack = 1
    Heal = 2
    Buff = 3
    Debuff = 4
    CrowdControl = 5
    Boss = 6
    Dummy = 7

class AimIKType(IntEnum):
    none = 0
    OneHandRight = 1
    OneHandLeft = 2
    TwoHandRight = 3
    TwoHandLeft = 4
    Tripod = 5
    Dual = 6
    Max = 7

class DamageAttribute(IntEnum):
    Resist = 0
    Normal = 1
    Weak = 2
    Effective = 3

class SkillPriorityCheckCondition(IntEnum):
    none = 0
    HPRateUnder = 1
    DebuffCountOver = 2
    BuffCountOver = 3
    CrowdControlOver = 4

class SkillPriorityCheckTarget(IntEnum):
    Ally = 0
    Enemy = 1
    All = 2

class StageType(IntEnum):
    Main = 0
    Sub = 1

class OperatorCondition(IntEnum):
    none = 0
    StrategyStart = 1
    StrategyVictory = 2
    StrategyDefeat = 3
    AdventureCombatStart = 4
    AdventureCombatVictory = 5
    AdventureCombatDefeat = 6
    ArenaCombatStart = 7
    ArenaCombatVictory = 8
    ArenaCombatDefeat = 9
    WeekDungeonCombatStart = 10
    WeekDungeonCombatVictory = 11
    WeekDungeonCombatDefeat = 12
    SchoolDungeonCombatStart = 13
    SchoolDungeonCombatVictory = 14
    SchoolDungeonCombatDefeat = 15
    StrategyWarpUnitFromHideTile = 16
    TimeAttackDungeonStart = 17
    TimeAttackDungeonVictory = 18
    TimeAttackDungeonDefeat = 19
    WorldRaidBossSpawn = 20
    WorldRaidBossKill = 21
    WorldRaidBossDamaged = 22
    WorldRaidScenarioBattle = 23
    MinigameTBGThemaOpen = 24
    MinigameTBGThemaComeback = 25
    MinigameTBGAllyRevive = 26
    MinigameTBGItemUse = 27

class KnockbackDirection(IntEnum):
    TargetToCaster = 0
    CasterToTarget = 1
    TargetToHitPosition = 2
    HitPositionToTarget = 3
    CasterToHitPosition = 4
    HitPositionToCaster = 5
    Caster = 6
    Target = 7

class EndCondition(IntEnum):
    Duration = 0
    ReloadCount = 1
    AmmoCount = 2
    AmmoHit = 3
    HitCount = 4
    none = 5
    UseExSkillCount = 6

class LogicEffectSound(IntEnum):
    none = 0
    Damage = 1
    Heal = 2
    Knockback = 3

class EffectBone(IntEnum):
    none = 0
    Shot = 1
    Head = 2
    Body = 3
    Shot2 = 4
    Shot3 = 5
    Extra = 6
    Extra2 = 7
    Extra3 = 8

class ArenaSimulatorServer(IntEnum):
    Preset = 0
    Live = 1
    Dev = 2
    QA = 3

class ClearCheck(IntEnum):
    none = 0
    Success_Play = 1
    Success_Sweep = 2
    Fail_Timeout = 3
    Fail_PlayerGiveUp = 4
    Fail_Annihilation = 5

class BuffType(IntEnum):
    none = 0
    Buff_AttackPower = 1
    Buff_CriticalChance = 2
    Buff_CriticalDamage = 3
    Buff_DefensePower = 4
    Buff_Dodge = 5
    Buff_Hit = 6
    Buff_WeaponRange = 7
    Buff_SightRange = 8
    Buff_MoveSpeed = 9
    Buff_AttackTime = 10
    Buff_MaxHp = 11
    Buff_MaxBulletCount = 12
    DeBuff_AttackPower = 13
    DeBuff_CriticalChance = 14
    DeBuff_CriticalDamage = 15
    DeBuff_DefensePower = 16
    DeBuff_Dodge = 17
    DeBuff_Hit = 18
    DeBuff_WeaponRange = 19
    DeBuff_SightRange = 20
    DeBuff_MoveSpeed = 21
    DeBuff_AttackTime = 22
    DeBuff_MaxHp = 23
    DeBuff_MaxBulletCount = 24

class WorldRaidDifficulty(IntEnum):
    none = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7

class TacticSpeed(IntEnum):
    none = 0
    Slow = 1
    Normal = 2
    Fast = 3

class TacticSkillUse(IntEnum):
    none = 0
    Auto = 1
    Manual = 2

class ShowSkillCutIn(IntEnum):
    none = 0
    Once = 1
    Always = 2

class BattleCalculationStat(IntEnum):
    FinalDamage = 0
    FinalHeal = 1
    FinalDamageRatio = 2
    FinalDamageRatio2 = 3
    FinalCriticalRate = 4

class StatTransType(IntEnum):
    SpecialTransStat = 0
    TSATransStat = 1

class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2
    Obstacle = 3
    TimeAttack = 4

class GrowthCategory(IntEnum):
    none = 0
    LevelUp = 1
    Transcend = 2
    SkillLevelUp = 3

class StatType(IntEnum):
    none = 0
    MaxHP = 1
    AttackPower = 2
    DefensePower = 3
    HealPower = 4
    AccuracyPoint = 5
    AccuracyRate = 6
    DodgePoint = 7
    DodgeRate = 8
    CriticalPoint = 9
    CriticalChanceRate = 10
    CriticalResistChanceRate = 11
    CriticalDamageRate = 12
    MoveSpeed = 13
    SightRange = 14
    ActiveGauge = 15
    StabilityPoint = 16
    StabilityRate = 17
    ReloadTime = 18
    MaxBulletCount = 19
    IgnoreDelayCount = 20
    WeaponRange = 21
    BlockRate = 22
    BodyRadius = 23
    ActionCount = 24
    StrategyMobility = 25
    StrategySightRange = 26
    StreetBattleAdaptation = 27
    OutdoorBattleAdaptation = 28
    IndoorBattleAdaptation = 29
    HealEffectivenessRate = 30
    CriticalChanceResistPoint = 31
    CriticalDamageResistRate = 32
    LifeRecoverOnHit = 33
    NormalAttackSpeed = 34
    AmmoCost = 35
    GroggyGauge = 36
    GroggyTime = 37
    DamageRatio = 38
    DamagedRatio = 39
    OppressionPower = 40
    OppressionResist = 41
    RegenCost = 42
    InitialWeaponRangeRate = 43
    DefensePenetration = 44
    DefensePenetrationResisit = 45
    ExtendBuffDuration = 46
    ExtendDebuffDuration = 47
    ExtendCrowdControlDuration = 48
    EnhanceExplosionRate = 49
    EnhancePierceRate = 50
    EnhanceMysticRate = 51
    EnhanceLightArmorRate = 52
    EnhanceHeavyArmorRate = 53
    EnhanceUnarmedRate = 54
    EnhanceSiegeRate = 55
    EnhanceNormalRate = 56
    EnhanceStructureRate = 57
    EnhanceNormalArmorRate = 58
    DamageRatio2Increase = 59
    DamageRatio2Decrease = 60
    DamagedRatio2Increase = 61
    DamagedRatio2Decrease = 62
    EnhanceSonicRate = 63
    EnhanceElasticArmorRate = 64
    ExDamagedRatioIncrease = 65
    ExDamagedRatioDecrease = 66
    Max = 67

class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3

class TacticRole(IntEnum):
    none = 0
    DamageDealer = 1
    Tanker = 2
    Supporter = 3
    Healer = 4
    Vehicle = 5

class TacticRange(IntEnum):
    Back = 0
    Front = 1
    Middle = 2

class CVCollectionType(IntEnum):
    CVNormal = 0
    CVEvent = 1
    CVEtc = 2

class CVPrintType(IntEnum):
    CharacterOverwrite = 0
    PrefabOverwrite = 1
    Add = 2

class CVExceptionTarget(IntEnum):
    CharacterId = 0
    SquadType = 1

class PotentialStatBonusRateType(IntEnum):
    none = 0
    MaxHP = 1
    AttackPower = 2
    HealPower = 3

class ClanSocialGrade(IntEnum):
    none = 0
    President = 1
    Manager = 2
    Member = 3
    Applicant = 4
    Refused = 5
    Kicked = 6
    Quit = 7
    VicePredisident = 8

class ClanJoinOption(IntEnum):
    Free = 0
    Permission = 1
    All = 2

class ClanSearchOption(IntEnum):
    Name = 0
    Id = 1

class ClanRewardType(IntEnum):
    none = 0
    AssistTerm = 1
    AssistRent = 2
    Attendance = 3

class ConquestEnemyType(IntEnum):
    none = 0
    Normal = 1
    MiddleBoss = 2
    Boss = 3
    UnexpectedEvent = 4
    Challenge = 5
    IndividualErosion = 6
    MassErosion = 7

class ConquestTeamType(IntEnum):
    none = 0
    Team1 = 1
    Team2 = 2
    Team3 = 3

class ConquestTileType(IntEnum):
    none = 0
    Start = 1
    Normal = 2
    Battle = 3
    Base = 4

class ConquestObjectType(IntEnum):
    none = 0
    ParcelOneTimePerAccount = 1

class ConquestItemType(IntEnum):
    none = 0
    EventPoint = 1
    EventToken1 = 2
    EventToken2 = 3
    EventToken3 = 4
    EventToken4 = 5
    EventToken5 = 6

class ConquestProgressType(IntEnum):
    none = 0
    Upgrade = 1
    Manage = 2

class TileState(IntEnum):
    none = 0
    PartiallyConquested = 1
    FullyConquested = 2

class ConquestEventType(IntEnum):
    none = 0
    Event01 = 1
    Event02 = 2

class ConquestConditionType(IntEnum):
    none = 0
    OpenDateOffset = 1
    ItemAcquire = 2
    ParcelUse = 3
    KillUnit = 4

class ConquestErosionType(IntEnum):
    none = 0
    IndividualErosion = 1
    MassErosion = 2

class ContentType(IntEnum):
    none = 0
    CampaignMainStage = 1
    CampaignSubStage = 2
    WeekDungeon = 3
    EventContentMainStage = 4
    EventContentSubStage = 5
    CampaignTutorialStage = 6
    EventContentMainGroundStage = 7
    SchoolDungeon = 8
    TimeAttackDungeon = 9
    Raid = 10
    Conquest = 11
    EventContentStoryStage = 12
    CampaignExtraStage = 13
    StoryStrategyStage = 14
    ScenarioMode = 15
    EventContent = 16
    WorldRaid = 17
    EliminateRaid = 18
    Chaser = 19
    FieldContentStage = 20
    MultiFloorRaid = 21
    MinigameDefense = 22

class EventContentType(IntEnum):
    Stage = 0
    Gacha = 1
    Mission = 2
    Shop = 3
    Raid = 4
    Arena = 5
    BoxGacha = 6
    Collection = 7
    Recollection = 8
    MiniGameRhythm = 9
    CardShop = 10
    EventLocation = 11
    MinigameRhythmEvent = 12
    FortuneGachaShop = 13
    SubEvent = 14
    EventMeetup = 15
    BoxGachaResult = 16
    Conquest = 17
    WorldRaid = 18
    DiceRace = 19
    MiniGameRhythmMission = 20
    WorldRaidEntrance = 21
    MiniEvent = 22
    MiniGameShooting = 23
    MiniGameShootingMission = 24
    MiniGameTBG = 25
    TimeAttackDungeon = 26
    EliminateRaid = 27
    Treasure = 28
    Field = 29
    MultiFloorRaid = 30
    MinigameDreamMaker = 31
    MiniGameDefense = 32

class OpenCondition(IntEnum):
    Hide = 0
    Lock = 1
    Open = 2

class ResetContentType(IntEnum):
    none = 0
    HardStagePlay = 1
    StarategyMapHeal = 2
    ShopRefresh = 3
    ArenaDefenseVictoryReward = 4
    WeeklyMasterCoin = 5
    WorldRaidGemEnterCount = 6
    ConquestDailyErosionCheck = 7
    MiniEventToken = 8

class WeekDungeonType(IntEnum):
    none = 0
    ChaserA = 1
    ChaserB = 2
    ChaserC = 3
    FindGift = 4
    Blood = 5

class StarGoalType(IntEnum):
    none = 0
    AllAlive = 1
    Clear = 2
    GetBoxes = 3
    ClearTimeInSec = 4
    AllyBaseDamage = 5

class OpenConditionContent(IntEnum):
    Shop = 0
    Gacha = 1
    LobbyIllust = 2
    Raid = 3
    Cafe = 4
    Unit_Growth_Skill = 5
    Unit_Growth_LevelUp = 6
    Unit_Growth_Transcendence = 7
    Arena = 8
    Academy = 9
    Equip = 10
    Item = 11
    Favor = 12
    Prologue = 13
    Mission = 14
    WeekDungeon_Chase = 15
    __Deprecated_WeekDungeon_FindGift = 16
    __Deprecated_WeekDungeon_Blood = 17
    Story_Sub = 18
    Story_Replay = 19
    WeekDungeon = 20
    none = 21
    Shop_Gem = 22
    Craft = 23
    Student = 24
    GuideMission = 25
    Clan = 26
    Echelon = 27
    Campaign = 28
    EventContent = 29
    Guild = 30
    EventStage_1 = 31
    EventStage_2 = 32
    Talk = 33
    Billing = 34
    Schedule = 35
    Story = 36
    Tactic_Speed = 37
    Cafe_Invite = 38
    EventMiniGame_1 = 39
    SchoolDungeon = 40
    TimeAttackDungeon = 41
    ShiftingCraft = 42
    WorldRaid = 43
    Tactic_Skip = 44
    Mulligan = 45
    EventPermanent = 46
    Main_L_1_2 = 47
    Main_L_1_3 = 48
    Main_L_1_4 = 49
    EliminateRaid = 50
    Cafe_2 = 51
    Cafe_Invite_2 = 52
    MultiFloorRaid = 53
    StrategySkip = 54
    MinigameDreamMaker = 55
    MiniGameDefense = 56

class ContentLockType(IntEnum):
    none = 0
    NotUseControlledByOtherSetting = 1
    Academy = 2
    MultiFloorRaid = 3
    EventContent = 4
    EventNotice = 5
    GuideMission = 6
    Campaign = 7
    Story = 8
    WeekDungeon_Chase = 9
    WeekDungeon = 10
    SchoolDungeon = 11
    Raid = 12
    EliminateRaid = 13
    TimeAttackDungeon = 14
    Arena = 15
    Cafe = 16
    GemShop = 17
    Gacha = 18
    Craft = 19
    MomoTalk = 20

class TutorialFailureContentType(IntEnum):
    none = 0
    Campaign = 1
    WeekDungeon = 2
    Raid = 3
    TimeAttackDungeon = 4
    WorldRaid = 5
    Conquest = 6
    EliminateRaid = 7
    MultiFloorRaid = 8

class FeverBattleType(IntEnum):
    Campaign = 0
    Raid = 1
    WeekDungeon = 2
    Arena = 3

class EventContentScenarioConditionType(IntEnum):
    none = 0
    DayAfter = 1
    EventPoint = 2

class EventTargetType(IntEnum):
    WeekDungeon = 0
    Chaser = 1
    Campaign_Normal = 2
    Campaign_Hard = 3
    SchoolDungeon = 4
    AcademySchedule = 5
    TimeAttackDungeon = 6
    AccountLevelExpIncrease = 7
    Raid = 8
    EliminateRaid = 9

class ContentResultType(IntEnum):
    Failure = 0
    Success = 1

class EventContentItemType(IntEnum):
    EventPoint = 0
    EventToken1 = 1
    EventToken2 = 2
    EventToken3 = 3
    EventToken4 = 4
    EventToken5 = 5
    EventMeetUpTicket = 6
    EventEtcItem = 7

class RaidSeasonType(IntEnum):
    none = 0
    Open = 1
    Close = 2
    Settlement = 3

class BuffConditionType(IntEnum):
    All = 0
    Character = 1
    School = 2
    Weapon = 3

class CollectionUnlockType(IntEnum):
    none = 0
    ClearSpecificEventStage = 1
    ClearSpecificEventScenario = 2
    ClearSpecificEventMission = 3
    PurchaseSpecificItemCount = 4
    SpecificEventLocationRank = 5
    DiceRaceConsumeDiceCount = 6
    MinigameTBGThemaClear = 7
    MinigameEnter = 8
    MinigameDreamMakerParameter = 9
    ClearSpecificScenario = 10

class ShortcutContentType(IntEnum):
    none = 0
    CampaignStage = 1
    EventStage = 2
    Blood = 3
    WeekDungeon = 4
    Arena = 5
    Raid = 6
    Shop = 7
    ItemInventory = 8
    Craft = 9
    SchoolDungeon = 10
    Academy = 11
    Mission = 12
    MultiFloorRaid = 13

class JudgeGrade(IntEnum):
    none = 0
    Miss = 1
    Attack = 2
    Critical = 3

class SchoolDungeonType(IntEnum):
    SchoolA = 0
    SchoolB = 1
    SchoolC = 2
    none = 3

class EventContentBuffFindRule(IntEnum):
    none = 0
    WeaponType = 1
    SquadType = 2
    StreetBattleAdaptation = 3
    OutdoorBattleAdaptation = 4
    IndoorBattleAdaptation = 5
    BulletType = 6
    School = 7
    TacticRange = 8

class TimeAttackDungeonRewardType(IntEnum):
    Fixed = 0
    TimeWeight = 1

class TimeAttackDungeonType(IntEnum):
    none = 0
    Defense = 1
    Shooting = 2
    Destruction = 3
    Escort = 4

class SuddenMissionContentType(IntEnum):
    OrdinaryState = 0
    CampaignNormalStage = 1
    CampaignHardStage = 2
    EventStage = 3
    WeekDungeon = 4
    Chaser = 5
    SchoolDungeon = 6
    TimeAttackDungeon = 7
    Raid = 8

class ContentsChangeType(IntEnum):
    none = 0
    WorldRaidBossDamageRatio = 1
    WorldRaidBossGroupDate = 2

class EventNotifyType(IntEnum):
    RewardIncreaseEvent = 0
    AccountExpIncreaseEvent = 1
    RaidSeasonManager = 2
    TimeAttackDungeonSeasonManage = 3
    EliminateRaidSeasonManage = 4

class EventContentDiceRaceResultType(IntEnum):
    DiceResult1 = 0
    DiceResult2 = 1
    DiceResult3 = 2
    DiceResult4 = 3
    DiceResult5 = 4
    DiceResult6 = 5
    MoveForward = 6
    LapFinish = 7
    EventOccur = 8
    DiceResultFixed1 = 9
    DiceResultFixed2 = 10
    DiceResultFixed3 = 11
    DiceResultFixed4 = 12
    DiceResultFixed5 = 13
    DiceResultFixed6 = 14
    SpecialReward = 15

class EventContentDiceRaceNodeType(IntEnum):
    StartNode = 0
    RewardNode = 1
    MoveForwardNode = 2
    SpecialRewardNode = 3

class MeetupConditionType(IntEnum):
    none = 0
    EventContentStageClear = 1
    ScenarioClear = 2

class MeetupConditionPrintType(IntEnum):
    none = 0
    Lock = 1
    Hide = 2

class GuideMissionTabType(IntEnum):
    none = 0
    Daily = 1
    StageClear = 2

class RankingSearchType(IntEnum):
    none = 0
    Rank = 1
    Score = 2

class EventContentReleaseType(IntEnum):
    none = 0
    Permanent = 1
    MainStory = 2
    PermanentSpecialOperate = 3
    PermanentConquest = 4

class CraftSlotIndex(IntEnum):
    Slot00 = 0
    Slot01 = 1
    Slot02 = 2
    Max = 3

class CraftNodeTier(IntEnum):
    Base = 0
    Node01 = 1
    Node02 = 2
    Node03 = 3
    Max = 4

class SubEventType(IntEnum):
    none = 0
    SubEvent = 1
    SubEventPermanent = 2

class EquipmentCategory(IntEnum):
    Unable = 0
    Exp = 1
    Bag = 2
    Hat = 3
    Gloves = 4
    Shoes = 5
    Badge = 6
    Hairpin = 7
    Charm = 8
    Watch = 9
    Necklace = 10
    WeaponExpGrowthA = 11
    WeaponExpGrowthB = 12
    WeaponExpGrowthC = 13
    WeaponExpGrowthZ = 14

class EquipmentOptionType(IntEnum):
    none = 0
    MaxHP_Base = 1
    MaxHP_Coefficient = 2
    AttackPower_Base = 3
    AttackPower_Coefficient = 4
    DefensePower_Base = 5
    DefensePower_Coefficient = 6
    HealPower_Base = 7
    HealPower_Coefficient = 8
    CriticalPoint_Base = 9
    CriticalPoint_Coefficient = 10
    CriticalChanceRate_Base = 11
    CriticalDamageRate_Base = 12
    CriticalDamageRate_Coefficient = 13
    SightRange_Base = 14
    SightRange_Coefficient = 15
    MaxBulletCount_Base = 16
    MaxBulletCount_Coefficient = 17
    HPRecoverOnKill_Base = 18
    HPRecoverOnKill_Coefficient = 19
    StreetBattleAdaptation_Base = 20
    OutdoorBattleAdaptation_Base = 21
    IndoorBattleAdaptation_Base = 22
    HealEffectivenessRate_Base = 23
    HealEffectivenessRate_Coefficient = 24
    CriticalChanceResistPoint_Base = 25
    CriticalChanceResistPoint_Coefficient = 26
    CriticalDamageResistRate_Base = 27
    CriticalDamageResistRate_Coefficient = 28
    ExSkillUpgrade = 29
    OppressionPower_Base = 30
    OppressionPower_Coefficient = 31
    OppressionResist_Base = 32
    OppressionResist_Coefficient = 33
    StabilityPoint_Base = 34
    StabilityPoint_Coefficient = 35
    AccuracyPoint_Base = 36
    AccuracyPoint_Coefficient = 37
    DodgePoint_Base = 38
    DodgePoint_Coefficient = 39
    MoveSpeed_Base = 40
    MoveSpeed_Coefficient = 41
    Max = 42
    NormalAttackSpeed_Base = 43
    NormalAttackSpeed_Coefficient = 44
    DefensePenetration_Base = 45
    DefensePenetrationResisit_Base = 46
    ExtendBuffDuration_Base = 47
    ExtendDebuffDuration_Base = 48
    ExtendCrowdControlDuration_Base = 49
    EnhanceExplosionRate_Base = 50
    EnhanceExplosionRate_Coefficient = 51
    EnhancePierceRate_Base = 52
    EnhancePierceRate_Coefficient = 53
    EnhanceMysticRate_Base = 54
    EnhanceMysticRate_Coefficient = 55
    EnhanceLightArmorRate_Base = 56
    EnhanceLightArmorRate_Coefficient = 57
    EnhanceHeavyArmorRate_Base = 58
    EnhanceHeavyArmorRate_Coefficient = 59
    EnhanceUnarmedRate_Base = 60
    EnhanceUnarmedRate_Coefficient = 61
    EnhanceSiegeRate_Base = 62
    EnhanceSiegeRate_Coefficient = 63
    EnhanceNormalRate_Base = 64
    EnhanceNormalRate_Coefficient = 65
    EnhanceStructureRate_Base = 66
    EnhanceStructureRate_Coefficient = 67
    EnhanceNormalArmorRate_Base = 68
    EnhanceNormalArmorRate_Coefficient = 69
    DamageRatio2Increase_Base = 70
    DamageRatio2Increase_Coefficient = 71
    DamageRatio2Decrease_Base = 72
    DamageRatio2Decrease_Coefficient = 73
    DamagedRatio2Increase_Base = 74
    DamagedRatio2Increase_Coefficient = 75
    DamagedRatio2Decrease_Base = 76
    DamagedRatio2Decrease_Coefficient = 77
    EnhanceSonicRate_Base = 78
    EnhanceSonicRate_Coefficient = 79
    EnhanceElasticArmorRate_Base = 80
    EnhanceElasticArmorRate_Coefficient = 81
    IgnoreDelayCount_Base = 82
    WeaponRange_Base = 83
    BlockRate_Base = 84
    BlockRate_Coefficient = 85
    AmmoCost_Base = 86
    RegenCost_Base = 87
    RegenCost_Coefficient = 88

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class Language(IntEnum):
    Kr = 0
    Jp = 1
    Th = 2
    Tw = 3
    En = 4

class SoundType(IntEnum):
    UI = 0
    BGM = 1
    FX = 2

class WeekDay(IntEnum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    All = 7

class EchelonType(IntEnum):
    none = 0
    Adventure = 1
    Raid = 2
    ArenaAttack = 3
    ArenaDefence = 4
    WeekDungeonChaserA = 5
    Scenario = 6
    WeekDungeonBlood = 7
    WeekDungeonChaserB = 8
    WeekDungeonChaserC = 9
    WeekDungeonFindGift = 10
    EventContent = 11
    SchoolDungeonA = 12
    SchoolDungeonB = 13
    SchoolDungeonC = 14
    TimeAttack = 15
    WorldRaid = 16
    Conquest = 17
    ConquestManage = 18
    StoryStrategyStage = 19
    EliminateRaid01 = 20
    EliminateRaid02 = 21
    EliminateRaid03 = 22
    Field = 23
    MultiFloorRaid = 24
    MinigameDefense = 25

class EchelonExtensionType(IntEnum):
    Base = 0
    Extension = 1

class NoticeType(IntEnum):
    none = 0
    Notice = 1
    Event = 2

class RewardTag(IntEnum):
    Default = 0
    FirstClear = 1
    StrategyObject = 2
    Event = 3
    ThreeStar = 4
    ProductMonthly = 5
    Rare = 6
    EventBonus = 7
    TimeWeight = 8
    ProductWeekly = 9
    ProductBiweekly = 10
    EventPermanentReward = 11
    ConquestManageEvent = 12
    ConquestManageDefault = 13
    ConquestCalculateDefault = 14
    ConquestCalculateLevel2 = 15
    ConquestCalculateLevel3 = 16
    ConquestFootholdUpgrade2 = 17
    ConquestFootholdUpgrade3 = 18
    ConquestErosionPenalty = 19
    GemBonus = 20
    GemPaid = 21
    ConquestTileConquer = 22

class ArenaRewardType(IntEnum):
    none = 0
    Time = 1
    Daily = 2
    SeasonRecord = 3
    OverallRecord = 4
    SeasonClose = 5
    AttackVictory = 6
    DefenseVictory = 7
    RankIcon = 8

class ServiceActionType(IntEnum):
    ClanCreate = 0
    HardAdventurePlayCountRecover = 1

class RaidStatus(IntEnum):
    none = 0
    Playing = 1
    Clear = 2
    Close = 3

class WebAPIErrorLevel(IntEnum):
    none = 0
    Warning = 1
    Error = 2

class GachaTicketType(IntEnum):
    none = 0
    PackageThreeStar = 1
    ThreeStar = 2
    TwoStar = 3
    Normal = 4
    NormalOnce = 5
    SelectRecruit = 6
    PackagePropertyThreeStar = 7
    Temp_1 = 8
    PackageAcademyThreeStar = 9

class EventChangeType(IntEnum):
    MainSub = 0
    SubMain = 1

class CafeCharacterState(IntEnum):
    none = 0
    Idle = 1
    Walk = 2
    Reaction = 3
    Interaction = 4
    Max = 5

class FurnitureFunctionType(IntEnum):
    none = 0
    EventCollection = 1
    VideoPlay = 2
    TrophyCollection = 3
    InteractionBGMPlay = 4

class NotificationEventReddot(IntEnum):
    StagePointReward = 0
    MissionComplete = 1
    MiniGameMissionComplete = 2
    WorldRaidReward = 3
    ConquestCalculateReward = 4
    DiceRaceLapReward = 5

class EmblemCategory(IntEnum):
    none = 0
    Default = 1
    Mission = 2
    GroupStory = 3
    Event = 4
    MainStory = 5
    Favor = 6
    Boss = 7
    Etc = 8
    Etc_Anniversary = 9
    MultiFloorRaid = 10
    Potential = 11

class EmblemDisplayType(IntEnum):
    Always = 0
    Time = 1
    Favor = 2
    Potential = 3

class EmblemCheckPassType(IntEnum):
    none = 0
    Default = 1
    Favor = 2
    Story = 3
    Potential = 4

class StickerGetConditionType(IntEnum):
    none = 0
    StickerCheckPass = 1
    GetStickerCondition = 2

class Nation(IntEnum):
    none = 0
    All = 1
    JP = 2
    GL = 3
    KR = 4

class FilterCategory(IntEnum):
    Character = 0
    Equipment = 1
    Item = 2
    Craft = 3
    ShiftCraft = 4
    Shop = 5
    MemoryLobby = 6
    Trophy = 7
    Emblem = 8

class FilterIcon(IntEnum):
    TextOnly = 0
    TextWithIcon = 1
    Pin = 2
    Role = 3
    CharacterStar = 4
    WeaponStar = 5
    Attack = 6
    Defense = 7
    Range = 8
    MemoryLobby = 9

class FieldConditionType(IntEnum):
    Invalid = 0
    Interaction = 1
    QuestInProgress = 2
    QuestClear = 3
    Date = 4
    StageClear = 5
    HasKeyword = 6
    HasEvidence = 7
    OpenDate = 8
    OpenDateAfter = 9

class FieldInteractionType(IntEnum):
    none = 0
    Scenario = 1
    Reward = 2
    Dialog = 3
    Stage = 4
    KeywordFound = 5
    EvidenceFound = 6
    SceneChange = 7
    Timeline = 8
    ActionTrigger = 9
    Interplay = 10

class FieldConditionClass(IntEnum):
    AndOr = 0
    OrAnd = 1
    Multi = 2

class FieldDialogType(IntEnum):
    none = 0
    Talk = 1
    Think = 2
    Exclaim = 3
    Question = 4
    Upset = 5
    Surprise = 6
    Bulb = 7
    Heart = 8
    Sweat = 9
    Angry = 10
    Music = 11
    Dot = 12
    Momotalk = 13
    Phone = 14
    Keyword = 15
    Evidence = 16

class FieldTutorialType(IntEnum):
    none = 0
    MasteryHUD = 1
    QuestHUD = 2
    WorldMapHUD = 3

class FriendSearchLevelOption(IntEnum):
    Recommend = 0
    All = 1
    Level1To30 = 2
    Level31To40 = 3
    Level41To50 = 4
    Level51To60 = 5
    Level61To70 = 6
    Level71To80 = 7
    Level81To90 = 8
    Level91To100 = 9

class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    InvisibleToken = 8

class MailType(IntEnum):
    System = 0
    Attendance = 1
    Event = 2
    MassTrade = 3
    InventoryFull = 4
    ArenaDefenseVictory = 5
    CouponUsageReward = 6
    ArenaSeasonClose = 7
    ProductReward = 8
    MonthlyProductReward = 9
    ExpiryChangeItem = 10
    ClanAttendance = 11
    AccountLink = 12
    NewUserBonus = 13
    LeftClanAssistReward = 14
    AttendanceImmediately = 15
    WeeklyProductReward = 16
    BiweeklyProductReward = 17
    Temp_1 = 18
    Temp_2 = 19
    Temp_3 = 20
    CouponCompleteReward = 21
    BirthdayMail = 22
    FromCS = 23
    ExpiryChangeCurrency = 24

class AttendanceType(IntEnum):
    Basic = 0
    Event = 1
    Newbie = 2
    EventCountDown = 3
    Event20Days = 4

class AttendanceCountRule(IntEnum):
    Accumulation = 0
    Date = 1

class AttendanceResetType(IntEnum):
    User = 0
    Server = 1

class DreamMakerMultiplierCondition(IntEnum):
    none = 0
    Round = 1
    CollectionCount = 2
    EndingCount = 3

class DreamMakerParameterType(IntEnum):
    none = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4

class DreamMakerResult(IntEnum):
    none = 0
    Fail = 1
    Success = 2
    Perfect = 3

class DreamMakerParamOperationType(IntEnum):
    none = 0
    GrowUpHigh = 1
    GrowUp = 2
    GrowDownHigh = 3
    GrowDown = 4

class DreamMakerEndingCondition(IntEnum):
    none = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4
    Round = 5
    CollectionCount = 6

class DreamMakerVoiceCondition(IntEnum):
    none = 0
    Fail = 1
    Success = 2
    Perfect = 3
    DailyResult = 4

class DreamMakerEndingType(IntEnum):
    none = 0
    Normal = 1
    Special = 2

class DreamMakerEndingRewardType(IntEnum):
    none = 0
    FirstEndingReward = 1
    LoopEndingReward = 2

class Geas(IntEnum):
    ForwardProjectile = 0
    DiagonalProjectile = 1
    SideProjectile = 2
    Pierce = 3
    Reflect = 4
    Burn = 5
    Chill = 6
    AttackPower = 7
    AttackSpeed = 8
    Critical = 9
    Heal = 10
    MoveSpeed = 11
    LifeSteal = 12
    Evasion = 13

class TBGObjectType(IntEnum):
    none = 0
    EnemyBoss = 1
    EnemyMinion = 2
    Random = 3
    Facility = 4
    TreasureBox = 5
    Start = 6
    Portal = 7

class TBGOptionSuccessType(IntEnum):
    none = 0
    TBGItemAcquire = 1
    ItemAcquire = 2
    TBGDiceAcquire = 3
    Portal = 4

class TBGItemType(IntEnum):
    none = 0
    Dice = 1
    Heal = 2
    HealExpansion = 3
    Defence = 4
    Guide = 5
    DiceResultValue = 6
    DefenceCritical = 7
    DiceResultConfirm = 8

class TBGItemEffectType(IntEnum):
    none = 0
    PermanentContinuity = 1
    TemporaryContinuation = 2
    Immediately = 3

class TBGTileType(IntEnum):
    none = 0
    Start = 1
    Movable = 2
    UnMovable = 3

class TBGThemaType(IntEnum):
    none = 0
    Normal = 1
    Hidden = 2

class TBGPortalCondition(IntEnum):
    none = 0
    ObjectAllEncounter = 1
    Round = 2

class TBGProbModifyCondition(IntEnum):
    none = 0
    AllyRevive = 1
    DicePlayFail = 2

class TBGVoiceCondition(IntEnum):
    none = 0
    DiceResultSuccess = 1
    DiceResultFailBattle = 2
    DiceResultFailRandom = 3
    EnemyDie = 4
    TreasureBoxNormal = 5
    TreasureBoxSpecial = 6
    FacilityResult = 7

class MiniGameTBGThemaRewardType(IntEnum):
    TreasureReward = 0
    EmptyTreasureReward = 1
    HiddenThemaTreasureReward = 2

class MissionCategory(IntEnum):
    Challenge = 0
    Daily = 1
    Weekly = 2
    Achievement = 3
    GuideMission = 4
    All = 5
    MiniGameScore = 6
    MiniGameEvent = 7
    EventAchievement = 8
    DailySudden = 9
    DailyFixed = 10
    EventFixed = 11

class MissionResetType(IntEnum):
    none = 0
    Daily = 1
    Weekly = 2
    Limit = 3

class MissionCompleteConditionType(IntEnum):
    none = 0
    Reset_DailyLogin = 1
    Reset_DailyLoginCount = 2
    Reset_CompleteMission = 3
    Achieve_EquipmentLevelUpCount = 4
    Achieve_EquipmentTierUpCount = 5
    Achieve_CharacterLevelUpCount = 6
    Reset_CharacterTranscendenceCount = 7
    Reset_ClearTaticBattleCount = 8
    Achieve_ClearCampaignStageCount = 9
    Reset_KillSpecificEnemyCount = 10
    Reset_KillEnemyWithTagCount = 11
    Reset_GetCharacterCount = 12
    Reset_GetCharacterWithTagCount = 13
    Reset_GetSpecificCharacterCount = 14
    Reset_AccountLevelUp = 15
    Reset_GetEquipmentCount = 16
    Reset_GachaCount = 17
    Reset_UseGem = 18
    Reset_GetGem = 19
    Reset_GetGemPaid = 20
    Achieve_GetGold = 21
    Achieve_GetItem = 22
    Reset_GetFavorLevel = 23
    Reset___Deprecated_EquipmentAtSpecificLevelCount = 24
    Reset_EquipmentAtSpecificTierUpCount = 25
    Reset_CharacterAtSpecificLevelCount = 26
    Reset_CharacterAtSpecificTranscendenceCount = 27
    Achieve_CharacterSkillLevelUpCount = 28
    Reset_CharacterAtSpecificSkillLevelCount = 29
    Reset_CompleteScheduleCount = 30
    Reset_CompleteScheduleGroupCount = 31
    Reset_AcademyLocationRankSum = 32
    Reset_CraftCount = 33
    Achieve_GetComfortPoint = 34
    Achieve_GetWeaponCount = 35
    Reset_EquipWeaponCount_Obsolete = 36
    Reset_CompleteScheduleWithSpecificCharacter = 37
    Reset_CafeInteractionCount = 38
    Reset_SpecificCharacterAtSpecificLevel = 39
    Reset_SpecificCharacterAtSpecificTranscendence = 40
    Reset_LobbyInteraction = 41
    Achieve_ClearFindGiftAndBloodDungeonCount = 42
    Reset_ClearSpecificFindGiftAndBloodDungeonCount = 43
    Achieve_JoinRaidCount = 44
    Reset_JoinSpecificRaidCount = 45
    Achieve_JoinArenaCount = 46
    Reset_ArenaVictoryCount = 47
    Reset_RaidDamageAmountOnOneBattle = 48
    Reset_ClearEventStageCount = 49
    Reset_UseSpecificCharacterCount = 50
    Achieve_UseGold = 51
    Reset_UseTiket = 52
    Reset_ShopBuyCount = 53
    Reset_ShopBuyActionPointCount = 54
    Reset_SpecificCharacterAtSpecificFavorRank = 55
    Reset_ClearSpecificScenario = 56
    Reset_GetSpecificItemCount = 57
    Achieve_TotalGetClearStarCount = 58
    Reset_CompleteCampaignStageMinimumTurn = 59
    Achieve_TotalLoginCount = 60
    Reset_LoginAtSpecificTime = 61
    Reset_CompleteFavorSchedule = 62
    Reset_CompleteFavorScheduleAtSpecificCharacter = 63
    Reset_GetMemoryLobbyCount = 64
    Reset_GetFurnitureGroupCount = 65
    Reset_AcademyLocationAtSpecificRank = 66
    Reset_ClearCampaignStageDifficultyNormal = 67
    Reset_ClearCampaignStageDifficultyHard = 68
    Achieve_ClearChaserDungeonCount = 69
    Reset_ClearSpecificChaserDungeonCount = 70
    Reset_GetCafeRank = 71
    Reset_SpecificStarCharacterCount = 72
    Reset_EventClearCampaignStageCount = 73
    Reset_EventClearSpecificCampaignStageCount = 74
    Reset_EventCompleteCampaignStageMinimumTurn = 75
    Reset_EventClearCampaignStageDifficultyNormal = 76
    Reset_EventClearCampaignStageDifficultyHard = 77
    Reset_ClearSpecificCampaignStageCount = 78
    Reset_GetItemWithTagCount = 79
    Reset_GetFurnitureWithTagCount = 80
    Reset_GetEquipmentWithTagCount = 81
    Reset_ClearCampaignStageTimeLimitFromSecond = 82
    Reset_ClearEventStageTimeLimitFromSecond = 83
    Reset_ClearRaidTimeLimitFromSecond = 84
    Reset_ClearBattleWithTagCount = 85
    Reset_ClearFindGiftAndBloodDungeonTimeLimitFromSecond = 86
    Reset_CompleteScheduleWithTagCount = 87
    Reset_ClearChaserDungeonTimeLimitFromSecond = 88
    Reset_GetTotalScoreRhythm = 89
    Reset_GetBestScoreRhythm = 90
    Reset_GetSpecificScoreRhythm = 91
    Reset_ClearStageRhythm = 92
    Reset_GetComboCountRhythm = 93
    Reset_GetFullComboRhythm = 94
    Reset_GetFeverCountRhythm = 95
    Reset_UseActionPoint = 96
    Achieve_ClearSchoolDungeonCount = 97
    Reset_ClearSchoolDungeonTimeLimitFromSecond = 98
    Reset_ClearSpecificSchoolDungeonCount = 99
    Reset_GetCriticalCountRhythm = 100
    Achieve_WeaponTranscendenceCount = 101
    Achieve_WeaponLevelUpCount = 102
    Reset_WeaponAtSpecificTranscendenceCount = 103
    Reset_WeaponAtSpecificLevelUpCount = 104
    Reset_BuyShopGoods = 105
    Reset_ClanLogin = 106
    Reset_AssistCharacterSetting = 107
    Reset_DailyMissionFulfill = 108
    Reset_SelectedMissionFulfill = 109
    Reset_TotalDamageToWorldRaid = 110
    Reset_JoinWorldRaidTypeNumber = 111
    Reset_JoinWorldRaidBattleWithTagCount = 112
    Reset_ClearWorldRaidTimeLimitFromSecond = 113
    Achieve_KillEnemyWithDecagrammatonSPOTagCount = 114
    Reset_ConquerTileCount = 115
    Reset_ConquerSpecificStepTileCount = 116
    Reset_ConquerSpecificStepTileAll = 117
    Reset_UpgradeConquestBaseTileCount = 118
    Reset_KillConquestBoss = 119
    Reset_ClearEventConquestTileTimeLimitFromSecond = 120
    Reset_DiceRaceUseDiceCount = 121
    Reset_DiceRaceFinishLapCount = 122
    Reset_FortuneGachaCount = 123
    Reset_FortuneGachaCountByGrade = 124
    Reset_ClearCountShooting = 125
    Reset_ClearSpecificStageShooting = 126
    Reset_ClearSpecificCharacterShooting = 127
    Reset_ClearSpecificSectionShooting = 128
    Achieve_JoinEliminateRaidCount = 129
    Reset_TBGCompleteRoundCount = 130
    Reset_CompleteStage = 131
    Reset_TBGClearSpecificThema = 132
    Reset_ClearGeneralChaserDungeonCount = 133
    Reset_ClearGeneralFindGiftAndBloodDungeonCount = 134
    Reset_ClearGeneralSchoolDungeonCount = 135
    Reset_JoinArenaCount = 136
    Reset_GetCafe2ndRank = 137
    Achieve_GetComfort2ndPoint = 138
    Reset_ClearSpecificTimeAttackDungeonCount = 139
    Reset_GetScoreTimeAttackDungeon = 140
    Reset_GetTotalScoreTimeAttackDungeon = 141
    Reset_JoinRaidCount = 142
    Reset_ClearTimeAttackDungeonCount = 143
    Reset_JoinEliminateRaidCount = 144
    Reset_FieldClearSpecificDate = 145
    Reset_FieldGetEvidenceCount = 146
    Reset_FieldMasteryLevel = 147
    Reset_TreasureCheckedCellCount = 148
    Reset_TreasureGetTreasureCount = 149
    Reset_TreasureRoundRefreshCount = 150
    Achieve_UseTicketCount = 151
    Reset_ClearMultiFloorRaidStage = 152
    Achieve_CharacterPotentialUpCount = 153
    Reset_CharacterPotentialUpCount = 154
    Reset_CharacterAtSpecificPotentialCount = 155
    Reset_PotentialAttackPowerAtSpecificLevel = 156
    Reset_PotentialMaxHPAtSpecificLevel = 157
    Reset_PotentialHealPowerAtSpecificLevel = 158
    Reset_DreamGetSpecificParameter = 159
    Reset_DreamGetSpecificScheduleCount = 160
    Reset_DreamGetScheduleCount = 161
    Reset_DreamGetEndingCount = 162
    Reset_DreamGetSpecificEndingCount = 163
    Reset_DreamGetCollectionScenarioCount = 164
    Reset_ClearCountDefense = 165
    Reset_ClearSpecificDefenseStage = 166
    Reset_ClearCharacterLimitDefense = 167
    Reset_ClearTimeLimitDefenseFromSecond = 168

class AccountAchievementType(IntEnum):
    TotalLoginCount = 0
    TotalGetClearStarCount = 1
    TotalCharacterLevelUpCount = 2
    TotalCharacterSkillLevelUpCount = 3
    TotalClearCampaignStageCount = 4
    TotalClearChaserDungeonCount = 5
    TotalClearFindGiftAndBloodDungeonCount = 6
    TotalEquipmentLevelUpCount = 7
    TotalEquipmentTierUpCount = 8
    MaxComfortPoint = 9
    TotalGetGold = 10
    TotalUseGold = 11
    TotalJoinArenaCount = 12
    TotalJoinRaidCount = 13
    TotalClearSchoolDungeonCount = 14
    TotalGetWeaponCount = 15
    TotalWeaponLevelUpCount = 16
    TotalWeaponTranscendenceCount = 17
    KillEnemyWithDecagrammatonSPOTagCount = 18
    EventPoint = 19
    ConquestCalculateReward = 20
    TotalJoinEliminateRaidCount = 21
    Cafe2MaxComfortPoint = 22
    TotalRaidTicketUseCount = 23
    TotalEliminateTicketUseCount = 24
    TotalCharacterPotentialUpCount = 25

class MissionToastDisplayConditionType(IntEnum):
    Always = 0
    Complete = 1
    Never = 2

class GetStickerConditionType(IntEnum):
    none = 0
    Reset_StikcerGetCondition_AccountLevel = 1
    Reset_StickerGetCondition_ScenarioModeId = 2
    Reset_StickerGetCondition_EnemyKillCount = 3
    Reset_StickerGetCondition_GetItemCount = 4
    Reset_StickerGetCondition_BuyItemCount = 5
    Reset_StickerGetCondition_ScheduleRank = 6
    Reset_StickerGetCondition_Change_LobbyCharacter = 7
    Reset_StickerGetCondition_Cafe_Character_Visit_Count = 8
    Reset_StickerGetCondition_Cafe_Chracter_Invite_Count = 9
    Reset_StickerGetCondition_GetChracterCount = 10
    Reset_StickerGetCondition_Cafe_Furniture_Interaction = 11
    Reset_StickerGetCondition_GetFurniture = 12
    Reset_StickerGetCondition_SetFurniture = 13
    Reset_StickerGetCondition_GivePresentChracterCount = 14
    Reset_StickerGetCondition_GivePresentCount = 15
    Reset_StickerGetCondition_MomotalkStudentCount = 16
    Reset_StickerGetCondition_CombatwithCharacterCount = 17
    Reset_StickerGetCondition_GachaCharacterCount = 18
    Reset_StickerGetCondition_TouchLobbyCharacter = 19
    Reset_StickerGetCondition_UseCircleEmoticonCount = 20
    Reset_StickerGetCondition_CraftCount = 21
    Reset_StickerGetCondition_NormalStageClear = 22
    Reset_StickerGetCondition_NormalStageClear3Star = 23
    Reset_StickerGetCondition_HardStageClear = 24
    Reset_StickerGetCondition_HardStageClear3Star = 25
    Achieve_StikcerGetCondition_AccountLevel = 26
    Achieve_StickerGetCondition_ClearStageId = 27
    Achieve_StickerGetCondition_ScenarioModeId = 28
    Achieve_StickerGetCondition_EnemyKillCount = 29
    Achieve_StickerGetCondition_GetItemCount = 30
    Achieve_StickerGetCondition_BuyItemCount = 31
    Achieve_StickerGetCondition_ScheduleRank = 32
    Achieve_StickerGetCondition_Change_LobbyCharacter = 33
    Achieve_StickerGetCondition_Cafe_Character_Visit_Count = 34
    Achieve_StickerGetCondition_Cafe_Chracter_Invite_Count = 35
    Achieve_StickerGetCondition_GetChracterCount = 36
    Achieve_StickerGetCondition_Cafe_Furniture_Interaction = 37
    Achieve_StickerGetCondition_GetFurniture = 38
    Achieve_StickerGetCondition_SetFurniture = 39
    Achieve_StickerGetCondition_GivePresentChracterCount = 40
    Achieve_StickerGetCondition_GivePresentCount = 41
    Achieve_StickerGetCondition_MomotalkStudentCount = 42
    Achieve_StickerGetCondition_CombatwithCharacterCount = 43
    Achieve_StickerGetCondition_GachaCharacterCount = 44
    Achieve_StickerGetCondition_TouchLobbyCharacter = 45
    Achieve_StickerGetCondition_UseCircleEmoticonCount = 46
    Achieve_StickerGetCondition_CraftCount = 47
    Achieve_StickerGetCondition_NormalStageClear = 48
    Achieve_StickerGetCondition_NormalStageClear3Star = 49
    Achieve_StickerGetCondition_HardStageClear = 50
    Achieve_StickerGetCondition_HardStageClear3Star = 51
    Reset_StickerGetCondition_EnemyKillCountbyTag = 52
    Reset_StickerGetCondition_GetItemCountbyTag = 53
    Reset_StickerGetCondition_ClearCampaignOrEventStageCount = 54
    Reset_StickerGetCondition_CompleteCampaignStageMinimumTurn = 55
    Reset_StickerGetCondition_ClearCampaignStageDifficultyNormal = 56
    Reset_StickerGetCondition_ClearCampaignStageDifficultyHard = 57
    Reset_StickerGetCondition_EventClearCampaignStageCount = 58
    Reset_StickerGetCondition_EventClearSpecificCampaignStageCount = 59
    Reset_StickerGetCondition_EventCompleteCampaignStageMinimumTurn = 60
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyNormal = 61
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyHard = 62
    Reset_StickerGetCondition_ClearSpecificCampaignStageCount = 63
    Reset_StickerGetCondition_ClearCampaignStageTimeLimitFromSecond = 64
    Reset_StickerGetCondition_ClearEventStageTimeLimitFromSecond = 65
    Reset_StickerGetCondition_ClearStageRhythm = 66
    Reset_StickerGetCondition_ClearSpecificStageShooting = 67
    Reset_StickerGetCondition_CompleteStage = 68
    Achieve_StickerGetCondition_ClearCampaignStageCount = 69
    Achieve_StickerGetCondition_ClearChaserDungeonCount = 70
    Reset_StickerGetCondition_ClearSpecificChaserDungeonCount = 71
    Achieve_StickerGetCondition_ClearSchoolDungeonCount = 72
    Reset_StickerGetCondition_ClearSpecificSchoolDungeonCount = 73
    Reset_StickerGetCondition_ClearSpecificWeekDungeonCount = 74
    Achieve_StickerGetCondition_ClearFindGiftAndBloodDungeonCount = 75

class StickerCheckPassType(IntEnum):
    none = 0
    ClearScenarioModeId = 1
    ClearCampaignStageId = 2

class ParcelType(IntEnum):
    none = 0
    Character = 1
    Currency = 2
    Equipment = 3
    Item = 4
    GachaGroup = 5
    Product = 6
    Shop = 7
    MemoryLobby = 8
    AccountExp = 9
    CharacterExp = 10
    FavorExp = 11
    TSS = 12
    Furniture = 13
    ShopRefresh = 14
    LocationExp = 15
    Recipe = 16
    CharacterWeapon = 17
    CharacterGear = 18
    IdCardBackground = 19
    Emblem = 20
    Sticker = 21
    Costume = 22

class Rarity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3

class Tier(IntEnum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3

class CurrencyTypes(IntEnum):
    Invalid = 0
    Gold = 1
    GemPaid = 2
    GemBonus = 3
    Gem = 4
    ActionPoint = 5
    AcademyTicket = 6
    ArenaTicket = 7
    RaidTicket = 8
    WeekDungeonChaserATicket = 9
    WeekDungeonFindGiftTicket = 10
    WeekDungeonBloodTicket = 11
    WeekDungeonChaserBTicket = 12
    WeekDungeonChaserCTicket = 13
    SchoolDungeonATicket = 14
    SchoolDungeonBTicket = 15
    SchoolDungeonCTicket = 16
    TimeAttackDungeonTicket = 17
    MasterCoin = 18
    WorldRaidTicketA = 19
    WorldRaidTicketB = 20
    WorldRaidTicketC = 21
    ChaserTotalTicket = 22
    SchoolDungeonTotalTicket = 23
    EliminateTicketA = 24
    EliminateTicketB = 25
    EliminateTicketC = 26
    EliminateTicketD = 27
    Max = 28

class SortingTarget(IntEnum):
    none = 0
    Rarity = 1
    Level = 2
    StarGrade = 3
    Tier = 4

class CurrencyOverChargeType(IntEnum):
    CanNotCharge = 0
    FitToLimit = 1
    ChargeOverLimit = 2

class CurrencyAdditionalChargeType(IntEnum):
    EnableAutoChargeOverLimit = 0
    DisableAutoChargeOverLimit = 1

class RecipeType(IntEnum):
    none = 0
    Craft = 1
    SkillLevelUp = 2
    CharacterTranscendence = 3
    EquipmentTierUp = 4
    CafeRankUp = 5
    SelectionItem = 6
    WeaponTranscendence = 7
    SelectRecruit = 8
    CharacterPotential = 9

class GachaGroupType(IntEnum):
    none = 0
    Reward_General = 1
    System_Craft = 2
    Reward_Pack = 3

class ParcelChangeReason(IntEnum):
    none = 0
    Acquire_NewAccount = 1
    Acquire_PlayReward = 2
    Acquire_ChapterReward = 3
    Acquire_LoginReward = 4
    Acquire_EventReward = 5
    Acquire_GMPush = 6
    Acquire_ShopBuy = 7
    Acquire_GachaBuy = 8
    Acquire_CurrencyBuy = 9
    Equipment_Equip = 10
    Equipment_Unequip = 11
    Equipment_Levelup = 12
    Equipment_LimitBreak = 13
    Equipment_Transcendence = 14
    Equipment_Enchant = 15
    Item_Use = 16
    Item_Lock = 17
    Item_CharacterGrowthMaterial = 18
    Item_Change = 19
    Item_Delete = 20
    Item_Consume = 21
    Item_SelectTicket = 22
    Character_ExpGrowth = 23
    Character_Transcendence = 24
    Character_SkillLevelUp = 25
    Character_FavorGrowth = 26
    Furniture_CafeSet = 27
    Furniture_CafeRecall = 28
    Academy_AttendSchedule = 29
    Academy_MessageList = 30
    Adventure_EnterMainStage = 31
    Adventure_EnterSubStage = 32
    Adventure_MainStageBattleResult = 33
    Adventure_SubStageBattleResult = 34
    Adventure_ChapterClearReward = 35
    Adventure_Retreat = 36
    Adventure_PurchasePlayCountHardStage = 37
    Adventure_TutorialStage = 38
    Adventure_TutorialStageBattleResult = 39
    ContentSweep_Sweep = 40
    Arena_TimeReward = 41
    Arena_DailyReward = 42
    Arena_EnterBattle = 43
    Arena_BattleResult = 44
    Cafe_Interact = 45
    Cafe_Production = 46
    Cafe_RankUp = 47
    Cafe_GiveGift = 48
    WeekDungeon_BattleResult = 49
    WeekDungeon_EnterBattle = 50
    WeekDungeon_Retreat = 51
    Mission_Clear = 52
    Shop_Refresh = 53
    Shop_BuyEligma = 54
    Shop_BuyMerchandise = 55
    Shop_BuyGacha = 56
    Scenario_Clear = 57
    Recipe_Craft = 58
    Raid_Failed = 59
    Raid_Reward = 60
    Raid_SeasonReward = 61
    Raid_CreateBattle = 62
    CumulativeTimeReward_Reward = 63
    Mail_Receive = 64
    MomoTalk_FavorSchedule = 65
    WeekDungeon_EnterBlood = 66
    WeekDungeon_EnterGift = 67
    Acquire_ActionPoint = 68
    Acquire_ArenaTicket = 69
    EventContent_TotalReward = 70
    Craft_UpdateNode = 71
    Craft_CompleteProcess = 72
    Craft_Reward = 73
    EventContent_BattleResult = 74
    Adventure_Sweep = 75
    EventContent_Sweep = 76
    WeekDungeon_Sweep = 77
    Acquire_MonthlyProduct = 78
    Acquire_DailyReward = 79
    Billing_PurchaseProduct = 80
    EventContent_EnterMainStage = 81
    EventContent_EnterSubStage = 82
    EventContent_MainStageResult = 83
    EventContent_SubStageResult = 84
    EventContent_Retreat = 85
    WeekDungeon_BloodResult = 86
    WeekDungeon_GiftResult = 87
    WeekDungeon_EnterChaserA = 88
    WeekDungeon_EnterChaserB = 89
    WeekDungeon_EnterChaserC = 90
    WeekDungeon_ChaserAResult = 91
    WeekDungeon_ChaserBResult = 92
    WeekDungeon_ChaserCResult = 93
    EventContent_BoxGacha = 94
    Raid_Sweep = 95
    Clan_AssistReward = 96
    EventContent_CardShop = 97
    CharacterWeapon_ExpGrowth = 98
    CharacterWeapon_Transcendence = 99
    MiniGameMission_Clear = 100
    SchoolDungeon_EnterSchoolA = 101
    SchoolDungeon_EnterSchoolB = 102
    SchoolDungeon_EnterSchoolC = 103
    SchoolDungeon_SchoolAResult = 104
    SchoolDungeon_SchoolBResult = 105
    SchoolDungeon_SchoolCResult = 106
    TimeAttackDungeon_CreateBattle = 107
    TimeAttackDungeon_EndBattle = 108
    TimeAttackDungeon_Reward = 109
    Clan_Create = 110
    Arena_SeasonReward = 111
    Arena_OverallReward = 112
    EventContent_AttendSchedule = 113
    EventContent_BuyFortuneGacha = 114
    Equipment_BatchGrowth = 115
    EventContent_EnterStoryStage = 116
    EventContent_StoryStageResult = 117
    WorldRaid_EndBattle = 118
    WorldRaid_Reward = 119
    Conquest_EnterBattle = 120
    Conquest_EnterUnExpectBattle = 121
    Conquest_BattleResult = 122
    Conquest_UnExpectBattleResult = 123
    Conquest_UpgradeBase = 124
    Conquest_ManageBase = 125
    Conquest_CalculatedReward = 126
    Conquest_TakeEventBoxObject = 127
    Conquest_ConquerNormalTile = 128
    Item_SelectRecruit = 129
    Adventure_EnterExtraStage = 130
    Adventure_ExtraStageBattleResult = 131
    Scenario_EnterMainStage = 132
    Scenario_MainStageResult = 133
    Scenario_RetreatMainStage = 134
    EventContent_DiceRaceRollReward = 135
    EventContent_DiceRaceLapReward = 136
    ShiftingCraft_BeginProcess = 137
    ShiftingCraft_CompleteProcess = 138
    ShiftingCraft_Reward = 139
    MiniGame_ShootingBattleResult = 140
    MiniGame_ShootingSweep = 141
    EliminateRaid_Failed = 142
    EliminateRaid_Reward = 143
    EliminateRaid_SeasonReward = 144
    EliminateRaid_CreateBattle = 145
    EliminateRaid_Sweep = 146
    Item_AutoSynth = 147
    ContentSweep_MultiSweep = 148
    Emblem_Acquire = 149
    MiniGame_TBGMove = 150
    MiniGame_TBGEncounterInput = 151
    MiniGame_TBGResurrect = 152
    MiniGame_TBGSweep = 153
    Shop_BeforehandGacha = 154
    EliminateRaid_LimitedReward = 155
    Craft_AutoBeginProcess = 156
    Craft_CompleteProcessAll = 157
    Craft_RewardAll = 158
    ShiftingCraft_CompleteProcessAll = 159
    ShiftingCraft_RewardAll = 160
    Temp_1 = 161
    Temp_2 = 162
    Temp_3 = 163
    Temp_4 = 164
    EventContent_Treasure = 165
    Field_EnterStage = 166
    Field_StageResult = 167
    Field_Interaction = 168
    Field_Quest = 169
    Character_PotentialGrowth = 170
    MultiFloorRaid_EndBattle = 171
    MultiFloorRaid_Reward = 172
    MiniGame_DreamSchedule = 173
    MiniGame_DreamDailyClosing = 174
    MiniGame_DreamEnding = 175
    Item_ExpireChange = 176
    MiniGame_DefenseBattleResult = 177
    Raid_FailCompensateReward = 178
    EliminateRaid_FailCompensateReward = 179
    Currency_ExpireChange = 180

class ConsumeCondition(IntEnum):
    And = 0
    Or = 1

class DailyRefillType(IntEnum):
    none = 0
    Default = 1
    Login = 2

class ScenarioBGType(IntEnum):
    none = 0
    Image = 1
    BlurRT = 2
    Spine = 3
    Hide = 4

class ScenarioType(IntEnum):
    none = 0
    Title = 1
    Place = 2

class ScenarioTypes(IntEnum):
    none = 0
    Title = 1
    Place = 2

class ScenarioCharacterAction(IntEnum):
    Idle = 0
    Shake = 1
    Greeting = 2
    FalldownLeft = 3
    FalldownRight = 4
    Stiff = 5
    Hophop = 6
    Jump = 7

class ScenarioCharacterBehaviors(IntEnum):
    none = 0
    Appear = 1
    Disappear = 2
    AppearToLeft = 3
    ApperToRight = 4
    DisappearToLeft = 5
    DisappearToRight = 6
    MoveToTarget = 7

class ScenarioCharacterShapes(IntEnum):
    none = 0
    Signal = 1
    BlackSilhouette = 2
    Closeup = 4
    Highlight = 8
    WhiteSilhouette = 16

class ScenarioBGScroll(IntEnum):
    none = 0
    Vertical = 1
    Horizontal = 2

class DialogCategory(IntEnum):
    Cafe = 0
    Echelon = 1
    CharacterSSRNew = 2
    CharacterGet = 3
    Birthday = 4
    Dating = 5
    Title = 6
    UILobby = 7
    UILobbySpecial = 8
    UIShop = 9
    UIGacha = 10
    UIRaidLobby = 11
    UIWork = 12
    UITitle = 13
    UIWeekDungeon = 14
    UIAcademyLobby = 15
    UIRaidLobbySeasonOff = 16
    UIRaidLobbySeasonOn = 17
    UIWorkAronaSit = 18
    UIWorkAronaSleep = 19
    UIWorkAronaWatch = 20
    UIGuideMission = 21
    UILobby2 = 22
    UIClanSearchList = 23
    UIAttendance = 24
    UIAttendanceEvent01 = 25
    UIEventLobby = 26
    UIEventShop = 27
    UIEventBoxGachaShop = 28
    UIAttendanceEvent02 = 29
    UIAttendanceEvent03 = 30
    UIEventCardShop = 31
    UISchoolDungeon = 32
    UIAttendanceEvent = 33
    UISpecialOperationLobby = 34
    WeaponGet = 35
    UIAttendanceEvent04 = 36
    UIEventFortuneGachaShop = 37
    UIAttendanceEvent05 = 38
    UIAttendanceEvent06 = 39
    UIMission = 40
    UIEventMission = 41
    UIAttendanceEvent08 = 42
    UIAttendanceEvent07 = 43
    UIEventMiniGameMission = 44
    UIAttendanceEvent09 = 45
    UIAttendanceEvent10 = 46
    UIAttendanceEvent11 = 47
    UIWorkPlanaSit = 48
    UIWorkPlanaUmbrella = 49
    UIWorkPlanaCabinet = 50
    UIWorkCoexist_AronaSleepSit = 51
    UIWorkCoexist_PlanaWatchSky = 52
    UIWorkCoexist_PlanaSitPeek = 53
    UIWorkCoexist_AronaSleepPeek = 54
    UIEventArchive = 55
    UIAttendanceEvent12 = 56
    UIAttendanceEvent13 = 57
    UIAttendanceEvent14 = 58
    Temp_1 = 59
    Temp_2 = 60
    Temp_3 = 61
    Temp_4 = 62
    Temp_5 = 63
    UIAttendanceEvent15 = 64
    UILobbySpecial2 = 65
    UIAttendanceEvent16 = 66
    UIEventTreasure = 67
    UIMultiFloorRaid = 68
    UIEventMiniGameDreamMaker = 69
    UIAttendanceEvent17 = 70

class DialogCondition(IntEnum):
    Idle = 0
    Enter = 1
    Exit = 2
    Buy = 3
    SoldOut = 4
    BoxGachaNormal = 5
    BoxGachaPrize = 6
    Prize0 = 7
    Prize1 = 8
    Prize2 = 9
    Prize3 = 10
    Interaction = 11
    Luck0 = 12
    Luck1 = 13
    Luck2 = 14
    Luck3 = 15
    Luck4 = 16
    Luck5 = 17
    StoryOpen = 18
    CollectionOpen = 19
    BoxGachaFinish = 20
    FindTreasure = 21
    GetTreasure = 22
    RoundRenewal = 23
    MiniGameDreamMakerEnough01 = 24
    MiniGameDreamMakerEnough02 = 25
    MiniGameDreamMakerEnough03 = 26
    MiniGameDreamMakerEnough04 = 27
    MiniGameDreamMakerDefault = 28

class DialogConditionDetail(IntEnum):
    none = 0
    Day = 1
    Close = 2
    MiniGameDreamMakerDay = 3

class DialogType(IntEnum):
    Talk = 0
    Think = 1
    UITalk = 2

class Anniversary(IntEnum):
    none = 0
    UserBDay = 1
    StudentBDay = 2

class School(IntEnum):
    none = 0
    Hyakkiyako = 1
    RedWinter = 2
    Trinity = 3
    Gehenna = 4
    Abydos = 5
    Millennium = 6
    Arius = 7
    Shanhaijing = 8
    Valkyrie = 9
    WildHunt = 10
    SRT = 11
    SCHALE = 12
    ETC = 13
    Tokiwadai = 14
    Sakugawa = 15

class EtcSchool(IntEnum):
    none = 0
    ETC = 1
    Tokiwadai = 2
    Sakugawa = 3
    Max = 4

class StoryCondition(IntEnum):
    Open = 0
    Locked = 1
    ComingSoon = 2
    Hide = 3

class EmojiEvent(IntEnum):
    EnterConver = 0
    EnterShelter = 1
    SignalLeader = 2
    Nice = 3
    Reload = 4
    Blind = 5
    Panic = 6
    Silence = 7
    NearyDead = 8
    Run = 9
    TerrainAdaptionS = 10
    TerrainAdaptionA = 11
    TerrainAdaptionB = 12
    TerrainAdaptionC = 13
    TerrainAdaptionD = 14
    TerrainAdaptionSS = 15
    Dot = 16
    Angry = 17
    Bulb = 18
    Exclaim = 19
    Surprise = 20
    Sad = 21
    Sigh = 22
    Steam = 23
    Upset = 24
    Respond = 25
    Question = 26
    Sweat = 27
    Music = 28
    Chat = 29
    Twinkle = 30
    Zzz = 31
    Tear = 32
    Heart = 33
    Shy = 34
    Think = 35

class ScenarioModeTypes(IntEnum):
    none = 0
    Main = 1
    Sub = 2
    Replay = 3
    Mini = 4
    SpecialOperation = 5
    Prologue = 6

class ScenarioModeSubTypes(IntEnum):
    none = 0
    Club = 1

class ScenarioModeReplayTypes(IntEnum):
    none = 0
    Event = 1
    Favor = 2
    Work = 3
    EventMeetup = 4

class ScenarioEffectDepth(IntEnum):
    none = 0
    AboveBg = 1
    AboveCharacter = 2
    AboveAll = 3

class ScenarioZoomAnchors(IntEnum):
    Center = 0
    LeftTop = 1
    LeftBottom = 2
    RightTop = 3
    RightBottom = 4

class ScenarioZoomType(IntEnum):
    Instant = 0
    Slide = 1

class ScenarioContentType(IntEnum):
    Prologue = 0
    WeekDungeon = 1
    Raid = 2
    Arena = 3
    Favor = 4
    Shop = 5
    EventContent = 6
    Craft = 7
    Chaser = 8
    EventContentMeetup = 9
    TimeAttack = 10
    Mission = 11
    EventContentPermanentPrologue = 12
    EventContentReturnSeason = 13
    MiniEvent = 14
    EliminateRaid = 15
    MultiFloorRaid = 16
    EventContentPermanent = 17

class MemoryLobbyCategory(IntEnum):
    none = 0
    UILobbySpecial = 1
    UILobbySpecial2 = 2

class PurchaseCountResetType(IntEnum):
    none = 0
    Day = 1
    Week = 2
    Month = 3

class ShopCategoryType(IntEnum):
    General = 0
    SecretStone = 1
    Raid = 2
    Gold = 3
    Ap = 4
    PickupGacha = 5
    NormalGacha = 6
    PointGacha = 7
    EventGacha = 8
    ArenaTicket = 9
    Arena = 10
    TutoGacha = 11
    RecruitSellection = 12
    EventContent_0 = 13
    EventContent_1 = 14
    EventContent_2 = 15
    EventContent_3 = 16
    EventContent_4 = 17
    _Obsolete = 18
    LimitedGacha = 19
    MasterCoin = 20
    SecretStoneGrowth = 21
    TicketGacha = 22
    DirectPayGacha = 23
    FesGacha = 24
    TimeAttack = 25
    Chaser = 26
    ChaserTicket = 27
    SchoolDungeonTicket = 28
    AcademyTicket = 29
    Special = 30
    Care = 31
    BeforehandGacha = 32
    EliminateRaid = 33
    GlobalSpecialGacha = 34

class PurchaseServerTag(IntEnum):
    Audit = 0
    PreAudit = 1
    Production = 2
    Hotfix = 3
    Standby2 = 4
    Standby1 = 5
    Major = 6
    Minor = 7
    Temp = 8
    Test = 9
    TestIn = 10

class PurchaseStatusCode(IntEnum):
    none = 0
    Start = 1
    PublishSuccess = 2
    End = 3
    Error = 4
    DuplicateOrder = 5
    Refund = 6

class StoreType(IntEnum):
    none = 0
    GooglePlay = 1
    AppStore = 2
    OneStore = 3
    MicrosoftStore = 4
    GalaxyStore = 5

class PurchasePeriodType(IntEnum):
    none = 0
    Day = 1
    Week = 2
    Month = 3

class PurchaseSourceType(IntEnum):
    none = 0
    Product = 1
    ProductMonthly = 2

class ProductCategory(IntEnum):
    none = 0
    Gem = 1
    Monthly = 2
    Package = 3
    GachaDirect = 4
    TimeLimit = 5

class ProductDisplayTag(IntEnum):
    none = 0
    New = 1
    Hot = 2
    Sale = 3

class ProductTagType(IntEnum):
    Monthly = 0
    Weekly = 1
    Biweekly = 2

class BillingTransactionEndType(IntEnum):
    none = 0
    Success = 1
    Cancel = 2

class GachaRewardType(IntEnum):
    none = 0
    Eligma = 1
    Eleph = 2

class ShopFreeRecruitType(IntEnum):
    none = 0
    Accumulation = 1
    Reset = 2

class GachaDisplayTag(IntEnum):
    none = 0
    Limited = 1
    TwoStar = 2
    ThreeStar = 3
    Free = 4
    New = 5
    Fes = 6
    SelectRecruit = 7

class ShopFilterType(IntEnum):
    GachaTicket = 0
    SecretStone = 1
    SecretStone_1 = 2
    SkillBook_Ultimate = 3
    ExSkill = 4
    SkillBook = 5
    Craft = 6
    AP = 7
    CharacterExpItem = 8
    Equip = 9
    Material = 10
    Creddit = 11
    Furniture = 12
    SelectItem = 13
    Currency = 14
    Hyakkiyako = 15
    RedWinter = 16
    Trinity = 17
    Gehenna = 18
    Abydos = 19
    Millennium = 20
    Arius = 21
    Shanhaijing = 22
    Valkyrie = 23
    SRT = 24
    Event = 25
    ChaserTotalTicket = 26
    SchoolTotalTicket = 27
    ShopFilterDUMMY_1 = 28
    ShopFilterDUMMY_2 = 29
    ShopFilterDUMMY_3 = 30
    ShopFilterDUMMY_4 = 31
    ShopFilterDUMMY_5 = 32
    ShopFilterDUMMY_6 = 33
    ShopFilterDUMMY_7 = 34
    ETC = 35
    Bundle = 36

class SocialMode(IntEnum):
    TITLE = 0
    LOBBY = 1
    FORMATION = 2
    STAGE_SELECT = 3
    BATTLE = 4
    POPUP = 5
    BATTLE_RESULT = 6
    BATTLE_RESULT_VICTORY = 7
    BATTLE_RESULT_DEFEAT = 8
    INVALID = 9
    TACTIC = 10
    STRATEGY = 11
    ACCONT = 12
    CAMPAIGN_STORY = 13
    CAMPAIGN_STAGE = 14
    TACTICREADY = 15

class AccountState(IntEnum):
    WaitingSignIn = 0
    Normal = 1
    Dormant = 2
    Comeback = 3
    Newbie = 4

class MessagePopupLayout(IntEnum):
    TextOnly = 0
    ImageBig = 1
    ImageSmall = 2
    UnlockCondition = 3

class MessagePopupImagePositionType(IntEnum):
    ImageFirst = 0
    TextFirst = 1

class MessagePopupButtonType(IntEnum):
    Accept = 0
    Cancel = 1
    Command = 2

class ToastType(IntEnum):
    none = 0
    Tactic_Left = 1
    Tactic_Right = 2
    Social_Center = 3
    Social_Mission = 4
    Social_Right = 5
    Notice_Center = 6

class StrategyAIType(IntEnum):
    none = 0
    Guard = 1
    Pursuit = 2

class StageDifficulty(IntEnum):
    none = 0
    Normal = 1
    Hard = 2
    VeryHard = 3
    VeryHard_Ex = 4

class HexaUnitGrade(IntEnum):
    Grade1 = 0
    Grade2 = 1
    Grade3 = 2
    Boss = 3

class TacticEnvironment(IntEnum):
    none = 0
    WarFog = 1

class StrategyObjectType(IntEnum):
    none = 0
    Start = 1
    Heal = 2
    Skill = 3
    StatBuff = 4
    Parcel = 5
    ParcelOneTimePerAccount = 6
    Portal = 7
    PortalOneWayEnterance = 8
    PortalOneWayExit = 9
    Observatory = 10
    Beacon = 11
    BeaconOneTime = 12
    EnemySpawn = 13
    SwitchToggle = 14
    SwitchMovableWhenToggleOff = 15
    SwitchMovableWhenToggleOn = 16
    FixedStart01 = 17
    FixedStart02 = 18
    FixedStart03 = 19
    FixedStart04 = 20

class StrategyEnvironment(IntEnum):
    none = 0
    MapFog = 1

class Tag(IntEnum):
    Furniture = 0
    MovieMania = 1
    Scientific = 2
    Military = 3
    Machine = 4
    Gamer = 5
    Cook = 6
    Farmer = 7
    Sociable = 8
    Officer = 9
    Eerie = 10
    Intellectual = 11
    Healthy = 12
    Gourmet = 13
    TreasureHunter = 14
    CraftItem = 15
    CDItem = 16
    ExpItem = 17
    SecretStone = 18
    BookItem = 19
    FavorItem = 20
    MaterialItem = 21
    Item = 22
    CraftCommitment = 23
    ExpendableItem = 24
    Equipment = 25
    EnemyLarge = 26
    Decagram = 27
    EnemySmall = 28
    EnemyMedium = 29
    EnemyXLarge = 30
    Gehenna = 31
    Millennium = 32
    Valkyrie = 33
    Hyakkiyako = 34
    RedWinter = 35
    Shanhaijing = 36
    Abydos = 37
    Trinity = 38
    Hanger = 39
    StudyRoom = 40
    ClassRoom = 41
    Library = 42
    Lobby = 43
    ShootingRange = 44
    Office = 45
    SchaleResidence = 46
    SchaleOffice = 47
    Restaurant = 48
    Laboratory = 49
    AVRoom = 50
    ArcadeCenter = 51
    Gym = 52
    Garden = 53
    Convenience = 54
    Soldiery = 55
    Lounge = 56
    SchoolBuilding = 57
    Club = 58
    Campus = 59
    SchoolYard = 60
    Plaza = 61
    StudentCouncilOffice = 62
    ClosedBuilding = 63
    Annex = 64
    Pool = 65
    AllySmall = 66
    AllyMedium = 67
    AllyLarge = 68
    AllyXLarge = 69
    Dessert = 70
    Sports = 71
    Bedding = 72
    Curios = 73
    Electronic = 74
    Toy = 75
    Reservation = 76
    Household = 77
    Horticulture = 78
    Fashion = 79
    Functional = 80
    Delicious = 81
    Freakish = 82
    MomoFriends = 83
    Music = 84
    LoveStory = 85
    Game = 86
    Girlish = 87
    Beauty = 88
    Army = 89
    Humanities = 90
    Observational = 91
    Jellyz = 92
    Detective = 93
    Roman = 94
    CuriousFellow = 95
    Mystery = 96
    Doll = 97
    Movie = 98
    Art = 99
    PureLiterature = 100
    Food = 101
    Smart = 102
    BigMeal = 103
    Simplicity = 104
    Specialized = 105
    Books = 106
    Cosmetics = 107
    Gift1 = 108
    Gift2 = 109
    F_Aru = 110
    F_Eimi = 111
    F_Haruna = 112
    F_Hihumi = 113
    F_Hina = 114
    F_Hoshino = 115
    F_Iori = 116
    F_Maki = 117
    F_Neru = 118
    F_Izumi = 119
    F_Shiroko = 120
    F_Shun = 121
    F_Sumire = 122
    F_Tsurugi = 123
    F_Akane = 124
    F_Chise = 125
    F_Akari = 126
    F_Hasumi = 127
    F_Nonomi = 128
    F_Kayoko = 129
    F_Mutsuki = 130
    F_Zunko = 131
    F_Serika = 132
    F_Tusbaki = 133
    F_Yuuka = 134
    F_Haruka = 135
    F_Asuna = 136
    F_Kotori = 137
    F_Suzumi = 138
    F_Pina = 139
    F_Aris = 140
    F_Azusa = 141
    F_Cherino = 142
    TagName0004 = 143
    TagName0005 = 144
    F_Koharu = 145
    F_Hanako = 146
    F_Midori = 147
    F_Momoi = 148
    F_Hibiki = 149
    F_Karin = 150
    F_Saya = 151
    F_Mashiro = 152
    F_Airi = 153
    F_Fuuka = 154
    F_Hanae = 155
    F_Hare = 156
    F_Utaha = 157
    F_Ayane = 158
    F_Chinatsu = 159
    F_Kotama = 160
    F_Juri = 161
    F_Serina = 162
    F_Shimiko = 163
    F_Yoshimi = 164
    TagName0009 = 165
    F_Shizuko = 166
    F_Izuna = 167
    F_Nodoka = 168
    F_Yuzu = 169
    Shield = 170
    Helmet = 171
    RedHelmet = 172
    Helicopter = 173
    RangeAttack = 174
    MeleeAttack = 175
    Sweeper = 176
    Blackmarket = 177
    Yoheki = 178
    Kaiserpmc = 179
    Crusader = 180
    Goliath = 181
    Drone = 182
    Piece = 183
    ChampionHeavyArmor = 184
    Sukeban = 185
    Arius = 186
    EnemyKotori = 187
    EnemyYuuka = 188
    KaiserpmcHeavyArmor = 189
    BlackmarketHeavyArmor = 190
    YohekiHeavyArmor = 191
    SweeperBlack = 192
    SweeperYellow = 193
    GasMaskLightArmor = 194
    GehennaFuuki = 195
    ChampionAutomata = 196
    YohekiAutomata = 197
    Automata = 198
    EnemyIori = 199
    EnemyAkari = 200
    NewAutomata = 201
    NewAutomataBlack = 202
    NewAutomataYellow = 203
    Hat = 204
    Gloves = 205
    Shoes = 206
    Bag = 207
    Badge = 208
    Hairpin = 209
    Charm = 210
    Watch = 211
    Necklace = 212
    Cafe = 213
    GameCenter = 214
    ChocolateCafe = 215
    Main = 216
    Support = 217
    Explosion = 218
    Pierce = 219
    Mystic = 220
    LightArmor = 221
    HeavyArmor = 222
    Unarmed = 223
    Cover = 224
    Uncover = 225
    AR = 226
    SR = 227
    DSG = 228
    SMG = 229
    MG = 230
    HG = 231
    GL = 232
    SG = 233
    MT = 234
    RG = 235
    Front = 236
    Middle = 237
    Back = 238
    StreetBattle_Over_A = 239
    OutdoorBattle_Over_A = 240
    IndoorBattle_Over_A = 241
    StreetBattle_Under_B = 242
    OutdoorBattle_Under_B = 243
    IndoorBattle_Under_B = 244
    Kaitenranger = 245
    Transport = 246
    Itcenter = 247
    Powerplant = 248
    SukebanSwim_SMG = 249
    SukebanSwim_MG = 250
    SukebanSwim_SR = 251
    SukebanSwim_Champion = 252
    Token_S6 = 253
    Swimsuit = 254
    WaterPlay = 255
    F_Hihumi_Swimsuit = 256
    F_Azusa_Swimsuit = 257
    F_Tsurugi_Swimsuit = 258
    F_Mashiro_Swimsuit = 259
    F_Hina_swimsuit = 260
    F_Iori_swimsuit = 261
    F_Izumi_swimsuit = 262
    F_Shiroko_RidingSuit = 263
    Church = 264
    Stronghold = 265
    Gallery = 266
    MusicRoom = 267
    Emotional = 268
    F_Shun_Kid = 269
    F_Kirino_default = 270
    F_Saya_Casual = 271
    TagName0270 = 272
    TagName0271 = 273
    TagName0272 = 274
    TagName0273 = 275
    TagName0274 = 276
    TagName0275 = 277
    TagName0276 = 278
    TagName0277 = 279
    TagName0278 = 280
    TagName0279 = 281
    TagName0280 = 282
    TagName0281 = 283
    TagName0282 = 284
    TagName0283 = 285
    TagName0284 = 286
    TagName0285 = 287
    TagName0286 = 288
    TagName0287 = 289
    TagName0288 = 290
    TagName0289 = 291
    TagName0290 = 292
    TagName0291 = 293
    TagName0292 = 294
    TagName0293 = 295
    TagName0294 = 296
    TagName0295 = 297
    TagName0296 = 298
    TagName0297 = 299
    TagName0298 = 300
    TagName0299 = 301
    TagName0300 = 302
    TagName0301 = 303
    TagName0302 = 304
    TagName0303 = 305
    TagName0304 = 306
    TagName0305 = 307
    TagName0306 = 308
    TagName0307 = 309
    TagName0308 = 310
    TagName0309 = 311
    TagName0310 = 312
    TagName0311 = 313
    TagName0312 = 314
    TagName0313 = 315
    TagName0314 = 316
    TagName0315 = 317
    TagName0316 = 318
    TagName0317 = 319
    TagName0318 = 320
    TagName0319 = 321
    TagName0320 = 322
    TagName0321 = 323
    TagName0322 = 324
    TagName0323 = 325
    TagName0324 = 326
    TagName0325 = 327
    TagName0326 = 328
    TagName0327 = 329
    TagName0328 = 330
    TagName0329 = 331
    TagName0330 = 332
    TagName0331 = 333
    TagName0332 = 334
    TagName0333 = 335
    TagName0334 = 336
    TagName0335 = 337
    TagName0336 = 338
    TagName0337 = 339
    TagName0338 = 340
    TagName0339 = 341
    TagName0340 = 342
    TagName0341 = 343
    TagName0342 = 344
    TagName0343 = 345
    TagName0344 = 346
    TagName0345 = 347
    TagName0346 = 348
    TagName0347 = 349
    TagName0348 = 350
    TagName0349 = 351
    TagName0350 = 352
    TagName0351 = 353
    TagName0352 = 354
    TagName0353 = 355
    TagName0354 = 356
    TagName0355 = 357
    TagName0356 = 358
    TagName0357 = 359
    TagName0358 = 360
    TagName0359 = 361
    TagName0360 = 362
    TagName0361 = 363
    TagName0362 = 364
    TagName0363 = 365
    TagName0364 = 366
    TagName0365 = 367
    TagName0366 = 368
    TagName0367 = 369
    TagName0368 = 370
    TagName0369 = 371
    TagName0370 = 372
    TagName0371 = 373
    TagName0372 = 374
    TagName0373 = 375
    TagName0374 = 376
    TagName0375 = 377
    TagName0376 = 378
    TagName0377 = 379
    TagName0378 = 380
    TagName0379 = 381
    TagName0380 = 382
    TagName0381 = 383
    TagName0382 = 384
    TagName0383 = 385
    TagName0384 = 386
    TagName0385 = 387
    TagName0386 = 388
    TagName0387 = 389
    TagName0388 = 390
    TagName0389 = 391
    TagName0390 = 392
    TagName0391 = 393
    TagName0392 = 394
    TagName0393 = 395
    TagName0394 = 396
    TagName0395 = 397
    TagName0396 = 398
    TagName0397 = 399
    TagName0398 = 400
    TagName0399 = 401
    TagName0400 = 402
    TagName0401 = 403
    TagName0402 = 404
    TagName0403 = 405
    TagName0404 = 406
    TagName0405 = 407
    TagName0406 = 408
    TagName0407 = 409
    TagName0408 = 410
    TagName0409 = 411
    TagName0410 = 412
    TagName0411 = 413
    TagName0412 = 414
    TagName0413 = 415
    TagName0414 = 416
    TagName0415 = 417
    TagName0416 = 418
    TagName0417 = 419
    TagName0418 = 420
    TagName0419 = 421
    TagName0420 = 422
    TagName0421 = 423
    TagName0422 = 424
    TagName0423 = 425
    TagName0424 = 426
    TagName0425 = 427
    TagName0426 = 428
    TagName0427 = 429
    TagName0428 = 430
    TagName0429 = 431
    TagName0430 = 432
    TagName0431 = 433
    TagName0432 = 434
    TagName0433 = 435
    TagName0434 = 436
    TagName0435 = 437
    TagName0436 = 438
    TagName0437 = 439
    TagName0438 = 440
    TagName0439 = 441
    TagName0440 = 442
    TagName0441 = 443
    TagName0442 = 444
    TagName0443 = 445
    TagName0444 = 446
    TagName0445 = 447
    TagName0446 = 448
    TagName0447 = 449
    TagName0448 = 450
    TagName0449 = 451
    TagName0450 = 452
    TagName0451 = 453
    TagName0452 = 454
    TagName0453 = 455
    TagName0454 = 456
    TagName0455 = 457
    TagName0456 = 458
    TagName0457 = 459
    TagName0458 = 460
    TagName0459 = 461
    TagName0460 = 462
    TagName0461 = 463
    TagName0462 = 464
    TagName0463 = 465
    TagName0464 = 466
    TagName0465 = 467
    TagName0466 = 468
    TagName0467 = 469
    TagName0468 = 470
    TagName0469 = 471
    TagName0470 = 472
    TagName0471 = 473
    TagName0472 = 474
    TagName0473 = 475
    TagName0474 = 476
    TagName0475 = 477
    TagName0476 = 478
    TagName0477 = 479
    TagName0478 = 480
    TagName0479 = 481
    TagName0480 = 482
    TagName0481 = 483
    TagName0482 = 484
    TagName0483 = 485
    TagName0484 = 486
    TagName0485 = 487
    TagName0486 = 488
    TagName0487 = 489
    TagName0488 = 490
    TagName0489 = 491
    TagName0490 = 492
    TagName0491 = 493
    TagName0492 = 494
    TagName0493 = 495
    TagName0494 = 496
    TagName0495 = 497
    TagName0496 = 498
    TagName0497 = 499
    TagName0498 = 500
    TagName0499 = 501
    TagName0500 = 502
    TagName0501 = 503
    TagName0502 = 504
    TagName0503 = 505
    TagName0504 = 506
    TagName0505 = 507
    TagName0506 = 508
    TagName0507 = 509
    TagName0508 = 510
    TagName0509 = 511
    TagName0510 = 512
    TagName0511 = 513
    TagName0512 = 514
    TagName0513 = 515
    TagName0514 = 516
    TagName0515 = 517
    TagName0516 = 518
    TagName0517 = 519
    TagName0518 = 520
    TagName0519 = 521
    TagName0520 = 522
    TagName0521 = 523
    TagName0522 = 524
    TagName0523 = 525
    TagName0524 = 526
    TagName0525 = 527
    TagName0526 = 528
    TagName0527 = 529
    TagName0528 = 530
    TagName0529 = 531
    TagName0530 = 532
    TagName0531 = 533
    TagName0532 = 534
    TagName0533 = 535
    TagName0534 = 536
    TagName0535 = 537
    TagName0536 = 538
    TagName0537 = 539
    TagName0538 = 540
    TagName0539 = 541
    TagName0540 = 542
    TagName0541 = 543
    TagName0542 = 544
    TagName0543 = 545
    TagName0544 = 546
    TagName0545 = 547
    TagName0546 = 548
    TagName0547 = 549
    TagName0548 = 550
    TagName0549 = 551
    TagName0550 = 552
    TagName0551 = 553
    TagName0552 = 554
    TagName0553 = 555
    TagName0554 = 556
    TagName0555 = 557
    TagName0556 = 558
    TagName0557 = 559
    TagName0558 = 560
    TagName0559 = 561
    TagName0560 = 562
    TagName0561 = 563
    TagName0562 = 564
    TagName0563 = 565
    TagName0564 = 566
    TagName0565 = 567
    TagName0566 = 568
    TagName0567 = 569
    TagName0568 = 570
    TagName0569 = 571
    TagName0570 = 572
    TagName0571 = 573
    TagName0572 = 574
    TagName0573 = 575
    TagName0574 = 576
    TagName0575 = 577
    TagName0576 = 578
    TagName0577 = 579
    TagName0578 = 580
    TagName0579 = 581
    TagName0580 = 582
    TagName0581 = 583
    TagName0582 = 584
    TagName0583 = 585
    TagName0584 = 586
    TagName0585 = 587
    TagName0586 = 588
    TagName0587 = 589
    TagName0588 = 590
    TagName0589 = 591
    TagName0590 = 592
    TagName0591 = 593
    TagName0592 = 594
    TagName0593 = 595
    TagName0594 = 596
    TagName0595 = 597
    TagName0596 = 598
    TagName0597 = 599
    TagName0598 = 600
    TagName0599 = 601
    TagName0600 = 602
    TagName0601 = 603
    TagName0602 = 604
    TagName0603 = 605
    TagName0604 = 606
    TagName0605 = 607
    TagName0606 = 608
    TagName0607 = 609
    TagName0608 = 610
    TagName0609 = 611
    TagName0610 = 612
    TagName0611 = 613
    TagName0612 = 614
    TagName0613 = 615
    TagName0614 = 616
    TagName0615 = 617
    TagName0616 = 618
    TagName0617 = 619
    TagName0618 = 620
    TagName0619 = 621
    TagName0620 = 622
    TagName0621 = 623
    TagName0622 = 624
    TagName0623 = 625
    TagName0624 = 626
    TagName0625 = 627
    TagName0626 = 628
    TagName0627 = 629
    TagName0628 = 630
    TagName0629 = 631
    TagName0630 = 632
    TagName0631 = 633
    TagName0632 = 634
    TagName0633 = 635
    TagName0634 = 636
    TagName0635 = 637
    TagName0636 = 638
    TagName0637 = 639
    TagName0638 = 640
    TagName0639 = 641
    TagName0640 = 642
    TagName0641 = 643
    TagName0642 = 644
    TagName0643 = 645
    TagName0644 = 646
    TagName0645 = 647
    TagName0646 = 648
    TagName0647 = 649
    TagName0648 = 650
    TagName0649 = 651
    TagName0650 = 652
    TagName0651 = 653
    TagName0652 = 654
    TagName0653 = 655
    TagName0654 = 656
    TagName0655 = 657
    TagName0656 = 658
    TagName0657 = 659
    TagName0658 = 660
    TagName0659 = 661
    TagName0660 = 662
    TagName0661 = 663
    TagName0662 = 664
    TagName0663 = 665
    TagName0664 = 666
    TagName0665 = 667
    TagName0666 = 668
    TagName0667 = 669
    TagName0668 = 670
    TagName0669 = 671
    TagName0670 = 672
    TagName0671 = 673
    TagName0672 = 674
    TagName0673 = 675
    TagName0674 = 676
    TagName0675 = 677
    TagName0676 = 678
    TagName0677 = 679
    TagName0678 = 680
    TagName0679 = 681
    TagName0680 = 682
    TagName0681 = 683
    TagName0682 = 684
    TagName0683 = 685
    TagName0684 = 686
    TagName0685 = 687
    TagName0686 = 688
    TagName0687 = 689
    TagName0688 = 690
    TagName0689 = 691
    TagName0690 = 692
    TagName0691 = 693
    TagName0692 = 694
    TagName0693 = 695
    TagName0694 = 696
    TagName0695 = 697
    TagName0696 = 698
    TagName0697 = 699
    TagName0698 = 700
    TagName0699 = 701
    TagName0700 = 702
    TagName0701 = 703
    TagName0702 = 704
    TagName0703 = 705
    TagName0704 = 706
    TagName0705 = 707
    TagName0706 = 708
    TagName0707 = 709
    TagName0708 = 710
    TagName0709 = 711
    TagName0710 = 712
    TagName0711 = 713
    TagName0712 = 714
    TagName0713 = 715
    TagName0714 = 716
    TagName0715 = 717
    TagName0716 = 718
    TagName0717 = 719
    TagName0718 = 720
    TagName0719 = 721
    TagName0720 = 722
    TagName0721 = 723
    TagName0722 = 724
    TagName0723 = 725
    TagName0724 = 726
    TagName0725 = 727
    TagName0726 = 728
    TagName0727 = 729
    TagName0728 = 730
    TagName0729 = 731
    TagName0730 = 732
    TagName0731 = 733
    TagName0732 = 734
    TagName0733 = 735
    TagName0734 = 736
    TagName0735 = 737
    TagName0736 = 738
    TagName0737 = 739
    TagName0738 = 740
    TagName0739 = 741
    TagName0740 = 742
    TagName0741 = 743
    TagName0742 = 744
    TagName0743 = 745
    TagName0744 = 746
    TagName0745 = 747
    TagName0746 = 748
    TagName0747 = 749
    TagName0748 = 750
    TagName0749 = 751
    TagName0750 = 752
    TagName0751 = 753
    TagName0752 = 754
    TagName0753 = 755
    TagName0754 = 756
    TagName0755 = 757
    TagName0756 = 758
    TagName0757 = 759
    TagName0758 = 760
    TagName0759 = 761
    TagName0760 = 762
    TagName0761 = 763
    TagName0762 = 764
    TagName0763 = 765
    TagName0764 = 766
    TagName0765 = 767
    TagName0766 = 768
    TagName0767 = 769
    TagName0768 = 770
    TagName0769 = 771
    TagName0770 = 772
    TagName0771 = 773
    TagName0772 = 774
    TagName0773 = 775
    TagName0774 = 776
    TagName0775 = 777
    TagName0776 = 778
    TagName0777 = 779
    TagName0778 = 780
    TagName0779 = 781
    TagName0780 = 782
    TagName0781 = 783
    TagName0782 = 784
    TagName0783 = 785
    TagName0784 = 786
    TagName0785 = 787
    TagName0786 = 788
    TagName0787 = 789
    TagName0788 = 790
    TagName0789 = 791
    TagName0790 = 792
    TagName0791 = 793
    TagName0792 = 794
    TagName0793 = 795
    TagName0794 = 796
    TagName0795 = 797
    TagName0796 = 798
    TagName0797 = 799
    TagName0798 = 800
    TagName0799 = 801
    TagName0800 = 802
    TagName0801 = 803
    TagName0802 = 804
    TagName0803 = 805
    TagName0804 = 806
    TagName0805 = 807
    TagName0806 = 808
    TagName0807 = 809
    TagName0808 = 810
    TagName0809 = 811
    TagName0810 = 812
    TagName0811 = 813
    TagName0812 = 814
    TagName0813 = 815
    TagName0814 = 816
    TagName0815 = 817
    TagName0816 = 818
    TagName0817 = 819
    TagName0818 = 820
    TagName0819 = 821
    TagName0820 = 822
    TagName0821 = 823
    TagName0822 = 824
    TagName0823 = 825
    TagName0824 = 826
    TagName0825 = 827
    TagName0826 = 828
    TagName0827 = 829
    TagName0828 = 830
    TagName0829 = 831
    TagName0830 = 832
    TagName0831 = 833
    TagName0832 = 834
    TagName0833 = 835
    TagName0834 = 836
    TagName0835 = 837
    TagName0836 = 838
    TagName0837 = 839
    TagName0838 = 840
    TagName0839 = 841
    TagName0840 = 842
    TagName0841 = 843
    TagName0842 = 844
    TagName0843 = 845
    TagName0844 = 846
    TagName0845 = 847
    TagName0846 = 848
    TagName0847 = 849
    TagName0848 = 850
    TagName0849 = 851
    TagName0850 = 852
    TagName0851 = 853
    TagName0852 = 854
    TagName0853 = 855
    TagName0854 = 856
    TagName0855 = 857
    TagName0856 = 858
    TagName0857 = 859
    TagName0858 = 860
    TagName0859 = 861
    TagName0860 = 862
    TagName0861 = 863
    TagName0862 = 864
    TagName0863 = 865
    TagName0864 = 866
    TagName0865 = 867
    TagName0866 = 868
    TagName0867 = 869
    TagName0868 = 870
    TagName0869 = 871
    TagName0870 = 872
    TagName0871 = 873
    TagName0872 = 874
    TagName0873 = 875
    TagName0874 = 876
    TagName0875 = 877
    TagName0876 = 878
    TagName0877 = 879
    TagName0878 = 880
    TagName0879 = 881
    TagName0880 = 882
    TagName0881 = 883
    TagName0882 = 884
    TagName0883 = 885
    TagName0884 = 886
    TagName0885 = 887
    TagName0886 = 888
    TagName0887 = 889
    TagName0888 = 890
    TagName0889 = 891
    TagName0890 = 892
    TagName0891 = 893
    TagName0892 = 894
    TagName0893 = 895
    TagName0894 = 896
    TagName0895 = 897
    TagName0896 = 898
    TagName0897 = 899
    TagName0898 = 900
    TagName0899 = 901
    TagName0900 = 902
    TagName0901 = 903
    TagName0902 = 904
    TagName0903 = 905
    TagName0904 = 906
    TagName0905 = 907
    TagName0906 = 908
    TagName0907 = 909
    TagName0908 = 910
    TagName0909 = 911
    TagName0910 = 912
    TagName0911 = 913
    TagName0912 = 914
    TagName0913 = 915
    TagName0914 = 916
    TagName0915 = 917
    TagName0916 = 918
    TagName0917 = 919
    TagName0918 = 920
    TagName0919 = 921
    TagName0920 = 922
    TagName0921 = 923
    TagName0922 = 924
    TagName0923 = 925
    TagName0924 = 926
    TagName0925 = 927
    TagName0926 = 928
    TagName0927 = 929
    TagName0928 = 930
    TagName0929 = 931
    TagName0930 = 932
    TagName0931 = 933
    TagName0932 = 934
    TagName0933 = 935
    TagName0934 = 936
    TagName0935 = 937
    TagName0936 = 938
    TagName0937 = 939
    TagName0938 = 940
    TagName0939 = 941
    TagName0940 = 942
    TagName0941 = 943
    TagName0942 = 944
    TagName0943 = 945
    TagName0944 = 946
    TagName0945 = 947
    TagName0946 = 948
    TagName0947 = 949
    TagName0948 = 950
    TagName0949 = 951
    TagName0950 = 952
    TagName0951 = 953
    TagName0952 = 954
    TagName0953 = 955
    TagName0954 = 956
    TagName0955 = 957
    TagName0956 = 958
    TagName0957 = 959
    TagName0958 = 960
    TagName0959 = 961
    TagName0960 = 962
    TagName0961 = 963
    TagName0962 = 964
    TagName0963 = 965
    TagName0964 = 966
    TagName0965 = 967
    TagName0966 = 968
    TagName0967 = 969
    TagName0968 = 970
    TagName0969 = 971
    TagName0970 = 972
    TagName0971 = 973
    TagName0972 = 974
    TagName0973 = 975
    TagName0974 = 976
    TagName0975 = 977
    TagName0976 = 978
    TagName0977 = 979
    TagName0978 = 980
    TagName0979 = 981
    TagName0980 = 982
    TagName0981 = 983
    TagName0982 = 984
    TagName0983 = 985
    TagName0984 = 986
    TagName0985 = 987
    TagName0986 = 988
    TagName0987 = 989
    TagName0988 = 990
    TagName0989 = 991
    TagName0990 = 992
    TagName0991 = 993
    TagName0992 = 994
    TagName0993 = 995
    TagName0994 = 996
    TagName0995 = 997
    TagName0996 = 998
    TagName0997 = 999
    TagName0998 = 1000
    TagName0999 = 1001
    TagName1000 = 1002
    TagName1001 = 1003
    TagName1002 = 1004
    TagName1003 = 1005
    TagName1004 = 1006
    TagName1005 = 1007
    TagName1006 = 1008
    TagName1007 = 1009
    TagName1008 = 1010
    TagName1009 = 1011
    TagName1010 = 1012
    TagName1011 = 1013
    TagName1012 = 1014
    TagName1013 = 1015
    TagName1014 = 1016
    TagName1015 = 1017
    TagName1016 = 1018
    TagName1017 = 1019
    TagName1018 = 1020
    TagName1019 = 1021
    TagName1020 = 1022
    TagName1021 = 1023
    TagName1022 = 1024
    TagName1023 = 1025
    TagName1024 = 1026
    TagName1025 = 1027
    TagName1026 = 1028
    TagName1027 = 1029
    TagName1028 = 1030
    TagName1029 = 1031
    TagName1030 = 1032
    TagName1031 = 1033
    TagName1032 = 1034
    TagName1033 = 1035
    TagName1034 = 1036
    TagName1035 = 1037
    TagName1036 = 1038
    TagName1037 = 1039
    TagName1038 = 1040
    TagName1039 = 1041
    TagName1040 = 1042
    TagName1041 = 1043
    TagName1042 = 1044
    TagName1043 = 1045
    TagName1044 = 1046
    TagName1045 = 1047
    TagName1046 = 1048
    TagName1047 = 1049
    TagName1048 = 1050
    TagName1049 = 1051
    TagName1050 = 1052
    TagName1051 = 1053
    TagName1052 = 1054
    TagName1053 = 1055
    TagName1054 = 1056
    TagName1055 = 1057
    TagName1056 = 1058
    TagName1057 = 1059
    TagName1058 = 1060
    TagName1059 = 1061
    TagName1060 = 1062
    TagName1061 = 1063
    TagName1062 = 1064
    TagName1063 = 1065
    TagName1064 = 1066
    TagName1065 = 1067
    TagName1066 = 1068
    TagName1067 = 1069
    TagName1068 = 1070
    TagName1069 = 1071
    TagName1070 = 1072
    TagName1071 = 1073
    TagName1072 = 1074
    TagName1073 = 1075
    TagName1074 = 1076
    TagName1075 = 1077
    TagName1076 = 1078
    TagName1077 = 1079
    TagName1078 = 1080
    TagName1079 = 1081
    TagName1080 = 1082
    TagName1081 = 1083
    TagName1082 = 1084
    TagName1083 = 1085
    TagName1084 = 1086
    TagName1085 = 1087
    TagName1086 = 1088
    TagName1087 = 1089
    TagName1088 = 1090
    TagName1089 = 1091
    TagName1090 = 1092
    TagName1091 = 1093
    TagName1092 = 1094
    TagName1093 = 1095
    TagName1094 = 1096
    TagName1095 = 1097
    TagName1096 = 1098
    TagName1097 = 1099
    TagName1098 = 1100
    TagName1099 = 1101
    TagName1100 = 1102
    TagName1101 = 1103
    TagName1102 = 1104
    TagName1103 = 1105
    TagName1104 = 1106
    TagName1105 = 1107
    TagName1106 = 1108
    TagName1107 = 1109
    TagName1108 = 1110
    TagName1109 = 1111
    TagName1110 = 1112
    TagName1111 = 1113
    TagName1112 = 1114
    TagName1113 = 1115
    TagName1114 = 1116
    TagName1115 = 1117
    TagName1116 = 1118
    TagName1117 = 1119
    TagName1118 = 1120
    TagName1119 = 1121
    TagName1120 = 1122
    TagName1121 = 1123
    TagName1122 = 1124
    TagName1123 = 1125
    TagName1124 = 1126
    TagName1125 = 1127
    TagName1126 = 1128
    TagName1127 = 1129
    TagName1128 = 1130
    TagName1129 = 1131
    TagName1130 = 1132
    TagName1131 = 1133
    TagName1132 = 1134
    TagName1133 = 1135
    TagName1134 = 1136
    TagName1135 = 1137
    TagName1136 = 1138
    TagName1137 = 1139
    TagName1138 = 1140
    TagName1139 = 1141
    TagName1140 = 1142
    TagName1141 = 1143
    TagName1142 = 1144
    TagName1143 = 1145
    TagName1144 = 1146
    TagName1145 = 1147
    TagName1146 = 1148
    TagName1147 = 1149
    TagName1148 = 1150
    TagName1149 = 1151
    TagName1150 = 1152
    TagName1151 = 1153
    TagName1152 = 1154
    TagName1153 = 1155
    TagName1154 = 1156
    TagName1155 = 1157
    TagName1156 = 1158
    TagName1157 = 1159
    TagName1158 = 1160
    TagName1159 = 1161
    TagName1160 = 1162
    TagName1161 = 1163
    TagName1162 = 1164
    TagName1163 = 1165
    TagName1164 = 1166
    TagName1165 = 1167
    TagName1166 = 1168
    TagName1167 = 1169
    TagName1168 = 1170
    TagName1169 = 1171
    TagName1170 = 1172
    TagName1171 = 1173
    TagName1172 = 1174
    TagName1173 = 1175
    TagName1174 = 1176
    TagName1175 = 1177
    TagName1176 = 1178
    TagName1177 = 1179
    TagName1178 = 1180
    TagName1179 = 1181
    TagName1180 = 1182
    TagName1181 = 1183
    TagName1182 = 1184
    TagName1183 = 1185
    TagName1184 = 1186
    TagName1185 = 1187
    TagName1186 = 1188
    TagName1187 = 1189
    TagName1188 = 1190
    TagName1189 = 1191
    TagName1190 = 1192
    TagName1191 = 1193
    TagName1192 = 1194
    TagName1193 = 1195
    TagName1194 = 1196
    TagName1195 = 1197
    TagName1196 = 1198
    TagName1197 = 1199
    TagName1198 = 1200
    TagName1199 = 1201
    TagName1200 = 1202
    TagName1201 = 1203
    TagName1202 = 1204
    TagName1203 = 1205
    TagName1204 = 1206
    TagName1205 = 1207
    TagName1206 = 1208
    TagName1207 = 1209
    TagName1208 = 1210
    TagName1209 = 1211
    TagName1210 = 1212
    TagName1211 = 1213
    TagName1212 = 1214
    TagName1213 = 1215
    TagName1214 = 1216
    TagName1215 = 1217
    TagName1216 = 1218
    TagName1217 = 1219
    TagName1218 = 1220
    TagName1219 = 1221
    TagName1220 = 1222
    TagName1221 = 1223
    TagName1222 = 1224
    TagName1223 = 1225
    TagName1224 = 1226
    TagName1225 = 1227
    TagName1226 = 1228
    TagName1227 = 1229
    TagName1228 = 1230
    TagName1229 = 1231
    TagName1230 = 1232
    TagName1231 = 1233
    TagName1232 = 1234
    TagName1233 = 1235
    TagName1234 = 1236
    TagName1235 = 1237
    TagName1236 = 1238
    TagName1237 = 1239
    TagName1238 = 1240
    TagName1239 = 1241
    TagName1240 = 1242
    TagName1241 = 1243
    TagName1242 = 1244
    TagName1243 = 1245
    TagName1244 = 1246
    TagName1245 = 1247
    TagName1246 = 1248
    TagName1247 = 1249
    TagName1248 = 1250
    TagName1249 = 1251
    TagName1250 = 1252
    TagName1251 = 1253
    TagName1252 = 1254
    TagName1253 = 1255
    TagName1254 = 1256
    TagName1255 = 1257
    TagName1256 = 1258
    TagName1257 = 1259
    TagName1258 = 1260
    TagName1259 = 1261
    TagName1260 = 1262
    TagName1261 = 1263
    TagName1262 = 1264
    TagName1263 = 1265
    TagName1264 = 1266
    TagName1265 = 1267
    TagName1266 = 1268
    TagName1267 = 1269
    TagName1268 = 1270
    TagName1269 = 1271
    TagName1270 = 1272
    TagName1271 = 1273
    TagName1272 = 1274
    TagName1273 = 1275
    TagName1274 = 1276
    TagName1275 = 1277
    TagName1276 = 1278
    TagName1277 = 1279
    TagName1278 = 1280
    TagName1279 = 1281
    TagName1280 = 1282
    TagName1281 = 1283
    TagName1282 = 1284
    TagName1283 = 1285
    TagName1284 = 1286
    TagName1285 = 1287
    TagName1286 = 1288
    TagName1287 = 1289
    TagName1288 = 1290
    TagName1289 = 1291
    TagName1290 = 1292
    TagName1291 = 1293
    TagName1292 = 1294
    TagName1293 = 1295
    TagName1294 = 1296
    TagName1295 = 1297
    TagName1296 = 1298
    TagName1297 = 1299
    TagName1298 = 1300
    TagName1299 = 1301
    TagName1300 = 1302
    TagName1301 = 1303
    TagName1302 = 1304
    TagName1303 = 1305
    TagName1304 = 1306
    TagName1305 = 1307
    TagName1306 = 1308
    TagName1307 = 1309
    TagName1308 = 1310
    TagName1309 = 1311
    TagName1310 = 1312
    TagName1311 = 1313
    TagName1312 = 1314
    TagName1313 = 1315
    TagName1314 = 1316
    TagName1315 = 1317
    TagName1316 = 1318
    TagName1317 = 1319
    TagName1318 = 1320
    TagName1319 = 1321
    TagName1320 = 1322
    TagName1321 = 1323
    TagName1322 = 1324
    TagName1323 = 1325
    TagName1324 = 1326
    TagName1325 = 1327
    TagName1326 = 1328
    TagName1327 = 1329
    TagName1328 = 1330
    TagName1329 = 1331
    TagName1330 = 1332
    TagName1331 = 1333
    TagName1332 = 1334
    TagName1333 = 1335
    TagName1334 = 1336
    TagName1335 = 1337
    TagName1336 = 1338
    TagName1337 = 1339
    TagName1338 = 1340
    TagName1339 = 1341
    TagName1340 = 1342
    TagName1341 = 1343
    TagName1342 = 1344
    TagName1343 = 1345
    TagName1344 = 1346
    TagName1345 = 1347
    TagName1346 = 1348
    TagName1347 = 1349
    TagName1348 = 1350
    TagName1349 = 1351
    TagName1350 = 1352
    TagName1351 = 1353
    TagName1352 = 1354
    TagName1353 = 1355
    TagName1354 = 1356
    TagName1355 = 1357
    TagName1356 = 1358
    TagName1357 = 1359
    TagName1358 = 1360
    TagName1359 = 1361
    TagName1360 = 1362
    TagName1361 = 1363
    TagName1362 = 1364
    TagName1363 = 1365
    TagName1364 = 1366
    TagName1365 = 1367
    TagName1366 = 1368
    TagName1367 = 1369
    TagName1368 = 1370
    TagName1369 = 1371
    TagName1370 = 1372
    TagName1371 = 1373
    TagName1372 = 1374
    TagName1373 = 1375
    TagName1374 = 1376
    TagName1375 = 1377
    TagName1376 = 1378
    TagName1377 = 1379
    TagName1378 = 1380
    TagName1379 = 1381
    TagName1380 = 1382
    TagName1381 = 1383
    TagName1382 = 1384
    TagName1383 = 1385
    TagName1384 = 1386
    TagName1385 = 1387
    TagName1386 = 1388
    TagName1387 = 1389
    TagName1388 = 1390
    TagName1389 = 1391
    TagName1390 = 1392
    TagName1391 = 1393
    TagName1392 = 1394
    TagName1393 = 1395
    TagName1394 = 1396
    TagName1395 = 1397
    TagName1396 = 1398
    TagName1397 = 1399
    TagName1398 = 1400
    TagName1399 = 1401
    TagName1400 = 1402
    TagName1401 = 1403
    TagName1402 = 1404
    TagName1403 = 1405
    TagName1404 = 1406
    TagName1405 = 1407
    TagName1406 = 1408
    TagName1407 = 1409
    TagName1408 = 1410
    TagName1409 = 1411
    TagName1410 = 1412
    TagName1411 = 1413
    TagName1412 = 1414
    TagName1413 = 1415
    TagName1414 = 1416
    TagName1415 = 1417
    TagName1416 = 1418
    TagName1417 = 1419
    TagName1418 = 1420
    TagName1419 = 1421
    TagName1420 = 1422
    TagName1421 = 1423
    TagName1422 = 1424
    TagName1423 = 1425
    TagName1424 = 1426
    TagName1425 = 1427
    TagName1426 = 1428
    TagName1427 = 1429
    TagName1428 = 1430
    TagName1429 = 1431
    TagName1430 = 1432
    TagName1431 = 1433
    TagName1432 = 1434
    TagName1433 = 1435
    TagName1434 = 1436
    TagName1435 = 1437
    TagName1436 = 1438
    TagName1437 = 1439
    TagName1438 = 1440
    TagName1439 = 1441
    TagName1440 = 1442
    TagName1441 = 1443
    TagName1442 = 1444
    TagName1443 = 1445
    TagName1444 = 1446
    TagName1445 = 1447
    TagName1446 = 1448
    TagName1447 = 1449
    TagName1448 = 1450
    TagName1449 = 1451
    TagName1450 = 1452
    TagName1451 = 1453
    TagName1452 = 1454
    TagName1453 = 1455
    TagName1454 = 1456
    TagName1455 = 1457
    TagName1456 = 1458
    TagName1457 = 1459
    TagName1458 = 1460
    TagName1459 = 1461
    TagName1460 = 1462
    TagName1461 = 1463
    TagName1462 = 1464
    TagName1463 = 1465
    TagName1464 = 1466
    TagName1465 = 1467
    TagName1466 = 1468
    TagName1467 = 1469
    TagName1468 = 1470
    TagName1469 = 1471
    TagName1470 = 1472
    TagName1471 = 1473
    TagName1472 = 1474
    TagName1473 = 1475
    TagName1474 = 1476
    TagName1475 = 1477
    TagName1476 = 1478
    TagName1477 = 1479
    TagName1478 = 1480
    TagName1479 = 1481
    TagName1480 = 1482
    TagName1481 = 1483
    TagName1482 = 1484
    TagName1483 = 1485
    TagName1484 = 1486
    TagName1485 = 1487
    TagName1486 = 1488
    TagName1487 = 1489
    TagName1488 = 1490
    TagName1489 = 1491
    TagName1490 = 1492
    TagName1491 = 1493
    TagName1492 = 1494
    TagName1493 = 1495
    TagName1494 = 1496
    TagName1495 = 1497
    TagName1496 = 1498
    TagName1497 = 1499
    TagName1498 = 1500
    TagName1499 = 1501
    TagName1500 = 1502
    TagName1501 = 1503
    TagName1502 = 1504
    TagName1503 = 1505
    TagName1504 = 1506
    TagName1505 = 1507
    TagName1506 = 1508
    TagName1507 = 1509
    TagName1508 = 1510
    TagName1509 = 1511
    TagName1510 = 1512
    TagName1511 = 1513
    TagName1512 = 1514
    TagName1513 = 1515
    TagName1514 = 1516
    TagName1515 = 1517
    TagName1516 = 1518
    TagName1517 = 1519
    TagName1518 = 1520
    TagName1519 = 1521
    TagName1520 = 1522
    TagName1521 = 1523
    TagName1522 = 1524
    TagName1523 = 1525
    TagName1524 = 1526
    TagName1525 = 1527
    TagName1526 = 1528
    TagName1527 = 1529
    TagName1528 = 1530
    TagName1529 = 1531
    TagName1530 = 1532
    TagName1531 = 1533
    TagName1532 = 1534
    TagName1533 = 1535
    TagName1534 = 1536
    TagName1535 = 1537
    TagName1536 = 1538
    TagName1537 = 1539
    TagName1538 = 1540
    TagName1539 = 1541
    TagName1540 = 1542
    TagName1541 = 1543
    TagName1542 = 1544
    TagName1543 = 1545
    TagName1544 = 1546
    TagName1545 = 1547
    TagName1546 = 1548
    TagName1547 = 1549
    TagName1548 = 1550
    TagName1549 = 1551
    TagName1550 = 1552
    TagName1551 = 1553
    TagName1552 = 1554
    TagName1553 = 1555
    TagName1554 = 1556
    TagName1555 = 1557
    TagName1556 = 1558
    TagName1557 = 1559
    TagName1558 = 1560
    TagName1559 = 1561
    TagName1560 = 1562
    TagName1561 = 1563
    TagName1562 = 1564
    TagName1563 = 1565
    TagName1564 = 1566
    TagName1565 = 1567
    TagName1566 = 1568
    TagName1567 = 1569
    TagName1568 = 1570
    TagName1569 = 1571
    TagName1570 = 1572
    TagName1571 = 1573
    TagName1572 = 1574
    TagName1573 = 1575
    TagName1574 = 1576
    TagName1575 = 1577
    TagName1576 = 1578
    TagName1577 = 1579
    TagName1578 = 1580
    TagName1579 = 1581
    TagName1580 = 1582
    TagName1581 = 1583
    TagName1582 = 1584
    TagName1583 = 1585
    TagName1584 = 1586
    TagName1585 = 1587
    TagName1586 = 1588
    TagName1587 = 1589
    TagName1588 = 1590
    TagName1589 = 1591
    TagName1590 = 1592
    TagName1591 = 1593
    TagName1592 = 1594
    TagName1593 = 1595
    TagName1594 = 1596
    TagName1595 = 1597
    TagName1596 = 1598
    TagName1597 = 1599
    TagName1598 = 1600
    TagName1599 = 1601
    TagName1600 = 1602
    TagName1601 = 1603
    TagName1602 = 1604
    TagName1603 = 1605
    TagName1604 = 1606
    TagName1605 = 1607
    TagName1606 = 1608
    TagName1607 = 1609
    TagName1608 = 1610
    TagName1609 = 1611
    TagName1610 = 1612
    TagName1611 = 1613
    TagName1612 = 1614
    TagName1613 = 1615
    TagName1614 = 1616
    TagName1615 = 1617
    TagName1616 = 1618
    TagName1617 = 1619
    TagName1618 = 1620
    TagName1619 = 1621
    TagName1620 = 1622
    TagName1621 = 1623
    TagName1622 = 1624
    TagName1623 = 1625
    TagName1624 = 1626
    TagName1625 = 1627
    TagName1626 = 1628
    TagName1627 = 1629
    TagName1628 = 1630
    TagName1629 = 1631
    TagName1630 = 1632
    TagName1631 = 1633
    TagName1632 = 1634
    TagName1633 = 1635
    TagName1634 = 1636
    TagName1635 = 1637
    TagName1636 = 1638
    TagName1637 = 1639
    TagName1638 = 1640
    TagName1639 = 1641
    TagName1640 = 1642
    TagName1641 = 1643
    TagName1642 = 1644
    TagName1643 = 1645
    TagName1644 = 1646
    TagName1645 = 1647
    TagName1646 = 1648
    TagName1647 = 1649
    TagName1648 = 1650
    TagName1649 = 1651
    TagName1650 = 1652
    TagName1651 = 1653
    TagName1652 = 1654
    TagName1653 = 1655
    TagName1654 = 1656
    TagName1655 = 1657
    TagName1656 = 1658
    TagName1657 = 1659
    TagName1658 = 1660
    TagName1659 = 1661
    TagName1660 = 1662
    TagName1661 = 1663
    TagName1662 = 1664
    TagName1663 = 1665
    TagName1664 = 1666
    TagName1665 = 1667
    TagName1666 = 1668
    TagName1667 = 1669
    TagName1668 = 1670
    TagName1669 = 1671
    TagName1670 = 1672
    TagName1671 = 1673
    TagName1672 = 1674
    TagName1673 = 1675
    TagName1674 = 1676
    TagName1675 = 1677
    TagName1676 = 1678
    TagName1677 = 1679
    TagName1678 = 1680
    TagName1679 = 1681
    TagName1680 = 1682
    TagName1681 = 1683
    TagName1682 = 1684
    TagName1683 = 1685
    TagName1684 = 1686
    TagName1685 = 1687
    TagName1686 = 1688
    TagName1687 = 1689
    TagName1688 = 1690
    TagName1689 = 1691
    TagName1690 = 1692
    TagName1691 = 1693
    TagName1692 = 1694
    TagName1693 = 1695
    TagName1694 = 1696
    TagName1695 = 1697
    TagName1696 = 1698
    TagName1697 = 1699
    TagName1698 = 1700
    TagName1699 = 1701
    TagName1700 = 1702
    TagName1701 = 1703
    TagName1702 = 1704
    TagName1703 = 1705
    TagName1704 = 1706
    TagName1705 = 1707
    TagName1706 = 1708
    TagName1707 = 1709
    TagName1708 = 1710
    TagName1709 = 1711
    TagName1710 = 1712
    TagName1711 = 1713
    TagName1712 = 1714
    TagName1713 = 1715
    TagName1714 = 1716
    TagName1715 = 1717
    TagName1716 = 1718
    TagName1717 = 1719
    TagName1718 = 1720
    TagName1719 = 1721
    TagName1720 = 1722
    TagName1721 = 1723
    TagName1722 = 1724
    TagName1723 = 1725
    TagName1724 = 1726
    TagName1725 = 1727
    TagName1726 = 1728
    TagName1727 = 1729
    TagName1728 = 1730
    TagName1729 = 1731
    TagName1730 = 1732
    TagName1731 = 1733
    TagName1732 = 1734
    TagName1733 = 1735
    TagName1734 = 1736
    TagName1735 = 1737
    TagName1736 = 1738
    TagName1737 = 1739
    TagName1738 = 1740
    TagName1739 = 1741
    TagName1740 = 1742
    TagName1741 = 1743
    TagName1742 = 1744
    TagName1743 = 1745
    TagName1744 = 1746
    TagName1745 = 1747
    TagName1746 = 1748
    TagName1747 = 1749
    TagName1748 = 1750
    TagName1749 = 1751
    TagName1750 = 1752
    TagName1751 = 1753
    TagName1752 = 1754
    TagName1753 = 1755
    TagName1754 = 1756
    TagName1755 = 1757
    TagName1756 = 1758
    TagName1757 = 1759
    TagName1758 = 1760
    TagName1759 = 1761
    TagName1760 = 1762
    TagName1761 = 1763
    TagName1762 = 1764
    TagName1763 = 1765
    TagName1764 = 1766
    TagName1765 = 1767
    TagName1766 = 1768
    TagName1767 = 1769
    TagName1768 = 1770
    TagName1769 = 1771
    TagName1770 = 1772
    TagName1771 = 1773
    TagName1772 = 1774
    TagName1773 = 1775
    TagName1774 = 1776
    TagName1775 = 1777
    TagName1776 = 1778
    TagName1777 = 1779
    TagName1778 = 1780
    TagName1779 = 1781
    TagName1780 = 1782
    TagName1781 = 1783
    TagName1782 = 1784
    TagName1783 = 1785
    TagName1784 = 1786
    TagName1785 = 1787
    TagName1786 = 1788
    TagName1787 = 1789
    TagName1788 = 1790
    TagName1789 = 1791
    TagName1790 = 1792
    TagName1791 = 1793
    TagName1792 = 1794
    TagName1793 = 1795
    TagName1794 = 1796
    TagName1795 = 1797
    TagName1796 = 1798
    TagName1797 = 1799
    TagName1798 = 1800
    TagName1799 = 1801
    TagName1800 = 1802
    TagName1801 = 1803
    TagName1802 = 1804
    TagName1803 = 1805
    TagName1804 = 1806
    TagName1805 = 1807
    TagName1806 = 1808
    TagName1807 = 1809
    TagName1808 = 1810
    TagName1809 = 1811
    TagName1810 = 1812
    TagName1811 = 1813
    TagName1812 = 1814
    TagName1813 = 1815
    TagName1814 = 1816
    TagName1815 = 1817
    TagName1816 = 1818
    TagName1817 = 1819
    TagName1818 = 1820
    TagName1819 = 1821
    TagName1820 = 1822
    TagName1821 = 1823
    TagName1822 = 1824
    TagName1823 = 1825
    TagName1824 = 1826
    TagName1825 = 1827
    TagName1826 = 1828
    TagName1827 = 1829
    TagName1828 = 1830
    TagName1829 = 1831
    TagName1830 = 1832
    TagName1831 = 1833
    TagName1832 = 1834
    TagName1833 = 1835
    TagName1834 = 1836
    TagName1835 = 1837
    TagName1836 = 1838
    TagName1837 = 1839
    TagName1838 = 1840
    TagName1839 = 1841
    TagName1840 = 1842
    TagName1841 = 1843
    TagName1842 = 1844
    TagName1843 = 1845
    TagName1844 = 1846
    TagName1845 = 1847
    TagName1846 = 1848
    TagName1847 = 1849
    TagName1848 = 1850
    TagName1849 = 1851
    TagName1850 = 1852
    TagName1851 = 1853
    TagName1852 = 1854
    TagName1853 = 1855
    TagName1854 = 1856
    TagName1855 = 1857
    TagName1856 = 1858
    TagName1857 = 1859
    TagName1858 = 1860
    TagName1859 = 1861
    TagName1860 = 1862
    TagName1861 = 1863
    TagName1862 = 1864
    TagName1863 = 1865
    TagName1864 = 1866
    TagName1865 = 1867
    TagName1866 = 1868
    TagName1867 = 1869
    TagName1868 = 1870
    TagName1869 = 1871
    TagName1870 = 1872
    TagName1871 = 1873
    TagName1872 = 1874
    TagName1873 = 1875
    TagName1874 = 1876
    TagName1875 = 1877
    TagName1876 = 1878
    TagName1877 = 1879
    TagName1878 = 1880
    TagName1879 = 1881
    TagName1880 = 1882
    TagName1881 = 1883
    TagName1882 = 1884
    TagName1883 = 1885
    TagName1884 = 1886
    TagName1885 = 1887
    TagName1886 = 1888
    TagName1887 = 1889
    TagName1888 = 1890
    TagName1889 = 1891
    TagName1890 = 1892
    TagName1891 = 1893
    TagName1892 = 1894
    TagName1893 = 1895
    TagName1894 = 1896
    TagName1895 = 1897
    TagName1896 = 1898
    TagName1897 = 1899
    TagName1898 = 1900
    TagName1899 = 1901
    TagName1900 = 1902
    TagName1901 = 1903
    TagName1902 = 1904
    TagName1903 = 1905
    TagName1904 = 1906
    TagName1905 = 1907
    TagName1906 = 1908
    TagName1907 = 1909
    TagName1908 = 1910
    TagName1909 = 1911
    TagName1910 = 1912
    TagName1911 = 1913
    TagName1912 = 1914
    TagName1913 = 1915
    TagName1914 = 1916
    TagName1915 = 1917
    TagName1916 = 1918
    TagName1917 = 1919
    TagName1918 = 1920
    TagName1919 = 1921
    TagName1920 = 1922
    TagName1921 = 1923
    TagName1922 = 1924
    TagName1923 = 1925
    TagName1924 = 1926
    TagName1925 = 1927
    TagName1926 = 1928
    TagName1927 = 1929
    TagName1928 = 1930
    TagName1929 = 1931
    TagName1930 = 1932
    TagName1931 = 1933
    TagName1932 = 1934
    TagName1933 = 1935
    TagName1934 = 1936
    TagName1935 = 1937
    TagName1936 = 1938
    TagName1937 = 1939
    TagName1938 = 1940
    TagName1939 = 1941
    TagName1940 = 1942
    TagName1941 = 1943
    TagName1942 = 1944
    TagName1943 = 1945
    TagName1944 = 1946
    TagName1945 = 1947
    TagName1946 = 1948
    TagName1947 = 1949
    TagName1948 = 1950
    TagName1949 = 1951
    TagName1950 = 1952
    TagName1951 = 1953
    TagName1952 = 1954
    TagName1953 = 1955
    TagName1954 = 1956
    TagName1955 = 1957
    TagName1956 = 1958
    TagName1957 = 1959
    TagName1958 = 1960
    TagName1959 = 1961
    TagName1960 = 1962
    TagName1961 = 1963
    TagName1962 = 1964
    TagName1963 = 1965
    TagName1964 = 1966
    TagName1965 = 1967
    TagName1966 = 1968
    TagName1967 = 1969
    TagName1968 = 1970
    TagName1969 = 1971
    TagName1970 = 1972
    TagName1971 = 1973
    TagName1972 = 1974
    TagName1973 = 1975
    TagName1974 = 1976
    TagName1975 = 1977
    TagName1976 = 1978
    TagName1977 = 1979
    TagName1978 = 1980
    TagName1979 = 1981
    TagName1980 = 1982
    TagName1981 = 1983
    TagName1982 = 1984
    TagName1983 = 1985
    TagName1984 = 1986
    TagName1985 = 1987
    TagName1986 = 1988
    TagName1987 = 1989
    TagName1988 = 1990
    TagName1989 = 1991
    TagName1990 = 1992
    TagName1991 = 1993
    TagName1992 = 1994
    TagName1993 = 1995
    TagName1994 = 1996
    TagName1995 = 1997
    TagName1996 = 1998
    TagName1997 = 1999
    TagName1998 = 2000
    TagName1999 = 2001
    TagName2000 = 2002
    TagName2001 = 2003
    TagName2002 = 2004
    TagName2003 = 2005
    TagName2004 = 2006
    TagName2005 = 2007
    TagName2006 = 2008
    TagName2007 = 2009
    TagName2008 = 2010
    TagName2009 = 2011
    TagName2010 = 2012
    TagName2011 = 2013
    TagName2012 = 2014
    TagName2013 = 2015
    TagName2014 = 2016
    TagName2015 = 2017
    TagName2016 = 2018
    TagName2017 = 2019
    TagName2018 = 2020
    TagName2019 = 2021
    TagName2020 = 2022
    TagName2021 = 2023
    TagName2022 = 2024
    TagName2023 = 2025
    TagName2024 = 2026
    TagName2025 = 2027
    TagName2026 = 2028
    TagName2027 = 2029
    TagName2028 = 2030
    TagName2029 = 2031
    TagName2030 = 2032
    TagName2031 = 2033
    TagName2032 = 2034
    TagName2033 = 2035
    TagName2034 = 2036
    TagName2035 = 2037
    TagName2036 = 2038
    TagName2037 = 2039
    TagName2038 = 2040
    TagName2039 = 2041
    TagName2040 = 2042
    TagName2041 = 2043
    TagName2042 = 2044
    TagName2043 = 2045
    TagName2044 = 2046
    TagName2045 = 2047
    TagName2046 = 2048
    TagName2047 = 2049
    TagName2048 = 2050
    TagName2049 = 2051
    TagName2050 = 2052
    TagName2051 = 2053
    TagName2052 = 2054
    TagName2053 = 2055
    TagName2054 = 2056
    TagName2055 = 2057
    TagName2056 = 2058
    TagName2057 = 2059
    TagName2058 = 2060
    TagName2059 = 2061
    TagName2060 = 2062
    TagName2061 = 2063
    TagName2062 = 2064
    TagName2063 = 2065
    TagName2064 = 2066
    TagName2065 = 2067
    TagName2066 = 2068
    TagName2067 = 2069
    TagName2068 = 2070
    TagName2069 = 2071
    TagName2070 = 2072
    TagName2071 = 2073
    TagName2072 = 2074
    TagName2073 = 2075
    TagName2074 = 2076
    TagName2075 = 2077
    TagName2076 = 2078
    TagName2077 = 2079
    TagName2078 = 2080
    TagName2079 = 2081
    TagName2080 = 2082
    TagName2081 = 2083
    TagName2082 = 2084
    TagName2083 = 2085
    TagName2084 = 2086
    TagName2085 = 2087
    TagName2086 = 2088
    TagName2087 = 2089
    TagName2088 = 2090
    TagName2089 = 2091
    TagName2090 = 2092
    TagName2091 = 2093
    TagName2092 = 2094
    TagName2093 = 2095
    TagName2094 = 2096
    TagName2095 = 2097
    TagName2096 = 2098
    TagName2097 = 2099
    TagName2098 = 2100
    TagName2099 = 2101
    TagName2100 = 2102
    TagName2101 = 2103
    TagName2102 = 2104
    TagName2103 = 2105
    TagName2104 = 2106
    TagName2105 = 2107
    TagName2106 = 2108
    TagName2107 = 2109
    TagName2108 = 2110
    TagName2109 = 2111
    TagName2110 = 2112
    TagName2111 = 2113
    TagName2112 = 2114
    TagName2113 = 2115
    TagName2114 = 2116
    TagName2115 = 2117
    TagName2116 = 2118
    TagName2117 = 2119
    TagName2118 = 2120
    TagName2119 = 2121
    TagName2120 = 2122
    TagName2121 = 2123
    TagName2122 = 2124
    TagName2123 = 2125
    TagName2124 = 2126
    TagName2125 = 2127
    TagName2126 = 2128
    TagName2127 = 2129
    TagName2128 = 2130
    TagName2129 = 2131
    TagName2130 = 2132
    TagName2131 = 2133
    TagName2132 = 2134
    TagName2133 = 2135
    TagName2134 = 2136
    TagName2135 = 2137
    TagName2136 = 2138
    TagName2137 = 2139
    TagName2138 = 2140
    TagName2139 = 2141
    TagName2140 = 2142
    TagName2141 = 2143
    TagName2142 = 2144
    TagName2143 = 2145
    TagName2144 = 2146
    TagName2145 = 2147
    TagName2146 = 2148
    TagName2147 = 2149
    TagName2148 = 2150
    TagName2149 = 2151
    TagName2150 = 2152
    TagName2151 = 2153
    TagName2152 = 2154
    TagName2153 = 2155
    TagName2154 = 2156
    TagName2155 = 2157
    TagName2156 = 2158
    TagName2157 = 2159
    TagName2158 = 2160
    TagName2159 = 2161
    TagName2160 = 2162
    TagName2161 = 2163
    TagName2162 = 2164
    TagName2163 = 2165
    TagName2164 = 2166
    TagName2165 = 2167
    TagName2166 = 2168
    TagName2167 = 2169
    TagName2168 = 2170
    TagName2169 = 2171
    TagName2170 = 2172
    TagName2171 = 2173
    TagName2172 = 2174
    TagName2173 = 2175
    TagName2174 = 2176
    TagName2175 = 2177
    TagName2176 = 2178
    TagName2177 = 2179
    TagName2178 = 2180
    TagName2179 = 2181
    TagName2180 = 2182
    TagName2181 = 2183
    TagName2182 = 2184
    TagName2183 = 2185
    TagName2184 = 2186
    TagName2185 = 2187
    TagName2186 = 2188
    TagName2187 = 2189
    TagName2188 = 2190
    TagName2189 = 2191
    TagName2190 = 2192
    TagName2191 = 2193
    TagName2192 = 2194
    TagName2193 = 2195
    TagName2194 = 2196
    TagName2195 = 2197
    TagName2196 = 2198
    TagName2197 = 2199
    TagName2198 = 2200
    TagName2199 = 2201
    TagName2200 = 2202
    TagName2201 = 2203
    TagName2202 = 2204
    TagName2203 = 2205
    TagName2204 = 2206
    TagName2205 = 2207
    TagName2206 = 2208
    TagName2207 = 2209
    TagName2208 = 2210
    TagName2209 = 2211
    TagName2210 = 2212
    TagName2211 = 2213
    TagName2212 = 2214
    TagName2213 = 2215
    TagName2214 = 2216
    TagName2215 = 2217
    TagName2216 = 2218
    TagName2217 = 2219
    TagName2218 = 2220
    TagName2219 = 2221
    TagName2220 = 2222
    TagName2221 = 2223
    TagName2222 = 2224
    TagName2223 = 2225
    TagName2224 = 2226
    TagName2225 = 2227
    TagName2226 = 2228
    TagName2227 = 2229
    TagName2228 = 2230
    TagName2229 = 2231
    TagName2230 = 2232
    TagName2231 = 2233
    TagName2232 = 2234
    TagName2233 = 2235
    TagName2234 = 2236
    TagName2235 = 2237
    TagName2236 = 2238
    TagName2237 = 2239
    TagName2238 = 2240
    TagName2239 = 2241
    TagName2240 = 2242
    TagName2241 = 2243
    TagName2242 = 2244
    TagName2243 = 2245
    TagName2244 = 2246
    TagName2245 = 2247
    TagName2246 = 2248
    TagName2247 = 2249
    TagName2248 = 2250
    TagName2249 = 2251
    TagName2250 = 2252
    TagName2251 = 2253
    TagName2252 = 2254
    TagName2253 = 2255
    TagName2254 = 2256
    TagName2255 = 2257
    TagName2256 = 2258
    TagName2257 = 2259
    TagName2258 = 2260
    TagName2259 = 2261
    TagName2260 = 2262
    TagName2261 = 2263
    TagName2262 = 2264
    TagName2263 = 2265
    TagName2264 = 2266
    TagName2265 = 2267
    TagName2266 = 2268
    TagName2267 = 2269
    TagName2268 = 2270
    TagName2269 = 2271
    TagName2270 = 2272
    TagName2271 = 2273
    TagName2272 = 2274
    TagName2273 = 2275
    TagName2274 = 2276
    TagName2275 = 2277
    TagName2276 = 2278
    TagName2277 = 2279
    TagName2278 = 2280
    TagName2279 = 2281
    TagName2280 = 2282
    TagName2281 = 2283
    TagName2282 = 2284
    TagName2283 = 2285
    TagName2284 = 2286
    TagName2285 = 2287
    TagName2286 = 2288
    TagName2287 = 2289
    TagName2288 = 2290
    TagName2289 = 2291
    TagName2290 = 2292
    TagName2291 = 2293
    TagName2292 = 2294
    TagName2293 = 2295
    TagName2294 = 2296
    TagName2295 = 2297
    TagName2296 = 2298
    TagName2297 = 2299
    TagName2298 = 2300
    TagName2299 = 2301
    TagName2300 = 2302
    TagName2301 = 2303
    TagName2302 = 2304
    TagName2303 = 2305
    TagName2304 = 2306
    TagName2305 = 2307
    TagName2306 = 2308
    TagName2307 = 2309
    TagName2308 = 2310
    TagName2309 = 2311
    TagName2310 = 2312
    TagName2311 = 2313
    TagName2312 = 2314
    TagName2313 = 2315
    TagName2314 = 2316
    TagName2315 = 2317
    TagName2316 = 2318
    TagName2317 = 2319
    TagName2318 = 2320
    TagName2319 = 2321
    TagName2320 = 2322
    TagName2321 = 2323
    TagName2322 = 2324
    TagName2323 = 2325
    TagName2324 = 2326
    TagName2325 = 2327
    TagName2326 = 2328
    TagName2327 = 2329
    TagName2328 = 2330
    TagName2329 = 2331
    TagName2330 = 2332
    TagName2331 = 2333
    TagName2332 = 2334
    TagName2333 = 2335
    TagName2334 = 2336
    TagName2335 = 2337
    TagName2336 = 2338
    TagName2337 = 2339
    TagName2338 = 2340
    TagName2339 = 2341
    TagName2340 = 2342
    TagName2341 = 2343
    TagName2342 = 2344
    TagName2343 = 2345
    TagName2344 = 2346
    TagName2345 = 2347
    TagName2346 = 2348
    TagName2347 = 2349
    TagName2348 = 2350
    TagName2349 = 2351
    TagName2350 = 2352
    TagName2351 = 2353
    TagName2352 = 2354
    TagName2353 = 2355
    TagName2354 = 2356
    TagName2355 = 2357
    TagName2356 = 2358
    TagName2357 = 2359
    TagName2358 = 2360
    TagName2359 = 2361
    TagName2360 = 2362
    TagName2361 = 2363
    TagName2362 = 2364
    TagName2363 = 2365
    TagName2364 = 2366
    TagName2365 = 2367
    TagName2366 = 2368
    TagName2367 = 2369
    TagName2368 = 2370
    TagName2369 = 2371
    TagName2370 = 2372
    TagName2371 = 2373
    TagName2372 = 2374
    TagName2373 = 2375
    TagName2374 = 2376
    TagName2375 = 2377
    TagName2376 = 2378
    TagName2377 = 2379
    TagName2378 = 2380
    TagName2379 = 2381
    TagName2380 = 2382
    TagName2381 = 2383
    TagName2382 = 2384
    TagName2383 = 2385
    TagName2384 = 2386
    TagName2385 = 2387
    TagName2386 = 2388
    TagName2387 = 2389
    TagName2388 = 2390
    TagName2389 = 2391
    TagName2390 = 2392
    TagName2391 = 2393
    TagName2392 = 2394
    TagName2393 = 2395
    TagName2394 = 2396
    TagName2395 = 2397
    TagName2396 = 2398
    TagName2397 = 2399
    TagName2398 = 2400
    TagName2399 = 2401
    TagName2400 = 2402
    TagName2401 = 2403
    TagName2402 = 2404
    TagName2403 = 2405
    TagName2404 = 2406
    TagName2405 = 2407
    TagName2406 = 2408
    TagName2407 = 2409
    TagName2408 = 2410
    TagName2409 = 2411
    TagName2410 = 2412
    TagName2411 = 2413
    TagName2412 = 2414
    TagName2413 = 2415
    TagName2414 = 2416
    TagName2415 = 2417
    TagName2416 = 2418
    TagName2417 = 2419
    TagName2418 = 2420
    TagName2419 = 2421
    TagName2420 = 2422
    TagName2421 = 2423
    TagName2422 = 2424
    TagName2423 = 2425
    TagName2424 = 2426
    TagName2425 = 2427
    TagName2426 = 2428
    TagName2427 = 2429
    TagName2428 = 2430
    TagName2429 = 2431
    TagName2430 = 2432
    TagName2431 = 2433
    TagName2432 = 2434
    TagName2433 = 2435
    TagName2434 = 2436
    TagName2435 = 2437
    TagName2436 = 2438
    TagName2437 = 2439
    TagName2438 = 2440
    TagName2439 = 2441
    TagName2440 = 2442
    TagName2441 = 2443
    TagName2442 = 2444
    TagName2443 = 2445
    TagName2444 = 2446
    TagName2445 = 2447
    TagName2446 = 2448
    TagName2447 = 2449
    TagName2448 = 2450
    TagName2449 = 2451
    TagName2450 = 2452
    TagName2451 = 2453
    TagName2452 = 2454
    TagName2453 = 2455
    TagName2454 = 2456
    TagName2455 = 2457
    TagName2456 = 2458
    TagName2457 = 2459
    TagName2458 = 2460
    TagName2459 = 2461
    TagName2460 = 2462
    TagName2461 = 2463
    TagName2462 = 2464
    TagName2463 = 2465
    TagName2464 = 2466
    TagName2465 = 2467
    TagName2466 = 2468
    TagName2467 = 2469
    TagName2468 = 2470
    TagName2469 = 2471
    TagName2470 = 2472
    TagName2471 = 2473
    TagName2472 = 2474
    TagName2473 = 2475
    TagName2474 = 2476
    TagName2475 = 2477
    TagName2476 = 2478
    TagName2477 = 2479
    TagName2478 = 2480
    TagName2479 = 2481
    TagName2480 = 2482
    TagName2481 = 2483
    TagName2482 = 2484
    TagName2483 = 2485
    TagName2484 = 2486
    TagName2485 = 2487
    TagName2486 = 2488
    TagName2487 = 2489
    TagName2488 = 2490
    TagName2489 = 2491
    TagName2490 = 2492
    TagName2491 = 2493
    TagName2492 = 2494
    TagName2493 = 2495
    TagName2494 = 2496
    TagName2495 = 2497
    TagName2496 = 2498
    TagName2497 = 2499
    TagName2498 = 2500
    TagName2499 = 2501
    TagName2500 = 2502
    TagName2501 = 2503
    TagName2502 = 2504
    TagName2503 = 2505
    TagName2504 = 2506
    TagName2505 = 2507
    TagName2506 = 2508
    TagName2507 = 2509
    TagName2508 = 2510
    TagName2509 = 2511
    TagName2510 = 2512
    TagName2511 = 2513
    TagName2512 = 2514
    TagName2513 = 2515
    TagName2514 = 2516
    TagName2515 = 2517
    TagName2516 = 2518
    TagName2517 = 2519
    TagName2518 = 2520
    TagName2519 = 2521
    TagName2520 = 2522
    TagName2521 = 2523
    TagName2522 = 2524
    TagName2523 = 2525
    TagName2524 = 2526
    TagName2525 = 2527
    TagName2526 = 2528
    TagName2527 = 2529
    TagName2528 = 2530
    TagName2529 = 2531
    TagName2530 = 2532
    TagName2531 = 2533
    TagName2532 = 2534
    TagName2533 = 2535
    TagName2534 = 2536
    TagName2535 = 2537
    TagName2536 = 2538
    TagName2537 = 2539
    TagName2538 = 2540
    TagName2539 = 2541
    TagName2540 = 2542
    TagName2541 = 2543
    TagName2542 = 2544
    TagName2543 = 2545
    TagName2544 = 2546
    TagName2545 = 2547
    TagName2546 = 2548
    TagName2547 = 2549
    TagName2548 = 2550
    TagName2549 = 2551
    TagName2550 = 2552
    TagName2551 = 2553
    TagName2552 = 2554
    TagName2553 = 2555
    TagName2554 = 2556
    TagName2555 = 2557
    TagName2556 = 2558
    TagName2557 = 2559
    TagName2558 = 2560
    TagName2559 = 2561
    TagName2560 = 2562
    TagName2561 = 2563
    TagName2562 = 2564
    TagName2563 = 2565
    TagName2564 = 2566
    TagName2565 = 2567
    TagName2566 = 2568
    TagName2567 = 2569
    TagName2568 = 2570
    TagName2569 = 2571
    TagName2570 = 2572
    TagName2571 = 2573
    TagName2572 = 2574
    TagName2573 = 2575
    TagName2574 = 2576
    TagName2575 = 2577
    TagName2576 = 2578
    TagName2577 = 2579
    TagName2578 = 2580
    TagName2579 = 2581
    TagName2580 = 2582
    TagName2581 = 2583
    TagName2582 = 2584
    TagName2583 = 2585
    TagName2584 = 2586
    TagName2585 = 2587
    TagName2586 = 2588
    TagName2587 = 2589
    TagName2588 = 2590
    TagName2589 = 2591
    TagName2590 = 2592
    TagName2591 = 2593
    TagName2592 = 2594
    TagName2593 = 2595
    TagName2594 = 2596
    TagName2595 = 2597
    TagName2596 = 2598
    TagName2597 = 2599
    TagName2598 = 2600
    TagName2599 = 2601
    TagName2600 = 2602
    TagName2601 = 2603
    TagName2602 = 2604
    TagName2603 = 2605
    TagName2604 = 2606
    TagName2605 = 2607
    TagName2606 = 2608
    TagName2607 = 2609
    TagName2608 = 2610
    TagName2609 = 2611
    TagName2610 = 2612
    TagName2611 = 2613
    TagName2612 = 2614
    TagName2613 = 2615
    TagName2614 = 2616
    TagName2615 = 2617
    TagName2616 = 2618
    TagName2617 = 2619
    TagName2618 = 2620
    TagName2619 = 2621
    TagName2620 = 2622
    TagName2621 = 2623
    TagName2622 = 2624
    TagName2623 = 2625
    TagName2624 = 2626
    TagName2625 = 2627
    TagName2626 = 2628
    TagName2627 = 2629
    TagName2628 = 2630
    TagName2629 = 2631
    TagName2630 = 2632
    TagName2631 = 2633
    TagName2632 = 2634
    TagName2633 = 2635
    TagName2634 = 2636
    TagName2635 = 2637
    TagName2636 = 2638
    TagName2637 = 2639
    TagName2638 = 2640
    TagName2639 = 2641
    TagName2640 = 2642
    TagName2641 = 2643
    TagName2642 = 2644
    TagName2643 = 2645
    TagName2644 = 2646
    TagName2645 = 2647
    TagName2646 = 2648
    TagName2647 = 2649
    TagName2648 = 2650
    TagName2649 = 2651
    TagName2650 = 2652
    TagName2651 = 2653
    TagName2652 = 2654
    TagName2653 = 2655
    TagName2654 = 2656
    TagName2655 = 2657
    TagName2656 = 2658
    TagName2657 = 2659
    TagName2658 = 2660
    TagName2659 = 2661
    TagName2660 = 2662
    TagName2661 = 2663
    TagName2662 = 2664
    TagName2663 = 2665
    TagName2664 = 2666
    TagName2665 = 2667
    TagName2666 = 2668
    TagName2667 = 2669
    TagName2668 = 2670
    TagName2669 = 2671
    TagName2670 = 2672
    TagName2671 = 2673
    TagName2672 = 2674
    TagName2673 = 2675
    TagName2674 = 2676
    TagName2675 = 2677
    TagName2676 = 2678
    TagName2677 = 2679
    TagName2678 = 2680
    TagName2679 = 2681
    TagName2680 = 2682
    TagName2681 = 2683
    TagName2682 = 2684
    TagName2683 = 2685
    TagName2684 = 2686
    TagName2685 = 2687
    TagName2686 = 2688
    TagName2687 = 2689
    TagName2688 = 2690
    TagName2689 = 2691
    TagName2690 = 2692
    TagName2691 = 2693
    TagName2692 = 2694
    TagName2693 = 2695
    TagName2694 = 2696
    TagName2695 = 2697
    TagName2696 = 2698
    TagName2697 = 2699
    TagName2698 = 2700
    TagName2699 = 2701
    TagName2700 = 2702
    TagName2701 = 2703
    TagName2702 = 2704
    TagName2703 = 2705
    TagName2704 = 2706
    TagName2705 = 2707
    TagName2706 = 2708
    TagName2707 = 2709
    TagName2708 = 2710
    TagName2709 = 2711
    TagName2710 = 2712
    TagName2711 = 2713
    TagName2712 = 2714
    TagName2713 = 2715
    TagName2714 = 2716
    TagName2715 = 2717
    TagName2716 = 2718
    TagName2717 = 2719
    TagName2718 = 2720
    TagName2719 = 2721
    TagName2720 = 2722
    TagName2721 = 2723
    TagName2722 = 2724
    TagName2723 = 2725
    TagName2724 = 2726
    TagName2725 = 2727
    TagName2726 = 2728
    TagName2727 = 2729
    TagName2728 = 2730
    TagName2729 = 2731
    TagName2730 = 2732
    TagName2731 = 2733
    TagName2732 = 2734
    TagName2733 = 2735
    TagName2734 = 2736
    TagName2735 = 2737
    TagName2736 = 2738
    TagName2737 = 2739
    TagName2738 = 2740
    TagName2739 = 2741
    TagName2740 = 2742
    TagName2741 = 2743
    TagName2742 = 2744
    TagName2743 = 2745
    TagName2744 = 2746
    TagName2745 = 2747
    TagName2746 = 2748
    TagName2747 = 2749
    TagName2748 = 2750
    TagName2749 = 2751
    TagName2750 = 2752
    TagName2751 = 2753
    TagName2752 = 2754
    TagName2753 = 2755
    TagName2754 = 2756
    TagName2755 = 2757
    TagName2756 = 2758
    TagName2757 = 2759
    TagName2758 = 2760
    TagName2759 = 2761
    TagName2760 = 2762
    TagName2761 = 2763
    TagName2762 = 2764
    TagName2763 = 2765
    TagName2764 = 2766
    TagName2765 = 2767
    TagName2766 = 2768
    TagName2767 = 2769
    TagName2768 = 2770
    TagName2769 = 2771
    TagName2770 = 2772
    TagName2771 = 2773
    TagName2772 = 2774
    TagName2773 = 2775
    TagName2774 = 2776
    TagName2775 = 2777
    TagName2776 = 2778
    TagName2777 = 2779
    TagName2778 = 2780
    TagName2779 = 2781
    TagName2780 = 2782
    TagName2781 = 2783
    TagName2782 = 2784
    TagName2783 = 2785
    TagName2784 = 2786
    TagName2785 = 2787
    TagName2786 = 2788
    TagName2787 = 2789
    TagName2788 = 2790
    TagName2789 = 2791
    TagName2790 = 2792
    TagName2791 = 2793
    TagName2792 = 2794
    TagName2793 = 2795
    TagName2794 = 2796
    TagName2795 = 2797
    TagName2796 = 2798
    TagName2797 = 2799
    TagName2798 = 2800
    TagName2799 = 2801
    TagName2800 = 2802
    TagName2801 = 2803
    TagName2802 = 2804
    TagName2803 = 2805
    TagName2804 = 2806
    TagName2805 = 2807
    TagName2806 = 2808
    TagName2807 = 2809
    TagName2808 = 2810
    TagName2809 = 2811
    TagName2810 = 2812
    TagName2811 = 2813
    TagName2812 = 2814
    TagName2813 = 2815
    TagName2814 = 2816
    TagName2815 = 2817
    TagName2816 = 2818
    TagName2817 = 2819
    TagName2818 = 2820
    TagName2819 = 2821
    TagName2820 = 2822
    TagName2821 = 2823
    TagName2822 = 2824
    TagName2823 = 2825
    TagName2824 = 2826
    TagName2825 = 2827
    TagName2826 = 2828
    TagName2827 = 2829
    TagName2828 = 2830
    TagName2829 = 2831
    TagName2830 = 2832
    TagName2831 = 2833
    TagName2832 = 2834
    TagName2833 = 2835
    TagName2834 = 2836
    TagName2835 = 2837
    TagName2836 = 2838
    TagName2837 = 2839
    TagName2838 = 2840
    TagName2839 = 2841
    TagName2840 = 2842
    TagName2841 = 2843
    TagName2842 = 2844
    TagName2843 = 2845
    TagName2844 = 2846
    TagName2845 = 2847
    TagName2846 = 2848
    TagName2847 = 2849
    TagName2848 = 2850
    TagName2849 = 2851
    TagName2850 = 2852
    TagName2851 = 2853
    TagName2852 = 2854
    TagName2853 = 2855
    TagName2854 = 2856
    TagName2855 = 2857
    TagName2856 = 2858
    TagName2857 = 2859
    TagName2858 = 2860
    TagName2859 = 2861
    TagName2860 = 2862
    TagName2861 = 2863
    TagName2862 = 2864
    TagName2863 = 2865
    TagName2864 = 2866
    TagName2865 = 2867
    TagName2866 = 2868
    TagName2867 = 2869
    TagName2868 = 2870
    TagName2869 = 2871
    TagName2870 = 2872
    TagName2871 = 2873
    TagName2872 = 2874
    TagName2873 = 2875
    TagName2874 = 2876
    TagName2875 = 2877
    TagName2876 = 2878
    TagName2877 = 2879
    TagName2878 = 2880
    TagName2879 = 2881
    TagName2880 = 2882
    TagName2881 = 2883
    TagName2882 = 2884
    TagName2883 = 2885
    TagName2884 = 2886
    TagName2885 = 2887
    TagName2886 = 2888
    TagName2887 = 2889
    TagName2888 = 2890
    TagName2889 = 2891
    TagName2890 = 2892
    TagName2891 = 2893
    TagName2892 = 2894
    TagName2893 = 2895
    TagName2894 = 2896
    TagName2895 = 2897
    TagName2896 = 2898
    TagName2897 = 2899
    TagName2898 = 2900
    TagName2899 = 2901
    TagName2900 = 2902
    TagName2901 = 2903
    TagName2902 = 2904
    TagName2903 = 2905
    TagName2904 = 2906
    TagName2905 = 2907
    TagName2906 = 2908
    TagName2907 = 2909
    TagName2908 = 2910
    TagName2909 = 2911
    TagName2910 = 2912
    TagName2911 = 2913
    TagName2912 = 2914
    TagName2913 = 2915
    TagName2914 = 2916
    TagName2915 = 2917
    TagName2916 = 2918
    TagName2917 = 2919
    TagName2918 = 2920
    TagName2919 = 2921
    TagName2920 = 2922
    TagName2921 = 2923
    TagName2922 = 2924
    TagName2923 = 2925
    TagName2924 = 2926
    TagName2925 = 2927
    TagName2926 = 2928
    TagName2927 = 2929
    TagName2928 = 2930
    TagName2929 = 2931
    TagName2930 = 2932
    TagName2931 = 2933
    TagName2932 = 2934
    TagName2933 = 2935
    TagName2934 = 2936
    TagName2935 = 2937
    TagName2936 = 2938
    TagName2937 = 2939
    TagName2938 = 2940
    TagName2939 = 2941
    TagName2940 = 2942
    TagName2941 = 2943
    TagName2942 = 2944
    TagName2943 = 2945
    TagName2944 = 2946
    TagName2945 = 2947
    TagName2946 = 2948
    TagName2947 = 2949
    TagName2948 = 2950
    TagName2949 = 2951
    TagName2950 = 2952
    TagName2951 = 2953
    TagName2952 = 2954
    TagName2953 = 2955
    TagName2954 = 2956
    TagName2955 = 2957
    TagName2956 = 2958
    TagName2957 = 2959
    TagName2958 = 2960
    TagName2959 = 2961
    TagName2960 = 2962
    TagName2961 = 2963
    TagName2962 = 2964
    TagName2963 = 2965
    TagName2964 = 2966
    TagName2965 = 2967
    TagName2966 = 2968
    TagName2967 = 2969
    TagName2968 = 2970
    TagName2969 = 2971
    TagName2970 = 2972
    TagName2971 = 2973
    TagName2972 = 2974
    TagName2973 = 2975
    TagName2974 = 2976
    TagName2975 = 2977
    TagName2976 = 2978
    TagName2977 = 2979
    TagName2978 = 2980
    TagName2979 = 2981
    TagName2980 = 2982
    TagName2981 = 2983
    TagName2982 = 2984
    TagName2983 = 2985
    TagName2984 = 2986
    TagName2985 = 2987
    TagName2986 = 2988
    TagName2987 = 2989
    TagName2988 = 2990
    TagName2989 = 2991
    TagName2990 = 2992
    TagName2991 = 2993
    TagName2992 = 2994
    TagName2993 = 2995
    TagName2994 = 2996
    TagName2995 = 2997
    TagName2996 = 2998
    TagName2997 = 2999
    TagName2998 = 3000
    TagName2999 = 3001
    TagName3000 = 3002
    TagName3001 = 3003

class Club(IntEnum):
    none = 0
    Engineer = 1
    CleanNClearing = 2
    KnightsHospitaller = 3
    IndeGEHENNA = 4
    IndeMILLENNIUM = 5
    IndeHyakkiyako = 6
    IndeShanhaijing = 7
    IndeTrinity = 8
    FoodService = 9
    Countermeasure = 10
    BookClub = 11
    MatsuriOffice = 12
    GourmetClub = 13
    HoukagoDessert = 14
    RedwinterSecretary = 15
    Schale = 16
    TheSeminar = 17
    AriusSqud = 18
    Justice = 19
    Fuuki = 20
    Kohshinjo68 = 21
    Meihuayuan = 22
    SisterHood = 23
    GameDev = 24
    anzenkyoku = 25
    RemedialClass = 26
    SPTF = 27
    TrinityVigilance = 28
    Veritas = 29
    TrainingClub = 30
    Onmyobu = 31
    Shugyobu = 32
    Endanbou = 33
    NinpoKenkyubu = 34
    Class227 = 35
    EmptyClub = 36
    Emergentology = 37
    RabbitPlatoon = 38
    PandemoniumSociety = 39
    HotSpringsDepartment = 40
    TeaParty = 41
    PublicPeaceBureau = 42
    Genryumon = 43
    BlackTortoisePromenade = 44
    LaborParty = 45
    KnowledgeLiberationFront = 46
    Hyakkayouran = 47
    ShinySparkleSociety = 48
    AbydosStudentCouncil = 49

