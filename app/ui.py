import streamlit as st
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope

def _is_Anomaly(x):
	if x == -1:
		return "Anomaly"
	else:
		return "Normal"

# f_path = "//home//shadihakim//Downloads//Attacks//git//conn_attack.csv"
f_path = "//app//conn_attack.csv"
df = pd.read_csv(f_path,names=["record ID","duration_", "src_bytes","dst_bytes"], header=None)

X = list(zip(df["duration_"].array, df["src_bytes"].array, df["dst_bytes"].array))

if 'flag' not in st.session_state:
	cov = EllipticEnvelope(random_state=0, contamination=0.0040)
	cov.fit_predict(X)
	st.session_state['flag'] = cov

st.title("The Predictor") 

dur = st.text_input('Duration', '0') #0 is the default here
st.write('The current Duration is', dur)

src = st.text_input('src_bytes ', '0') #0 is the default here
st.write('The current src_bytes is', src)

dst = st.text_input('dst_bytes ', '0') #0 is the default here
st.write('The current dst_bytes is', dst)

if st.button('Click Me To Predict'):
    st.write('The result is:')
    st.text(_is_Anomaly(st.session_state['flag'].predict([(int(dur), int(src), int(dst))])))


