# 🏀 Steph Curry Longevity Analytics Project
*An exploratory analysis of NBA player performance decline using statistical modeling and machine learning*

---

## Abstract
This project investigates the question: **How sustainable is Steph Curry’s elite performance as he ages?**  
Using NBA historical data, advanced feature engineering, and predictive modeling, I built a framework for analyzing age-related decline in shooting efficiency, usage, and overall productivity. The goal is to forecast future performance while comparing Curry’s trajectory to league baselines.

---

## Motivation
Longevity in professional basketball is rare — especially for guards who rely heavily on agility and shooting volume. Steph Curry has redefined the game through 3-point shooting, and his career raises a natural question: **how long can his style remain effective?**

This project extends traditional metrics with time-series and regression analysis to provide data-driven insights into player aging curves.

---

## Data Sources
- **Basketball-Reference & NBA API** – raw box score and advanced stats (scraped with `requests` + `BeautifulSoup`).  
- **Seasons 2009–2025** (Curry’s full career to date).  
- Data cleaned and stored in **Snowflake SQL warehouse**.  

Final dataset: ~**12,000 player-game rows**, 40+ engineered features.

---

## Methodology

### 1. Data Engineering
- Scraped HTML tables and JSON from NBA API → transformed into structured DataFrames.  
- Computed rolling averages, inter-season “gap metrics,” and advanced stats (TS%, usage rate, assist-to-turnover).  
- Stored datasets in **Snowflake** and queried with SQL for reproducibility.  

### 2. Feature Engineering
- **Gap Metrics**: Year-to-year deltas in shooting efficiency and usage.  
- **Rolling Stats**: Moving averages to smooth game-to-game volatility.  
- **Baseline Normalization**: Compared Curry’s stats to league-wide averages (z-scores).  

### 3. Modeling
- Trained linear & polynomial regressors in `scikit-learn` on normalized season metrics.  
- Cross-validated with RMSE to evaluate prediction accuracy.  
- Forecasted decline curves beyond age 37.  

---

## Results

### Trend Analysis
- Curry’s **TS% remains 8–10% above league average**, even as usage increases.  
- Inter-season “gap metrics” show *delayed decline* compared to peers, consistent with skill-based aging vs. athletic decline.

### Forecasts
- Polynomial regression predicts gradual decline, but **productive shooting efficiency sustained until ~age 39**.  
- Usage rate expected to taper earlier, suggesting a potential shift in playstyle (off-ball, spot-up shooter role).  

### Visualization
<img width="2539" height="1228" alt="steph curry ts graph" src="https://github.com/user-attachments/assets/0c4d2066-0454-4749-bdd2-becb321bf673" />
*Polynomial regression of TS% deviation from baseline, ages 21–40.*

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://steph-curry-longevity-analytics-projectgit-atbk2hxbfpauueppznd.streamlit.app/)

---

## Deployment
- Interactive **Streamlit dashboard** with Snowflake backend and embedded Tableau visualizations.  
- Users can filter by season, compare with other players, and adjust decline model assumptions in real time.  

Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py


## ⚙️ Features
- 📊 **Exploratory Data Analysis (EDA):** Interactive visualizations of Curry’s career statistics.  
- 🔮 **Modeling:** Predictive analytics with machine learning (e.g., Linear Regression).  
- 🖥️ **Streamlit App:** Easy-to-use interface for exploring results.  
- 🗂️ **Organized Project Structure:**
  - `app/` → Streamlit app (`app.py`)
  - `notebooks/` → Jupyter notebooks for EDA and modeling
  - `src/` → Python scripts/utilities
  - `data/` → Data files

---

## 🛠️ Installation (Local Setup)
Clone the repository and run the Streamlit app locally.

```bash
# 1. Clone this repo
git clone https://github.com/USERNAME/Steph-Curry-Longevity-Analytics-Project.git
cd Steph-Curry-Longevity-Analytics-Project

# 2. Create and activate virtual environment (optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app/app.py


















