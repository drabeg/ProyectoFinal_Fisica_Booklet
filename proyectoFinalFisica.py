import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Booklet Educativo - Física 1",
    layout="wide"
)

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
- Ejercicios con procedimiento

---

Seleccione un tema en el menú lateral para comenzar.
""")

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

seleccion = st.sidebar.radio("Selecciona un tema", TEMAS)

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
        "https://youtu.be/hXBBBTbqWPY?si=pge4frOmQEN1QHFW"
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
        "https://youtu.be/IrTeyyzerjI?si=fWPFEwXVfI2tflec"
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
        "https://youtu.be/TWdLKBC_AgA?si=nYyrSBkGrSPe7dHR"
    )

    ejercicio_slider(
        "Ejercicio Suma Gráfica",

        "Seleccione la componente X correcta del vector resultante",

        -20,
        20,

        9,

        """
1. Sumamos las componentes en X:

Rx = 4 + 5

2. Resultado:

Rx = 9

3. En el método gráfico se colocan
los vectores cabeza con cola
para obtener la resultante.
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Magnitud Resultante",

        "¿Cuál es la magnitud aproximada del vector resultante R=(9,5)?",

        [
            "10.30",
            "8.50",
            "12.10",
            "14.00"
        ],

        "10.30",

        """
1. Aplicamos Pitágoras:

R = √(9² + 5²)

2. Elevamos:

R = √(81 + 25)

3. Sumamos:

R = √106

4. Resultado:

R ≈ 10.30
        """
    )    


# --------------------------------------------------------
# SUMA ANALÍTICA
# --------------------------------------------------------

elif seleccion == "Suma de vectores por método analítico":

    st.header("Suma de vectores por método analítico")

    st.write(
        "El método analítico consiste en sumar las componentes "
        "en X y Y de cada vector para encontrar el vector resultante."
    )

    st.write(
        "Primero se suman las componentes horizontales y verticales. "
        "Luego se calcula la magnitud del vector resultante usando "
        "el teorema de Pitágoras."
    )

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
        "https://youtu.be/nQnxMF1Jwso?si=IoeW9yppEjouXB9g"
    )

    ejercicio_opcion_multiple(
        "Ejercicio Suma Analítica",

        "Dos vectores tienen componentes A=(4,3) y B=(2,5). ¿Cuál es la magnitud del vector resultante?",

        [
            "8.60",
            "10.00",
            "7.21",
            "6.00"
        ],

        "10.00",

        """
1. Sumamos componentes en X:

Rx = 4 + 2 = 6

2. Sumamos componentes en Y:

Ry = 3 + 5 = 8

3. Aplicamos Pitágoras:

R = √(6² + 8²)

4. Resolvemos:

R = √(36 + 64)

R = √100

5. Resultado final:

R = 10
        """
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
        "https://youtu.be/XE9UXxtep6M?si=svZ14z21MkMjt22K"
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
# MRUV
# --------------------------------------------------------

elif seleccion == "MRUV":

    st.header("Movimiento Rectilíneo Uniformemente Variado")

    st.write(
        "El Movimiento Rectilíneo Uniformemente Variado ocurre "
        "cuando un objeto se mueve en línea recta con una "
        "aceleración constante."
    )

    st.write(
        "En este tipo de movimiento la velocidad cambia "
        "uniformemente con respecto al tiempo."
    )

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
        "https://youtu.be/USFdbyGp8w8?si=nbOSRQwjmpOt5okH"
    )

    ejercicio_numerico(
        "Ejercicio MRUV",

        "Calcule la velocidad final de un objeto con velocidad inicial de 10 m/s, aceleración de 5 m/s² y tiempo de 4 s",

        30,

        0.1,

        """
1. Aplicamos la fórmula:

vf = vi + at

2. Sustituimos:

vf = 10 + (5 × 4)

3. Multiplicamos:

vf = 10 + 20

4. Resultado:

vf = 30 m/s
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Distancia MRUV",

        "¿Qué distancia recorre un objeto con vi = 0 m/s, a = 2 m/s² y t = 5 s?",

        [
            "10 m",
            "20 m",
            "25 m",
            "50 m"
        ],

        "25 m",

        """
1. Aplicamos:

d = vit + 1/2 at²

2. Sustituimos:

d = (0)(5) + 1/2(2)(5²)

3. Resolvemos:

d = 0 + (1)(25)

4. Resultado:

d = 25 m
        """
    )

# --------------------------------------------------------
# CAÍDA LIBRE
# --------------------------------------------------------

elif seleccion == "Caída Libre":

    st.header("Caída Libre")

    st.write(
        "La caída libre es el movimiento de un objeto "
        "cuando únicamente actúa la fuerza de gravedad."
    )

    st.write(
        "En este tipo de movimiento no se toma en cuenta "
        "la resistencia del aire y todos los cuerpos "
        "caen con la misma aceleración gravitacional."
    )

    st.latex(r"v = gt")

    st.latex(r"h = \frac{1}{2}gt^2")

    g = 9.8

    tiempo = st.slider("Tiempo de caída", 1, 10, 3)

    velocidad = g * tiempo

    altura = 0.5 * g * (tiempo**2)

    st.success(f"Velocidad: {velocidad:.2f} m/s")

    st.success(f"Altura recorrida: {altura:.2f} m")

    mostrar_video(
        "https://youtu.be/b0FW0grwWks?si=ECRe3WqF4LQdR7pT"
    )

    ejercicio_numerico(
        "Ejercicio Caída Libre",

        "Calcule la velocidad de un objeto después de 4 segundos de caída libre",

        39.2,

        0.1,

        """
1. Aplicamos la fórmula:

v = gt

2. Sustituimos:

v = 9.8 × 4

3. Resultado:

v = 39.2 m/s
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Altura Caída Libre",

        "¿Qué altura recorre un objeto en 2 segundos de caída libre?",

        [
            "9.8 m",
            "19.6 m",
            "4.9 m",
            "39.2 m"
        ],

        "19.6 m",

        """
1. Aplicamos:

h = 1/2 gt²

2. Sustituimos:

h = 1/2 (9.8)(2²)

3. Elevamos:

2² = 4

4. Resolvemos:

h = 4.9 × 4

5. Resultado:

h = 19.6 m
        """
    )


