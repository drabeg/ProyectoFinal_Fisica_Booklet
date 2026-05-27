# Booklet Educativo e Interactivo: Física I 🚀

Este repositorio contiene un **Booklet Digital Interactivo** desarrollado para la asignación práctica del curso de **Física I** en la **Universidad Mariano Gálvez de Guatemala**. La aplicación combina fundamentos teóricos de la mecánica clásica con simulaciones dinámicas y cuestionarios en tiempo real para evaluar el aprendizaje.

Desarrollado con un enfoque profesional, limpio y académico, el booklet elimina distracciones visuales e implementa una distribución simétrica para garantizar una experiencia de usuario formal y de alta calidad.

---

## 🧑‍💻 Información del Estudiante
* **Nombre:** Dario Alfredo Rabe Godoy
* **Carnet:** 5190-25-23683
* **Institución:** Universidad Mariano Gálvez de Guatemala (UMG)
* **Curso:** Física I

---

## 🛠️ Características Principales

* **Estructura Modular:** Navegación fluida a través de los temas troncales de la física mecánica.
* **Diseño Simétrico Profesional:** Interfaz balanceada de doble columna (teoría/parámetros a la izquierda, gráficas dinámicas centradas a la derecha) utilizando alineaciones nativas de Streamlit.
* **Simulaciones en Tiempo Real:** Gráficas interactivas generadas dinámicamente con Matplotlib y NumPy para visualizar vectores, trayectorias e incrementos de velocidad.
* **Módulos Interactivos Corregidos:** Implementación matemática precisa para el análisis de tiro parabólico en el módulo de Movimiento de Proyectiles.
* **Evaluación Integrada:** Cuestionarios dinámicos con retroalimentación inmediata para el estudiante.
* **Recursos Multimedia:** Enlaces e integraciones de video verificadas para soporte didáctico en aplicaciones de la dinámica.

---

## 📚 Contenido del Booklet

El proyecto cubre las unidades fundamentales de la mecánica clásica:
1. **Vectores y Mediciones:** Análisis dimensional, cálculo de magnitudes y visualización analítica/gráfica en el plano cartesiano.
2. **Cinemática:** Estudio del MRU, MRUV (gráficas de aceleración cuadrática) y Movimiento de Proyectiles (trayectorias balísticas calculadas en radianes).
3. **Dinámica:** Leyes de Newton (Inercia, Fuerza, Acción y Reacción) y sus aplicaciones en ingeniería civil, automotriz y aeronáutica.
4. **Energía:** Conservación de la energía mecánica (balances de energía cinética y potencial).

---

## 🚀 Instalación y Ejecución Local

Para ejecutar este proyecto en tu entorno local, seguí estos pasos:

1. **Cloná el repositorio:**
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO

2. **Instalá las dependencias requeridas:**
   Asegurate de tener instalado Python y las librerías base del proyecto:
   pip install streamlit matplotlib numpy

3. **Iniciá la aplicación con Streamlit:**
   streamlit run app.py
   *(Nota: Reemplaza app.py por el nombre exacto de tu archivo principal si es diferente).*

---

## 🎨 Decisiones de Diseño y Refactorización
El código original fue sometido a un proceso de **refactorización estética y estructural** para cumplir con estándares profesionales:
* Se removieron decoraciones e íconos informales (emojis) para priorizar un entorno formal y académico.
* Se configuró vertical_alignment en las filas de Streamlit para erradicar desfaces verticales entre columnas.
* Se estandarizaron las cajas de respuestas (st.success) y fórmulas matemáticas (st.latex) para una legibilidad óptima.
