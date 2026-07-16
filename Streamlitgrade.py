import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Find your grade",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #E3F2FD, #F3E5F5);
}

.title {
    text-align:center;
    font-size:42px;
    color:#1565C0;
    font-weight:bold;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    color:#555;
    font-size:18px;
    margin-bottom:25px;
}

.stButton>button {
    width:100%;
    background: linear-gradient(90deg,#1976D2,#42A5F5);
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    padding:12px;
    font-weight:bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg,#1565C0,#1E88E5);
    color:white;
}

.result-card {
    background-color:#ffffff;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #1976D2;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    margin-top:20px;
}

.grade-box {
    background:#E8F5E9;
    padding:12px;
    border-radius:10px;
    margin-top:10px;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="title">🎓 Find your grade</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Enter marks for all five subjects (0 - 100)</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Grade Function
# -----------------------------
def find_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    english = st.number_input(
        "English",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

    maths = st.number_input(
        "Maths",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

    physics = st.number_input(
        "Physics",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

with col2:
    chemistry = st.number_input(
        "Chemistry",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

    computer = st.number_input(
        "Computer Science",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

st.markdown("")

# -----------------------------
# Button
# -----------------------------
if st.button("Calculate Grade"):

    marks = {
        "English": english,
        "Maths": maths,
        "Physics": physics,
        "Chemistry": chemistry,
        "Computer Science": computer
    }

    average = sum(marks.values()) / len(marks)
    overall_grade = find_grade(average)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.subheader("📊 Subject Grades")

    for subject, mark in marks.items():
        grade = find_grade(mark)
        st.markdown(
            f'<div class="grade-box">{subject}: <b>{mark:.1f}</b> → Grade <b>{grade}</b></div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.metric("Average Marks", f"{average:.1f}")

    st.success(f"🎉 Overall Grade: {overall_grade}")

    st.markdown("</div>", unsafe_allow_html=True)