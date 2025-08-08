import mysql.connector

# Database connection config
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'dnd_game'
}

# All INSERT statements (split with semicolons for compatibility)
insert_statements = [

    # Race Table
    """
    INSERT IGNORE INTO Race (RaceID) VALUES (301);
    INSERT IGNORE INTO Race (RaceID) VALUES (303);
    INSERT IGNORE INTO Race (RaceID) VALUES (304);
    INSERT IGNORE INTO Race (RaceID) VALUES (305);
    """,

    # Class Table
    """
    INSERT IGNORE INTO Class (ClassID) VALUES (201);
    INSERT IGNORE INTO Class (ClassID) VALUES (202);
    INSERT IGNORE INTO Class (ClassID) VALUES (203);
    INSERT IGNORE INTO Class (ClassID) VALUES (204);
    """,

    # Player Table
    """
    INSERT IGNORE INTO Player (PlayerID, Name) VALUES (101, 'Arin');
    INSERT IGNORE INTO Player (PlayerID, Name) VALUES (102, 'Brenna');
    INSERT IGNORE INTO Player (PlayerID, Name) VALUES (103, 'Cedric');
    INSERT IGNORE INTO Player (PlayerID, Name) VALUES (104, 'Daria');
    INSERT IGNORE INTO Player (PlayerID, Name) VALUES (105, 'Elandor');
    """,

    # Character Table
    """
    INSERT IGNORE INTO Character (CharacterID, Name, Level) VALUES (501, 'worf', 10);
    INSERT IGNORE INTO Character (CharacterID, Name, Level) VALUES (502, 'creeger', 12);
    INSERT IGNORE INTO Character (CharacterID, Name, Level) VALUES (503, 'fendal', 15);
    INSERT IGNORE INTO Character (CharacterID, Name, Level) VALUES (504, 'dar', 8);
    INSERT IGNORE INTO Character (CharacterID, Name, Level) VALUES (505, 'edlor', 20);
    """,
    # PlayerCharacter Table
    """
    INSERT IGNORE INTO PlayerCharacter (CharacterID, PlayerID) VALUES (501,  101);
    INSERT IGNORE INTO PlayerCharacter (CharacterID, PlayerID) VALUES (502,  102);
    INSERT IGNORE INTO PlayerCharacter (CharacterID, PlayerID) VALUES (503,  103);
    INSERT IGNORE INTO PlayerCharacter (CharacterID, PlayerID) VALUES (504,  104);
    INSERT IGNORE INTO PlayerCharacter (CharacterID, PlayerID) VALUES (505,  105);
    """,
    # Equipment Table
    """
    INSERT IGNORE INTO Equipment (EquipmentID, Name, Type, Bonus, Rarity, Description, Equipped )
    VALUES (894, 'Longsword of Valor', 'Weapon', '+2 ATK', 'Rare', 'A shining blade blessed by paladins.', TRUE);
    INSERT IGNORE INTO Equipment (EquipmentID, Name, Type, Bonus, Rarity, Description, Equipped)
    VALUES (847, 'Cloak of Shadows', 'Armor', '+1 STEALTH', 'Uncommon', 'Blends with the darkness.', TRUE);
    INSERT IGNORE INTO Equipment (EquipmentID, Name, Type, Bonus, Rarity, Description, Equipped)
    VALUES (857, 'Ring of Fire', 'Accessory', '+1 FIRE DMG', 'Rare', 'Grants control over flame.', TRUE);
    INSERT IGNORE INTO Equipment (EquipmentID, Name, Type, Bonus, Rarity, Description, Equipped)
    VALUES (820, 'Boots of Haste', 'Armor', '+10 SPEED', 'Rare', 'Doubles movement speed.', TRUE);
    INSERT IGNORE INTO Equipment (EquipmentID, Name, Type, Bonus, Rarity, Description, Equipped)
    VALUES (869, 'Amulet of Vitality', 'Accessory', '+15 HP', 'Epic', 'Boosts health significantly.', TRUE);
    """,

    # CharacterEquipment Table
    """
    INSERT IGNORE INTO CharacterEquipment (CharacterID, EquipmentID) VALUES (501, 894);
    INSERT IGNORE INTO CharacterEquipment (CharacterID, EquipmentID) VALUES (502, 847);
    INSERT IGNORE INTO CharacterEquipment (CharacterID, EquipmentID) VALUES (503, 857);
    INSERT IGNORE INTO CharacterEquipment (CharacterID, EquipmentID) VALUES (504, 820);
    INSERT IGNORE INTO CharacterEquipment (CharacterID, EquipmentID) VALUES (505, 869);
    """,

    # Monster Table
    """
    INSERT IGNORE INTO Monster (MonsterID, Name, RaceID, ClassID, CR, HP, AC, Type, XP)
    VALUES (647, 'Goblin Brute', 303, 201, 0.25, 22, 15, 'Beast', 100);
    INSERT IGNORE INTO Monster (MonsterID, Name, RaceID, ClassID, CR, HP, AC, Type, XP)
    VALUES (650, 'Fire Imp', 304, 202, 0.5, 18, 13, 'Fiend', 150);
    INSERT IGNORE INTO Monster (MonsterID, Name, RaceID, ClassID, CR, HP, AC, Type, XP)
    VALUES (626, 'Skeleton Archer', 303, 203, 0.75, 30, 12, 'Undead', 200);
    INSERT IGNORE INTO Monster (MonsterID, Name, RaceID, ClassID, CR, HP, AC, Type, XP)
    VALUES (635, 'Bandit Captain', 301, 201, 1.5, 60, 16, 'Humanoid', 450);
    INSERT IGNORE INTO Monster (MonsterID, Name, RaceID, ClassID, CR, HP, AC, Type, XP)
    VALUES (637, 'Dark Druid', 305, 204, 2.0, 75, 14, 'Caster', 600);
    """,

    # Boss Table
    """
    INSERT IGNORE INTO Boss (BossID, Name, MonsterID, PhaseCount, Lair)
    VALUES (751, 'Goroth the Devourer', 637, 3, 'Ashen Caverns');
    INSERT IGNORE INTO Boss (BossID, Name, MonsterID, PhaseCount, Lair)
    VALUES (733, 'Zeriel the Flameborn', 650, 2, 'Crimson Tower');
    INSERT IGNORE INTO Boss (BossID, Name, MonsterID, PhaseCount, Lair)
    VALUES (735, 'Thornshade', 626, 1, 'Whispering Woods');
    INSERT IGNORE INTO Boss (BossID, Name, MonsterID, PhaseCount, Lair)
    VALUES (746, 'Valkor Doomhammer', 647, 2, 'Broken Citadel');
    INSERT IGNORE INTO Boss (BossID, Name, MonsterID, PhaseCount, Lair)
    VALUES (729, 'Morwenna the Hollow', 635, 4, 'Eclipsed Sanctum');
    """,

    # NPC Table
    """
    INSERT IGNORE INTO NPC (NPCID, Name, Role, Faction, Location)
    VALUES (904, 'Marcus Ironshield', 'Blacksmith', 'Steelguard', 'Forge Town');
    INSERT IGNORE INTO NPC (NPCID, Name, Role, Faction, Location)
    VALUES (993, 'Selene Moonwhisper', 'Merchant', 'Silver Circle', 'Elaria Market');
    INSERT IGNORE INTO NPC (NPCID, Name, Role, Faction, Location)
    VALUES (987, 'Thaddeus Grin', 'Guard', 'Crimson Watch', 'North Gate');
    INSERT IGNORE INTO NPC (NPCID, Name, Role, Faction, Location)
    VALUES (964, 'Lira Sunpetal', 'Healer', 'Verdant Grove', 'Sacred Glade');
    INSERT IGNORE INTO NPC (NPCID, Name, Role, Faction, Location)
    VALUES (984, 'Drogath Stonefist', 'Trainer', 'Stoneclaw Clan', 'Battle Arena');
    """,

    # Event Table
    """
    INSERT IGNORE INTO Event (EventID, Name, Date, Description, Type)
    VALUES (1063, 'Battle of Emberfall', '2024-05-12', 'The city was nearly razed by flame elementals.', 'Battle');
    INSERT IGNORE INTO Event (EventID, Name, Date, Description, Type)
    VALUES (1090, 'Siege of Thornkeep', '2024-06-23', 'A brutal 3-day battle against undead forces.', 'Battle');
    INSERT IGNORE INTO Event (EventID, Name, Date, Description, Type)
    VALUES (1057, 'Festival of Light', '2024-07-15', 'Celebration of the gods’ blessings.', 'Festival');
    INSERT IGNORE INTO Event (EventID, Name, Date, Description, Type)
    VALUES (1087, 'Rogue Uprising', '2024-08-02', 'Thieves guild attacked the capital.', 'Quest');
    INSERT IGNORE INTO Event (EventID, Name, Date, Description, Type)
    VALUES (1004, 'Mystic Eclipse', '2024-09-30', 'A magical event altering mana flows.', 'Quest');
    """,

    # CharacterEvent Table
    """
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID) VALUES (501, 1063);
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID) VALUES (502, 1090);
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID) VALUES (503, 1057);
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID) VALUES (504, 1087);
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID) VALUES (505, 1004);
    """,

    # Achievement Table
    """
    INSERT IGNORE INTO Achievement (AchievementID, Name, Description, XPReward)
    VALUES (1130, 'First Blood', 'Defeat your first enemy.', 100);
    INSERT IGNORE INTO Achievement (AchievementID, Name, Description, XPReward)
    VALUES (1143, 'Explorer', 'Visit 10 unique locations.', 250);
    INSERT IGNORE INTO Achievement (AchievementID, Name, Description, XPReward)
    VALUES (1193, 'Elite Slayer', 'Defeat an elite monster.', 500);
    INSERT IGNORE INTO Achievement (AchievementID, Name, Description, XPReward)
    VALUES (1160, 'Master of Magic', 'Learn 10 spells.', 400);
    INSERT IGNORE INTO Achievement (AchievementID, Name, Description, XPReward)
    VALUES (1116, 'Hero of the Realm', 'Complete the main questline.', 1000);
    """,

    # PlayerAchievement Table
    """
    INSERT IGNORE INTO PlayerAchievement (PlayerID, AchievementID) VALUES (101, 1130);
    INSERT IGNORE INTO PlayerAchievement (PlayerID, AchievementID) VALUES (102, 1143);
    INSERT IGNORE INTO PlayerAchievement (PlayerID, AchievementID) VALUES (103, 1193);
    INSERT IGNORE INTO PlayerAchievement (PlayerID, AchievementID) VALUES (104, 1160);
    INSERT IGNORE INTO PlayerAchievement (PlayerID, AchievementID) VALUES (105, 1116);
    """

    # CharacterEvent Table
    """
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID, Result) VALUES (501, 1063, 'Won');
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID, Result) VALUES (502, 1063, 'Won');
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID, Result) VALUES (503, 1063, 'Lost');
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID, Result) VALUES (504, 1063, 'Lost');
    INSERT IGNORE INTO CharacterEvent (CharacterID, EventID, Result) VALUES (505, 1063, 'Lost');
    """
]

# Initialize connection
conn = None
cursor = None

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for block in insert_statements:
        statements = [s.strip() for s in block.strip().split(';') if s.strip()]
        for stmt in statements:
            try:
                cursor.execute(stmt)
                print("✅ Executed:", stmt[:60] + "...")
            except mysql.connector.Error as err:
                print("❌ Error:", err)
                print("↪ Statement:", stmt)

    conn.commit()
    print("✅ All data inserted successfully.")

except mysql.connector.Error as err:
    print("❌ Connection error:", err)

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
    print("🔌 Connection closed.")
