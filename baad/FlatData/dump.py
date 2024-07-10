from ..lib.TableEncryptionService import TableEncryptionService


def dump_table(obj) -> list:
    table_encryption = TableEncryptionService()

    typ_name = obj.__class__.__name__[:-5]
    dump_func = next(f for x,f in globals().items() if x.endswith('_' + typ_name))
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
        'MessageTH': table_encryption.convert_string(obj.MessageTH(), password),
        'MessageTW': table_encryption.convert_string(obj.MessageTW(), password),
        'MessageEN': table_encryption.convert_string(obj.MessageEN(), password),
        'MessageDE': table_encryption.convert_string(obj.MessageDE(), password),
        'MessageFR': table_encryption.convert_string(obj.MessageFR(), password),
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
        'MessageTH': table_encryption.convert_string(obj.MessageTH(), password),
        'MessageTW': table_encryption.convert_string(obj.MessageTW(), password),
        'MessageEN': table_encryption.convert_string(obj.MessageEN(), password),
        'MessageDE': table_encryption.convert_string(obj.MessageDE(), password),
        'MessageFR': table_encryption.convert_string(obj.MessageFR(), password),
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
        'MessageTH': table_encryption.convert_string(obj.MessageTH(), password),
        'MessageTW': table_encryption.convert_string(obj.MessageTW(), password),
        'MessageEN': table_encryption.convert_string(obj.MessageEN(), password),
        'MessageDE': table_encryption.convert_string(obj.MessageDE(), password),
        'MessageFR': table_encryption.convert_string(obj.MessageFR(), password),
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
        'MessageTH': table_encryption.convert_string(obj.MessageTH(), password),
        'MessageTW': table_encryption.convert_string(obj.MessageTW(), password),
        'MessageEN': table_encryption.convert_string(obj.MessageEN(), password),
        'MessageDE': table_encryption.convert_string(obj.MessageDE(), password),
        'MessageFR': table_encryption.convert_string(obj.MessageFR(), password),
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
        'RewardGroupId': [table_encryption.convert_long(obj.RewardGroupId(j), password) for j in range(obj.RewardGroupIdLength())],
        'Tags': [Tag(table_encryption.convert_int(obj.Tags(j), password)).name for j in range(obj.TagsLength())],
    }


def dump_AccountLevelExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Level': table_encryption.convert_long(obj.Level(), password),
        'Exp': table_encryption.convert_long(obj.Exp(), password),
        'APAutoChargeMax': table_encryption.convert_long(obj.APAutoChargeMax(), password),
    }


def dump_AddressableBlackListExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'FolderPath': [table_encryption.convert_string(obj.FolderPath(j), password) for j in range(obj.FolderPathLength())],
        'ResourcePath': [table_encryption.convert_string(obj.ResourcePath(j), password) for j in range(obj.ResourcePathLength())],
    }


def dump_AddressableWhiteListExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'FolderPath': [table_encryption.convert_string(obj.FolderPath(j), password) for j in range(obj.FolderPathLength())],
        'ResourcePath': [table_encryption.convert_string(obj.ResourcePath(j), password) for j in range(obj.ResourcePathLength())],
    }


def dump_BlendData(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Type': table_encryption.convert_int(obj.Type(), password),
        'InfoList': [None if obj.InfoList() is None else dump_BlendInfo(obj.InfoList(j), password) for j in range(obj.InfoListLength())],
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
        'DataList': [None if obj.DataList() is None else dump_AniStateData(obj.DataList(j), password) for j in range(obj.DataListLength())],
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
        'Events': [None if obj.Events() is None else dump_AniEventData(obj.Events(j), password) for j in range(obj.EventsLength())],
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
        'UseTSS': obj.UseTSS(),
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


def dump_AttendanceExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Type': AttendanceType(table_encryption.convert_int(obj.Type(), password)).name,
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
        'AudioPriority': table_encryption.convert_int(obj.AudioPriority(), password),
        'AudioClipPath': [table_encryption.convert_string(obj.AudioClipPath(j), password) for j in range(obj.AudioClipPathLength())],
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
    }


def dump_BGMExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'Path': table_encryption.convert_string(obj.Path(), password),
        'Volume': table_encryption.convert_float(obj.Volume(), password),
        'LoopStartTime': table_encryption.convert_float(obj.LoopStartTime(), password),
        'LoopEndTime': table_encryption.convert_float(obj.LoopEndTime(), password),
        'LoopTranstionTime': table_encryption.convert_float(obj.LoopTranstionTime(), password),
        'LoopOffsetTime': table_encryption.convert_float(obj.LoopOffsetTime(), password),
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
    }


def dump_BGM_GlobalExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupBGMId': table_encryption.convert_long(obj.GroupBGMId(), password),
        'BGMIdKr': table_encryption.convert_long(obj.BGMIdKr(), password),
        'BGMIdJp': table_encryption.convert_long(obj.BGMIdJp(), password),
        'BGMIdTh': table_encryption.convert_long(obj.BGMIdTh(), password),
        'BGMIdTw': table_encryption.convert_long(obj.BGMIdTw(), password),
        'BGMIdEn': table_encryption.convert_long(obj.BGMIdEn(), password),
        'BGMIdDe': table_encryption.convert_long(obj.BGMIdDe(), password),
        'BGMIdFr': table_encryption.convert_long(obj.BGMIdFr(), password),
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
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
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


def dump_CafeInteractionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'BubbleType': [BubbleType(table_encryption.convert_int(obj.BubbleType_(j), password)).name for j in range(obj.BubbleTypeLength())],
        'BubbleDuration': [table_encryption.convert_long(obj.BubbleDuration(j), password) for j in range(obj.BubbleDurationLength())],
        'FavorEmoticonRewardParcelType': ParcelType(table_encryption.convert_int(obj.FavorEmoticonRewardParcelType(), password)).name,
        'FavorEmoticonRewardId': table_encryption.convert_long(obj.FavorEmoticonRewardId(), password),
        'FavorEmoticonRewardAmount': table_encryption.convert_long(obj.FavorEmoticonRewardAmount(), password),
        'CafeCharacterState': [CafeCharacterState(table_encryption.convert_int(obj.CafeCharacterState_(j), password)).name for j in range(obj.CafeCharacterStateLength())],
    }


def dump_CafeRankExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Rank': table_encryption.convert_long(obj.Rank(), password),
        'RecipeId': table_encryption.convert_long(obj.RecipeId(), password),
        'ComfortMax': table_encryption.convert_long(obj.ComfortMax(), password),
        'ActionPointProductionCoefficient': table_encryption.convert_long(obj.ActionPointProductionCoefficient(), password),
        'ActionPointProductionCorrectionValue': table_encryption.convert_long(obj.ActionPointProductionCorrectionValue(), password),
        'ActionPointStorageMax': table_encryption.convert_long(obj.ActionPointStorageMax(), password),
        'GoldProductionCoefficient': table_encryption.convert_long(obj.GoldProductionCoefficient(), password),
        'GoldProductionCorrectionValue': table_encryption.convert_long(obj.GoldProductionCorrectionValue(), password),
        'GoldStorageMax': table_encryption.convert_long(obj.GoldStorageMax(), password),
        'TagCountMax': table_encryption.convert_long(obj.TagCountMax(), password),
        'CharacterVisitMin': table_encryption.convert_int(obj.CharacterVisitMin(), password),
        'CharacterVisitMax': table_encryption.convert_int(obj.CharacterVisitMax(), password),
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
        'LeftMargin': table_encryption.convert_float(obj.LeftMargin(), password),
        'BottomMargin': table_encryption.convert_float(obj.BottomMargin(), password),
        'IgnoreEnemies': obj.IgnoreEnemies(),
        'UseRailPointCompensation': obj.UseRailPointCompensation(),
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
        'HardCampaignStageId': [table_encryption.convert_long(obj.HardCampaignStageId(j), password) for j in range(obj.HardCampaignStageIdLength())],
        'VeryHardCampaignStageId': [table_encryption.convert_long(obj.VeryHardCampaignStageId(j), password) for j in range(obj.VeryHardCampaignStageIdLength())],
    }


def dump_CampaignChapterRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ChapterRewardParcelType': [ParcelType(table_encryption.convert_int(obj.ChapterRewardParcelType(j), password)).name for j in range(obj.ChapterRewardParcelTypeLength())],
        'ChapterRewardId': [table_encryption.convert_long(obj.ChapterRewardId(j), password) for j in range(obj.ChapterRewardIdLength())],
        'ChapterRewardAmount': [table_encryption.convert_int(obj.ChapterRewardAmount(j), password) for j in range(obj.ChapterRewardAmountLength())],
    }


def dump_CampaignStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'StageNumber': table_encryption.convert_int(obj.StageNumber(), password),
        'CleardScenarioId': table_encryption.convert_long(obj.CleardScenarioId(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': CurrencyTypes(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
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
        'ContentType': ContentType(table_encryption.convert_int(obj.ContentType_(), password)).name,
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'FirstClearReportEventName': table_encryption.convert_string(obj.FirstClearReportEventName(), password),
        'FirstClearFunnelMessage': table_encryption.convert_string(obj.FirstClearFunnelMessage(), password),
        'FirstClearEventMessage': table_encryption.convert_string(obj.FirstClearEventMessage(), password),
        'TacticRewardExp': table_encryption.convert_long(obj.TacticRewardExp(), password),
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
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
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'IsBoss': obj.IsBoss(),
        'MoveRange': table_encryption.convert_int(obj.MoveRange(), password),
        'AIMoveType': StrategyAIType(table_encryption.convert_int(obj.AIMoveType(), password)).name,
        'Grade': HexaUnitGrade(table_encryption.convert_int(obj.Grade(), password)).name,
        'EnvironmentType': TacticEnvironment(table_encryption.convert_int(obj.EnvironmentType(), password)).name,
        'Scale': table_encryption.convert_float(obj.Scale(), password),
    }


def dump_CharacterAIExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EngageType': EngageType(table_encryption.convert_int(obj.EngageType_(), password)).name,
        'Positioning': PositioningType(table_encryption.convert_int(obj.Positioning(), password)).name,
        'DistanceReduceRatioObstaclePath': table_encryption.convert_long(obj.DistanceReduceRatioObstaclePath(), password),
        'DistanceReduceObstaclePath': table_encryption.convert_long(obj.DistanceReduceObstaclePath(), password),
        'DistanceReduceRatioFormationPath': table_encryption.convert_long(obj.DistanceReduceRatioFormationPath(), password),
        'DistanceReduceFormationPath': table_encryption.convert_long(obj.DistanceReduceFormationPath(), password),
        'MinimumPositionGap': table_encryption.convert_long(obj.MinimumPositionGap(), password),
        'CanUseObstacleOfKneelMotion': obj.CanUseObstacleOfKneelMotion(),
        'CanUseObstacleOfStandMotion': obj.CanUseObstacleOfStandMotion(),
        'HasTargetSwitchingMotion': obj.HasTargetSwitchingMotion(),
    }


def dump_CharacterAcademyTagsExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'FavorTags': [Tag(table_encryption.convert_int(obj.FavorTags(j), password)).name for j in range(obj.FavorTagsLength())],
        'FavorItemTags': [Tag(table_encryption.convert_int(obj.FavorItemTags(j), password)).name for j in range(obj.FavorItemTagsLength())],
        'ForbiddenTags': [Tag(table_encryption.convert_int(obj.ForbiddenTags(j), password)).name for j in range(obj.ForbiddenTagsLength())],
    }


def dump_CharacterCombatSkinExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupId': table_encryption.convert_string(obj.GroupId(), password),
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'ResourcePath': table_encryption.convert_string(obj.ResourcePath(), password),
    }


def dump_CharacterDialogEventExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
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
        'LocalizeTH': table_encryption.convert_string(obj.LocalizeTH(), password),
        'LocalizeTW': table_encryption.convert_string(obj.LocalizeTW(), password),
        'LocalizeEN': table_encryption.convert_string(obj.LocalizeEN(), password),
        'LocalizeDE': table_encryption.convert_string(obj.LocalizeDE(), password),
        'LocalizeFR': table_encryption.convert_string(obj.LocalizeFR(), password),
        'VoiceClipsKr': [table_encryption.convert_string(obj.VoiceClipsKr(j), password) for j in range(obj.VoiceClipsKrLength())],
        'VoiceClipsJp': [table_encryption.convert_string(obj.VoiceClipsJp(j), password) for j in range(obj.VoiceClipsJpLength())],
        'VoiceClipsTh': [table_encryption.convert_string(obj.VoiceClipsTh(j), password) for j in range(obj.VoiceClipsThLength())],
        'VoiceClipsTw': [table_encryption.convert_string(obj.VoiceClipsTw(j), password) for j in range(obj.VoiceClipsTwLength())],
        'VoiceClipsEn': [table_encryption.convert_string(obj.VoiceClipsEn(j), password) for j in range(obj.VoiceClipsEnLength())],
        'VoiceClipsDe': [table_encryption.convert_string(obj.VoiceClipsDe(j), password) for j in range(obj.VoiceClipsDeLength())],
        'VoiceClipsFr': [table_encryption.convert_string(obj.VoiceClipsFr(j), password) for j in range(obj.VoiceClipsFrLength())],
    }


