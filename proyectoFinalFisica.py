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
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Concepto")
        st.write("La medición es el proceso de comparar una magnitud física con una unidad estándar.")
        st.subheader("Fórmula")
        st.latex(r"Error\ porcentual = \frac{|Valor\ real - Valor\ medido|}{Valor\ real} \times 100")
        
        valor_real = 50
        valor_medido = st.slider("Valor medido", 40, 60, 48)
        error = abs(valor_real - valor_medido) / valor_real * 100
        st.success(f"Error porcentual calculado: {error:.2f}%")
        
    with col2:
        st.subheader("Comparación de Valores")
        fig, ax = plt.subplots(figsize=(5, 3.8))
        ax.bar(["Valor Real", "Valor Medido"], [valor_real, valor_medido], color=["#2ca02c", "#d62728"])
        ax.set_ylabel("Magnitud")
        ax.set_ylim(0, 70)
        for i, v in enumerate([valor_real, valor_medido]):
            ax.text(i, v + 1.5, f"{v}", ha="center", fontweight="bold")
        ax.grid(True, axis='y', linestyle="--", alpha=0.5)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/hXBBBTbqWPY?si=pge4frOmQEN1QHFW")
    ejercicio_opcion_multiple(
        "Ejercicio Mediciones",
        "Si el valor real es 100 cm y se mide 96 cm, ¿cuál es el error porcentual?",
        ["2%", "4%", "6%", "8%"], "4%",
        "1. Restamos:\n100 - 96 = 4\n\n2. Dividimos:\n4 / 100 = 0.04\n\n3. Multiplicamos por 100:\n0.04 × 100 = 4%"
    )

# --------------------------------------------------------
# VECTORES
# --------------------------------------------------------
elif seleccion == "Vectores":
    st.header("Vectores")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="top")
    with col1:
        st.subheader("Fundamento Teórico")
        st.write("Los vectores son cantidades físicas que poseen magnitud, dirección y sentido en un plano bidimensional.")
        st.latex(r"|\vec{v}| = \sqrt{x^2 + y^2}")
        
        x = st.slider("Componente X", -10, 10, 5)
        y = st.slider("Componente Y", -10, 10, 4)
        magnitud = math.sqrt(x**2 + y**2)
        st.success(f"Magnitud del vector: {magnitud:.2f}")
        
    with col2:
        st.subheader("Plano Cartesiano") 
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.arrow(0, 0, x, y, head_width=0.4, head_length=0.6, length_includes_head=True, color="#1f77b4")
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.6)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/IrTeyyzerjI?si=fWPFEwXVfI2tflec")
    ejercicio_numerico(
        "Ejercicio Vectores", "Ingrese la magnitud del vector (6,8)", 10, 0.1,
        "1. Aplicamos:\n√(x² + y²)\n\n2. Sustituimos:\n√(6² + 8²)\n\n3. Resultado:\n10"
    )

# --------------------------------------------------------
# SUMA GRÁFICA
# --------------------------------------------------------
elif seleccion == "Suma de vectores por método gráfico":
    st.header("Suma de vectores por método gráfico")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Consiste en colocar vectores cabeza con cola para encontrar la resultante.")
        ax1 = st.slider("Vector A - X", -10, 10, 4)
        ay1 = st.slider("Vector A - Y", -10, 10, 3)
        bx1 = st.slider("Vector B - X", -10, 10, 5)
        by1 = st.slider("Vector B - Y", -10, 10, 2)
        rx = ax1 + bx1
        ry = ay1 + by1
        st.success(f"Vector resultante: ({rx}, {ry})")
        
    with col2:
        st.subheader("Método Cabeza con Cola")
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.arrow(0, 0, ax1, ay1, head_width=0.5, length_includes_head=True, color="blue", label="Vector A")
        ax.arrow(ax1, ay1, bx1, by1, head_width=0.5, length_includes_head=True, color="green", label="Vector B")
        ax.arrow(0, 0, rx, ry, head_width=0.6, length_includes_head=True, color="red", label="Resultante R")
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/TWdLKBC_AgA?si=nYyrSBkGrSPe7dHR")
    ejercicio_slider(
        "Ejercicio Suma Gráfica", 
        "Seleccione la componente X correcta del vector resultante para los vectores A = (4, 3) y B = (5, 2)", 
        -20, 20, 
        9,
        """
1. Sumamos las componentes en X:
Rx = Ax + Bx
Rx = 4 + 5

2. Resultado:
Rx = 9

3. En el método gráfico se colocan los vectores cabeza con cola para obtener la resultante.
        """
    )
    ejercicio_opcion_multiple(
        "Ejercicio Magnitud Resultante", "¿Cuál es la magnitud aproximada del vector resultante R=(9,5)?",
        ["10.30", "8.50", "12.10", "14.00"], "10.30",
        "1. Aplicamos Pitágoras:\nR = √(9² + 5²)\n\n2. Elevamos:\nR = √(81 + 25)\n\n3. Sumamos:\nR = √106\n\n4. Resultado:\nR ≈ 10.30"
    )

