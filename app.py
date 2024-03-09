import streamlit as st

st.set_page_config(page_title='CSS Fitler Preview', page_icon='favicon.ico', layout='wide')

if 'blur' not in st.session_state:
    st.session_state['blur'] = 0.0

if 'brightness' not in st.session_state:
    st.session_state['brightness'] = 1.0

if 'contrast' not in st.session_state:
    st.session_state['contrast'] = 1.0

if 'grayscale' not in st.session_state:
    st.session_state['grayscale'] = 0.0

if 'hue_rotate' not in st.session_state:
    st.session_state['hue_rotate'] = 0

if 'invert' not in st.session_state:
    st.session_state['invert'] = 0.0

if 'opacity' not in st.session_state:
    st.session_state['opacity'] = 1.0

if 'saturate' not in st.session_state:
    st.session_state['saturate'] = 1.0

if 'sepia' not in st.session_state:
    st.session_state['sepia'] = 0.0

if 'drop_shadow_1' not in st.session_state:
    st.session_state['drop_shadow_1'] = 0.0

if 'drop_shadow_2' not in st.session_state:
    st.session_state['drop_shadow_2'] = 0.0

if 'drop_shadow_3' not in st.session_state:
    st.session_state['drop_shadow_3'] = 0.0

if 'drop_shadow_color' not in st.session_state:
    st.session_state['drop_shadow_color'] = "#000000"


with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def update_image():
    st.markdown(f'''<style>
                    div[data-testid="stImage"] img {{
                        filter: blur({st.session_state['blur']}px) 
                        brightness({st.session_state['brightness']}) 
                        contrast({st.session_state['contrast']}) 
                        drop-shadow({st.session_state['drop_shadow_1']}px {st.session_state['drop_shadow_2']}px {st.session_state['drop_shadow_3']}px {st.session_state['drop_shadow_color']}) 
                        grayscale({st.session_state['grayscale']}) 
                        hue-rotate({st.session_state['hue_rotate']}deg) 
                        invert({st.session_state['invert']}) 
                        opacity({st.session_state['opacity']}) 
                        saturate({st.session_state['saturate']}) 
                        sepia({st.session_state['sepia']})) !important;
                    }}
                </style>''', unsafe_allow_html=True)


col1, col2, col3 = st.columns([6.5, 5, 2.5])

with col2:
    uploaded_image = st.file_uploader("Upload your image", type=['png', 'jpg', 'svg', 'jpeg', 'webp'])

col1, col2, col3, col4 = st.columns([4,1,6,1])

with col1:
    col11, col12 = st.columns(2)
    with col11:
        st.number_input("Blur", min_value=0.0, max_value=1000.00, step=1.0, key='blur', on_change=update_image, help="Value in px. From 0 to 1000")
        st.number_input('Brightness', min_value=0.0, max_value=1000.0, step=1.0, key="brightness", on_change=update_image, help='From 0 to 1000')
        st.number_input("Contrast", min_value=0.0, max_value=1000.0, step=1.0, key='contrast', on_change=update_image, help='From 0  to 1000')
        st.number_input("Grayscale", min_value=0.0, max_value=1.0, step=0.01, key='grayscale', on_change=update_image, help='From 0 to 1')
        st.number_input("Hue-rotate", min_value=0, max_value=360, step=1, key='hue_rotate', on_change=update_image, help='Value in degrees. From 0 to 360')

    with col12:
        st.number_input("Invert", min_value=0.0, max_value=1.0, step=0.01, key='invert', on_change=update_image, help='From 0 to 1')
        st.number_input("Opacity", min_value=0.0, max_value=1.0, step=0.00, key='opacity', on_change=update_image, help='From 0 to 1')
        st.number_input("Saturate", min_value=0.0, max_value=100.0, step=0.1, key='saturate', on_change=update_image, help='From 0 to 100')
        st.number_input("Sepia", min_value=0.0, max_value=1.0, step=0.01, key='sepia', on_change=update_image, help='From 0 to 1')
    col121, col122, col123, col124 = st.columns(4)

    with col121:
        st.number_input("Length 1", min_value=-100.0, max_value=500.0, step=1.0, key='drop_shadow_1', on_change=update_image, help='From -500 to 500')

    with col122:
        st.number_input("Length 2", min_value=-100.0, max_value=500.0, step=1.0, key='drop_shadow_2', on_change=update_image, help='From -500 to 500')

    with col123:
        st.number_input("Length 3", min_value=0.0, max_value=500.0, step=1.0, key='drop_shadow_3', on_change=update_image, help='From 1 to 100')

    with col124:
        st.color_picker("Color", key='drop_shadow_color', on_change=update_image, help='Pick a color')

css_code = 'filter:'

if st.session_state['blur'] != 0.0:
    css_code += f" blur({round(st.session_state['blur'],2)}px)"

if st.session_state['brightness'] != 1.0:
    css_code += f" brightness({round(st.session_state['brightness'],2)})"

if st.session_state['contrast'] != 1.0:
    css_code += f" contrast({round(st.session_state['contrast'],2)})"

if st.session_state['drop_shadow_1'] != 0.0 or st.session_state['drop_shadow_2'] != 0.0 or st.session_state['drop_shadow_3'] != 0.0:
    css_code += f" drop-shadow({round(st.session_state['drop_shadow_1'],2)} {round(st.session_state['drop_shadow_2'],2)} {round(st.session_state['drop_shadow_3'],2)} {st.session_state['drop_shadow_color']})"

if st.session_state['grayscale'] != 0.0:
    css_code += f" grayscale({round(st.session_state['grayscale'],2)})"

if st.session_state['hue_rotate'] != 0.0:
    css_code += f" hue-rotate({round(st.session_state['hue_rotate'],2)}deg)"

if st.session_state['invert'] != 0.0:
    css_code += f" invert({round(st.session_state['invert'],2)})"

if st.session_state['opacity'] != 1.0:
    css_code += f" opacity({round(st.session_state['opacity'],2)})"

if st.session_state['saturate'] != 1.0:
    css_code += f" saturate({round(st.session_state['saturate'],2)})"

if st.session_state['sepia'] != 0.0:
    css_code += f" sepia({round(st.session_state['sepia'],2)})"

if css_code == 'filter:':
    css_code = ''
    with col1:
        st.code(f'{css_code}', language='css')
else:
    with col1:
        st.code(f'{css_code};', language='css')

try:
    with col3:
        image = st.image(uploaded_image)
except AttributeError as e:
    pass