def dump_CharacterDialogExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
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
        'LocalizeTH': table_encryption.convert_string(obj.LocalizeTH(), password),
        'LocalizeTW': table_encryption.convert_string(obj.LocalizeTW(), password),
        'LocalizeEN': table_encryption.convert_string(obj.LocalizeEN(), password),
        'LocalizeDE': table_encryption.convert_string(obj.LocalizeDE(), password),
        'LocalizeFR': table_encryption.convert_string(obj.LocalizeFR(), password),
        'VoiceClipsKr': [table_encryption.convert_string(obj.VoiceClipsKr(j), password) for j in range(obj.VoiceClipsKrLength())],
        'VoiceClipsJp': [table_encryption.convert_string(obj.VoiceClipsJp(j), password) for j in range(obj.VoiceClipsJpLength())],
        'VoiceClipsTh': [table_encryption.convert_string(obj.VoiceClipsTh(j), password) for j in range(obj.VoiceClipsThLength())],
        'VoiceClipsTw': [table_encryption.convert_string(obj.VoiceClipsTw(j), password) for j in range(obj.VoiceClipsTwLength())],
        'VoiceClipsEn': [table_encryption.convert_string(obj.VoiceClipsEn(j), password) for j in range(obj.VoiceClipsEnLength())],
        'VoiceClipsDe': [table_encryption.convert_string(obj.VoiceClipsDe(j), password) for j in range(obj.VoiceClipsDeLength())],
        'VoiceClipsFr': [table_encryption.convert_string(obj.VoiceClipsFr(j), password) for j in range(obj.VoiceClipsFrLength())],
    }


def dump_CharacterExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'CollectionVisible': obj.CollectionVisible(),
        'IsPlayableCharacter': obj.IsPlayableCharacter(),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'Rarity': Rarity(table_encryption.convert_int(obj.Rarity_(), password)).name,
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
        'ScenarioCharacter': table_encryption.convert_string(obj.ScenarioCharacter(), password),
        'SpawnTemplateId': table_encryption.convert_uint(obj.SpawnTemplateId(), password),
        'FavorLevelupType': table_encryption.convert_int(obj.FavorLevelupType(), password),
        'EquipmentSlot': [EquipmentCategory(table_encryption.convert_int(obj.EquipmentSlot(j), password)).name for j in range(obj.EquipmentSlotLength())],
        'SpineResourceName': table_encryption.convert_string(obj.SpineResourceName(), password),
        'SpineResourceNameDiorama': table_encryption.convert_string(obj.SpineResourceNameDiorama(), password),
        'EntityMaterialType': EntityMaterialType(table_encryption.convert_int(obj.EntityMaterialType_(), password)).name,
        'ModelPrefabName': table_encryption.convert_string(obj.ModelPrefabName(), password),
        'TextureDir': table_encryption.convert_string(obj.TextureDir(), password),
        'TextureEchelon': table_encryption.convert_string(obj.TextureEchelon(), password),
        'CollectionTexturePath': table_encryption.convert_string(obj.CollectionTexturePath(), password),
        'CollectionBGTexturePath': table_encryption.convert_string(obj.CollectionBGTexturePath(), password),
        'TextureBoss': table_encryption.convert_string(obj.TextureBoss(), password),
        'TextureSkillCard': [table_encryption.convert_string(obj.TextureSkillCard(j), password) for j in range(obj.TextureSkillCardLength())],
        'WeaponImagePath': table_encryption.convert_string(obj.WeaponImagePath(), password),
        'WeaponLocalizeId': table_encryption.convert_uint(obj.WeaponLocalizeId(), password),
        'DisplayEnemyInfo': obj.DisplayEnemyInfo(),
        'BodyRadius': table_encryption.convert_long(obj.BodyRadius(), password),
        'RandomEffectRadius': table_encryption.convert_long(obj.RandomEffectRadius(), password),
        'HpBarHeight': table_encryption.convert_float(obj.HpBarHeight(), password),
        'HighlightFloaterHeight': table_encryption.convert_float(obj.HighlightFloaterHeight(), password),
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
        'InformationPacel': table_encryption.convert_string(obj.InformationPacel(), password),
        'AnimationSSR': table_encryption.convert_string(obj.AnimationSSR(), password),
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
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'MinimumGradeCharacterWeapon': table_encryption.convert_int(obj.MinimumGradeCharacterWeapon(), password),
        'IsFormConversion': obj.IsFormConversion(),
        'IsRootMotion': obj.IsRootMotion(),
        'IsMoveLeftRight': obj.IsMoveLeftRight(),
        'UseRandomAnimation': obj.UseRandomAnimation(),
        'NormalSkillGroupId': [table_encryption.convert_string(obj.NormalSkillGroupId(j), password) for j in range(obj.NormalSkillGroupIdLength())],
        'ExSkillGroupId': [table_encryption.convert_string(obj.ExSkillGroupId(j), password) for j in range(obj.ExSkillGroupIdLength())],
        'PublicSkillGroupId': [table_encryption.convert_string(obj.PublicSkillGroupId(j), password) for j in range(obj.PublicSkillGroupIdLength())],
        'PassiveSkillGroupId': [table_encryption.convert_string(obj.PassiveSkillGroupId(j), password) for j in range(obj.PassiveSkillGroupIdLength())],
        'LeaderSkillGroupId': [table_encryption.convert_string(obj.LeaderSkillGroupId(j), password) for j in range(obj.LeaderSkillGroupIdLength())],
        'ExtraPassiveSkillGroupId': [table_encryption.convert_string(obj.ExtraPassiveSkillGroupId(j), password) for j in range(obj.ExtraPassiveSkillGroupIdLength())],
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
        'TransSupportStatsFactor': table_encryption.convert_int(obj.TransSupportStatsFactor(), password),
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
        'SkillGroupIdA': [table_encryption.convert_string(obj.SkillGroupIdA(j), password) for j in range(obj.SkillGroupIdALength())],
        'SkillGroupIdB': [table_encryption.convert_string(obj.SkillGroupIdB(j), password) for j in range(obj.SkillGroupIdBLength())],
        'MaxlevelStar': [table_encryption.convert_int(obj.MaxlevelStar(j), password) for j in range(obj.MaxlevelStarLength())],
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
        'PreviousSkillGroupId': [table_encryption.convert_string(obj.PreviousSkillGroupId(j), password) for j in range(obj.PreviousSkillGroupIdLength())],
        'AfterSkillGroupId': [table_encryption.convert_string(obj.AfterSkillGroupId(j), password) for j in range(obj.AfterSkillGroupIdLength())],
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
    }


def dump_ClanChattingEmojiExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ImagePathKr': table_encryption.convert_string(obj.ImagePathKr(), password),
        'ImagePathJp': table_encryption.convert_string(obj.ImagePathJp(), password),
        'ImagePathTh': table_encryption.convert_string(obj.ImagePathTh(), password),
        'ImagePathTw': table_encryption.convert_string(obj.ImagePathTw(), password),
        'ImagePathEn': table_encryption.convert_string(obj.ImagePathEn(), password),
        'ImagePathDe': table_encryption.convert_string(obj.ImagePathDe(), password),
        'ImagePathFr': table_encryption.convert_string(obj.ImagePathFr(), password),
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
        'SuppliesConditionStringId': table_encryption.convert_string(obj.SuppliesConditionStringId(), password),
        'PublicSpeechBubbleOffsetX': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetX(), password),
        'PublicSpeechBubbleOffsetY': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetY(), password),
        'PublicSpeechBubbleOffsetZ': table_encryption.convert_float(obj.PublicSpeechBubbleOffsetZ(), password),
        'PublicSpeechDuration': table_encryption.convert_float(obj.PublicSpeechDuration(), password),
        'ShowRaidListCount': table_encryption.convert_int(obj.ShowRaidListCount(), password),
        'MaxFinalDamage': table_encryption.convert_long(obj.MaxFinalDamage(), password),
        'MaxFinalHeal': table_encryption.convert_long(obj.MaxFinalHeal(), password),
        'MaxRaidTicketCount': table_encryption.convert_long(obj.MaxRaidTicketCount(), password),
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
    }


def dump_ConstCommonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CampaignMainStageMaxRank': table_encryption.convert_int(obj.CampaignMainStageMaxRank(), password),
        'CampaignMainStageBestRecord': table_encryption.convert_int(obj.CampaignMainStageBestRecord(), password),
        'HardAdventurePlayCountRecoverDailyNumber': table_encryption.convert_int(obj.HardAdventurePlayCountRecoverDailyNumber(), password),
        'HardStageCount': table_encryption.convert_int(obj.HardStageCount(), password),
        'EventContentHardStageCount': table_encryption.convert_int(obj.EventContentHardStageCount(), password),
        'TacticRankClearTime': table_encryption.convert_int(obj.TacticRankClearTime(), password),
        'BaseTimeScale': table_encryption.convert_long(obj.BaseTimeScale(), password),
        'GachaPercentage': table_encryption.convert_int(obj.GachaPercentage(), password),
        'AcademyFavorZoneId': table_encryption.convert_long(obj.AcademyFavorZoneId(), password),
        'CafePresetSlotCount': table_encryption.convert_int(obj.CafePresetSlotCount(), password),
        'CafeMonologueIntervalMillisec': table_encryption.convert_long(obj.CafeMonologueIntervalMillisec(), password),
        'CafeMonologueDefaultDuration': table_encryption.convert_long(obj.CafeMonologueDefaultDuration(), password),
        'CafeBubbleIdleDurationMilliSec': table_encryption.convert_long(obj.CafeBubbleIdleDurationMilliSec(), password),
        'FindGiftTimeLimit': table_encryption.convert_int(obj.FindGiftTimeLimit(), password),
        'CafeVisitProbabilityBase': table_encryption.convert_int(obj.CafeVisitProbabilityBase(), password),
        'CafeVisitProbabilityTagBonus': table_encryption.convert_int(obj.CafeVisitProbabilityTagBonus(), password),
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
        'CraftTicketItemUniqueId': table_encryption.convert_int(obj.CraftTicketItemUniqueId(), password),
        'CraftTicketConsumeAmount': table_encryption.convert_int(obj.CraftTicketConsumeAmount(), password),
        'AcademyTicketCost': table_encryption.convert_int(obj.AcademyTicketCost(), password),
        'MassangerMessageExpireDay': table_encryption.convert_int(obj.MassangerMessageExpireDay(), password),
        'CraftLeafNodeGenerateLv1Count': table_encryption.convert_int(obj.CraftLeafNodeGenerateLv1Count(), password),
        'CraftLeafNodeGenerateLv2Count': table_encryption.convert_int(obj.CraftLeafNodeGenerateLv2Count(), password),
        'TutorialGachaShopId': table_encryption.convert_int(obj.TutorialGachaShopId(), password),
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
        'EventStrategyPlayTimeLimitInSeconds': table_encryption.convert_long(obj.EventStrategyPlayTimeLimitInSeconds(), password),
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
        'FormationCollider01OffsetX': table_encryption.convert_long(obj.FormationCollider01OffsetX(), password),
        'FormationCollider01OffsetY': table_encryption.convert_long(obj.FormationCollider01OffsetY(), password),
        'FormationCollider01OffsetZ': table_encryption.convert_long(obj.FormationCollider01OffsetZ(), password),
        'FormationCollider01SizeX': table_encryption.convert_long(obj.FormationCollider01SizeX(), password),
        'FormationCollider01SizeY': table_encryption.convert_long(obj.FormationCollider01SizeY(), password),
        'FormationCollider01SizeZ': table_encryption.convert_long(obj.FormationCollider01SizeZ(), password),
        'FormationCollider02OffsetX': table_encryption.convert_long(obj.FormationCollider02OffsetX(), password),
        'FormationCollider02OffsetY': table_encryption.convert_long(obj.FormationCollider02OffsetY(), password),
        'FormationCollider02OffsetZ': table_encryption.convert_long(obj.FormationCollider02OffsetZ(), password),
        'FormationCollider02SizeX': table_encryption.convert_long(obj.FormationCollider02SizeX(), password),
        'FormationCollider02SizeY': table_encryption.convert_long(obj.FormationCollider02SizeY(), password),
        'FormationCollider02SizeZ': table_encryption.convert_long(obj.FormationCollider02SizeZ(), password),
        'FormationCollider03OffsetX': table_encryption.convert_long(obj.FormationCollider03OffsetX(), password),
        'FormationCollider03OffsetY': table_encryption.convert_long(obj.FormationCollider03OffsetY(), password),
        'FormationCollider03OffsetZ': table_encryption.convert_long(obj.FormationCollider03OffsetZ(), password),
        'FormationCollider03SizeX': table_encryption.convert_long(obj.FormationCollider03SizeX(), password),
        'FormationCollider03SizeY': table_encryption.convert_long(obj.FormationCollider03SizeY(), password),
        'FormationCollider03SizeZ': table_encryption.convert_long(obj.FormationCollider03SizeZ(), password),
        'ShowFurnitureTag': obj.ShowFurnitureTag(),
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
        'MasterCoinItemId': table_encryption.convert_long(obj.MasterCoinItemId(), password),
        'CallnameLengthEn': table_encryption.convert_int(obj.CallnameLengthEn(), password),
        'CallnameLengthKr': table_encryption.convert_int(obj.CallnameLengthKr(), password),
        'NicknameLengthKr': table_encryption.convert_int(obj.NicknameLengthKr(), password),
        'ClanNameLength': table_encryption.convert_int(obj.ClanNameLength(), password),
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


