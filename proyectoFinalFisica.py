import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Booklet Educativo - Física 1",
    layout="wide"
)

# --------------------------------------------------------
# PANTALLA INICIAL
# --------------------------------------------------------

if "inicio" not in st.session_state:
    st.session_state.inicio = True

if st.session_state.inicio:

    st.title("BOOKLET EDUCATIVO INTERACTIVO")
    st.subheader("Física I")

    st.image(
        "imagenes/logo_umg.png",
        width=250
    )

    st.markdown("""
### Universidad Mariano Gálvez de Guatemala

**Creado por:** Dario Alfredo Rabe Godoy  
**Carnet:** 5190-25-23683  
**Curso:** Física I

---

Este booklet interactivo contiene:

- Conceptos fundamentales
- Fórmulas físicas
- Simulaciones interactivas
- Ejemplos resueltos
- Videos educativos
- Ejercicios interactivos

---

Seleccione un tema en el menú lateral para comenzar.
""")

    if st.button("Ingresar al booklet"):
        st.session_state.inicio = False
        st.rerun()

    st.stop()

# --------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------

st.sidebar.image(
    "imagenes/logo_umg.png",
    width=220
)

st.sidebar.title("Temas")

TEMAS = [
    "Mediciones",
    "Vectores",
    "Suma de vectores por método gráfico",
    "Suma de vectores por método analítico",
    "MRU",
    "MRUV",
    "Caída Libre",
    "Tiro Vertical",
    "Movimiento semiparabólico",
    "Movimiento de proyectiles",
    "Movimiento circular",
    "Movimiento circular uniformemente variado",
    "Leyes de Newton",
    "Primera Ley",
    "Segunda Ley",
    "Tercera Ley",
    "Aplicaciones de las Leyes de Newton",
    "Trabajo",
    "Energía Cinética",
    "Energía Potencial y Conservación",
    "Momentum Lineal",
    "Choques"
]

seleccion = st.sidebar.radio(
    "Selecciona un tema",
    TEMAS
)

# --------------------------------------------------------
# FUNCIONES
# --------------------------------------------------------

def mostrar_video(url):
    st.video(url)


def ejercicio_opcion_multiple(
    titulo,
    pregunta,
    opciones,
    correcta,
    procedimiento
):

    st.subheader(titulo)

    respuesta = st.radio(
        pregunta,
        opciones,
        key=titulo
    )

    if st.button(
        f"Verificar - {titulo}",
        key=f"btn_{titulo}"
    ):

        if respuesta == correcta:
            st.success("Respuesta correcta")
        else:
            st.error(
                f"Respuesta incorrecta. "
                f"La correcta es: {correcta}"
            )

        st.info("Procedimiento")
        st.write(procedimiento)


def ejercicio_numerico(
    titulo,
    pregunta,
    correcta,
    tolerancia,
    procedimiento
):

    st.subheader(titulo)

    respuesta = st.number_input(
        pregunta,
        value=0.0,
        key=titulo
    )

    if st.button(
        f"Comprobar - {titulo}",
        key=f"btn_{titulo}"
    ):

        if abs(respuesta - correcta) <= tolerancia:
            st.success("Resultado correcto")
        else:
            st.error(
                f"Resultado incorrecto. "
                f"Respuesta correcta: {correcta}"
            )

        st.info("Procedimiento")
        st.write(procedimiento)


def ejercicio_verdadero_falso(
    titulo,
    pregunta,
    correcta,
    procedimiento
):

    st.subheader(titulo)

    respuesta = st.radio(
        pregunta,
        ["Verdadero", "Falso"],
        key=titulo
    )

    if st.button(
        f"Revisar - {titulo}",
        key=f"btn_{titulo}"
    ):

        if respuesta == correcta:
            st.success("Correcto")
        else:
            st.error(
                f"Incorrecto. "
                f"La respuesta correcta es: {correcta}"
            )

        st.info("Procedimiento")
        st.write(procedimiento)


def ejercicio_slider(
    titulo,
    pregunta,
    minimo,
    maximo,
    correcta,
    procedimiento
):

    st.subheader(titulo)

    respuesta = st.slider(
        pregunta,
        minimo,
        maximo,
        minimo,
        key=titulo
    )

    if st.button(
        f"Validar - {titulo}",
        key=f"btn_{titulo}"
    ):

        if respuesta == correcta:
            st.success("Correcto")
        else:
            st.error(
                f"Incorrecto. "
                f"La respuesta correcta es: {correcta}"
            )

        st.info("Procedimiento")
        st.write(procedimiento)

# --------------------------------------------------------
# MEDICIONES
# --------------------------------------------------------

if seleccion == "Mediciones":

    st.header("Mediciones")

    st.write(
        "La medición es el proceso de comparar una magnitud "
        "con una unidad de referencia."
    )

    st.latex(
        r"Error\ porcentual = \frac{|Valor\ real - Valor\ medido|}{Valor\ real} \times 100"
    )

    valor_real = 50

    valor_medido = st.slider(
        "Valor medido",
        40,
        60,
        48
    )

    error = abs(valor_real - valor_medido) / valor_real * 100

    st.success(f"Error porcentual: {error:.2f}%")

    mostrar_video(
        "https://youtu.be/hXBBBTbqWPY"
    )

    ejercicio_opcion_multiple(
        "Ejercicio Mediciones",

        "Si el valor real es 100 cm y se mide 96 cm, ¿cuál es el error porcentual?",

        [
            "2%",
            "4%",
            "6%",
            "8%"
        ],

        "4%",

        """
1. Restamos:
100 - 96 = 4

2. Dividimos:
4 / 100 = 0.04

3. Multiplicamos por 100:
0.04 × 100 = 4%
        """
    )

