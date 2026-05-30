import streamlit as st

# Configuración móvil
st.set_page_config(page_title="Álbum Mundial 2026", page_icon="⚽", layout="centered")

st.title("⚽ Mi Álbum Interactivo")
st.write("¡Agregá figuritas nuevas y registrá lo que vas pegando en el momento!")

# 1. BASE DE DATOS INICIAL
@st.cache_data
def inicializar_datos():
    paginas = {
        "Coca-Cola": ["CC7", "CC10", "CC11", "CC12", "CC13"],
        "FIFA History": ["FWC13", "FWC19"],
        "ALG": [f"ALG{i}" for i in range(1, 21)], "ARG": [f"ARG{i}" for i in range(1, 21)],
        "AUS": [f"AUS{i}" for i in range(1, 21)], "AUT": [f"AUT{i}" for i in range(1, 21)],
        "BHN": [f"BHN{i}" for i in range(1, 21)], "BIH": [f"BIH{i}" for i in range(1, 21)],
        "BRA": [f"BRA{i}" for i in range(1, 21)], "CAN": [f"CAN{i}" for i in range(1, 21)],
        "CIV": [f"CIV{i}" for i in range(1, 21)], "COD": [f"COD{i}" for i in range(1, 21)],
        "COL": [f"COL{i}" for i in range(1, 21)], "CRO": [f"CRO{i}" for i in range(1, 21)],
        "CUW": [f"CUW{i}" for i in range(1, 21)], "CZE": [f"CZE{i}" for i in range(1, 21)],
        "EGY": [f"EGY{i}" for i in range(1, 21)], "ENG": [f"ENG{i}" for i in range(1, 21)],
        "ESP": [f"ESP{i}" for i in range(1, 21)], "FIN": [f"FIN{i}" for i in range(1, 21)],
        "FRA": [f"FRA{i}" for i in range(1, 21)], "FWC": [f"FWC{i}" for i in range(1, 21)],
        "GHA": [f"GHA{i}" for i in range(1, 21)], "GPV": [f"GPV{i}" for i in range(1, 21)],
        "HAI": [f"HAI{i}" for i in range(1, 21)], "IRQ": [f"IRQ{i}" for i in range(1, 21)],
        "JOR": [f"JOR{i}" for i in range(1, 21)], "JPN": [f"JPN{i}" for i in range(1, 21)],
        "KOR": [f"KOR{i}" for i in range(1, 21)], "MAR": [f"MAR{i}" for i in range(1, 21)],
        "MEX": [f"MEX{i}" for i in range(1, 21)], "NED": [f"NED{i}" for i in range(1, 21)],
        "NOR": [f"NOR{i}" for i in range(1, 21)], "NZL": [f"NZL{i}" for i in range(1, 21)],
        "PAN": [f"PAN{i}" for i in range(1, 21)], "PAR": [f"PAR{i}" for i in range(1, 21)],
        "POR": [f"POR{i}" for i in range(1, 21)], "QAT": [f"QAT{i}" for i in range(1, 21)],
        "RSA": [f"RSA{i}" for i in range(1, 21)], "SCO": [f"SCO{i}" for i in range(1, 21)],
        "SEN": [f"SEN{i}" for i in range(1, 21)], "SUI": [f"SUI{i}" for i in range(1, 21)],
        "SWE": [f"SWE{i}" for i in range(1, 21)], "TUN": [f"TUN{i}" for i in range(1, 21)],
        "TUR": [f"TUR{i}" for i in range(1, 21)], "USA": [f"USA{i}" for i in range(1, 21)],
        "UZB": [f"UZB{i}" for i in range(1, 21)],
    }
    
    faltantes = {
        "Coca-Cola": ["CC7", "CC10", "CC11", "CC12", "CC13"], "FIFA History": ["FWC13", "FWC19"],
        "PAN": ["PAN1", "PAN2", "PAN3", "PAN6", "PAN7", "PAN9", "PAN15", "PAN19"],
        "CRO": ["CRO5", "CRO6", "CRO8", "CRO10", "CRO12", "CRO15", "CRO16", "CRO17", "CRO18", "CRO19", "CRO20"],
        "GHA": ["GHA1", "GHA8", "GHA11", "GHA12", "GHA14", "GHA15", "GHA16", "GHA17", "GHA18"],
        "ENG": ["ENG1", "ENG2", "ENG5", "ENG8", "ENG9", "ENG10", "ENG14", "ENG15", "ENG19"],
        "UZB": ["UZB1", "UZB8", "UZB10", "UZB14", "UZB16", "UZB18"], "COL": ["COL1", "COL4", "COL8", "COL12", "COL16", "COL17", "COL18"],
        "COD": ["COD7", "COD8", "COD13"], "POR": ["POR1", "POR2", "POR7", "POR13", "POR14", "POR15", "POR19", "POR20"],
        "JOR": ["JOR1", "JOR2", "JOR3", "JOR6", "JOR7", "JOR10", "JOR11", "JOR15", "JOR16", "JOR18", "JOR19"],
        "AUT": ["AUT1", "AUT2", "AUT5", "AUT6", "AUT7", "AUT10", "AUT16", "AUT18", "AUT20"],
        "ARG": ["ARG1", "ARG3", "ARG4", "ARG7", "ARG8", "ARG16", "ARG19", "ARG20"],
        "ALG": ["ALG2", "ALG4", "ALG5", "ALG6", "ALG9", "ALG10", "ALG12", "ALG13", "ALG14", "ALG15", "ALG18"],
        "NOR": ["NOR1", "NOR2", "NOR3", "NOR4", "NOR6", "NOR7", "NOR8", "NOR9", "NOR11", "NOR12", "NOR14", "NOR15", "NOR16", "NOR17", "NOR18", "NOR19", "NOR20"],
        "IRQ": ["IRQ1", "IRQ2", "IRQ4", "IRQ6", "IRQ12", "IRQ17", "IRQ18"], "SEN": ["SEN2", "SEN4", "SEN8", "SEN12", "SEN13", "SEN14", "SEN16"],
        "FRA": ["FRA4", "FRA9", "FRA11", "FRA16", "FRA20"], "MAR": ["MAR1", "MAR2", "MAR8", "MAR10", "MAR12", "MAR16", "MAR19"],
        "SWE": ["SWE1", "SWE2", "SWE3", "SWE4", "SWE5", "SWE7", "SWE8", "SWE9", "SWE10", "SWE11", "SWE13", "SWE14", "SWE15", "SWE16", "SWE18", "SWE19", "SWE20"],
        "CZE": ["CZE5", "CZE6", "CZE8", "CZE11", "CZE14", "CZE16"],
        "EGY": ["EGY1", "EGY2", "EGY3", "EGY4", "EGY5", "EGY6", "EGY7", "EGY8", "EGY9", "EGY10", "EGY11", "EGY12", "EGY14", "EGY15", "EGY16", "EGY17", "EGY18", "EGY19", "EGY20"],
        "TUR": ["TUR6", "TUR10", "TUR14", "TUR19"],
        "TUN": ["TUN1", "TUN2", "TUN3", "TUN4", "TUN5", "TUN6", "TUN7", "TUN8", "TUN9", "TUN11", "TUN12", "TUN13", "TUN15", "TUN16", "TUN17", "TUN18", "TUN19", "TUN20"],
        "BHN": ["BHN1", "BHN2", "BHN3", "BHN4", "BHN6", "BHN7", "BHN8", "BHN9", "BHN10", "BHN11", "BHN12", "BHN13", "BHN14", "BHN15", "BHN16", "BHN17", "BHN18", "BHN19", "BHN20"],
        "GPV": ["GPV1", "GPV2", "GPV3", "GPV4", "GPV5", "GPV6", "GPV7", "GPV9", "GPV10", "GPV11", "GPV12", "GPV13", "GPV14", "GPV15", "GPV16", "GPV17", "GPV18", "GPV19", "GPV20"],
        "CIV": ["CIV3", "CIV10", "CIV11", "CIV12", "CIV13", "CIV15", "CIV18", "CIV19", "CIV20"],
        "JPN": ["JPN1", "JPN2", "JPN3", "JPN5", "JPN6", "JPN7", "JPN8", "JPN10", "JPN11", "JPN12", "JPN13", "JPN15", "JPN16", "JPN17", "JPN18", "JPN19", "JPN20"],
        "NED": ["NED1", "NED3", "NED7", "NED14", "NED16", "NED17", "NED18", "NED19"],
        "ECU": ["ECU2", "ECU4", "ECU7", "ECU8", "ECU9", "ECU11", "ECU12", "ECU13", "ECU14", "ECU16", "ECU17", "ECU20"],
        "CUW": ["CUW1", "CUW3", "CUW5", "CUW7", "CUW9", "CUW10", "CUW13", "CUW16", "CUW19", "CUW20"],
        "GER": ["GER1", "GER2", "GER5", "GER6", "GER7", "GER8", "GER9", "GER10", "GER11", "GER12", "GER13", "GER16", "GER18", "GER19"],
        "AUS": ["AUS1", "AUS2", "AUS3", "AUS4", "AUS5", "AUS7", "AUS8", "AUS12", "AUS14", "AUS17"],
        "PAR": ["PAR4", "PAR6", "PAR7", "PAR10", "PAR11", "PAR14", "PAR17", "PAR18", "PAR19"],
        "MEX": ["MEX2", "MEX3", "MEX5", "MEX6", "MEX7", "MEX9", "MEX10", "MEX11", "MEX12", "MEX13", "MEX20"],
        "RSA": ["RSA3", "RSA4", "RSA6", "RSA9", "RSA10", "RSA12", "RSA14", "RSA17", "RSA18"],
        "KOR": ["KOR1", "KOR2", "KOR4", "KOR5", "KOR6", "KOR7", "KOR8", "KOR12", "KOR14", "KOR17", "KOR19"],
        "CAN": ["CAN2", "CAN4", "CAN5", "CAN6", "CAN8", "CAN9", "CAN13", "CAN14", "CAN15", "CAN17", "CAN19"],
        "BIH": ["BIH2", "BIH3", "BIH4", "BIH8", "BIH9", "BIH12", "BIH14", "BIH16", "BIH19", "BIH20"],
        "QAT": ["QAT4", "QAT5", "QAT8", "QAT9", "QAT10", "QAT11", "QAT13", "QAT15", "QAT19", "QAT20"],
        "SUI": ["SUI2", "SUI6", "SUI8", "SUI10", "SUI11", "SUI15", "SUI16"],
        "BRA": ["BRA1", "BRA2", "BRA3", "BRA4", "BRA8", "BRA10", "BRA11", "BRA12", "BRA15", "BRA16", "BRA17", "BRA20"],
        "HAI": ["HAI2", "HAI6", "HAI7", "HAI8", "HAI11", "HAI16", "HAI18", "HAI20"],
        "SCO": ["SCO2", "SCO4", "SCO8", "SCO9", "SCO10", "SCO11", "SCO13", "SCO14", "SCO15", "SCO16", "SCO17", "SCO19", "SCO20"],
        "USA": ["USA2", "USA5", "USA14", "USA15"]
    }
    
    repetidas = {
        "ALG": {"3": 1, "7": 1}, "ARG": {"13": 1}, "BHN": {"5": 1}, "BRA": {"18": 2}, 
        "CAN": {}, "CIV": {"9": 1}, "COL": {"2": 1, "13": 1, "20": 1}, 
        "COD": {"1": 1, "2": 1, "3": 1, "5": 1, "6": 1, "10": 1, "15": 1, "19": 1, "20": 1}, 
        "CRO": {"7": 1, "13": 1}, "CUW": {"18": 1}, "CZE": {"3": 1, "4": 1, "12": 1, "17": 1, "20": 1}, 
        "EGY": {"13": 1}, "ESP": {"7": 1, "14": 1}, "FIN": {"8": 1}, "FRA": {"1": 1, "13": 1, "15": 1}, 
        "FWC": {"5": 1, "11": 1, "16": 1, "18": 1}, "GPV": {"8": 1}, "IRQ": {"15": 1, "16": 1, "19": 1}, 
        "JOR": {"5": 1}, "JPN": {"14": 1}, "KOR": {"10": 1, "11": 1}, 
        "MAR": {"3": 1, "6": 1, "7": 1, "9": 1, "11": 1, "13": 1}, "MEX": {"17": 1}, 
        "NED": {"2": 1, "6": 1, "10": 1, "15": 1}, "NOR": {}, "NZL": {"2": 1, "7": 1}, 
        "PAN": {"4": 1, "8": 1, "11": 1, "13": 1, "14": 1, "18": 1}, "PAR": {"3": 1, "13": 1}, 
        "POR": {"4": 1}, "QAT": {"6": 1}, "RSA": {"1": 1, "5": 1}, "SEN": {"7": 1}, 
        "SWE": {"6": 1, "12": 1, "17": 1}, "TUN": {"10": 2, "14": 1}, "TUR": {"3": 1, "5": 1, "16": 1}, 
        "USA": {"3": 1, "4": 1, "7": 1, "11": 1, "12": 2, "17": 1}, "UZB": {"3": 1, "9": 1, "15": 1, "19": 1}
    }
    return paginas, faltantes, repetidas