def dump_ContentsScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'LocalizeId': table_encryption.convert_uint(obj.LocalizeId(), password),
        'ScenarioContentType': ScenarioContentType(table_encryption.convert_int(obj.ScenarioContentType_(), password)).name,
        'ScenarioGroupId': [table_encryption.convert_long(obj.ScenarioGroupId(j), password) for j in range(obj.ScenarioGroupIdLength())],
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


def dump_CumulativeTimeRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Description': table_encryption.convert_string(obj.Description(), password),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'TimeCondition': [table_encryption.convert_long(obj.TimeCondition(j), password) for j in range(obj.TimeConditionLength())],
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardId': [table_encryption.convert_long(obj.RewardId(j), password) for j in range(obj.RewardIdLength())],
        'RewardAmount': [table_encryption.convert_int(obj.RewardAmount(j), password) for j in range(obj.RewardAmountLength())],
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
        'DailyRefillAmount': table_encryption.convert_long(obj.DailyRefillAmount(), password),
        'DailyRefillTime': [table_encryption.convert_long(obj.DailyRefillTime(j), password) for j in range(obj.DailyRefillTimeLength())],
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
        'CraftQuality': table_encryption.convert_long(obj.CraftQuality(), password),
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
        'SkillGroupId': table_encryption.convert_string(obj.SkillGroupId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
        'SpriteName': table_encryption.convert_string(obj.SpriteName(), password),
        'BuffDescriptionLocalizeCodeId': table_encryption.convert_string(obj.BuffDescriptionLocalizeCodeId(), password),
        'BuffDescriptionIconPath': table_encryption.convert_string(obj.BuffDescriptionIconPath(), password),
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
        'EventContentBuffId2': table_encryption.convert_long(obj.EventContentBuffId2(), password),
        'BuffNameLocalizeCodeId2': table_encryption.convert_string(obj.BuffNameLocalizeCodeId2(), password),
        'EventContentDebuffId': table_encryption.convert_long(obj.EventContentDebuffId(), password),
        'DebuffNameLocalizeCodeId': table_encryption.convert_string(obj.DebuffNameLocalizeCodeId(), password),
        'BuffGroupProb': table_encryption.convert_long(obj.BuffGroupProb(), password),
    }


