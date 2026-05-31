import streamlit as st
import re

# Configuración móvil con estilo oscuro/deportivo
st.set_page_config(page_title="Álbum Mundial 2026", page_icon="⚽", layout="centered")

# Estilo visual personalizado
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        border-radius: 8px; font-weight: bold; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ Mi Álbum Interactivo 2026")

# 1. BASE DE DATOS INICIAL CON EMÓJIS (ACTUALIZADA CON LAS PÁGINAS COMPLETAS DE LAS FOTOS)
@st.cache_data
def inicializar_datos():
    nombres_paises = {
        "Coca-Cola": "🥤 Coca-Cola", "FIFA History": "📜 FIFA History",
        "ALG": "🇩🇿 ALG (Argelia)", "ARG": "🇦🇷 ARG (Argentina)", "AUS": "🇦🇺 AUS (Australia)", "AUT": "🇦🇹 AUT (Austria)",
        "BHN": "🇧🇭 BHN (Bahréin)", "BIH": "🇧🇦 BIH (Bosnia)", "BRA": "🇧🇷 BRA (Brasil)", "CAN": "🇨🇦 CAN (Canadá)",
        "CIV": "🇨🇮 CIV (Costa de Marfil)", "COD": "🇨🇩 COD (Congo DR)", "COL": "🇨🇴 COL (Colombia)", "CRO": "🇭🇷 CRO (Croacia)",
        "CUW": "🇨🇼 CUW (Curazao)", "CZE": "🇨🇿 CZE (Rep. Checa)", "EGY": "🇪🇬 EGY (Egipto)", "ENG": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG (Inglaterra)",
        "ESP": "🇪🇸 ESP (España)", "FIN": "🇫🇮 FIN (Finlandia)", "FRA": "🇫🇷 FRA (Francia)", "FWC": "🏆 FWC (Especiales)",
        "GHA": "🇬🇭 GHA (Ghana)", "GPV": "🇨🇻 GPV (Cabo Verde)", "HAI": "🇭🇹 HAI (Haití)", "IRQ": "🇮🇶 IRQ (Irak)",
        "IRN": "🇮🇷 IRN (Irán)", "JOR": "🇯🇴 JOR (Jordania)", "JPN": "🇯🇵 JPN (Japón)", "KOR": "🇰🇷 KOR (Corea del Sur)", 
        "MAR": "🇲🇦 MAR (Marruecos)", "MEX": "🇲🇽 MEX (México)", "NED": "🇳🇱 NED (Países Bajos)", "NOR": "🇳🇴 NOR (Noruega)", 
        "NZL": "🇳🇿 NZL (Nueva Zelanda)", "PAN": "🇵🇦 PAN (Panamá)", "PAR": "🇵🇾 PAR (Paraguay)", "POR": "🇵🇹 POR (Portugal)", 
        "QAT": "🇶🇦 QAT (Catar)", "RSA": "🇿🇦 RSA (Sudáfrica)", "SCO": "🏴󠁧󠁢󠁳󠁣󠁴󠁿 SCO (Escocia)", "SEN": "🇸🇳 SEN (Senegal)", 
        "SUI": "🇨🇭 SUI (Suiza)", "SWE": "🇸🇪 SWE (Suecia)", "TUN": "🇹🇳 TUN (Túnez)", "TUR": "🇹🇷 TUR (Turquía)", 
        "USA": "🇺🇸 USA (EE.UU.)", "UZB": "🇺🇿 UZB (Uzbekistán)", "URU": "🇺🇾 URU (Uruguay)", "BEL": "🇧🇪 BEL (Bélgica)",
        "ECU": "🇪🇨 ECU (Ecuador)", "GER": "🇩🇪 GER (Alemania)", "KSA": "🇸🇦 KSA (Arabia Saudita)"
    }
    
    paginas = {p: [f"CC{i}" if p=="Coca-Cola" else f"FWC{i}" if p=="FIFA History" else f"{p}{i}" for i in range(1, 21)] for p in nombres_paises.keys()}
    paginas["Coca-Cola"] = ["CC7", "CC10", "CC11", "CC12", "CC13"]
    paginas["FIFA History"] = ["FWC13", "FWC19"]

    # Faltantes reales leídas minuciosamente de las fotos paso a paso
    faltantes = {
        "Coca-Cola": ["CC7", "CC10", "CC11", "CC12", "CC13"], 
        "FIFA History": ["FWC13", "FWC19"],
        "ALG": ["ALG2", "ALG4", "ALG5", "ALG6", "ALG9", "ALG10", "ALG12", "ALG13", "ALG14", "ALG15", "ALG18"],
        "ARG": ["ARG1", "ARG3", "ARG4", "ARG7", "ARG8", "ARG16", "ARG19", "ARG20"],
        "AUS": ["AUS1", "AUS2", "AUS3", "AUS4", "AUS5", "AUS7", "AUS8", "AUS12", "AUS14", "AUS17"],
        "AUT": ["AUT1", "AUT2", "AUT5", "AUT6", "AUT7", "AUT10", "AUT16", "AUT18", "AUT20"],
        "BHN": ["BHN1", "BHN2", "BHN3", "BHN4", "BHN6", "BHN7", "BHN8", "BHN9", "BHN10", "BHN11", "BHN12", "BHN13", "BHN14", "BHN15", "BHN16", "BHN17", "BHN18", "BHN19", "BHN20"],
        "BIH": ["BIH2", "BIH3", "BIH4", "BIH8", "BIH9", "BIH12", "BIH14", "BIH16", "BIH19", "BIH20"],
        "BRA": ["BRA1", "BRA2", "BRA3", "BRA4", "BRA8", "BRA10", "BRA11", "BRA12", "BRA15", "BRA16", "BRA17", "BRA20"],
        "CAN": ["CAN2", "CAN4", "CAN5", "CAN6", "CAN8", "CAN9", "CAN13", "CAN14", "CAN15", "CAN17", "CAN19"],
        
        # --- CARGAS NUEVAS DETECTADAS EN LAS FOTOS ---
        "ESP": ["ESP2", "ESP3", "ESP4", "ESP5", "ESP6", "ESP8", "ESP9", "ESP10", "ESP12", "ESP13", "ESP17", "ESP18", "ESP20"],
        "URU": ["URU1", "URU2", "URU3", "URU4", "URU5", "URU7", "URU8", "URU9", "URU10", "URU11", "URU15", "URU20"],
        "GPV": ["GPV1", "GPV3", "GPV4", "GPV7", "GPV8", "GPV13", "GPV16", "GPV18", "GPV19"],
        "IRN": ["IRN2", "IRN4", "IRN6", "IRN10", "IRN11", "IRN12", "IRN14", "IRN15", "IRN16", "IRN17", "IRN18", "IRN19", "IRN20"],
        "BEL": ["BEL1", "BEL3", "BEL4", "BEL5", "BEL7", "BEL8", "BEL9", "BEL10", "BEL12", "BEL14", "BEL15", "BEL17", "BEL19", "BEL20"],
        "ECU": ["ECU2", "ECU4", "ECU7", "ECU8", "ECU9", "ECU11", "ECU12", "ECU13", "ECU14", "ECU16", "ECU17", "ECU20"],
        "GER": ["GER1", "GER2", "GER5", "GER6", "GER7", "GER8", "GER9", "GER10", "GER11", "GER12", "GER13", "GER16", "GER18", "GER19"],
        "KSA": ["KSA2", "KSA3", "KSA4", "KSA6", "KSA8", "KSA10", "KSA11", "KSA15", "KSA16"],
        # ---------------------------------------------
        
        "PAN": ["PAN1", "PAN2", "PAN3", "PAN6", "PAN7", "PAN9", "PAN15", "PAN19"],
        "CRO": ["CRO5", "CRO6", "CRO8", "CRO10", "CRO12", "CRO15", "CRO16", "CRO17", "CRO18", "CRO19", "CRO20"],
        "GHA": ["GHA1", "GHA8", "GHA11", "GHA12", "GHA14", "GHA15", "GHA16", "GHA17", "GHA18"],
        "ENG": ["ENG1", "ENG2", "ENG5", "ENG8", "ENG9", "ENG10", "ENG14", "ENG15", "ENG19"],
        "UZB": ["UZB1", "UZB8", "UZB10", "UZB14", "UZB16", "UZB18"], 
        "COL": ["COL1", "COL4", "COL8", "COL12", "COL16", "COL17", "COL18"],
        "COD": ["COD7", "COD8", "COD13"], 
        "POR": ["POR1", "POR2", "POR7", "POR13", "POR14", "POR15", "POR19", "POR20"],
        "JOR": ["JOR1", "JOR2", "JOR3", "JOR6", "JOR7", "JOR10", "JOR11", "JOR15", "JOR16", "JOR18", "JOR19"],
        "NOR": ["NOR1", "NOR2", "NOR3", "NOR4", "NOR6", "NOR7", "NOR8", "NOR9", "NOR11", "NOR12", "NOR14", "NOR15", "NOR16", "NOR17", "NOR18", "NOR19", "NOR20"],
        "IRQ": ["IRQ1", "IRQ2", "IRQ4", "IRQ6", "IRQ12", "IRQ17", "IRQ18"], 
        "SEN": ["SEN2", "SEN4", "SEN8", "SEN12", "SEN13", "SEN14", "SEN16"],
        "FRA": ["FRA4", "FRA9", "FRA11", "FRA16", "FRA20"], 
        "MAR": ["MAR1", "MAR2", "MAR8", "MAR10", "MAR12", "MAR16", "MAR19"],
        "SWE": ["SWE1", "SWE2", "SWE3", "SWE4", "SWE5", "SWE7", "SWE8", "SWE9", "SWE10", "SWE11", "SWE13", "SWE14", "SWE15", "SWE16", "SWE18", "SWE19", "SWE20"],
        "CZE": ["CZE5", "CZE6", "CZE8", "CZE11", "CZE14", "CZE16"],
        "EGY": ["EGY1", "EGY2", "EGY3", "EGY4", "EGY5", "EGY6", "EGY7", "EGY8", "EGY9", "EGY10", "EGY11", "EGY12", "EGY14", "EGY15", "EGY16", "EGY17", "EGY18", "EGY19", "EGY20"],
        "TUR": ["TUR6", "TUR10", "TUR14", "TUR19"],
        "TUN": ["TUN1", "TUN2", "TUN3", "TUN4", "TUN5", "TUN6", "TUN7", "TUN8", "TUN9", "TUN11", "TUN12", "TUN13", "TUN15", "TUN16", "TUN17", "TUN18", "TUN19", "TUN20"],
        "CIV": ["CIV3", "CIV10", "CIV11", "CIV12", "CIV13", "CIV15", "CIV18", "CIV19", "CIV20"],
        "JPN": ["JPN1", "JPN2", "JPN3", "JPN5", "JPN6", "JPN7", "JPN8", "JPN10", "JPN11", "JPN12", "JPN13", "JPN15", "JPN16", "JPN17", "JPN18", "JPN19", "JPN20"],
        "NED": ["NED1", "NED3", "NED7", "NED14", "NED16", "NED17", "NED18", "NED19"],
        "CUW": ["CUW1", "CUW3", "CUW5", "CUW7", "CUW9", "CUW10", "CUW13", "CUW16", "CUW19", "CUW20"],
        "PAR": ["PAR4", "PAR6", "PAR7", "PAR10", "PAR11", "PAR14", "PAR17", "PAR18", "PAR19"],
        "MEX": ["MEX2", "MEX3", "MEX5", "MEX6", "MEX7", "MEX9", "MEX10", "MEX11", "MEX12", "MEX13", "MEX20"],
        "RSA": ["RSA3", "RSA4", "RSA6", "RSA9", "RSA10", "RSA12", "RSA14", "RSA17", "RSA18"],
        "KOR": ["KOR1", "KOR2", "KOR4", "KOR5", "KOR6", "KOR7", "KOR8", "KOR12", "KOR14", "KOR17", "KOR19"],
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
    return paginas, faltantes, repetidas, nombres_paises

paginas, f_ini, r_ini, nombres_paises = inicializar_datos()

if "faltantes" not in st.session_state:
    st.session_state.faltantes = f_ini
if "repetidas" not in st.session_state:
    st.session_state.repetidas = r_ini

# 2. SECCIÓN DE ESTADÍSTICAS Y BARRA DE PROGRESO
total_figus_album = sum(len(v) for v in paginas.values())
total_faltantes = sum(len(v) for v in st.session_state.faltantes.values())
total_pegadas = total_figus_album - total_faltantes
porcentaje = (total_pegadas / total_figus_album)

st.markdown(f"### 📈 ¡Llevamos completado el **{porcentaje:.1%}** del álbum!")
st.progress(porcentaje)

met1, met2 = st.columns(2)
with met1:
    st.metric("📌 Pegadas en el Álbum", f"{total_pegadas} / {total_figus_album}")
with met2:
    st.metric("🔍 Aún nos Faltan", total_faltantes)

st.write("---")

# 3. PESTAÑAS PRINCIPALES
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Buscador", "📌 Registrar Cambios", "🚀 Carga por Bloque", "📋 Faltantes", "🔄 Repetidas"])

with tab1:
    st.subheader("Consultar Figurita")
    busqueda = st.text_input("Ingresá el código entero (Ej: ARG13 o CC7):").strip().upper()
    if busqueda:
        m = re.match(r"([A-ZáéíóúÁÉÍÓÚ\s\-]+)(\d+)", busqueda)
        if m:
            p, n = m.groups()
            if "COCA" in p: p = "Coca-Cola"
            if "HISTORY" in p: p = "FIFA History"
            
            if p in paginas:
                if busqueda in st.session_state.faltantes.get(p, []):
                    st.error(f"🚨 ¡¡NOS FALTA!! La figurita {busqueda} se necesita en el álbum.")
                else:
                    cant = st.session_state.repetidas.get(p, {}).get(n, 0)
                    st.success(f"✅ YA ESTÁ PEGADA. (Tienes {cant} repetidas en el mazo)")
            else:
                st.warning("Esa selección no está registrada.")
        else:
            st.warning("Poné las letras y los números juntos (Ej: MEX17).")

with tab2:
    st.subheader("Modificar Inventario (1 a 1)")
    col1, col2 = st.columns(2)
    with col1:
        seleccion_label = st.selectbox("Elegí el País/Sección:", list(nombres_paises.values()))
        pais_n = [k for k, v in nombres_paises.items() if v == seleccion_label][0]
    with col2:
        num_n = st.number_input("Número de figu:", min_value=1, max_value=20, value=1)
    
    if pais_n == "Coca-Cola": code_n = f"CC{num_n}"
    elif pais_n == "FIFA History": code_n = f"FWC{num_n}"
    else: code_n = f"{pais_n}{num_n}"
    
    str_num = str(num_n)
    cant_actual_repe = st.session_state.repetidas.get(pais_n, {}).get(str_num, 0)
    estado_album = "❌ FALTANTE" if code_n in st.session_state.faltantes.get(pais_n, []) else "✅ PEGADA"
    
    st.info(f"Estado actual de **{code_n}**: Álbum: **{estado_album}** | Repetidas en stock: **{cant_actual_repe}**")
    
    st.write("🟢 **SI CONSEGUISTE ESTA FIGURITA:**")
    btn_pegar, btn_repe = st.columns(2)
    with btn_pegar:
        if st.button("📌 Pegar en el Álbum", key="pegar_manual"):
            if code_n in st.session_state.faltantes.get(pais_n, []):
                st.session_state.faltantes[pais_n].remove(code_n)
                st.success(f"¡Buenísimo! {code_n} guardada en el álbum.")
                st.rerun()
            else:
                st.info("Esa figurita ya figuraba como pegada.")
                
    with btn_repe:
        if st.button("➕ Sumar 1 a Repetidas", key="repe_manual"):
            if pais_n not in st.session_state.repetidas:
                st.session_state.repetidas[pais_n] = {}
            st.session_state.repetidas[pais_n][str_num] = cant_actual_repe + 1
            st.success(f"¡Agregada 1 unidad de {code_n} a las repetidas!")
            st.rerun()

    st.write("🔴 **SI REGALASTE, CAMBIASTE O QUERÉS DESPEGAR:**")
    btn_sacar_repe, btn_despegar = st.columns(2)
    with btn_sacar_repe:
        if st.button("➖ Descontar 1 de Repetidas", key="sacar_repe"):
            if cant_actual_repe > 0:
                st.session_state.repetidas[pais_n][str_num] = cant_actual_repe - 1
                st.error(f"Se descontó 1 repetida de {code_n}. Quedan: {cant_actual_repe - 1}")
                st.rerun()
            else:
                st.warning("No tenías repetidas de esta figurita para restar.")
                
    with btn_despegar:
        if st.button("🗑️ Despegar (Vuelve a faltar)", key="despegar_figu"):
            if code_n not in st.session_state.faltantes.get(pais_n, []):
                st.session_state.faltantes[pais_n].append(code_n)
                st.session_state.faltantes[pais_n].sort(key=lambda x: int(re.search(r'\d+', x).group()))
                st.error(f"{code_n} volvió a la lista de faltantes.")
                st.rerun()
            else:
                st.info("Esta figurita ya estaba marcada como faltante.")

with tab3:
    st.subheader("🚀 Carga o Consulta Masiva")
    st.write("Pegá el texto completo que te mandaron por WhatsApp:")
    texto_bloque = st.text_area("Códigos separados por espacios, comas o renglones:", height=120)
    
    tipo_carga = st.radio("¿Qué querés hacer con esta lista?", [
        "🔎 Solo CONSULTAR cuáles de estas nos sirven (No modifica nada)",
        "📌 Marcar todas como PEGADAS en el álbum", 
        "🔄 Sumar todas a la pila de REPETIDAS"
    ])
    
    if st.button("⚡ Procesar Bloque"):
        if texto_bloque:
            figus_encontradas = re.findall(r"\b([A-ZáéíóúÁÉÍÓÚ\s\-]+)(\d+)\b", texto_bloque.upper())
            
            servir = []
            ya_estan = []
            exito_count = 0
            
            for p, n in figus_encontradas:
                p = p.strip()
                if "COCA" in p: p = "Coca-Cola"
                if "HISTORY" in p: p = "FIFA History"
                
                if p in paginas:
                    if p == "Coca-Cola": full_code = f"CC{n}"
                    elif p == "FIFA History": full_code = f"FWC{n}"
                    else: full_code = f"{p}{n}"
                    
                    if "CONSULTAR" in tipo_carga:
                        if full_code in st.session_state.faltantes.get(p, []):
                            if full_code not in servir: servir.append(full_code)
                        else:
                            if full_code not in ya_estan: ya_estan.append(full_code)
                    elif "PEGADAS" in tipo_carga:
                        if full_code in st.session_state.faltantes.get(p, []):
                            st.session_state.faltantes[p].remove(full_code)
                            exito_count += 1
                    else:
                        if p not in st.session_state.repetidas:
                            st.session_state.repetidas[p] = {}
                        st.session_state.repetidas[p][n] = st.session_state.repetidas[p].get(n, 0) + 1
                        exito_count += 1
            
            if "CONSULTAR" in tipo_carga:
                st.write("---")
                if servir:
                    st.error(f"🚨 **¡¡SÍ, NOS SIRVEN ESTAS ({len(servir)})!!** Van directo al álbum:")
                    st.code(", ".join(servir))
                else:
                    st.success("❌ De esa lista **no nos sirve ninguna**, las tenemos todas pegadas.")
                
                if ya_estan:
                    st.info(f"✅ Esas ya las tenemos pegadas ({len(ya_estan)}):")
                    st.caption(", ".join(ya_estan))
            else:
                if exito_count > 0:
                    st.success(f"¡Espectacular! Se procesaron con éxito **{exito_count}** figuritas.")
                    st.rerun()
                else:
                    st.warning("No se encontraron códigos nuevos para procesar.")
        else:
            st.warning("Por favor, pegá el texto antes de procesar.")

with tab4:
    st.subheader("Baches del Álbum")
    label_f = st.selectbox("Filtrar Faltantes por País:", list(nombres_paises.values()), key="p_f")
    pais_f = [k for k, v in nombres_paises.items() if v == label_f][0]
    
    lista_f = st.session_state.faltantes.get(pais_f, [])
    if lista_f:
        st.write(f"Te faltan **{len(lista_f)}** figuritas en esta sección:")
        st.code(", ".join(lista_f))
    else:
        st.success("¡Página 100% LLENA! 🏆")

with tab5:
    st.subheader("Mazo de Repetidas")
    
    texto_repes = "⚽ REPETIDAS PARA CAMBIAR:\n"
    hay_repes = False
    for p_key, p_name in nombres_paises.items():
        dict_r = st.session_state.repetidas.get(p_key, {})
        activas = {k: v for k, v in dict_r.items() if v > 0}
        if activas:
            hay_repes = True
            repes_str = ", ".join([f"{p_key} {num}" + (f" (x{c})" if c>1 else "") for num, c in activas.items()])
            texto_repes += f"• {p_name}: {repes_str}\n"
            
    if hay_repes:
        st.text_area("📋 Lista lista para copiar y mandar a WhatsApp:", value=texto_repes, height=200)
        st.write("---")
    
    label_r = st.selectbox("Ver Repetidas de:", list(nombres_paises.values()), key="p_r")
    pais_r = [k for k, v in nombres_paises.items() if v == label_r][0]
    
    dict_r = st.session_state.repetidas.get(pais_r, {})
    repes_activas = {k: v for k, v in dict_r.items() if v > 0}
    
    if repes_activas:
        for num, cant in repes_activas.items():
            st.write(f"• **{pais_r} {num}** — Cantidad en mazo: **{cant}**")
    else:
        st.write("Sin repetidas de este país por acá.")
