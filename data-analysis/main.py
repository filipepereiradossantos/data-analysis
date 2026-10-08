# pyrefly: ignore [missing-import]
import sweetviz as sv
import pandas as pd

df = pd.read_csv('dataset.csv')

analise_completa = sv.analyze(df)
analise_completa.show_html('#')