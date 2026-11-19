from html import escape
from pathlib import Path
from random import Random

import streamlit as st


st.set_page_config(page_title="Para mi amor", page_icon="💌")
MEDIA = Path(__file__).parent / "media"


# ── 1. TUS MENSAJES ──────────────────────────────────────────

CARTA = """Mi amor, ya van cuatro meses y todavía me da una alegría toda boba cuando sé que te voy a ver. Me gusta poder contarte cualquier cosa y terminar riéndome contigo hasta de las bobadas que me pasan.

Me haces muy feliz. Estaba mirando unas fotos de nosotros y te quería mostrar algo. ❤️"""

RECUERDOS = [
    (
        "salida-1.jpg",
        "Volvería a ese día",
        "Si me dijeras que mañana podemos repetir esta salida, "
        "ya estaría listo para ir por ti.",
    ),
    (
        "salida-2.jpg",
        "Esta me la guardo",
        "Me gusta que ahora tenga lugares por los que paso "
        "y enseguida pienso en ti.",
    ),
]

RAZON = (
    "Porque cuando me pasa algo, así sea la bobada más pequeña del día, "
    "ya estoy pensando en cómo te lo voy a contar. "
    "Me encanta que seas esa persona para mí."
)

SECRETO = (
    "La página estaba arreglada desde el principio… escogieras lo que "
    "escogieras, yo terminaba saliendo contigo dos veces. "
    "Perdón por semejante manipulación jajaja 🤭"
)

DESPEDIDA = (
    "Felices cuatro meses, mi amor. La primera vez que te hice una página "
    "estaba pendiente de si me ibas a decir que sí. Hoy ya sé lo rico "
    "que es salir contigo y aquí estoy, inventándome otra para volver "
    "a invitarte. Qué ganas de verte. Te quiero muchísimo. ❤️"
)


# ── 2. PÁGINAS Y COLORES ─────────────────────────────────────

s = st.session_state
s.setdefault("pagina", 0)
s.setdefault("abiertos", set())
p = s.pagina

# Cada fila corresponde a una pantalla: dos colores de fondo y un acento.
PALETAS = [
    ("#ffc2ce", "#ffc984", "#a02955"),  # Sobre
    ("#ffd6da", "#e4baff", "#962f61"),  # Carta
    ("#b8afff", "#ffbad9", "#553987"),  # Video
    ("#ffcf96", "#ffadbc", "#963854"),  # Primera foto
    ("#b7eadc", "#dfc3ff", "#405f72"),  # Segunda foto
    ("#ffc0ba", "#ffd892", "#993c43"),  # Esta semana
    ("#dac1ff", "#ffce97", "#713565"),  # Segunda cita
    ("#a9e7dc", "#ffc4db", "#315c62"),  # Resumen
    ("#ffb4c8", "#cabaff", "#903057"),  # Despedida
]

a, b, tinta = PALETAS[p]

