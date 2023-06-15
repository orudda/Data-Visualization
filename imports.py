import os

try:
    import streamlit
except ImportError:
    os.system("pip install streamlit")
try:
    import pandas
except ImportError:
    os.system("pip install pandas")
try:
    import matplotlib
except ImportError:
    os.system("pip install matplotlib")
try:
    import seaborn
except ImportError:
    os.system("pip install seaborn")

#run de system
#os.system("py -m streamlit run main.py")