# --------------------------------------------------------
# SUMA ANALÍTICA
# --------------------------------------------------------
elif seleccion == "Suma de vectores por método analítico":
    st.header("Suma de vectores por método analítico")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    with col1:
        st.subheader("Análisis por Componentes")
        st.write("Consiste en descomponer cada vector en sus ejes ortogonales para sumarlos de forma independiente.")
        st.latex(r"R_x = A_x + B_x \quad | \quad R_y = A_y + B_y")
        st.latex(r"R = \sqrt{R_x^2 + R_y^2}")
        axv = st.number_input("A_x", value=4.0)
        ayv = st.number_input("A_y", value=3.0)
        bxv = st.number_input("B_x", value=2.0)
        byv = st.number_input("B_y", value=5.0)
        rx = axv + bxv
        ry = ayv + byv
        magnitud = math.sqrt(rx**2 + ry**2)
        st.success(f"Resultante: ({rx}, {ry}) | Magnitud: {magnitud:.2f}")
        
    with col2:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.arrow(0, 0, axv, ayv, head_width=0.4, length_includes_head=True, color="blue", label="Vector A")
        ax.arrow(0, 0, bxv, byv, head_width=0.4, length_includes_head=True, color="green", label="Vector B")
        ax.arrow(0, 0, rx, ry, head_width=0.5, length_includes_head=True, color="purple", label="R resultante")
        lim_dinamico = max(abs(rx), abs(ry), abs(axv), abs(bxv), 5) + 3
        ax.set_xlim(-lim_dinamico, lim_dinamico)
        ax.set_ylim(-lim_dinamico, lim_dinamico)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/nQnxMF1Jwso?si=IoeW9yppEjouXB9g")
    ejercicio_opcion_multiple(
        "Ejercicio Suma Analítica", "Dos vectores tienen componentes A=(4,3) y B=(2,5). ¿Cuál es la magnitud del vector resultante?",
        ["8.60", "10.00", "7.21", "6.00"], "10.00",
        "1. Sumamos componentes en X:\nRx = 4 + 2 = 6\n\n2. Sumamos componentes en Y:\nRy = 3 + 5 = 8\n\n3. Aplicamos Pitágoras:\nR = √(6² + 8²)\n\n4. Resolvemos:\nR = √(36 + 64) -> R = √100\n\n5. Resultado final:\nR = 10"
    )


# --------------------------------------------------------
# MRU
# --------------------------------------------------------
elif seleccion == "MRU":
    st.header("Movimiento Rectilíneo Uniforme")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Es un movimiento donde la velocidad permanece constante.")
        st.latex(r"d = vt")
        velocidad = st.slider("Velocidad (m/s)", 1, 50, 10)
        tiempo = st.slider("Tiempo (s)", 1, 20, 5)
        distancia = velocidad * tiempo
        st.success(f"Distancia recorrida: {distancia} m")
        
    with col2:
        st.subheader("Gráfica Distancia vs Tiempo")
        tiempo_x = np.linspace(0, tiempo, 100)
        distancia_y = velocidad * tiempo_x
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(tiempo_x, distancia_y, color="orange", linewidth=2.5, label="Posición")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Distancia (m)")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/XE9UXxtep6M?si=svZ14z21MkMjt22K")
    ejercicio_slider(
        "Ejercicio MRU", "Seleccione la distancia correcta recorrida por un automóvil que viaja a 20 m/s durante 10 s",
        0, 500, 200, "1. Aplicamos:\nd = vt\n\n2. Sustituimos:\n20 × 10\n\n3. Resultado:\n200 metros"
    )

# --------------------------------------------------------
# MRUV
# --------------------------------------------------------
elif seleccion == "MRUV":
    st.header("Movimiento Rectilíneo Uniformemente Variado")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    with col1:
        st.write("Ocurre cuando un objeto se mueve en línea recta con una aceleración constante.")
        st.latex(r"v_f = v_i + at")
        st.latex(r"d = v_i t + \frac{1}{2}at^2")
        vi = st.slider("Velocidad inicial (m/s)", 0, 50, 10)
        a = st.slider("Aceleración (m/s²)", -10, 20, 5)
        t = st.slider("Tiempo (s)", 1, 20, 5)
        vf = vi + a * t
        d = vi * t + 0.5 * a * (t**2)
        st.success(f"Velocidad final: {vf} m/s")
        st.success(f"Distancia recorrida: {d:.2f} m")
        
    with col2:
        t_arr = np.linspace(0, t, 100)
        d_arr = vi * t_arr + 0.5 * a * (t_arr**2)
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(t_arr, d_arr, color="red", linewidth=2.5, label="Acelerando")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Distancia (m)")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/USFdbyGp8w8?si=nbOSRQwjmpOt5okH")
    ejercicio_numerico(
        "Ejercicio MRUV", "Calcule la velocidad final de un objeto con velocidad inicial de 10 m/s, aceleración de 5 m/s² y tiempo de 4 s",
        30, 0.1, "1. Aplicamos la fórmula:\nvf = vi + at\n\n2. Sustituimos:\nvf = 10 + (5 × 4)\n\n3. Multiplicamos:\nvf = 10 + 20\n\n4. Resultado:\nvf = 30 m/s"
    )
    ejercicio_opcion_multiple(
        "Ejercicio Distancia MRUV", "¿Qué distancia recorre un objeto con vi = 0 m/s, a = 2 m/s² y t = 5 s?",
        ["10 m", "20 m", "25 m", "50 m"], "25 m",
        "1. Aplicamos:\nd = vit + 1/2 at²\n\n2. Sustituimos:\nd = (0)(5) + 1/2(2)(5²)\n\n3. Resolvemos:\nd = 0 + (1)(25)\n\n4. Resultado:\nd = 25 m"
    )

