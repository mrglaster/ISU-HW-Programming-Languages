import pandas as pd
import matplotlib.pyplot as plt


def get_data():
    data = pd.read_csv('data.csv', sep='\t', header=None, names=['timestamp', 'type', 'value'])
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data


def draw_smoothed_photo_resistor_data(ax, data):
    data_sorted = data[data['type'] == 'p'].sort_values(by='timestamp')
    print(f"Photoresistor records: {len(data_sorted)}")
    data_filtered = data_sorted[(data_sorted['timestamp'] >= '2023-12-17')]
    data_smoothed = data_filtered['value'].rolling(window=60).mean()
    ax.plot(data_filtered['timestamp'], data_smoothed, label='Smoothed p', drawstyle='steps-mid')
    ax.set_title('Smoothed Photo Resistor Data')
    ax.set_ylabel('Smoothed Value of p')
    ax.legend()

    # Return min and max timestamps
    return data_filtered['timestamp'].min(), data_filtered['timestamp'].max()


def draw_tap_data(ax, data, xlim_min, xlim_max):
    data_sorted = data[data['type'] == 't'].sort_values(by='timestamp')
    x = data_sorted['timestamp']
    y = range(1, len(data_sorted) + 1)
    ax.stem(x, y, label='Tap')
    ax.set_title('Tap Data')
    ax.set_ylabel('Times Button was Pressed')
    ax.legend()

    # Set x-axis limits
    ax.set_xlim(xlim_min, xlim_max)


def draw_magnet_data(ax, data, xlim_min, xlim_max):
    data_sorted = data[data['type'] == 'm'].sort_values(by='timestamp')
    x = data_sorted['timestamp']
    y = range(1, len(data_sorted) + 1)
    ax.stem(x, y, label='Magnet')
    ax.set_title('Magnet Data')
    ax.set_xlabel('Time')  # Only the last subplot needs xlabel
    ax.set_ylabel('Times Magnet was Pressed')
    ax.legend()

    # Set x-axis limits
    ax.set_xlim(xlim_min, xlim_max)


def main():
    data = get_data()

    # Create subplots with 3 rows and 1 column, sharing the x-axis
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 18))

    xlim_min, xlim_max = draw_smoothed_photo_resistor_data(ax1, data)
    draw_tap_data(ax2, data, xlim_min, xlim_max)
    draw_magnet_data(ax3, data, xlim_min, xlim_max)

    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()


if __name__ == '__main__':
    main()
