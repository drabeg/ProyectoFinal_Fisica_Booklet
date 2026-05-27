import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Booklet Educativo - Física 1",
    layout="wide"
)

st.title("BOOKLET EDUCATIVO INTERACTIVO - FÍSICA 1")

st.markdown("""
## Proyecto Digital de Física 1

Este booklet incluye:
- Conceptos
- Fórmulas
- Ejemplos
- Videos educativos
- Simulaciones interactivas
- Ejercicios resueltos
""")

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/70/Logo_Universidad_Mariano_Galvez.png",
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
    "Leyes de Newton",
    "Primera Ley",
    "Segunda Ley",
    "Tercera Ley",
    "Aplicaciones de las Leyes de Newton",
    "Movimiento circular",
    "Trabajo",
    "Energía Cinética",
    "Energía Potencial y Conservación",
    "Momentum Lineal",
    "Choques"
]

seleccion = st.sidebar.radio("Selecciona un tema", TEMAS)


def mostrar_video(url):
    st.video(url)


def ejercicio(titulo, pregunta, procedimiento, respuesta):
    st.subheader(titulo)

    st.write(pregunta)

    boton_id = titulo.replace(" ", "_")

    if st.button(f"Mostrar solución - {titulo}", key=boton_id):
        st.info("Procedimiento")
        st.write(procedimiento)

        st.success(f"Respuesta final: {respuesta}")


# --------------------------------------------------------
# MEDICIONES
# --------------------------------------------------------

if seleccion == "Mediciones":

    st.header("Mediciones")

    st.subheader("Concepto")

    st.write(
        "La medición es el proceso de comparar una magnitud física "
        "con una unidad estándar."
    )

    st.subheader("Esquema")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/Metric_system_explanation.svg",
        width=500
    )

    st.subheader("Fórmula")

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
        "https://www.youtube.com/watch?v=JX7m2L7f7Ac"
    )

    ejercicio(
        "Ejercicio Mediciones",
        "Si el valor real es 100 cm y se mide 96 cm, ¿cuál es el error porcentual?",
        """
1. Restamos:
100 - 96 = 4

2. Dividimos entre el valor real:
4 / 100 = 0.04

3. Multiplicamos por 100:
0.04 × 100 = 4%
        """,
        "4%"
    )


# --------------------------------------------------------
# VECTORES
# --------------------------------------------------------

elif seleccion == "Vectores":

    st.header("Vectores")

    st.write(
        "Los vectores son cantidades físicas que poseen "
        "magnitud, dirección y sentido."
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

    ax.set_aspect("equal")

    ax.grid(True)

    st.pyplot(fig)

    plt.close(fig)

    magnitud = math.sqrt(x**2 + y**2)

    st.success(f"Magnitud del vector: {magnitud:.2f}")

    mostrar_video(
        "https://www.youtube.com/watch?v=4Wh22ynlLyk"
    )

    ejercicio(
        "Ejercicio Vectores",
        "Encuentra la magnitud del vector (6, 8).",
        """
1. Aplicamos la fórmula:

√(x² + y²)

2. Sustituimos:

√(6² + 8²)

3. Resolvemos:

√(36 + 64)

4. Resultado:

√100 = 10
        """,
        "10"
    )


# --------------------------------------------------------
# SUMA GRÁFICA
# --------------------------------------------------------

elif seleccion == "Suma de vectores por método gráfico":

    st.header("Suma de vectores por método gráfico")

    st.write(
        "Consiste en colocar vectores cabeza con cola "
        "para encontrar la resultante."
    )

    ax1 = st.slider("Vector A - X", -10, 10, 4)
    ay1 = st.slider("Vector A - Y", -10, 10, 3)

    bx1 = st.slider("Vector B - X", -10, 10, 5)
    by1 = st.slider("Vector B - Y", -10, 10, 2)

    rx = ax1 + bx1
    ry = ay1 + by1

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.arrow(
        0,
        0,
        ax1,
        ay1,
        head_width=0.4,
        length_includes_head=True
    )

    ax.arrow(
        ax1,
        ay1,
        bx1,
        by1,
        head_width=0.4,
        length_includes_head=True
    )

    ax.arrow(
        0,
        0,
        rx,
        ry,
        head_width=0.5,
        length_includes_head=True
    )

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)

    ax.set_aspect("equal")

    ax.grid(True)

    st.pyplot(fig)

    plt.close(fig)

    st.success(f"Vector resultante: ({rx}, {ry})")

    mostrar_video(
        "https://www.youtube.com/watch?v=8wQY7v1Zx7k"
    )


# --------------------------------------------------------
# SUMA ANALÍTICA
# --------------------------------------------------------