def dump_EventContentCardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CardGroupId': table_encryption.convert_int(obj.CardGroupId(), password),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'IconPath': table_encryption.convert_string(obj.IconPath(), password),
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
        'IsLegacy': obj.IsLegacy(),
        'CardGroupId': table_encryption.convert_int(obj.CardGroupId(), password),
        'RefreshGroup': table_encryption.convert_int(obj.RefreshGroup(), password),
        'Prob': table_encryption.convert_int(obj.Prob(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_long(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
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
        'UnlockConditionType': EventCollectionUnlockType(table_encryption.convert_int(obj.UnlockConditionType(), password)).name,
        'UnlockConditionParameter': table_encryption.convert_long(obj.UnlockConditionParameter(), password),
        'UnlockConditionCount': table_encryption.convert_long(obj.UnlockConditionCount(), password),
        'IsObject': obj.IsObject(),
        'IsHorizon': obj.IsHorizon(),
        'ThumbResource': table_encryption.convert_string(obj.ThumbResource(), password),
        'FullResource': table_encryption.convert_string(obj.FullResource(), password),
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


def dump_EventContentExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'DevName': table_encryption.convert_string(obj.DevName(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'BgImagePath': table_encryption.convert_string(obj.BgImagePath(), password),
    }


def dump_EventContentMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'GroupName': table_encryption.convert_string(obj.GroupName(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_string(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ViewFlag': obj.ViewFlag(),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterName': [table_encryption.convert_string(obj.CompleteConditionParameterName(j), password) for j in range(obj.CompleteConditionParameterNameLength())],
        'RewardIcon': table_encryption.convert_string(obj.RewardIcon(), password),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
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
        'Order': table_encryption.convert_long(obj.Order(), password),
        'RecollectionNumber': table_encryption.convert_long(obj.RecollectionNumber(), password),
        'IsRecollection': obj.IsRecollection(),
        'ScenarioGroupId': [table_encryption.convert_long(obj.ScenarioGroupId(j), password) for j in range(obj.ScenarioGroupIdLength())],
        'ScenarioConditionType': EventContentScenarioConditionType(table_encryption.convert_int(obj.ScenarioConditionType(), password)).name,
        'ConditionAmount': table_encryption.convert_long(obj.ConditionAmount(), password),
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
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventContentType': EventContentType(table_encryption.convert_int(obj.EventContentType_(), password)).name,
        'OpenConditionContent': OpenConditionContent(table_encryption.convert_int(obj.OpenConditionContent_(), password)).name,
        'ContentLockType': ContentLockType(table_encryption.convert_int(obj.ContentLockType_(), password)).name,
        'EventDisplay': obj.EventDisplay(),
        'EventItemId': table_encryption.convert_long(obj.EventItemId(), password),
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
    }


def dump_EventContentShopInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'LocalizeCode': table_encryption.convert_uint(obj.LocalizeCode(), password),
        'CostParcelType': ParcelType(table_encryption.convert_int(obj.CostParcelType(), password)).name,
        'CostParcelId': table_encryption.convert_long(obj.CostParcelId(), password),
        'IsRefresh': obj.IsRefresh(),
        'AutoRefreshCoolTime': table_encryption.convert_long(obj.AutoRefreshCoolTime(), password),
        'RefreshAbleCount': table_encryption.convert_long(obj.RefreshAbleCount(), password),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'OpenPeriodFrom': table_encryption.convert_string(obj.OpenPeriodFrom(), password),
        'OpenPeriodTo': table_encryption.convert_string(obj.OpenPeriodTo(), password),
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
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'SpineOffsetX': table_encryption.convert_float(obj.SpineOffsetX(), password),
        'SpineOffsetY': table_encryption.convert_float(obj.SpineOffsetY(), password),
        'DialogOffsetX': table_encryption.convert_float(obj.DialogOffsetX(), password),
        'DialogOffsetY': table_encryption.convert_float(obj.DialogOffsetY(), password),
    }


def dump_EventContentStageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Name': table_encryption.convert_string(obj.Name(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'StageDifficulty': StageDifficulty(table_encryption.convert_int(obj.StageDifficulty_(), password)).name,
        'StageNumber': table_encryption.convert_int(obj.StageNumber(), password),
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
        'ChallengeDisplay': obj.ChallengeDisplay(),
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


def dump_FixedEchelonSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'FixedEchelonID': table_encryption.convert_long(obj.FixedEchelonID(), password),
        'MainLeaderSlot': table_encryption.convert_int(obj.MainLeaderSlot(), password),
        'MainCharacterID': [table_encryption.convert_long(obj.MainCharacterID(j), password) for j in range(obj.MainCharacterIDLength())],
        'MainLevel': [table_encryption.convert_int(obj.MainLevel(j), password) for j in range(obj.MainLevelLength())],
        'MainGrade': [table_encryption.convert_int(obj.MainGrade(j), password) for j in range(obj.MainGradeLength())],
        'MainExSkillLevel': [table_encryption.convert_int(obj.MainExSkillLevel(j), password) for j in range(obj.MainExSkillLevelLength())],
        'MainNoneExSkillLevel': [table_encryption.convert_int(obj.MainNoneExSkillLevel(j), password) for j in range(obj.MainNoneExSkillLevelLength())],
        'MainEquipment1ID': [table_encryption.convert_long(obj.MainEquipment1ID(j), password) for j in range(obj.MainEquipment1IDLength())],
        'MainEquipment1Level': [table_encryption.convert_int(obj.MainEquipment1Level(j), password) for j in range(obj.MainEquipment1LevelLength())],
        'MainEquipment2ID': [table_encryption.convert_long(obj.MainEquipment2ID(j), password) for j in range(obj.MainEquipment2IDLength())],
        'MainEquipment2Level': [table_encryption.convert_int(obj.MainEquipment2Level(j), password) for j in range(obj.MainEquipment2LevelLength())],
        'MainEquipment3ID': [table_encryption.convert_long(obj.MainEquipment3ID(j), password) for j in range(obj.MainEquipment3IDLength())],
        'MainEquipment3Level': [table_encryption.convert_int(obj.MainEquipment3Level(j), password) for j in range(obj.MainEquipment3LevelLength())],
        'SupportCharacterID': [table_encryption.convert_long(obj.SupportCharacterID(j), password) for j in range(obj.SupportCharacterIDLength())],
        'SupportLevel': [table_encryption.convert_int(obj.SupportLevel(j), password) for j in range(obj.SupportLevelLength())],
        'SupportGrade': [table_encryption.convert_int(obj.SupportGrade(j), password) for j in range(obj.SupportGradeLength())],
        'SupportExSkillLevel': [table_encryption.convert_int(obj.SupportExSkillLevel(j), password) for j in range(obj.SupportExSkillLevelLength())],
        'SupportNoneExSkillLevel': [table_encryption.convert_int(obj.SupportNoneExSkillLevel(j), password) for j in range(obj.SupportNoneExSkillLevelLength())],
        'SupportEquipment1ID': [table_encryption.convert_long(obj.SupportEquipment1ID(j), password) for j in range(obj.SupportEquipment1IDLength())],
        'SupportEquipment1Level': [table_encryption.convert_int(obj.SupportEquipment1Level(j), password) for j in range(obj.SupportEquipment1LevelLength())],
        'SupportEquipment2ID': [table_encryption.convert_long(obj.SupportEquipment2ID(j), password) for j in range(obj.SupportEquipment2IDLength())],
        'SupportEquipment2Level': [table_encryption.convert_int(obj.SupportEquipment2Level(j), password) for j in range(obj.SupportEquipment2LevelLength())],
        'SupportEquipment3ID': [table_encryption.convert_long(obj.SupportEquipment3ID(j), password) for j in range(obj.SupportEquipment3IDLength())],
        'SupportEquipment3Level': [table_encryption.convert_int(obj.SupportEquipment3Level(j), password) for j in range(obj.SupportEquipment3LevelLength())],
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
        'CraftQuality': table_encryption.convert_long(obj.CraftQuality(), password),
        'EventCollectionId': table_encryption.convert_long(obj.EventCollectionId(), password),
        'EventCollectionBubbleOffsetX': table_encryption.convert_long(obj.EventCollectionBubbleOffsetX(), password),
        'EventCollectionBubbleOffsetY': table_encryption.convert_long(obj.EventCollectionBubbleOffsetY(), password),
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'CafeCharacterState': [CafeCharacterState(table_encryption.convert_int(obj.CafeCharacterState_(j), password)).name for j in range(obj.CafeCharacterStateLength())],
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


def dump_GachaCraftNodeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'Tier': table_encryption.convert_long(obj.Tier(), password),
        'Tag': [Tag(table_encryption.convert_int(obj.Tag_(j), password)).name for j in range(obj.TagLength())],
        'NodeQuality': table_encryption.convert_long(obj.NodeQuality(), password),
        'Lv1Exp': table_encryption.convert_long(obj.Lv1Exp(), password),
        'Lv2Exp': table_encryption.convert_long(obj.Lv2Exp(), password),
        'Icon': table_encryption.convert_string(obj.Icon(), password),
        'LocalizeKey': table_encryption.convert_uint(obj.LocalizeKey(), password),
        'Lv1Property': table_encryption.convert_long(obj.Lv1Property(), password),
        'Lv2Property': table_encryption.convert_long(obj.Lv2Property(), password),
        'GP100': table_encryption.convert_int(obj.GP100(), password),
        'GP101': table_encryption.convert_int(obj.GP101(), password),
        'GP102': table_encryption.convert_int(obj.GP102(), password),
        'GP103': table_encryption.convert_int(obj.GP103(), password),
        'GP120': table_encryption.convert_int(obj.GP120(), password),
        'GP121': table_encryption.convert_int(obj.GP121(), password),
        'GP122': table_encryption.convert_int(obj.GP122(), password),
        'GP123': table_encryption.convert_int(obj.GP123(), password),
        'GP140': table_encryption.convert_int(obj.GP140(), password),
        'GP141': table_encryption.convert_int(obj.GP141(), password),
        'GP142': table_encryption.convert_int(obj.GP142(), password),
        'GP143': table_encryption.convert_int(obj.GP143(), password),
        'GP130': table_encryption.convert_int(obj.GP130(), password),
        'GP131': table_encryption.convert_int(obj.GP131(), password),
        'GP132': table_encryption.convert_int(obj.GP132(), password),
        'GP133': table_encryption.convert_int(obj.GP133(), password),
        'GP112': table_encryption.convert_int(obj.GP112(), password),
        'GP151': table_encryption.convert_int(obj.GP151(), password),
        'GP152': table_encryption.convert_int(obj.GP152(), password),
        'GP153': table_encryption.convert_int(obj.GP153(), password),
        'GP2100': table_encryption.convert_int(obj.GP2100(), password),
        'GP2101': table_encryption.convert_int(obj.GP2101(), password),
        'GP2102': table_encryption.convert_int(obj.GP2102(), password),
        'GP2103': table_encryption.convert_int(obj.GP2103(), password),
        'GP2000': table_encryption.convert_int(obj.GP2000(), password),
        'GP2001': table_encryption.convert_int(obj.GP2001(), password),
        'GP2002': table_encryption.convert_int(obj.GP2002(), password),
        'GP2003': table_encryption.convert_int(obj.GP2003(), password),
        'GP2004': table_encryption.convert_int(obj.GP2004(), password),
        'GP2005': table_encryption.convert_int(obj.GP2005(), password),
        'GP2006': table_encryption.convert_int(obj.GP2006(), password),
        'GP2007': table_encryption.convert_int(obj.GP2007(), password),
        'GP2008': table_encryption.convert_int(obj.GP2008(), password),
        'GP2009': table_encryption.convert_int(obj.GP2009(), password),
        'GP1100': table_encryption.convert_int(obj.GP1100(), password),
        'GP1101': table_encryption.convert_int(obj.GP1101(), password),
        'GP1102': table_encryption.convert_int(obj.GP1102(), password),
        'GP1103': table_encryption.convert_int(obj.GP1103(), password),
        'GP1104': table_encryption.convert_int(obj.GP1104(), password),
        'GP1105': table_encryption.convert_int(obj.GP1105(), password),
        'GP1106': table_encryption.convert_int(obj.GP1106(), password),
        'GP1107': table_encryption.convert_int(obj.GP1107(), password),
        'GP1108': table_encryption.convert_int(obj.GP1108(), password),
        'GP1109': table_encryption.convert_int(obj.GP1109(), password),
        'GP1110': table_encryption.convert_int(obj.GP1110(), password),
        'GP1111': table_encryption.convert_int(obj.GP1111(), password),
        'GP1112': table_encryption.convert_int(obj.GP1112(), password),
        'GP1000': table_encryption.convert_int(obj.GP1000(), password),
        'GP1001': table_encryption.convert_int(obj.GP1001(), password),
        'GP1002': table_encryption.convert_int(obj.GP1002(), password),
        'GP1003': table_encryption.convert_int(obj.GP1003(), password),
        'GP1004': table_encryption.convert_int(obj.GP1004(), password),
        'GP1005': table_encryption.convert_int(obj.GP1005(), password),
        'GP1007': table_encryption.convert_int(obj.GP1007(), password),
        'GP1008': table_encryption.convert_int(obj.GP1008(), password),
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
        'ConsumeCondition': [table_encryption.convert_string(obj.ConsumeCondition(j), password) for j in range(obj.ConsumeConditionLength())],
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
        'EnemyArmorType': ArmorType(table_encryption.convert_int(obj.EnemyArmorType(), password)).name,
        'LevelMinion': table_encryption.convert_long(obj.LevelMinion(), password),
        'LevelElite': table_encryption.convert_long(obj.LevelElite(), password),
        'LevelChampion': table_encryption.convert_long(obj.LevelChampion(), password),
        'LevelBoss': table_encryption.convert_long(obj.LevelBoss(), password),
        'ObstacleLevel': table_encryption.convert_long(obj.ObstacleLevel(), password),
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
        'TSSAirUnitHeight': table_encryption.convert_long(obj.TSSAirUnitHeight(), password),
        'IsRaid': obj.IsRaid(),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'WarningUI': obj.WarningUI(),
        'TSSHatchOpen': obj.TSSHatchOpen(),
    }


def dump_GroundGridFlat(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'X': table_encryption.convert_int(obj.X(), password),
        'Y': table_encryption.convert_int(obj.Y(), password),
        'StartX': table_encryption.convert_float(obj.StartX(), password),
        'StartY': table_encryption.convert_float(obj.StartY(), password),
        'Gap': table_encryption.convert_float(obj.Gap(), password),
        'Nodes': [None if obj.Nodes() is None else dump_GroundNodeFlat(obj.Nodes(j), password) for j in range(obj.NodesLength())],
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


def dump_GuideMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'SeasonId': table_encryption.convert_long(obj.SeasonId(), password),
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'LoginCount': table_encryption.convert_long(obj.LoginCount(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'Description': table_encryption.convert_string(obj.Description(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterName': table_encryption.convert_string(obj.CompleteConditionParameterName(), password),
        'MissionRewardParcelType': [ParcelType(table_encryption.convert_int(obj.MissionRewardParcelType(j), password)).name for j in range(obj.MissionRewardParcelTypeLength())],
        'MissionRewardParcelId': [table_encryption.convert_long(obj.MissionRewardParcelId(j), password) for j in range(obj.MissionRewardParcelIdLength())],
        'MissionRewardAmount': [table_encryption.convert_int(obj.MissionRewardAmount(j), password) for j in range(obj.MissionRewardAmountLength())],
    }


def dump_GuideMissionSeasonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'TitleLocalizeCode': table_encryption.convert_string(obj.TitleLocalizeCode(), password),
        'InfomationLocalizeCode': table_encryption.convert_string(obj.InfomationLocalizeCode(), password),
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'Enabled': obj.Enabled(),
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
    }


def dump_HpBarAbbreviationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'MonsterLv': table_encryption.convert_int(obj.MonsterLv(), password),
        'StandardHpBar': table_encryption.convert_int(obj.StandardHpBar(), password),
        'RaidBossHpBar': table_encryption.convert_int(obj.RaidBossHpBar(), password),
    }


def dump_InformationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupID': table_encryption.convert_long(obj.GroupID(), password),
        'PageName': table_encryption.convert_string(obj.PageName(), password),
        'TutorialParentName': [table_encryption.convert_string(obj.TutorialParentName(j), password) for j in range(obj.TutorialParentNameLength())],
        'UIName': [table_encryption.convert_string(obj.UIName(j), password) for j in range(obj.UINameLength())],
    }


def dump_InformationStrategyObjectExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'PageName': table_encryption.convert_string(obj.PageName(), password),
    }


def dump_ItemExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
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
        'CraftQuality': table_encryption.convert_long(obj.CraftQuality(), password),
        'ShopCategory': [ShopCategoryType(table_encryption.convert_int(obj.ShopCategory(j), password)).name for j in range(obj.ShopCategoryLength())],
        'ExpirationDateTime': table_encryption.convert_string(obj.ExpirationDateTime(), password),
        'ShortcutTypeId': table_encryption.convert_long(obj.ShortcutTypeId(), password),
        'IsThreeGachaItem': obj.IsThreeGachaItem(),
    }


def dump_KatakanaConvertExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
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
        'StageNumber': table_encryption.convert_int(obj.StageNumber(), password),
        'StageDisplay': table_encryption.convert_int(obj.StageDisplay(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'OpenDate': table_encryption.convert_long(obj.OpenDate(), password),
        'OpenEventPoint': table_encryption.convert_long(obj.OpenEventPoint(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'StageEnterCostType': CurrencyTypes(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
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


def dump_LoadingImageExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'ImagePathKr': table_encryption.convert_string(obj.ImagePathKr(), password),
        'ImagePathJp': table_encryption.convert_string(obj.ImagePathJp(), password),
        'ImagePathTh': table_encryption.convert_string(obj.ImagePathTh(), password),
        'ImagePathTw': table_encryption.convert_string(obj.ImagePathTw(), password),
        'ImagePathEn': table_encryption.convert_string(obj.ImagePathEn(), password),
        'ImagePathDe': table_encryption.convert_string(obj.ImagePathDe(), password),
        'ImagePathFr': table_encryption.convert_string(obj.ImagePathFr(), password),
        'DisplayWeight': table_encryption.convert_int(obj.DisplayWeight(), password),
    }


def dump_LocalizeCharProfileExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'StatusMessageKr': table_encryption.convert_string(obj.StatusMessageKr(), password),
        'StatusMessageJp': table_encryption.convert_string(obj.StatusMessageJp(), password),
        'StatusMessageTh': table_encryption.convert_string(obj.StatusMessageTh(), password),
        'StatusMessageTw': table_encryption.convert_string(obj.StatusMessageTw(), password),
        'StatusMessageEn': table_encryption.convert_string(obj.StatusMessageEn(), password),
        'StatusMessageDe': table_encryption.convert_string(obj.StatusMessageDe(), password),
        'StatusMessageFr': table_encryption.convert_string(obj.StatusMessageFr(), password),
        'FullNameKr': table_encryption.convert_string(obj.FullNameKr(), password),
        'FullNameJp': table_encryption.convert_string(obj.FullNameJp(), password),
        'FullNameTh': table_encryption.convert_string(obj.FullNameTh(), password),
        'FullNameTw': table_encryption.convert_string(obj.FullNameTw(), password),
        'FullNameEn': table_encryption.convert_string(obj.FullNameEn(), password),
        'FullNameDe': table_encryption.convert_string(obj.FullNameDe(), password),
        'FullNameFr': table_encryption.convert_string(obj.FullNameFr(), password),
        'FamilyNameKr': table_encryption.convert_string(obj.FamilyNameKr(), password),
        'FamilyNameRubyKr': table_encryption.convert_string(obj.FamilyNameRubyKr(), password),
        'PersonalNameKr': table_encryption.convert_string(obj.PersonalNameKr(), password),
        'PersonalNameRubyKr': table_encryption.convert_string(obj.PersonalNameRubyKr(), password),
        'FamilyNameJp': table_encryption.convert_string(obj.FamilyNameJp(), password),
        'FamilyNameRubyJp': table_encryption.convert_string(obj.FamilyNameRubyJp(), password),
        'PersonalNameJp': table_encryption.convert_string(obj.PersonalNameJp(), password),
        'PersonalNameRubyJp': table_encryption.convert_string(obj.PersonalNameRubyJp(), password),
        'FamilyNameTh': table_encryption.convert_string(obj.FamilyNameTh(), password),
        'FamilyNameRubyTh': table_encryption.convert_string(obj.FamilyNameRubyTh(), password),
        'PersonalNameTh': table_encryption.convert_string(obj.PersonalNameTh(), password),
        'PersonalNameRubyTh': table_encryption.convert_string(obj.PersonalNameRubyTh(), password),
        'FamilyNameTw': table_encryption.convert_string(obj.FamilyNameTw(), password),
        'FamilyNameRubyTw': table_encryption.convert_string(obj.FamilyNameRubyTw(), password),
        'PersonalNameTw': table_encryption.convert_string(obj.PersonalNameTw(), password),
        'PersonalNameRubyTw': table_encryption.convert_string(obj.PersonalNameRubyTw(), password),
        'FamilyNameEn': table_encryption.convert_string(obj.FamilyNameEn(), password),
        'FamilyNameRubyEn': table_encryption.convert_string(obj.FamilyNameRubyEn(), password),
        'PersonalNameEn': table_encryption.convert_string(obj.PersonalNameEn(), password),
        'PersonalNameRubyEn': table_encryption.convert_string(obj.PersonalNameRubyEn(), password),
        'FamilyNameDe': table_encryption.convert_string(obj.FamilyNameDe(), password),
        'FamilyNameRubyDe': table_encryption.convert_string(obj.FamilyNameRubyDe(), password),
        'PersonalNameDe': table_encryption.convert_string(obj.PersonalNameDe(), password),
        'PersonalNameRubyDe': table_encryption.convert_string(obj.PersonalNameRubyDe(), password),
        'FamilyNameFr': table_encryption.convert_string(obj.FamilyNameFr(), password),
        'FamilyNameRubyFr': table_encryption.convert_string(obj.FamilyNameRubyFr(), password),
        'PersonalNameFr': table_encryption.convert_string(obj.PersonalNameFr(), password),
        'PersonalNameRubyFr': table_encryption.convert_string(obj.PersonalNameRubyFr(), password),
        'SchoolYearKr': table_encryption.convert_string(obj.SchoolYearKr(), password),
        'SchoolYearJp': table_encryption.convert_string(obj.SchoolYearJp(), password),
        'SchoolYearTh': table_encryption.convert_string(obj.SchoolYearTh(), password),
        'SchoolYearTw': table_encryption.convert_string(obj.SchoolYearTw(), password),
        'SchoolYearEn': table_encryption.convert_string(obj.SchoolYearEn(), password),
        'SchoolYearDe': table_encryption.convert_string(obj.SchoolYearDe(), password),
        'SchoolYearFr': table_encryption.convert_string(obj.SchoolYearFr(), password),
        'CharacterAgeKr': table_encryption.convert_string(obj.CharacterAgeKr(), password),
        'CharacterAgeJp': table_encryption.convert_string(obj.CharacterAgeJp(), password),
        'CharacterAgeTh': table_encryption.convert_string(obj.CharacterAgeTh(), password),
        'CharacterAgeTw': table_encryption.convert_string(obj.CharacterAgeTw(), password),
        'CharacterAgeEn': table_encryption.convert_string(obj.CharacterAgeEn(), password),
        'CharacterAgeDe': table_encryption.convert_string(obj.CharacterAgeDe(), password),
        'CharacterAgeFr': table_encryption.convert_string(obj.CharacterAgeFr(), password),
        'BirthDay': table_encryption.convert_string(obj.BirthDay(), password),
        'BirthdayKr': table_encryption.convert_string(obj.BirthdayKr(), password),
        'BirthdayJp': table_encryption.convert_string(obj.BirthdayJp(), password),
        'BirthdayTh': table_encryption.convert_string(obj.BirthdayTh(), password),
        'BirthdayTw': table_encryption.convert_string(obj.BirthdayTw(), password),
        'BirthdayEn': table_encryption.convert_string(obj.BirthdayEn(), password),
        'BirthdayDe': table_encryption.convert_string(obj.BirthdayDe(), password),
        'BirthdayFr': table_encryption.convert_string(obj.BirthdayFr(), password),
        'CharHeightKr': table_encryption.convert_string(obj.CharHeightKr(), password),
        'CharHeightJp': table_encryption.convert_string(obj.CharHeightJp(), password),
        'CharHeightTh': table_encryption.convert_string(obj.CharHeightTh(), password),
        'CharHeightTw': table_encryption.convert_string(obj.CharHeightTw(), password),
        'CharHeightEn': table_encryption.convert_string(obj.CharHeightEn(), password),
        'CharHeightDe': table_encryption.convert_string(obj.CharHeightDe(), password),
        'CharHeightFr': table_encryption.convert_string(obj.CharHeightFr(), password),
        'ArtistNameKr': table_encryption.convert_string(obj.ArtistNameKr(), password),
        'ArtistNameJp': table_encryption.convert_string(obj.ArtistNameJp(), password),
        'ArtistNameTh': table_encryption.convert_string(obj.ArtistNameTh(), password),
        'ArtistNameTw': table_encryption.convert_string(obj.ArtistNameTw(), password),
        'ArtistNameEn': table_encryption.convert_string(obj.ArtistNameEn(), password),
        'ArtistNameDe': table_encryption.convert_string(obj.ArtistNameDe(), password),
        'ArtistNameFr': table_encryption.convert_string(obj.ArtistNameFr(), password),
        'CharacterVoiceKr': table_encryption.convert_string(obj.CharacterVoiceKr(), password),
        'CharacterVoiceJp': table_encryption.convert_string(obj.CharacterVoiceJp(), password),
        'CharacterVoiceTh': table_encryption.convert_string(obj.CharacterVoiceTh(), password),
        'CharacterVoiceTw': table_encryption.convert_string(obj.CharacterVoiceTw(), password),
        'CharacterVoiceEn': table_encryption.convert_string(obj.CharacterVoiceEn(), password),
        'CharacterVoiceDe': table_encryption.convert_string(obj.CharacterVoiceDe(), password),
        'CharacterVoiceFr': table_encryption.convert_string(obj.CharacterVoiceFr(), password),
        'HobbyKr': table_encryption.convert_string(obj.HobbyKr(), password),
        'HobbyJp': table_encryption.convert_string(obj.HobbyJp(), password),
        'HobbyTh': table_encryption.convert_string(obj.HobbyTh(), password),
        'HobbyTw': table_encryption.convert_string(obj.HobbyTw(), password),
        'HobbyEn': table_encryption.convert_string(obj.HobbyEn(), password),
        'HobbyDe': table_encryption.convert_string(obj.HobbyDe(), password),
        'HobbyFr': table_encryption.convert_string(obj.HobbyFr(), password),
        'WeaponNameKr': table_encryption.convert_string(obj.WeaponNameKr(), password),
        'WeaponDescKr': table_encryption.convert_string(obj.WeaponDescKr(), password),
        'WeaponNameJp': table_encryption.convert_string(obj.WeaponNameJp(), password),
        'WeaponDescJp': table_encryption.convert_string(obj.WeaponDescJp(), password),
        'WeaponNameTh': table_encryption.convert_string(obj.WeaponNameTh(), password),
        'WeaponDescTh': table_encryption.convert_string(obj.WeaponDescTh(), password),
        'WeaponNameTw': table_encryption.convert_string(obj.WeaponNameTw(), password),
        'WeaponDescTw': table_encryption.convert_string(obj.WeaponDescTw(), password),
        'WeaponNameEn': table_encryption.convert_string(obj.WeaponNameEn(), password),
        'WeaponDescEn': table_encryption.convert_string(obj.WeaponDescEn(), password),
        'WeaponNameDe': table_encryption.convert_string(obj.WeaponNameDe(), password),
        'WeaponDescDe': table_encryption.convert_string(obj.WeaponDescDe(), password),
        'WeaponNameFr': table_encryption.convert_string(obj.WeaponNameFr(), password),
        'WeaponDescFr': table_encryption.convert_string(obj.WeaponDescFr(), password),
        'ProfileIntroductionKr': table_encryption.convert_string(obj.ProfileIntroductionKr(), password),
        'ProfileIntroductionJp': table_encryption.convert_string(obj.ProfileIntroductionJp(), password),
        'ProfileIntroductionTh': table_encryption.convert_string(obj.ProfileIntroductionTh(), password),
        'ProfileIntroductionTw': table_encryption.convert_string(obj.ProfileIntroductionTw(), password),
        'ProfileIntroductionEn': table_encryption.convert_string(obj.ProfileIntroductionEn(), password),
        'ProfileIntroductionDe': table_encryption.convert_string(obj.ProfileIntroductionDe(), password),
        'ProfileIntroductionFr': table_encryption.convert_string(obj.ProfileIntroductionFr(), password),
        'CharacterSSRNewKr': table_encryption.convert_string(obj.CharacterSSRNewKr(), password),
        'CharacterSSRNewJp': table_encryption.convert_string(obj.CharacterSSRNewJp(), password),
        'CharacterSSRNewTh': table_encryption.convert_string(obj.CharacterSSRNewTh(), password),
        'CharacterSSRNewTw': table_encryption.convert_string(obj.CharacterSSRNewTw(), password),
        'CharacterSSRNewEn': table_encryption.convert_string(obj.CharacterSSRNewEn(), password),
        'CharacterSSRNewDe': table_encryption.convert_string(obj.CharacterSSRNewDe(), password),
        'CharacterSSRNewFr': table_encryption.convert_string(obj.CharacterSSRNewFr(), password),
    }


def dump_LocalizeCodeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizeCodeInBuildExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizeErrorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'ErrorLevel': WebAPIErrorLevel(table_encryption.convert_int(obj.ErrorLevel(), password)).name,
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizeEtcExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'NameKr': table_encryption.convert_string(obj.NameKr(), password),
        'DescriptionKr': table_encryption.convert_string(obj.DescriptionKr(), password),
        'NameJp': table_encryption.convert_string(obj.NameJp(), password),
        'DescriptionJp': table_encryption.convert_string(obj.DescriptionJp(), password),
        'NameTh': table_encryption.convert_string(obj.NameTh(), password),
        'DescriptionTh': table_encryption.convert_string(obj.DescriptionTh(), password),
        'NameTw': table_encryption.convert_string(obj.NameTw(), password),
        'DescriptionTw': table_encryption.convert_string(obj.DescriptionTw(), password),
        'NameEn': table_encryption.convert_string(obj.NameEn(), password),
        'DescriptionEn': table_encryption.convert_string(obj.DescriptionEn(), password),
        'NameDe': table_encryption.convert_string(obj.NameDe(), password),
        'DescriptionDe': table_encryption.convert_string(obj.DescriptionDe(), password),
        'NameFr': table_encryption.convert_string(obj.NameFr(), password),
        'DescriptionFr': table_encryption.convert_string(obj.DescriptionFr(), password),
    }


def dump_LocalizeGachaShopExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GachaShopId': table_encryption.convert_long(obj.GachaShopId(), password),
        'TabNameKr': table_encryption.convert_string(obj.TabNameKr(), password),
        'TabNameJp': table_encryption.convert_string(obj.TabNameJp(), password),
        'TabNameTh': table_encryption.convert_string(obj.TabNameTh(), password),
        'TabNameTw': table_encryption.convert_string(obj.TabNameTw(), password),
        'TabNameEn': table_encryption.convert_string(obj.TabNameEn(), password),
        'TabNameDe': table_encryption.convert_string(obj.TabNameDe(), password),
        'TabNameFr': table_encryption.convert_string(obj.TabNameFr(), password),
        'TitleNameKr': table_encryption.convert_string(obj.TitleNameKr(), password),
        'TitleNameJp': table_encryption.convert_string(obj.TitleNameJp(), password),
        'TitleNameTh': table_encryption.convert_string(obj.TitleNameTh(), password),
        'TitleNameTw': table_encryption.convert_string(obj.TitleNameTw(), password),
        'TitleNameEn': table_encryption.convert_string(obj.TitleNameEn(), password),
        'TitleNameDe': table_encryption.convert_string(obj.TitleNameDe(), password),
        'TitleNameFr': table_encryption.convert_string(obj.TitleNameFr(), password),
        'SubTitleKr': table_encryption.convert_string(obj.SubTitleKr(), password),
        'SubTitleJp': table_encryption.convert_string(obj.SubTitleJp(), password),
        'SubTitleTh': table_encryption.convert_string(obj.SubTitleTh(), password),
        'SubTitleTw': table_encryption.convert_string(obj.SubTitleTw(), password),
        'SubTitleEn': table_encryption.convert_string(obj.SubTitleEn(), password),
        'SubTitleDe': table_encryption.convert_string(obj.SubTitleDe(), password),
        'SubTitleFr': table_encryption.convert_string(obj.SubTitleFr(), password),
        'GachaDescriptionKr': table_encryption.convert_string(obj.GachaDescriptionKr(), password),
        'GachaDescriptionJp': table_encryption.convert_string(obj.GachaDescriptionJp(), password),
        'GachaDescriptionTh': table_encryption.convert_string(obj.GachaDescriptionTh(), password),
        'GachaDescriptionTw': table_encryption.convert_string(obj.GachaDescriptionTw(), password),
        'GachaDescriptionEn': table_encryption.convert_string(obj.GachaDescriptionEn(), password),
        'GachaDescriptionDe': table_encryption.convert_string(obj.GachaDescriptionDe(), password),
        'GachaDescriptionFr': table_encryption.convert_string(obj.GachaDescriptionFr(), password),
    }


def dump_LocalizeInformationExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizeOperatorExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizePrefabExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
    }


def dump_LocalizeScenarioExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Key': table_encryption.convert_uint(obj.Key(), password),
        'Kr': table_encryption.convert_string(obj.Kr(), password),
        'Jp': table_encryption.convert_string(obj.Jp(), password),
        'Th': table_encryption.convert_string(obj.Th(), password),
        'Tw': table_encryption.convert_string(obj.Tw(), password),
        'En': table_encryption.convert_string(obj.En(), password),
        'De': table_encryption.convert_string(obj.De(), password),
        'Fr': table_encryption.convert_string(obj.Fr(), password),
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
        'NameTh': table_encryption.convert_string(obj.NameTh(), password),
        'DescriptionTh': table_encryption.convert_string(obj.DescriptionTh(), password),
        'SkillInvokeLocalizeTh': table_encryption.convert_string(obj.SkillInvokeLocalizeTh(), password),
        'NameTw': table_encryption.convert_string(obj.NameTw(), password),
        'DescriptionTw': table_encryption.convert_string(obj.DescriptionTw(), password),
        'SkillInvokeLocalizeTw': table_encryption.convert_string(obj.SkillInvokeLocalizeTw(), password),
        'NameEn': table_encryption.convert_string(obj.NameEn(), password),
        'DescriptionEn': table_encryption.convert_string(obj.DescriptionEn(), password),
        'SkillInvokeLocalizeEn': table_encryption.convert_string(obj.SkillInvokeLocalizeEn(), password),
        'NameDe': table_encryption.convert_string(obj.NameDe(), password),
        'DescriptionDe': table_encryption.convert_string(obj.DescriptionDe(), password),
        'SkillInvokeLocalizeDe': table_encryption.convert_string(obj.SkillInvokeLocalizeDe(), password),
        'NameFr': table_encryption.convert_string(obj.NameFr(), password),
        'DescriptionFr': table_encryption.convert_string(obj.DescriptionFr(), password),
        'SkillInvokeLocalizeFr': table_encryption.convert_string(obj.SkillInvokeLocalizeFr(), password),
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


def dump_MemoryLobbyExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'ProductionStep': ProductionStep(table_encryption.convert_int(obj.ProductionStep_(), password)).name,
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'PrefabName': table_encryption.convert_string(obj.PrefabName(), password),
        'SlotTextureName': table_encryption.convert_string(obj.SlotTextureName(), password),
        'RewardTextureName': table_encryption.convert_string(obj.RewardTextureName(), password),
        'BGMId': table_encryption.convert_long(obj.BGMId(), password),
        'AudioClipJp': table_encryption.convert_string(obj.AudioClipJp(), password),
        'AudioClipKr': table_encryption.convert_string(obj.AudioClipKr(), password),
        'AudioClipTh': table_encryption.convert_string(obj.AudioClipTh(), password),
        'AudioClipTw': table_encryption.convert_string(obj.AudioClipTw(), password),
        'AudioClipEn': table_encryption.convert_string(obj.AudioClipEn(), password),
        'AudioClipDe': table_encryption.convert_string(obj.AudioClipDe(), password),
        'AudioClipFr': table_encryption.convert_string(obj.AudioClipFr(), password),
    }


def dump_MessagePopupExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StringId': table_encryption.convert_uint(obj.StringId(), password),
        'MessagePopupLayout': MessagePopupLayout(table_encryption.convert_int(obj.MessagePopupLayout_(), password)).name,
        'OrderType': MessagePopupImagePositionType(table_encryption.convert_int(obj.OrderType(), password)).name,
        'Image': table_encryption.convert_string(obj.Image(), password),
        'TitleText': table_encryption.convert_uint(obj.TitleText(), password),
        'MessageText': table_encryption.convert_uint(obj.MessageText(), password),
        'DisplayXButton': obj.DisplayXButton(),
        'Button': [MessagePopupButtonType(table_encryption.convert_int(obj.Button(j), password)).name for j in range(obj.ButtonLength())],
        'ButtonText': [table_encryption.convert_uint(obj.ButtonText(j), password) for j in range(obj.ButtonTextLength())],
        'ButtonCommand': [table_encryption.convert_string(obj.ButtonCommand(j), password) for j in range(obj.ButtonCommandLength())],
        'ButtonParameter': [table_encryption.convert_string(obj.ButtonParameter(j), password) for j in range(obj.ButtonParameterLength())],
    }


def dump_MiniGameMissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'EventContentId': table_encryption.convert_long(obj.EventContentId(), password),
        'GroupId': table_encryption.convert_long(obj.GroupId(), password),
        'GroupName': table_encryption.convert_string(obj.GroupName(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_string(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ViewFlag': obj.ViewFlag(),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterName': [table_encryption.convert_string(obj.CompleteConditionParameterName(j), password) for j in range(obj.CompleteConditionParameterNameLength())],
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
        'BgmComposerText': table_encryption.convert_string(obj.BgmComposerText(), password),
        'BgmLength': table_encryption.convert_int(obj.BgmLength(), password),
    }


def dump_MiniGameRhythmExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'UniqueId': table_encryption.convert_long(obj.UniqueId(), password),
        'RhythmBgmId': table_encryption.convert_long(obj.RhythmBgmId(), password),
        'PresetId': table_encryption.convert_long(obj.PresetId(), password),
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


def dump_MiniGameRhythmPresetExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'PresetId': table_encryption.convert_long(obj.PresetId(), password),
        'CameraId': table_encryption.convert_long(obj.CameraId(), password),
        'PCSpawnPositionX': table_encryption.convert_float(obj.PCSpawnPositionX(), password),
        'PCSpawnPositionY': table_encryption.convert_float(obj.PCSpawnPositionY(), password),
        'DetectionLinePositionX': table_encryption.convert_float(obj.DetectionLinePositionX(), password),
        'DetectionLinePositionY': table_encryption.convert_float(obj.DetectionLinePositionY(), password),
        'Speed': table_encryption.convert_float(obj.Speed(), password),
        'RhythmNoteObjectLeft': table_encryption.convert_string(obj.RhythmNoteObjectLeft(), password),
        'RhythmNoteObjectRight': table_encryption.convert_string(obj.RhythmNoteObjectRight(), password),
        'RhythmNoteObjectBoth': table_encryption.convert_string(obj.RhythmNoteObjectBoth(), password),
        'JudgeValuesCritical': table_encryption.convert_float(obj.JudgeValuesCritical(), password),
        'JudgeValuesAttack': table_encryption.convert_float(obj.JudgeValuesAttack(), password),
    }


def dump_MissionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'Category': MissionCategory(table_encryption.convert_int(obj.Category(), password)).name,
        'Description': table_encryption.convert_string(obj.Description(), password),
        'ResetType': MissionResetType(table_encryption.convert_int(obj.ResetType(), password)).name,
        'ViewFlag': obj.ViewFlag(),
        'StartDate': table_encryption.convert_string(obj.StartDate(), password),
        'EndDate': table_encryption.convert_string(obj.EndDate(), password),
        'EndDay': table_encryption.convert_long(obj.EndDay(), password),
        'StartableEndDate': table_encryption.convert_string(obj.StartableEndDate(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'PreMissionId': [table_encryption.convert_long(obj.PreMissionId(j), password) for j in range(obj.PreMissionIdLength())],
        'AccountType': AccountState(table_encryption.convert_int(obj.AccountType(), password)).name,
        'AccountLevel': table_encryption.convert_long(obj.AccountLevel(), password),
        'ShortcutUI': [table_encryption.convert_string(obj.ShortcutUI(j), password) for j in range(obj.ShortcutUILength())],
        'CompleteConditionType': MissionCompleteConditionType(table_encryption.convert_int(obj.CompleteConditionType(), password)).name,
        'CompleteConditionCount': table_encryption.convert_long(obj.CompleteConditionCount(), password),
        'CompleteConditionParameter': [table_encryption.convert_long(obj.CompleteConditionParameter(j), password) for j in range(obj.CompleteConditionParameterLength())],
        'CompleteConditionParameterName': [table_encryption.convert_string(obj.CompleteConditionParameterName(j), password) for j in range(obj.CompleteConditionParameterNameLength())],
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
        'HighlightFloaterHeight': table_encryption.convert_float(obj.HighlightFloaterHeight(), password),
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
        'CampaignStageId': table_encryption.convert_long(obj.CampaignStageId(), password),
        'MultipleConditionCheckType': MultipleConditionCheckType(table_encryption.convert_int(obj.MultipleConditionCheckType_(), password)).name,
        'OpenDayOfWeek': WeekDay(table_encryption.convert_int(obj.OpenDayOfWeek(), password)).name,
        'OpenHour': table_encryption.convert_long(obj.OpenHour(), password),
        'CloseDayOfWeek': WeekDay(table_encryption.convert_int(obj.CloseDayOfWeek(), password)).name,
        'CloseHour': table_encryption.convert_long(obj.CloseHour(), password),
        'CafeRank': table_encryption.convert_long(obj.CafeRank(), password),
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
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'TextLocalizeKey': table_encryption.convert_string(obj.TextLocalizeKey(), password),
        'VoiceClipsKr': [table_encryption.convert_string(obj.VoiceClipsKr(j), password) for j in range(obj.VoiceClipsKrLength())],
        'VoiceClipsJp': [table_encryption.convert_string(obj.VoiceClipsJp(j), password) for j in range(obj.VoiceClipsJpLength())],
        'VoiceClipsTh': [table_encryption.convert_string(obj.VoiceClipsTh(j), password) for j in range(obj.VoiceClipsThLength())],
        'VoiceClipsTw': [table_encryption.convert_string(obj.VoiceClipsTw(j), password) for j in range(obj.VoiceClipsTwLength())],
        'VoiceClipsEn': [table_encryption.convert_string(obj.VoiceClipsEn(j), password) for j in range(obj.VoiceClipsEnLength())],
        'VoiceClipsDe': [table_encryption.convert_string(obj.VoiceClipsDe(j), password) for j in range(obj.VoiceClipsDeLength())],
        'VoiceClipsFr': [table_encryption.convert_string(obj.VoiceClipsFr(j), password) for j in range(obj.VoiceClipsFrLength())],
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


def dump_PresetCharactersExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CharacterId': table_encryption.convert_long(obj.CharacterId(), password),
        'PresetGroupId': table_encryption.convert_long(obj.PresetGroupId(), password),
        'ArenaSimulatorFixed': obj.ArenaSimulatorFixed(),
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
        'MonthlyDays': table_encryption.convert_long(obj.MonthlyDays(), password),
        'ParcelType': [ParcelType(table_encryption.convert_int(obj.ParcelType_(j), password)).name for j in range(obj.ParcelTypeLength())],
        'ParcelId': [table_encryption.convert_long(obj.ParcelId(j), password) for j in range(obj.ParcelIdLength())],
        'ParcelAmount': [table_encryption.convert_long(obj.ParcelAmount(j), password) for j in range(obj.ParcelAmountLength())],
        'DailyParcelType': [ParcelType(table_encryption.convert_int(obj.DailyParcelType(j), password)).name for j in range(obj.DailyParcelTypeLength())],
        'DailyParcelId': [table_encryption.convert_long(obj.DailyParcelId(j), password) for j in range(obj.DailyParcelIdLength())],
        'DailyParcelAmount': [table_encryption.convert_long(obj.DailyParcelAmount(j), password) for j in range(obj.DailyParcelAmountLength())],
    }


def dump_ProtocolSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Protocol': table_encryption.convert_string(obj.Protocol(), password),
        'ContentLockType': ContentLockType(table_encryption.convert_int(obj.ContentLockType_(), password)).name,
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
        'RankStartTw': table_encryption.convert_long(obj.RankStartTw(), password),
        'RankEndTw': table_encryption.convert_long(obj.RankEndTw(), password),
        'RankStartAsia': table_encryption.convert_long(obj.RankStartAsia(), password),
        'RankEndAsia': table_encryption.convert_long(obj.RankEndAsia(), password),
        'RankStartNa': table_encryption.convert_long(obj.RankStartNa(), password),
        'RankEndNa': table_encryption.convert_long(obj.RankEndNa(), password),
        'RankStartGlobal': table_encryption.convert_long(obj.RankStartGlobal(), password),
        'RankEndGlobal': table_encryption.convert_long(obj.RankEndGlobal(), password),
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
        'RaidBossGroup': table_encryption.convert_string(obj.RaidBossGroup(), password),
        'PortraitPath': table_encryption.convert_string(obj.PortraitPath(), password),
        'BGPath': table_encryption.convert_string(obj.BGPath(), password),
        'RaidCharacterId': table_encryption.convert_long(obj.RaidCharacterId(), password),
        'BossCharacterId': [table_encryption.convert_long(obj.BossCharacterId(j), password) for j in range(obj.BossCharacterIdLength())],
        'Difficulty': Difficulty(table_encryption.convert_int(obj.Difficulty_(), password)).name,
        'DifficultyOpenCondition': obj.DifficultyOpenCondition(),
        'MaxPlayerCount': table_encryption.convert_long(obj.MaxPlayerCount(), password),
        'StageCreateCostType': CurrencyTypes(table_encryption.convert_int(obj.StageCreateCostType(), password)).name,
        'StageCreateCostAmount': table_encryption.convert_int(obj.StageCreateCostAmount(), password),
        'StageEnterCostType': CurrencyTypes(table_encryption.convert_int(obj.StageEnterCostType(), password)).name,
        'StageEnterCostAmount': table_encryption.convert_int(obj.StageEnterCostAmount(), password),
        'RaidRoomLifeTime': table_encryption.convert_int(obj.RaidRoomLifeTime(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'GroundDevName': table_encryption.convert_string(obj.GroundDevName(), password),
        'EnterTimeLine': table_encryption.convert_string(obj.EnterTimeLine(), password),
        'TacticEnvironment': TacticEnvironment(table_encryption.convert_int(obj.TacticEnvironment_(), password)).name,
        'SeasonDamageRatio': table_encryption.convert_int(obj.SeasonDamageRatio(), password),
        'DefaultClearScore': table_encryption.convert_long(obj.DefaultClearScore(), password),
        'MaximumScore': table_encryption.convert_long(obj.MaximumScore(), password),
        'PerSecondMinusScore': table_encryption.convert_long(obj.PerSecondMinusScore(), password),
        'HPPercentScore': table_encryption.convert_long(obj.HPPercentScore(), password),
        'RaidRewardGroupId': table_encryption.convert_long(obj.RaidRewardGroupId(), password),
        'RaidRewardDevName': table_encryption.convert_string(obj.RaidRewardDevName(), password),
        'BattleReadyTimelinePath': [table_encryption.convert_string(obj.BattleReadyTimelinePath(j), password) for j in range(obj.BattleReadyTimelinePathLength())],
        'BattleReadyTimelinePhaseStart': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseStart(j), password) for j in range(obj.BattleReadyTimelinePhaseStartLength())],
        'BattleReadyTimelinePhaseEnd': [table_encryption.convert_int(obj.BattleReadyTimelinePhaseEnd(j), password) for j in range(obj.BattleReadyTimelinePhaseEndLength())],
        'VictoryTimelinePath': table_encryption.convert_string(obj.VictoryTimelinePath(), password),
        'PhaseChangeTimelinePath': table_encryption.convert_string(obj.PhaseChangeTimelinePath(), password),
        'TimeLinePhase': table_encryption.convert_long(obj.TimeLinePhase(), password),
        'EnterScenarioKey': table_encryption.convert_uint(obj.EnterScenarioKey(), password),
        'ClearScenarioKey': table_encryption.convert_uint(obj.ClearScenarioKey(), password),
        'ReviveParcelType': ParcelType(table_encryption.convert_int(obj.ReviveParcelType(), password)).name,
        'ReviveParcelId': table_encryption.convert_long(obj.ReviveParcelId(), password),
        'ReviveParcelDevName': table_encryption.convert_string(obj.ReviveParcelDevName(), password),
        'ReviveParcelAmount': table_encryption.convert_long(obj.ReviveParcelAmount(), password),
        'InitSupplyCount': table_encryption.convert_int(obj.InitSupplyCount(), password),
        'ShowSkillCard': obj.ShowSkillCard(),
        'BossBGInfoKey': table_encryption.convert_uint(obj.BossBGInfoKey(), password),
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
        'Positions': [None if obj.Positions() is None else dump_Position(obj.Positions(j), password) for j in range(obj.PositionsLength())],
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
        'Forms': [None if obj.Forms() is None else dump_Form(obj.Forms(j), password) for j in range(obj.FormsLength())],
        'ExSkills': [None if obj.ExSkills() is None else dump_Motion(obj.ExSkills(j), password) for j in range(obj.ExSkillsLength())],
        'MoveLeft': dump_Motion(obj.MoveLeft(), password),
        'MoveRight': dump_Motion(obj.MoveRight(), password),
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


def dump_ScenarioBGName_GlobalExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'GroupName': table_encryption.convert_uint(obj.GroupName(), password),
        'NameKr': table_encryption.convert_uint(obj.NameKr(), password),
        'NameTw': table_encryption.convert_uint(obj.NameTw(), password),
        'NameAsia': table_encryption.convert_uint(obj.NameAsia(), password),
        'NameNa': table_encryption.convert_uint(obj.NameNa(), password),
        'NameGlobal': table_encryption.convert_uint(obj.NameGlobal(), password),
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
        'NameTH': table_encryption.convert_string(obj.NameTH(), password),
        'NicknameTH': table_encryption.convert_string(obj.NicknameTH(), password),
        'NameTW': table_encryption.convert_string(obj.NameTW(), password),
        'NicknameTW': table_encryption.convert_string(obj.NicknameTW(), password),
        'NameEN': table_encryption.convert_string(obj.NameEN(), password),
        'NicknameEN': table_encryption.convert_string(obj.NicknameEN(), password),
        'NameDE': table_encryption.convert_string(obj.NameDE(), password),
        'NicknameDE': table_encryption.convert_string(obj.NicknameDE(), password),
        'NameFR': table_encryption.convert_string(obj.NameFR(), password),
        'NicknameFR': table_encryption.convert_string(obj.NicknameFR(), password),
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
        'FrontScenarioGroupId': [table_encryption.convert_long(obj.FrontScenarioGroupId(j), password) for j in range(obj.FrontScenarioGroupIdLength())],
        'GroundId': table_encryption.convert_long(obj.GroundId(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'BackScenarioGroupId': [table_encryption.convert_long(obj.BackScenarioGroupId(j), password) for j in range(obj.BackScenarioGroupIdLength())],
        'ClearedModeId': table_encryption.convert_long(obj.ClearedModeId(), password),
        'AccountLevelLimit': table_encryption.convert_long(obj.AccountLevelLimit(), password),
        'ClearedStageId': table_encryption.convert_long(obj.ClearedStageId(), password),
        'NeedClub': Club(table_encryption.convert_int(obj.NeedClub(), password)).name,
        'NeedClubStudentCount': table_encryption.convert_int(obj.NeedClubStudentCount(), password),
        'NeedTSS': table_encryption.convert_long(obj.NeedTSS(), password),
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'FixedEchelonId': table_encryption.convert_long(obj.FixedEchelonId(), password),
        'CompleteReportEventName': table_encryption.convert_string(obj.CompleteReportEventName(), password),
    }


def dump_ScenarioModeRewardExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ModeId': table_encryption.convert_long(obj.ModeId(), password),
        'RewardParcelType': [ParcelType(table_encryption.convert_int(obj.RewardParcelType(j), password)).name for j in range(obj.RewardParcelTypeLength())],
        'RewardParcelId': [table_encryption.convert_long(obj.RewardParcelId(j), password) for j in range(obj.RewardParcelIdLength())],
        'RewardParcelAmount': [table_encryption.convert_int(obj.RewardParcelAmount(j), password) for j in range(obj.RewardParcelAmountLength())],
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


def dump_ScenarioScriptContentExcel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptEvent1Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptEvent2Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptEvent3Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptFavor1Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptFavor2Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptFavor3Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptGroup1Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptGroup2Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptGroup3Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptMain1Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptMain2Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptMain3Excel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
    }


def dump_ScenarioScriptTestExcel(obj, password) -> dict:
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
        'TextTh': table_encryption.convert_string(obj.TextTh(), password),
        'TextTw': table_encryption.convert_string(obj.TextTw(), password),
        'TextEn': table_encryption.convert_string(obj.TextEn(), password),
        'TextDe': table_encryption.convert_string(obj.TextDe(), password),
        'TextFr': table_encryption.convert_string(obj.TextFr(), password),
        'VoiceJp': table_encryption.convert_string(obj.VoiceJp(), password),
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
        'StageActionPointCostAmount': table_encryption.convert_long(obj.StageActionPointCostAmount(), password),
        'EnterCostType': CurrencyTypes(table_encryption.convert_int(obj.EnterCostType(), password)).name,
        'EnterCostAmount': table_encryption.convert_long(obj.EnterCostAmount(), password),
        'GroundId': table_encryption.convert_int(obj.GroundId(), password),
        'StarGoal': [WeekDungeonStarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_long(obj.RecommandLevel(), password),
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_long(obj.PlayTimeLimitInSeconds(), password),
    }


def dump_ServiceActionExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ServiceActionType': ServiceActionType(table_encryption.convert_int(obj.ServiceActionType_(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': table_encryption.convert_long(obj.GoodsId(), password),
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
        'PackageClientType': PurchaseSourceType(table_encryption.convert_int(obj.PackageClientType(), password)).name,
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
    }


def dump_ShopInfoExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsRefresh': obj.IsRefresh(),
        'ParcelType': ParcelType(table_encryption.convert_int(obj.ParcelType_(), password)).name,
        'ParcelId': table_encryption.convert_long(obj.ParcelId(), password),
        'AutoRefreshCoolTime': table_encryption.convert_long(obj.AutoRefreshCoolTime(), password),
        'RefreshAbleCount': table_encryption.convert_long(obj.RefreshAbleCount(), password),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'OpenPeriodFrom': table_encryption.convert_string(obj.OpenPeriodFrom(), password),
        'OpenPeriodTo': table_encryption.convert_string(obj.OpenPeriodTo(), password),
    }


def dump_ShopRecruitExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'CategoryType': ShopCategoryType(table_encryption.convert_int(obj.CategoryType(), password)).name,
        'IsLegacy': obj.IsLegacy(),
        'GoodsId': [table_encryption.convert_long(obj.GoodsId(j), password) for j in range(obj.GoodsIdLength())],
        'GoodsDevName': table_encryption.convert_string(obj.GoodsDevName(), password),
        'DisplayOrder': table_encryption.convert_long(obj.DisplayOrder(), password),
        'MovieBannerPath': [table_encryption.convert_string(obj.MovieBannerPath(j), password) for j in range(obj.MovieBannerPathLength())],
        'LinkedRobbyBannerId': table_encryption.convert_long(obj.LinkedRobbyBannerId(), password),
        'InfoCharacterId': [table_encryption.convert_long(obj.InfoCharacterId(j), password) for j in range(obj.InfoCharacterIdLength())],
        'SalePeriodFrom': table_encryption.convert_string(obj.SalePeriodFrom(), password),
        'SalePeriodTo': table_encryption.convert_string(obj.SalePeriodTo(), password),
        'RecruitCoinId': table_encryption.convert_long(obj.RecruitCoinId(), password),
        'RecruitSellectionShopId': table_encryption.convert_long(obj.RecruitSellectionShopId(), password),
        'PurchaseCooltimeMin': table_encryption.convert_long(obj.PurchaseCooltimeMin(), password),
        'PurchaseCountLimit': table_encryption.convert_long(obj.PurchaseCountLimit(), password),
        'PurchaseCountResetType': PurchaseCountResetType(table_encryption.convert_int(obj.PurchaseCountResetType_(), password)).name,
        'ProbabilityUrlDev': table_encryption.convert_string(obj.ProbabilityUrlDev(), password),
        'ProbabilityUrlLive': table_encryption.convert_string(obj.ProbabilityUrlLive(), password),
    }