# --------------------------------------------------------
# VECTORES
# --------------------------------------------------------

elif seleccion == "Vectores":

    st.header("Vectores")

    st.write(
        "Los vectores poseen magnitud, dirección y sentido."
    )

    st.latex(
        r"|\vec{v}| = \sqrt{x^2 + y^2}"
    )

    x = st.slider("Componente X", -10, 10, 5)
    y = st.slider("Componente Y", -10, 10, 4)

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.arrow(
        0,
        0,
        x,
        y,
        head_width=0.4,
        head_length=0.6,
        length_includes_head=True
    )

    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)

    ax.grid(True)

    ax.set_aspect("equal")

    st.pyplot(fig)

    plt.close(fig)

    magnitud = math.sqrt(x**2 + y**2)

    st.success(f"Magnitud del vector: {magnitud:.2f}")

    mostrar_video(
        "https://youtu.be/IrTeyyzerjI"
    )

    ejercicio_numerico(
        "Ejercicio Vectores",

        "Ingrese la magnitud del vector (6,8)",

        10,

        0.1,

        """
1. Aplicamos:

√(x² + y²)

2. Sustituimos:

√(6² + 8²)

3. Resultado:

10
        """
    )

# --------------------------------------------------------
# MRU
# --------------------------------------------------------

elif seleccion == "MRU":

    st.header("Movimiento Rectilíneo Uniforme")

    st.write(
        "El MRU ocurre cuando la velocidad permanece constante."
    )

    st.latex(r"d = vt")

    velocidad = st.slider(
        "Velocidad",
        1,
        50,
        10
    )

    tiempo = st.slider(
        "Tiempo",
        1,
        20,
        5
    )

    distancia = velocidad * tiempo

    st.success(f"Distancia recorrida: {distancia} m")

    tiempo_x = np.linspace(0, tiempo, 100)

    distancia_y = velocidad * tiempo_x

    fig, ax = plt.subplots()

    ax.plot(
        tiempo_x,
        distancia_y
    )

    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Distancia")

    ax.grid(True)

    st.pyplot(fig)

    plt.close(fig)

    mostrar_video(
        "https://youtu.be/XE9UXxtep6M"
    )

    ejercicio_slider(
        "Ejercicio MRU",

        "Seleccione la distancia correcta recorrida por un automóvil que viaja a 20 m/s durante 10 s",

        0,
        500,

        200,

        """
1. Aplicamos:

d = vt

2. Sustituimos:

20 × 10

3. Resultado:

200 metros
        """
    )

# --------------------------------------------------------
# PRIMERA LEY
# --------------------------------------------------------

elif seleccion == "Primera Ley":

    st.header("Primera Ley de Newton")

    st.write(
        "La primera ley establece que un cuerpo "
        "mantendrá su estado de movimiento "
        "si no actúa una fuerza neta."
    )

    fuerza = st.slider(
        "Fuerza aplicada",
        0,
        100,
        0
    )

    if fuerza == 0:
        st.success("El objeto permanece en reposo.")
    else:
        st.success("El objeto cambia su movimiento.")

    mostrar_video(
        "https://youtu.be/uUyAFlIdBqw"
    )

    ejercicio_verdadero_falso(
        "Ejercicio Primera Ley",

        "Un objeto permanecerá en reposo si no actúa una fuerza neta sobre él.",

        "Verdadero",

        """
La primera ley de Newton indica que un objeto
mantiene su estado de movimiento
si no existe una fuerza neta externa.
        """
    )

# --------------------------------------------------------
# SEGUNDA LEY
# --------------------------------------------------------

elif seleccion == "Segunda Ley":

    st.header("Segunda Ley de Newton")

    st.latex(r"F = ma")

    masa = st.slider(
        "Masa",
        1,
        100,
        10
    )

    aceleracion = st.slider(
        "Aceleración",
        1,
        20,
        5
    )

    fuerza = masa * aceleracion

    st.success(f"Fuerza resultante: {fuerza} N")

    mostrar_video(
        "https://youtu.be/RlXxqscdnYw"
    )

    ejercicio_numerico(
        "Ejercicio Segunda Ley",

        "Calcule la fuerza para una masa de 10 kg y aceleración de 5 m/s²",

        50,

        0.1,

        """
1. Fórmula:

F = ma

2. Sustituimos:

10 × 5

3. Resultado:

50 N
        """
    )

# --------------------------------------------------------
# CHOQUES
# --------------------------------------------------------

elif seleccion == "Choques":

    st.header("Choques")

    st.write(
        "En los choques se conserva el momentum lineal."
    )

    st.latex(
        r"m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2"
    )

    mostrar_video(
        "https://youtu.be/_zu67RXVuUM"
    )

    ejercicio_opcion_multiple(
        "Ejercicio Choques",

        "¿Qué magnitud se conserva en un choque?",

        [
            "Temperatura",
            "Momentum lineal",
            "Color",
            "Volumen"
        ],

        "Momentum lineal",

        """
En un sistema aislado,
el momentum total permanece constante.
        """
    )

# --------------------------------------------------------
# FOOTER
# --------------------------------------------------------

st.markdown("---")

st.markdown("""
### Información del Proyecto

**Creado por:** Dario Alfredo Rabe Godoy  
**Carnet:** 5190-25-23683  
**Curso:** Física I
""")