# --------------------------------------------------------
# TIRO VERTICAL
# --------------------------------------------------------

elif seleccion == "Tiro Vertical":

    st.header("Tiro Vertical")

    st.write(
        "El tiro vertical ocurre cuando un objeto es lanzado "
        "hacia arriba o hacia abajo en dirección vertical."
    )

    st.write(
        "Durante el movimiento actúa la gravedad, "
        "provocando que el objeto disminuya su velocidad "
        "al subir y aumente al bajar."
    )

    st.latex(r"h = v_i t - \frac{1}{2}gt^2")

    vi = st.slider("Velocidad inicial", 10, 100, 40)

    tiempo = st.slider("Tiempo", 1, 10, 3)

    h = vi * tiempo - 0.5 * 9.8 * (tiempo**2)

    st.success(f"Altura alcanzada: {h:.2f} m")

    mostrar_video(
        "https://youtu.be/K1ex_ingNTY?si=qKSAqsfgi4eIQZbp"
    )

    ejercicio_numerico(
        "Ejercicio Tiro Vertical",

        "Calcule la altura alcanzada por un objeto lanzado con velocidad inicial de 30 m/s durante 2 segundos",

        40.4,

        0.1,

        """
1. Aplicamos la fórmula:

h = vit - 1/2 gt²

2. Sustituimos:

h = (30)(2) - 1/2(9.8)(2²)

3. Elevamos:

2² = 4

4. Resolvemos:

h = 60 - 19.6

5. Resultado:

h = 40.4 m
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Velocidad Tiro Vertical",

        "¿Qué ocurre con la velocidad de un objeto cuando sube en un tiro vertical?",

        [
            "Aumenta constantemente",
            "Permanece igual",
            "Disminuye debido a la gravedad",
            "Se vuelve negativa instantáneamente"
        ],

        "Disminuye debido a la gravedad",

        """
Durante el ascenso la gravedad actúa
en sentido contrario al movimiento.

Por eso la velocidad disminuye
hasta llegar momentáneamente a cero
en la altura máxima.
        """
    )

# --------------------------------------------------------
# MOVIMIENTO SEMIPARABÓLICO
# --------------------------------------------------------

elif seleccion == "Movimiento semiparabólico":

    st.header("Movimiento semiparabólico")

    st.write(
        "El movimiento semiparabólico ocurre cuando un objeto "
        "es lanzado horizontalmente desde cierta altura."
    )

    st.write(
        "En este movimiento existe velocidad horizontal constante "
        "y aceleración vertical causada por la gravedad."
    )

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

    mostrar_video(
        "https://youtu.be/vT_jT-6Owo4?si=DA_fjzl24g3gS0Jm"
    )

    ejercicio_numerico(
        "Ejercicio Movimiento Semiparabólico",

        "Calcule el tiempo de caída de un objeto lanzado horizontalmente desde una altura de 20 m",

        2.02,

        0.1,

        """
1. Aplicamos la fórmula:

t = √(2h/g)

2. Sustituimos:

t = √((2 × 20)/9.8)

3. Resolvemos:

t = √(40/9.8)

4. Resultado:

t ≈ 2.02 s
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Alcance Horizontal",

        "Si un objeto tiene velocidad horizontal de 10 m/s y tarda 2 s en caer, ¿cuál es su alcance horizontal?",

        [
            "5 m",
            "10 m",
            "20 m",
            "40 m"
        ],

        "20 m",

        """
1. Aplicamos:

R = vt

2. Sustituimos:

R = 10 × 2

3. Resultado:

R = 20 m
        """
    )


