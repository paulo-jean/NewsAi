import win32com.client as win32
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from google import generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

api = DuckDuckGoSearchAPIWrapper(region='br-pt', backend='api', time='w', source='text')
ddg = DuckDuckGoSearchResults(api_wrapper=api, num_results=3)
api_timao = DuckDuckGoSearchAPIWrapper(region='br-pt', backend='api', time='d', source='text')
ddg_timao = DuckDuckGoSearchResults(api_wrapper=api_timao, num_results=4)
#p_iallms = ddg.run('IA llms')
# p_ia = ddg.run('IA, llms')
# p_politica = ddg.run('política em SP')
# p_time = ddg_timao.run('corinthians')
#print(p_ia)

#for m in genai.list_models():print(m)
gmodel = ChatGoogleGenerativeAI(model='models/gemini-1.0-pro', api_key='AIzaSyCvQ-H2J72SEtJO9I-QSu-jGUAAsIHccJ4')
headers = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
data_hoje = datetime.today().date()
llm = ChatGroq(model='llama-3.1-70b-versatile', api_key='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', verbose=True)
#llm = ChatGroq(model='llama-3.1-8b-instant', api_key='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', verbose=True)
    

def enviar_email(texto):
    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = "machado.jeanpaulo@gmail.com"
    email.Subject = "News de hoje!"
    email.HTMLBody = texto
    # f"""
    # <p>Eaí JP, aqui é o Jean</p>

    # <p>Atenciosamente,</p>
    # <p>Jean Paulo</p>
    # """

    # anexo = r"C:\Users\jmachado\Desktop\llm\AutoEmail.py"
    # email.Attachments.Add(anexo)

    email.Send()
    welldone = "Email Enviado"
    return welldone

# def criar_conteudo_v1():
#     '''Função responsável por criar a notícia extraindo os conteúdos da web setados
#     e passando-os para o llm elaborar'''
#     #cnn
#     url_cnn = 'https://www.cnnbrasil.com.br/tudo-sobre/inteligencia-artificial/'
#     cnn = requests.get(url_cnn, headers=headers)
#     soup = BeautifulSoup(cnn.content, 'html.parser')
#     cnn_noticias = soup.find_all('a', class_="home__list__tag")
#     cnn_texto = [texto.find('h3', class_='news-item-header__title').text.strip() for texto in cnn_noticias] #soup.get_text()
#     cnn_urls = [u['href'] for u in cnn_noticias if u['href']]
#     cnn_img_urls = [u.find('img')['src'] for u in cnn_noticias if u.find('img')['src']]
    
#     #blog
#     url_blog = 'https://iaexpert.academy/blog/'
#     blog = requests.get(url_blog, headers=headers)
#     blog_soup = BeautifulSoup(blog.content, 'html.parser')
#     blog_texto = blog_soup.get_text()
#     blog_noticias = blog_soup.find_all("h2")
#     blog_urls = []
#     for url in blog_noticias:
#         blog_urls.append(url.a)

   
#     #llm = ChatGroq(model='llama-3.1-70b-versatile', api_key='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', verbose=True)
#     #{context_cnn} {urls_cnn} \ {context_blog} {urls_blog}
#     template = '''
#     você é um escritor de notícias responsável por extrair as últimas notícias mais recentes sobre Inteligência Artificial.
#     Utilize os conteúdos fornecidos como contexto: {context} {urls} {img}

#     Sua tarefa é extrair 3 notícias e elaborar um resumo de cada notícia com sua imagem e sua respectiva url.
#     Coloque sua resposta no estilo de uma Newsletter seguindo o modelo abaixo:

#     [título da notícia]\n
#     [imagem]\n
#     [resumo da notícia]\n
#     [link da notícia]\n
    
#     *obervação_1 -> Utilize o seguinte texto para iniciar a Newsletter:

#     "Olá, leitores! 📰

#     Sejam bem-vindos à nossa newsletter sobre Inteligência Artificial 👨‍💻🤖\n
#     Reunimos alguns artigos relevantes para você se manter atualizado sobre o universo da IA."

#     *observação_2 -> O formato de saída final deve ser em: <!DOCTYPE html>
#     '''
#     #{context_cnn} Formate sua resposta final em Markdown no estilo de uma newsletter

#     prompt = ChatPromptTemplate.from_template(template)

#     chain = prompt | llm | StrOutputParser()

#     resultado_texto = chain.invoke({'context': cnn_texto, 'urls': cnn_urls, 'img': cnn_img_urls})
#     #resultado_texto = chain.invoke({'context': contextos})
#     return resultado_texto

