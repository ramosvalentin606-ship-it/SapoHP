from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Para mi amor", page_icon="💌", layout="centered")
MEDIA = Path(__file__).resolve().parent / "media"

# Personaliza aquí los textos que verá ella.
CARTA = """Mi amor, ya van cuatro meses y todavía me da una alegría toda boba cuando sé que te voy a ver. Me gusta poder contarte cualquier cosa y terminar riéndome contigo hasta de las bobadas que me pasan.

Me haces muy feliz. Estaba mirando unas fotos de nosotros y te quería mostrar algo. ❤️"""
RECUERDOS = [
    ("salida-1.jpg", "Volvería a ese día", "Si me dijeras que mañana podemos repetir esta salida, ya estaría listo para ir por ti."),
    ("salida-2.jpg", "Esta me la guardo", "Me gusta que ahora tenga lugares por los que paso y enseguida pienso en ti."),
]
RAZON = "Porque cuando me pasa algo, así sea la bobada más pequeña del día, ya estoy pensando en cómo te lo voy a contar. Me encanta que seas esa persona para mí."
SECRETO = "Lo tenía todo planeado… escogieras lo que escogieras, yo terminaba saliendo contigo dos veces. Perdón por semejante manipulación jajaja 🤭"
DESPEDIDA = "Felices cuatro meses, mi amor. La primera vez que te hice una página estaba pendiente de si me ibas a decir que sí. Hoy ya sé lo rico que es salir contigo y aquí estoy, inventándome otra para volver a invitarte. Qué ganas de verte. Te quiero muchísimo. ❤️"

s = st.session_state
s.setdefault("pagina", 0)
s.setdefault("abiertos", set())

def ir(pagina):
    s.pagina = pagina

def elegir(clave, opcion, pagina):
    s[clave] = opcion
    ir(pagina)

def seguir(texto):
    st.button(texto, type="primary", use_container_width=True,
              on_click=ir, args=(s.pagina + 1,))

def foto(nombre, descripcion):
    ruta = MEDIA / nombre
    if ruta.is_file():
        st.image(str(ruta), use_container_width=True)
    else:
        st.info(f"{descripcion} · Agrega media/{nombre}")

def abrir(clave):
    s.abiertos = s.abiertos | {clave}

st.markdown("""
<style>
.block-container{max-width:34rem;padding-top:3rem;padding-bottom:3rem}
h1,h2,h3{font-family:Georgia,serif!important;letter-spacing:-.035em}
div.stButton button{min-height:3rem;border-radius:1rem}
.env{position:relative;margin:3rem auto;width:min(260px,84%);height:153px;
background:#f5e4ca;border-radius:7px;isolation:isolate;box-shadow:0 12px 30px #542d3522;perspective:650px}
.env:before,.env:after{content:"";position:absolute;inset:0}
.env:before{background:#eacdaf;clip-path:polygon(0 0,50% 58%,100% 0);z-index:3;transform-origin:top}
.env:after{background:#f0d9bd;clip-path:polygon(0 0,50% 55%,100% 0,100% 100%,0 100%);z-index:2}
.seal{position:absolute;top:39%;left:44%;z-index:4;color:#953e57;font:32px Georgia}
.paper{position:absolute;inset:12px 14px;background:#fffcf5;border-radius:4px;text-align:center;padding:10px;color:#71394b;font:italic 21px Georgia}
.open:before{animation:flap .6s forwards}.open .paper{animation:rise .7s .5s both}.open .seal{opacity:0}
@keyframes flap{to{transform:rotateX(175deg);z-index:0}}
@keyframes rise{to{transform:translateY(-52px)}}
@media(prefers-reduced-motion:reduce){.open:before{display:none}.open .paper{animation:none;transform:translateY(-45px)}}
</style>
""", unsafe_allow_html=True)

def sobre(abierto=False):
    clase = "env open" if abierto else "env"
    st.markdown(f'<div class="{clase}" aria-hidden="true"><div class="paper">Para mi amor</div><span class="seal">♥</span></div>', unsafe_allow_html=True)

p = s.pagina
if p == 0:
    st.title("Para mi amor")
    sobre()
    seguir("Abrir mi carta 💌")
elif p == 1:
    sobre(True)
    foto("nosotros.jpg", "Foto de ustedes dos")
    st.write(CARTA)
    seguir("Mira lo que encontré →")
elif p == 2:
    st.title("Dale play, mi amor")
    video = MEDIA / "recuerdo.mp4"
    if video.is_file():
        st.video(str(video))
    else:
        st.info("Tu video va aquí · Agrega media/recuerdo.mp4")
    seguir("Ver nuestras fotos →")
elif p in (3, 4):
    nombre, titulo, frase = RECUERDOS[p - 3]
    st.title(titulo)
    foto(nombre, titulo)
    st.write(frase)
    seguir("Una más →" if p == 3 else "Tengo una pregunta para ti →")
elif p in (5, 6):
    if p == 5:
        st.title("¿Salimos esta semana?")
        st.write("Mi amor, esta vez tú eliges. ¿Qué te provoca?")
        clave = "semana"
        opciones = ["🍝 Ir a cenar", "🍿 Ir a cine", "🕯️ Una noche para los dos"]
        st.caption("Para la noche juntos pedimos algo rico, ponemos música y nos quedamos junticos.")
    else:
        st.title("¿Quién dijo que era una sola cita? 💌")
        st.write("Quiero guardar otro día para ti, de aquí a fin de noviembre o en diciembre. ¿Qué te gustaría?")
        clave = "especial"
        opciones = ["🥂 Una cena especial", "🎻 Un concierto Candlelight"]
    for opcion in opciones:
        st.button(opcion, use_container_width=True, on_click=elegir, args=(clave, opcion, p + 1))
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
    for clave, etiqueta, mensaje in [("razon", "❤️ Una razón por la que me gustas", RAZON),
                                     ("secreto", "🤫 Mi secreto turbio", SECRETO)]:
        st.button(etiqueta, use_container_width=True, on_click=abrir, args=(clave,))
        if clave in s.abiertos:
            st.write(mensaje)
    if len(s.abiertos) == 2:
        st.divider()
        st.subheader("Una última cosita, mi amor")
        st.write(DESPEDIDA)
        st.button("Volver a abrir mi carta", on_click=s.clear)
if 1 <= p <= 8:
    st.button("← Volver", on_click=ir, args=(p - 1,))
