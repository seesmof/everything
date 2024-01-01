MetaUpgradeData =
{
	BaseMetaUpgrade =
	{
		UsePromptOffsetX = 60,
		UsePromptOffsetY = 15,
		ResourceName = "LockKeys",
		UnlockCost = 10,
	},

	HealthMetaUpgrade = -- Thick Skin
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_StartingHealth",
		RequiredAccumulatedMetaPoints = 200,
		Starting = true,
		CostTable = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 43, 49, 52, 55, 58, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 114, 119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 170, 176, 182, 188, 194, 200, 206, 212, 218, 224, 230, 237, 244, 251, 258, 265, 272, 279, 286, 293, 300, 308, 316, 324, 332, 340, 348, 356, 364, 372, 380, 389, 398, 407, 416, 425, 434, 443, 452, 461, 470 },
		ShortTotal = "HealthMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "HealthMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
		PropertyChanges =
		{
			{
				LuaProperty = "MaxHealth",
				ChangeValue = 1,
				ChangeType = "Add",
			},
		}
	},

	HighHealthDamageMetaUpgrade = -- High Confidence
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_HighHealthDamage",
		RequiredAccumulatedMetaPoints = 200,
		Starting = true,
		CostTable = { 1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 145, 148 },
		ShortTotal = "HighHealthDamageMetaUpgrade_ShortTotal",
		ChangeValue = 1.04,
		DisplayValue = 75, -- display variable to show the health threshold
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			HighHealthSourceMultiplierData = { Threshold = 0.75, Multiplier = 1.04 },
		}
	},

	HealthEncounterEndRegenMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		RequiredAccumulatedMetaPoints = 75,
		ResourceName = "LockKeys",
		UnlockCost = 3,
		CostTable = { 25, 75, 150, 500 },
		ShortTotal = "HealthEncounterEndRegenMetaUpgrade_ShortTotal",
		ChangeValue = 10,
	},

	DoorHealMetaUpgrade = -- Chtonic Vitality
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DoorHeal",
		Starting = true,
		CostTable = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250 },
		ShortTotal = "DoorHealMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "DoorHealMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	DarknessHealMetaUpgrade = -- Dark Regeneration
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DarknessHeal",
		Starting = true,
		CostTable = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250 },
		ShortTotal = "DarknessHealMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "DarknessHealMetaUpgrade_ShortTotalNoIcon",
		FormatAsPercent = true,
		ChangeValue = 1.1,
	},

	HealthDropMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		RequiredAccumulatedMetaPoints = 200,
		CostTable = { 50, 100, 150, 200, 300 },
		ShortTotal = "HealthDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.01,
		FormatAsPercent = true,
	},

	WeaponDamageMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		Cost = 10,
		CostIncreaseInterval = 1,
		CostIncrease = 10,
		ShortTotal = "WeaponDamageMetaUpgrade_ShortTotal",
		PropertyChanges =
		{
			{
				WeaponNames = WeaponSets.HeroPhysicalWeapons,
				ProjectileProperty = "DamageLow",
				ChangeValue = 1.10,
				ChangeType = "MultiplyBase",
			},
			{
				WeaponNames = WeaponSets.HeroPhysicalWeapons,
				ProjectileProperty = "DamageHigh",
				ChangeValue = 1.10,
				ChangeType = "MultiplyBase",
			},
		},

	},

	DashAttackMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		ResourceName = "LockKeys",
		UnlockCost = 3,
		CostTable = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 },
		Skip = true,
		ShortTotal = "DashAttackMetaUpgrade_ShortTotal",
		ReapplyOnWeaponSwitch = true,
		ChangeValue = 1.10,
		FormatAsPercent = true,
		PropertyChanges =
		{
			{
				WeaponName = "SwordWeaponDash",
				ProjectileProperty = "DamageAddition",
				ChangeValue = 1,
				ChangeType = "Add",
			},
			{
				WeaponName = "ShieldWeaponDash",
				ProjectileProperty = "DamageAddition",
				ChangeValue = 2,
				ChangeType = "Add",
			},
			{
				WeaponName = "SpearWeaponDash",
				ProjectileProperty = "DamageAddition",
				ChangeValue = 1.5,
				ChangeType = "Add",
			},
			{
				WeaponName = "BowWeaponDash",
				ProjectileProperty = "DamageAddition",
				ChangeValue = 3,
				ChangeType = "Add",
			},
		},
	},

	AmmoMetaUpgrade = -- Infernal Soul
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_AmmoSupply",
		Starting = true,
		Cost = 10,
		CostTable = { 20, 60, 180, 540, 1620 },
		ShortTotal = "AmmoMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "AmmoMetaUpgrade_ShortTotalNoIcon",
		KeywordOverrides =
		{
			{
				Key = "Cast",
				Value = "Cast",
			},
			{
				Key = "Ammo",
				Value = "Ammo",
			}
		},
		PropertyChanges =
		{
			{
				WeaponNames = WeaponSets.HeroNonPhysicalWeapons,
				WeaponProperty = "MaxAmmo",
				ChangeValue = 1,
				ChangeType = "Add",
			},
		},
	},

	ReloadAmmoMetaUpgrade = -- Stygian Soul
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_ReloadAmmo",
		Starting = true,
		Cost = 10,
		CostTable = { 120, 240, 360, 480, 600, 750 },
		KeywordOverrides =
		{
			{
				Key = "Cast",
				Value = "CastAlt",
			},
			{
				Key = "Ammo",
				Value = "AmmoAlt",
			}
		},
		BaseValue = 7.0,
		ShortTotal = "ReloadAmmoMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ReloadAmmoMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = -1,
	},

	StaminaMetaUpgrade = -- Greater Reflex
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DashCharges",
		Starting = true,
		CostTable = { 100, 300, 900, 2700, 8100 },
		ShortTotal = "StaminaMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "StaminaMetaUpgrade_ShortTotalNoIcon",
		HelpTextTable =
		{
			[0] = "StaminaMetaUpgrade_Off",
			[1] = "StaminaMetaUpgrade_On",
		},
		PropertyChanges =
		{
			{
				WeaponNames = WeaponSets.HeroRushWeapons,
				WeaponProperty = "ClipSize",
				ChangeValue = 1,
				ChangeType = "Add",
			},
		},
	},

	PerfectDashMetaUpgrade = -- Ruthless Reflex
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_PerfectDash",
		Starting = true,
		CostTable = { 50, 100, 150, 200, 250, 300, 350, 400, 450, 500 },
		ShortTotal = "PerfectDashMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "PerfectDashMetaUpgrade_ShortTotalNoIcon",
		PreEquipWeapon = "PerfectDashEmpowerApplicator",
		ChangeValue = 1.3, -- display variable, change below value to affect gameplay
		DisplayValue = 2, -- display variable used to display duration of buff
		PropertyChanges =
		{
			{
				WeaponName = "PerfectDashEmpowerApplicator",
				EffectName = "PerfectDashDamageBonus",
				EffectProperty = "Modifier",
				ChangeValue = 0.3,
				ChangeType = "Add",
			},
		},
		HelpTextTable =
		{
			[0] = "PerfectDashMetaUpgrade_Off",
			[1] = "PerfectDashMetaUpgrade_On",
		},

	},

	BackstabMetaUpgrade = -- Shadow Presence
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_SneakAttack",
		Starting = true,
		CostTable = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200 },
		ShortTotal = "BackstabMetaUpgrade_ShortTotal",
		ChangeValue = 1.1,
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			HitVulnerabilityMultiplier = 1.1,
		}
	},
	FirstStrikeMetaUpgrade = -- Fiery Presence
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_FirstStrike",
		Starting = true,
		CostTable = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100 },
		ShortTotal = "FirstStrikeMetaUpgrade_ShortTotal",
		ChangeValue = 1.25,
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			ValidWeapons = WeaponSets.HeroPrimarySecondaryWeapons,
			HitMaxHealthMultiplier = 1.25,
		}
	},

	StoredAmmoVulnerabilityMetaUpgrade = -- Boiling Blood
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_AmmoVulnerability",
		Starting = true,
		CostTable = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "StoredAmmoVulnerabilityMetaUpgrade_ShortTotal",
		ChangeValue = 1.1,
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			ValidWeapons = WeaponSets.HeroPrimarySecondaryWeapons,
			StoredAmmoMultiplier = 1.1,
			HitMaxHealthMultiplier = 1.1,
			HitVulnerabilityMultiplier = 1.1,
		}
	},
	StoredAmmoSlowMetaUpgrade = -- Abyssal Blood
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_UnstoredAmmoVulnerability",
		Starting = true,
		CostTable = { 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "StoredAmmoSlowMetaUpgrade_ShortTotal",
		ChangeValue = 1.1,
		FormatAsPercent = true,
		PreEquipWeapon = "StoredAmmoSlowApplicator",
		ChangeValue = 1.04, -- display variable, change below value to affect gameplay
		PropertyChanges =
		{
			{
				WeaponName = "StoredAmmoSlowApplicator",
				EffectName = "StoredAmmoSlowReduceDamageOutput",
				EffectProperty = "Modifier",
				ChangeValue = -0.04,
				ChangeType = "Add",
			},
			{
				WeaponName = "StoredAmmoSlowApplicator",
				EffectName = "StoredAmmoSlow",
				EffectProperty = "Modifier",
				ChangeValue = -0.04,
				ChangeType = "Add",
			},
		},

	},

	UnstoredAmmoVulnerabilityMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_UnstoredAmmoVulnerability",
		Starting = true,
		CostTable = { 10, 30, 50, 70, 90 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "UnstoredAmmoVulnerabilityMetaUpgrade_ShortTotal",
		ChangeValue = 1.1,
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			ValidWeapons = WeaponSets.HeroNonPhysicalWeapons,
			UnstoredAmmoMultiplier = 1.1,
		}
	},

	VulnerabilityEffectBonusMetaUpgrade = -- Privileged Status
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_EffectVulnerability",
		Starting = true,
		CostTable = { 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "VulnerabilityEffectBonusMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "VulnerabilityEffectBonusMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1.15,
		FormatAsPercent = true,
		AddOutgoingDamageModifiers =
		{
			MinRequiredVulnerabilityEffects = 1,
			PerVulnerabilityEffectAboveMinMultiplier = 1.15,
		}
	},

	GodEnhancementMetaUpgrade = -- Family Favourite
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_GodEnhancement",
		Starting = true,
		CostTable = { 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "GodEnhancementMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "GodEnhancementMetaUpgrade_ShortTotalNoIcon",
		InRunTooltip = "GodEnhancementMetaUpgrade_InRun",
		InRunValueFunctionName = "GetTotalGodEnhancement",
		ChangeValue = 1.01,
		DecimalPlaces = 1,
		AddOutgoingDamageModifiers =
		{
			PerUniqueGodMultiplier = 1.01,
		}
	},

	ExtraChanceMetaUpgrade = -- Death Defiance
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_ExtraChance",
		Starting = true,
		CostTable = { 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "ExtraChanceMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ExtraChanceMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
		KeywordOverride =
		{
			Key = "ExtraChance",
			Value = "ExtraChance",
		},
	},


	ExtraChanceWrathMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_ExtraChance",
		Starting = true,
		CostTable = { 30, 500, 1000 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "ExtraChanceWrathMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ExtraChanceWrathMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	ExtraChanceReplenishMetaUpgrade=
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_ExtraChanceReplenish",
		Starting = true,
		CostTable = { 600 },
		Color = { 255, 255, 255, 255 },
		ShortTotal = "ExtraChanceReplenishMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ExtraChanceReplenishMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
		HealPercent = 0.3,
		KeywordOverride =
		{
			Key = "ExtraChance",
			Value = "ExtraChanceAlt",
		},
		HelpTextTable =
		{
			[0] = "ExtraChanceReplenishMetaUpgrade_Off",
			[1] = "ExtraChanceReplenishMetaUpgrade_On",
		},
	},

	RallyMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		RequiredAccumulatedMetaPoints = 200,
		ResourceName = "LockKeys",
		UnlockCost = 6,
		CostTable = { 40, 60, 100, 200 },
		ShortTotal = "RallyMetaUpgrade_ShortTotal",
		ChangeValue = 1.15,
		FormatAsPercent = true,
	},

	MoneyMetaUpgrade = -- Deep Pockets
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_StartingMoney",
		RequiredAccumulatedMetaPoints = 120,
		Starting = true,
		Cost = 5,
		MaxInvestment = 100,
		ShortTotal = "MoneyMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "MoneyMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 5,
	},

	InterestMetaUpgrade = -- Golden Touch
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_Interest",
		RequiredAccumulatedMetaPoints = 120,
		Starting = true,
		CostTable = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250 },
		ShortTotal = "InterestMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "InterestMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1.025,
	},

	RareBoonDropMetaUpgrade = -- Olympian Favour
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_RareBoonChance",
		RequiredAccumulatedMetaPoints = 500,
		Starting = true,
		Cost = 20,
		MaxInvestment = 80,
		ShortTotal = "RareBoonDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.01,
	},

	EpicBoonDropMetaUpgrade = -- God's Pride
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_EpicBoonChance",
		RequiredAccumulatedMetaPoints = 1000,
		Starting = true,
		Cost = 50,
		MaxInvestment = 60,
		ShortTotal = "EpicBoonDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.01,
	},

	DuoRarityBoonDropMetaUpgrade = -- God's Legacy
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DuoRarityBoon",
		Starting = true,
		Cost = 75,
		MaxInvestment = 50,
		ShortTotal = "DuoRarityBoonDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.01,
	},

	EpicHeroicBoonMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_EpicHeroicBoon",
		Starting = true,
		Cost = 250,
		MaxInvestment = 10,
		ShortTotal = "EpicHeroicBoonMetaUpgrade_ShortTotal",
		ChangeValue = 1.01,
	},

	RunProgressRewardMetaUpgrade = -- Dark Foresight
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_EpicHeroicBoon",
		Starting = true,
		Cost = 50,
		MaxInvestment = 30,
		ShortTotal = "RunProgressRewardMetaUpgrade_ShortTotal",
		ChangeValue = 1.02,
	},

	RerollMetaUpgrade = -- Fated Authority
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_Reroll",
		Starting = true,
		Cost = 250,
		MaxInvestment = 50,
		ShortTotal = "RerollMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "RerollMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	RerollPanelMetaUpgrade = -- Fated Persuasion
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_RerollPanel",
		Starting = true,
		Cost = 250,
		MaxInvestment = 50,
		ShortTotal = "RerollPanelMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "RerollPanelMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	LimitMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		Cost = 1,
		CostIncreaseInterval = 1,
		CostIncrease = 1,
		ShortTotal = "LimitMetaUpgrade_ShortTotal",
		ChangeValue = 1.02,
	},

	SpeedMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		Cost = 50,
		CostIncreaseInterval = 1,
		CostIncrease = 50,
		ShortTotal = "SpeedMetaUpgrade_ShortTotal",
		PropertyChanges =
		{
			{
				UnitProperty = "Speed",
				ChangeValue = 100,
				ChangeType = "Add",
			},
		},
	},

	-- Shrine/Difficulty/Heat MetaUpgrades
	MetaPointCapShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_DarknessCap",
		Starting = true,
		CostTable = { 1, 1, 1, 1, 1 },
		--CostTable = { 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 },
		NoPointsHelpTextId = "MetaPointCapShrineUpgrade_NoPoints",
		ShortTotal = "MetaPointCapShrineUpgrade_ShortTotal",
		BaseValue = 3000,
		ChangeValue = -500,
	},

	MetaUpgradeStrikeThroughShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_DarknessCap",
		Starting = true,
		CostTable = { 2, 2, 2, 2 },
		NoPointsHelpTextId = "MetaUpgradeStrikeThroughShrineUpgrade_NoPoints",
		ShortTotal = "MetaUpgradeStrikeThroughShrineUpgrade_ShortTotal",
		ChangeValue = -3,

		GameStateRequirements =
		{
			RequiredMetaUpgradeStageUnlocked = 4
		},
		DisablesMetaUpgrades = true, -- Alt name "MetaMetaUpgrade" rejected for being too confusing
	},
	HealingReductionShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_HealingReduction",
		Starting = true,
		CostTable = { 1, 1, 1, 1 },
		ShortTotal = "HealingReductionShrineUpgrade_ShortTotal",
		ShortTotalNoIcon = "HealingReductionShrineUpgrade_ShortTotalNoIcon",
		ChangeValue = 1.25,
	},

	ReducedLootChoicesShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_LockedChoice",
		Starting = true,
		CostTable = { 2, 3 },
		ShortTotal = "ReducedLootChoicesShrineUpgrade_ShortTotal",
		ChangeValue = 1,
	},

	ShopPricesShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_ShopPrices",
		Starting = true,
		Cost = 1,
		MaxInvestment = 2,
		ShortTotal = "ShopPricesShrineUpgrade_ShortTotal",
		ChangeValue = 1.4,
	},

	EnemyHealthShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_EnemyHealth",
		Starting = true,
		Cost = 1,
		MaxInvestment = 2,
		ShortTotal = "EnemyHealthShrineUpgrade_ShortTotal",
		ShortTotalNoIcon = "EnemyHealthShrineUpgrade_ShortTotalNoIcon",
		ChangeValue = 1.15,
	},

	EnemyDamageShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_EnemyDamage",
		Starting = true,
		Cost = 1,
		MaxInvestment = 5,
		ShortTotal = "EnemyDamageShrineUpgrade_ShortTotal",
		ChangeValue = 1.20,
	},

	TrapDamageShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_TrapDamage",
		Starting = true,
		Cost = 1,
		MaxInvestment = 1,
		ShortTotal = "EnemyDamageShrineUpgrade_ShortTotal",
		ChangeValue = 5,
		FormatAsPercent = true,
		HelpTextTable =
		{
			[0] = "TrapDamageShrineUpgrade_Off",
			[1] = "TrapDamageShrineUpgrade_On",
		},
	},

	EnemySpeedShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_EnemySpeed",
		Starting = true,
		Cost = 3,
		MaxInvestment = 2,
		ShortTotal = "EnemySpeedShrineUpgrade_ShortTotal",
		ChangeValue = 1.2,
		--ChangeValues = { 1.1, 1.25, 1.5 },
		--[[
		HelpTextTable =
		{
			[0] = "EnemySpeedShrineUpgrade_0",
			[1] = "EnemySpeedShrineUpgrade_1",
			[2] = "EnemySpeedShrineUpgrade_2",
			[3] = "EnemySpeedShrineUpgrade_3"
		},
		]]
	},

	EnemyShieldShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_ShieldHealth",
		Starting = true,
		CostTable = { 1, 1 },
		ShortTotal = "EnemyShieldShrineUpgrade_ShortTotal",
		ShortTotalNoIcon = "EnemyShieldShrineUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	EnemyCountShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_EnemyCount",
		Starting = true,
		CostTable = { 1, 1, 1 },
		ShortTotal = "EnemyCountShrineUpgrade_ShortTotal",
		ChangeValue = 1.20,
	},

	MinibossCountShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_MinibossCount",
		Starting = true,
		CostTable = { 2 },
		ShortTotal = "MinibossCountShrineUpgrade_ShortTotal",
		ShortTotalNoIcon = "MinibossCountShrineUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
		HelpTextTable =
		{
			[0] = "MinibossCountShrineUpgrade_Off",
			[1] = "MinibossCountShrineUpgrade_On",
		},
	},

	EnemyEliteShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_EnemyElites",
		Starting = true,
		CostTable = { 2, 3 },
		ShortTotal = "EnemyEliteShrineUpgrade_ShortTotal",
		ShortTotalNoIcon = "EnemyEliteShrineUpgrade_ShortTotalNoIcon",
		ChangeValue = 1,
	},

	ForceSellShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_ForceSell",
		Starting = true,
		CostTable = { 2 },
		ShortTotal = "ForceSellShrineUpgrade_ShortTotal",
		ChangeValue = 1,
		HelpTextTable =
		{
			[0] = "ForceSellShrineUpgrade_Off",
			[1] = "ForceSellShrineUpgrade_On",
		},
	},

	BossDifficultyShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_BossDifficulty",
		Starting = true,
		CostTable = { 1, 2, 3, 4 },
		ShortTotal = "BossDifficultyShrineUpgrade_ShortTotal",
		ChangeValue = 1,
		GameStateRequirements =
		{
			RequiredTextLines = { "Fury2FirstAppearance", "Fury3FirstAppearance" }
		},
		RankGameStateRequirements = 
		{
			[4] = { RequiredCosmetics = { "HadesEMFight"}}
		}
	},

	HarpyDifficultyShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Skip = true,
		CostTable = { 1, 1 },
		ShortTotal = "HarpyDifficultyShrineUpgrade_ShortTotal",
		ChangeValue = 1,
		GameStateRequirements =
		{
			RequiredTextLines = { "Fury2FirstAppearance", "Fury3FirstAppearance" }
		},
	},
	HydraDifficultyShrineUpgrade =
	{
		Skip = true,
		InheritFrom = { "BaseMetaUpgrade", },
		CostTable = { 1 },
		ShortTotal = "HydraDifficultyShrineUpgrade_ShortTotal",
		ChangeValue = 1,
	},


	HardEncounterShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Starting = true,
		CostTable = { 2, 2, 2 },
		ShortTotal = "HardEncounterShrineUpgrade_ShortTotal",
		ChangeValue = 1,
	},

	BiomeSpeedShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_BiomeSpeed",
		Starting = true,
		CostTable = { 1, 2, 3 },
		ShortTotal = "BiomeSpeedShrineUpgrade_ShortTotal",
		HelpTextTable =
		{
			[0] = "BiomeSpeedShrineUpgrade_0",
			[1] = "BiomeSpeedShrineUpgrade_1",
			[2] = "BiomeSpeedShrineUpgrade_2",
			[3] = "BiomeSpeedShrineUpgrade_3"
		},
		ChangeValue = 2,
		BaseValue = 9,
	},

	NoInvulnerabilityShrineUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "ShrineIcon_NoInvulnerability",
		Starting = true,
		CostTable = { 1 },
		ShortTotal = "NoInvulnerabilityShrineUpgrade_ShortTotal",
		ChangeValue = 2,
		FormatAsPercent = true,
		HelpTextTable =
		{
			[0] = "NoInvulnerabilityShrineUpgrade_Off",
			[1] = "NoInvulnerabilityShrineUpgrade_On",
		},
		GameStateRequirements =
		{
			RequiredTrueFlags = { "HardMode", },
		},
	}
}

