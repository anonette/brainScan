import nibabel as nib
import numpy as np

nifti_file = "dk.nii"
ply_file = "dk_output.ply"

# Load the NIfTI file
img = nib.load(nifti_file)

# Extract the voxel data and intensities
data = img.get_fdata()

# Extract the coordinates
x, y, z = np.where(data != 0)

# Extract the corresponding labels or segmentation information
labels = data[x, y, z].astype(int)

# Get the unique labels and their counts
unique_labels, label_counts = np.unique(labels, return_counts=True)

# Generate a suggested color map based on the unique labels
color_map = {}
for label in unique_labels:
    color_map[label] = np.random.randint(0, 256, size=3).tolist()

# Save the voxel coordinates and colorized labels to the PLY file
with open(ply_file, "w") as f:
    f.write("ply\n")
    f.write("format ascii 1.0\n")
    f.write(f"element vertex {len(x)}\n")
    f.write("property float x\n")
    f.write("property float y\n")
    f.write("property float z\n")
    f.write("property uchar red\n")
    f.write("property uchar green\n")
    f.write("property uchar blue\n")
    f.write("end_header\n")
    for i in range(len(x)):
        label = labels[i]
        color = color_map.get(label, (0, 0, 0))
        f.write(f"{x[i]} {y[i]} {z[i]} {color[0]} {color[1]} {color[2]}\n")
