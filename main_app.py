# main_app.py
import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Pencarian Aksara Kawi (Semantic Web)",
    page_icon="📜",
    layout="wide"
)

# --- Inject Global CSS ---
st.markdown("""
    <style>
        body {
            font-family: 'Noto Sans Javanese', sans-serif;
        }
        .stButton > button {
            font-size: 58px !important;
            padding: 25px 10px !important;
            width: 100% !important;
            height: auto !important;
            line-height: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 8px;
            border: 1px solid #444;
            background-color: #262730;
            color: #ffffff;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #383a48;
            border-color: #666;
            transform: translateY(-2px);
        }
        .stButton > button + p {
            font-size: 1.2em !important;
            text-align: center;
            color: #a0a0a0;
            margin-top: 5px;
        }
        h3 {
            margin-top: 30px !important;
            margin-bottom: 15px !important;
        }
        [data-testid="stSidebar"] textarea {
            font-family: 'Noto Sans Javanese', sans-serif !important;
            font-size: 28px !important;
            line-height: 1.5 !important;
            height: 200px !important;
        }
        .stAlert {
            padding: 1rem 1.25rem;
            border-radius: 0.5rem;
            font-size: 1.1em;
            font-weight: bold;
        }
        .stAlert.success { background-color: #1a5e2c; color: #e6ffe6; border-color: #0d381c; }
        .stAlert.error { background-color: #8c1e21; color: #ffe6e6; border-color: #4a0d0e; }
        .stAlert.warning { background-color: #806800; color: #fffacd; border-color: #ffeeba; }
        .result-box {
            background-color: #33363e;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            border: 1px solid #555;
        }
        .result-label {
            font-weight: bold;
            color: #f0f2f6;
            font-size: 1.1em;
            margin-bottom: 5px;
            display: block;
        }
        .result-value {
            font-family: 'monospace';
            font-size: 1.3em;
            font-weight: bold;
            color: #00ff99;
            background-color: #1a1c22;
            padding: 5px 10px;
            border-radius: 5px;
            display: inline-block;
            word-wrap: break-word;
            white-space: normal;
        }
        .result-value.arti {
            font-family: 'sans-serif';
            font-size: 1.2em;
            color: #87ceeb;
        }
    </style>
    """, unsafe_allow_html=True)

# --- SPARQL endpoint configuration ---
SPARQL_ENDPOINT = "http://34.34.221.164:3040/kebonkawiII/sparql"
NAMED_GRAPH_URI = "http://contoh.org/graph/prasasti_kawi"

# --- Session state ---
if "hasil_input" not in st.session_state:
    st.session_state.hasil_input = ""
if "search_history" not in st.session_state:
    st.session_state.search_history = []

# --- SPARQL query execution ---
@st.cache_data(ttl=3600)
def perform_sparql_query(query_type, search_term):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    
    if query_type == "aksara":
        query = f"""
            PREFIX : <http://contoh.org/prasasti#>
            SELECT ?aksaraValue ?latin ?arti
            FROM <{NAMED_GRAPH_URI}>
            WHERE {{
                ?a a :AksaraKawi ;
                    :aksaraValue "{search_term}" ;
                    :hasTransliterasi ?l ;
                    :hasArti ?r .
                ?l :valueLatin ?latin .
                ?r :valueArti ?arti .
            }}
        """
    elif query_type == "latin":
        query = f"""
            PREFIX : <http://contoh.org/prasasti#>
            SELECT ?aksaraValue ?latin ?arti
            FROM <{NAMED_GRAPH_URI}>
            WHERE {{
                ?a a :AksaraKawi ;
                    :aksaraValue ?aksaraValue ;
                    :hasTransliterasi ?l ;
                    :hasArti ?r .
                ?l :valueLatin ?latin .
                ?r :valueArti ?arti .
                FILTER regex(?latin, "{search_term}", "i")
            }}
        """
    elif query_type == "arti":
        query = f"""
            PREFIX : <http://contoh.org/prasasti#>
            SELECT ?aksaraValue ?latin ?arti
            FROM <{NAMED_GRAPH_URI}>
            WHERE {{
                ?a a :AksaraKawi ;
                    :aksaraValue ?aksaraValue ;
                    :hasTransliterasi ?l ;
                    :hasArti ?r .
                ?l :valueLatin ?latin .
                ?r :valueArti ?arti .
                FILTER regex(?arti, "{search_term}", "i")
            }}
        """
    else:
        return None

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        return sparql.query().convert()
    except Exception as e:
        st.error(f"Koneksi ke SPARQL endpoint gagal: {e}")
        return None

# --- Import halaman ---
import page_aksara_kawi
import page_latin
import page_arti

# --- Homepage ---
st.title("📜 Aplikasi Pencarian Aksara Kawi")
st.markdown("---")
st.header("Pilih Jenis Pencarian:")

pilihan_pencarian = st.selectbox(
    "Pilih metode pencarian Anda:",
    [
        "Homepage",
        "Cari Berdasarkan Aksara Kawi",
        "Cari Berdasarkan Transliterasi Latin",
        "Cari Berdasarkan Arti Bahasa Indonesia"
    ]
)

if pilihan_pencarian == "Homepage":
    st.info("Selamat datang! Silakan pilih metode pencarian dari dropdown di atas.")

elif pilihan_pencarian == "Cari Berdasarkan Aksara Kawi":
    page_aksara_kawi.app()

elif pilihan_pencarian == "Cari Berdasarkan Transliterasi Latin":
    page_latin.app()

elif pilihan_pencarian == "Cari Berdasarkan Arti Bahasa Indonesia":
    page_arti.app()

st.markdown("---")
