import streamlit as st
import random
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

st.set_page_config(page_title="Quantum Entanglement Demo", page_icon="🔗", layout="centered")

st.title("🔗 Quantum Entanglement — Bell State Visualizer")

# --- Build Bell State Circuit ---
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

shots = 1000
sampler = StatevectorSampler()
result = sampler.run([qc], shots=shots).result()[0]
counts = result.join_data().get_counts()

st.subheader("Qiskit Measurement Results (from simulation)")
st.json(counts)

# --- Visualization State ---
if "measured" not in st.session_state:
    st.session_state.measured = False
    st.session_state.outcome = None

st.subheader("🎱 Entangled Qubits")

# Draw balls
col1, col2 = st.columns(2)

def render_ball(col, outcome, measured):
    color_map = {"0": "#3b82f6", "1": "#ef4444"}  # blue for 0, red for 1
    if not measured:
        col.markdown(
            f"""
            <div style="width:120px;height:120px;border-radius:60px;
                        background:#9ca3af;display:flex;
                        align-items:center;justify-content:center;
                        color:white;font-size:24px;box-shadow:0 0 20px #555;">
                ?
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        col.markdown(
            f"""
            <div style="width:120px;height:120px;border-radius:60px;
                        background:{color_map[outcome]};display:flex;
                        align-items:center;justify-content:center;
                        color:white;font-size:24px;box-shadow:0 0 30px {color_map[outcome]};">
                {outcome}
            </div>
            """,
            unsafe_allow_html=True
        )

# Render two entangled balls
render_ball(col1, st.session_state.outcome, st.session_state.measured)
render_ball(col2, st.session_state.outcome, st.session_state.measured)

# --- Measurement Button ---
if st.button("📏 Measure Qubits"):
    if not st.session_state.measured:
        # Collapse state to 00 or 11 (Bell pair)
        outcome = "0" if random.random() < 0.5 else "1"
        st.session_state.outcome = outcome
        st.session_state.measured = True
        st.rerun()   # ✅ modern rerun
