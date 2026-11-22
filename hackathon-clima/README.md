# 🌍 EcoPegada — Hackathon: Mudanças Climáticas

## Esse é o tipo do meu projeto:
> **Site (Flask + HTML/CSS)** — uma calculadora de pegada de carbono que mostra o impacto dos hábitos diários da pessoa e sugere ações práticas para reduzi-lo.

## Aqui está a ideia do meu projeto:
> As mudanças climáticas são causadas principalmente pela emissão de gases de efeito estufa (CO₂, metano...) por atividades humanas como transporte, energia e alimentação.
> O **EcoPegada** deixa isso concreto: a pessoa responde algumas perguntas simples (quanto anda de carro/ônibus, consumo de energia, quantas vezes come carne por semana, como descarta o lixo) e recebe:
> 1. Sua **pegada de carbono estimada por ano** (em toneladas de CO₂);
> 2. Uma **comparação** com a média mundial;
> 3. **Dicas personalizadas** para reduzir as emissões nas categorias em que ela mais pesa.
>
> **Por que ajuda?** Pesquisas mostram que as pessoas agem mais quando enxergam o impacto das próprias escolhas. O site transforma um problema global em ações individuais mensuráveis.

## Como as perguntas do hackathon são respondidas
1. **O que é mudança climática?** Alterações de longo prazo nas temperaturas e nos padrões do clima.
2. **Qual a gravidade? Nos diz respeito?** Sim: secas, enchentes, ondas de calor e elevação do nível do mar já afetam o Brasil, inclusive o Nordeste.
3. **O que causa?** Principalmente a queima de combustíveis fósseis, o desmatamento e a pecuária.
4. **Como conter?** Reduzindo emissões (energia limpa, transporte eficiente, alimentação, reciclagem) e conscientizando as pessoas — é isso que o site faz.

## As bibliotecas que vou usar:
- **Flask** — servidor web e rotas (`pip install Flask`)
- **Jinja2** (já vem com o Flask) — templates HTML dinâmicos
- *(opcional, próxima etapa)* **matplotlib** ou **Chart.js** — gráfico da pegada por categoria
- *(opcional, próxima etapa)* **SQLite / Flask-SQLAlchemy** — salvar o histórico de resultados

## Referências úteis:
- Projeto "Calculadora ecológica" feito nas aulas do curso (HTML + CSS + templates Flask) — base do template
- Arquivos `flask.py` e `site.html` deste repositório (exemplos das aulas)
- Documentação oficial do Flask — exemplos de rotas e formulários: https://flask.palletsprojects.com/en/stable/quickstart/

## Os artigos de orientação que me ajudarão durante o desenvolvimento
- Visão geral sobre o tema: [O que são mudanças climáticas? (ONU Brasil)](https://brasil.un.org/pt-br/175180-o-que-s%C3%A3o-mudan%C3%A7as-clim%C3%A1ticas)
- Causas e efeitos, para embasar as dicas: [Causas e efeitos das mudanças climáticas (ONU)](https://www.un.org/pt/climatechange/science/causes-effects-climate-change)
- Como receber dados de formulários no Flask (`request.form`): [Flask Quickstart — The Request Object](https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object)
- Como usar templates e variáveis Jinja: [Flask — Templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)

> ⚠️ Antes de entregar, confira se os links acima abrem e troque/adicione os que você e sua equipe acharem melhores.

## Como rodar
```bash
cd hackathon-clima
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
python app.py
```
Abra http://127.0.0.1:5000

> ⚠️ Este repositório tem um arquivo chamado `flask.py` na raiz. **Não rode o projeto de dentro da raiz** nem copie o `flask.py` para dentro desta pasta: ele "esconde" a biblioteca Flask e causa erro de import.

## Estrutura
```
hackathon-clima/
├── app.py                 # rotas e cálculo
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html         # formulário
│   └── resultado.html     # resultado + dicas
├── static/style.css
├── PERGUNTAS_TUTOR.md
└── README.md
```

## Aviso sobre os números
Os fatores de emissão em `app.py` são **estimativas simplificadas** para fins educacionais. Na próxima etapa, vale substituí-los por fontes oficiais e citá-las aqui.
