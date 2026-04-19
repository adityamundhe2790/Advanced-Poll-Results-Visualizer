# Advanced Poll Results Visualizer

 **Live App:** http://10.250.0.14:8501  

> An end-to-end data analytics dashboard that transforms raw survey data into actionable insights using visualization and NLP.

---

## Overview

The **Advanced Poll Results Visualizer** is an interactive dashboard built using **Streamlit + Plotly** that analyzes user preferences, satisfaction levels, and sentiment across different data tools.

It demonstrates a complete **data pipeline**:

👉 Raw Data → Preprocessing → Feature Engineering → Visualization → Insights

---

## Key Features

- 📊 Interactive dashboard with real-time filtering  
- 🧠 Sentiment analysis using NLP (TextBlob)  
- ⭐ Rating analysis and distribution  
- 🛠 Tool preference insights (Python, Excel, Power BI, R)  
- 👥 Demographic segmentation (Age, Gender)  
- 🎨 Modern UI (Dark theme + Glassmorphism + Animations)  
- ⚡ Fast and responsive visualizations with Plotly  

---

## Insights Generated

- Identify the **most preferred tool**
- Analyze **user satisfaction (ratings)**
- Understand **user sentiment (positive/negative)**
- Compare behavior across **age groups and gender**

---

## 🏗️ Project Structure
Poll-Results-Visualizer/
│
├── data/
│ └── cleaned_poll_data.csv
│
├── src/
│ ├── app.py # Streamlit dashboard
│ ├── data_generator.py # Raw data generation
│ ├── preprocessing.py # Data cleaning & transformation
│ ├── nlp.py # Sentiment analysis
│ └── analysis.py # Data insights
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Tech Stack

- **Python**
- **Streamlit**
- **Plotly**
- **Pandas**
- **TextBlob (NLP)**

---

## Run Locally

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Advanced-Poll-Results-Visualizer.git

# Navigate to project folder
cd Advanced-Poll-Results-Visualizer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/app.py
