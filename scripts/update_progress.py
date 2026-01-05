import pandas as pd

# Read Weekly_Checklist.xlsx to calculate progress
excel_file = 'Weekly_Checklist.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Calculate completed tasks percentage
completed_tasks = (df['Status'].str.lower() == 'completed').sum()
total_tasks = len(df)
progress_percentage = int((completed_tasks / total_tasks) * 100)

# Update README.md with progress badge or text
readme_file = 'README.md'
with open(readme_file, 'r') as f:
    readme_content = f.read()

# Prepare progress section
progress_text = f"\n## 📊 Progress\n![Progress](https://img.shields.io/badge/Progress-{progress_percentage}%25-brightgreen)\n"

import re
if '## 📊 Progress' in readme_content:
    # Replace existing progress section
    readme_content = re.sub(r'## 📊 Progress.*', progress_text, readme_content, flags=re.DOTALL)
else:
    # Append progress section
    readme_content += progress_text

# Save updated README.md
# with open(readme_file, 'w') as f:
#     f.write(readme_content)
