import discord
from discord.ext import commands
from bot_logic import gen_pass
import os, random,requests
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='.', intents=intents)
@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá eu sou um bot subimisso ao {bot.user}!')
@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def decompose(ctx, material: str = None):
    """Descobre quanto tempo um material leva para se decompor!"""
    
    materiais = {
        'papel': {'tempo': '2-6 meses', 'emoji': '📄', 'frase': 'Esse papel tá decompondo mais rápido que meu código! 💀'},
        'plastico': {'tempo': '400-1000 anos', 'emoji': '🟦', 'frase': 'Esse plástico vai durar mais que sua amizade no Discord! 💔'},
        'vidro': {'tempo': '1 milhão de anos', 'emoji': '🍾', 'frase': 'Esse vidro é mais durável que um admin! 👑'},
        'metal': {'tempo': '200-500 anos', 'emoji': '⚙️', 'frase': 'Ferroso e furioso! 🚗'},
        'banana': {'tempo': '2-10 dias', 'emoji': '🍌', 'frase': 'Banana decompondo mais rápido que sua motivação na segunda! 😂'},
        'madeira': {'tempo': '3-6 anos', 'emoji': '🌳', 'frase': 'Mais resistente que minha motivação! 😴'},
        'eletronico': {'tempo': '50+ anos', 'emoji': '📱', 'frase': 'E-lixo que ninguém quer! 🚫'},
        'algodao': {'tempo': '1-5 meses', 'emoji': '👕', 'frase': 'Mais rápido que dizer "só mais um episódio"! 📺'}
    }
    
    if material is None:
        materiais_list = ', '.join(list(materiais.keys()))
        await ctx.send(f"📋 Materiais: `{materiais_list}`\nUse `.decompose <material>`")
        return

    material = material.lower()
    
    if material not in materiais:
        await ctx.send(f"❌ Material '{material}' não encontrado!")
        return

    dados = materiais[material]
    await ctx.send(f"{dados['emoji']} **{material.upper()}**\n⏱️ Tempo: {dados['tempo']}\n💡 {dados['frase']}")
bot.run
