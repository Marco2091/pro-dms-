from flask import Flask, render_template, request

app = Flask(__name__)

# Fatores de emissão SIMPLIFICADOS (estimativas educacionais).
# TODO (próxima etapa): trocar por fontes oficiais e citar no README.
KG_CO2_POR_KM_CARRO = 0.17
KG_CO2_POR_KM_ONIBUS = 0.09
KG_CO2_POR_KWH = 0.08          # matriz elétrica brasileira (aprox.)
KG_CO2_POR_REFEICAO_CARNE = 3.0
KG_CO2_LIXO_POR_SEMANA = {"separa": 0.5, "parcial": 1.5, "nao_separa": 3.0}
MEDIA_MUNDIAL_TON = 4.7        # t CO2 por pessoa/ano (aprox.)

DICAS = {
    "transporte": "Troque alguns trajetos de carro por ônibus, bicicleta ou caminhada, e divida caronas.",
    "energia": "Apague luzes, desligue aparelhos da tomada e prefira lâmpadas LED e eletrodomésticos eficientes.",
    "alimentacao": "Reduza as refeições com carne vermelha e inclua mais refeições com legumes, grãos e vegetais.",
    "lixo": "Separe o lixo reciclável e faça compostagem dos restos de comida quando possível.",
}


def numero(campo, padrao=0.0):
    """Lê um número do formulário com segurança (nunca negativo)."""
    try:
        return max(0.0, float(request.form.get(campo, padrao)))
    except (TypeError, ValueError):
        return padrao


def calcular(km_carro, km_onibus, kwh_mes, refeicoes_carne, lixo):
    """Retorna as emissões anuais por categoria, em toneladas de CO2."""
    semanas = 52
    return {
        "transporte": (km_carro * KG_CO2_POR_KM_CARRO + km_onibus * KG_CO2_POR_KM_ONIBUS) * semanas / 1000,
        "energia": kwh_mes * KG_CO2_POR_KWH * 12 / 1000,
        "alimentacao": refeicoes_carne * KG_CO2_POR_REFEICAO_CARNE * semanas / 1000,
        "lixo": KG_CO2_LIXO_POR_SEMANA.get(lixo, 1.5) * semanas / 1000,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    emissoes = calcular(
        numero("km_carro"),
        numero("km_onibus"),
        numero("kwh_mes"),
        numero("refeicoes_carne"),
        request.form.get("lixo", "parcial"),
    )
    total = sum(emissoes.values())
    maior = max(emissoes, key=emissoes.get)
    return render_template(
        "resultado.html",
        emissoes={k: round(v, 2) for k, v in emissoes.items()},
        total=round(total, 2),
        media=MEDIA_MUNDIAL_TON,
        acima=total > MEDIA_MUNDIAL_TON,
        maior=maior,
        dica=DICAS[maior],
    )


if __name__ == "__main__":
    app.run(debug=True)