css = """
<style>
.stApp {
    color: #402837;
    background: linear-gradient(125deg, var(--a), #fff3dd, var(--b), var(--a));
    background-size: 260% 260%;
    animation: cielo 16s ease-in-out infinite alternate;
}
[data-testid="stHeader"] { background: transparent; }
.block-container {
    max-width: 34rem;
    padding: 3.6rem 1.3rem 4rem;
}
h1, h2, h3 {
    font-family: Georgia, serif !important;
    color: var(--t) !important;
    letter-spacing: -.04em;
}
h1 { animation: entra .65s both; }
[data-testid="stCaptionContainer"] { color: #5a4050 !important; }

/* Botones */
div.stButton button {
    width: 100%;
    min-height: 3rem;
    border: 1px solid #ffffffb0;
    border-radius: 18px;
    background: linear-gradient(110deg, var(--t), #813663, var(--t));
    background-size: 220% 100%;
    color: white;
    font-weight: 650;
    box-shadow: 0 6px 15px #61364e24;
    transition: transform .2s, background-position .4s;
}
div.stButton button:hover {
    transform: translateY(-2px);
    background-position: 100%;
    color: white;
}
div.stButton button:active { transform: scale(.97); }
div.stButton button:focus-visible {
    outline: 3px solid #38233e;
    outline-offset: 3px;
}

/* Sobre, sello y papel */
.sobre {
    width: min(255px, 80%);
    height: 150px;
    margin: 4.5rem auto 2rem;
    position: relative;
    isolation: isolate;
    perspective: 650px;
    background: #fcafab;
    border-radius: 9px;
    box-shadow: 0 16px 32px #85234844;
    animation: flotar 3.8s ease-in-out infinite;
}
.sobre:before, .sobre:after {
    content: "";
    position: absolute;
    inset: 0;
}
.sobre:before {
    background: linear-gradient(145deg, #ff868e, #d95177);
    clip-path: polygon(0 0, 100% 0, 50% 62%);
    transform-origin: top;
    z-index: 3;
}
.sobre:after {
    background: linear-gradient(120deg, #ffcfb7, #fa8999);
    clip-path: polygon(0 0, 50% 57%, 100% 0, 100% 100%, 0 100%);
    z-index: 2;
}
.sello {
    position: absolute;
    z-index: 4;
    top: 41%;
    left: 44%;
    color: #a82250;
    font-size: 34px;
    line-height: 1;
    animation: latir 1.8s ease-in-out infinite;
}
.papel {
    position: absolute;
    inset: 10px;
    background: #fff9e9;
    text-align: center;
    padding: 12px;
    font: italic 22px Georgia;
    color: #822b50;
    border-radius: 5px;
}
.abierto { animation: none; }
.abierto:before { animation: tapa .65s forwards; }
.abierto .sello { opacity: 0; }
.abierto .papel { animation: carta .8s .35s both; }

/* Corazones flotantes y confeti */
.adorno {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
}
.adorno i {
    position: absolute;
    left: var(--x);
    top: 0;
    color: var(--c);
    font-size: var(--size);
    font-style: normal;
    animation: subir var(--dur) var(--delay) linear infinite;
    opacity: .45;
}
.fiesta { z-index: 6; }
.fiesta i {
    width: 9px;
    height: 16px;
    border-radius: 3px;
    background: var(--c);
    opacity: 0;
    animation: caer var(--dur) var(--delay) ease-in 1 both;
}

/* Fotos, video, notas y entradas de las citas */
.escena {
    position: relative;
    text-align: center;
    color: var(--t);
    font: 2.1rem Georgia;
    letter-spacing: .22em;
    margin: .25rem auto;
}
.escena span {
    display: inline-block;
    animation: flotar 2.5s ease-in-out infinite alternate;
}
.escena span:nth-child(2) { animation-delay: -1s; }
.escena span:nth-child(3) { animation-delay: -1.7s; }

[data-testid="stImage"] img {
    box-sizing: border-box;
    background: #fffaf3;
    padding: 9px 9px 24px;
    border-radius: 4px;
    box-shadow: 0 10px 20px #48233929;
    animation: foto .85s both;
}
video {
    border-radius: 16px;
    box-shadow: 0 8px 30px #6544aa55;
    animation: entra .8s both;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #fff9ebdc;
    border-radius: 18px;
    border: 2px dashed var(--t) !important;
    animation: entra .65s both;
}
.nota {
    animation: entra .6s both;
    background: #fffbf1eb;
    padding: 16px 20px;
    border-radius: 4px 22px 22px 22px;
    box-shadow: 0 6px 16px #60394f17;
    white-space: pre-line;
}

@keyframes cielo { to { background-position: 100% 80%; } }
@keyframes entra {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: none; }
}
@keyframes flotar {
    50% { transform: translateY(-7px) rotate(-2deg); }
}
@keyframes latir { 50% { transform: scale(1.22); } }
@keyframes tapa { to { transform: rotateX(177deg); z-index: 0; } }
@keyframes carta { to { transform: translateY(-53px); } }
@keyframes foto {
    from { opacity: 0; transform: translateY(22px) rotate(-5deg); }
    to { opacity: 1; transform: rotate(-1deg); }
}
@keyframes subir {
    from { transform: translateY(105vh) rotate(-12deg); }
    to { transform: translate(14px, -8vh) rotate(26deg); }
}
@keyframes caer {
    0% { opacity: 0; transform: translateY(-6vh); }
    6% { opacity: .9; }
    95% { opacity: .85; }
    100% { opacity: 0; transform: translate(28px, 105vh) rotate(400deg); }
}
@media (prefers-reduced-motion: reduce) {
    *, *:before, *:after { animation: none !important; transition: none !important; }
    .adorno { display: none; }
    .abierto:before { visibility: hidden; }
    .abierto .papel { transform: translateY(-53px); }
}
</style>
"""

st.html(
    css.replace("var(--a)", a)
       .replace("var(--b)", b)
       .replace("var(--t)", tinta)
)


# ── 3. ANIMACIONES Y NAVEGACIÓN ──────────────────────────────

def particulas(fiesta=False):
    rng = Random(40 + p)
    piezas = []

    for i in range(44 if fiesta else 14):
        color = rng.choice(["#c04271", "#8655bf", "#df9637", "#279995"])
        demora = rng.uniform(0, .9) if fiesta else -rng.uniform(0, 16)
        tiempo = rng.uniform(2, 3.8) if fiesta else rng.uniform(10, 17)
        simbolo = "" if fiesta else "♡✦✧"[i % 3]

        estilo = (
            f"--x:{rng.randrange(100)}%;"
            f"--size:{rng.randrange(12, 24)}px;"
            f"--delay:{demora:.2f}s;"
            f"--dur:{tiempo:.2f}s;"
            f"--c:{color}"
        )
        piezas.append(f'<i style="{estilo}">{simbolo}</i>')

    clase = "adorno fiesta" if fiesta else "adorno"
    st.html(
        f'<div class="{clase}" aria-hidden="true">'
        f'{"".join(piezas)}</div>'
    )


