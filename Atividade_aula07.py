import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixa o léxico do VADER
nltk.download("vader_lexicon")

# Inicializa o analisador
sia = SentimentIntensityAnalyzer()

st.title("Análise de Sentimentos (Português)")
st.write("Digite um texto em português para analisar o sentimento.")

# Entrada de texto
texto = st.text_area(
    "Texto",
    placeholder="Ex.: Hoje foi um dia incrível, estou muito feliz com os resultados!"
)

# Botão para analisar
if st.button("Analisar"):

    if texto.strip():

        # Tradução simples PT -> EN para melhorar o VADER
        traducoes = {
            "bom": "good",
            "boa": "good",
            "ótimo": "great",
            "otimo": "great",
            "excelente": "excellent",
            "incrível": "amazing",
            "incrivel": "amazing",
            "feliz": "happy",
            "amor": "love",
            "gosto": "like",
            "maravilhoso": "wonderful",
            "ruim": "bad",
            "péssimo": "terrible",
            "pessimo": "terrible",
            "horrível": "horrible",
            "horrivel": "horrible",
            "triste": "sad",
            "ódio": "hate",
            "odio": "hate",
            "raiva": "angry",
            "decepcionado": "disappointed",
            "decepcionante": "disappointing",
            "não": "not",
            "nao": "not",
            "nunca": "never",
            "sim": "yes",
            "muito": "very"
        }

        texto_processado = texto.lower()

        # Substitui palavras em português por equivalentes em inglês
        for pt, en in traducoes.items():
            texto_processado = texto_processado.replace(pt, en)

        # Analisa o sentimento
        score = sia.polarity_scores(texto_processado)
        compound = score["compound"]

        # Define o rótulo
        if compound >= 0.05:
            sentimento = "😊 Positivo"
        elif compound <= -0.05:
            sentimento = "😞 Negativo"
        else:
            sentimento = "😐 Neutro"

        st.write("### Resultado")
        st.write(f"**Sentimento:** {sentimento}")
        st.write(f"**Compound:** {compound:.3f}")

    else:
        st.warning("Digite um texto para analisar.")