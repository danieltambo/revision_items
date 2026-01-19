import streamlit as st
from helpers.html_loader import load_html
from event_logger import event_logger
from pathlib import Path


# =============================
# CONFIGURACIÓN
# =============================
DEV = False  # ← pon True solo para desarrollo interno

st.set_page_config(layout="wide")

# st.title("📬 Banco de Ítems – Visualización ")


# =============================
# CARGA DE ÍTEMS
# =============================
ITEMS_DIR = Path("./")

item_files = sorted([
    f.stem for f in ITEMS_DIR.glob("*.html")
])

if not item_files:
    st.stop()


# =============================
# OBTENER item_id DESDE URL
# =============================
query_item_id = st.query_params.get("item_id")

# Si NO estamos en DEV y:
# - no hay item_id
# - o no es válido
# → página en blanco
if not DEV:
    if not query_item_id or query_item_id not in item_files:
        st.stop()


# =============================
# SELECCIÓN DE ÍTEM (solo DEV)
# =============================
if DEV:
    item_id = st.selectbox(
        "Selector de ítems (DEV)",
        item_files,
        index=item_files.index(query_item_id) if query_item_id in item_files else 0
    )
else:
    item_id = query_item_id

# =============================
# TÍTULO
# =============================
st.title(item_id)

# =============================
# RENDER DEL ÍTEM
# =============================
html = load_html(ITEMS_DIR / f"{item_id}.html")
html = html + "<br>"  # workaround iframe

evento= event_logger(
    key=f"item_{item_id}",
    html=html,
)


# Es una prueba para ver si llega
# st.write("EVENT RAW:", evento)