# --------------------------------------------------------
# CAÍDA LIBRE
# --------------------------------------------------------
elif seleccion == "Caída Libre":
    st.header("Caída Libre")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Es el movimiento de un objeto cuando únicamente actúa la fuerza de gravedad sin resistencia del aire.")
        st.latex(r"v = gt")
        st.latex(r"h = \frac{1}{2}gt^2")
        g = 9.8
        tiempo = st.slider("Tiempo de caída (s)", 1, 10, 3)
        velocidad = g * tiempo
        altura = 0.5 * g * (tiempo**2)
        st.success(f"Velocidad: {velocidad:.2f} m/s")
        st.success(f"Altura recorrida: {altura:.2f} m")
        
    with col2:
        st.subheader("Desplazamiento de Caída")
        t_arr = np.linspace(0, tiempo, 100)
        h_arr = altura - (0.5 * g * (t_arr**2))
        fig, ax = plt.subplots(figsize=(3, 4.5))
        ax.plot(np.zeros_like(h_arr), h_arr, color="blue", linestyle="--", alpha=0.4)
        ax.scatter(0, h_arr[-1], color="red", s=120, label="Cuerpo en caída")
        ax.set_ylabel("Altura de caída (m)")
        ax.set_xlim(-1, 1)
        ax.set_ylim(-5, altura + 5)
        ax.set_xticks([])
        ax.grid(True, axis='y', linestyle="--")
        ax.legend(loc="upper right")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/b0FW0grwWks?si=ECRe3WqF4LQdR7pT")
    ejercicio_numerico(
        "Ejercicio Caída Libre", "Calcule la velocidad de un objeto después de 4 segundos de caída libre",
        39.2, 0.1, "1. Aplicamos la fórmula:\nv = gt\n\n2. Sustituimos:\nv = 9.8 × 4\n\n3. Resultado:\nv = 39.2 m/s"
    )
    ejercicio_opcion_multiple(
        "Ejercicio Altura Caída Libre", "¿Qué altura recorre un objeto en 2 segundos de caída libre?",
        ["9.8 m", "19.6 m", "4.9 m", "39.2 m"], "19.6 m",
        "1. Aplicamos:\nh = 1/2 gt²\n\n2. Sustituimos:\nh = 1/2 (9.8)(2²)\n\n3. Elevamos:\n2² = 4\n\n4. Resolvemos:\nh = 4.9 × 4\n\n5. Resultado:\nh = 19.6 m"
    )

# --------------------------------------------------------
# TIRO VERTICAL
# --------------------------------------------------------
elif seleccion == "Tiro Vertical":
    st.header("Tiro Vertical")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Ocurre cuando un objeto es lanzado verticalmente, la gravedad disminuye su velocidad al subir.")
        st.latex(r"h = v_i t - \frac{1}{2}gt^2")
        vi = st.slider("Velocidad inicial (m/s)", 10, 100, 40)
        tiempo = st.slider("Tiempo transcurrido (s)", 1, 10, 3)
        g = 9.8
        h = vi * tiempo - 0.5 * g * (tiempo**2)
        st.success(f"Altura alcanzada: {h:.2f} m")
        
    with col2:
        st.subheader("Perfil de Altura vs Tiempo")
        t_arr = np.linspace(0, tiempo, 100)
        h_arr = vi * t_arr - 0.5 * g * (t_arr**2)
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(t_arr, h_arr, color="purple", linewidth=2.5, label="Lanzamiento Vertical")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Altura (m)")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/K1ex_ingNTY?si=qKSAqsfgi4eIQZbp")
    ejercicio_numerico(
        "Ejercicio Tiro Vertical", "Calcule la altura alcanzada por un objeto lanzado con velocidad inicial de 30 m/s durante 2 segundos",
        40.4, 0.1, "1. Aplicamos la fórmula:\nh = vit - 1/2 gt²\n\n2. Sustituimos:\nh = (30)(2) - 1/2(9.8)(2²)\n\n3. Elevamos:\n2² = 4\n\n4. Resolvemos:\nh = 60 - 19.6\n\n5. Resultado:\nh = 40.4 m"
    )
    ejercicio_opcion_multiple(
        "Ejercicio Velocidad Tiro Vertical", "¿Qué ocurre con la velocidad de un objeto cuando sube en un tiro vertical?",
        ["Aumenta constantemente", "Permanece igual", "Disminuye debido a la gravedad", "Se vuelve negativa instantáneamente"],
        "Disminuye debido a la gravedad", "Durante el ascenso la gravedad actúa en sentido contrario al movimiento. Por eso disminuye hasta llegar momentáneamente a cero en la altura máxima."
    )