paginas, f_ini, r_ini = inicializar_datos()

if "faltantes" not in st.session_state:
    st.session_state.faltantes = f_ini
if "repetidas" not in st.session_state:
    st.session_state.repetidas = r_ini

# 2. PESTAÑAS PRINCIPALES
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Buscador", "➕ Cargar Nuevas", "📋 Faltantes", "🔄 Repetidas"])

with tab1:
    st.subheader("Consultar Figu")
    busqueda = st.text_input("Ingresá el código entero (Ej: ARG13):").strip().upper()
    if busqueda:
        import re
        m = re.match(r"([A-ZáéíóúÁÉÍÓÚ\s\-]+)(\d+)", busqueda)
        if m:
            p, n = m.groups()
            if "COCA" in p: p = "Coca-Cola"
            if "HISTORY" in p: p = "FIFA History"
            
            if p in paginas:
                if busqueda in st.session_state.faltantes.get(p, []):
                    st.error(f"🚨 ¡FALTA! La {busqueda} se necesita en el álbum.")
                else:
                    cant = st.session_state.repetidas.get(p, {}).get(n, 0)
                    st.success(f"✅ YA ESTÁ PEGADA. (Repetidas disponibles: {cant})")
            else:
                st.warning("Esa selección no existe.")
        else:
            st.warning("Escribí letras y números juntos (Ej: USA4).")

