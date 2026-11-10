import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_excel('Dash_Sales_Data.xlsx')

# Create the interactive figure
fig = px.pie(
    df, 
    names='Month', 
    values='Sales', 
    title='Sales Distribution by Month',
    hole=0.3
)

# Custom HTML layout wrapper with styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Sales Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1f4e78;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Interactive Sales Dashboard</h1>
        {fig.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
</body>
</html>
"""

# Save as index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generated successfully!")