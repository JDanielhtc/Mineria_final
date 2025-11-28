import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Riesgo de Abandono del Cliente", page_icon="📉")

# -------------------------------------------------
# BASE DE CLIENTES (CON SECTOR ASIGNADO)
# -------------------------------------------------
clientes = [
    {"id": 1, "nombre": "Carlos Ruiz", "total_gasto": 150, "frecuencia": 3, "ticket_promedio": 50, "sector": 3},
    {"id": 2, "nombre": "Ana Torres", "total_gasto": 800, "frecuencia": 12, "ticket_promedio": 67, "sector": 2},
    {"id": 3, "nombre": "Luis Gómez", "total_gasto": 2600, "frecuencia": 34, "ticket_promedio": 76, "sector": 1},
    {"id": 4, "nombre": "Marta Silva", "total_gasto": 5000, "frecuencia": 58, "ticket_promedio": 86, "sector": 1},
    {"id": 5, "nombre": "Javier Soto", "total_gasto": 980, "frecuencia": 22, "ticket_promedio": 44, "sector": 2},
    {"id": 6, "nombre": "Elena Prado", "total_gasto": 12000, "frecuencia": 120, "ticket_promedio": 100, "sector": 1},
    {"id": 7, "nombre": "Fabian León", "total_gasto": 320, "frecuencia": 6, "ticket_promedio": 53, "sector": 3},
    {"id": 8, "nombre": "Lucía Ramos", "total_gasto": 1800, "frecuencia": 29, "ticket_promedio": 62, "sector": 2},
    {"id": 9, "nombre": "Diego Núñez", "total_gasto": 4500, "frecuencia": 41, "ticket_promedio": 109, "sector": 1},
    {"id": 10, "nombre": "Gabriela Vega", "total_gasto": 750, "frecuencia": 16, "ticket_promedio": 47, "sector": 2},
]

df_clientes = pd.DataFrame(clientes)


# -------------------------------------------------
# FUNCIÓN PARA CALCULAR EL RIESGO DE ABANDONO
# -------------------------------------------------
def calcular_riesgo(total, frecuencia, ticket, sector):
    # Normalización simple para puntaje de abandono inverso
    total_n = min(total / 5000, 1)
    freq_n = min(frecuencia / 60, 1)
    ticket_n = min(ticket / 100, 1)

    # Cuanto más alto el sector (1=alto, 3=bajo) → más riesgo
    if sector == 1:
        sector_score = 0.1
    elif sector == 2:
        sector_score = 0.5
    else:
        sector_score = 0.9

    # Score final (entre 0 y 1)
    riesgo = (
        (1 - total_n) * 0.3 +
        (1 - freq_n) * 0.3 +
        (1 - ticket_n) * 0.2 +
        (sector_score) * 0.2
    )

    # Clasificación
    if riesgo >= 0.66:
        return "ALTO", riesgo
    elif riesgo >= 0.33:
        return "MEDIO", riesgo
    else:
        return "BAJO", riesgo


# -------------------------------------------------
# RECOMENDACIONES SEGÚN RIESGO
# -------------------------------------------------
acciones = {
    "ALTO": [
        "Enviar cupón del 20% inmediatamente",
        "Llamada de retención con oferta personalizada",
        "Promoción VIP si vuelve a comprar esta semana"
    ],
    "MEDIO": [
        "Enviar recordatorio de productos similares",
        "Promoción de 2x1 en su categoría principal",
        "Correo de seguimiento con productos recomendados"
    ],
    "BAJO": [
        "Reforzar fidelización con puntos extra",
        "Ofrecer una membresía para aumentar engagement",
        "Mostrar productos premium de interés"
    ]
}


# -------------------------------------------------
# INTERFAZ PRINCIPAL
# -------------------------------------------------
st.title("📉 Predicción de Riesgo de Abandono del Cliente")

sector = st.selectbox(
    "Selecciona el sector:",
    ["Sector 1 – Clientes ALTOS", "Sector 2 – Clientes MEDIOS", "Sector 3 – Clientes BAJOS"]
)

# Mapeo sector → número
n_sector = {"Sector 1 – Clientes ALTOS": 1,
            "Sector 2 – Clientes MEDIOS": 2,
            "Sector 3 – Clientes BAJOS": 3}[sector]

# Filtrar clientes por sector seleccionado
clientes_filtrados = df_clientes[df_clientes["sector"] == n_sector]

# Dropdown dinámico
opciones = {c["nombre"]: c for c in clientes_filtrados.to_dict(orient="records")}
nombre_cliente = st.selectbox("Cliente:", list(opciones.keys()))
cliente = opciones[nombre_cliente]


# ----------------------------------------
# DATOS DEL CLIENTE
# ----------------------------------------
st.subheader("📊 Datos del Cliente")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total gastado", f"${cliente['total_gasto']}")
col2.metric("Frecuencia", f"{cliente['frecuencia']} compras")
col3.metric("Ticket promedio", f"${cliente['ticket_promedio']}")
col4.metric("Sector", cliente["sector"])


# ----------------------------------------
# HISTORIAL SIMULADO DE COMPRAS
# ----------------------------------------
st.subheader("📈 Historial de Compras (Simulado)")
historial = pd.DataFrame({
    "Compra": list(range(1, cliente["frecuencia"] + 1)),
    "Monto": [random.randint(cliente["ticket_promedio"] - 10,
                             cliente["ticket_promedio"] + 50)
              for _ in range(cliente["frecuencia"])]
})

st.line_chart(historial, x="Compra", y="Monto")


# -------------------------------------------------
# BOTÓN PARA CALCULAR RIESGO
# -------------------------------------------------
if st.button("🔮 Calcular Riesgo de Abandono"):
    nivel, score = calcular_riesgo(
        cliente["total_gasto"],
        cliente["frecuencia"],
        cliente["ticket_promedio"],
        cliente["sector"]
    )

    st.subheader("🎯 Resultado del Riesgo de Abandono")
    st.write(f"**Nivel:** `{nivel}`")
    st.write(f"**Puntaje interno:** `{round(score, 2)}`")

    st.subheader("💡 Recomendación Estratégica")
    for r in acciones[nivel]:
        st.write(f"- {r}")
