import streamlit as st
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from database import engine_employees_anonymized

def visualizar_insights():
    st.title("📊 Insights de los Empleados")

    # Conexión a la base de datos
    try:
        with engine_employees_anonymized.connect() as conn:
            # Cargar datos relevantes para los Insights
            query = """
                SELECT 
                    "monthly_salary", 
                    "DepartmentType", 
                    "EmployeeType", 
                    "Performance Score", 
                    "Current Employee Rating", 
                    "GenderCode", 
                    "Age"
                FROM "Employees_anonymized"
            """
            df = pd.read_sql(query, conn)
    except Exception as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return

    # Insight 1: Distribución salarial por departamento y tipo de empleado
    st.subheader("Insight 1: Distribución salarial por departamento y tipo de empleado")
    fig1 = px.box(df, 
                  x="DepartmentType", 
                  y="monthly_salary", 
                  color="EmployeeType", 
                  title="Distribución Salarial por Departamento y Tipo de Empleado")
    st.plotly_chart(fig1)

    # Insight 2: Relación entre salario, desempeño y evaluación
    st.subheader("Insight 2: Relación entre salario, desempeño y evaluación")
    fig2 = px.box(df, 
                x="Performance Score", 
                y="monthly_salary", 
                color="Current Employee Rating", 
                title="Distribución del Salario por Desempeño y Evaluación")
    st.plotly_chart(fig2)

    # Insight 3: Disparidad salarial por género y edad
    st.subheader("Insight 3: Disparidad salarial por género y edad")
    fig3 = px.box(df, 
                  x="GenderCode", 
                  y="monthly_salary", 
                  color="Age", 
                  title="Disparidad Salarial por Género y Edad")
    st.plotly_chart(fig3)
