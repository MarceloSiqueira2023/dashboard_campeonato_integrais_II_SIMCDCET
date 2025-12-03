import streamlit as st

st.set_page_config(page_title="Campeonato de Integrais", layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.image("logo_unifap.png", use_container_width=False, width=200)

with col2:
    st.subheader("**FUNDAÇÃO UNIVERSIDADE FEDERAL DO AMAPÁ - UNIFAP**")
    st.subheader("**DEPARTAMENTO DE CIÊNCIAS EXATAS E TECNOLÓGICAS - DCET**")
    st.subheader("**II SIMPÓSIO CIENTÍFICO DO DCET**")

with col3:
    st.image("logo_simposio_2025.png", use_container_width=False, width=220)

#st.title("🏆 Campeonato de Integrais - 2025")
st.markdown("<h1 style='text-align: center;'>🏆 Campeonato de Integrais - 2025</h1>", unsafe_allow_html=True)
st.markdown("---")
# Dados das integrais
integrais = [
    {
        "nome": "Integral 1",
        "integral": r"\int \frac{x^4 - 5x^2 + 10}{x^2} \, dx",
        "dica": r"Resolvida por integração por partes, com $\int u \, dv = uv - \int v \, du$. Escolhemos $u = x$ e $dv = \cos(x) dx$. Daí, $du = dx$ e $v = \sin(x)$.",
        "dica_eq": r"""\begin{aligned}
\int \left(\frac{x^4}{x^2} - \frac{5x^2}{x^2} + \frac{10}{x^2}\right) dx &= \int (x^2 - 5 + 10x^{-2}) dx \\
&= \frac{x^3}{3} - 5x + \frac{10x^{-1}}{-1} + c
\end{aligned}""",
        "solucao": r"\frac{x^3}{3} - 5x - \frac{10}{x} + c"
    },
    {
        "nome": "Integral 2",
        "integral": r"\int e^{2x+1} \, dx",
        "dica": r"Utiliza-se o método da substituição. Definimos $u = 2x+1$, o que implica $du = 2dx$. Retornando à variável original, temos a solução.",
        "dica_eq": r"""\begin{aligned}
\int e^u \frac{du}{2} &= \frac{1}{2} \int e^u du = \frac{1}{2} e^u + c
\end{aligned}""",
        "solucao": r"\frac{e^{2x+1}}{2} + c"
    },
    {
        "nome": "Integral 3",
        "integral": r"\int x \cos(x) \, dx",
        "dica": r"Resolvida por integração por partes, com $\int u \, dv = uv - \int v \, du$. Escolhemos $u = x$ e $dv = \cos(x) dx$. Daí, $du = dx$ e $v = \sin(x)$.",
        "dica_eq": r"""\begin{aligned}
\int x \cos(x) dx &= x \sin(x) - \int \sin(x) dx \\
&= x \sin(x) - (-\cos(x)) + C
\end{aligned}""",
        "solucao": r"x \sin(x) + \cos(x) + C"
    },
    {
        "nome": "Integral 4",
        "integral": r"\int \ln(2x+1) \, dx",
        "dica": r"Aplica-se integração por partes. Escolhemos $u = \ln(2x+1)$ e $dv = dx$. Com isso, $du = \frac{2}{2x+1} dx$ e $v = x$. A integral restante resolve-se por manipulação algébrica.",
        "dica_eq": r"""\begin{aligned}
\int \ln(2x+1) dx &= x \ln(2x+1) - \int \frac{2x}{2x+1} dx \\
\int \frac{2x+1-1}{2x+1} dx &= \int \left(1 - \frac{1}{2x+1}\right) dx = x - \frac{1}{2}\ln|2x+1|
\end{aligned}""",
        "solucao": r"x \ln(2x+1) - x + \frac{1}{2}\ln|2x+1| + C"
    },
    {
        "nome": "Integral 5",
        "integral": r"\int \ln(x) \, dx",
        "dica": r"Integração por partes. Definimos $u = \ln(x)$ e $dv = dx$. Assim, $du = \frac{1}{x} dx$ e $v = x$.",
        "dica_eq": r"""\begin{aligned}
\int \ln(x) dx &= x \ln(x) - \int x \cdot \frac{1}{x} dx \\
&= x \ln(x) - \int dx
\end{aligned}""",
        "solucao": r"x \ln(x) - x + C"
    },
    {
        "nome": "Integral 6",
        "integral": r"\int x \cos(x) \, dx",
        "dica": r"Esta é a mesma integral da de número 3, apresentada aqui para reforçar o método.",
        "dica_eq": "",
        "solucao": r"x \sin(x) + \cos(x) + C"
    },
    {
        "nome": "Integral 7",
        "integral": r"\int x^2 e^{x^3} \, dx",
        "dica": r"Método da substituição. Escolhemos $u = x^3$, de modo que $du = 3x^2 dx$.",
        "dica_eq": r"""\begin{aligned}
\int e^{x^3} (x^2 dx) &= \int e^u \frac{du}{3} = \frac{1}{3} e^u + C
\end{aligned}""",
        "solucao": r"\frac{1}{3} e^{x^3} + C"
    },
    {
        "nome": "Integral 8",
        "integral": r"\int \frac{x}{(1+4x^2)^2} \, dx",
        "dica": r"Método da substituição. Definimos $u = 1+4x^2$, o que implica $du = 8x dx$.",
        "dica_eq": r"""\begin{aligned}
\int \frac{1}{u^2} \frac{du}{8} &= \frac{1}{8} \int u^{-2} du \\
&= \frac{1}{8} \cdot \frac{u^{-1}}{-1} + C = -\frac{1}{8u} + C
\end{aligned}""",
        "solucao": r"-\frac{1}{8(1+4x^2)} + C"
    },
    {
        "nome": "Integral 9",
        "integral": r"\int\frac{\sqrt{2+x^{2}}-\sqrt{2-x^{2}}}{\sqrt{4-x^{4}}}\,dx",
        "dica": r"Simplificação do integrando. O denominador $\sqrt{4-x^4}$ é fatorado como $\sqrt{(2-x^2)(2+x^2)}$, permitindo a separação em duas integrais de tabela. A solução vem da aplicação das fórmulas para $\int\frac{1}{\sqrt{a^2-x^2}}$ e $\int\frac{1}{\sqrt{a^2+x^2}}$.",
        "dica_eq": r"""\int\frac{1}{\sqrt{2-x^{2}}}dx - \int\frac{1}{\sqrt{2+x^{2}}}dx""",
        "solucao": r"\arcsin\left(\frac{x}{\sqrt{2}}\right) - \ln|x+\sqrt{2+x^{2}}|+C"
    },
    {
        "nome": "Integral 10",
        "integral": r"\int\frac{dx}{\sqrt{x(1-x)}}",
        "dica": r"Substituição trigonométrica. Definimos $x = \sin^2(u)$, o que leva a $dx = 2\sin(u)\cos(u)du$. A integral se simplifica para $\int 2du = 2u+c$. Retornando a variável, $u = \arcsin(\sqrt{x})$.",
        "dica_eq": "",
        "solucao": r"2\arcsin(\sqrt{x}) + c"
    },
    {
        "nome": "Integral 11",
        "integral": r"\int\frac{dx}{1+\sin(x)+\cos(x)}",
        "dica": r"Substituição de Weierstrass, usando $\alpha = \tan(x/2)$. Isso transforma a integral trigonométrica em uma integral de função racional, $\int\frac{1}{1+\alpha}d\alpha$, que é $\ln|1+\alpha| + C$.",
        "dica_eq": "",
        "solucao": r"\ln\left|1+\tan\left(\frac{x}{2}\right)\right| + C"
    },
    {
        "nome": "Integral 12",
        "integral": r"\int\frac{\cos(x)}{\sqrt{1+\sin^2(x)}}\,dx",
        "dica": r"Substituição simples. Com $t = \sin(x)$ e $dt = \cos(x)dx$, a integral se torna $\int\frac{dt}{\sqrt{1+t^2}}$, que é uma integral de tabela.",
        "dica_eq": "",
        "solucao": r"\ln|\sin(x)+\sqrt{1+\sin^2(x)}| + C"
    },
    {
        "nome": "Integral 13",
        "integral": r"\int\frac{x}{(x-1)(x+1)^2}\,dx",
        "dica": r"Decomposição em frações parciais. A expressão é decomposta como $\frac{A}{x-1} + \frac{B}{x+1} + \frac{C}{(x+1)^2}$. Resolvendo o sistema, encontramos $A=1/4, B=-1/4, C=1/2$. Integra-se cada termo separadamente.",
        "dica_eq": "",
        "solucao": r"\frac{1}{4}\ln|x-1| - \frac{1}{4}\ln|x+1| - \frac{1}{2(x+1)} + C"
    },
    {
        "nome": "Integral 14",
        "integral": r"\int\frac{\cos(x)}{\sqrt{2\sin(x)+1}}\,dx",
        "dica": r"Substituição. Com $u = 2\sin(x)+1$, temos $du = 2\cos(x)dx$. A integral se reduz a $\frac{1}{2}\int u^{-1/2}du$.",
        "dica_eq": "",
        "solucao": r"\sqrt{2\sin(x)+1} + C"
    },
    {
        "nome": "Integral 15",
        "integral": r"\int\frac{dx}{(a^2+x^2)^{3/2}}",
        "dica": r"Substituição trigonométrica. Usando $x = a\tan(\theta)$, a integral se simplifica para $\frac{1}{a^2}\int\cos(\theta)d\theta$. Para retornar à variável $x$, usamos o triângulo retângulo, onde $\sin(\theta) = \frac{x}{\sqrt{a^2+x^2}}$.",
        "dica_eq": "",
        "solucao": r"\frac{1}{a^2}\frac{x}{\sqrt{a^2+x^2}} + C"
    },
    {
        "nome": "Integral 16",
        "integral": r"\int \ln(1-x)\,dx",
        "dica": r"Combinação de substituição ($u=1-x$) e integração por partes. A integral se torna $-\int \ln(u)du$, resolvida por partes, resultando em $-(u\ln(u)-u)+C$.",
        "dica_eq": "",
        "solucao": r"-(1-x)\ln(1-x) + (1-x) + C"
    },
    {
        "nome": "Integral 17",
        "integral": r"\int x\cos^2(x)\,dx",
        "dica": r"Primeiro, usa-se a identidade de redução de potência $\cos^2(x) = \frac{1+\cos(2x)}{2}$. A integral é então separada em $\frac{1}{2}\int xdx + \frac{1}{2}\int x\cos(2x)dx$. A segunda parte requer integração por partes.",
        "dica_eq": "",
        "solucao": r"\frac{x^2}{4} + \frac{x}{4}\sin(2x) + \frac{\cos(2x)}{8} + C"
    },
    {
        "nome": "Integral 18",
        "integral": r"\int x^m \ln(x)\,dx \quad (m \neq -1)",
        "dica": r"Integração por partes, com $u = \ln(x)$ e $dv = x^m dx$.",
        "dica_eq": r"""\frac{x^{m+1}}{m+1}\ln(x) - \int \frac{x^{m+1}}{m+1}\frac{1}{x}dx = \frac{x^{m+1}}{m+1}\ln(x) - \frac{1}{(m+1)^2}x^{m+1} + C""",
        "solucao": r"\frac{x^{m+1}}{m+1}\left(\ln(x) - \frac{1}{m+1}\right) + C"
    },
    {
        "nome": "Integral 19",
        "integral": r"\int_{-2}^{3}(x^{2}-3)\,dx",
        "dica": r"Integração direta de polinômio e aplicação do Teorema Fundamental do Cálculo.",
        "dica_eq": r"""\begin{aligned}
\int_{-2}^{3}(x^{2}-3)dx &= \left[ \frac{x^3}{3} - 3x \right]_{-2}^{3} \\
&= \left( \frac{3^3}{3} - 3(3) \right) - \left( \frac{(-2)^3}{3} - 3(-2) \right) \\
&= (9 - 9) - \left( -\frac{8}{3} + \frac{18}{3} \right) = 0 - \frac{10}{3}
\end{aligned}""",
        "solucao": r"-\frac{10}{3}"
    },
    {
        "nome": "Integral 20",
        "integral": r"\int_{1}^{2}(4x^{3}-3x^{2}+2x)\,dx",
        "dica": r"Integração direta e aplicação do Teorema Fundamental do Cálculo.",
        "dica_eq": r"""\left[ x^4 - x^3 + x^2 \right]_{1}^{2} = (16-8+4) - (1-1+1) = 12 - 1""",
        "solucao": r"11"
    },
    {
        "nome": "Integral 21",
        "integral": r"\int x^{3}\cos(x^{4}+2)\,dx",
        "dica": r"Substituição. Seja $u=x^4+2$, então $du=4x^3dx$. A integral vira $\frac{1}{4}\int\cos(u)du = \frac{1}{4}\sin(u)+C$.",
        "dica_eq": "",
        "solucao": r"\frac{1}{4}\sin(x^4+2) + C"
    },
    {
        "nome": "Integral 22",
        "integral": r"\int \sqrt{2x+1}\,dx",
        "dica": r"Substituição. Seja $u=2x+1$, então $du=2dx$. A integral vira $\frac{1}{2}\int u^{1/2}du = \frac{1}{2}\frac{u^{3/2}}{3/2}+C = \frac{1}{3}u^{3/2}+C$.",
        "dica_eq": "",
        "solucao": r"\frac{1}{3}(2x+1)^{3/2} + C"
    },
    {
        "nome": "Integral 23",
        "integral": r"\int x\sin(x)\,dx",
        "dica": r"Integração por partes. Com $u=x$ e $dv=\sin(x)dx$, temos $du=dx$ e $v=-\cos(x)$. A fórmula resulta em $-x\cos(x) - \int(-\cos(x))dx$.",
        "dica_eq": "",
        "solucao": r"-x\cos(x) + \sin(x) + C"
    },
    {
        "nome": "Integral 24",
        "integral": r"\int t^{2}e^{t}\,dt",
        "dica": r"Integração por partes aplicada duas vezes. Primeira: $u=t^2, dv=e^t dt$. Resulta em $t^2e^t - 2\int te^t dt$. Segunda: $u=t, dv=e^t dt$ para a nova integral.",
        "dica_eq": "",
        "solucao": r"(t^2 - 2t + 2)e^t + C"
    },
    {
        "nome": "Integral 25",
        "integral": r"\int \cos^{3}(x)\,dx",
        "dica": r"Identidade trigonométrica. Reescrevemos como $\int(1-\sin^2(x))\cos(x)dx$. Com $u=\sin(x)$, vira $\int(1-u^2)du = u - u^3/3+C$.",
        "dica_eq": "",
        "solucao": r"\sin(x) - \frac{\sin^3(x)}{3} + C"
    },
    {
        "nome": "Integral 26",
        "integral": r"\int\frac{\sqrt{9-x^{2}}}{x^{2}}\,dx",
        "dica": r"Substituição trigonométrica. Com $x=3\sin(\theta)$, a integral se torna $\int\cot^2(\theta)d\theta = \int(\csc^2(\theta)-1)d\theta = -\cot(\theta)-\theta+C$. Retornar a $x$ requer o triângulo.",
        "dica_eq": "",
        "solucao": r"-\frac{\sqrt{9-x^2}}{x} - \arcsin(x/3) + C"
    },
    {
        "nome": "Integral 27",
        "integral": r"\int \frac{x^{3}+x}{x-1}\,dx",
        "dica": r"Divisão de polinômios, pois o grau do numerador é maior. $(x^3+x) \div (x-1) = x^2+x+2$ com resto 2. A integral se torna $\int(x^2+x+2+\frac{2}{x-1})dx$.",
        "dica_eq": "",
        "solucao": r"\frac{x^3}{3} + \frac{x^2}{2} + 2x + 2\ln|x-1| + C"
    },
    {
        "nome": "Integral 28",
        "integral": r"\int \frac{2x^{2}-x+4}{x^{3}+4x}\,dx",
        "dica": r"Frações parciais. O denominador é $x(x^2+4)$. A decomposição é $\frac{A}{x} + \frac{Bx+C}{x^2+4}$. Encontramos $A=1, B=1, C=-1$. A integral se torna $\int\frac{1}{x}dx + \int\frac{x}{x^2+4}dx - \int\frac{1}{x^2+4}dx$.",
        "dica_eq": "",
        "solucao": r"\ln|x| + \frac{1}{2}\ln(x^2+4) - \frac{1}{2}\arctan(x/2) + C"
    }
]

# Sidebar
st.sidebar.header("📚 Selecione uma Integral")
selected_nome = st.sidebar.selectbox("Escolha:", [i["nome"] for i in integrais])

# Encontrar índice
idx = next(i for i, integral in enumerate(integrais) if integral["nome"] == selected_nome)
integral_data = integrais[idx]

# Conteúdo principal
st.header(integral_data["nome"])
st.markdown("### Integral a ser resolvida:")
st.latex(integral_data["integral"])

# Estado para botões
if "show_dica" not in st.session_state:
    st.session_state.show_dica = False
if "show_solucao" not in st.session_state:
    st.session_state.show_solucao = False

col1, col2 = st.columns(2)
with col1:
    if st.button("💡 Mostrar Dica"):
        st.session_state.show_dica = not st.session_state.show_dica

with col2:
    if st.button("🎯 Mostrar Resultado"):
        st.session_state.show_solucao = not st.session_state.show_solucao

# Dica
if st.session_state.show_dica:
    with st.expander("Dica de Solução", expanded=True):
        st.markdown(integral_data["dica"])
        if integral_data["dica_eq"]:
            st.latex(integral_data["dica_eq"])

# Solução
if st.session_state.show_solucao:
    with st.expander("Solução Final", expanded=True):
        st.latex(integral_data["solucao"])

st.markdown("---")
st.markdown("*Desenvolvido para o II Simpósio Científico do DCET - UNIFAP*")