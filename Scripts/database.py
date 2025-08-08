import mysql.connector

# Connection parameters
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'dnd_game'
}

# Establish MySQL connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Helper to run queries safely
def execute_query(query):
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

# Create tables in correct order
queries = [

    # 1. Class
    """
    CREATE TABLE IF NOT EXISTS Class (
        ClassID INT PRIMARY KEY,
        ClassName VARCHAR(255),
        HitDie INT,
        PrimaryStat VARCHAR(255),
        Description TEXT
    );
    """,

    # 2. Race
    """
    CREATE TABLE IF NOT EXISTS Race (
        RaceID INT PRIMARY KEY,
        RaceName VARCHAR(255),
        BonusStat VARCHAR(255),
        Description TEXT
    );
    """,

    # 3. Spell
    """
    CREATE TABLE IF NOT EXISTS Spell (
        SpellID INT PRIMARY KEY,
        Name VARCHAR(255),
        Level INT,
        School VARCHAR(255),
        Effect TEXT,
        CastingTime VARCHAR(255),
        Duration VARCHAR(255)
    );
    """,

    # 4. ClassSpell
    """
    CREATE TABLE IF NOT EXISTS ClassSpell (
        ClassID INT,
        SpellID INT,
        PRIMARY KEY (ClassID, SpellID),
        FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
        FOREIGN KEY (SpellID) REFERENCES Spell(SpellID)
    );
    """,

    # 5. Equipment
    """
    CREATE TABLE IF NOT EXISTS Equipment (
        EquipmentID INT PRIMARY KEY,
        Name VARCHAR(255),
        Type VARCHAR(255),
        Bonus VARCHAR(255),
        Rarity VARCHAR(255),
        Description TEXT,
        Equipped BOOLEAN
    );
    """,

    # 6. Achievement
    """
    CREATE TABLE IF NOT EXISTS Achievement (
        AchievementID INT PRIMARY KEY,
        Name VARCHAR(100),
        Description TEXT,
        XPReward INT
    );
    """,

    # 7. Faction
    """
    CREATE TABLE IF NOT EXISTS Faction (
        FactionID INT PRIMARY KEY,
        Name VARCHAR(100),
        Alignment VARCHAR(50),
        Description TEXT
    );
    """,

    # 8. Character
    """
    CREATE TABLE IF NOT EXISTS `Character` (
        CharacterID INT PRIMARY KEY,
        Name VARCHAR(100),
        Level INT,
        charClassID INT,
        XP INT,
        charRaceID INT,
        HP INT,
        Mana INT,
        Alignment VARCHAR(20),
        FOREIGN KEY (charClassID) REFERENCES Class(ClassID),
        FOREIGN KEY (charRaceID) REFERENCES Race(RaceID)
    );
    """,

    # 9. Player
    """
    CREATE TABLE IF NOT EXISTS Player ( 
        PlayerID INT PRIMARY KEY,
        Name VARCHAR(255),
        UserName VARCHAR(255)
    );
    """,

    # 10. PlayerCharacter
    """
    CREATE TABLE IF NOT EXISTS PlayerCharacter (
        PlayerID INT,
        CharacterID INT,
        PRIMARY KEY (PlayerID, CharacterID),
        FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
        FOREIGN KEY (CharacterID) REFERENCES `Character`(CharacterID)
    );
    """,

    # 11. CharacterEquipment
    """
    CREATE TABLE IF NOT EXISTS CharacterEquipment ( 
        CharacterID INT,
        EquipmentID INT,
        PRIMARY KEY (CharacterID, EquipmentID),
        FOREIGN KEY (CharacterID) REFERENCES `Character`(CharacterID),
        FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)
    );
    """,

    # 12. NPC
    """
    CREATE TABLE IF NOT EXISTS NPC (
        NPCID INT PRIMARY KEY,
        Name VARCHAR(100),
        Role VARCHAR(50),
        classID INT,
        raceID INT,
        FactionID INT,
        FOREIGN KEY (classID) REFERENCES Class(ClassID),
        FOREIGN KEY (raceID) REFERENCES Race(RaceID),
        FOREIGN KEY (FactionID) REFERENCES Faction(FactionID)
    );
    """,

    # 13. NPCLocation
    """
    CREATE TABLE IF NOT EXISTS NPCLocation (
        NPCLocID INT PRIMARY KEY,
        NPCID INT,
        Location VARCHAR(100),
        IsCurrent BOOLEAN,
        FOREIGN KEY (NPCID) REFERENCES NPC(NPCID)
    );
    """,

    # 14. Monster
    """
    CREATE TABLE IF NOT EXISTS Monster (
        MonsterID INT PRIMARY KEY,
        Name VARCHAR(100),
        raceID INT,
        classID INT,
        CR FLOAT,
        HP INT,
        AC INT,
        Type VARCHAR(50),
        XP INT,
        FOREIGN KEY (raceID) REFERENCES Race(RaceID),
        FOREIGN KEY (classID) REFERENCES Class(ClassID)
    );
    """,

    # 15. Boss
    """
    CREATE TABLE IF NOT EXISTS Boss (
        BossID INT PRIMARY KEY,
        Name VARCHAR(100),
        MonsterID INT,
        PhaseCount INT,
        Lair VARCHAR(100),
        FOREIGN KEY (MonsterID) REFERENCES Monster(MonsterID)
    );
    """,

    # 16. Event
    """
    CREATE TABLE IF NOT EXISTS Event (
        EventID INT PRIMARY KEY,
        Name VARCHAR(100),
        Date DATE,
        Description TEXT,
        Type VARCHAR(100)
    );
    """,

    # 17. CharacterEvent
    """
    CREATE TABLE IF NOT EXISTS CharacterEvent (
        CharacterID INT,
        EventID INT,
        Result VARCHAR(100),
        PRIMARY KEY (CharacterID, EventID),
        FOREIGN KEY (CharacterID) REFERENCES `Character`(CharacterID),
        FOREIGN KEY (EventID) REFERENCES Event(EventID)
    );
    """,

    # 18. PlayerAchievement
    """
    CREATE TABLE IF NOT EXISTS PlayerAchievement (
        PlayerID INT,
        AchievementID INT,
        PRIMARY KEY (PlayerID, AchievementID),
        FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
        FOREIGN KEY (AchievementID) REFERENCES Achievement(AchievementID)
    );
    """
    
   
]

# Execute queries
for q in queries:
    execute_query(q)

conn.commit()
cursor.close()
conn.close()

print("✅ D&D database schema created successfully!")
