# 📉 Predicción de Riesgo de Abandono de Clientes  
Aplicación desarrollada con **Streamlit** para clasificar clientes según su riesgo de abandono (churn) y recomendar acciones estratégicas de retención.

---

## 🚀 Funcionalidades Principales

- ✔ Clasificación de clientes por **sector** (Alto, Medio, Bajo)  
- ✔ Predicción del **riesgo de abandono**  
- ✔ Análisis basado en gasto, frecuencia y ticket promedio  
- ✔ Visualización del historial de compras  
- ✔ Recomendaciones automáticas según el nivel de riesgo  
- ✔ Interfaz amigable en Streamlit  

---

## 🧠 Modelo de Riesgo de Abandono

El riesgo se calcula considerando:

- Disminución del total gastado  
- Menor frecuencia de compras  
- Reducción del ticket promedio  
- Sector al que pertenece (1, 2 o 3)

Cada cliente se clasifica en:

- 🔥 **Riesgo ALTO**
- ⚠️ **Riesgo MEDIO**
- 🟢 **Riesgo BAJO**

---

## 📦 Instalación

Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
