import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

# Update the path below
file_path = '/path/to/results/results.xlsx'

df = pd.read_excel(file_path)

fig, ax = plt.subplots()

image_resolutions = {}
datasets = {}

markers = cycle(['o', 's', 'D', '^', 'v', 'P', 'X'])

marker_size = 80

# Loop through the DataFrame and plot data for each combination of image resolution and dataset
for index, row in df.iterrows():
    dataset = row['Dataset']
    image_resolution = row['Image Resolution']
    time = row['Time']
    accuracy = row['Accuracy']

    if image_resolution not in image_resolutions:
        image_resolutions[image_resolution] = next(markers)

    if dataset not in datasets:
        datasets[dataset] = (len(datasets) + 1, f'C{len(datasets)}')

    color_index, color = datasets[dataset]

    ax.scatter(time, accuracy, label=f'{dataset}', marker=image_resolutions[image_resolution], c=color, edgecolor='black', s=marker_size)

ax.set_ylim(0, 1)

ax.set_xlabel('Time [s]', fontsize=16)

ax.set_ylabel('Accuracy', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=14)

legend1_elements = [plt.Line2D([], [], marker='None', color=color, label=dataset) for dataset, (_, color) in datasets.items()]
legend1 = ax.legend(handles=legend1_elements, title='Datasets', loc='center left', bbox_to_anchor=(0.415, 0.185))

custom_legend_elements = [plt.Line2D([], [], marker=marker, color='k', linestyle='None', markersize=6) for marker in image_resolutions.values()]
legend2 = ax.legend(custom_legend_elements, image_resolutions.keys(),
                    title='Image Resolution', loc='center right', bbox_to_anchor=(1.01, 0.24), ncol=1, markerscale=1.5)

ax.add_artist(legend1)
ax.add_artist(legend2)

plt.title('GIST', fontsize=20)

plt.show()

plt.savefig('GIST_accuracy_vs_time.png', dpi=250)