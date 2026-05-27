import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN DE PÁGINA (Estilo Profesional Wide)
st.set_page_config(
    page_title="Booklet Educativo - Física 1",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PARA ESTILO CONSULTORÍA (Opcional, mejora la estética) ---
st.markdown("""
    <style>
    .main-title { font-size: 50px !important; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
    .section-header { border-left: 5px solid #1E3A8A; padding-left: 15px; color: #1E3A8A; font-weight: bold; margin-top: 25px; }
    .info-card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border: 1px solid #E2E8F0; }
    </style>
""", unsafe_allow_html=True)

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
# 2. DEFINICIÓN DEL MENÚ LATERAL (Controlador de Navegación)
# --------------------------------------------------------

st.sidebar.image(
    "imagenes/logo_umg.png",
    width=220
)

temas = [
    "Inicio", 
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
    "Simulación MCUV (Órbitas)",
    "Leyes de Newton",
    "Trabajo", 
    "Energía Cinética", 
    "Energía Potencial y Conservación",
    "Momentum Lineal", 
    "Choques"
]

st.sidebar.title("Menú principal")
seleccion = st.sidebar.radio("Seleccione un módulo:", temas)

# --------------------------------------------------------
# PÁGINA INICIAL
# --------------------------------------------------------

if seleccion == "Inicio":
    # Fila 1: Header Principal
    col_logo, col_text = st.columns([1, 3])
    
    with col_logo:
        # Asegúrate de que la ruta de la imagen sea correcta
        try:
            st.image("imagenes/logo_umg.png", width=220)
        except:
            st.warning("Logo UMG no encontrado en 'imagenes/logo_umg.png'")

    with col_text:
        st.markdown('<p class="main-title">BOOKLET EDUCATIVO INTERACTIVO</p>', unsafe_allow_html=True)
        st.subheader("Física I | Ingeniería en Sistemas de Información")
        st.markdown("**Universidad Mariano Gálvez de Guatemala**")

    st.markdown("---")

    # Fila 2: Información del Proyecto (Columnas de Valor)
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<p class="section-header">Objetivos del Proyecto</p>', unsafe_allow_html=True)
        st.write("""
        Este booklet fue creado como un resumen de los temas vistos durante el curso de Física I. Se incluyó 
        un resumen de cada tema, un video de fuentes curadas durante el semestre, simulaciones dinámicas y 
        validación inmediata de ejercicios.
        """)

    with c2:
        st.markdown('<p class="section-header">Metodología Digital</p>', unsafe_allow_html=True)
        st.write("""
        - **Visualización:** Gráficas dinámicas.
        - **Interactividad:** Parámetros ajustables en tiempo real.
        - **Práctica:** Ejercicios resueltos de ejemplo y ejercicios con retroalimentación paso a paso.
        - **Multimedia:** Vídeos de refuerzo integrados.
        """)

    with c3:
        st.markdown('<p class="section-header">Creado por:</p>', unsafe_allow_html=True)
        st.markdown("""
        Dario Alfredo Rabe Godoy  
        *Carnet: 5190-25-23683*  

        **Facultad:**  
        Ingeniería en Sistemas de Información y Ciencias de la Computación.
        """)

    st.markdown("---")
    
    # Fila 3: Guía de Uso
    st.info("**Instrucción de navegación:** Utilice el menú desplegable en la barra lateral izquierda para explorar los módulos de aprendizaje. Cada módulo contiene teoría, fórmulas y un componente práctico interactivo.")

# --------------------------------------------------------
# MEDICIONES
# --------------------------------------------------------
elif seleccion == "Mediciones":
    st.header("Mediciones y Magnitudes Físicas")
    
    # --------------------------------------------------------
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    # --------------------------------------------------------
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "La **medición** es el proceso fundamental de la física que consiste en comparar una cantidad o magnitud física "
            "desconocida con una unidad estándar preestablecida como patrón de referencia."
        )
        
        st.markdown("**1. Magnitudes Físicas y Dimensionales (SI):**")
        st.write(
            "Las propiedades medibles se dividen en **Fundamentales** (no dependen de otras, como la Longitud [$m$], "
            "Masa [$kg$] y Tiempo [$s$]) y **Derivadas** (combinaciones matemáticas de las anteriores, como la Velocidad [$m/s$] "
            "o la Fuerza [$N = kg \cdot m/s^2$])."
        )
        
        # Tabla formal de dimensionales para darle peso académico
        st.markdown("**Unidades Patrón Básicas (Sistema Internacional):**")
        st.table({
            "Magnitud": ["Longitud", "Masa", "Tiempo", "Corriente Eléctrica"],
            "Unidad Base": ["Metro", "Kilogramo", "Segundo", "Amperio"],
            "Símbolo / Dimensión": ["m", "kg", "s", "A"]
        })

    with col_teoria2:
        st.subheader("Clasificación y Conversión")
        st.markdown("**2. Magnitudes Escalares y Vectoriales:**")
        st.write(
            "- **Escalares:** Quedan completamente definidas con un número y su unidad. No tienen dirección. *(Ejemplos: Masa [5 kg], Tiempo [10 s], Temperatura [180°C]).*\n"
            "- **Vectoriales:** Además del número y la unidad, requieren obligatoriamente una dirección y sentido para tener lógica física. *(Ejemplos: Velocidad [60 km/h al Norte], Fuerza [12 N a 45°]).*"
        )
        
        st.markdown("**3. Factores de Conversión:**")
        st.write(
            "Para operar magnitudes en las mismas ecuaciones, es vital que pertenezcan al mismo sistema homogéneo. "
            "Se utiliza el método del **factor de conversión nulo** (multiplicar por fracciones equivalentes a la unidad) "
            "para transformar dimensionales sin alterar el valor físico real de la medida."
        )
        st.latex(r"1\text{ pulgada} = 2.54\text{ cm} \quad | \quad 1\text{ m/s} = 3.6\text{ km/h}")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            r"**Enunciado:** Un vehículo en un tramo de prueba viaja a una velocidad constante de $90\,\text{km/h}$. "
    r"El ingeniero a cargo realiza una medición local con un sensor de radar ultrasónico que registra un valor "
    r"de $24.5\,\text{m/s}$. Calcule el error porcentual de la medición del sensor, transformando previamente las dimensionales al Sistema Internacional ($\text{m/s}$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Conversión Homogénea de Dimensionales**")
            st.write("Convertimos el valor teórico real ($90\text{ km/h}$) a metros por segundo ($m/s$):")
            st.latex(r"v = 90\,\frac{\text{km}}{\text{h}} \times \left(\frac{1000\,\text{m}}{1\,\text{km}}\right) \times \left(\frac{1\,\text{h}}{3600\,\text{s}}\right)")
            st.latex(r"v_{\text{real}} = \frac{90000\,\text{m}}{3600\,\text{s}} = 25.0\,\text{m/s}")
            
        with col_res2:
            st.markdown("**Paso 2: Cálculo del Error Porcentual**")
            st.write("Aplicamos la fórmula analítica del error:")
            st.latex(r"\text{Error \%} = \frac{|25.0\,\text{m/s} - 24.5\,\text{m/s}|}{25.0\,\text{m/s}} \times 100")
            st.latex(r"\text{Error \%} = \frac{0.5}{25.0} \times 100 = 2.00\%")
            st.info("**Resultado:** El error instrumental del sensor es exactamente del **2.00%**, lo cual está dentro de los rangos de tolerancia permitidos en ingeniería de tránsito.")

    st.markdown("---")

    
    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Simulador Interactivo de Error Instrumental")
    st.write("Modificá el deslizador para simular diferentes lecturas de un instrumento y analizar cómo impacta la desviación matemática en la gráfica de control.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        valor_real = 50.0  # Unidad estándar arbitraria
        valor_medido = st.slider("Lectura del instrumento de medición", 40.0, 60.0, 48.0, step=0.5)
        
        error = (abs(valor_real - valor_medido) / valor_real) * 100
        st.latex(r"\text{Error \%} = \frac{|Valor\ Real - Valor\ Medido|}{Valor\ Real} \times 100")
        st.success(f"Error porcentual calculado dinámicamente: {error:.2f}%")
        
    with col_sim2:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.bar(["Valor Real", "Tu Medición"], [valor_real, valor_medido], color=["#1f77b4", "#e41a1c"], width=0.5)
        ax.set_ylabel("Magnitud (Unidades)")
        ax.set_ylim(0, 70)
        
        for i, v in enumerate([valor_real, valor_medido]):
            ax.text(i, v + 1.5, f"{v:.1f}", ha="center", fontweight="bold")
            
        ax.grid(True, axis='y', linestyle="--", alpha=0.5)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # Funciones auxiliares de video y evaluación al final
    mostrar_video("https://youtu.be/hXBBBTbqWPY?si=pge4frOmQEN1QHFW")
    ejercicio_opcion_multiple(
        "Evaluación Rápida: Mediciones",
        "Si el valor real de una constante de masa es 100 kg y un laboratorio entrega un reporte de 96 kg, ¿cuál es el error porcentual de la muestra?",
        ["2%", "4%", "6%", "8%"], "4%",
        "1. Diferencia absoluta:\n|100 - 96| = 4 kg\n\n2. Razón respecto al valor real:\n4 / 100 = 0.04\n\n3. Conversión a porcentaje:\n0.04 × 100 = 4%"
    )

# --------------------------------------------------------
# VECTORES
# --------------------------------------------------------
elif seleccion == "Vectores":
    st.header("Vectores en el Plano Bidimensional")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "Un **vector** es un ente matemático que se utiliza en física para representar magnitudes que no pueden "
            "definirse únicamente con un número real, sino que requieren una orientación espacial. "
            "A diferencia de un escalar, un vector queda determinado por tres propiedades indispensables:"
        )
        st.write(
            "- **Magnitud o Módulo:** Representa la longitud o valor numérico de la cantidad física medida. "
            "Se calcula algebraicamente mediante el Teorema de Pitágoras.\n"
            "- **Dirección:** Es el ángulo de inclinación de la línea de acción del vector respecto a un eje de referencia "
            "(usualmente el eje X positivo), determinado mediante funciones trigonométricas.\n"
            "- **Sentido:** Indicado gráficamente por la punta de la flecha, señala hacia dónde se dirige el vector sobre su línea de acción."
        )

    with col_teoria2:
        st.subheader("Formulación Analítica")
        st.write(
            "En un plano de dos dimensiones (2D), un vector se descompone en sus componentes rectangulares "
            "ortogonales ($x$ e $y$). Las expresiones matemáticas fundamentales para su cálculo analítico son:"
        )
        st.markdown("**Cálculo del Módulo:**")
        st.latex(r"|\vec{v}| = \sqrt{x^2 + y^2}")
        
        st.markdown("**Cálculo de la Dirección (Ángulo):**")
        st.latex(r"\theta = \tan^{-1}\left(\frac{y}{x}\right)")
        st.write(
            "Nota: Dependiendo de los signos algebraicos de las componentes $x$ e $y$, el ángulo obtenido "
            "debe ajustarse al cuadrante cartesiano correspondiente para reflejar la dirección real del vector."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Una fuerza aplicada sobre un nodo de anclaje estructural posee las componentes rectangulares "
            "$\vec{F} = (-8\,\text{N},\, 6\,\text{N})$. Calcule analíticamente la magnitud de la fuerza resultante y determine "
            "su dirección angular exacta medida desde el eje X positivo de referencia."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Cálculo del Módulo (Magnitud)**")
            st.write("Sustituimos las componentes ortogonales de la fuerza en la ecuación pitagórica:")
            st.latex(r"|\vec{F}| = \sqrt{(-8\,\text{N})^2 + (6\,\text{N})^2}")
            st.latex(r"|\vec{F}| = \sqrt{64 + 36} = \sqrt{100} = 10.00\,\text{N}")
            
        with col_res2:
            st.markdown("**Paso 2: Cálculo de la Dirección Angular**")
            st.write("Determinamos el ángulo base utilizando la función de la tangente inversa:")
            st.latex(r"\theta_{\text{base}} = \tan^{-1}\left(\frac{6}{-8}\right) \approx -36.87^\circ")
            st.write(
                "Dado que la componente X es negativa y la componente Y es positiva, el vector se localiza "
                "en el **Segundo Cuadrante**. Ajustamos el ángulo sumando $180^\circ$:"
            )
            st.latex(r"\theta_{\text{real}} = -36.87^\circ + 180^\circ = 143.13^\circ")
            st.info("Resultado: La fuerza resultante posee una magnitud de **10.00 N** orientada a **143.13°** respecto al eje horizontal.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Geométrico Interactivo")
    st.write("Ajustá los controles deslizantes para alterar las componentes espaciales y observar en tiempo real cómo cambia la magnitud del vector en el plano cartesiano.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        x = st.slider("Componente rectangular X", -10, 10, 5)
        y = st.slider("Componente rectangular Y", -10, 10, 4)
        
        magnitud = math.sqrt(x**2 + y**2)
        st.success(f"Magnitud calculada del vector: {magnitud:.2f} unidades")
        
    with col_sim2:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.arrow(0, 0, x, y, head_width=0.4, head_length=0.6, length_includes_head=True, color="#1f77b4")
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.6)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # funciones y video
    mostrar_video("https://youtu.be/IrTeyyzerjI?si=fWPFEwXVfI2tflec")
    ejercicio_numerico(
        "Ejercicio Vectores", "Ingrese la magnitud del vector (6,8)", 10, 0.1,
        "1. Aplicamos:\n√(x² + y²)\n\n2. Sustituimos:\n√(6² + 8²)\n\n3. Resultado:\n10"
    )

# --------------------------------------------------------
# SUMA GRÁFICA
# --------------------------------------------------------
elif seleccion == "Suma de vectores por método gráfico":
    st.header("Suma de Vectores por Método Gráfico")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "La **suma gráfica de vectores** es un procedimiento geométrico utilizado para determinar el efecto "
            "combinado de dos o más magnitudes vectoriales de la misma especie (como fuerzas o desplazamientos) "
            "actuando sobre un sistema. A diferencia de la suma aritmética común, el método gráfico respeta la "
            "orientación espacial de cada vector."
        )
        st.write(
            "El método más utilizado en dos dimensiones es el **Método del Polígono** (o cabeza con cola). "
            "Este consiste en dibujar el primer vector a escala desde un origen cartesiano, y a partir de la punta (cabeza) "
            "de este, trazar el segundo vector manteniendo su magnitud, dirección y sentido exactos."
        )

    with col_teoria2:
        st.subheader("Propiedades de la Resultante")
        st.write(
            "El **vector resultante** ($\vec{R}$) representa el vector único capaz de producir el mismo efecto físico "
            "que todos los vectores originales juntos. Geométricamente, la resultante se obtiene trazando una línea "
            "recta que parte estrictamente desde el origen del primer vector hasta la cabeza del último vector colocado."
        )
        st.write(
            "Este método es altamente intuitivo para visualizar la dirección y sentido del sistema resultante, "
            "sirviendo como validación visual indispensable antes de realizar cálculos algebraicos complejos."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un topógrafo realiza dos desplazamientos consecutivos en un terreno plano. "
            "El primer desplazamiento es $\vec{A} = (4.0\,\text{m},\, 3.0\,\text{m})$ y el segundo es "
            "$\vec{B} = (5.0\,\text{m},\, 2.0\,\text{m})$. Determine analítica y gráficamente las componentes rectangulares "
            "del vector de desplazamiento resultante ($\vec{R}$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Suma de Componentes en el Eje X**")
            st.write("Agrupamos y sumamos algebraicamente las proyecciones horizontales:")
            st.latex(r"R_x = A_x + B_x")
            st.latex(r"R_x = 4.0\,\text{m} + 5.0\,\text{m} = 9.0\,\text{m}")
            
        with col_res2:
            st.markdown("**Paso 2: Suma de Componentes en el Eje Y**")
            st.write("Agrupamos y sumamos algebraicamente las proyecciones verticales:")
            st.latex(r"R_y = A_y + B_y")
            st.latex(r"R_y = 3.0\,\text{m} + 2.0\,\text{m} = 5.0\,\text{m}")
            st.info("Resultado: Las componentes analíticas del desplazamiento total son $\vec{R} = (9.0\,\text{m},\, 5.0\,\text{m})$.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Construcción Geométrica Interactiva")
    st.write("Modificá los deslizadores para alterar las dimensiones de los vectores base y observar cómo se construye la cadena geométrica cabeza con cola.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Vectores de Entrada")
        ax1 = st.slider("Vector A - Componente X", -10, 10, 4)
        ay1 = st.slider("Vector A - Componente Y", -10, 10, 3)
        bx1 = st.slider("Vector B - Componente X", -10, 10, 5)
        by1 = st.slider("Vector B - Componente Y", -10, 10, 2)
        
        rx = ax1 + bx1
        ry = ay1 + by1
        st.success(f"Coordenadas de la Resultante R: ({rx}, {ry}) unidades")
        
    with col_sim2:
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
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
        "1. Aplicamos Pitágoras:\nR = \sqrt{9^2 + 5^2}\n\n2. Elevamos:\nR = \sqrt{81 + 25}\n\n3. Sumamos:\nR = \sqrt{106}\n\n4. Resultado:\nR \approx 10.30"
    )