with tab2:
    st.subheader("¡Sumar figuritas nuevas!")
    col1, col2 = st.columns(2)
    with col1:
        pais_n = st.selectbox("Selección:", list(paginas.keys()))
    with col2:
        # Extraer solo el número para el casillero visual
        num_n = st.number_input("Número de figu:", min_value=1, max_value=20, value=1)
    
    # Crear código exacto
    if pais_n == "Coca-Cola": code_n = f"CC{num_n}"
    elif pais_n == "FIFA History": code_n = f"FWC{num_n}"
    else: code_n = f"{pais_n}{num_n}"
    
    st.write(f"Seleccionaste la figurita: **{code_n}**")
    
    btn_pegar, btn_repe = st.columns(2)
    
    with btn_pegar:
        if st.button("📌 ¡La pegamos en el álbum!"):
            if code_n in st.session_state.faltantes.get(pais_n, []):
                st.session_state.faltantes[pais_n].remove(code_n)
                st.toast(f"¡Buenísimo! {code_n} registrada como pegada.", icon="🎉")
            else:
                st.toast(f"Esa ya estaba pegada, ¡pero gracias por chequear!", icon="👀")
                
    with btn_repe:
        if st.button("🔄 Guardar como repetida"):
            str_num = str(num_n)
            if pais_n not in st.session_state.repetidas:
                st.session_state.repetidas[pais_n] = {}
            st.session_state.repetidas[pais_n][str_num] = st.session_state.repetidas[pais_n].get(str_num, 0) + 1
            st.toast(f"¡Agregada {code_n} a la pila de cambios!", icon="🔄")

with tab3:
    st.subheader("Lista de Faltantes")
    pais_f = st.selectbox("Elegí el país:", list(paginas.keys()), key="p_f")
    lista_f = st.session_state.faltantes.get(pais_f, [])
    if lista_f:
        st.write(f"Faltan **{len(lista_f)}** figuritas:")
        st.code(", ".join(lista_f))
    else:
        st.success("¡Página llena! 🏆")

with tab4:
    st.subheader("Tus Repetidas")
    pais_r = st.selectbox("Elegí el país:", list(paginas.keys()), key="p_r")
    dict_r = st.session_state.repetidas.get(pais_r, {})
    repes_activas = {k: v for k, v in dict_r.items() if v > 0}
    
    if repes_activas:
        for num, cant in repes_activas.items():
            st.write(f"• **{pais_r} {num}** — Cantidad: {cant}")
    else:
        st.write("Sin repetidas por acá.")
