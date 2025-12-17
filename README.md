# YouTube Analysis 2023

A comprehensive data analysis project that explores YouTube channel statistics and trends using Python, Pandas, and Seaborn visualization library.

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Analysis Functions](#analysis-functions)
- [Visualizations](#visualizations)
- [Author](#author)

---

## 🎯 Overview

This project analyzes the "Global YouTube Statistics 2023" dataset to extract meaningful insights about YouTube channels, their growth patterns, earnings, geographic distribution, and relationships between various metrics. The analysis includes statistical computations, data visualizations, and trend identification.

---

## 📊 Dataset

**Dataset Name:** Global YouTube Statistics 2023  
**File:** `Global YouTube Statistics.csv`  
**Encoding:** Latin-1

**Key Columns:**
- `Youtuber`: Channel name
- `subscribers`: Number of subscribers
- `video views`: Total video views
- `uploads`: Number of videos uploaded
- `category`: Content category
- `Country`: Country of origin
- `Gross tertiary education enrollment (%)`: Education metric
- `Unemployment rate`: Unemployment rate in country
- `Urban_population`: Urban population percentage
- `highest_yearly_earnings`: Highest yearly earnings
- `lowest_monthly_earnings`: Lowest monthly earnings
- `highest_monthly_earnings`: Highest monthly earnings
- `subscribers_for_last_30_days`: Recent subscriber growth
- `video_views_for_the_last_30_days`: Recent view counts
- `created_year`, `created_month`, `created_date`: Channel creation date
- `Latitude`, `Longitude`: Geographic coordinates
- `Population`: Country population

---

## ✨ Features

- **Top YouTubers Analysis**: Identifies and visualizes the top 10 most subscribed channels
- **Category Analysis**: Analyzes average subscribers and upload counts by content category
- **Geographic Distribution**: Identifies countries with the most YouTube channels
- **Earnings Analysis**: Examines monthly and yearly earnings trends across categories
- **Correlation Studies**: Analyzes relationships between:
  - Subscribers and video views
  - Tertiary education enrollment and channel count
  - Unemployment rate and channel growth
  - Subscribers and population
- **Channel Creation Trends**: Visualizes when YouTube channels were created
- **Trend Analysis**: Examines subscriber growth over the past 30 days
- **Outlier Detection**: Identifies outliers in yearly earnings using IQR method
- **3D Geographic Visualization**: Shows channel distribution by coordinates

---

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/bramhayyachar018/Youtube-analysis-2023.git
cd Youtube-analysis-2023
```

---

## 📦 Dependencies

The project requires the following Python libraries:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
python-dateutil>=2.8.0
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn python-dateutil
```

---

## 📁 Project Structure

```
Youtube-analysis-2023/
├── README.md                          # Project documentation
├── python_case_project.py             # Main analysis script
├── Global YouTube Statistics.csv      # Dataset
├── html.html                          # HTML file
├── practicecss1.html                  # Practice HTML file
├── style.css                          # CSS stylesheet
├── new.css                            # Additional CSS
└── python/                            # Python utilities
    ├── lowerto upper.py               # Case conversion utility
    ├── numberpalindrom.py             # Number palindrome checker
    ├── palindrom.py                   # String palindrome checker
    └── strriver.py                    # String manipulation utility
```

---

## 🚀 Usage

### Run the Complete Analysis

```bash
python python_case_project.py
```

This will execute all analysis functions and display visualizations. Close each matplotlib window to proceed to the next visualization.

### Run Individual Functions

Uncomment the desired function at the bottom of `python_case_project.py`:

```python
# Uncomment any function to run it individually
# top_10_youtubers()
# top_avg_category()
# upload_count()
# correlation()
# ... etc
```

---

## 📈 Analysis Functions

### 1. `top_10_youtubers()`
Displays a bar chart of the top 10 most subscribed YouTube channels.

### 2. `top_avg_category()`
Identifies the content category with the highest average subscriber count.

### 3. `upload_count()`
Finds the category with the most uploads on average.

### 4. `top_country_youtubechannel()`
Shows which country has the most YouTube channels.

### 5. `distribution_of_channels_across_categories()`
Visualizes the distribution of YouTube channels across different content categories.

### 6. `correlation()`
Calculates the correlation between subscriber count and video views.

### 7. `monthly_earnings_categories()`
Analyzes monthly earnings (minimum and maximum) across content categories.

### 8. `trends_subs_gained_in_30_days()`
Examines subscriber growth trends in the past 30 days by category.

### 9. `outliers_yearly_earning()`
Identifies channels with outlier earnings using the Interquartile Range (IQR) method.

### 10. `creation_of_channel_trends()`
Shows trends of channel creation over the years.

### 11. `relation_btw_grosstertiaryedu_n_noofyoutubers()`
Analyzes the correlation between tertiary education enrollment and number of YouTube channels by country.

### 12. `Unemployment_vs_NoOfYoutubeChannels()`
Compares unemployment rates with YouTube channel density in the top 10 countries.

### 13. `avg_urban_population_in_counties_with_most_channels()`
Examines urban population percentage in countries with the most YouTube channels.

### 14. `latitude_longitude_number_of_channels_pattern()`
Creates a 3D visualization showing the relationship between geographic coordinates and channel count.

### 15. `corelation_btw_subscribers_and_population()`
Analyzes correlation between subscriber count and country population.

### 16. `No_of_channels_vs_population()`
Compares the top 10 countries by YouTube channels with their population size.

### 17. `no_of_subs_vs_unemployment_rate()`
Examines the correlation between subscriber growth and unemployment rates.

### 18. `video_views_in_last_30_days_in_categories()`
Shows video view counts by content category in the past 30 days.

### 19. `avg_subs_per_month_over_lifetime()`
Calculates the average subscribers gained per month for each channel since its creation.

### 20. `interquaratile_and_1stquaratile(x)`
Helper function that calculates Q1 and IQR for outlier detection.

---

## 📊 Visualizations

The project generates various types of visualizations:

- **Bar Charts**: Top YouTubers, category analysis, earnings
- **Heatmaps**: Correlation analysis between metrics
- **3D Scatter Plots**: Geographic distribution of channels
- **Time Series**: Channel creation trends over years
- **Comparative Charts**: Country-wise statistics with multiple metrics

---

## 📝 Notes

- Data is loaded with `latin1` encoding to handle special characters
- Missing values are handled using mean, median, or dropna() depending on context
- IQR method (Q1 ± 1.5 × IQR) is used for outlier detection
- Matplotlib plots are displayed interactively
- Some functions may show deprecation warnings from Seaborn (future versions)

---

## 🐛 Known Issues

- Seaborn deprecation warning about `palette` parameter without `hue` assignment
- Some visualizations may take time to render with large datasets

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for:
- Additional analysis functions
- Data visualizations improvements
- Bug fixes
- Documentation enhancements

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Bramh Ayyachar**
- GitHub: [@bramhayyachar018](https://github.com/bramhayyachar018)
- Email: bramhayyachar018@gmail.com

---

## 🔗 Repository

- **Repository URL:** https://github.com/bramhayyachar018/Youtube-analysis-2023
- **Dataset Source:** Global YouTube Statistics 2023

---

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Last Updated:** December 17, 2025