def nota(texto):
    st.html(f'<div class="nota">{escape(texto)}</div>')


def sobre(abierto=False):
    clase = "sobre abierto" if abierto else "sobre"
    st.html(
        f'<div class="{clase}" aria-hidden="true">'
        '<div class="papel">Para mi amor</div>'
        '<span class="sello">♥</span></div>'
    )


def ir(destino):
    s.pagina = destino


def seguir(texto):
    st.button(
        texto, on_click=ir, args=(p + 1,), use_container_width=True
    )


def foto(nombre):
    ruta = MEDIA / nombre
    if ruta.is_file():
        st.image(str(ruta), use_container_width=True)
    else:
        st.info(f"Tu foto va aquí · media/{nombre}")


def elegir(clave, opcion):
    s[clave] = opcion
    ir(p + 1)


def revelar(clave):
    s.abiertos = s.abiertos | {clave}


particulas()

if p >= 2:
    iconos = [
        "", "", "✧🎞✧", "✿♡✿", "✧♡✧",
        "♡✉♡", "✦🕯✦", "✧🎟✧", "✦♥✦",
    ]
    figuras = "".join(f"<span>{icono}</span>" for icono in iconos[p])
    st.html(f'<div class="escena" aria-hidden="true">{figuras}</div>')


# ── 4. EL RECORRIDO QUE VERÁ ELLA ────────────────────────────

if p == 0:
    st.title("Para mi amor")
    sobre()
    seguir("Abrir mi carta 💌")

elif p == 1:
    sobre(abierto=True)
    foto("nosotros.jpg")
    nota(CARTA)
    seguir("Mira lo que encontré →")

elif p == 2:
    st.title("Dale play, mi amor")
    video = MEDIA / "recuerdo.mp4"

    if video.is_file():
        st.video(str(video))
    else:
        st.info("Tu video va aquí · media/recuerdo.mp4")

    seguir("Ver nuestras fotos →")

elif p in (3, 4):
    nombre, titulo, frase = RECUERDOS[p - 3]
    st.title(titulo)
    foto(nombre)
    nota(frase)
    seguir("Una más →" if p == 3 else "Tengo una pregunta para ti →")

elif p in (5, 6):
    if p == 5:
        st.title("¿Salimos esta semana?")
        nota("Mi amor, esta vez tú eliges. ¿Qué te provoca?")
        clave = "semana"
        opciones = [
            "🍝 Ir a cenar",
            "🍿 Ir a cine",
            "🕯️ Una noche para los dos",
        ]
        st.caption(
            "Para la noche juntos pedimos algo rico, "
            "ponemos música y nos quedamos junticos."
        )
    else:
        st.title("¿Quién dijo que era una sola cita?")
        nota(
            "Quiero guardar otro día para ti, de aquí a fin de noviembre "
            "o en diciembre. ¿Qué te gustaría?"
        )
        clave = "especial"
        opciones = ["🥂 Una cena especial", "🎻 Un concierto Candlelight"]

    for opcion in opciones:
        st.button(
            opcion,
            on_click=elegir,
            args=(clave, opcion),
            use_container_width=True,
        )

elif p == 7:
    st.title("Nos debemos dos citas")

    with st.container(border=True):
        st.caption("ESTA SEMANA")
        st.subheader(s.semana)
        st.caption("FINALES DE NOVIEMBRE O DICIEMBRE")
        st.subheader(s.especial)

    st.caption("Mi amor, mándame una captura para saber qué escogiste 🤭")
    seguir("Antes de irte…")

else:
    st.title("¿Qué quieres saber primero?")

    for clave, etiqueta, mensaje in [
        ("razon", "❤️ Una razón por la que me gustas", RAZON),
        ("secreto", "🤫 Mi secreto turbio", SECRETO),
    ]:
        st.button(
            etiqueta,
            on_click=revelar,
            args=(clave,),
            use_container_width=True,
        )
        if clave in s.abiertos:
            nota(mensaje)

    if len(s.abiertos) == 2:
        particulas(fiesta=True)
        st.subheader("Una última cosita, mi amor")
        nota(DESPEDIDA)
        st.button("Volver a abrir mi carta", on_click=s.clear)

if p:
    st.button("← Volver", on_click=ir, args=(p - 1,))
