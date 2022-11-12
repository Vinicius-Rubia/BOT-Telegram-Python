import telebot

# Token access API 
CHAVE_API = "5107846500:AAHRZLTptLDIrfUgxPh73l7EMW8hSx6ya4w"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["front"])
def front(mensagem):
  bot.send_message(mensagem.chat.id, "Desenvolvimento web front-end é o desenvolvimento da interface gráfica do usuário de um site, através do uso de HTML, CSS e JavaScript, para que os usuários possam visualizar e interagir com esse site.")

@bot.message_handler(commands=["back"])
def back(mensagem):
  bot.send_message(mensagem.chat.id, "O desenvolvedor back end trabalha com o lado servidor da aplicação, sendo o responsável por tudo o que acontece por trás da tela. Ele é o responsável por desenvolver os códigos que passarão as instruções para a aplicação, para que os usuários possam acessar a interface e cumprir as solicitações desejadas.")

@bot.message_handler(commands=["full"])
def full(mensagem):
  bot.send_message(mensagem.chat.id, "Full Stack é um tipo de profissional ligado à área de TI capaz de trabalhar nas mais diversas atividades que dizem respeito ao desenvolvimento e programação web, muito valorizado no mercado graças ao seu conhecimento em diferentes linguagens, códigos e tecnologias.")

@bot.message_handler(commands=["opcao_1"])
def opcao1(mensagem):
  bot.send_message(mensagem.chat.id, "Bot, diminutivo de robot, também conhecido como Internet bot ou web robot, é uma aplicação de software concebido para simular ações humanas repetidas vezes de maneira padrão, da mesma forma como faria um robô.")

@bot.message_handler(commands=["opcao_2"])
def opca2(mensagem):
  texto = """
Qual área que saber?
  /front - Front-end
  /back - Back-end
  /full - Fullstack
  /start - Voltar ao início
  """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao_3"])
def opcao3(mensagem):
  bot.send_message(mensagem.chat.id, "Valeu! Vinicius mandou um abraço de volta.")

def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  texto = """
Olá, eu sou um bot do conhecimento, o que quer saber?
  /opcao_1 - O que é um bot?
  /opcao_2 - Quero saber sobre programação
  /opcao_3 - Mandar um abraço pro Vinicius
Responder qualquer outra coisa não vai funcionar, escolha uma das opções.
  """
  bot.reply_to(mensagem, texto)

bot.polling()