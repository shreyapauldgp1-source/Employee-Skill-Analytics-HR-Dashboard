"""
Employee Skill Analytics & HR Dashboard
UI redesign only - Power BI inspired lavender BI theme.

Backend (model loading + prediction) is unchanged.
"""

import os

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Employee Skill Analytics & HR Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# BACKEND BLOCK 1 - model loading (unchanged logic)
# ---------------------------------------------------------------------
MODEL_PATH = os.path.join("models", "random_forest_streamlit.pkl")
model = joblib.load(MODEL_PATH)

# ---------------------------------------------------------------------
# THEME
# ---------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
  --bg:#F7F4FF; --bg2:#F1ECFF; --p1:#34117A; --p2:#5C43A5;
  --lav:#D8C7F7; --acc:#E8DDFF; --card:#FFFFFF; --bd:#DDD5F7;
  --tx:#2F2F3A; --tx2:#6D6D80; --ok:#34C759; --warn:#FF4D4F;
}

html, body, [class*="css"] { font-family:'Inter',sans-serif; }

.stApp{
  background:linear-gradient(135deg,#F7F4FF 0%,#EAE2FF 50%,#DDD1FF 100%);
  background-attachment:fixed;
}
.block-container{ padding-top:1.6rem; padding-bottom:2.5rem; max-width:1400px; }

/* ---------- header ---------- */
.hdr{ display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:.4rem; }
.hdr h1{
  font-size:2.45rem; font-weight:800; color:var(--p1);
  letter-spacing:-.02em; margin:0; line-height:1.1;
}
.hdr p{ color:var(--tx2); font-size:1rem; margin:.35rem 0 0; font-weight:500; }
.slashes{ display:flex; gap:7px; padding-top:6px; }
.slashes span{
  display:block; width:5px; height:56px; background:var(--p1);
  transform:skewX(-22deg); border-radius:2px; opacity:.9;
}
.divider{
  height:2px; border:0; margin:1.1rem 0 1.6rem;
  background:linear-gradient(90deg,var(--p1) 0%,var(--lav) 45%,rgba(216,199,247,0) 100%);
}

/* ---------- cards ---------- */
.card{
  background:rgba(255,255,255,.86);
  backdrop-filter:blur(14px);
  border:1px solid var(--bd);
  border-radius:20px;
  box-shadow:0 8px 26px -14px rgba(52,17,122,.28);
  padding:1.35rem 1.5rem;
  transition:transform .25s ease, box-shadow .25s ease;
}
.card:hover{ transform:translateY(-3px); box-shadow:0 16px 34px -16px rgba(52,17,122,.38); }

.kpi{ display:flex; align-items:center; justify-content:space-between; gap:1rem; min-height:104px; }
.kpi .val{ font-size:2.1rem; font-weight:800; color:var(--tx); line-height:1; }
.kpi .lbl{ font-size:.82rem; color:var(--tx2); margin-top:.5rem; font-weight:500; letter-spacing:.01em; }
.kpi .ico{
  width:48px; height:48px; border-radius:14px; background:var(--acc);
  display:flex; align-items:center; justify-content:center; font-size:1.35rem;
  box-shadow:inset 0 0 0 1px var(--bd);
}

.sec-title{
  font-size:1.02rem; font-weight:700; color:var(--p1);
  margin:0 0 .2rem; display:flex; align-items:center; gap:.5rem;
}
.sec-sub{ font-size:.8rem; color:var(--tx2); margin:0 0 .6rem; }

/* ---------- inputs ---------- */
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div{
  background:#FFFFFF !important;
  border:1px solid var(--bd) !important;
  border-radius:12px !important;
  color:var(--tx) !important;
  font-weight:500;
}
div[data-testid="stNumberInput"] input:focus{
  border-color:var(--p2) !important; box-shadow:0 0 0 3px rgba(92,67,165,.15) !important;
}
label, .stMarkdown p{ color:var(--tx) !important; }
div[data-testid="stWidgetLabel"] p{ font-size:.82rem !important; font-weight:600 !important; color:var(--tx2) !important; }

/* ---------- button ---------- */
div.stButton > button{
  width:100%; padding:.95rem 1rem; border:0; border-radius:16px;
  background:linear-gradient(135deg,#34117A 0%,#5C43A5 60%,#7B5FC7 100%);
  color:#fff !important; font-weight:700; font-size:1.02rem; letter-spacing:.01em;
  box-shadow:0 12px 26px -12px rgba(52,17,122,.75);
  transition:transform .2s ease, box-shadow .2s ease, filter .2s ease;
}
div.stButton > button:hover{ transform:translateY(-2px); filter:brightness(1.08);
  box-shadow:0 18px 34px -14px rgba(52,17,122,.85); }
div.stButton > button:active{ transform:translateY(0); }

/* ---------- result ---------- */
.result{ border-radius:20px; padding:1.6rem 1.8rem; border:1px solid; text-align:center; }
.result h3{ margin:0; font-size:1.35rem; font-weight:800; }
.result .conf{ margin-top:.55rem; font-size:.92rem; color:var(--tx2); font-weight:500; }
.result .pct{ font-size:2.4rem; font-weight:800; margin-top:.4rem; }
.ok{ background:rgba(52,199,89,.10); border-color:rgba(52,199,89,.35); }
.ok h3,.ok .pct{ color:#1E8E3E; }
.bad{ background:rgba(255,77,79,.10); border-color:rgba(255,77,79,.35); }
.bad h3,.bad .pct{ color:#C42B2D; }

/* ---------- sidebar ---------- */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#FFFFFF 0%,#F5F0FF 100%);
  border-right:1px solid var(--bd);
}
.sb-brand{ font-weight:800; color:var(--p1); font-size:1.05rem; line-height:1.25; margin-bottom:.15rem; }
.sb-tag{ font-size:.76rem; color:var(--tx2); margin-bottom:1rem; }
.sb-h{ font-size:.72rem; letter-spacing:.13em; text-transform:uppercase;
  color:var(--p2); font-weight:700; margin:1.1rem 0 .5rem; }
.sb-meta{ background:#fff; border:1px solid var(--bd); border-radius:14px; padding:.9rem 1rem; }
.sb-row{ display:flex; justify-content:space-between; gap:.75rem; padding:.32rem 0; font-size:.82rem; }
.sb-row span:first-child{ color:var(--tx2); }
.sb-row span:last-child{ color:var(--tx); font-weight:600; text-align:right; }

/* ---------- footer ---------- */
.foot{ text-align:center; margin-top:2.4rem; padding-top:1.3rem; border-top:1px solid var(--bd); }
.foot .t{ color:var(--p1); font-weight:700; font-size:.95rem; }
.foot .s{ color:var(--tx2); font-size:.8rem; margin-top:.3rem; }

#MainMenu, footer, header{ visibility:hidden; }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="sb-brand">Employee Skill Analytics</div>'
        '<div class="sb-tag">HR Intelligence Portal</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="sb-h">Project Details</div>', unsafe_allow_html=True)
    st.markdown(
        """
<div class="sb-meta">
  <div class="sb-row"><span>Algorithm</span><span>Random Forest Classifier</span></div>
  <div class="sb-row"><span>Dataset</span><span>HR Analytics Dashboard</span></div>
  <div class="sb-row"><span>Accuracy</span><span>88.81%</span></div>
  <div class="sb-row"><span>Developer</span><span>Shreya Paul</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------
st.markdown(
    """
<div class="hdr">
  <div>
    <h1>Employee Skill Analytics &amp; HR Dashboard</h1>
    <p>Workforce Overview &amp; Insights</p>
  </div>
  <div class="slashes"><span></span><span></span><span></span><span></span></div>
</div>
<hr class="divider"/>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------------------
KPIS = [
    ("1,473", "Total Employees", "👥"),
    ("6,500", "Average Salary", "💰"),
    ("52.05", "Average Skill Score", "⭐"),
    ("16.09%", "Attrition Rate", "📈"),
]
for col, (val, lbl, ico) in zip(st.columns(4, gap="medium"), KPIS):
    col.markdown(
        f"""
<div class="card kpi">
  <div>
    <div class="val">{val}</div>
    <div class="lbl">{lbl}</div>
  </div>
  <div class="ico">{ico}</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ---------------------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------------------
left, right = st.columns(2, gap="medium")

with left:
    with st.container():
        st.markdown(
            '<div class="sec-title">🧑‍💼 Employee Information</div>'
            '<div class="sec-sub">Personal &amp; compensation attributes</div>',
            unsafe_allow_html=True,
        )
        MonthlyIncome = st.number_input("Monthly Income", min_value=0, value=6500, step=100)
        Age = st.number_input("Age", min_value=18, max_value=70, value=35, step=1)
        DailyRate = st.number_input("Daily Rate", min_value=0, value=800, step=10)
        DistanceFromHome = st.number_input("Distance From Home", min_value=0, max_value=100, value=8, step=1)
        HourlyRate = st.number_input("Hourly Rate", min_value=0, value=65, step=1)

with right:
    with st.container():
        st.markdown(
            '<div class="sec-title">📋 Employment Details</div>'
            '<div class="sec-sub">Records, rates &amp; skill metrics</div>',
            unsafe_allow_html=True,
        )
        EmployeeNumber = st.number_input("Employee Number", min_value=0, value=1024, step=1)
        EmployeeID = st.number_input("Employee ID", min_value=0, value=101, step=1)
        MonthlyRate = st.number_input("Monthly Rate", min_value=0, value=14000, step=100)
        SkillScore = st.number_input("Skill Score", min_value=0.0, max_value=100.0, value=52.05, step=0.01)
        OverTime = st.selectbox("OverTime", ["No", "Yes"])

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ---------------------------------------------------------------------
# PREDICT
# ---------------------------------------------------------------------
_, mid, _ = st.columns([1, 2, 1])
with mid:
    predict = st.button("🔮  Predict Employee Attrition")

if predict:
    # -----------------------------------------------------------------
    # BACKEND BLOCK 2 - prediction (unchanged logic)
    # -----------------------------------------------------------------
    input_data = pd.DataFrame([{
        "MonthlyIncome": MonthlyIncome,
        "OverTime": 1 if OverTime == "Yes" else 0,
        "SkillScore": SkillScore,
        "DailyRate": DailyRate,
        "Age": Age,
        "EmployeeNumber": EmployeeNumber,
        "DistanceFromHome": DistanceFromHome,
        "MonthlyRate": MonthlyRate,
        "EmpID": EmployeeID,
        "HourlyRate": HourlyRate,
    }])

    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data).max() * 100

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    _, res, _ = st.columns([1, 2, 1])
    with res:
        if prediction == 0:
            st.markdown(
                f"""
<div class="result ok">
  <h3>✅ Employee is Likely to Stay</h3>
  <div class="pct">{confidence:.2f}%</div>
  <div class="conf">Model confidence · Random Forest Classifier</div>
</div>
""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
<div class="result bad">
  <h3>⚠️ Employee is Likely to Leave</h3>
  <div class="pct">{confidence:.2f}%</div>
  <div class="conf">Model confidence · Random Forest Classifier</div>
</div>
""",
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------
st.markdown(
    """
<div class="foot">
  <div class="t">Employee Skill Analytics &amp; HR Dashboard</div>
  <div class="s">Developed using Python • Streamlit • Scikit-learn • Pandas • Power BI</div>
</div>
""",
    unsafe_allow_html=True,
)