# --------------------------------------------------------
# MOVIMIENTO DE PROYECTILES
# --------------------------------------------------------

elif seleccion == "Movimiento de proyectiles":

    st.header("Movimiento de proyectiles")

    st.write(
        "El movimiento de proyectiles combina un movimiento "
        "horizontal uniforme y un movimiento vertical "
        "uniformemente acelerado."
    )

    st.write(
        "La trayectoria que sigue el objeto tiene forma "
        "parabólica debido a la acción de la gravedad."
    )

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
        "https://youtu.be/lsStZ8xH4y4?si=_kahycp9XCW_HT61"
    )

    ejercicio_numerico(
        "Ejercicio Movimiento de Proyectiles",

        "Calcule el alcance de un proyectil lanzado con velocidad de 20 m/s y ángulo de 45°",

        40.82,

        0.2,

        """
1. Aplicamos la fórmula:

R = (v² sen(2θ)) / g

2. Sustituimos:

R = (20² × sen(90°)) / 9.8

3. Resolvemos:

R = (400 × 1) / 9.8

4. Resultado:

R ≈ 40.82 m
        """
    )

    ejercicio_opcion_multiple(
        "Ejercicio Ángulo de Proyectiles",

        "¿Con qué ángulo se obtiene el alcance máximo ideal en un lanzamiento de proyectiles?",

        [
            "30°",
            "45°",
            "60°",
            "90°"
        ],

        "45°",

        """
En condiciones ideales y sin resistencia del aire,
el alcance máximo ocurre cuando:

θ = 45°

Esto sucede porque el movimiento horizontal
y vertical se equilibran de forma óptima.
        """
    )

# --------------------------------------------------------
# MOVIMIENTO CIRCULAR UNIFORME
# --------------------------------------------------------

elif seleccion == "Movimiento circular":

    st.header("Movimiento Circular")

    st.subheader("Concepto")

    st.write(
        "El movimiento circular ocurre cuando un objeto "
        "se desplaza siguiendo una trayectoria circular."
    )

    st.write(
        "Aunque la rapidez puede permanecer constante, "
        "la dirección de la velocidad cambia continuamente."
    )

    st.subheader("Aceleración centrípeta")

    st.write(
        "La aceleración centrípeta es la responsable "
        "de mantener el movimiento circular."
    )

    st.latex(r"a_c = \frac{v^2}{r}")

    velocidad = st.slider("Velocidad", 1, 50, 10)

    radio = st.slider("Radio", 1, 20, 5)

    ac = (velocidad**2) / radio

    st.success(f"Aceleración centrípeta: {ac:.2f} m/s²")

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Un automóvil dando vueltas en una rotonda "
        "es un ejemplo de movimiento circular."
    )

    mostrar_video(
        "https://youtu.be/HmkGsCZZNXg?si=LYHkV6sAt_K9FTDZ"
    )

    ejercicio_numerico(
    "Ejercicio Movimiento Circular",

    "Calcule la aceleración centrípeta si v = 10 m/s y r = 5 m",

    20,

    0.1,

    """
1. Fórmula:

a = v²/r

2. Sustituimos:

a = 10² / 5

3. Resultado:

20 m/s²
    """
)

# --------------------------------------------------------
# MOVIMIENTO CIRCULAR UNIFORMEMENTE VARIADO
# --------------------------------------------------------

