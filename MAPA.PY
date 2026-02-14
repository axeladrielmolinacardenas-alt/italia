import folium
import geopandas as gpd

# Cargar regiones
italia = gpd.read_file("limits_IT_regions.geojson")
italia["reg_name"] = italia["reg_name"].str.upper()

info_gastronomica = {
    "PIEMONTE": {
        "comida": "TRUFA BLANCA",
        "descripcion": "UNO DE LOS PRODUCTOS MÁS EXCLUSIVOS DE ITALIA, UTILIZADO EN PASTAS Y RISOTTOS.",
        "extra": "FAMOSO POR SUS VINOS COMO BAROLO.",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP._RZc_2cZaw3u4Qd4SZBkXQHaE6?cb=defcachec2&w=800&h=531&rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    "LOMBARDIA": {
        "comida": "RISOTTO ALLA MILANESE",
        "descripcion": "ARROZ CREMOSO CON AZAFRÁN TÍPICO DE MILÁN.",
        "extra": "UNA DE LAS REGIONES MÁS INDUSTRIALIZADAS DE ITALIA.",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.XVerPP7HmKjGyuQdfcS7FAHaFj?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    "VENETO": {
        "comida": "TIRAMISÚ",
        "descripcion": "POSTRE A BASE DE CAFÉ, MASCARPONE Y CACAO.",
        "extra": "REGIÓN DONDE SE ENCUENTRA VENECIA.",
        "imagen": "https://img2.rtve.es/v/6897051?w=1600&preview=1684846584492.jpg"
    },

    "LIGURIA": {
        "comida": "PESTO GENOVÉS",
        "descripcion": "SALSA DE ALBAHACA, PIÑONES Y QUESO PARMESANO.",
        "extra": "FAMOSA POR LA COSTA CINQUE TERRE.",
        "imagen": "https://www.thermorecetas.com/wp-content/uploads/2021/01/Salsa-pesto-genoves.jpg"
    },

    "EMILIA-ROMAGNA": {
        "comida": "LASAÑA BOLOÑESA",
        "descripcion": "PASTA HORNEADA CON CARNE Y SALSA BECHAMEL.",
        "extra": "CONSIDERADA LA CAPITAL GASTRONÓMICA DE ITALIA.",
        "imagen": "https://www.hola.com/horizon/landscape/3e8b3904ac1a-adobe-lasana-t.jpg"
    },

    "TOSCANA": {
        "comida": "BISTECCA ALLA FIORENTINA",
        "descripcion": "CORTE DE CARNE GRUESO A LA PARRILLA.",
        "extra": "TIERRA DE VINOS Y ARTE RENACENTISTA.",
        "imagen": "https://d21klxpge3tttg.cloudfront.net/wp-content/uploads/2016/02/BISTECCA-093022.jpg"
    },

    "LAZIO": {
        "comida": "PASTA CARBONARA",
        "descripcion": "PASTA CON HUEVO, QUESO PECORINO Y GUANCIALE.",
        "extra": "REGIÓN DONDE SE ENCUENTRA ROMA.",
        "imagen": "https://littlespoonfarm.com/wp-content/uploads/2024/07/Pasta-Carbonara-Recipe.jpg"
    },

    "CAMPANIA": {
        "comida": "PIZZA NAPOLETANA",
        "descripcion": "PIZZA ORIGINAL DE MASA DELGADA Y BORDE ESPONJOSO.",
        "extra": "CUNA DE LA PIZZA EN EL MUNDO.",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.4ahv2pt1iM_M37L_q_L-vAHaE8?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    "SICILIA": {
        "comida": "ARANCINI",
        "descripcion": "BOLAS DE ARROZ RELLENAS Y FRITAS.",
        "extra": "INFLUENCIA ÁRABE Y MEDITERRÁNEA.",
        "imagen": "https://insanelygoodrecipes.com/wp-content/uploads/2024/09/arancini-recipe.jpg"
    },

    "SARDEGNA": {
        "comida": "PORCEDDU",
        "descripcion": "CERDO ASADO TRADICIONAL.",
        "extra": "ISLA CON FUERTE IDENTIDAD CULTURAL.",
        "imagen": "https://www.virtuquotidiane.it/wp-content/uploads/2018/12/porceddu.png"
    },
    "TRENTINO-ALTO ADIGE/SÜDTIROL": {
        "comida": "CANEDERLI",
        "descripcion": "BOLAS DE PAN CON SPECK Y QUESO, TÍPICAS DE LA ZONA ALPINA.",
        "extra": "REGIÓN CON FUERTE INFLUENCIA AUSTRIACA Y CULTURA BILINGÜE.",
        "imagen": "https://tse3.mm.bing.net/th/id/OIP.VN_NX3TzNcNg_OGeR494lQHaE8?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    "VALLE D'AOSTA/VALLÉE D'AOSTE": {
        "comida": "FONDUTA VALDOSTANA",
        "descripcion": "PLATO TRADICIONAL A BASE DE QUESO FONTINA DERRETIDO.",
        "extra": "PEQUEÑA REGIÓN ALPINA CON INFLUENCIA FRANCESA.",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.STVLjNrGYKquFfM_LTvRsQHaHa?cb=defcachec2&w=768&h=768&rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    "FRIULI-VENEZIA GIULIA": {
        "comida": "FRICO",
        "descripcion": "PLATO A BASE DE QUESO MONTASIO DERRETIDO Y PAPA.",
        "extra": "REGIÓN CON INFLUENCIA CENTROEUROPEA.",
        "imagen": "https://www.moltofood.it/wp-content/uploads/2024/04/Frico-1536x1024.jpg"
    },

    "UMBRIA": {
        "comida": "PORCHETTA",
        "descripcion": "CERDO ASADO CON HIERBAS AROMÁTICAS.",
        "extra": "CONOCIDA COMO EL CORAZÓN VERDE DE ITALIA.",
        "imagen": "https://www.datocms-assets.com/32685/1656946809-porchetta-2.jpg"
    },

    "MARCHE": {
        "comida": "OLIVE ALL'ASCOLANA",
        "descripcion": "ACEITUNAS RELLENAS DE CARNE Y FRITAS.",
        "extra": "REGIÓN COSTERA CON GRAN TRADICIÓN MARINA.",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.bE8K1MAi6bNDqmdSyxf8ZgHaF4?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3"
     },

    "ABRUZZO": {
        "comida": "ARROSTICINI",
        "descripcion": "BROCHETAS DE CARNE DE CORDERO A LA PARRILLA.",
        "extra": "REGIÓN MONTAÑOSA CON FUERTE TRADICIÓN GANADERA.",
        "imagen": "https://www.italia.it/content/dam/tdh/es/interests/abruzzo/gli-arrosticini-vanto-e-patrimonio-della-gastronomia-abruzzese/media/1600X1000_gli_arrosticini_hero.jpg"
    },

    "MOLISE": {
        "comida": "CAVATELLI",
        "descripcion": "PASTA TRADICIONAL SERVIDA CON SALSA DE CARNE.",
        "extra": "UNA DE LAS REGIONES MÁS PEQUEÑAS Y TRADICIONALES.",
        "imagen": "https://polentaebaccaladotcom.files.wordpress.com/2019/04/cavatelli_peperoni_cruschi_1.jpg?w=1000"
    },

    "PUGLIA": {
        "comida": "ORECCHIETTE",
        "descripcion": "PASTA EN FORMA DE OREJA SERVIDA CON BRÓCOLI O RAGÚ.",
        "extra": "FAMOSA POR SU ACEITE DE OLIVA Y COSTAS ADRIÁTICAS.",
        "imagen": "https://www.thespruceeats.com/thmb/d2bUkwWo-5g-dYq47g11oiwqyAI=/4997x3331/filters:no_upscale():max_bytes(150000):strip_icc()/orecchiette-pasta-944161200-f09ae8f792604894a300b32bc36a4811.jpg"
    },

    "BASILICATA": {
        "comida": "PASTA CON PEPERONI CRUSCHI",
        "descripcion": "PASTA CON PIMIENTOS SECOS CRUJIENTES.",
        "extra": "REGIÓN HISTÓRICA CON PAISAJES MONTAÑOSOS.",
        "imagen": "https://blog.giallozafferano.it/fornoefornelli/wp-content/uploads/2020/08/pasta-con-peperoni-cruschi-1.jpg"
    },

    "CALABRIA": {
        "comida": "NDUJA",
        "descripcion": "EMBUTIDO PICANTE UNTABLE TÍPICO DEL SUR.",
        "extra": "REGIÓN CON SABORES INTENSOS Y PICANTES.",
        "imagen": "https://www.seriouseats.com/thmb/Wr0ZOhB9s3Nu-D2RKy4mjpUHO40=/1500x1125/filters:fill(auto,1)/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2020__02__20200210-nduja-product-vicky-wasik-70e99d1cd4a644398fe50e3b23373f18.jpg"
    }

}

# Crear HTML dinámico para popup
def crear_popup(region):
    if region in info_gastronomica:
        datos = info_gastronomica[region]
        return f"""
        <div style="font-family: Georgia; text-align:center;">
            <h2 style="color:#8B0000;">{region}</h2>
            <h3>🍝 {datos['comida']}</h3>
            <p>{datos['descripcion']}</p>
            <img src="{datos['imagen']}" width="220">
        </div>
        """
    else:
        return f"""
        <div style="font-family: Georgia; text-align:center;">
            <h2>{region}</h2>
            <p>Información gastronómica próximamente...</p>
        </div>
        """

# Agregar columna con HTML
italia["popup_html"] = italia["reg_name"].apply(crear_popup)

# Crear mapa
mapa = folium.Map(location=[42.5, 12.5], zoom_start=6, tiles="CartoDB positron")

# Agregar GeoJson
folium.GeoJson(
    italia,
    tooltip=folium.GeoJsonTooltip(
        fields=["reg_name"],
        aliases=["🍝 NOMBRE:"],
        style="""
            font-family: Georgia;
            font-size: 18px;
            font-weight: bold;
            color: darkred;
            background-color: #FFF8DC;
            border-radius: 6px;
            padding: 6px;
            text-align: center;
        """
    ),
    popup=folium.GeoJsonPopup(
        fields=["popup_html"],
        labels=False,
        parse_html=True
    ),
    style_function=lambda x: {
        "fillColor": "#6E2AA5",
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.6,
    }
).add_to(mapa)

# Guardar archivo
mapa.save("italia_gastronomico.html")
