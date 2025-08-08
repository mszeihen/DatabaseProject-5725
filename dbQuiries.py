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
                e.Name AS EquipmentName,
                e.Type,
                e.Bonus,
                e.Rarity
            FROM 
                `Character` c
            JOIN 
                CharacterEquipment ce ON c.CharacterID = ce.CharacterID
            JOIN 
                Equipment e ON ce.EquipmentID = e.EquipmentID
            WHERE 
                e.Equipped = TRUE
            ORDER BY c.Name;
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
                p.Name AS PlayerName,
                e.Name AS EventName,
                e.Date AS EventDate
            FROM 
                Player p
            JOIN 
                PlayerCharacter pc ON p.PlayerID = pc.PlayerID
            JOIN 
                CharacterEvent ce ON pc.CharacterID = ce.CharacterID
            JOIN 
                Event e ON ce.EventID = e.EventID
            ORDER BY 
                p.Name ASC,
                e.Date ASC;
        """
    },
    {
        "title": "4. Average Level and Total XP by Class",
        "sql": """
            SELECT 
                cl.ClassName,
                AVG(c.Level) AS AverageLevel,
                SUM(c.XP) AS TotalXP
            FROM 
                `Character`  c
            JOIN 
                Class cl ON c.charClassID = cl.ClassID
            GROUP BY 
                cl.ClassName;
        """
    },
    {
        "title": "5. Characters and Battles Won",
        "sql": """
            SELECT 
            c.Name AS CharacterName,
            e.Name AS EventName,
            e.Date AS EventDate
            FROM 
                `Character`  c
            JOIN 
                CharacterEvent ce ON c.CharacterID = ce.CharacterID
            JOIN 
                Event e ON ce.EventID = e.EventID
            WHERE 
                ce.Result = 'Won'
                AND e.Type = 'Battle';
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