def dump_ShopRefreshExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
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


def dump_ShortcutTypeExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'IsAscending': obj.IsAscending(),
        'ContentType': [ShortcutContentType(table_encryption.convert_int(obj.ContentType(j), password)).name for j in range(obj.ContentTypeLength())],
    }


def dump_SkillExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_long(obj.Id(), password),
        'LocalizeSkillId': table_encryption.convert_uint(obj.LocalizeSkillId(), password),
        'GroupId': table_encryption.convert_string(obj.GroupId(), password),
        'Level': table_encryption.convert_int(obj.Level(), password),
        'SkillCost': table_encryption.convert_int(obj.SkillCost(), password),
        'EnemySkillCost': table_encryption.convert_int(obj.EnemySkillCost(), password),
        'BulletType': BulletType(table_encryption.convert_int(obj.BulletType_(), password)).name,
        'StartCoolTime': table_encryption.convert_int(obj.StartCoolTime(), password),
        'CoolTime': table_encryption.convert_int(obj.CoolTime(), password),
        'EnemyStartCoolTime': table_encryption.convert_int(obj.EnemyStartCoolTime(), password),
        'EnemyCoolTime': table_encryption.convert_int(obj.EnemyCoolTime(), password),
        'UseAtg': table_encryption.convert_int(obj.UseAtg(), password),
        'RequireCharacterLevel': table_encryption.convert_int(obj.RequireCharacterLevel(), password),
        'RequireLevelUpMaterial': table_encryption.convert_long(obj.RequireLevelUpMaterial(), password),
        'IconName': table_encryption.convert_string(obj.IconName(), password),
        'IsShowInfo': obj.IsShowInfo(),
    }