MetaUpgradeLockOrder =
{
	BaseUnlocked = 4,
	LockedSetsCount = 2,
	LockedSetCosts = { 2, 4, 8, 16 }
}

MetaUpgradeOrder =
{
	{ "BackstabMetaUpgrade", "FirstStrikeMetaUpgrade" },
	{ "DoorHealMetaUpgrade", "DarknessHealMetaUpgrade" },
	{ "ExtraChanceMetaUpgrade", "ExtraChanceReplenishMetaUpgrade" },
	{ "StaminaMetaUpgrade", "PerfectDashMetaUpgrade" },
	{ "StoredAmmoVulnerabilityMetaUpgrade", "StoredAmmoSlowMetaUpgrade" },
	{ "AmmoMetaUpgrade", "ReloadAmmoMetaUpgrade" },
	{ "MoneyMetaUpgrade", "InterestMetaUpgrade" },
	{ "HealthMetaUpgrade", "HighHealthDamageMetaUpgrade" },
	{ "VulnerabilityEffectBonusMetaUpgrade", "GodEnhancementMetaUpgrade" },
	{ "RareBoonDropMetaUpgrade", "RunProgressRewardMetaUpgrade" },
	{ "EpicBoonDropMetaUpgrade", "DuoRarityBoonDropMetaUpgrade" },
	{ "RerollMetaUpgrade", "RerollPanelMetaUpgrade" },
}

