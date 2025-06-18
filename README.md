# FinanceML Analytics Suite 📈

A comprehensive financial analysis and machine learning platform that combines AI-powered stock analysis, interactive dashboards, and advanced predictive modeling for financial markets.

## 🚀 Features

### 1. AI-Powered Stock Analysis Chatbot
- **OpenAI Integration**: GPT-4 powered chatbot for intelligent stock analysis
- **Real-time Data**: Live stock price fetching using Yahoo Finance API
- **Technical Indicators**: SMA, EMA, RSI, MACD calculations
- **Interactive Charts**: Dynamic stock price visualization
- **Streamlit Interface**: User-friendly web interface

### 2. Interactive Financial Dashboard
- **Multi-Stock Comparison**: Compare multiple stocks side-by-side
- **Technical Analysis**: 30-day SMA, 100-day SMA, Linear Regression
- **Synchronized Charts**: Linked pan/zoom functionality
- **Bokeh Visualization**: Professional interactive charts
- **Date Range Selection**: Flexible time period analysis

### 3. Machine Learning Models
- **S&P 500 Predictor**: Random Forest classifier for market direction
- **XGBoost Implementation**: Advanced gradient boosting for stock prediction
- **CatBoost Models**: Categorical boosting algorithms
- **LSTM Networks**: Deep learning for time series forecasting
- **ARMA/GARCH Models**: Statistical time series analysis

### 4. Computer Vision
- **SVHN Object Detection**: Street View House Numbers detection using deep learning
- **TensorFlow/Keras**: Advanced neural network implementations

## 🛠️ Technology Stack

- **Backend**: Python, Streamlit, Bokeh
- **Machine Learning**: scikit-learn, XGBoost, CatBoost, TensorFlow
- **Data Processing**: pandas, numpy, yfinance
- **Visualization**: matplotlib, plotly, bokeh
- **AI Integration**: OpenAI GPT-4 API
- **Development**: Jupyter Notebooks

## 📋 Prerequisites

- Python 3.8+
- OpenAI API Key
- Internet connection for real-time data

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/FinanceML-Analytics-Suite.git
cd FinanceML-Analytics-Suite
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up API Key**
```bash
# Create API_KEY file in root directory
echo "your_openai_api_key_here" > API_KEY
```

## 🚀 Usage

### Quick Start
```bash
# Run setup script
python setup.py

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key
```

### Stock Analysis Chatbot
```bash
streamlit run src/main.py
```
- Open your browser to `http://localhost:8501`
- Ask questions like "What's the current price of AAPL?"
- Request technical analysis: "Calculate RSI for Tesla"

### Financial Dashboard
```bash
bokeh serve src/FInancial_Dashboard.py --show
```
- Compare stocks with interactive charts
- Apply technical indicators
- Analyze historical trends

### Machine Learning Models
```bash
# Run S&P 500 prediction
jupyter notebook notebooks/s&p500_predictor.ipynb

# XGBoost stock prediction
cd models/XGBoost/
python addingfeatures_xgboost_ml.py
```

## 📊 Project Structure

```
FinanceML-Analytics-Suite/
├── src/                          # Source code
│   ├── main.py                   # Stock analysis chatbot
│   ├── FInancial_Dashboard.py    # Interactive dashboard
│   ├── stockprediction.py        # Core prediction logic
│   └── app.py                    # GPU configuration
├── notebooks/                    # Jupyter notebooks
│   ├── s&p500_predictor.ipynb    # S&P 500 analysis
│   ├── ARMA_Stock_Forecasting.ipynb
│   ├── GARCH_Stock_Modeling.ipynb
│   └── 13_svhn_object_detection.ipynb
├── models/                       # ML model implementations
│   ├── XGBoost/                  # XGBoost models
│   └── Catboost/                 # CatBoost models
├── data/                         # Data files
│   ├── sp500.csv                 # S&P 500 historical data
│   └── assets.h5                 # Model assets
├── docs/                         # Documentation
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   └── LICENSE                   # MIT License
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Dependencies
├── setup.py                      # Setup script
└── README.md                     # This file
```

## 🔍 Key Features Explained

### Technical Indicators
- **SMA (Simple Moving Average)**: Trend identification
- **EMA (Exponential Moving Average)**: Weighted recent prices
- **RSI (Relative Strength Index)**: Momentum oscillator
- **MACD**: Trend-following momentum indicator

### Machine Learning Approaches
- **Classification**: Predict market direction (up/down)
- **Regression**: Forecast exact price values
- **Time Series**: ARMA/GARCH statistical models
- **Deep Learning**: LSTM networks for sequential data

## 📈 Performance Metrics

- **Accuracy**: Model prediction accuracy scores
- **Precision/Recall**: Classification performance
- **RMSE**: Root Mean Square Error for regression
- **Sharpe Ratio**: Risk-adjusted returns

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Yahoo Finance for real-time stock data
- OpenAI for GPT-4 API
- Streamlit and Bokeh communities
- scikit-learn and TensorFlow teams

## 📞 Contact

Mayank Anand- anandmayank698@gmail.com
Project Link: https://github.com/AnandMayank/FinanceML-Analytics-Suite

---
⭐ Star this repository if you found it helpful!