def dump_SoundUIExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'ID': table_encryption.convert_long(obj.ID(), password),
        'SoundUniqueId': table_encryption.convert_string(obj.SoundUniqueId(), password),
        'Path': table_encryption.convert_string(obj.Path(), password),
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
        'Standard': table_encryption.convert_long(obj.Standard(), password),
        'Premature': table_encryption.convert_long(obj.Premature(), password),
        'LateBloom': table_encryption.convert_long(obj.LateBloom(), password),
        'Obstacle': table_encryption.convert_long(obj.Obstacle(), password),
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
        'InteractionChar': [table_encryption.convert_long(obj.InteractionChar(j), password) for j in range(obj.InteractionCharLength())],
        'CharacterInteractionStartDelay': table_encryption.convert_long(obj.CharacterInteractionStartDelay(), password),
        'GetOnStartEffectPath': table_encryption.convert_string(obj.GetOnStartEffectPath(), password),
        'GetOnEndEffectPath': table_encryption.convert_string(obj.GetOnEndEffectPath(), password),
    }


def dump_TagSettingExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': Tag(table_encryption.convert_int(obj.Id(), password)).name,
        'IsOpen': obj.IsOpen(),
        'LocalizeEtcId': table_encryption.convert_uint(obj.LocalizeEtcId(), password),
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


