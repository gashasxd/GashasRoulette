import streamlit as st
import random
import pandas as pd
from datetime import datetime
import pytz 

# Configuración de la página
st.set_page_config(page_title="GashasXD", layout="wide")
st.title("🌀 GashasXD: Ruleta de Duelo")

# Inicializar histórico en la sesión
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Definir la zona horaria de Colombia
bogota_tz = pytz.timezone('America/Bogota')

# Formulario de giro
nombre = st.text_input("Ingresa tu nombre de duelista:")
boton_giro = st.button("✨ ¡GIRAR RULETA! ✨")

if boton_giro and nombre:
    premios = ["🃏 COMÚN", "💎 RARO", "🔥 LEGENDARIO"]
    # Puedes ajustar estos pesos en GitHub cuando quieras
    pesos = [0.55, 0.35, 0.10] 
    
    resultado = random.choices(premios, weights=pesos, k=1)[0]
    
    # Efectos visuales
    st.balloons()
    st.success(f"¡Felicidades {nombre}! Has obtenido: {resultado}")
    
    # Guardar en histórico con hora de Bogotá
    hora_actual = datetime.now(bogota_tz).strftime("%H:%M:%S")
    nuevo_registro = {"Hora": hora_actual, "Nombre": nombre, "Premio": resultado}
    st.session_state.historico.insert(0, nuevo_registro)

# Mostrar histórico
st.subheader("📜 Registro de Ganadores (Hoy)")
st.table(pd.DataFrame(st.session_state.historico))
