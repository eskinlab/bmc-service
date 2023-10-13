# app.py
from flask import render_template

import pandas as pd
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import io
import base64

from config import app, use_sql


DATA = pd.read_csv('titanic.csv')


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


def get_img_from_plot(plot):
    # Save the plot to a buffer
    buffer = io.BytesIO()
    plot.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert plot buffer to base64-encoded string
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    img = f"<img src='data:image/png;base64,{plot_data}'/>"
    return img


# Show fare histogram
@app.route("/fare_histogram", methods=['GET', 'POST'])
def calculate_fare_histogram():
    if not use_sql:
        fares = DATA['Fare']
    # Split fare data into 10 ranges
    fare_ranges = pd.cut(fares, bins=10)
    # Calculate frequency of fares within each range
    fare_counts = fare_ranges.value_counts().sort_index()
    counts = fare_counts.index.astype(str)
    print(counts)
    values = fare_counts.values

    plt.figure(figsize=(6, 4))
    plt.bar(counts, values, color='blue', width=0.8)

    # Create the histogram using matplotlib
    plt.xlabel('Fare Percent')
    plt.xticks(rotation=45)
    plt.ylabel('Ticket Count')
    plt.title('Fare Histogram')

    image = get_img_from_plot(plt)
    return render_template('fare-histogram.html', image=image)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
