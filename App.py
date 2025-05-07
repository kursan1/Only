import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import time

# Yurak tenglamasi
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

st.set_page_config(layout="wide")
st.title("Yurak Urishi Animatsiyasi")

plot = st.empty()

for i in range(100):
    scale = 1 + 0.05 * np.sin(i * 0.2)
    fig, ax = plt.subplots()
    ax.plot(x * scale, y * scale, color='red')
    ax.set_aspect('equal')
    ax.axis('off')
    plot.pyplot(fig)
    time.sleep(0.05)