elif seleccion == "Movimiento circular uniformemente variado":

    st.header("Movimiento Circular Uniformemente Variado")

    st.subheader("Concepto")

    st.write(
        "El MCUV ocurre cuando un objeto se mueve "
        "en trayectoria circular con aceleración angular constante."
    )

    st.write(
        "En este movimiento la velocidad angular cambia "
        "uniformemente con respecto al tiempo."
    )

    st.subheader("Fórmulas")

    st.latex(r"\omega_f = \omega_i + \alpha t")

    st.latex(r"\theta = \omega_i t + \frac{1}{2}\alpha t^2")

    wi = st.slider(
        "Velocidad angular inicial",
        0,
        20,
        5
    )

    alpha = st.slider(
        "Aceleración angular",
        1,
        10,
        2
    )

    tiempo = st.slider(
        "Tiempo",
        1,
        20,
        5
    )

    wf = wi + alpha * tiempo

    theta = wi * tiempo + 0.5 * alpha * (tiempo**2)

    st.success(f"Velocidad angular final: {wf:.2f} rad/s")

    st.success(f"Desplazamiento angular: {theta:.2f} rad")

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Las ruedas de una bicicleta acelerando "
        "son un ejemplo de MCUV."
    )

    mostrar_video(
        "https://youtu.be/VesfI_8ydpA?si=7adjiZ5EuX3wArgV"
    )

    ejercicio_slider(
    "Ejercicio MCUV",

    "Seleccione la velocidad angular final correcta",

    0,
    30,

    15,

    """
1. Fórmula:

ωf = ωi + αt

2. Sustituimos:

5 + (2 × 5)

3. Resultado:

15 rad/s
    """
)

# --------------------------------------------------------
# LEYES DE NEWTON
# --------------------------------------------------------

elif seleccion == "Leyes de Newton":

    st.header("Leyes de Newton")

    st.write(
        "Las leyes de Newton son tres principios fundamentales "
        "que explican cómo se comportan los cuerpos cuando "
        "actúan fuerzas sobre ellos."
    )

    st.write(
        "Estas leyes permiten comprender fenómenos relacionados "
        "con el movimiento, equilibrio, aceleración y las "
        "interacciones entre objetos."
    )

    st.subheader("Importancia")

    st.write(
        """
Las leyes de Newton tienen aplicaciones en:

- Ingeniería
- Astronomía
- Deportes
- Vehículos
- Construcción
- Tecnología espacial
        """
    )

    st.subheader("Resumen de las leyes")

    st.write(
        """
- Primera Ley: Ley de la inercia.
- Segunda Ley: Relación entre fuerza y aceleración.
- Tercera Ley: Acción y reacción.
        """
    )

    mostrar_video(
        "https://youtu.be/9lgVjHJqTZc?si=nns1ZACQ3Fvshm3g"
    )

    ejercicio_opcion_multiple(
        "Pregunta General 1",

        "¿Cuál es la ley de Newton conocida como ley de la inercia?",

        [
            "Primera Ley",
            "Segunda Ley",
            "Tercera Ley",
            "Ley de gravitación"
        ],

        "Primera Ley",

        """
La Primera Ley de Newton establece
que un cuerpo mantiene su estado
de reposo o movimiento rectilíneo uniforme
si no existe una fuerza neta actuando sobre él.
        """
    )

    ejercicio_opcion_multiple(
        "Pregunta General 2",

        "¿Qué relación expresa la Segunda Ley de Newton?",

        [
            "Acción y reacción",
            "Fuerza, masa y aceleración",
            "Conservación de energía",
            "Movimiento circular"
        ],

        "Fuerza, masa y aceleración",

        """
La Segunda Ley de Newton establece:

F = ma

La fuerza neta aplicada sobre un cuerpo
produce una aceleración proporcional
a la masa y a la aceleración.
        """
    )

# --------------------------------------------------------
# PRIMERA LEY
# --------------------------------------------------------