def cnn_newsletter_v2():
    '''Função responsável por criar a notícia extraindo os conteúdos da web setados
    e passando-os para o llm elaborar'''
    #cnn
    url_cnn = 'https://www.cnnbrasil.com.br/tudo-sobre/inteligencia-artificial/'
    cnn = requests.get(url_cnn, headers=headers)
    soup = BeautifulSoup(cnn.content, 'html.parser')
    cnn_noticias = soup.find_all('a', class_="home__list__tag")
    #cnn_titulos = [texto.find('h3', class_='news-item-header__title').text.strip() for texto in cnn_noticias]
    cnn_texto = [texto.get_text() for texto in cnn_noticias]
    cnn_imgs = [img['src'] for img in soup.select('.home__list__tag img')]
    cnn_urls = [u['href'] for u in cnn_noticias if u['href']]
    #cnn_img_urls = [u.find('img')['src'] for u in cnn_noticias if u.find('img')['src']]
    #lista_cnn = [item for pair in zip(cnn_texto, cnn_urls) for item in pair]
    lista_cnn = []
    for texto, img, url in zip(cnn_texto, cnn_imgs, cnn_urls):
        lista_cnn.append(texto)
        lista_cnn.append(img)
        lista_cnn.append(url)
    # Com base na data atual: {data}
    template = '''
    você é um agente Jornalista e Escritor.
   
    Com base na data atual {data}
    utilize o contexto fornecido para extrair as 3 notícias mais recentes.
    contexto: {context}

    expected output: json

    "title":
    "date":
    "image":  
    "link": 

    '''
    #{context_cnn} Formate sua resposta final em Markdown no estilo de uma newsletter

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    resultado_texto = chain.invoke({"data":data_hoje, "context":lista_cnn})
    return resultado_texto

def corinthians_newsletter_v2():
    '''Função responsável por criar a notícia extraindo os conteúdos da web setados
    e passando-os para o llm elaborar'''
    # Corinthians
    c = requests.get("https://www.uol.com.br/esporte/futebol/times/corinthians/", headers=headers)
    csoup = BeautifulSoup(c.content, 'html.parser')
    ctexto = [text.get_text() for text in csoup.select('.thumbnails-wrapper a')]
    cimgs = [img['data-src'] for img in csoup.select('.thumb-layer img')]
    clinks = [link['href'] for link in csoup.select('.thumbnails-wrapper a')]
    lista_corinthians = []
    for t, i, l in zip(ctexto,cimgs,clinks):
        lista_corinthians.append(t)
        lista_corinthians.append(i)
        lista_corinthians.append(l)
   
    #llm = ChatGroq(model='llama-3.1-70b-versatile', api_key='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', verbose=True)
    
    template = '''
    você é um agente Jornalista e Escritor.
    Com base na data atual: {data}
    extraia as 3 notícias mais recentes do contexto fornecido,
    contexto: {context}

    expected output: json

    "title":
    "date":
    "image":  
    "link": 

    '''
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    resultado_texto = chain.invoke({"data":data_hoje,"context":lista_corinthians})
    return resultado_texto

def converter_html(news):
    template_html = '''
    você é responsável por converter a newsletter recebida como contexto para o formato <!DOCTYPE html>.

    *obervação_1 -> Utilize o seguinte texto para iniciar a Newsletter:

    "Olá, JP! 📰

    Seja bem-vindo à sua Newsletter 👨‍💻🤖\n
    Reunimos alguns artigos relevantes para você se manter atualizado!"

    contexto:
    {noticias}

    *não remova e nem acrescente nenhuma informação adicional, apenas faça a conversão do contexto recebido para o formato HTML.
    '''
    prompt_html = ChatPromptTemplate.from_template(template_html)
    chain_html = prompt_html | llm | StrOutputParser()

    resultado_final = chain_html.invoke({'noticias':news})
    return resultado_final

# #print(criar_conteudo())

# news = criar_newsletter_v2()
# news_html = converter_html(news)

#print(enviar_email(news_html))  Utilize os conteúdos fornecidos como contexto: {context} e elaborar um resumo de cada notícia com sua imagem e sua respectiva url.

#version 3
def criar():
    template = '''
    você é um escritor de notícias responsável por escrever um resumo das notícias recebidas como contexto: {context1} | {context2} | {context3}
   
    Sua tarefa é escrever 2 notícias sobre cada assunto recebido nos contextos.
    Coloque sua resposta no estilo de uma Newsletter seguindo o modelo abaixo:

    [título da notícia]\n
    [resumo da notícia]\n
    [link da notícia]\n
    
    *obervação_1 -> Utilize o seguinte texto para iniciar a Newsletter:

    "Olá, JP! 📰

    Seja bem-vindo à sua Newsletter 👨‍💻🤖\n
    Reunimos alguns artigos relevantes para você se manter atualizado!"
    
    *observação_2 -> O formato de saída final deve ser em: <!DOCTYPE html>
    '''
    
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | gmodel | StrOutputParser()

    resultado = chain.invoke({'context1': p_ia, 'context2': p_politica, 'context3': p_time })
    #resultado_texto = chain.invoke({'context': contextos})
    return resultado

noticias = [cnn_newsletter_v2(), corinthians_newsletter_v2()]
#print(converter_html(noticias))
enviar_email(converter_html(noticias))

#enviar_email(criar())