# --------------------------------------------------------
# MOVIMIENTO SEMIPARABÓLICO
# --------------------------------------------------------
elif seleccion == "Movimiento semiparabólico":
    st.header("Movimiento semiparabólico")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Ocurre cuando un objeto es lanzado horizontalmente desde cierta altura combinando MRU y caída libre.")
        velocidad = st.slider("Velocidad horizontal (m/s)", 1, 50, 20)
        altura = st.slider("Altura inicial (m)", 1, 100, 20)
        g = 9.8
        tiempo = math.sqrt((2 * altura) / g)
        alcance = velocidad * tiempo
        st.success(f"Tiempo de caída estimado: {tiempo:.2f} s")
        st.success(f"Alcance horizontal obtenido: {alcance:.2f} m")
        
    with col2:
        st.subheader("Mitad de Parábola")
        t_arr = np.linspace(0, tiempo, 100)
        x_arr = velocidad * t_arr
        y_arr = altura - (0.5 * g * (t_arr**2))
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(x_arr, y_arr, color="teal", linewidth=2.5, label="Semiparábola")
        ax.set_xlabel("Distancia Horizontal (m)")
        ax.set_ylabel("Altura (m)")
        ax.set_ylim(bottom=0)
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/vT_jT-6Owo4?si=DA_fjzl24g3gS0Jm")
    ejercicio_numerico(
        "Ejercicio Movimiento Semiparabólico", "Calcule el tiempo de caída de un objeto lanzado horizontalmente desde una altura de 20 m",
        2.02, 0.1, "1. Aplicamos la fórmula:\nt = √(2h/g)\n\n2. Sustituimos:\nt = √((2 × 20)/9.8)\n\n3. Resolvemos:\nt = √(40/9.8)\n\n4. Resultado:\nt ≈ 2.02 s"
    )
    ejercicio_opcion_multiple(
        "Ejercicio Alcance Horizontal", "Si un objeto tiene velocidad horizontal de 10 m/s y tarda 2 s en caer, ¿cuál es su alcance horizontal?",
        ["5 m", "10 m", "20 m", "40 m"], "20 m", "1. Aplicamos:\nR = vt\n\n2. Sustituimos:\nR = 10 × 2\n\n3. Resultado:\nR = 20 m"
    )


# --------------------------------------------------------
# MOVIMIENTO DE PROYECTILES
# --------------------------------------------------------

