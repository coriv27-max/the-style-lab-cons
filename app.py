import os
import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="The Style Lab",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILOS CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Italianno&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500&display=swap');

    .stApp {
        background-color: #EBEFF7;
        color: #17171C;
        font-family: 'Playfair Display', serif;
    }

    h1, h2, h3, .italianno-title {
        font-family: 'Italianno', cursive !important;
        color: #870005;
        font-weight: 400;
    }

    p, span, label, .stMarkdown {
        font-family: 'Playfair Display', serif;
        color: #17171C;
    }

    .editorial-container {
        background-color: #FFFFFF;
        border: 1px solid #DAE0EC;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(23, 23, 28, 0.05);
        margin-bottom: 1.5rem;
    }

    .stButton>button {
        background-color: #870005;
        color: #FFFFFF;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-family: 'Playfair Display', serif;
        font-weight: 500;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #17171C;
        color: #FFFFFF;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 4px;
        color: #17171C;
        font-family: 'Playfair Display', serif;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background-color: #870005 !important;
        color: #FFFFFF !important;
    }

    .badge {
        display: inline-block;
        background-color: #DAE0EC;
        color: #17171C;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 0.5rem;
    }

    [data-testid="stSidebar"] {
        background-color: #542638;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# 3. CARGA DE DATOS
@st.cache_data
def cargar_datos():
    ruta_csv = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Base de datos de moda.csv"
    )

    if os.path.exists(ruta_csv):
        return pd.read_csv(ruta_csv)

    else:
        data = {
            "seccion": [
                "tendencias", "tendencias", "tendencias", "tendencias",
                "colorimetria", "colorimetria", "colorimetria",
                "tipo de cuerpo", "tipo de cuerpo", "tipo de cuerpo",
                "tipo de cuerpo", "tipo de cuerpo"
            ],

            "tema": [
                "Sastrería sin rigidez", "Volumen protagonista",
                "Romance oscuro", "Cintura baja",
                "Tonos cálidos", "Tonos fríos", "Contraste e intensidad",
                "Reloj de arena", "Triángulo o pera",
                "Triángulo invertido", "Rectángulo", "Óvalo o manzana"
            ],

            "contenido": [
                "Dior, Chanel y Givenchy exploraron chaquetas relajadas. Un blazer con cintura sugerida acompaña la silueta reloj de arena.",
                "Loewe, Mugler y Givenchy destacaron abrigos y hombros. El volumen superior puede equilibrar una silueta triángulo.",
                "McQueen y Givenchy incorporaron encaje y bordados. Los detalles en el torso pueden equilibrar caderas más anchas.",
                "Chanel, Dior, Alaïa y Saint Laurent retomaron la cintura descendida. Puede acompañar una cintura poco marcada o un torso corto.",
                "Marfil, durazno, coral, terracota, mostaza, camel y verde oliva. Sus matices dorados pueden iluminar especialmente los rasgos.",
                "Azul hielo, azul marino, gris azulado, rosa malva, frambuesa y violeta. Sus matices azulados suelen armonizar con plata.",
                "Compara prendas junto al rostro: un blanco nítido y vino intenso frente a gris suave y rosa empolvado.",
                "Hombros y caderas de anchura similar, cintura marcada. Para seguir esa línea, prueba vestidos cruzados o prendas entalladas sin apretar.",
                "Caderas más anchas que hombros. Si buscas equilibrio visual, prueba escotes abiertos y chaquetas con estructura ligera en hombros.",
                "Hombros más anchos que caderas. Para distribuir el volumen, prueba faldas en A, pantalones amplios y escotes en V.",
                "Hombros, cintura y caderas con anchuras próximas. Para crear curvas visuales, prueba cinturones cómodos y vestidos cruzados.",
                "Mayor amplitud en la zona media, a menudo con piernas o brazos más definidos. Prueba telas con caída y líneas verticales."
            ],

            "detalle": [
                "Dior, Chanel, Givenchy",
                "Loewe, Mugler, Givenchy",
                "McQueen, Givenvy",
                "Chanel, Dior, Alaïa",
                "Paleta Cálida",
                "Paleta Fría",
                "Estudio de Contraste",
                "Silueta Proporcionada",
                "Equilibrio Visual",
                "Estructura Superior",
                "Líneas Rectas",
                "Fluidez y Caída"
            ]
        }

        return pd.DataFrame(data)


df_datos = cargar_datos()

# Normalizar nombres de columnas
df_datos.columns = (
    df_datos.columns
    .str.strip()
    .str.lower()
    .str.replace("ó", "o")
)

