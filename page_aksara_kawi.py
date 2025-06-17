# page_aksara_kawi.py
import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = "http://34.34.221.164:3040/kebonkawiII/sparql"
NAMED_GRAPH_URI = "http://contoh.org/graph/prasasti_kawi"

if "hasil_input_aksara" not in st.session_state:
    st.session_state.hasil_input_aksara = ""

st.markdown("""
<style>
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
    h3 { margin-top: 30px !important; margin-bottom: 15px !important; }
    [data-testid="stSidebar"] textarea {
        font-family: 'Noto Sans Javanese', sans-serif !important;
        font-size: 28px !important;
        line-height: 1.5 !important;
        height: 200px !important;
    }
</style>
""", unsafe_allow_html=True)

keyboard_data = [
    {"kategori": "Vokal Mandiri", "karakter": [
        {"label": "ꦄ", "latin": "a"}, {"label": "ꦆ", "latin": "i"}, {"label": "ꦈ", "latin": "u"},
        {"label": "ꦌ", "latin": "e"}, {"label": "ꦎ", "latin": "o"}
    ]},
    {"kategori": "Aksara Dasar", "karakter": [
        {"label": "ꦲ", "latin": "ha"}, {"label": "ꦤ", "latin": "na"}, {"label": "ꦕ", "latin": "ca"},
        {"label": "ꦗ", "latin": "ja"}, {"label": "ꦫ", "latin": "ra"}, {"label": "ꦏ", "latin": "ka"},
        {"label": "ꦢ", "latin": "da"}, {"label": "ꦠ", "latin": "ta"}, {"label": "ꦱ", "latin": "sa"},
        {"label": "ꦭ", "latin": "la"}, {"label": "ꦪ", "latin": "ya"}, {"label": "ꦡ", "latin": "dha"},
        {"label": "ꦣ", "latin": "tha"}, {"label": "ꦚ", "latin": "nya"}, {"label": "ꦖ", "latin": "ga"},
        {"label": "ꦥ", "latin": "pa"}, {"label": "ꦧ", "latin": "ba"}, {"label": "ꦔ", "latin": "nga"},
        {"label": "ꦨ", "latin": "ma"}, {"label": "ꦮ", "latin": "wa"}, {"label": "ꦯ", "latin": "sha"}
    ]}
]

def perform_sparql_query(search_term):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
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
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        return sparql.query().convert()
    except Exception as e:
        st.error(f"SPARQL query gagal: {e}")
        return None

def app():
    st.title("⌨️ Keyboard Aksara Kawi")
    st.markdown("---")

    with st.sidebar:
        st.header("📝 Aksara Kawi Anda")
        st.text_area("Teks Aksara:",
                     value=st.session_state.hasil_input_aksara,
                     height=200,
                     key="aksara_sidebar_output_text_area",
                     label_visibility="collapsed")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Hapus Terakhir"):
                st.session_state.hasil_input_aksara = st.session_state.hasil_input_aksara[:-1]
                st.rerun()
        with col2:
            if st.button("🗑️ Hapus Semua"):
                st.session_state.hasil_input_aksara = ""
                st.rerun()

        st.markdown("---")
        st.subheader("🔮 Tempel Aksara Cepat")
        if st.button("Tempel 'ꦄꦱ꧀ꦠꦸ' (astu)"):
            st.session_state.hasil_input_aksara += "ꦄꦱ꧀ꦠꦸ"
        if st.button("Tempel 'ꦱꦶꦢ꧀ꦝꦩ꧀' (siddham)"):
            st.session_state.hasil_input_aksara += "ꦱꦶꦢ꧀ꦝꦩ꧀"
        if st.button("Tempel 'ꦥꦔꦏ꧀ꦱꦩꦤꦶꦔ꧀' (pangaksamaning)"):
            st.session_state.hasil_input_aksara += "ꦥꦔꦏ꧀ꦱꦩꦤꦶꦔ꧀"

        st.markdown("---")
        st.subheader("🔍 Hasil Pencarian Aksara Kawi")
        if st.button("🚀 Cari Aksara Kawi di Database"):
            if st.session_state.hasil_input_aksara.strip() == "":
                st.warning("Masukkan Aksara Kawi terlebih dahulu.")
            else:
                results = perform_sparql_query(st.session_state.hasil_input_aksara)
                if results:
                    bindings = results["results"]["bindings"]
                    if bindings:
                        for row in bindings:
                            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                            st.markdown("<span class='result-label'>Transliterasi Latin:</span>", unsafe_allow_html=True)
                            st.markdown(f"<span class='result-value'>{row['latin']['value']}</span>", unsafe_allow_html=True)
                            st.markdown("<span class='result-label'>Arti Bahasa Indonesia:</span>", unsafe_allow_html=True)
                            st.markdown(f"<span class='result-value arti'>{row['arti']['value']}</span>", unsafe_allow_html=True)
                            st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error("Data tidak ditemukan.")
                else:
                    st.error("Gagal mengambil hasil dari server.")

    st.markdown("---")
    st.header("Ketik Aksara Kawi untuk Mencari")

    for data in keyboard_data:
        st.subheader(f"✨ {data['kategori']}")
        cols = st.columns(10)
        for i, item in enumerate(data["karakter"]):
            if st.button(item["label"], key=f"btn-{item['label']}"):
                st.session_state.hasil_input_aksara += item["label"]
                st.rerun()
            with cols[i % 10]:
                st.markdown(f"<p style='text-align:center; color:#aaa'>{item['latin']}</p>", unsafe_allow_html=True)