elif seleccion == "Movimiento de proyectiles":
    st.header("Movimiento de Proyectiles")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    with col1:
        st.subheader("Análisis Parabólico")
        st.write("El movimiento de un proyectil es una combinación de movimiento horizontal con velocidad constante y movimiento vertical con aceleración constante.")
        st.latex(r"x = (v_i \cos\theta)t")
        st.latex(r"y = (v_i \sin\theta)t - \frac{1}{2}gt^2")
        
        v0 = st.slider("Velocidad inicial (m/s)", 10, 50, 25)
        angulo_grados = st.slider("Ángulo de lanzamiento (°)", 15, 90, 45)
        
        g = 9.8
        ang_rad = math.radians(angulo_grados)
        t_vuelo = (2 * v0 * math.sin(ang_rad)) / g
        distancia_max = (v0**2 * math.sin(2 * ang_rad)) / g
        
        st.success(f"Distancia máxima estimada: {distancia_max:.2f} m")
        
    with col2:
        # Generación de la curva parabólica dinámica
        t_pos = np.linspace(0, t_vuelo, 100)
        x_pos = v0 * math.cos(ang_rad) * t_pos
        y_pos = v0 * math.sin(ang_rad) * t_pos - 0.5 * g * (t_pos**2)
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(x_pos, y_pos, color="blue", linewidth=2, label="Trayectoria teórica")
        ax.set_xlabel("Distancia Horizontal (m)")
        ax.set_ylabel("Altura (m)")
        ax.set_ylim(bottom=0)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    # Separador visual para los recursos adicionales y evaluación
    st.markdown("---")
    
    st.subheader("Video de ejemplo")
    mostrar_video("https://youtu.be/lsStZ8xH4y4?si=_kahycp9XCW_HT61")

    st.markdown("---")
    st.subheader("Evaluación del Tema")

    # AQUÍ ESTÁN TUS DOS EJERCICIOS ORIGINALES:
    
    # Ejercicio 1: Numérico
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

    # Ejercicio 2: Opción Múltiple
    ejercicio_opcion_multiple(
        "Ejercicio Ángulo de Proyectiles",
        "¿Con qué ángulo se obtiene el alcance máximo ideal en un lanzamiento de proyectiles?",
        ["30°", "45°", "60°", "90°"],
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
# MOVIMIENTO CIRCULAR
# --------------------------------------------------------
elif seleccion == "Movimiento circular":
    st.header("Movimiento Circular")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Concepto")
        st.write("Ocurre cuando un objeto se desplaza siguiendo una trayectoria circular. La dirección de la velocidad cambia continuamente.")
        st.subheader("Aceleración centrípeta")
        st.latex(r"a_c = \frac{v^2}{r}")
        velocidad = st.slider("Velocidad (m/s)", 1, 50, 10)
        radio = st.slider("Radio de la curva (m)", 1, 20, 5)
        ac = (velocidad**2) / radio
        st.success(f"Aceleración centrípeta: {ac:.2f} m/s²")
        
    with col2:
        st.subheader("Órbita y Vectores Dinámicos")
        ang_rad = np.linspace(0, 2*np.pi, 200)
        x_c = radio * np.cos(ang_rad)
        y_c = radio * np.sin(ang_rad)
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.plot(x_c, y_c, linestyle="--", color="gray")
        ax.scatter(radio, 0, color="blue", s=100, label="Objeto")
        ax.arrow(radio, 0, 0, radio*0.6, head_width=radio*0.1, color="green", label="Velocidad (v)")
        ax.arrow(radio, 0, -radio*0.6, 0, head_width=radio*0.1, color="red", label="Ac. Centrípeta (ac)")
        lim = radio + 4
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.legend(loc="upper right")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/HmkGsCZZNXg?si=LYHkV6sAt_K9FTDZ")
    ejercicio_numerico(
        "Ejercicio Movimiento Circular", "Calcule la aceleración centrípeta si v = 10 m/s y r = 5 m",
        20, 0.1, "1. Fórmula:\na = v²/r\n\n2. Sustituimos:\na = 10² / 5\n\n3. Resultado:\n20 m/s²"
    )

# --------------------------------------------------------
# MOVIMIENTO CIRCULAR UNIFORMEMENTE VARIADO
# --------------------------------------------------------
elif seleccion == "Movimiento circular uniformemente variado":
    st.header("Movimiento Circular Uniformemente Variado")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("El MCUV ocurre cuando un objeto se mueve en trayectoria circular con aceleración angular constante.")
        st.latex(r"\omega_f = \omega_i + \alpha t")
        st.latex(r"\theta = \omega_i t + \frac{1}{2}\alpha t^2")
        wi = st.slider("Velocidad angular inicial (rad/s)", 0, 20, 5)
        alpha = st.slider("Aceleración angular (rad/s²)", 1, 10, 2)
        tiempo = st.slider("Tiempo de giro (s)", 1, 20, 5)
        wf = wi + alpha * tiempo
        theta = wi * tiempo + 0.5 * alpha * (tiempo**2)
        st.success(f"Velocidad angular final: {wf:.2f} rad/s")
        st.success(f"Desplazamiento angular: {theta:.2f} rad")
        
    with col2:
        st.subheader("Gráfica Velocidad Angular vs Tiempo")
        t_arr = np.linspace(0, tiempo, 100)
        w_arr = wi + alpha * t_arr
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(t_arr, w_arr, color="brown", linewidth=2.5, label="Aceleración Angular")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Velocidad Angular (rad/s)")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/VesfI_8ydpA?si=7adjiZ5EuX3wArgV")
    ejercicio_slider(
        "Ejercicio MCUV", 
        "Seleccione la velocidad angular final correcta para un cuerpo con ωi = 5 rad/s, α = 2 rad/s² y t = 5 s", 
        0, 30, 
        15,
        """
1. Fórmula:
ωf = ωi + αt

2. Sustituimos:
ωf = 5 + (2 × 5)

3. Resultado:
ωf = 15 rad/s
        """
    )