# Normalizar secciones
df_datos["seccion"] = (
    df_datos["seccion"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("í", "i")
)


# 4. NAVEGACIÓN LATERAL
pagina = st.sidebar.radio(
    "THE STYLE LAB",
    [
        "Inicio",
        "Sobre el proyecto",
        "Tendencias",
        "Colorimetría",
        "Tipo de cuerpo"
    ]
)


# 5. FUNCIÓN PARA LAS SECCIONES DINÁMICAS
def renderizar_seccion_dinamica(
    nombre_seccion,
    titulo_principal,
    subtitulo_seccion
):

    st.markdown(
        f"<h1 style='font-size: 3rem;'>{titulo_principal}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='font-size: 0.9rem; letter-spacing: 2px; color: #870005;'>{subtitulo_seccion}</p>",
        unsafe_allow_html=True
    )

    # Filtrar datos
    df_filtrado = df_datos[
        df_datos["seccion"].str.lower().str.strip()
        == nombre_seccion.lower().strip()
    ]

    if df_filtrado.empty:
        st.warning(
            f"No hay registros disponibles para la sección '{nombre_seccion}'."
        )
        return

    # Selector de temas
    temas = df_filtrado["tema"].tolist()

    seleccion_tema = st.selectbox(
        "Selecciona un concepto clave para explorar:",
        temas,
        key=f"select_{nombre_seccion}"
    )

    # Obtener información del tema
    fila_seleccionada = df_filtrado[
        df_filtrado["tema"] == seleccion_tema
    ].iloc[0]

    st.markdown("---")

    col_izq, col_der = st.columns(
        [1.2, 1],
        gap="large"
    )

    with col_izq:
        st.markdown(f"""
        <div class="editorial-container">
            <h3 style="color: #870005; font-family: 'Playfair Display', serif; font-size: 1.8rem;">
                {fila_seleccionada['tema']}
            </h3>

            <p style="font-size: 1.1rem; line-height: 1.6;">
                {fila_seleccionada['contenido']}
            </p>

            <div class="badge">
                📌 {fila_seleccionada['detalle']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_der:

        # Limpiar el nombre del tema para encontrar la imagen
        nombre_limpio = (
            seleccion_tema.strip().lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace(" ", "_")
        )

        # Crear ruta de la imagen
        nombre_archivo_img = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            f"{nombre_seccion.strip().lower().replace(' ', '_')}_{nombre_limpio}.jpeg"
        )

        # Mostrar imagen si existe
        if os.path.exists(nombre_archivo_img):
            st.image(
                nombre_archivo_img,
                use_container_width=True
            )

        else:
            st.markdown(f"""
            <div class="editorial-container" style="text-align: center; padding: 4rem 1rem; color: #666;">
                <p style="font-style: italic;">Ilustración editorial de pasarela</p>
                <span style="font-size: 0.8rem;">
                    No se encontró: <code>{nombre_archivo_img}</code>
                </span>
            </div>
            """, unsafe_allow_html=True)


# 6. PÁGINA DE INICIO
if pagina == "Inicio":

    st.markdown(
        "<h1 style='text-align: center; font-size: 4rem;'>The Style Lab</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; font-style: italic; font-size: 1.2rem; color: #870005;'>Un espacio para mirar la moda</p>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )

    with col1:
        st.markdown("""
        <div class="editorial-container">
            <h3>La moda también es una forma de contar historias.</h3>
            <p>Explora ideas, siluetas y detalles de pasarela desde una mirada editorial. No se trata de seguir reglas estrictas, sino de descubrir posibilidades y traducir las tendencias a tu propio estilo.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        ruta_banner = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "inicio_banner.jpeg"
        )

        if os.path.exists(ruta_banner):
            st.image(
                ruta_banner,
                use_container_width=True
            )

        else:
            st.markdown("""
            <div class="editorial-container" style="text-align: center; padding: 4rem 1rem; color: #666;">
                <p style="font-style: italic;">Banner principal de inspiración</p>
                <span style="font-size: 0.8rem;">
                    Coloca la imagen en: <code>assets/inicio_banner.jpeg</code>
                </span>
            </div>
            """, unsafe_allow_html=True)


# 7. SOBRE EL PROYECTO
elif pagina == "Sobre el proyecto":

    st.markdown(
        "<h1 style='font-size: 3rem;'>Sobre el proyecto</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='font-size: 0.9rem; letter-spacing: 2px; color: #870005;'>01 / SOBRE NOSOTROS</p>",
        unsafe_allow_html=True
    )

    col_a, col_b = st.columns(
        2,
        gap="large"
    )

    with col_a:
        st.markdown("""
        <div class="editorial-container">
            <h3>Sobre autores</h3>
            <p><strong>The Style Lab</strong> es un espacio editorial para quienes observan la moda con curiosidad. Aquí reunimos referencias e interpretaciones para abrir conversaciones sobre la manera en que vestimos.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="editorial-container">
            <h3>Cómo sirve</h3>
            <p>Recorre las tendencias, conoce los detalles que aparecen en las pasarelas y encuentra una idea que puedas adaptar a tu propio estilo. No se trata de seguir reglas: se trata de descubrir posibilidades.</p>
        </div>
        """, unsafe_allow_html=True)


# 8. TENDENCIAS
elif pagina == "Tendencias":

    renderizar_seccion_dinamica(
        "tendencias",
        "Tendencias con carácter",
        "02 / INFORME DE TEMPORADA · OTOÑO-INVIERNO 2026"
    )


# 9. COLORIMETRÍA
elif pagina == "Colorimetría":

    renderizar_seccion_dinamica(
        "colorimetria",
        "El color también comunica",
        "03 / EL LENGUAJE DEL COLOR"
    )


# 10. TIPO DE CUERPO
elif pagina == "Tipo de cuerpo":

    renderizar_seccion_dinamica(
        "tipo de cuerpo",
        "Vestir tu silueta",
        "04 / SILUETAS Y PROPORCIONES"
    )