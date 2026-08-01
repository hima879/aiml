import numpy as np

try:
    import pandas as pd  # type: ignore[import-not-found]
except ModuleNotFoundError:
    pd = None

try:
    from sklearn.preprocessing import StandardScaler  # type: ignore[import-not-found]
    from sklearn.cluster import KMeans  # type: ignore[import-not-found]
except ModuleNotFoundError:
    StandardScaler = None
    KMeans = None

import matplotlib.pyplot as plt

if pd is None:
    raise ModuleNotFoundError("pandas is required to run this script.")

data = {
    'Customer': ['A','B','C','D','E','F','G','H','I','J'],
    'Recency': [5, 10, 3, 250, 300, 8, 200, 15, 30, 280],
    'Frequency': [20, 5, 25, 1, 1, 15, 2, 8, 3, 1],
    'Monetary': [5000, 800, 6000, 50, 30, 3000, 100, 1200, 400, 60]
}
df = pd.DataFrame(data)
print("Raw Data:")
print(df)

df['Monetary_log'] = np.log1p(df['Monetary'])
scaler = StandardScaler()
features = ['Recency', 'Frequency', 'Monetary_log']
df_scaled = scaler.fit_transform(df[features])
print("\nScaled Data (mean=0, std=1):")
print(pd.DataFrame(df_scaled, columns=features))

# 4. Apply K-Means with k=2 (just to see groups)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

print("\nClustered Customers:")
print(df[['Customer', 'Recency', 'Frequency', 'Monetary', 'Cluster']])
print("\nCluster Centers (in original scale):")
for cluster_id in [0, 1]:
    cluster_data = df[df['Cluster'] == cluster_id]
    print(f"Cluster {cluster_id}: {len(cluster_data)} customers")
    print(f"  Avg Recency: {cluster_data['Recency'].mean():.1f} days")
    print(f"  Avg Frequency: {cluster_data['Frequency'].mean():.1f} orders")
    print(f"  Avg Monetary: £{cluster_data['Monetary'].mean():,.2f}")
    print()

# Elbow method for k=1 to 6
inertias = []
for k in range(1, 7):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df_scaled)
    inertias.append(km.inertia_)

plt.plot(range(1, 7), inertias, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.grid(True)
plt.show()