def dump_ToastExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Id': table_encryption.convert_uint(obj.Id(), password),
        'ToastType': ToastType(table_encryption.convert_int(obj.ToastType_(), password)).name,
        'MissionId': table_encryption.convert_uint(obj.MissionId(), password),
        'TextId': table_encryption.convert_uint(obj.TextId(), password),
        'LifeTime': table_encryption.convert_long(obj.LifeTime(), password),
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


def dump_TutorialCharacterDialogExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'TalkId': table_encryption.convert_long(obj.TalkId(), password),
        'AnimationName': table_encryption.convert_string(obj.AnimationName(), password),
        'LocalizeKR': table_encryption.convert_string(obj.LocalizeKR(), password),
        'LocalizeJP': table_encryption.convert_string(obj.LocalizeJP(), password),
        'LocalizeTH': table_encryption.convert_string(obj.LocalizeTH(), password),
        'LocalizeTW': table_encryption.convert_string(obj.LocalizeTW(), password),
        'LocalizeEN': table_encryption.convert_string(obj.LocalizeEN(), password),
        'LocalizeDE': table_encryption.convert_string(obj.LocalizeDE(), password),
        'LocalizeFR': table_encryption.convert_string(obj.LocalizeFR(), password),
        'SoundPathKR': table_encryption.convert_string(obj.SoundPathKR(), password),
        'SoundPathJP': table_encryption.convert_string(obj.SoundPathJP(), password),
        'SoundPathTH': table_encryption.convert_string(obj.SoundPathTH(), password),
        'SoundPathTW': table_encryption.convert_string(obj.SoundPathTW(), password),
        'SoundPathEN': table_encryption.convert_string(obj.SoundPathEN(), password),
        'SoundPathDE': table_encryption.convert_string(obj.SoundPathDE(), password),
        'SoundPathFR': table_encryption.convert_string(obj.SoundPathFR(), password),
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
        'ImagePathTh': table_encryption.convert_string(obj.ImagePathTh(), password),
        'ImagePathTw': table_encryption.convert_string(obj.ImagePathTw(), password),
        'ImagePathEn': table_encryption.convert_string(obj.ImagePathEn(), password),
        'ImagePathDe': table_encryption.convert_string(obj.ImagePathDe(), password),
        'ImagePathFr': table_encryption.convert_string(obj.ImagePathFr(), password),
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
        'NameHash': table_encryption.convert_uint(obj.NameHash(), password),
        'OnlyOne': obj.OnlyOne(),
        'VolumeJp': table_encryption.convert_float(obj.VolumeJp(), password),
        'DelayJp': table_encryption.convert_float(obj.DelayJp(), password),
        'Priority': table_encryption.convert_int(obj.Priority(), password),
        'AudioClipJp': table_encryption.convert_string(obj.AudioClipJp(), password),
        'VolumeKr': table_encryption.convert_float(obj.VolumeKr(), password),
        'DelayKr': table_encryption.convert_float(obj.DelayKr(), password),
        'AudioClipKr': table_encryption.convert_string(obj.AudioClipKr(), password),
        'VolumeTh': table_encryption.convert_float(obj.VolumeTh(), password),
        'DelayTh': table_encryption.convert_float(obj.DelayTh(), password),
        'AudioClipTh': table_encryption.convert_string(obj.AudioClipTh(), password),
        'VolumeTw': table_encryption.convert_float(obj.VolumeTw(), password),
        'DelayTw': table_encryption.convert_float(obj.DelayTw(), password),
        'AudioClipTw': table_encryption.convert_string(obj.AudioClipTw(), password),
        'VolumeEn': table_encryption.convert_float(obj.VolumeEn(), password),
        'DelayEn': table_encryption.convert_float(obj.DelayEn(), password),
        'AudioClipEn': table_encryption.convert_string(obj.AudioClipEn(), password),
        'VolumeDe': table_encryption.convert_float(obj.VolumeDe(), password),
        'DelayDe': table_encryption.convert_float(obj.DelayDe(), password),
        'AudioClipDe': table_encryption.convert_string(obj.AudioClipDe(), password),
        'VolumeFr': table_encryption.convert_float(obj.VolumeFr(), password),
        'DelayFr': table_encryption.convert_float(obj.DelayFr(), password),
        'AudioClipFr': table_encryption.convert_string(obj.AudioClipFr(), password),
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


