import mysql.connector

# --- Connection Configuration ---
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'dnd_game'
}

# --- Queries ---
queries = [
    {
        "title": "1. Characters and Equipped Equipment",
        "sql": """
            SELECT 
                c.Name AS CharacterName,
                cl.ClassName,
                r.RaceName,
                e.Name AS EquipmentName,
                e.Type AS EquipmentType,
                e.Bonus
            FROM `Character` c
            JOIN `Class` cl ON c.charClassID = cl.ClassID
            JOIN `Race` r ON c.charRaceID = r.RaceID
            JOIN `CharacterEquipment` ce ON c.CharacterID = ce.CharacterID
            JOIN `Equipment` e ON ce.EquipmentID = e.EquipmentID
            WHERE e.Equipped = TRUE
            ORDER BY c.Name, e.Name;
        """
    },
    {
        "title": "2. Characters and Spells by Class",
        "sql": """
            SELECT 
                c.Name AS CharacterName,
                cl.ClassName,
                s.Name AS SpellName,
                s.Level,
                s.School
            FROM `Character` c
            JOIN `Class` cl ON c.charClassID = cl.ClassID
            JOIN `ClassSpell` cs ON cl.ClassID = cs.ClassID
            JOIN `Spell` s ON cs.SpellID = s.SpellID
            ORDER BY c.Name, s.Level;
        """
    },
    {
        "title": "3. Players and Character Events",
        "sql": """
            SELECT
                p.UserName,
                c.Name AS CharacterName,
                e.Name AS EventName,
                e.Date AS EventDate
            FROM `Player` p
            JOIN `PlayerCharacter` pc ON p.PlayerID = pc.PlayerID
            JOIN `Character` c ON pc.CharacterID = c.CharacterID
            JOIN `CharacterEvent` ce ON c.CharacterID = ce.CharacterID
            JOIN `Event` e ON ce.EventID = e.EventID
            ORDER BY p.UserName, e.Date DESC;
        """
    },
    {
        "title": "4. Average Level and Total XP by Class",
        "sql": """
            SELECT
                cl.ClassName,
                AVG(c.Level) AS AvgLevel,
                SUM(c.XP) AS TotalXP
            FROM `Character` c
            JOIN `Class` cl ON c.charClassID = cl.ClassID
            GROUP BY cl.ClassName
            ORDER BY AvgLevel DESC;
        """
    },
    {
        "title": "5. Characters and Battles Won",
        "sql": """
            SELECT
                c.Name AS CharacterName,
                COUNT(DISTINCT e.EventID) AS BattlesWon
            FROM `Character` c
            JOIN `CharacterEvent` ce ON c.CharacterID = ce.CharacterID
            JOIN `Event` e ON ce.EventID = e.EventID
            WHERE e.Type = 'Battle'
              AND ce.Result = 'Won'
            GROUP BY c.Name
            ORDER BY BattlesWon DESC;
        """
    }
]

# --- Main Execution ---
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for q in queries:
        print(f"\n--- {q['title']} ---")
        cursor.execute(q['sql'])

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        if rows:
            print("\t".join(columns))
            for row in rows:
                print("\t".join(str(col) for col in row))
        else:
            print("No results found.")

except mysql.connector.Error as err:
    print(f"\n❌ Database error: {err}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