elif seleccion == "Suma de vectores por método analítico":

    st.header("Suma de vectores por método analítico")

    st.latex(r"R_x = A_x + B_x")
    st.latex(r"R_y = A_y + B_y")
    st.latex(r"R = \sqrt{R_x^2 + R_y^2}")

    axv = st.number_input("A_x", value=4.0)
    ayv = st.number_input("A_y", value=3.0)

    bxv = st.number_input("B_x", value=2.0)
    byv = st.number_input("B_y", value=5.0)

    rx = axv + bxv
    ry = ayv + byv

    magnitud = math.sqrt(rx**2 + ry**2)

    st.success(f"Resultante: ({rx}, {ry})")
    st.success(f"Magnitud: {magnitud:.2f}")

    mostrar_video(
        "https://www.youtube.com/watch?v=6A5mY0K0g0E"
    )


# --------------------------------------------------------
# MRU
# --------------------------------------------------------

elif seleccion == "MRU":

    st.header("Movimiento Rectilíneo Uniforme")

    st.write(
        "Es un movimiento donde la velocidad permanece constante."
    )

    st.latex(r"d = vt")

    velocidad = st.slider("Velocidad (m/s)", 1, 50, 10)

    tiempo = st.slider("Tiempo (s)", 1, 20, 5)

    distancia = velocidad * tiempo

    st.success(f"Distancia recorrida: {distancia} m")

    tiempo_x = np.linspace(0, tiempo, 100)

    distancia_y = velocidad * tiempo_x

    fig, ax = plt.subplots()

    ax.plot(tiempo_x, distancia_y)

    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Distancia")

    ax.grid(True)

    st.pyplot(fig)

    plt.close(fig)

    mostrar_video(
        "https://www.youtube.com/watch?v=G7Tn5jDsb8c"
    )

    ejercicio(
        "Ejercicio MRU",
        "Un automóvil viaja a 20 m/s durante 10 s. ¿Qué distancia recorre?",
        """
1. Aplicamos la fórmula:

d = vt

2. Sustituimos:

d = 20 × 10

3. Resultado:

d = 200 metros
        """,
        "200 metros"
    )


# --------------------------------------------------------
# MRUV
# --------------------------------------------------------

elif seleccion == "MRUV":

    st.header("Movimiento Rectilíneo Uniformemente Variado")

    st.latex(r"v_f = v_i + at")

    st.latex(r"d = v_i t + \frac{1}{2}at^2")

    vi = st.slider("Velocidad inicial", 0, 50, 10)

    a = st.slider("Aceleración", -10, 20, 5)

    t = st.slider("Tiempo", 1, 20, 5)

    vf = vi + a * t

    d = vi * t + 0.5 * a * (t**2)

    st.success(f"Velocidad final: {vf} m/s")

    st.success(f"Distancia recorrida: {d:.2f} m")

    mostrar_video(
        "https://www.youtube.com/watch?v=Qa_7f3nH8fY"
    )


# --------------------------------------------------------
# CAÍDA LIBRE
# --------------------------------------------------------

elif seleccion == "Caída Libre":

    st.header("Caída Libre")

    st.latex(r"v = gt")

    st.latex(r"h = \frac{1}{2}gt^2")

    g = 9.8

    tiempo = st.slider("Tiempo de caída", 1, 10, 3)

    velocidad = g * tiempo

    altura = 0.5 * g * (tiempo**2)

    st.success(f"Velocidad: {velocidad:.2f} m/s")

    st.success(f"Altura recorrida: {altura:.2f} m")

    mostrar_video(
        "https://www.youtube.com/watch?v=6A0Yw6Q6YNE"
    )


# --------------------------------------------------------
# TIRO VERTICAL
# --------------------------------------------------------

elif seleccion == "Tiro Vertical":

    st.header("Tiro Vertical")

    st.latex(r"h = v_i t - \frac{1}{2}gt^2")

    vi = st.slider("Velocidad inicial", 10, 100, 40)

    tiempo = st.slider("Tiempo", 1, 10, 3)

    h = vi * tiempo - 0.5 * 9.8 * (tiempo**2)

    st.success(f"Altura alcanzada: {h:.2f} m")

    mostrar_video(
        "https://www.youtube.com/watch?v=WU8v7H8Vd1U"
    )


# --------------------------------------------------------
# MOVIMIENTO SEMIPARABÓLICO
# --------------------------------------------------------

elif seleccion == "Movimiento semiparabólico":

    st.header("Movimiento semiparabólico")

    velocidad = st.slider(
        "Velocidad horizontal",
        1,
        50,
        20
    )

    altura = st.slider(
        "Altura inicial",
        1,
        100,
        20
    )

    tiempo = math.sqrt((2 * altura) / 9.8)

    alcance = velocidad * tiempo

    st.success(f"Tiempo de caída: {tiempo:.2f} s")

    st.success(f"Alcance horizontal: {alcance:.2f} m")


# --------------------------------------------------------
# MOVIMIENTO DE PROYECTILES
# --------------------------------------------------------