elif seleccion == "Primera Ley":

    st.header("Primera Ley de Newton")

    st.subheader("Concepto")

    st.write(
        "La primera ley de Newton también es conocida "
        "como la ley de la inercia."
    )

    st.write(
        "Establece que un cuerpo permanecerá en reposo "
        "o en movimiento rectilíneo uniforme mientras "
        "no exista una fuerza neta actuando sobre él."
    )

    st.subheader("Inercia")

    st.write(
        "La inercia es la resistencia que poseen los cuerpos "
        "a cambiar su estado de movimiento."
    )

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Cuando un automóvil frena bruscamente, "
        "los pasajeros tienden a seguir moviéndose hacia adelante "
        "debido a la inercia."
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
        st.success("El objeto cambia su estado de movimiento.")

    mostrar_video(
        "https://youtu.be/uUyAFlIdBqw?si=SX0b7e8BM6J7Qg59"
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

    st.subheader("Concepto")

    st.write(
        "La segunda ley de Newton explica la relación "
        "entre fuerza, masa y aceleración."
    )

    st.write(
        "Mientras mayor sea la fuerza aplicada sobre un cuerpo, "
        "mayor será su aceleración."
    )

    st.write(
        "Sin embargo, mientras mayor sea la masa, "
        "más difícil será acelerar el objeto."
    )

    st.subheader("Fórmula")

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

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Empujar un carrito vacío requiere menos fuerza "
        "que empujar un carrito lleno."
    )

    mostrar_video(
        "https://youtu.be/RlXxqscdnYw?si=SPaq5V3PDetwwSfT"
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
# TERCERA LEY
# --------------------------------------------------------

elif seleccion == "Tercera Ley":

    st.header("Tercera Ley de Newton")

    st.subheader("Concepto")

    st.write(
        "La tercera ley de Newton establece que "
        "a toda acción corresponde una reacción "
        "de igual magnitud y sentido contrario."
    )

    st.subheader("Explicación")

    st.write(
        "Las fuerzas siempre aparecen en pares. "
        "Si un objeto ejerce fuerza sobre otro, "
        "el segundo objeto ejerce una fuerza igual "
        "pero opuesta."
    )

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Cuando una persona camina, empuja el suelo hacia atrás "
        "y el suelo impulsa a la persona hacia adelante."
    )

    fuerza = st.slider(
        "Fuerza de acción",
        1,
        100,
        20
    )

    st.success(
        f"La fuerza de reacción también es de {fuerza} N."
    )

    mostrar_video(
        "https://youtu.be/wMBPOkMO69o?si=fnh1MluZAID-tjY1"
    )

    ejercicio_opcion_multiple(
    "Ejercicio Tercera Ley",

    "¿Qué establece la tercera ley de Newton?",

    [
        "La fuerza desaparece",
        "Toda acción tiene una reacción",
        "Los objetos no se mueven",
        "La masa cambia"
    ],

    "Toda acción tiene una reacción",

    """
La tercera ley establece que
a toda acción corresponde
una reacción igual y opuesta.
    """
)


# --------------------------------------------------------
# APLICACIONES
# --------------------------------------------------------

elif seleccion == "Aplicaciones de las Leyes de Newton":

    st.header("Aplicaciones de las Leyes de Newton")

    st.write(
        "Las leyes de Newton tienen aplicaciones "
        "en numerosos campos de la ciencia y la ingeniería."
    )

    st.subheader("Aplicaciones comunes")

    st.write(
        """
- Lanzamiento de cohetes
- Movimiento de automóviles
- Diseño de puentes
- Deportes
- Aviación
- Astronomía
- Satélites artificiales
        """
    )

    st.subheader("Aplicación en astronomía")

    st.write(
        "Las órbitas planetarias y el movimiento de satélites "
        "pueden analizarse utilizando las leyes de Newton."
    )

    mostrar_video(
        "https://youtu.be/86ZNmoAdlNg?si=ILSGube9z924-kWr"
    )

# --------------------------------------------------------
# TRABAJO
# --------------------------------------------------------

elif seleccion == "Trabajo":

    st.header("Trabajo")

    st.subheader("Concepto")

    st.write(
        "En física, el trabajo representa la energía "
        "transferida cuando una fuerza desplaza un objeto."
    )

    st.write(
        "El trabajo depende de la fuerza aplicada, "
        "la distancia recorrida y el ángulo entre ambas."
    )

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

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Empujar una caja a lo largo del suelo "
        "es un ejemplo de trabajo mecánico."
    )

    mostrar_video(
        "https://youtu.be/_xtJLgOAIH4?si=zP8UrIczKC2sYSB3"
    )

    ejercicio_numerico(
    "Ejercicio Trabajo",

    "Ingrese el trabajo realizado por una fuerza de 20 N aplicada durante 5 m",

    100,

    0.1,

    """
1. Fórmula:

W = Fd

2. Sustituimos:

20 × 5

3. Resultado:

100 J
    """
)


# --------------------------------------------------------
# ENERGÍA CINÉTICA
# --------------------------------------------------------

