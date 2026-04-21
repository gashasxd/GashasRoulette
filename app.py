import streamlit as st
import random
import pandas as pd
import pytz 
from datetime import datetime

# Configuración de la página
st.title("🌀 Gashas: Ruleta de Duelo")
st.write("¡Prueba tu suerte para ganar accesorios de Yu-Gi-Oh! y Pokémon!")

# Inicializar histórico en la sesión
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Formulario de giro
nombre = st.text_input("Ingresa tu nombre de duelista:")
boton_giro = st.button("✨ ¡GIRAR RULETA! ✨")

if boton_giro and nombre:
    premios = ["🃏 COMÚN", "💎 RARO", "🔥 LEGENDARIO"]
    pesos = [0.67, 0.29, 0.04]
    resultado = random.choices(premios, weights=pesos, k=1)[0]
    
    # Mostrar resultado con efecto
    st.balloons() # ¡Tira confeti en la pantalla!
    st.success(f"¡Felicidades {nombre}! Ganaste: {resultado}")
    
#Mostrar Hístorico
zona_horaria = pytz.timezone('America/Bogota')
hora_actual = datetime.now(zona_horaria).strftime("%H:%M:%S")
nuevo_registro = {"Hora": hora_actual, "Nombre": nombre, "Premio": resultado[0]}

# Mostrar histórico
st.subheader("📜 Registro de Ganadores")
st.table(pd.DataFrame(st.session_state.historico))
