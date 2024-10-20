import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',
                   page_title='thomas-killman-test')

V = 0
P = 0
K = 0
E = 0
A = 0

if "page" not in st.session_state:
    st.session_state.page = 0


def calculation():
    global A, V, E, P, K
    if index == 1 or index == 27:
        if option == f"***A***:{questions_list[i]}":
            E += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            A += 1
    elif index == 15:
        if option == f"***A***:{questions_list[i]}":
            A += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            E += 1

    elif index == 2 or index == 26:
        if option == f"***A***:{questions_list[i]}":
            K += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            P += 1
    elif index == 20:
        if option == f"***A***:{questions_list[i]}":
            P += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            K += 1

    elif index == 3 or index == 25:
        if option == f"***A***:{questions_list[i]}":
            V += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            A += 1
    elif index == 16:
        if option == f"***A***:{questions_list[i]}":
            A += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            V += 1

    elif index == 5 or index == 19 or index == 23:
        if option == f"***A***:{questions_list[i]}":
            P += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            E += 1

    elif index == 6 or index == 9:
        if option == f"***A***:{questions_list[i]}":
            E += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            V += 1
    elif index == 17:
        if option == f"***A***:{questions_list[i]}":
            V += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            E += 1

    elif index == 7 or index == 12:
        if option == f"***A***:{questions_list[i]}":
            E += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            K += 1
    elif index == 29:
        if option == f"***A***:{questions_list[i]}":
            K += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            E += 1

    elif index == 8 or index == 28:
        if option == f"***A***:{questions_list[i]}":
            V += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            P += 1
    elif index == 14:
        if option == f"***A***:{questions_list[i]}":
            P += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            V += 1

    elif index == 13 or index == 22:
        if option == f"***A***:{questions_list[i]}":
            K += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            V += 1
    elif index == 10:
        if option == f"***A***:{questions_list[i]}":
            V += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            K += 1

    elif index == 18 or index == 24:
        if option == f"***A***:{questions_list[i]}":
            A += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            K += 1
    elif index == 4:
        if option == f"***A***:{questions_list[i]}":
            K += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            A += 1

    elif index == 21 or index == 30:
        if option == f"***A***:{questions_list[i]}":
            A += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            P += 1
    elif index == 11:
        if option == f"***A***:{questions_list[i]}":
            P += 1
        elif option == f"***B***:{questions_list[i + 1]}":
            A += 1
def nextpage(): st.session_state.page += 1


def goback(): st.session_state.page -= 1


placeholder = st.empty()

if st.session_state.page == 0:
    Main_Page_HTML = open("main_page.html", "r", encoding='utf-8')
    html_source = Main_Page_HTML.read()
    st.html(html_source)

    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column ratios as needed
    with col2:
        st.button("Teszt kitöltése", on_click=nextpage)

elif st.session_state.page == 1:
    st.write("#")
    Test_Page_HTML = open("test_page.html", "r", encoding='utf-8')
    html_source = Test_Page_HTML.read()
    st.html(html_source)

    txt_source = open("questions", "r", encoding='utf-8')
    questions = txt_source.read()
    questions_list = questions.split("\n")

    i = 0
    for index, item in enumerate(questions_list, start=1):
        option = st.radio(
            label=f"{index}",
            options=(f"***A***:{questions_list[i]}", f"***B***:{questions_list[i + 1]}"),
            index=None,
            key=index,
        )
        calculation()
        i += 2
        if index == 30:
            break

    #st.markdown(f"A:{A}")
    #st.markdown(f"E:{E}")
    #st.markdown(f"K:{K}")
    #st.markdown(f"P:{P}")
    #st.markdown(f"V:{V}")

    st.session_state['A'] = A
    st.session_state['E'] = E
    st.session_state['K'] = K
    st.session_state['P'] = P
    st.session_state['V'] = V

    if A + E + K + P + V == 30:
        st.button("Eredmények megtekintése", on_click=nextpage)

elif st.session_state.page == 2:
    Test_HTML = open("test.html", "r", encoding='utf-8')
    html_source = Test_HTML.read()
    st.html(html_source)

    A = st.session_state['A']
    E = st.session_state['E']
    K = st.session_state['K']
    P = st.session_state['P']
    V = st.session_state['V']

    A_pct = (round(A / 30 * 100, None))
    E_pct = (round(E / 30 * 100, None))
    K_pct = (round(K / 30 * 100, None))
    P_pct = (round(P / 30 * 100, None))
    V_pct = (round(V / 30 * 100, None))

    labels = 'Alkalmazkodó', 'Elkerülő', 'Kompromisszumkereső', 'Problémamegoldó', 'Versengő'
    sizes = [A_pct, E_pct, K_pct, P_pct, V_pct]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%.0f%%', textprops={'size': 'smaller'}, radius=0.9)

    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column ratios as needed

    st.markdown("""
            <style>
            [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
                gap: 0rem;
            }
            </style>
            """, unsafe_allow_html=True)

    with col2:
        st.pyplot(fig1)

    c1, c2, c3 = st.columns([1, 1, 1])  # Adjust column ratios as needed
    with c2:
        st.button("eredmények leírása", on_click=nextpage)

elif st.session_state.page == 3:
    st.button("vissza az előző oldalra", on_click=goback)
    Test_results = open("tests_results.html", "r", encoding='utf-8')
    html_source = Test_results.read()
    st.html(html_source)