# --------------------------------------------------------
# LEYES DE NEWTON (GENERAL)
# --------------------------------------------------------
elif seleccion == "Leyes de Newton":
    st.header("Leyes de Newton")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Principios fundamentales que explican cómo se comportan los cuerpos cuando actúan fuerzas sobre ellos.")
        st.subheader("Resumen de los principios")
        st.info("• Primera Ley: Ley de la inercia.\n\n• Segunda Ley: Relación fuerza, masa y aceleración.\n\n• Tercera Ley: Acción y reacción.")
    with col2:
        st.subheader("Áreas de Aplicación")
        st.write("- Ingeniería Mecánica y Civil\n- Astronomía y Órbitas\n- Diseño Vehicular y Seguridad\n- Aeronáutica y Deportes")
        
    st.markdown("---")
    mostrar_video("https://youtu.be/9lgVjHJqTZc?si=nns1ZACQ3Fvshm3g")
    ejercicio_opcion_multiple(
        "Pregunta General 1", "¿Cuál es la ley de Newton conocida como ley de la inercia?",
        ["Primera Ley", "Segunda Ley", "Tercera Ley", "Ley de gravitación"], "Primera Ley",
        "La Primera Ley establece que un cuerpo mantiene su estado de reposo o MRU si no existe una fuerza neta actuando sobre él."
    )
    ejercicio_opcion_multiple(
        "Pregunta General 2", "¿Qué relación expresa la Segunda Ley de Newton?",
        ["Acción y reacción", "Fuerza, masa y aceleración", "Conservación de energía", "Movimiento circular"], "Fuerza, masa y aceleración",
        "La Segunda Ley establece F = ma. La fuerza neta produce una aceleración directamente proporcional."
    )

# --------------------------------------------------------
# PRIMERA LEY
# --------------------------------------------------------
elif seleccion == "Primera Ley":
    st.header("Primera Ley de Newton")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Inercia")
        st.write("Establece que un cuerpo permanecerá en reposo o en MRU mientras no exista una fuerza neta externa actuando sobre él.")
        fuerza = st.slider("Fuerza neta aplicada (N)", 0, 100, 0)
        
        if fuerza == 0:
            st.success("Equilibrio: El objeto permanece en reposo.")
            estado_texto = "En reposo (v = 0)"
            color_bloque = "blue"
        else:
            st.warning("Fuerza detectada: El objeto cambia su estado de movimiento.")
            estado_texto = "Acelerando (v > 0)"
            color_bloque = "orange"
            
    with col2:
        st.subheader("Diagrama de Inercia")
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.text(0.5, 0.5, f"BLOQUE\n{estado_texto}", color="white", weight="bold", ha="center", va="center", bbox=dict(boxstyle="square,pad=1", fc=color_bloque))
        if fuerza > 0:
            ax.arrow(0.1, 0.5, 0.2, 0, head_width=0.05, color="red", width=0.01)
            ax.text(0.2, 0.58, f"F = {fuerza} N", color="red")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/uUyAFlIdBqw?si=SX0b7e8BM6J7Qg59")
    ejercicio_verdadero_falso(
        "Ejercicio Primera Ley", "Un objeto permanecerá en reposo si no actúa una fuerza neta sobre él.",
        "Verdadero", "La primera ley indica que mantiene su estado si la sumatoria de fuerzas externas es cero."
    )

# --------------------------------------------------------
# SEGUNDA LEY
# --------------------------------------------------------
elif seleccion == "Segunda Ley":
    st.header("Segunda Ley de Newton")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Explica la relación proporcional de las fuerzas con la masa y la aceleración.")
        st.latex(r"F = ma")
        masa = st.slider("Masa del bloque (kg)", 1, 100, 10)
        aceleracion = st.slider("Aceleración deseada (m/s²)", 1, 20, 5)
        fuerza = masa * aceleracion
        st.success(f"Fuerza resultante necesaria: {fuerza} N")
        
    with col2:
        st.subheader("Relación Dinámica")
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.bar(["Masa (kg)", "Aceleración (m/s²)", "Fuerza (N)"], [masa, aceleracion, fuerza], color=["#1f77b4", "#ff7f0e", "#2ca02c"])
        ax.set_yscale("log") # Escala logarítmica para balancear las diferencias numéricas grandes
        ax.set_ylabel("Magnitud (Escala Log)")
        ax.grid(True, which="both", linestyle="--", alpha=0.4)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/RlXxqscdnYw?si=SPaq5V3PDetwwSfT")
    ejercicio_numerico(
        "Ejercicio Segunda Ley", "Calcule la fuerza para una masa de 10 kg y aceleración de 5 m/s²",
        50, 0.1, "1. Fórmula:\nF = ma\n\n2. Sustituimos:\n10 × 5\n\n3. Resultado:\n50 N"
    )

