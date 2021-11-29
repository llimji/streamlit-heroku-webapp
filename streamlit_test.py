# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:39:42 2021

@author: kosuk
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write ("""
#Header Test          
          
          """)
          

tickerSymbol = 'AMD'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-11-29', end = '2021-11-28')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)