import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Poll Dashboard", layout="wide")

# -----------------------
# 🔥 PREMIUM CSS
# -----------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0c29, #1a1a40);
}

h1, h2, h3, h4, h5, h6, p, div {
    color: white !important;
}

.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 0 25px rgba(108,99,255,0.25);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 40px rgba(108,99,255,0.6);
}

.stMultiSelect div, .stSelectbox div {
    background-color: #1e1e2f !important;
    color: white !important;
}

header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_poll_data.csv")

df = load_data()

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio("Go to", ["Dashboard", "Analytics", "Insights"])

st.sidebar.subheader("Filters")

tools = st.sidebar.multiselect("Tool", df["Tool"].unique(), default=df["Tool"].unique())
age = st.sidebar.multiselect("Age", df["Age"].unique(), default=df["Age"].unique())
gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())

df_filtered = df[
    (df["Tool"].isin(tools)) &
    (df["Age"].isin(age)) &
    (df["Gender"].isin(gender))
]

# -----------------------
# 🏠 DASHBOARD
# -----------------------
if page == "Dashboard":

    st.title("📊 Poll Results Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Responses", len(df_filtered))
    col2.metric("Tools Analyzed", df_filtered["Tool"].nunique())
    col3.metric("Avg Rating", round(df_filtered["Rating"].mean(), 2))

    positive = (df_filtered["Sentiment"] > 0).mean() * 100
    col4.metric("Positive Sentiment (%)", round(positive, 1))

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🟢 Tool Preference Share")
        fig1 = px.pie(df_filtered, names="Tool")
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Age Distribution")
        fig2 = px.histogram(df_filtered, x="Age", color="Gender")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# 📊 ANALYTICS
# -----------------------
elif page == "Analytics":

    st.title("📊 Advanced Analytics")

    # ⭐ Average Rating per Tool
    avg_tool_rating = df_filtered.groupby("Tool")["Rating"].mean().reset_index()
    avg_tool_rating = avg_tool_rating.sort_values(by="Rating", ascending=False)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("⭐ Average Rating per Tool")

    fig_avg = px.bar(
        avg_tool_rating,
        x="Tool",
        y="Rating",
        color="Tool",
        text=avg_tool_rating["Rating"].round(2)
    )
    fig_avg.update_traces(textposition="outside")

    st.plotly_chart(fig_avg, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("👥 Gender Distribution")
        fig3 = px.pie(df_filtered, names="Gender", hole=0.5)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("⭐ Rating Distribution")
        fig4 = px.histogram(df_filtered, x="Rating")
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("💬 Sentiment Analysis")
        fig5 = px.histogram(df_filtered, x="Sentiment")
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# 💡 INSIGHTS
# -----------------------
elif page == "Insights":

    st.title("💡 Insights")

    top_tool = df_filtered["Tool"].mode()[0]
    avg_rating = df_filtered["Rating"].mean()

    st.markdown(f"""
    <div class='card'>
        <h3>🏆 Top Tool: {top_tool}</h3>
        <h4>⭐ Avg Rating: {avg_rating:.2f}</h4>
        <p>This tool is most preferred and performs best based on user feedback.</p>
    </div>
    """, unsafe_allow_html=True)