elif seleccion == "Energía Cinética":

    st.header("Energía Cinética")

    st.subheader("Concepto")

    st.write(
        "La energía cinética es la energía "
        "que posee un cuerpo debido a su movimiento."
    )

    st.write(
        "Mientras mayor sea la velocidad o la masa, "
        "mayor será la energía cinética."
    )

    st.latex(r"E_k = \frac{1}{2}mv^2")

    masa = st.slider("Masa", 1, 100, 10)

    velocidad = st.slider("Velocidad", 1, 100, 20)

    energia = 0.5 * masa * (velocidad**2)

    st.success(f"Energía cinética: {energia:.2f} J")

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Un automóvil en movimiento posee energía cinética."
    )

    mostrar_video(
        "https://youtu.be/cL4H9Vwd8v4?si=dSDS8OPYtIhi_Cky"
    )

    ejercicio_opcion_multiple(
    "Ejercicio Energía Cinética",

    "¿Cuál es la energía cinética de un cuerpo de 10 kg que viaja a 4 m/s?",

    [
        "40 J",
        "60 J",
        "80 J",
        "100 J"
    ],

    "80 J",

    """
1. Fórmula:

Ek = 1/2 mv²

2. Sustituimos:

1/2 (10)(4²)

3. Resultado:

80 J
    """
)


# --------------------------------------------------------
# ENERGÍA POTENCIAL
# --------------------------------------------------------

elif seleccion == "Energía Potencial y Conservación":

    st.header("Energía Potencial y Conservación")

    st.subheader("Concepto")

    st.write(
        "La energía potencial es la energía almacenada "
        "debido a la posición de un objeto."
    )

    st.write(
        "La energía mecánica total puede conservarse "
        "cuando no existen pérdidas por fricción."
    )

    st.latex(r"E_p = mgh")

    masa = st.slider("Masa", 1, 100, 10)

    altura = st.slider("Altura", 1, 100, 20)

    energia = masa * 9.8 * altura

    st.success(f"Energía potencial: {energia:.2f} J")

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Un libro colocado en una repisa tiene energía potencial."
    )

    mostrar_video(
        "https://youtu.be/AeT_kbFXsQc?si=5bEnur2Xx_-NtxAg"
    )

    ejercicio_numerico(
    "Ejercicio Energía Potencial",

    "Ingrese la energía potencial de un objeto de 5 kg a 10 m",

    490,

    0.1,

    """
1. Fórmula:

Ep = mgh

2. Sustituimos:

5 × 9.8 × 10

3. Resultado:

490 J
    """
)


# --------------------------------------------------------
# MOMENTUM
# --------------------------------------------------------

elif seleccion == "Momentum Lineal":

    st.header("Momentum Lineal")

    st.subheader("Concepto")

    st.write(
        "El momentum lineal representa "
        "la cantidad de movimiento de un cuerpo."
    )

    st.write(
        "Depende de la masa y la velocidad."
    )

    st.latex(r"p = mv")

    masa = st.slider("Masa", 1, 100, 5)

    velocidad = st.slider("Velocidad", 1, 100, 20)

    momentum = masa * velocidad

    st.success(f"Momentum lineal: {momentum} kg·m/s")

    st.subheader("Ejemplo cotidiano")

    st.write(
        "Un camión posee mayor momentum "
        "que una bicicleta debido a su masa."
    )

    mostrar_video(
        "https://youtu.be/-ZJmQ0RCXto?si=xWUuwL8_erCro7gw"
    )

    ejercicio_slider(
    "Ejercicio Momentum",

    "Seleccione el momentum correcto para una masa de 10 kg y velocidad de 5 m/s",

    0,
    100,

    50,

    """
1. Fórmula:

p = mv

2. Sustituimos:

10 × 5

3. Resultado:

50 kg·m/s
    """
)


# --------------------------------------------------------
# CHOQUES
# --------------------------------------------------------

elif seleccion == "Choques":

    st.header("Choques")

    st.subheader("Concepto")

    st.write(
        "Un choque ocurre cuando dos cuerpos "
        "interactúan durante un corto intervalo de tiempo."
    )

    st.write(
        "Durante los choques se conserva "
        "el momentum lineal total."
    )

    st.latex(
        r"m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2"
    )

    st.subheader("Tipos de choques")

    st.write(
        """
- Elásticos
- Inelásticos
- Perfectamente inelásticos
        """
    )

    mostrar_video(
        "https://youtu.be/_zu67RXVuUM?si=9ebOdmLHNgbkxkch"
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