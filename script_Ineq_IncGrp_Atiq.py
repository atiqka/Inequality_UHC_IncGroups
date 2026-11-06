import matplotlib
matplotlib.use("Agg")   # safer backend for macOS scripts
import matplotlib.pyplot as plt
import pandas as pd
import ineqpy.inequality as ineq

# Load your local CSV file
data_path = "/Users/atiq/Atiq_R-test/macro6_data_17Jan2025.csv"
df = pd.read_csv(data_path)

# Keep relevant columns, now using UHC_SCI
uhc_data = df[['countryname', 'uhc_sci', 'inc_grp', 'pop']].dropna()

# --- Define desired order of income groups ---
ordered_groups = ["High income", "Upper middle income", "Lower middle income", "Low income"]

# --- Faceted plots by income group using ineqpy ---
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, inc_grp in enumerate(ordered_groups):
    subset = uhc_data[uhc_data['inc_grp'] == inc_grp]
    uhc_values = subset['uhc_sci'].values
    pop_weights = subset['pop'].values
    
    # Lorenz curve from ineqpy (returns DataFrame)
    lorenz_df = ineq.lorenz(uhc_values, weights=pop_weights)
    
    # Gini coefficient (population-weighted)
    gini_val = ineq.gini(uhc_values, weights=pop_weights)
    
    # Plot using DataFrame columns (iloc for safety)
    axes[i].plot(lorenz_df.iloc[:,0], lorenz_df.iloc[:,1],
                 label="Lorenz Curve (pop-weighted)", color="blue", linewidth=2)
    axes[i].plot([0,1], [0,1], label="Line of Equality", color="red", linestyle="--", linewidth=2)
    axes[i].fill_between(lorenz_df.iloc[:,0], lorenz_df.iloc[:,1],
                         lorenz_df.iloc[:,0], color="lightblue", alpha=0.5)
    axes[i].set_title(f"{inc_grp} (Pop-weighted Gini={gini_val:.3f})")
    axes[i].set_xlabel("Cumulative Share of Population")
    axes[i].set_ylabel("Cumulative Share of UHC-SCI")
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.savefig("/Users/atiq/Pyvs_2026/lorenz_facets_uhc_ordered.png", dpi=300)
print("Population-weighted Lorenz facet plot saved to /Users/atiq/Pyvs_2026/lorenz_facets_uhc_ordered.png")
