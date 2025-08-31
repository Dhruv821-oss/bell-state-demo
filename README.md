Entangled Qubits Demo

An interactive quantum entanglement visualizer built with Python, Qiskit, and Streamlit.
This demo simulates a Bell state and shows two glowing “quantum balls” that remain entangled.
When you measure one, both collapse into the same outcome (00 or 11) — a playful way to explore “spooky action at a distance.”

✨ Features

🎱 Visualizes two entangled qubits as glowing balls.

🌀 Shows superposition before measurement.

📏 Collapse into 00 or 11 when measured.


🌐 Runs in the browser with Streamlit frontend.

📸 Demo Preview
<img width="1004" height="717" alt="Screenshot 2025-09-01 000057" src="https://github.com/user-attachments/assets/c77c3e7e-30f4-4f80-88bc-bcadc1974644" />

<img width="1408" height="823" alt="Screenshot 2025-08-31 233003" src="https://github.com/user-attachments/assets/868b1b77-b7f3-4033-98ba-7e829a51c3ff" />

🛠️ Installation
# Clone repo
https://github.com/Dhruv821-oss/bell-state-demo


# Install dependencies
pip install qiskit


pip install streamlit

🚀 Run the App
streamlit run app.py

📚 How It Works

A 2-qubit Bell State is created using Qiskit:

Apply Hadamard gate to qubit 0.

Apply CNOT gate from qubit 0 → qubit 1.

This creates the entangled state:

1
2
(
∣
00
⟩
+
∣
11
⟩
)
2
	​

1
	​

(∣00⟩+∣11⟩)

Measurement collapses both qubits into the same outcome.

Streamlit frontend shows the entangled balls collapsing together.

🎯 Educational Value

This project is designed as a beginner-friendly introduction to:

Quantum entanglement

Bell states

Qiskit simulation

Interactive visualization
