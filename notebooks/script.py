import pandas as pd
import matplotlib.pyplot as plt
import os

# Find project root correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Load data
data_path = os.path.join(project_root, "data", "raw_transactions.csv")
df = pd.read_csv(data_path)

# Create assets folder if not exists
assets_path = os.path.join(project_root, "assets")
os.makedirs(assets_path, exist_ok=True)

# Calculate
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['month'] = df['transaction_date'].dt.to_period('M').astype(str)
mau = df.groupby('month')['customer_id'].nunique()
counts = df['customer_id'].value_counts()
repeat = (counts > 1).sum()
one_time = (counts == 1).sum()

# Create image
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('CUSTOMER SERVICE RETENTION - PROJECT OUTPUT', fontweight='bold')

ax1.bar(mau.index, mau.values, color='#4CAF50')
ax1.set_title('Monthly Active Users')
ax1.tick_params(axis='x', rotation=30)

ax2.pie([repeat, one_time], labels=['Repeat', 'One-Time'], autopct='%1.1f%%', colors=['#2196F3', '#FF9800'])
ax2.set_title('Retention Rate')

output_file = os.path.join(assets_path, "project_output.png")
plt.tight_layout()
plt.savefig(output_file, dpi=150)
print(f"OUTPUT IMAGE CREATED: {output_file}")
print("PROJECT EXECUTION SUCCESSFUL!")