elif seleccion == "Movimiento de proyectiles":

    st.header("Movimiento de proyectiles")

    st.latex(
        r"R = \frac{v^2 \sin(2\theta)}{g}"
    )

    velocidad = st.slider(
        "Velocidad inicial",
        1,
        100,
        40
    )

    angulo = st.slider(
        "Ángulo",
        1,
        89,
        45
    )

    gravedad = 9.8

    theta = math.radians(angulo)

    alcance = (
        velocidad**2 * math.sin(2 * theta)
    ) / gravedad

    st.success(f"Alcance máximo: {alcance:.2f} m")

    mostrar_video(
        "https://www.youtube.com/watch?v=ot5m3V6K8mY"
    )


# --------------------------------------------------------
# LEYES DE NEWTON
# --------------------------------------------------------

elif seleccion == "Leyes de Newton":

    st.header("Leyes de Newton")

    st.write(
        "Las leyes de Newton describen el movimiento "
        "de los cuerpos y las fuerzas que actúan sobre ellos."
    )

    mostrar_video(
        "https://www.youtube.com/watch?v=kKKM8Y-u7ds"
    )


# --------------------------------------------------------
# PRIMERA LEY
# --------------------------------------------------------

elif seleccion == "Primera Ley":

    st.header("Primera Ley de Newton")

    st.write(
        "Un cuerpo permanece en reposo o movimiento "
        "rectilíneo uniforme si no actúa una fuerza neta."
    )


# --------------------------------------------------------
# SEGUNDA LEY
# --------------------------------------------------------

elif seleccion == "Segunda Ley":

    st.header("Segunda Ley de Newton")

    st.latex(r"F = ma")

    masa = st.slider("Masa", 1, 100, 10)

    aceleracion = st.slider(
        "Aceleración",
        1,
        20,
        5
    )

    fuerza = masa * aceleracion

    st.success(f"Fuerza resultante: {fuerza} N")


# --------------------------------------------------------
# TERCERA LEY
# --------------------------------------------------------

elif seleccion == "Tercera Ley":

    st.header("Tercera Ley de Newton")

    st.write(
        "A toda acción corresponde una reacción "
        "de igual magnitud y sentido opuesto."
    )


# --------------------------------------------------------
# APLICACIONES
# --------------------------------------------------------

elif seleccion == "Aplicaciones de las Leyes de Newton":

    st.header("Aplicaciones de las Leyes de Newton")

    st.write(
        "Las leyes de Newton tienen aplicaciones "
        "en ingeniería, deportes y vehículos."
    )


# --------------------------------------------------------
# MOVIMIENTO CIRCULAR
# --------------------------------------------------------

elif seleccion == "Movimiento circular":

    st.header("Movimiento Circular")

    st.latex(r"a_c = \frac{v^2}{r}")

    velocidad = st.slider("Velocidad", 1, 50, 10)

    radio = st.slider("Radio", 1, 20, 5)

    ac = (velocidad**2) / radio

    st.success(f"Aceleración centrípeta: {ac:.2f} m/s²")


# --------------------------------------------------------
# TRABAJO
# --------------------------------------------------------

elif seleccion == "Trabajo":

    st.header("Trabajo")

    st.latex(r"W = Fd \cos(\theta)")

    fuerza = st.slider("Fuerza", 1, 100, 20)

    distancia = st.slider("Distancia", 1, 50, 10)

    angulo = st.slider("Ángulo", 0, 180, 0)

    trabajo = (
        fuerza
        * distancia
        * math.cos(math.radians(angulo))
    )

    st.success(f"Trabajo realizado: {trabajo:.2f} J")


# --------------------------------------------------------
# ENERGÍA CINÉTICA
# --------------------------------------------------------

elif seleccion == "Energía Cinética":

    st.header("Energía Cinética")

    st.latex(r"E_k = \frac{1}{2}mv^2")

    masa = st.slider("Masa", 1, 100, 10)

    velocidad = st.slider("Velocidad", 1, 100, 20)

    energia = 0.5 * masa * (velocidad**2)

    st.success(f"Energía cinética: {energia:.2f} J")


# --------------------------------------------------------
# ENERGÍA POTENCIAL
# --------------------------------------------------------

elif seleccion == "Energía Potencial y Conservación":

    st.header("Energía Potencial y Conservación")

    st.latex(r"E_p = mgh")

    masa = st.slider("Masa", 1, 100, 10)

    altura = st.slider("Altura", 1, 100, 20)

    energia = masa * 9.8 * altura

    st.success(f"Energía potencial: {energia:.2f} J")


# --------------------------------------------------------
# MOMENTUM
# --------------------------------------------------------

elif seleccion == "Momentum Lineal":

    st.header("Momentum Lineal")

    st.latex(r"p = mv")

    masa = st.slider("Masa", 1, 100, 5)

    velocidad = st.slider("Velocidad", 1, 100, 20)

    momentum = masa * velocidad

    st.success(f"Momentum lineal: {momentum} kg·m/s")


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

    ejercicio(
        "Ejercicio Choques",
        "Dos carros chocan y se conserva el momentum. Explica por qué.",
        """
1. Antes del choque existe una cantidad total de movimiento.

2. Durante el choque las fuerzas internas se compensan.

3. Por eso el momentum total se conserva.
        """,
        "El momentum total del sistema permanece constante."
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