# --------------------------------------------------------
# SUMA ANALÍTICA
# --------------------------------------------------------
elif seleccion == "Suma de vectores por método analítico":
    st.header("Suma de Vectores por Método Analítico")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **método analítico** es el procedimiento más preciso para sumar vectores concurrentes en un plano. "
            "A diferencia del método gráfico, elimina los errores de escala y apreciación instrumental al fundamentarse "
            "completamente en el álgebra y la trigonometría rectangular."
        )
        st.write(
            "Este principio establece que la proyección en el eje X de la resultante ($\vec{R}$) es igual a la suma algebraica "
            "de todas las componentes horizontales del sistema. De igual forma, la proyección en el eje Y corresponde "
            "a la sumatoria de todas las componentes verticales independientes."
        )

    with col_teoria2:
        st.subheader("Formulación y Composición")
        st.write(
            "Una vez obtenidas las sumatorias totales de las componentes ortogonales ($R_x$ y $R_y$), el sistema vectorial "
            "se reduce a un único par coordenado. La magnitud geométrica final y su orientación se calculan mediante:"
        )
        st.latex(r"R_x = \sum V_x \quad | \quad R_y = \sum V_y")
        st.latex(r"R = \sqrt{R_x^2 + R_y^2}")
        st.latex(r"\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Dos fuerzas concurrentes actúan sobre un perno de sujeción mecánica. "
            "La fuerza $\vec{A} = (4.0\,\text{N},\, 3.0\,\text{N})$ y la fuerza $\vec{B} = (2.0\,\text{N},\, 5.0\,\text{N})$. "
            "Determine de forma analítica el vector de fuerza resultante y calcule el valor exacto de su magnitud en Newtons ($N$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Sumatoria del Sistema Ortogonal**")
            st.write("Efectuamos la descomposición y suma analítica por ejes independientes:")
            st.latex(r"R_x = A_x + B_x = 4.0\,\text{N} + 2.0\,\text{N} = 6.0\,\text{N}")
            st.latex(r"R_y = A_y + B_y = 3.0\,\text{N} + 5.0\,\text{N} = 8.0\,\text{N}")
            st.write("El vector resultante unificado queda expresado como $\vec{R} = (6.0,\, 8.0)\,\text{N}$.")
            
        with col_res2:
            st.markdown("**Paso 2: Composición del Módulo Resultante**")
            st.write("Aplicamos el Teorema de Pitágoras sobre las componentes totales calculadas:")
            st.latex(r"|\vec{R}| = \sqrt{(6.0\,\text{N})^2 + (8.0\,\text{N})^2}")
            st.latex(r"|\vec{R}| = \sqrt{36 + 64} = \sqrt{100} = 10.00\,\text{N}")
            st.info("Resultado: La magnitud exacta de la fuerza total que experimenta el perno es de **10.00 N**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Matemático Interactivo")
    st.write("Ingresá los valores numéricos de las componentes para evaluar analíticamente los cambios del vector resultante en el plano cartesiano.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        axv = st.number_input("Componente A_x", value=4.0)
        ayv = st.number_input("Componente A_y", value=3.0)
        bxv = st.number_input("Componente B_x", value=2.0)
        byv = st.number_input("Componente B_y", value=5.0)
        
        rx = axv + bxv
        ry = ayv + byv
        magnitud = math.sqrt(rx**2 + ry**2)
        st.success(f"Resultante: ({rx:.2f}, {ry:.2f}) | Magnitud total: {magnitud:.2f} unidades")
        
    with col_sim2:
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
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
    mostrar_video("https://youtu.be/nQnxMF1Jwso?si=IoeW9yppEjouXB9g")
    ejercicio_opcion_multiple(
        "Ejercicio Suma Analítica", "Dos vectores tienen componentes A=(4,3) y B=(2,5). ¿Cuál es la magnitud del vector resultante?",
        ["8.60", "10.00", "7.21", "6.00"], "10.00",
        "1. Sumamos componentes en X:\nRx = 4 + 2 = 6\n\n2. Sumamos componentes en Y:\nRy = 3 + 5 = 8\n\n3. Aplicamos Pitágoras:\nR = \\sqrt{6^2 + 8^2}\n\n4. Resolvemos:\nR = \\sqrt{36 + 64} -> R = \\sqrt{100}\n\n5. Resultado final:\nR = 10"
    )


# --------------------------------------------------------
# MRU
# --------------------------------------------------------
elif seleccion == "MRU":
    st.header("Movimiento Rectilíneo Uniforme")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento Rectilíneo Uniforme (MRU)** es el modelo cinemático más simple de la mecánica clásica. "
            "Describe el desplazamiento de un cuerpo a lo largo de una trayectoria completamente recta con la propiedad "
            "fundamental de que su **velocidad permanece constante** durante todo el intervalo temporal."
        )
        st.write(
            "Debido a que la velocidad no sufre variaciones ni en magnitud, dirección o sentido, se concluye "
            "estrictamente que la aceleración en este sistema es completamente nula ($a = 0$). El móvil recorre "
            "distancias exactamente iguales en intervalos de tiempo iguales."
        )

    with col_teoria2:
        st.subheader("Formulación Cinemática")
        st.write(
            "La relación matemática que gobierna este movimiento es lineal y relaciona de forma directa la posición, "
            "el tiempo transcurrido y la tasa de cambio posicional:"
        )
        st.latex(r"d = v \cdot t")
        st.write(
            "Donde en el Sistema Internacional (SI), la distancia ($d$) se mide en metros ($m$), el tiempo ($t$) en "
            "segundos ($s$) y la velocidad ($v$) en metros por segundo ($m/s$)."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un tren de carga de alta velocidad se desplaza en línea recta manteniendo una velocidad "
            "constante de $20.0\,\text{m/s}$ a lo largo de un tramo de vía ferroviaria automatizada. Determine analíticamente "
            "la distancia total en metros ($m$) que el tren habrá recorrido tras un tiempo continuo de operación de $10.0\,\text{seconds}$."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Planteamiento Analítico**")
            st.write("Identificamos las variables del sistema físico homogéneo:")
            st.latex(r"v = 20.0\,\text{m/s} \quad | \quad t = 10.0\,\text{s}")
            
        with col_res2:
            st.markdown("**Paso 2: Sustitución Algebraica**")
            st.write("Aplicamos la ecuación cinemática para el cálculo posicional lineal:")
            st.latex(r"d = (20.0\,\text{m/s}) \times (10.0\,\text{s})")
            st.latex(r"d = 200.0\,\text{m}")
            st.info("Resultado: El tren de carga recorre una distancia lineal exacta de **200.0 metros**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Gráfico e Interactivo")
    st.write("Modificá las variables dinámicas de rapidez y tiempo de recorrido para observar el comportamiento lineal de la pendiente de posición.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        velocidad = st.slider("Velocidad constante (m/s)", 1, 50, 10)
        tiempo = st.slider("Tiempo de trayecto (s)", 1, 20, 5)
        
        distancia = velocidad * tiempo
        st.success(f"Distancia calculada dinámicamente: {distancia} m")
        
    with col_sim2:
        st.subheader("Gráfica Distancia vs Tiempo")
        tiempo_x = np.linspace(0, tiempo, 100)
        distancia_y = velocidad * tiempo_x
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(tiempo_x, distancia_y, color="orange", linewidth=2.5, label="Posición Lineal (x)")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Distancia (m)")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento Rectilíneo Uniformemente Variado (MRUV)**, también conocido como acelerado, describe el "
            "desplazamiento de un objeto sobre una trayectoria recta mientras experimenta un cambio constante en su velocidad "
            "a lo largo del tiempo."
        )
        st.write(
            "La propiedad crítica de este movimiento es que la **aceleración permanece constante** ($\vec{a} = \text{constante}$). "
            "Esto implica que la velocidad del móvil aumenta o disminuye de manera lineal y proporcional por cada segundo que transcurre. "
            "Si la aceleración tiene el mismo signo que la velocidad, el cuerpo acelera; si tiene signo opuesto, el cuerpo frena o desacelera."
        )

    with col_teoria2:
        st.subheader("Formulación Cinemática")
        st.write(
            "El comportamiento cinemático se rige por ecuaciones cuadráticas para la posición y lineales para la velocidad, "
            "dependiendo directamente de las condiciones iniciales del sistema:"
        )
        st.latex(r"v_f = v_i + a \cdot t")
        st.latex(r"d = v_i \cdot t + \frac{1}{2}a \cdot t^2")
        st.write(
            "Donde en el Sistema Internacional (SI), la velocidad inicial ($v_i$) y final ($v_f$) se expresan en metros por segundo ($m/s$), "
            "la aceleración ($a$) en metros por segundo al cuadrado ($m/s^2$), el tiempo ($t$) en segundos ($s$) y la distancia ($d$) en metros ($m$)."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un vehículo de pruebas arranca desde el reposo con una velocidad inicial de $10.0\,\text{m/s}$. "
            "Al ingresar a una pista recta de aceleración, activa sus sistemas y experimenta una aceleración constante de $5.0\,\text{m/s}^2$ "
            "durante un intervalo de tiempo continuo de $4.0\,\text{seconds}$. Calcule de forma analítica la velocidad final lograda en metros por segundo ($m/s$) "
            "y la distancia total recorrida en metros ($m$) bajo este régimen de aceleración."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Cálculo de la Velocidad Final**")
            st.write("Aplicamos la ecuación lineal de velocidad con los parámetros del sistema:")
            st.latex(r"v_f = v_i + a \cdot t")
            st.latex(r"v_f = 10.0\,\text{m/s} + (5.0\,\text{m/s}^2 \times 4.0\,\text{s})")
            st.latex(r"v_f = 10.0 + 20.0 = 30.0\,\text{m/s}")
            
        with col_res2:
            st.markdown("**Paso 2: Cálculo del Desplazamiento Lineal**")
            st.write("Evaluamos la ecuación cuadrática de posición para determinar el espacio recorrido:")
            st.latex(r"d = v_i \cdot t + \frac{1}{2}a \cdot t^2")
            st.latex(r"d = (10.0\,\text{m/s} \times 4.0\,\text{s}) + \frac{1}{2}(5.0\,\text{m/s}^2 \times (4.0\,\text{s})^2)")
            st.latex(r"d = 40.0\,\text{m} + \frac{1}{2}(5.0 \times 16.0)\,\text{m}")
            st.latex(r"d = 40.0\,\text{m} + 40.0\,\text{m} = 80.0\,\text{m}")
            st.info("Resultado: El automóvil alcanza una velocidad de **30.0 m/s** y recorre un total de **80.0 metros**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis de Curvatura Cinemática")
    st.write("Modificá los deslizadores de velocidad inicial, aceleración y tiempo para analizar cómo cambia la curvatura de la parábola de posición.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        vi = st.slider("Velocidad inicial (m/s)", 0, 50, 10)
        a = st.slider("Aceleración constante (m/s²)", -10, 20, 5)
        t = st.slider("Tiempo transcurrido (s)", 1, 20, 5)
        
        vf = vi + a * t
        d = vi * t + 0.5 * a * (t**2)
        st.success(f"Velocidad final en t: {vf:.2f} m/s")
        st.success(f"Distancia acumulada recorrida: {d:.2f} m")
        
    with col_sim2:
        st.subheader("Gráfica Distancia vs Tiempo")
        t_arr = np.linspace(0, t, 100)
        d_arr = vi * t_arr + 0.5 * a * (t_arr**2)
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(t_arr, d_arr, color="red", linewidth=2.5, label="Trayectoria Parabólica (x)")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Distancia (m)")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    st.header("Caída Libre de los Cuerpos")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "La **Caída Libre** es un caso particular del MRUV en el cual un cuerpo se deja descender verticalmente "
            "desde una altura determinada, partiendo estrictamente del reposo ($v_i = 0$). La característica primordial "
            "de este modelo es que se desprecia por completo la resistencia friccional del aire u otro fluido."
        )
        st.write(
            "Bajo estas condiciones ideales, todos los cuerpos (independientemente de su masa, peso o forma) "
            "experimentan exactamente la misma aceleración hacia el centro de la Tierra, acelerando de forma uniforme "
            "conforme caen."
        )

    with col_teoria2:
        st.subheader("La Constante Gravitacional")
        st.write(
            "La aceleración que gobierna este movimiento es la **aceleración de la gravedad** ($\vec{g}$), cuyo valor "
            "estándar promedio adoptado a nivel del mar se define analíticamente mediante:"
        )
        st.latex(r"g = 9.8\,\text{m/s}^2")
        st.write("Las ecuaciones cinemáticas adaptadas para el eje vertical son lineales para rapidez y cuadráticas para la altura:")
        st.latex(r"v = g \cdot t \quad | \quad h = \frac{1}{2}g \cdot t^2")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un componente de hardware experimental se suelta desde una plataforma de andamiaje elevada. "
            "El objeto tarda un intervalo de tiempo exacto de $4.0\,\text{seconds}$ en impactar la superficie de control inferior. "
            "Despreciando la fricción con la atmósfera, determine de forma analítica la velocidad de impacto final en metros por segundo ($m/s$) "
            "y calcule la altura total recorrida por la muestra en metros ($m$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Cálculo de la Velocidad Terminal**")
            st.write("Evaluamos la velocidad final en función del tiempo transcurrido:")
            st.latex(r"v = g \cdot t")
            st.latex(r"v = (9.8\,\text{m/s}^2) \times (4.0\,\text{s}) = 39.20\,\text{m/s}")
            
        with col_res2:
            st.markdown("**Paso 2: Cálculo de la Altura de Caída**")
            st.write("Aplicamos la integral de posición para determinar el espacio vertical:")
            st.latex(r"h = \frac{1}{2}g \cdot t^2")
            st.latex(r"h = \frac{1}{2}(9.8\,\text{m/s}^2) \times (4.0\,\text{s})^2")
            st.latex(r"h = 4.9 \times 16.0 = 78.40\,\text{m}")
            st.info("Resultado: El objeto alcanza una velocidad final de **39.20 m/s** al caer desde una altura de **78.40 metros**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Dinámico de Caída")
    st.write("Ajustá el control de tiempo de caída para observar la posición instantánea del objeto y calcular la altura consumida por la gravedad.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        g = 9.8
        tiempo = st.slider("Tiempo de caída (s)", 1, 10, 3)
        
        velocidad = g * tiempo
        altura = 0.5 * g * (tiempo**2)
        st.success(f"Velocidad instantánea lograda: {velocidad:.2f} m/s")
        st.success(f"Altura neta recorrida: {altura:.2f} m")
        
    with col_sim2:
        st.subheader("Representación del Desplazamiento Vertical")
        t_arr = np.linspace(0, tiempo, 100)
        h_arr = altura - (0.5 * g * (t_arr**2))
        
        fig, ax = plt.subplots(figsize=(4, 5))
        # Dibujamos la línea de trayectoria guía
        ax.plot(np.zeros_like(h_arr), h_arr, color="#1f77b4", linestyle="--", alpha=0.5, linewidth=1.5)
        # Dibujamos el objeto como un punto de masa esférico en su posición actual
        ax.scatter(0, h_arr[-1], color="#e41a1c", s=150, zorder=3)
        
        ax.set_ylabel("Altura respecto al suelo (m)")
        ax.set_xlim(-2, 2)
        ax.set_ylim(-5, altura + 5)
        ax.set_xticks([])  # Ocultamos divisiones del eje X que no aportan valor
        ax.grid(True, axis='y', linestyle="--", alpha=0.5)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    st.header("Tiro Vertical Ascendente")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Tiro Vertical** ocurre cuando un objeto es lanzado hacia arriba con una velocidad inicial "
            "diferente de cero ($v_i > 0$), describiendo una trayectoria recta perpendicular al suelo. "
            "Durante la fase de ascenso, el vector de la aceleración gravitacional ($\vec{g}$) actúa en sentido "
            "opuesto al movimiento, comportándose como una desaceleración constante."
        )
        st.write(
            "Este efecto provoca que la rapidez del objeto disminuya de manera uniforme hasta anularse por "
            "completo ($v = 0$) en el punto más alto del recorrido. A este punto se le conoce analíticamente "
            "como la **altura máxima** ($h_{\text{máx}}$)."
        )

    with col_teoria2:
        st.subheader("Análisis de la Parábola Temporal")
        st.write(
            "La gráfica de Altura vs. Tiempo se modela mediante una función matemática de segundo grado (cuadrática). "
            "El signo negativo en el término cuadrático de la aceleración define una **parábola cóncava hacia abajo**:"
        )
        st.latex(r"h = v_i \cdot t - \frac{1}{2}g \cdot t^2")
        st.write(
            "Físicamente, la curvatura de la parábola demuestra que el objeto cambia su posición de manera no lineal: "
            "recorre distancias cada vez más pequeñas por cada unidad de tiempo transcurrida a medida que se aproxima "
            "a su cúspide, reflejando la pérdida progresiva de energía cinética."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un proyectil de calibración es disparado verticalmente hacia arriba desde una estación de prueba "
            "con una velocidad inicial de $30.0\,\text{m/s}$. Calcule de forma analítica la altura neta en metros ($m$) alcanzada "
            "por el dispositivo exactamente a los $2.0\,\text{seconds}$ de haber iniciado su trayectoria ascendente."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Identificación de Variables**")
            st.write("Extraemos los valores del sistema físico en unidades del Sistema Internacional:")
            st.latex(r"v_i = 30.0\,\text{m/s} \quad | \quad t = 2.0\,\text{s} \quad | \quad g = 9.8\,\text{m/s}^2")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Cuadrática**")
            st.write("Sustituimos los parámetros en la ecuación de desplazamiento vertical:")
            st.latex(r"h = (30.0\,\text{m/s} \times 2.0\,\text{s}) - \frac{1}{2}(9.8\,\text{m/s}^2 \times (2.0\,\text{s})^2)")
            st.latex(r"h = 60.0\,\text{m} - \frac{1}{2}(9.8 \times 4.0)\,\text{m}")
            st.latex(r"h = 60.0\,\text{m} - 19.6\,\text{m} = 40.40\,\text{m}")
            st.info("Resultado: El proyectil logra una altura de **40.40 metros** al cabo de los dos segundos indicados.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Simulación Parabólica del Ascenso")
    st.write("Modificá la velocidad de salida y el tiempo transcurrido para analizar la variación de la curva parabólica del movimiento.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        vi = st.slider("Velocidad inicial de disparo (m/s)", 10, 100, 40)
        tiempo = st.slider("Tiempo de vuelo evaluado (s)", 1, 10, 3)
        g = 9.8
        
        h = vi * tiempo - 0.5 * g * (tiempo**2)
        st.success(f"Altura calculada en tiempo t: {h:.2f} m")
        
    with col_sim2:
        st.subheader("Perfil de Altura vs Tiempo (Curva Cinemática)")
        t_arr = np.linspace(0, tiempo, 100)
        h_arr = vi * t_arr - 0.5 * g * (t_arr**2)
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(t_arr, h_arr, color="purple", linewidth=2.5, label="Trayectoria Cuadrática h(t)")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Altura (m)")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    st.header("Movimiento Semiparabólico")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento Semiparabólico** describe la trayectoria bidimensional que describe un cuerpo al ser lanzado "
            "horizontalmente desde una altura inicial ($h$) con una velocidad puramente horizontal ($v_x = v_i$). "
            "Este fenómeno se fundamenta en el **Principio de Independencia de los Movimientos** establecido por Galileo Galilei."
        )
        st.write(
            "Según este principio, el desplazamiento resultante es la combinación superpuesta de dos movimientos "
            "simultáneos que actúan de forma completamente independiente sin interferir entre sí."
        )

    with col_teoria2:
        st.subheader("Análisis de Ejes Independientes")
        st.write(
            "- **Eje Horizontal (X):** No experimenta ninguna fuerza externa tras el lanzamiento, por lo que actúa bajo un "
            "**MRU** a velocidad constante ($v_x = \text{constante}$).\n"
            "- **Eje Vertical (Y):** Está sometido de manera exclusiva a la aceleración de la gravedad ($g$), por lo que actúa "
            "exactamente como una **Caída Libre** partiendo de una velocidad inicial vertical nula ($v_{iy} = 0$)."
        )
        st.write("Las ecuaciones de control cinemático para determinar el tiempo total de vuelo y el alcance horizontal máximo son:")
        st.latex(r"t = \sqrt{\frac{2h}{g}} \quad | \quad x = v_x \cdot t")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un dispositivo de monitoreo industrial es proyectado de forma horizontal con una velocidad inicial "
            "de $10.0\,\text{m/s}$ desde el borde superior de una torre de distribución que posee una altura neta de $20.0\,\text{m}$. "
            "Despreciando la fricción con la atmósfera, determine analíticamente el tiempo total de caída en segundos ($s$) "
            "y calcule el alcance horizontal máximo logrado por el componente antes del impacto."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Cálculo del Tiempo de Vuelo**")
            st.write("Determinamos el tiempo analítico basándonos puramente en la restricción geométrica vertical de la caída libre:")
            st.latex(r"t = \sqrt{\frac{2 \cdot 20.0\,\text{m}}{9.8\,\text{m/s}^2}} = \sqrt{\frac{40.0}{9.8}} \approx 2.02\,\text{s}")
            
        with col_res2:
            st.markdown("**Paso 2: Cálculo del Alcance Horizontal**")
            st.write("Utilizamos el tiempo de vuelo calculado para evaluar el desplazamiento rectilíneo uniforme en el eje X:")
            st.latex(r"x = v_x \cdot t")
            st.latex(r"x = (10.0\,\text{m/s}) \times (2.02\,\text{s}) = 20.20\,\text{m}")
            st.info("Resultado: El dispositivo tarda **2.02 segundos** en caer y logra un alcance horizontal máximo de **20.20 metros**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Cinémetico de la Semiparábola")
    st.write("Modificá la velocidad horizontal de disparo y la altura inicial de la plataforma para analizar la curvatura de la media parábola.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        velocidad = st.slider("Velocidad horizontal inicial (m/s)", 1, 50, 20)
        altura = st.slider("Altura inicial de lanzamiento (m)", 1, 100, 20)
        g = 9.8
        
        tiempo = math.sqrt((2 * altura) / g)
        alcance = velocidad * tiempo
        st.success(f"Tiempo de caída estimado: {tiempo:.2f} s")
        st.success(f"Alcance horizontal obtenido: {alcance:.2f} m")
        
    with col_sim2:
        st.subheader("Perfil Geométrico de la Trayectoria")
        t_arr = np.linspace(0, tiempo, 100)
        x_arr = velocidad * t_arr
        y_arr = altura - (0.5 * g * (t_arr**2))
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(x_arr, y_arr, color="teal", linewidth=2.5, label="Semiparábola Cinemática")
        ax.set_xlabel("Distancia Horizontal (m)")
        ax.set_ylabel("Altura (m)")
        ax.set_ylim(bottom=0)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento de Proyectiles** (o Tiro Parabólico) es el análisis cinemático bidimensional de un objeto "
            "lanzado con un ángulo de inclinación ($\theta$) respecto a la horizontal. Al igual que el movimiento semiparabólico, "
            "se rige bajo el Principio de Independencia de los Movimientos de Galileo."
        )
        st.write(
            "La diferencia crítica radica en que la velocidad inicial ($\vec{v}_i$) no es puramente horizontal. "
            "El vector debe descomponerse trigonométricamente en sus componentes rectangulares ortogonales iniciales "
            "para poder realizar el análisis por separado en cada eje:"
        )
        st.latex(r"v_{ix} = v_i \cdot \cos\theta \quad | \quad v_{iy} = v_i \cdot \sin\theta")

    with col_teoria2:
        st.subheader("Ecuaciones de Trayectoria Coordenada")
        st.write(
            "El comportamiento del proyectil es gobernado simultáneamente por un **MRU** horizontal y un **MRUV** vertical "
            "bajo la acción constante y desaceleradora de la aceleración de la gravedad ($g = 9.8\,\text{m/s}^2$):"
        )
        st.latex(r"x = (v_i \cdot \cos\theta) \cdot t")
        st.latex(r"y = (v_i \cdot \sin\theta) \cdot t - \frac{1}{2}g \cdot t^2")
        st.write(
            "A partir de estas expresiones analíticas, se deducen las fórmulas fundamentales para ingeniería que calculan "
            "el tiempo de vuelo total ($t_v$) y el alcance horizontal máximo acumulado ($R$):"
        )
        st.latex(r"t_v = \frac{2v_i \cdot \sin\theta}{g} \quad | \quad R = \frac{v_i^2 \cdot \sin(2\theta)}{g}")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un espécimen de prueba cinemática es lanzado desde el suelo con una velocidad inicial "
            "de $20.0\,\text{m/s}$ y un ángulo de tiro de $45.0^\circ$. Despreciando los efectos disipativos de la fricción del aire, "
            "calcule de forma analítica el alcance horizontal máximo en metros ($m$) logrado por el proyectil antes de regresar al nivel del suelo."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Planteamiento y Descomposición**")
            st.write("Identificamos los parámetros físicos iniciales del proyectil:")
            st.latex(r"v_i = 20.0\,\text{m/s} \quad | \quad \theta = 45.0^\circ \quad | \quad g = 9.8\,\text{m/s}^2")
            st.write("Para calcular el alcance total, empleamos la identidad del ángulo doble en la fórmula de rango:")
            st.latex(r"2\theta = 2 \times 45.0^\circ = 90.0^\circ")
            
        with col_res2:
            st.markdown("**Paso 2: Resolución Algebraica del Rango**")
            st.write("Sustituimos las magnitudes cinemáticas homogéneas en la ecuación de rango:")
            st.latex(r"R = \frac{(20.0\,\text{m/s})^2 \times \sin(90.0^\circ)}{9.8\,\text{m/s}^2}")
            st.latex(r"R = \frac{400.0 \times 1.0}{9.8} \approx 40.82\,\text{m}")
            st.info("Resultado: El proyectil logra un alcance horizontal máximo exacto de **40.82 metros**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Parabólico Dinámico")
    st.write("Ajustá las variables de velocidad de salida y ángulo de inclinación para comprobar geométricamente el alcance del vector resultante.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="top")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        v0 = st.slider("Velocidad inicial (m/s)", 10, 50, 25)
        angulo_grados = st.slider("Ángulo de lanzamiento (°)", 15, 90, 45)
        
        g = 9.8
        ang_rad = math.radians(angulo_grados)
        t_vuelo = (2 * v0 * math.sin(ang_rad)) / g
        distancia_max = (v0**2 * math.sin(2 * ang_rad)) / g
        
        st.success(f"Distancia máxima estimada: {distancia_max:.2f} m")
        
    with col_sim2:
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

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
    st.subheader("Video de ejemplo")
    mostrar_video("https://youtu.be/lsStZ8xH4y4?si=_kahycp9XCW_HT61")

    st.markdown("---")
    st.subheader("Evaluación del Tema")

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
    st.header("Movimiento Circular Uniforme")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento Circular Uniforme (MCU)** describe la trayectoria de un objeto que se desplaza "
            "alrededor de un punto central fijo, manteniendo un radio de curvatura ($r$) constante y describiendo "
            "una trayectoria completamente circunferencial."
        )
        st.write(
            "Aunque la rapidez (el módulo de la velocidad) sea constante, este movimiento posee una propiedad crítica: "
            "el vector de la **velocidad tangencial cambia continuamente de dirección** en cada instante del recorrido. "
            "Cualquier cambio en el vector velocidad genera, por definición, una aceleración."
        )

    with col_teoria2:
        st.subheader("Aceleración Centrípeta")
        st.write(
            "La aceleración responsable de modificar puramente la dirección de la velocidad, obligando al cuerpo "
            "a curvarse en lugar de seguir una trayectoria recta, es la **Aceleración Centrípeta** ($\vec{a}_c$)."
        )
        st.write(
            "Este vector se caracteriza por ser estrictamente perpendicular a la velocidad tangencial y estar "
            "orientado en todo momento **hacia el centro de la trayectoria** circular. Su magnitud analítica se calcula mediante:"
        )
        st.latex(r"a_c = \frac{v^2}{r}")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un componente en un rotor de centrífuga industrial gira describiendo una órbita circular estable "
            "con un radio de curvatura de $5.0\,\text{m}$. Si los sensores registran que el objeto mantiene una velocidad tangencial "
            "constante de $10.0\,\text{m/s}$, calcule analíticamente la magnitud de la aceleración centrípeta en metros por "
            "segundo al cuadrado ($m/s^2$) que soporta la estructura del componente."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Identificación de Parámetros**")
            st.write("Definimos las variables cinemáticas dadas por el sistema ortogonal:")
            st.latex(r"v = 10.0\,\text{m/s} \quad | \quad r = 5.0\,\text{m}")
            
        with col_res2:
            st.markdown("**Paso 2: Sustitución y Cálculo**")
            st.write("Aplicamos la relación matemática de la aceleración hacia el centro de masa:")
            st.latex(r"a_c = \frac{(10.0\,\text{m/s})^2}{5.0\,\text{m}}")
            st.latex(r"a_c = \frac{100.0}{5.0} = 20.00\,\text{m/s}^2")
            st.info("Resultado: El componente experimenta una aceleración centrípeta neta de **20.00 m/s²**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis de Vectores Dinámicos")
    st.write("Ajustá el control de velocidad y radio orbital para calcular la variación del vector de aceleración dirigido hacia el centro.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        velocidad = st.slider("Velocidad tangencial (m/s)", 1, 50, 10)
        radio = st.slider("Radio de la curva (m)", 1, 20, 5)
        
        ac = (velocidad**2) / radio
        st.success(f"Aceleración centrípeta calculada: {ac:.2f} m/s²")
        
    with col_sim2:
        st.subheader("Órbita y Vectores Cinemáticos")
        ang_rad = np.linspace(0, 2*np.pi, 200)
        x_c = radio * np.cos(ang_rad)
        y_c = radio * np.sin(ang_rad)
        
        fig, ax = plt.subplots(figsize=(4, 4))
        # Dibujamos la trayectoria circular de la órbita
        ax.plot(x_c, y_c, linestyle="--", color="gray", alpha=0.7)
        # Posicionamos el objeto físico en la coordenada (radio, 0)
        ax.scatter(radio, 0, color="blue", s=120, zorder=4)
        
        # Vectores dinámicos representativos (Fijamos una escala visual proporcional)
        ax.arrow(radio, 0, 0, radio*0.6, head_width=radio*0.08, length_includes_head=True, color="green")
        ax.arrow(radio, 0, -radio*0.6, 0, head_width=radio*0.08, length_includes_head=True, color="red")
        
        # Etiquetas de texto estables en lugar de leyenda flotante para evitar colisiones visuales
        ax.text(radio * 1.1, radio * 0.3, "Velocidad (v)", color="green", fontsize=9, fontweight="bold")
        ax.text(radio * 0.2, radio * 0.08, "Ac. Centrípeta (ac)", color="red", fontsize=9, fontweight="bold")
        
        lim = radio + 4
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.4)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Movimiento Circular Uniformemente Variado (MCUV)** describe el desplazamiento de un cuerpo "
            "sobre una trayectoria circunferencial donde su velocidad de giro cambia de manera uniforme con "
            "respecto al tiempo. Esto se debe a la acción de una **aceleración angular constante** ($\alpha$)."
        )
        st.write(
            "A diferencia del movimiento circular uniforme, aquí la rapidez tangencial también cambia a un "
            "ritmo constante, introduciendo una componente conocida como aceleración tangencial ($\vec{a}_t$), "
            "la cual es directamente proporcional a la aceleración angular multiplicada por el radio."
        )

    with col_teoria2:
        st.subheader("Formulación Cinemática Rotacional")
        st.write(
            "Las ecuaciones analíticas que gobiernan las variables de rotación son análogas a las del MRUV, "
            "utilizando magnitudes angulares expresadas estrictamente en radianes:"
        )
        st.latex(r"\omega_f = \omega_i + \alpha \cdot t")
        st.latex(r"\theta = \omega_i \cdot t + \frac{1}{2}\alpha \cdot t^2")
        st.write(
            "Donde en el Sistema Internacional (SI), el desplazamiento angular ($\theta$) se mide en radianes ($rad$), "
            "la velocidad angular ($\omega$) en radianes por segundo ($rad/s$) y la aceleración angular ($\alpha$) "
            "en radianes por segundo al cuadrado ($rad/s^2$)."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un volante de inercia acoplado a un motor experimental inicia su operación con una velocidad "
            "angular inicial de $5.0\,\text{rad/s}$. Al activarse la etapa de potencia, experimenta una aceleración angular "
            "constante de $2.0\,\text{rad/s}^2$ durante un intervalo de $5.0\,\text{seconds}$. Calcule de manera analítica la "
            "velocidad angular final obtenida en radianes por segundo ($rad/s$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Planteamiento Analítico**")
            st.write("Identificamos las propiedades de rotación del sistema de transmisión:")
            st.latex(r"\omega_i = 5.0\,\text{m/s} \quad | \quad \alpha = 2.0\,\text{rad/s}^2 \quad | \quad t = 5.0\,\text{s}")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Lineal Angular**")
            st.write("Sustituimos las variables en la ecuación de rapidez de cambio rotacional:")
            st.latex(r"\omega_f = \omega_i + \alpha \cdot t")
            st.latex(r"\omega_f = 5.0\,\text{rad/s} + (2.0\,\text{rad/s}^2 \times 5.0\,\text{s})")
            st.latex(r"\omega_f = 5.0 + 10.0 = 15.00\,\text{rad/s}")
            st.info("Resultado: La velocidad angular final lograda por el volante es de **15.00 rad/s**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Simulador Gráfico del Incremento de Giro")
    st.write("Ajustá los parámetros del deslizador para visualizar geométricamente cómo el objeto barre arcos de circunferencia cada vez mayores por unidad de tiempo.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        wi = st.slider("Velocidad angular inicial (rad/s)", 0, 20, 5)
        alpha = st.slider("Aceleración angular (rad/s²)", 1, 10, 2)
        tiempo = st.slider("Tiempo de giro (s)", 1, 20, 5)
        
        wf = wi + alpha * tiempo
        theta = wi * tiempo + 0.5 * alpha * (tiempo**2)
        st.success(f"Velocidad angular final: {wf:.2f} rad/s")
        st.success(f"Desplazamiento angular: {theta:.2f} rad")
        
    with col_sim2:
        st.subheader("Visualización del Incremento de Velocidad")
        
        # Generamos una distribución de tiempo para graficar puntos discretos de la trayectoria
        t_puntos = np.linspace(0, tiempo, 30)
        # Calculamos el ángulo acumulado en cada punto para evidenciar el incremento
        theta_puntos = wi * t_puntos + 0.5 * alpha * (t_puntos**2)
        
        # Usamos un radio unitario fijo para la representación geométrica de la órbita
        r_grafica = 5
        x_puntos = r_grafica * np.cos(theta_puntos)
        y_puntos = r_grafica * np.sin(ang_linea := np.linspace(0, 2*np.pi, 200))
        
        fig, ax = plt.subplots(figsize=(4, 4))
        # Línea guía de la trayectoria circunferencial completa
        ax.plot(r_grafica * np.cos(ang_linea), r_grafica * np.sin(ang_linea), linestyle="--", color="gray", alpha=0.5)
        
        # Graficamos los puntos. Al acelerar, la distancia entre los puntos consecutivos debe aumentar notablemente
        ax.scatter(x_puntos, r_grafica * np.sin(theta_puntos), c=t_puntos, cmap="copper", s=60, zorder=3, label="Posición en t")
        
        # Flecha indicadora del sentido de giro
        ax.arrow(x_puntos[-1], r_grafica * np.sin(theta_puntos[-1]), -0.1*y_puntos[-1], 0.1*x_puntos[-1], 
                 head_width=0.4, color="brown", length_includes_head=True)
        
        lim = r_grafica + 2
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.3)
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    
    # SECCIÓN 4: EVALUACIÓN Y MULTIMEDIA
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
# LEYES DE NEWTON
# --------------------------------------------------------
elif seleccion == "Leyes de Newton":
    st.header("Leyes de la Dinámica de Newton")
    
    # Navegación interna estructurada mediante componentes nativos
    tab_general, tab_primera, tab_segunda, tab_tercera, tab_aplicaciones = st.tabs([
        "General", "Primera Ley (Inercia)", "Segunda Ley (Dinámica)", "Tercera Ley (Acción/Reacción)", "Aplicaciones"
    ])
    
    # --------------------------------------------------------
    # SUBPUNTO: GENERAL
    # --------------------------------------------------------
    with tab_general:
        col_gen1, col_gen2 = st.columns([1, 1], vertical_alignment="top")
        with col_gen1:
            st.subheader("Principios Fundamentales")
            st.write(
                "Las **Leyes de Newton** constituyen los axiomas centrales de la mecánica clásica a través de los cuales "
                "se describe de forma matemática el comportamiento de los cuerpos cuando actúan fuerzas sobre ellos. "
                "Fueron postuladas por Sir Isaac Newton en 1687 en su obra *Philosophiae Naturalis Principia Mathematica*."
            )
            st.info(
                "• **Primera Ley:** Ley de la inercia y estados de equilibrio.\n\n"
                "• **Segunda Ley:** Ley fundamental de la dinámica (relación fuerza, masa y aceleración).\n\n"
                "• **Tercera Ley:** Principio de acción y reacción recíproca."
            )
        with col_gen2:
            st.subheader("Áreas de Aplicación")
            st.write(
                "El análisis analítico de estos principios es la base del diseño y cálculo de estructuras en diversas "
                "disciplinas tecnológicas de la ingeniería moderna:"
            )
            st.write("- **Ingeniería Mecánica y Civil:** Estática de puentes y cinemática de maquinaria.")
            st.write("- **Ingeniería Aeroespacial:** Dinámica orbital, aeronáutica y propulsión.")
            st.write("- **Diseño Vehicular:** Análisis de colisiones, sistemas de frenado abs y seguridad pasiva.")
            
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
    # SUBPUNTO: PRIMERA LEY
    # --------------------------------------------------------
    with tab_primera:
        col_p1, col_p2 = st.columns([1, 1], vertical_alignment="top")
        with col_p1:
            st.subheader("Ley de la Inercia")
            st.write(
                "La **Primera Ley** establece formalmente que un cuerpo permanecerá en su estado original de reposo "
                "o de movimiento rectilíneo uniforme (MRU) a menos que se vea obligado a cambiar dicho estado "
                "por fuerzas netas externas impresas sobre él."
            )
            st.write(
                "La inercia es la resistencia intrínseca de la masa a modificar su estado cinemático. "
                "En términos analíticos, cuando un sistema se encuentra en equilibrio, se cumple estrictamente que:"
            )
            st.latex(r"\sum \vec{F} = 0 \implies \vec{a} = 0")
            
            fuerza = st.slider("Fuerza neta aplicada (N)", 0, 100, 0, key="slider_p1")
            if fuerza == 0:
                st.success("Equilibrio Estático: La sumatoria de fuerzas es cero (Objeto en reposo).")
                estado_texto = "En reposo\n(v = 0)"
                color_bloque = "#1f77b4"
            else:
                st.warning("Desequilibrio Dinámico: Fuerza neta distinta de cero detectada.")
                estado_texto = "Acelerando\n(v > 0)"
                color_bloque = "#ff7f0e"
                
        with col_p2:
            st.subheader("Diagrama Físico de Inercia")
            fig, ax = plt.subplots(figsize=(5, 3.5))
            
            # Dibujamos el bloque central con dimensiones bien definidas
            ax.text(0.5, 0.5, f"MASA\n{estado_texto}", color="white", weight="bold", 
                    ha="center", va="center", bbox=dict(boxstyle="square,pad=1.2", fc=color_bloque))
            
            # Corregimos la flecha posicionándola externamente para que no la tape el bloque
            if fuerza > 0:
                ax.arrow(0.05, 0.5, 0.2, 0, head_width=0.04, head_length=0.04, color="red", width=0.01, length_includes_head=True)
                ax.text(0.05, 0.56, f"F = {fuerza} N", color="red", weight="bold", fontsize=10)
                
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            st.pyplot(fig)
            plt.close(fig)

        st.markdown("---")
        mostrar_video("https://youtu.uUyAFlIdBqw?si=SX0b7e8BM6J7Qg59")
        ejercicio_verdadero_falso(
            "Ejercicio Primera Ley", "Un objeto permanecerá en reposo si no actúa una fuerza neta sobre él.",
            "Verdadero", "La primera ley indica que mantiene su estado si la sumatoria de fuerzas externas es cero."
        )

    # --------------------------------------------------------
    # SUBPUNTO: SEGUNDA LEY
    # --------------------------------------------------------
    with tab_segunda:
        col_s1, col_s2 = st.columns([1, 1], vertical_alignment="top")
        with col_s1:
            st.subheader("Ley Fundamental de la Dinámica")
            st.write(
                "La **Segunda Ley** cuantifica el concepto de fuerza. Establece que la aceleración que experimenta "
                "un cuerpo es directamente proporcional a la fuerza neta resultante que actúa sobre él, e inversamente "
                "proporcional a la masa inercial del objeto:"
            )
            st.latex(r"\vec{F} = m \cdot \vec{a}")
            
            masa = st.slider("Masa del bloque (kg)", 1, 100, 10, key="slider_s2_m")
            aceleracion = st.slider("Aceleración deseada (m/s²)", 1, 20, 5, key="slider_s2_a")
            fuerza_calc = masa * aceleracion
            st.success(f"Fuerza resultante necesaria recalculada: {fuerza_calc} N")
            
        with col_s2:
            st.subheader("Relación de Magnitudes Proporcionales")
            fig, ax = plt.subplots(figsize=(5, 3.5))
            ax.bar(["Masa (kg)", "Aceleración (m/s²)", "Fuerza (N)"], [masa, aceleracion, fuerza_calc], color=["#1f77b4", "#ff7f0e", "#2ca02c"])
            ax.set_yscale("log")
            ax.set_ylabel("Magnitud (Escala Logarítmica)")
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
    # SUBPUNTO: TERCERA LEY
    # --------------------------------------------------------
    with tab_tercera:
        col_t1, col_t2 = st.columns([1, 1], vertical_alignment="top")
        with col_t1:
            st.subheader("Principio de Acción y Reacción")
            st.write(
                "La **Tercera Ley** postula que las fuerzas en la naturaleza siempre ocurren en pares simétricos "
                "e interactivos. Cuando un cuerpo ejerce una fuerza (acción) sobre un segundo cuerpo, este responde "
                "ejerciendo una fuerza de igual magnitud y dirección, pero en sentido opuesto (reacción) sobre el primero."
            )
            st.latex(r"\vec{F}_{12} = -\vec{F}_{21}")
            
            fuerza_accion = st.slider("Fuerza de acción ejercida (N)", 1, 100, 20, key="slider_t3")
            st.success(f"Fuerza de reacción opuesta calculada: {-fuerza_accion} N")
            
        with col_t2:
            st.subheader("Representación Vectorial del Par Simétrico") 
            fig, ax = plt.subplots(figsize=(5, 3))
            # Ajustamos el grosor y tamaño de la flecha proporcional a los vectores analíticos
            ax.arrow(0, 0, fuerza_accion, 0, head_width=3, color="blue", length_includes_head=True, label="Fuerza Acción")
            ax.arrow(0, 0, -fuerza_accion, 0, head_width=3, color="red", length_includes_head=True, label="Fuerza Reacción")
            ax.set_xlim(-120, 120)
            ax.set_ylim(-10, 10)
            ax.grid(True, axis='x', linestyle="--", alpha=0.5)
            ax.legend(loc="upper right")
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
    # SUBPUNTO: APLICACIONES
    # --------------------------------------------------------
    with tab_aplicaciones:
        col_ap1, col_ap2 = st.columns([1, 1], vertical_alignment="top")
        with col_ap1:
            st.subheader("Ingeniería y Análisis del Entorno Físico")
            st.write("La aplicación analítica de los tres axiomas permite resolver problemas de diseño industrial complejos:")
            st.markdown(
                "- **Sistemas de Propulsión:** Los cohetes se elevan expulsando masa de combustible a alta velocidad hacia abajo, "
                "generando una fuerza de reacción ascendente neta.\n"
                "- **Estática de Estructuras:** Puentes y edificaciones se calculan igualando la sumatoria de fuerzas y momentos "
                "a cero para garantizar un estado estable de inercia de reposo.\n"
                "- **Dinámica Automotriz:** El desarrollo mecánico de bolsas de aire y frenos se fundamenta en controlar el tiempo "
                "de desaceleración de la masa inercial."
            )
        with col_ap2:
            st.info(
                "**Dato de Ingeniería Civil:** Sin el modelado numérico de las leyes dinámicas de Newton, calcular las fuerzas de fricción "
                "y peraltes necesarios en los tramos curvos de las autopistas de montaña en relieves complejos como los de Guatemala sería "
                "imposible, comprometiendo gravemente la adherencia de los vehículos."
            )
            
        st.markdown("---")
        mostrar_video("https://youtu.be/_oxzQLp7ezk?si=E6Yp5L5bV8F9t1X2")

# --------------------------------------------------------
# TRABAJO
# --------------------------------------------------------
elif seleccion == "Trabajo":
    st.header("Trabajo Mecánico")
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Trabajo Mecánico** ($W$) es una magnitud escalar que cuantifica la transferencia de energía "
            "hacia un cuerpo cuando se le aplica una fuerza externa que produce un desplazamiento neto. "
            "No basta con aplicar una fuerza; para que exista trabajo en términos físicos, debe ocurrir un movimiento "
            "a lo largo de la línea de acción de dicha fuerza."
        )

    with col_teoria2:
        st.subheader("Dependencia Angular")
        st.write(
            "La efectividad de la fuerza depende estrictamente del ángulo ($\theta$) formado entre el vector "
            "fuerza y el vector desplazamiento. Analíticamente, el modelo se define como el producto escalar:"
        )
        st.latex(r"W = \vec{F} \cdot \vec{d} = F \cdot d \cdot \cos(\theta)")
        st.write(
            "Si el ángulo es de $0^\circ$, el trabajo es máximo y positivo. Si es de $90^\circ$ (perpendicular), "
            "el trabajo es nulo ($W = 0$), lo que significa que la fuerza no aporta ni retira energía del movimiento."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un operario arrastra un bloque de prueba aplicando una fuerza constante de $20.0\,\text{N}$ "
            "de forma completamente paralela al suelo ($\theta = 0.0^\circ$). Determine analíticamente el trabajo mecánico neto "
            "desarrollado en Joules ($J$) tras desplazar el objeto una distancia horizontal de $5.0\,\text{m}$."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Identificación de Vectores**")
            st.write("Establecemos los módulos físicos del problema en el Sistema Internacional:")
            st.latex(r"F = 20.0\,\text{N} \quad | \quad d = 5.0\,\text{m} \quad | \quad \theta = 0.0^\circ")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Escalar**")
            st.write("Sustituimos las componentes en la función trigonométrica del modelo:")
            st.latex(r"W = 20.0\,\text{N} \times 5.0\,\text{m} \times \cos(0.0^\circ)")
            st.latex(r"W = 100.0 \times 1.0 = 100.00\,\text{J}")
            st.info("Resultado: La transferencia neta de energía en forma de trabajo es de **100.00 Joules**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis de Orientación Vectorial")
    st.write("Ajustá los controles para observar cómo la variación del ángulo modifica radicalmente el signo y la magnitud del trabajo resultante.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        fuerza = st.slider("Fuerza aplicada (N)", 1, 100, 20)
        distancia = st.slider("Distancia recorrida (m)", 1, 50, 10)
        angulo = st.slider("Ángulo relativo (°)", 0, 180, 0)
        
        trabajo = fuerza * distancia * math.cos(math.radians(angulo))
        st.success(f"Trabajo neto realizado: {trabajo:.2f} J")
        
    with col_sim2:
        st.subheader("Dirección de la Fuerza Aplicada")
        ang_rad = math.radians(angulo)
        fig, ax = plt.subplots(figsize=(4, 4))
        
        # Vectores normalizados para una representación clara en el plano coordenado
        ax.arrow(0, 0, 1, 0, head_width=0.06, head_length=0.06, color="green", length_includes_head=True)
        ax.arrow(0, 0, math.cos(ang_rad), math.sin(ang_rad), head_width=0.06, head_length=0.06, color="purple", length_includes_head=True)
        
        ax.text(0.4, -0.15, "Desplazamiento (d)", color="green", fontsize=9, fontweight="bold")
        ax.text(math.cos(ang_rad)*0.6, math.sin(ang_rad)*0.6 + 0.1, "Fuerza (F)", color="purple", fontsize=9, fontweight="bold")
        
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.4)
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "La **Energía Cinética** ($E_k$) es la medida cuantitativa del trabajo acumulado en un objeto "
            "debido exclusivamente a su estado de movimiento lineal. Representa la cantidad de energía escalar "
            "necesaria para acelerar un cuerpo de una masa determinada desde el reposo absoluto hasta una velocidad dada."
        )

    with col_teoria2:
        st.subheader("El Teorema Trabajo-Energía")
        st.write(
            "De acuerdo con el cálculo fundamental, el trabajo neto realizado sobre una partícula se traduce "
            "directamente en un cambio en su energía de movimiento. La relación matemática obedece a una proporción "
            "cuadrática respecto a la velocidad instantánea:"
        )
        st.latex(r"E_k = \frac{1}{2}m \cdot v^2")
        st.write(
            "Esta naturaleza cuadrática implica que si un vehículo duplica su velocidad, su energía cinética no se "
            "duplica, sino que se cuadruplica ($2^2 = 4$). Esto explica la severidad exponencial de los impactos mecánicos."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un bloque de prueba con una masa inercial de $10.0\,\text{kg}$ es impulsado en línea recta "
            "hasta alcanzar una velocidad uniforme de $4.0\,\text{m/s}$. Determine analíticamente la energía cinética total "
            "almacenada por el objeto en Joules ($J$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Parámetros del Sistema**")
            st.write("Extraemos los datos medidos en el laboratorio:")
            st.latex(r"m = 10.0\,\text{kg} \quad | \quad v = 4.0\,\text{m/s}")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Cuadrática**")
            st.write("Sustituimos dentro de la integral de movimiento:")
            st.latex(r"E_k = \frac{1}{2}(10.0\,\text{kg}) \times (4.0\,\text{m/s})^2")
            st.latex(r"E_k = 5.0 \times 16.0 = 80.00\,\text{J}")
            st.info("Resultado: La energía cinética acumulada por la masa es de **80.00 Joules**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Cuadrático del Movimiento")
    st.write("Modificá la velocidad para comprobar visualmente en la curva cómo la energía se eleva de forma exponencial.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        masa = st.slider("Masa (kg)", 1, 100, 10, key="slider_ek_m")
        velocidad = st.slider("Velocidad (m/s)", 1, 100, 20, key="slider_ek_v")
        
        energia = 0.5 * masa * (velocidad**2)
        st.success(f"Energía cinética calculada: {energia:.2f} J")
        
    with col_sim2:
        st.subheader("Crecimiento Exponencial (v²)")
        v_rango = np.linspace(0, 100, 100)
        e_rango = 0.5 * masa * (v_rango**2)
        
        fig, ax = plt.subplots(figsize=(5, 3.5))
        ax.plot(v_rango, e_rango, color="#1f77b4", linewidth=2.5, label="Curva Parabólica $E_k(v)$")
        ax.scatter(velocidad, energia, color="red", s=100, zorder=3, label="Estado Actual")
        ax.set_xlabel("Velocidad (m/s)")
        ax.set_ylabel("Energía Cinética (J)")
        ax.grid(True, linestyle="--", alpha=0.5)
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Energía Coordenada y Almacenamiento")
        st.write(
            "La **Energía Potencial Gravitacional** ($E_p$) representa la energía almacenada por un cuerpo "
            "en virtud de su posición o configuración geométrica dentro de un campo gravitatorio de referencia. "
            "Es un trabajo latente que depende estrictamente de la altura respecto al suelo:"
        )
        st.latex(r"E_p = m \cdot g \cdot h")

    with col_teoria2:
        st.subheader("Ley de Conservación de la Energía")
        st.write(
            "En un sistema mecánico ideal (libre de fuerzas disipativas como la fricción), la **Energía Mecánica Total** "
            "($E_m$) permanece estrictamente constante en cualquier punto de la trayectoria. "
            "La energía no se crea ni se destruye, únicamente se transforma de manera continua:"
        )
        st.latex(r"E_m = E_k + E_p = \text{Constante}")

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Una masa de calibración de $5.0\,\text{kg}$ es suspendida estáticamente a una altura de $10.0\,\text{m}$ "
            "respecto a una superficie de referencia. Tomando un valor de aceleración de la gravedad estándar de $9.8\,\text{m/s}^2$, "
            "calcule analíticamente la energía potencial almacenada por el sistema en Joules ($J$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Variables Mecánicas**")
            st.write("Agrupamos las variables escalares definidas para el sistema:")
            st.latex(r"m = 5.0\,\text{kg} \quad | \quad h = 10.0\,\text{m} \quad | \quad g = 9.8\,\text{m/s}^2")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Lineal**")
            st.write("Sustituimos directamente en la ecuación de posición del campo:")
            st.latex(r"E_p = 5.0\,\text{kg} \times 9.8\,\text{m/s}^2 \times 10.0\,\text{m}")
            st.latex(r"E_p = 49.0 \times 10.0 = 490.00\,\text{J}")
            st.info("Resultado: La energía potencial acumulada en el punto de suspensión es de **490.00 Joules**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis Dinámico del Balance Mecánico")
    st.write("Modificá la masa y la altura del objeto para analizar el comportamiento proporcional de los gráficos de barra energéticos.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        masa = st.slider("Masa (kg)", 1, 100, 10, key="slider_ep_m")
        altura = st.slider("Altura de posición (m)", 1, 100, 20, key="slider_ep_h")
        
        g_const = 9.8
        energia_p = masa * g_const * altura
        st.success(f"Energía potencial calculada: {energia_p:.2f} J")
        
    with col_sim2:
        st.subheader("Balance Mecánico del Sistema Estático") 
        fig, ax = plt.subplots(figsize=(5, 3.8))
        
        # Mostramos visualmente el balance simétrico de la energía mecánica total
        barras = ax.bar(["E. Potencial", "E. Cinética (Mín)", "Energía Total"], [energia_p, 0, energia_p], color=["#ff7f0e", "#aec7e8", "#2ca02c"])
        ax.set_ylabel("Energía (J)")
        ax.grid(True, axis='y', linestyle="--", alpha=0.4)
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
    
    # SECCIÓN 1: TEORÍA ROBUSTA (Doble Columna)
    col_teoria1, col_teoria2 = st.columns([1, 1], vertical_alignment="top")
    
    with col_teoria1:
        st.subheader("Fundamentos Teóricos")
        st.write(
            "El **Momentum Lineal** ($\vec{p}$), también conocido como cantidad de movimiento, es una magnitud "
            "vectorial que cuantifica el estado cinemático de una masa en movimiento continuo. "
            "Describe la dificultad física que presenta un cuerpo para modificar su estado de velocidad o detenerse por completo."
        )

    with col_teoria2:
        st.subheader("Naturaleza Vectorial e Impulso")
        st.write(
            "El momentum comparte la misma dirección y sentido que el vector velocidad. Analíticamente, "
            "se define mediante el producto de la masa inercial escalar por el vector velocidad lineal:"
        )
        st.latex(r"\vec{p} = m \cdot \vec{v}")
        st.write(
            "Este concepto es fundamental en el estudio de colisiones e impactos, ya que de acuerdo con la "
            "Segunda Ley de Newton expresada de forma general, la fuerza neta es igual a la tasa de cambio temporal "
            "del momentum ($\vec{F} = \frac{d\vec{p}}{dt}$)."
        )

    st.markdown("---")

    # SECCIÓN 2: EJERCICIO RESUELTO COMPLETO
    st.subheader("Ejercicio Práctico Resuelto")
    
    with st.container():
        st.markdown(
            "**Enunciado:** Un componente balístico con una masa de $10.0\,\text{kg}$ viaja en una línea de trayectoria de control "
            "a una velocidad constante de $5.0\,\text{m/s}$. Calcule analíticamente la cantidad de momentum lineal absoluto "
            "almacenado por la muestra en kilogramos metros por segundo ($kg \cdot m/s$)."
        )
        
        col_res1, col_res2 = st.columns([1, 1], vertical_alignment="top")
        with col_res1:
            st.markdown("**Paso 1: Variables Cinemáticas**")
            st.write("Registramos las propiedades inerciales elementales:")
            st.latex(r"m = 10.0\,\text{kg} \quad | \quad v = 5.0\,\text{m/s}")
            
        with col_res2:
            st.markdown("**Paso 2: Evaluación Lineal**")
            st.write("Multiplicamos las variables vectoriales ortogonales:")
            st.latex(r"p = 10.0\,\text{kg} \times 5.0\,\text{m/s}")
            st.latex(r"p = 50.00\,\text{kg} \cdot \text{m/s}")
            st.info("Resultado: La cantidad de movimiento lineal calculada para la masa es de **50.00 kg·m/s**.")

    st.markdown("---")

    # SECCIÓN 3: COMPONENTE INTERACTIVO Y SIMULADOR
    st.subheader("Análisis de Proporcionalidad del Momentum")
    st.write("Modificá las magnitudes en los deslizadores para comprobar cómo cambia la escala de la cantidad de movimiento de forma lineal.")

    col_sim1, col_sim2 = st.columns([1, 1], vertical_alignment="center")
    with col_sim1:
        st.subheader("Cálculos Dinámicos")
        masa = st.slider("Masa del cuerpo (kg)", 1, 100, 5, key="slider_p_m")
        velocidad = st.slider("Velocidad lineal (m/s)", 1, 100, 20, key="slider_p_v")
        
        momentum = masa * velocidad
        st.success(f"Momentum lineal calculado: {momentum:.2f} kg·m/s")
        
    with col_sim2:
        st.subheader("Comparación Relativa de Variables")
        fig, ax = plt.subplots(figsize=(5, 3.5))
        
        ax.bar(["Masa", "Velocidad", "Momentum"], [masa, velocidad, momentum], color=["#9467bd", "#17becf", "#e377c2"])
        ax.set_yscale("log")
        ax.set_ylabel("Magnitud (Escala Logarítmica)")
        ax.grid(True, which="both", linestyle="--", alpha=0.4)
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
    st.header("Colisiones y Leyes de Conservación")
    
    # Navegación interna estructurada mediante componentes nativos por insistencia de cátedra
    tab_diagnostico, tab_elastico, tab_inelastico = st.tabs([
        "Identificación de Choques", "Choques Elásticos", "Choques Inelásticos / Acoplados"
    ])
    
    # --------------------------------------------------------
    # SUBPUNTO: TEORÍA DE IDENTIFICACIÓN
    # --------------------------------------------------------
    with tab_diagnostico:
        col_id1, col_id2 = st.columns([1, 1], vertical_alignment="top")
        
        with col_id1:
            st.subheader("Criterios de Identificación Analítica")
            st.write(
                "En cualquier sistema aislado (donde la sumatoria de fuerzas externas neta es nula), el **Momentum Lineal Total** "
                "permanece estrictamente constante antes, durante y después del impacto. Sin embargo, el comportamiento de la "
                "**Energía Cinética** varía drásticamente, lo que nos permite clasificar e identificar el tipo de colisión:"
            )
            st.markdown(
                "- **Choque Elástico:** Los cuerpos impactan y rebotan separadamente sin sufrir deformaciones permanentes. "
                "No hay disipación térmica. Se conserva tanto el momentum lineal como la energía cinética total.\n"
                "- **Choque Inelástico:** Los cuerpos se separan tras el impacto, pero experimentan deformaciones mecánicas. "
                "El momentum se conserva, pero la energía cinética disminuye al transformarse en calor o energía interna.\n"
                "- **Choque Perfectamente Inelástico:** Es el caso extremo del inelástico. Los cuerpos quedan completamente "
                "**unidos y acoplados** tras la colisión, viajando con una única velocidad final común ($v'_1 = v'_2 = v_f$)."
            )

        with col_id2:
            st.subheader("Modelado Físico General")
            st.write("Ecuación fundamental de conservación del momentum lineal para dos masas en interacción directa:")
            st.latex(r"m_1 \cdot v_1 + m_2 \cdot v_2 = m_1 \cdot v'_1 + m_2 \cdot v'_2")
            st.write("Para identificar el balance de energía cinética ($E_k$), evaluamos el estado antes y después mediante:")
            st.latex(r"\Delta E_k = E_{kf} - E_{ki}")
            st.info(
                "**Regla de Oro de Ingeniería:** Si las masas quedan unidas tras el impacto, diagnostique inmediatamente un "
                "choque perfectamente inelástico. Si rebotan sin pérdida de energía, es estrictamente elástico."
            )

        st.markdown("---")
        mostrar_video("https://youtu.be/_zu67RXVuUM?si=9ebOdmLHNgbkxkch")
        ejercicio_opcion_multiple(
            "Ejercicio Identificación", "¿Qué magnitud se conserva invariante en cualquier tipo de choque aislado?",
            ["Temperatura", "Momentum lineal", "Color", "Volumen"], "Momentum lineal",
            "En un sistema aislado, la cantidad de movimiento o momentum lineal total permanece constante antes y después del impacto."
        )

    # --------------------------------------------------------
    # SUBPUNTO: CHOQUE ELÁSTICO
    # --------------------------------------------------------
    with tab_elastico:
        st.subheader("Simulación Analítica de Choque Elástico")
        st.write("En este sistema, los dos cuerpos rebotan conservando la energía cinética neta ($\Delta E_k = 0$).")
        
        col_el1, col_el2 = st.columns([1, 1], vertical_alignment="top")
        with col_el1:
            st.markdown("**Variables de Entrada (Masas y Velocidades)**")
            m1_el = st.slider("Masa Cuerpo 1 (kg)", 1.0, 20.0, 5.0, key="m1_el")
            v1_el = st.slider("Velocidad Inicial 1 (m/s)", -10.0, 10.0, 4.0, key="v1_el")
            m2_el = st.slider("Masa Cuerpo 2 (kg)", 1.0, 20.0, 8.0, key="m2_el")
            v2_el = st.slider("Velocidad Inicial 2 (m/s)", -10.0, 10.0, -2.0, key="v2_el")
            
            # Ecuaciones explícitas de velocidad final para choques perfectamente elásticos
            v1_fin = ((m1_el - m2_el) * v1_el + 2 * m2_el * v2_el) / (m1_el + m2_el)
            v2_fin = (2 * m1_el * v1_el + (m2_el - m1_el) * v2_el) / (m1_el + m2_el)
            
            # Balances de Energía Cinética
            ek_ini_el = 0.5 * m1_el * (v1_el**2) + 0.5 * m2_el * (v2_el**2)
            ek_fin_el = 0.5 * m1_el * (v1_fin**2) + 0.5 * m2_el * (v2_fin**2)
            
            st.success(f"Velocidad Final Cuerpo 1: {v1_fin:.2f} m/s")
            st.success(f"Velocidad Final Cuerpo 2: {v2_fin:.2f} m/s")

        with col_el2:
            st.markdown("**Gráfica de Comprobación Energética ($E_k$)**")
            
            fig, ax = plt.subplots(figsize=(5, 3.5))
            ax.bar(["$E_k$ Inicial", "$E_k$ Final"], [ek_ini_el, ek_fin_el], color=["#2ca02c", "#2ca02c"], width=0.4)
            ax.set_ylabel("Energía Cinética Total (J)")
            ax.set_ylim(0, max(ek_ini_el, ek_fin_el) * 1.3 if ek_ini_el > 0 else 10)
            ax.grid(True, axis='y', linestyle="--", alpha=0.5)
            
            # Anotaciones numéricas de control sobre las barras
            ax.text(0, ek_ini_el + (ek_ini_el*0.02), f"{ek_ini_el:.2f} J", ha="center", weight="bold")
            ax.text(1, ek_fin_el + (ek_fin_el*0.02), f"{ek_fin_el:.2f} J", ha="center", weight="bold")
            st.pyplot(fig)
            plt.close(fig)
            st.info("Nota: Observe cómo las barras de energía se mantienen perfectamente idénticas antes y después del choque.")

    # --------------------------------------------------------
    # SUBPUNTO: CHOQUE INELÁSTICO
    # --------------------------------------------------------
    with tab_inelastico:
        st.subheader("Simulación Analítica de Choque Perfecto Inelástico (Acoplado)")
        st.write("En este sistema, los cuerpos quedan completamente unidos tras el impacto, disipando la máxima cantidad de energía cinética.")
        
        col_in1, col_in2 = st.columns([1, 1], vertical_alignment="top")
        with col_in1:
            st.markdown("**Variables de Entrada (Masas y Velocidades)**")
            m1_in = st.slider("Masa Cuerpo 1 (kg)", 1.0, 20.0, 5.0, key="m1_in")
            v1_in = st.slider("Velocidad Inicial 1 (m/s)", -10.0, 10.0, 6.0, key="v1_in")
            m2_in = st.slider("Masa Cuerpo 2 (kg)", 1.0, 20.0, 10.0, key="m2_in")
            v2_in = st.slider("Velocidad Inicial 2 (m/s)", -10.0, 10.0, 0.0, key="v2_in")
            
            # Cálculo de la velocidad común del sistema unificado (Acoplado)
            v_comun = (m1_in * v1_in + m2_in * v2_in) / (m1_in + m2_in)
            
            # Balances de Energía Cinética
            ek_ini_in = 0.5 * m1_in * (v1_in**2) + 0.5 * m2_in * (v2_in**2)
            ek_fin_in = 0.5 * (m1_in + m2_in) * (v_comun**2)
            energia_perdida = ek_ini_in - ek_fin_in
            
            st.warning(f"Velocidad Final Común (Masa Acoplada): {v_comun:.2f} m/s")
            st.error(f"Energía Cinética Disipada (Calor/Deformación): {energia_perdida:.2f} J")

        with col_in2:
            st.markdown("**Gráfica de Degradación Energética ($E_k$)**")
            
            fig, ax = plt.subplots(figsize=(5, 3.5))
            ax.bar(["$E_k$ Inicial", "$E_k$ Final"], [ek_ini_in, ek_fin_in], color=["#1f77b4", "#d62728"], width=0.4)
            ax.set_ylabel("Energía Cinética Total (J)")
            ax.set_ylim(0, ek_ini_in * 1.3 if ek_ini_in > 0 else 10)
            ax.grid(True, axis='y', linestyle="--", alpha=0.5)
            
            # Anotaciones numéricas de control sobre las barras
            ax.text(0, ek_ini_in + (ek_ini_in*0.02), f"{ek_ini_in:.2f} J", ha="center", weight="bold")
            ax.text(1, ek_fin_in + (ek_fin_in*0.02), f"{ek_fin_el if ek_fin_in > 0 else 0:.2f} J", ha="center", weight="bold")
            st.pyplot(fig)
            plt.close(fig)
            st.info("Nota: La drástica reducción de la barra final demuestra la conversión de energía cinética en deformación interna estructural.")


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