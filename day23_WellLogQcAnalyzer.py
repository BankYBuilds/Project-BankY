
import pandas as pd
import matplotlib.pyplot as plt

# Load well log data
data = pd.read_csv("well_log_data.csv")

# Extract well log curves
depth = data["DEPTH"]
gr = data["GR"]
res = data["RES"]
nphi = data["NPHI"]
rhob = data["RHOB"]



print("========== WELL LOG QC REPORT ==========")

missing_values = data.isna().sum()

print("\nMissing Values:")
print(missing_values)

duplicate_depths = depth.duplicated().sum()

print(f"\nDuplicate Depths: {duplicate_depths}")

depth_ordered = depth.is_monotonic_increasing

print(f"Depth Ordered: {depth_ordered}")

negative_gr = (gr < 0).sum()
negative_res = (res < 0).sum()
negative_nphi = (nphi < 0).sum()
negative_rhob = (rhob < 0).sum()

print("\nNegative Values:")
print(f"GR: {negative_gr}")
print(f"RES: {negative_res}")
print(f"NPHI: {negative_nphi}")
print(f"RHOB: {negative_rhob}")

q1 = gr.quantile(0.25)
q3 = gr.quantile(0.75)

iqr = q3 - q1

lower_boundary = q1 - 1.5 * iqr
upper_boundary = q3 + 1.5 * iqr

lower_outlier_count = (gr < lower_boundary).sum()
upper_outlier_count = (gr > upper_boundary).sum()

print("\nGR Outlier Detection:")
print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Lower Boundary: {lower_boundary:.2f}")
print(f"Upper Boundary: {upper_boundary:.2f}")
print(f"Potential Low Outliers: {lower_outlier_count}")
print(f"Potential High Outliers: {upper_outlier_count}")

print("\n========== QC CHECK COMPLETE ==========")



sort_depth = data.sort_values("DEPTH")
print (sort_depth)

data = sort_depth
depth = data["DEPTH"]
gr = data["GR"]
res = data["RES"]
nphi = data["NPHI"]
rhob = data["RHOB"]


lower_outlier = (gr < lower_boundary)
upper_outlier = (gr > upper_boundary)
lower_gr_outliers = gr[lower_outlier]
upper_gr_outliers = gr[upper_outlier]

lower_depth_outliers = depth[lower_outlier]
upper_depth_outliers = depth[upper_outlier]

plt.plot(gr, depth, label="GR")

plt.scatter(
    lower_gr_outliers,
    lower_depth_outliers,
    label="Low Outliers"
)

plt.scatter(
    upper_gr_outliers,
    upper_depth_outliers,
    label="High Outliers"
)

plt.xlabel("Gamma Ray (GR)")
plt.ylabel("Depth")
plt.title("Gamma Ray vs Depth — QC Analysis")

plt.gca().invert_yaxis()
plt.grid()
plt.legend()

plt.show()