def dump_VoiceSkillUseExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'Name': table_encryption.convert_string(obj.Name(), password),
        'VoiceHash': [table_encryption.convert_uint(obj.VoiceHash(j), password) for j in range(obj.VoiceHashLength())],
    }


def dump_WeekDungeonExcel(obj, password) -> dict:
    table_encryption = TableEncryptionService()

    return {
        'StageId': table_encryption.convert_long(obj.StageId(), password),
        'WeekDungeonType': WeekDungeonType(table_encryption.convert_int(obj.WeekDungeonType_(), password)).name,
        'Difficulty': table_encryption.convert_int(obj.Difficulty(), password),
        'BattleDuration': table_encryption.convert_long(obj.BattleDuration(), password),
        'PrevStageId': table_encryption.convert_long(obj.PrevStageId(), password),
        'StageActionPointCostAmount': table_encryption.convert_long(obj.StageActionPointCostAmount(), password),
        'ConsumeTicket': obj.ConsumeTicket(),
        'GroundId': table_encryption.convert_int(obj.GroundId(), password),
        'StarGoal': [WeekDungeonStarGoalType(table_encryption.convert_int(obj.StarGoal(j), password)).name for j in range(obj.StarGoalLength())],
        'StarGoalAmount': [table_encryption.convert_int(obj.StarGoalAmount(j), password) for j in range(obj.StarGoalAmountLength())],
        'StageTopography': StageTopography(table_encryption.convert_int(obj.StageTopography_(), password)).name,
        'RecommandLevel': table_encryption.convert_long(obj.RecommandLevel(), password),
        'StageRewardId': table_encryption.convert_long(obj.StageRewardId(), password),
        'PlayTimeLimitInSeconds': table_encryption.convert_long(obj.PlayTimeLimitInSeconds(), password),
        'BattleRewardExp': table_encryption.convert_long(obj.BattleRewardExp(), password),
        'BattleRewardPlayerExp': table_encryption.convert_long(obj.BattleRewardPlayerExp(), password),
        'GroupBuffID': [table_encryption.convert_long(obj.GroupBuffID(j), password) for j in range(obj.GroupBuffIDLength())],
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


from enum import IntEnum


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

class CafeCharacterState(IntEnum):
    none = 0
    Idle = 1
    Walk = 2
    Reaction = 3
    Speedrace = 4
    Hockey1 = 5
    Hockey2 = 6
    Max = 7

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

class KnockbackDirection(IntEnum):
    TargetToCaster = 0
    CasterToTarget = 1
    TargetToHitPosition = 2
    HitPositionToTarget = 3
    CasterToHitPosition = 4
    HitPositionToCaster = 5

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

class NexonBillingState(IntEnum):
    ValiDateWait = 0
    ValiDateFail = 1
    ValiDateSuccess = 2
    Finish = 3

class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2

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
    Max = 45

class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3

class TacticRole(IntEnum):
    DamageDealer = 0
    Tanker = 1
    Supporter = 2
    Healer = 3
    Vehicle = 4

class TacticRange(IntEnum):
    Back = 0
    Front = 1
    Middle = 2

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

class WeekDungeonType(IntEnum):
    none = 0
    ChaserA = 1
    ChaserB = 2
    ChaserC = 3
    FindGift = 4
    Blood = 5

class WeekDungeonStarGoalType(IntEnum):
    none = 0
    AllAlive = 1
    Clear = 2
    GetBoxes = 3
    ClearTimeInSec = 4

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

class ContentLockType(IntEnum):
    none = 0
    NotUseControlledByOtherSetting = 1
    Academy = 2
    Arena = 3
    Billing = 4
    Cafe = 5
    Campaign = 6
    Clan = 7
    Craft = 8
    Echelon = 9
    Equipment = 10
    EventContent = 11
    EventStage_1 = 12
    EventStage_2 = 13
    Favor = 14
    Gacha = 15
    GuideMission = 16
    Item = 17
    LobbyIllust = 18
    Mission = 19
    MomoTalk = 20
    Raid = 21
    Schedule = 22
    Shop = 23
    SkipHistorySave = 24
    Story = 25
    Unit_Growth_LevelUp = 26
    Unit_Growth_Skill = 27
    Unit_Growth_Transcendence = 28
    WeekDungeon = 29
    WeekDungeon_Chase = 30
    SchoolDungeon = 31

class TutorialFailureContentType(IntEnum):
    none = 0
    Campaign = 1
    WeekDungeon = 2
    Raid = 3

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

class EventCollectionUnlockType(IntEnum):
    none = 0
    ClearSpecificEventStage = 1
    ClearSpecificEventScenario = 2
    ClearSpecificEventMission = 3
    PurchaseSpecificItemCount = 4

class ShortcutContentType(IntEnum):
    none = 0
    CampaignStage = 1
    EventStage = 2
    Blood = 3
    WeekDungeon = 4
    Arena = 5
    Raid = 6
    Shop = 7

class JudgeGrade(IntEnum):
    none = 0
    Miss = 1
    Attack = 2
    Critical = 3

class SchoolDungeonType(IntEnum):
    SchoolA = 0
    SchoolB = 1
    SchoolC = 2

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

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class Language(IntEnum):
    Kr = 0
    Jp = 1
    Th = 2
    Tw = 3
    En = 4
    De = 5
    Fr = 6

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

class AccountBanType(IntEnum):
    none = 0
    AbuseGamePlay = 1
    AbuseMarket = 2
    AbuseGameSystem = 3
    OperaionPolicyViolate = 4
    Useillegalprogram = 5
    Temporaryconstraint = 6

class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    MonthlyBonus = 8

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
    CashShopBuy = 15
    MonthlyProductPackage = 16

class AttendanceType(IntEnum):
    Basic = 0
    Event = 1
    Newbie = 2

class AttendanceCountRule(IntEnum):
    Accumulation = 0
    Date = 1

class AttendanceResetType(IntEnum):
    User = 0
    Server = 1

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

class MissionResetType(IntEnum):
    none = 0
    Daily = 1
    Weekly = 2

class MissionCompleteConditionType(IntEnum):
    none = 0
    DailyLogin = 1
    DailyLoginCount = 2
    CompleteMission = 3
    EquipmentLevelUpCount = 4
    EquipmentTierUpCount = 5
    CharacterLevelUpCount = 6
    CharacterTranscendenceCount = 7
    ClearTaticBattleCount = 8
    ClearCampaignStageCount = 9
    KillSpecificEnemyCount = 10
    KillEnemyWithTagCount = 11
    GetCharacterCount = 12
    GetCharacterWithTagCount = 13
    GetSpecificCharacterCount = 14
    AccountLevelUp = 15
    GetEquipmentCount = 16
    GachaCount = 17
    UseGem = 18
    GetGem = 19
    GetGemPaid = 20
    GetGold = 21
    GetItem = 22
    GetFavorLevel = 23
    EquipmentAtSpecificLevelCount = 24
    EquipmentAtSpecificTierUpCount = 25
    CharacterAtSpecificLevelCount = 26
    CharacterAtSpecificTranscendenceCount = 27
    CharacterSkillLevelUpCount = 28
    CharacterAtSpecificSkillLevelCount = 29
    CompleteScheduleCount = 30
    CompleteScheduleGroupCount = 31
    AcademyLocationRankSum = 32
    CraftCount = 33
    GetComfortPoint = 34
    GetWeaponCount = 35
    EquipWeaponCount = 36
    CompleteScheduleWithSpecificCharacter = 37
    CafeInteractionCount = 38
    SpecificCharacterAtSpecificLevel = 39
    SpecificCharacterAtSpecificTranscendence = 40
    LobbyInteraction = 41
    ClearWeekDungeonCount = 42
    ClearSpecificWeekDungeonCount = 43
    JoinRaidCount = 44
    JoinSpecificRaidCount = 45
    JoinArenaCount = 46
    ArenaVictoryCount = 47
    RaidDamageAmountOnOneBattle = 48
    ClearEventStageCount = 49
    UseSpecificCharacterCount = 50
    UseGold = 51
    UseTiket = 52
    ShopBuyCount = 53
    ShopBuyActionPointCount = 54
    SpecificCharacterAtSpecificFavorRank = 55
    ClearSpecificScenario = 56
    GetSpecificItemCount = 57
    TotalGetClearStarCount = 58
    CompleteCampaignStageMinimumTurn = 59
    TotalLoginCount = 60
    LoginAtSpecificTime = 61
    CompleteFavorSchedule = 62
    CompleteFavorScheduleAtSpecificCharacter = 63
    GetMemoryLobbyCount = 64
    GetFurnitureGroupCount = 65
    AcademyLocationAtSpecificRank = 66
    ClearCampaignStageDifficultyNormal = 67
    ClearCampaignStageDifficultyHard = 68
    ClearChaserDungeonCount = 69
    ClearSpecificChaserDungeonCount = 70
    GetCafeRank = 71
    SpecificStarCharacterCount = 72
    EventClearCampaignStageCount = 73
    EventClearSpecificCampaignStageCount = 74
    EventCompleteCampaignStageMinimumTurn = 75
    EventClearCampaignStageDifficultyNormal = 76
    EventClearCampaignStageDifficultyHard = 77
    ClearSpecificCampaignStageCount = 78
    GetItemWithTagCount = 79
    GetFurnitureWithTagCount = 80
    GetEquipmentWithTagCount = 81
    ClearCampaignStageTimeLimitFromSecond = 82
    ClearEventStageTimeLimitFromSecond = 83
    ClearRaidTimeLimitFromSecond = 84
    ClearBattleWithTagCount = 85
    ClearWeekDungeonTimeLimitFromSecond = 86
    CompleteScheduleWithTagCount = 87
    ClearChaserDungeonTimeLimitFromSecond = 88
    GetTotalScoreRhythm = 89
    GetBestScoreRhythm = 90
    GetSpecificScoreRhythm = 91
    ClearStageRhythm = 92
    GetComboCountRhythm = 93
    GetFullComboRhythm = 94
    GetFeverCountRhythm = 95
    UseActionPoint = 96

class AccountAchievementType(IntEnum):
    TotalLoginCount = 0
    TotalGetClearStarCount = 1
    TotalCharacterLevelUpCount = 2
    TotalCharacterSkillLevelUpCount = 3
    TotalClearCampaignStageCount = 4
    TotalClearChaserDungeonCount = 5
    TotalClearWeekDungeonCount = 6
    TotalEquipmentLevelUpCount = 7
    TotalEquipmentTierUpCount = 8
    MaxComfortPoint = 9
    TotalGetGold = 10
    TotalUseGold = 11
    TotalJoinArenaCount = 12
    TotalJoinRaidCount = 13

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
    ProductMonthly = 18

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
    MasterCoin = 17
    Max = 18

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

class GachaGroupType(IntEnum):
    none = 0
    Reward_General = 1
    System_Craft = 2

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
    Clan_Create = 101
    ContentDiscard_Currency = 102

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

class DialogConditionDetail(IntEnum):
    none = 0
    Day = 1
    Close = 2

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

class ScenarioModeTypes(IntEnum):
    none = 0
    Main = 1
    Sub = 2
    Replay = 3

class ScenarioModeSubTypes(IntEnum):
    none = 0
    Club = 1
    TSS = 2

class ScenarioModeReplayTypes(IntEnum):
    none = 0
    Event = 1
    Favor = 2
    Work = 3

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
    ThreeStarGacha = 18
    LimitedGacha = 19
    MasterCoin = 20

class PurchaseServerTag(IntEnum):
    Audit = 0
    PreAudit = 1
    Production = 2
    Hotfix = 3
    Temp1 = 4
    Temp2 = 5
    Temp3 = 6
    Temp4 = 7
    Temp5 = 8
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

class ProductDisplayTag(IntEnum):
    none = 0
    New = 1
    Hot = 2
    Sale = 3

class BillingTransactionEndType(IntEnum):
    none = 0
    Success = 1
    Cancel = 2

class GachaRewardType(IntEnum):
    none = 0
    Eligma = 1
    Eleph = 2

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

class GroundNodeType(IntEnum):
    none = 0
    WalkAble = 1
    JumpAble = 2
    TSSOnly = 3
    NotWalkAble = 2147483647

