"""
Stock Analysis Chatbot using OpenAI GPT-4 and Yahoo Finance

This module provides an interactive Streamlit application that allows users to:
- Get real-time stock prices
- Calculate technical indicators (SMA, EMA, RSI, MACD)
- Generate stock price charts
- Chat with an AI assistant about stock analysis

Author: [Your Name]
Date: 2024
License: MIT
"""

import json
import os
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf
from openai import OpenAI

# Initialize OpenAI client
try:
    if os.path.exists('API_KEY'):
        with open('API_KEY', 'r') as f:
            api_key = f.read().strip()
        client = OpenAI(api_key=api_key)
    else:
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            client = OpenAI(api_key=api_key)
        else:
            st.error("API_KEY file not found and OPENAI_API_KEY environment variable not set. Please provide your OpenAI API key.")
            st.stop()
except Exception as e:
    st.error(f"Error initializing OpenAI client: {str(e)}")
    st.stop()

def get_stock_price(ticker):
    """
    Get the latest closing price for a given stock ticker.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOGL')

    Returns:
        str: Latest closing price as a string
    """
    try:
        data = yf.Ticker(ticker).history(period='1y')
        if data.empty:
            return f"No data found for ticker {ticker}"
        return str(data.iloc[-1].Close)
    except Exception as e:
        return f"Error fetching price for {ticker}: {str(e)}"


def calculate_SMA(ticker, window):
    """
    Calculate Simple Moving Average for a given ticker and window.

    Args:
        ticker (str): Stock ticker symbol
        window (int): Number of periods for the moving average

    Returns:
        str: SMA value as a string
    """
    try:
        data = yf.Ticker(ticker).history(period='1y').Close
        if data.empty:
            return f"No data found for ticker {ticker}"
        sma = data.rolling(window=window).mean().iloc[-1]
        return str(sma)
    except Exception as e:
        return f"Error calculating SMA for {ticker}: {str(e)}"


def calculate_EMA(ticker, window):
    """
    Calculate Exponential Moving Average for a given ticker and window.

    Args:
        ticker (str): Stock ticker symbol
        window (int): Number of periods for the moving average

    Returns:
        str: EMA value as a string
    """
    try:
        data = yf.Ticker(ticker).history(period='1y').Close
        if data.empty:
            return f"No data found for ticker {ticker}"
        ema = data.ewm(span=window, adjust=False).mean().iloc[-1]
        return str(ema)
    except Exception as e:
        return f"Error calculating EMA for {ticker}: {str(e)}"


def calculate_RSI(ticker):
    """
    Calculate Relative Strength Index (RSI) for a given ticker.

    Args:
        ticker (str): Stock ticker symbol

    Returns:
        str: RSI value as a string
    """
    try:
        data = yf.Ticker(ticker).history(period='1y').Close
        if data.empty:
            return f"No data found for ticker {ticker}"

        delta = data.diff()
        up = delta.clip(lower=0)
        down = -1 * delta.clip(upper=0)
        ema_up = up.ewm(com=14-1, adjust=False).mean()
        ema_down = down.ewm(com=14-1, adjust=False).mean()
        rs = ema_up / ema_down
        rsi = 100 - (100 / (1 + rs)).iloc[-1]
        return str(rsi)
    except Exception as e:
        return f"Error calculating RSI for {ticker}: {str(e)}"


def calculate_MACD(ticker):
    """
    Calculate MACD (Moving Average Convergence Divergence) for a given ticker.

    Args:
        ticker (str): Stock ticker symbol

    Returns:
        str: MACD, Signal, and Histogram values as a comma-separated string
    """
    try:
        data = yf.Ticker(ticker).history(period='1y').Close
        if data.empty:
            return f"No data found for ticker {ticker}"

        short_EMA = data.ewm(span=12, adjust=False).mean()
        long_EMA = data.ewm(span=26, adjust=False).mean()

        MACD = short_EMA - long_EMA
        signal = MACD.ewm(span=9, adjust=False).mean()
        MACD_histogram = MACD - signal

        return f'{MACD.iloc[-1]:.4f}, {signal.iloc[-1]:.4f}, {MACD_histogram.iloc[-1]:.4f}'
    except Exception as e:
        return f"Error calculating MACD for {ticker}: {str(e)}"