# --------------------------------------------------------
# TERCERA LEY
# --------------------------------------------------------
elif seleccion == "Tercera Ley":
    st.header("Tercera Ley de Newton")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="top")
    with col1:
        st.subheader("Acción y Reacción")
        st.write("Establece que a toda fuerza de acción le corresponde una fuerza de reacción de igual magnitud pero dirección opuesta.")
        fuerza = st.slider("Fuerza de acción ejercida (N)", 1, 100, 20)
        st.success(f"Fuerza de reacción opuesta: {-fuerza} N")
        
    with col2:
        st.subheader("Representación Vectorial") 
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.arrow(0, 0, fuerza, 0, head_width=3, color="blue", length_includes_head=True, label="Acción")
        ax.arrow(0, 0, -fuerza, 0, head_width=3, color="red", length_includes_head=True, label="Reacción")
        ax.set_xlim(-120, 120)
        ax.set_ylim(-10, 10)
        ax.grid(True, axis='x', linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/wMBPOkMO69o?si=fnh1MluZAID-tjY1")
    ejercicio_opcion_multiple(
        "Ejercicio Tercera Ley", "¿Qué establece la tercera ley de Newton?",
        ["La fuerza desaparece", "Toda acción tiene una reacción", "Los objetos no se mueven", "La masa cambia"],
        "Toda acción tiene una reacción", "Las fuerzas siempre aparecen en pares opuestos y simétricos: F12 = -F21"
    )

# --------------------------------------------------------
# APLICACIONES DE LAS LEYES
# --------------------------------------------------------
elif seleccion == "Aplicaciones de las Leyes de Newton":
    st.header("Aplicaciones de las Leyes de Newton")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Permiten modelar desde estructuras mecánicas estáticas hasta ingeniería espacial avanzada.")
        st.markdown("""
        **Campos clave:**
        - **Lanzamiento de cohetes:** Impulso por reacción de gases.
        - **Diseño estructural:** Equilibrio estático en puentes y edificios.
        - **Dinámica automotriz:** Sistemas de frenado, fricción en curvas y bolsas de aire.
        """)
    with col2:
        st.info("**Dato Curioso de Ingeniería:** Sin el análisis vectorial de las aplicaciones de Newton, calcular la fricción necesaria en las curvas de las carreteras de Guatemala sería imposible, provocando derrapes continuos.")

    st.markdown("---")
    mostrar_video("https://youtu.be/_oxzQLp7ezk?si=E6Yp5L5bV8F9t1X2")

# --------------------------------------------------------
# TRABAJO
# --------------------------------------------------------
elif seleccion == "Trabajo":
    st.header("Trabajo")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Representa la energía transferida cuando una fuerza provoca el desplazamiento de un cuerpo.")
        st.latex(r"W = Fd \cos(\theta)")
        fuerza = st.slider("Fuerza aplicada (N)", 1, 100, 20)
        distancia = st.slider("Distancia recorrida (m)", 1, 50, 10)
        angulo = st.slider("Ángulo relativo (°)", 0, 180, 0)
        
        trabajo = fuerza * distancia * math.cos(math.radians(angulo))
        st.success(f"Trabajo neto realizado: {trabajo:.2f} J")
        
    with col2:
        st.subheader("Dirección de la Fuerza")
        ang_rad = math.radians(angulo)
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.arrow(0, 0, 1, 0, head_width=0.05, color="green", length_includes_head=True, label="Desplazamiento (d)")
        ax.arrow(0, 0, math.cos(ang_rad), math.sin(ang_rad), head_width=0.05, color="purple", length_includes_head=True, label="Fuerza (F)")
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.3)
        ax.legend(loc="lower left")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/_xtJLgOAIH4?si=zP8UrIczKC2sYSB3")
    ejercicio_numerico(
        "Ejercicio Trabajo", "Ingrese el trabajo realizado por una fuerza de 20 N aplicada durante 5 m (θ = 0°)",
        100, 0.1, "1. Fórmula:\nW = Fd\n\n2. Sustituimos:\n20 × 5\n\n3. Resultado:\n100 J"
    )

# --------------------------------------------------------
# ENERGÍA CINÉTICA
# --------------------------------------------------------
elif seleccion == "Energía Cinética":
    st.header("Energía Cinética")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Energía que posee un objeto debido exclusivamente a su estado de movimiento.")
        st.latex(r"E_k = \frac{1}{2}mv^2")
        masa = st.slider("Masa (kg)", 1, 100, 10)
        velocidad = st.slider("Velocidad (m/s)", 1, 100, 20)
        energia = 0.5 * masa * (velocidad**2)
        st.success(f"Energía cinética calculada: {energia:.2f} J")
        
    with col2:
        st.subheader("Crecimiento Exponencial (v²)")
        v_rango = np.linspace(0, 100, 100)
        e_rango = 0.5 * masa * (v_rango**2)
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(v_rango, e_rango, color="blue", linewidth=2)
        ax.scatter(velocidad, energia, color="red", s=80, label="Punto Actual")
        ax.set_xlabel("Velocidad (m/s)")
        ax.set_ylabel("Energía Cinética (J)")
        ax.grid(True, linestyle="--")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/cL4H9Vwd8v4?si=dSDS8OPYtIhi_Cky")
    ejercicio_opcion_multiple(
        "Ejercicio Energía Cinética", "¿Cuál es la energía cinética de un cuerpo de 10 kg que viaja a 4 m/s?",
        ["40 J", "60 J", "80 J", "100 J"], "80 J", "1. Fórmula:\nEk = 1/2 mv²\n\n2. Sustituimos:\n1/2 (10)(4²)\n\n3. Resultado:\n80 J"
    )

