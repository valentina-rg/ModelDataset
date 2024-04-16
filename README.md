# Vogue Magazine Female Cover Models Skin Tone Data Visualization

This project serves as a data visualization exercise using a dataset representing the skin tone of female cover models of Vogue magazine between 2000 and 2019, by issue.

## Understanding the Dataset

The dataset contains information about female cover models, with each row representing one model's face. Here's a brief overview of the dataset:

- Shape: (262, 4) (262 rows and 4 columns)
- Data types: The dataset consists of a combination of numerical and categorical data.
- No duplicate values are present.
- There are no missing values in the dataset.

## Data Visualization

### Top 10 Models with the Most Magazine Covers

To understand the distribution of magazine covers among models, a pie chart is created to visualize the top 10 models with the most covers. Each slice of the pie represents the percentage of covers for a specific model.

### Most Common Skin Tone Color per Year

To analyze the predominant skin tone color of cover models over the years, a scatter plot is generated. Each point on the plot represents the most common skin tone color for a particular year. The x-axis represents the year, and the y-axis represents the hex value of the skin tone color.

## Libraries Used

- Pandas: For data manipulation and analysis
- Matplotlib: For data visualization

## How to Use

To run the code and visualize the data, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries by running `pip install pandas matplotlib`.
3. Download the dataset (`faces.csv`) and place it in the `data` directory.
4. Execute the Python script (`main.py`) in your preferred environment.

## Author

[Valentina Rigato]

## License

Data available under the MIT License

##Source:
https://github.com/the-pudding/data/tree/master/vogue