def plot_stock_price(ticker):
    """
    Generate and save a stock price chart for the last year.

    Args:
        ticker (str): Stock ticker symbol

    Returns:
        str: Success message or error message
    """
    try:
        data = yf.Ticker(ticker).history(period='1y')
        if data.empty:
            return f"No data found for ticker {ticker}"

        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data.Close, linewidth=2, color='#1f77b4')
        plt.title(f'{ticker.upper()} Stock Price Over Last Year', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Stock Price ($)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('stock.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f"Chart generated successfully for {ticker}"
    except Exception as e:
        return f"Error generating chart for {ticker}: {str(e)}"



functions = [
   {
      'name': 'get_stock_price',
      'description': 'Gets the latest stock price given the ticker symbol of a company.',
      'parameters' : {
         'type' : 'object',
         'properties' :{
            'ticker': {
               'type' : 'string',
                'description': 'The stock ticker symbol for a company ( for example AAPL for Apple).'            
         }
      },
      'required' : ['ticker']
   }
   },
   {
      "name": "calculate_SMA",
      "description": " Calculate the simple average for a given ticker and a window.",
      "parameters" : {
         "type": "object",
         "properties": {
            "ticker":{
               "type":"string",
               "description" : "The stock ticker symbol for a company ( for example AAPL for Apple)."
            },
            "window":{
               "type": "integer",
               "description":"The timeframe to consider when calculating the EMA "
            }
         },
         "required":["ticker", "window"],
      },
     
   },
   {
      "name": "calculate_EMA",
      "description": " Calculate the exponential average for a given ticker and a window.",
      "parameters" : {
         "type": "object",
         "properties": {
            "ticker":{
               "type":"string",
               "description" : "The stock ticker symbol for a company ( for example AAPL for Apple)."
            },
            "window":{
               "type": "integer",
               "description":"The timeframe to consider when calculating the EMA "
            }
         },
         "required":["ticker", "window"],
      },
     
   },
   {
      "name":"calculate_RSI",
      "description": "Calculate the RSI for a goven stock",
      "parameters":{
         "type": "object",
         "properties": {
            "ticker":{
               "type": "string",
               "description":"The stock ticker symbol for a company ( e.g..AAPL for Apple)",
            },
         },
         "required":["ticker"],
      },
   },
   {
      "name":"calculate_MACD",
      "description":"Calculate the MACD  for a given ticker. ",
      "parameters":{
         "type":"object",
         "properties":{
            "ticker":{
               "type": "string",
               "description":" The stock ticker symbol for a company (e.g..AAPL for Apple )",
            },
         },
         "required": ["ticker"],
      },
   },
   {
      "name": "plot_stock_price",
      "description": "Plot the stock price for the last year given the ticker symbol of a company ",
      "parameters":{
         "type":"object",
         "properties":{
            "ticker":{
               "type":"string",
               "description":"The stock ticker for a company ( e.g.. AAPL for Apple)",

            },
         },
         "required":["ticker"],
      },
   },
]

available_functions ={
   'get_stock_price': get_stock_price,
   'calculate_SMA' : calculate_SMA,
   'calculate_EMA' : calculate_EMA,
   'calculate_RSI' : calculate_RSI,
   'calculate_MACD' : calculate_MACD,
   'plot_stock_price' : plot_stock_price
}

if 'messages' not in st.session_state:
   st.session_state['messages'] = []

st.title('Stock Analysis Chatbot Assistant 📈')

user_input = st.text_input('Your input:', placeholder="Ask me about stock prices, technical indicators, or request charts...")

if user_input:
    try:
        st.session_state['messages'].append({'role': 'user','content': user_input})
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=st.session_state['messages'],
            tools=[{"type": "function", "function": func} for func in functions],
            tool_choice='auto'
        )

        response_message = response.choices[0].message

        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name in ['get_stock_price', 'calculate_RSI', 'calculate_MACD', 'plot_stock_price']:
                args_dict = {'ticker': function_args.get('ticker')}
            elif function_name in ['calculate_SMA','calculate_EMA']:
                args_dict = {'ticker': function_args.get('ticker'), 'window': function_args.get('window')}

            function_to_call = available_functions[function_name]
            function_response = function_to_call(**args_dict)

            if function_name == 'plot_stock_price':
                st.image('stock.png')
            else:
                st.session_state['messages'].append(response_message.model_dump())
                st.session_state['messages'].append({
                    'role': 'tool',
                    'tool_call_id': tool_call.id,
                    'content': function_response
                })
                second_response = client.chat.completions.create(
                    model='gpt-4o-mini',
                    messages=st.session_state['messages']
                )
                st.text(second_response.choices[0].message.content)
                st.session_state['messages'].append({
                    'role': 'assistant',
                    'content': second_response.choices[0].message.content
                })
        else:
            st.text(response_message.content)
            st.session_state['messages'].append({
                'role': 'assistant',
                'content': response_message.content
            })
    except Exception as e:
        st.error(f'Error occurred: {str(e)}')
         



  

