import os
import subprocess

# Replace with your actual MySQL credentials
USER = "root"
PASSWORD = "1234"
HOST = "localhost"
PORT = "3306"
DB = "dnd_game"

# === Output files ===
ER_FILE = "erd_output.er"
DOT_FILE = "erd_output.dot"
PNG_FILE = "erd_output.png"

# Step 1: Generate .er file from MySQL
eralchemy_cmd = f"eralchemy -i mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB} -o {ER_FILE}"
print(f"Running: {eralchemy_cmd}")
os.system(eralchemy_cmd)

# Step 2: Convert .er to .dot (Graphviz format)
eralchemy_to_dot_cmd = f"eralchemy -i {ER_FILE} -o {DOT_FILE}"
print(f"Running: {eralchemy_to_dot_cmd}")
os.system(eralchemy_to_dot_cmd)

# Step 3: Convert .dot to .png using Graphviz
dot_to_png_cmd = f"dot -Tpng {DOT_FILE} -o {PNG_FILE}"
print(f"Running: {dot_to_png_cmd}")
subprocess.run(dot_to_png_cmd, shell=True, check=True)

print(f"✅ PNG ER Diagram created: {PNG_FILE}")