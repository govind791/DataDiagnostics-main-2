# How to run (VS Code / Windows)

```powershell
# 1) open VS Code in the folder that contains 'DataDiagnostics-main'
cd DataDiagnostics-main-2

# 2) create + activate venv
py -m venv .venv
.\.venv\Scripts\Activate

# 3) install deps
pip install -r DataDiagnostics-main/requirements.txt

# 4) run the app (Home is the main page)
streamlit run DataDiagnostics-main/Home.py
# (or) python -m streamlit run DataDiagnostics-main/Home.py
```

The sidebar includes **Data Analysis** and **Data Visualization** pages.
Upload a CSV/XLSX on **Home** or pick a sample dataset.