# --------------------------------------------------------
# ENERGÍA POTENCIAL Y CONSERVACIÓN
# --------------------------------------------------------
elif seleccion == "Energía Potencial y Conservación":
    st.header("Energía Potencial y Conservación")
    
    col1, col2 = st.columns([1, 1], vertical_alignment="top")
    with col1:
        st.subheader("Energía de Posición")
        st.write("La energía potencial depende de la posición. En un sistema ideal sin fricción, la energía mecánica total se conserva.")
        st.latex(r"E_p = mgh")
        masa = st.slider("Masa (kg)", 1, 100, 10)
        altura = st.slider("Altura de posición (m)", 1, 100, 20)
        energia_p = masa * 9.8 * altura
        st.success(f"Energía potencial calculada: {energia_p:.2f} J")
        
    with col2:
        st.subheader("Balance Mecánico") 
        fig, ax = plt.subplots(figsize=(4, 3.8))
        ax.bar(["E. Potencial", "E. Cinética (Mín)", "Energía Total"], [energia_p, 0, energia_p], color=["orange", "lightblue", "green"])
        ax.set_ylabel("Energía (J)")
        ax.grid(True, axis='y', linestyle="--")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/AeT_kbFXsQc?si=5bEnur2Xx_-NtxAg")
    ejercicio_numerico(
        "Ejercicio Energía Potencial", "Ingrese la energía potencial de un objeto de 5 kg a 10 m",
        490, 0.1, "1. Fórmula:\nEp = mgh\n\n2. Sustituimos:\n5 × 9.8 × 10\n\n3. Resultado:\n490 J"
    )

# --------------------------------------------------------
# MOMENTUM LINEAL
# --------------------------------------------------------
elif seleccion == "Momentum Lineal":
    st.header("Momentum Lineal")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Representa la inercia en movimiento de un cuerpo, ligada a su masa y velocidad vectorial.")
        st.latex(r"p = mv")
        masa = st.slider("Masa del cuerpo (kg)", 1, 100, 5)
        velocidad = st.slider("Velocidad lineal (m/s)", 1, 100, 20)
        momentum = masa * velocidad
        st.success(f"Momentum lineal: {momentum} kg·m/s")
        
    with col2:
        st.subheader("Comparación p = m × v")
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.bar(["Masa", "Velocidad", "Momentum"], [masa, velocidad, momentum], color=["purple", "teal", "magenta"])
        ax.set_yscale("log")
        ax.set_ylabel("Valores (Escala Log)")
        ax.grid(True, which="both", linestyle="--", alpha=0.3)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/-ZJmQ0RCXto?si=xWUuwL8_erCro7gw")
    ejercicio_slider(
        "Ejercicio Momentum", "Seleccione el momentum correcto para una masa de 10 kg y velocidad de 5 m/s",
        0, 100, 50, "1. Fórmula:\np = mv\n\n2. Sustituimos:\n10 × 5\n\n3. Resultado:\n50 kg·m/s"
    )

# --------------------------------------------------------
# CHOQUES
# --------------------------------------------------------
elif seleccion == "Choques":
    st.header("Choques")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Colisiones de corto intervalo donde el momentum lineal total se conserva invariante ante la ausencia de fuerzas externas.")
        st.latex(r"m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2")
        st.markdown("""
        **Clasificación fundamental:**
        - **Elásticos:** Se conserva el momentum y la energía cinética total.
        - **Inelásticos:** Se conserva el momentum, pero parte de la energía cinética se disipa.
        - **Perfectamente inelásticos:** Los cuerpos quedan completamente unidos tras el impacto.
        """)
    with col2:
        st.subheader("Conservación del Sistema")
        fig, ax = plt.subplots(figsize=(4, 3.5))
        ax.bar(["Momentum Antes", "Momentum Después"], [100, 100], color=["#2ca02c", "#1f77b4"])
        ax.set_ylim(0, 140)
        ax.set_ylabel("Total p (kg·m/s)")
        ax.text(0, 105, "P_total", ha="center", weight="bold")
        ax.text(1, 105, "P_total", ha="center", weight="bold")
        ax.grid(True, axis='y', linestyle="--")
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    mostrar_video("https://youtu.be/_zu67RXVuUM?si=9ebOdmLHNgbkxkch")
    ejercicio_opcion_multiple(
        "Ejercicio Choques", "¿Qué magnitud se conserva invariante en cualquier tipo de choque aislado?",
        ["Temperatura", "Momentum lineal", "Color", "Volumen"], "Momentum lineal",
        "En un sistema aislado, la cantidad de movimiento o momentum lineal total permanece constante antes y después del impacto."
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