BiomeTimeLimits =
{
	ValidBiomes = { "Tartarus", "Asphodel", "Elysium", "Styx" },
	-- corresponds to BiomeList
	Penalty =
	{
		Damage = 5,
		Interval = 1,
	},
	Timers =
	{
		{ 0, 540, 540, 540, 540 },
		{ 0, 420, 420, 420, 420 },
		{ 0, 300, 300, 300, 300 },
	}
}

RerollCosts =
{
	Boon = 1,
	Shop = 1,
	SellTrait = 1,
	Hammer = -1, -- Disabled
	ReuseIncrement = 1,
}

ShrineUpgradeOrder =
{
	"EnemyDamageShrineUpgrade",
	"HealingReductionShrineUpgrade",
	"ShopPricesShrineUpgrade",
	"EnemyCountShrineUpgrade",
	"BossDifficultyShrineUpgrade",

	"EnemyHealthShrineUpgrade",
	"EnemyEliteShrineUpgrade",
	"MinibossCountShrineUpgrade",
	"ForceSellShrineUpgrade",
	"EnemySpeedShrineUpgrade",

	"TrapDamageShrineUpgrade",
	"MetaUpgradeStrikeThroughShrineUpgrade",
	"EnemyShieldShrineUpgrade",
	"ReducedLootChoicesShrineUpgrade",
	"BiomeSpeedShrineUpgrade",
	"NoInvulnerabilityShrineUpgrade",
}

ShrineClearData =
{
	ClearThreshold = 1,
	BossRoomNames = { "A_Boss", "B_Boss01", "C_Boss01", "D_Boss01" },
}