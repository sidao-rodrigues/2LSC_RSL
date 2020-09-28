#caso você não possua o pdfminer instalado, pode instalá-lo através do seguinte link: https://pypi.org/project/pdfminer/
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import re

#endereço do arquivo a ser analisado
#exemplo para linux '/home/sidao/pesquisa.pdf'
#exemplo para windows 'C:\\Users\\sidao\\Documentos\\pesquisa.pdf'
path_arquivo = '/home/sidao/pesquisa.pdf'

fp = open(path_arquivo, 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)

pagina = 0
qtd_trabalhos = 0
paginas = []
for page in pages:
    pagina = int(pagina) + 1
    interpreter.process_page(page)
    layout = device.get_result()
    for lobj in layout:
        if isinstance(lobj, LTTextBox):
            #verifica a primeira página dos artigos nos anais de acordo com os e-mails válidos dos pesquisadores, ou seja,
            #o algorítmo irá identificar a primeira página ao encontrar um email válido nos anais.
            if re.search(r"[^@]+@[^@]+\.[^@]+", lobj.get_text()):
                #Identificado a primeira página do artigo, o algoritmo irá imprimir no console a página de todos os artigos do arquivo.
                qtd_trabalhos = int(qtd_trabalhos) + 1
                print("Artigo "+str(qtd_trabalhos)+" na pagina: "+str(pagina))
                texto = ""
                for l in layout:
                    if isinstance(l, LTTextBox):
                        #Nesse momento o algoritmo irá pegar todo o texto da primeira página do artigo dos anais e armazenar na variável texto
                        #que em seguida será utilizada para comparar com a string de busca da RSL.
                        #(Obs.: Todo o texto da primeira página foi convertido para caixa baixa (minúsculo) para evitar problemas.)
                        texto = texto + l.get_text().lower()
                texto = ' '.join(texto.split())
                #Armazenado todo o texto da primeira página encontrada, o algoritmo irá realizar o teste da string de busca e verificar se as palavras da string se adaqua ao artigo.
                #Nesse momento foi utilizado várias condições para combinar os operadores lógicos AND e OR. Quando se tem o operador OR em várias palavras dentro do mesmo escopo uitiliza-se o caratere | (pipe)
                #e quando se quer fazer outra operação com AND, utiliza-se o código re.search('palavra_que_se_quer_pesquisar', texto).
                #Por exemplo, em nossa RSL a string de busca utilizada foi a seguinte como pode-se ver no código:
                #(mobilidade OR locomoção OR localização) AND ("deficiência visual" OR "deficiente visual" OR cegueira) AND ("tecnologia assistiva" OR "tecnologias assistivas")
                if re.search("mobilidade|locomoção|localização", texto) and re.search("deficiência visual|deficiente visual|cegueira", texto) and re.search("tecnologia assistiva|tecnologias assistivas", texto):
                    #Caso encontre as palavras da string de busca, o algoritmo irá imprimir no console que foi encontrado um artigo com essas caracteristicas na página tal.
                    print("Artigo encontrado referente a string de busca encontrado na pagina :"+str(pagina))
                    paginas.append(pagina)
                break
                
#APRESENTAÇÃO DE RESULTADOS
print("\n\n"+("#" * 60))
print("#"+(" " * 18)+"RESULTADO DA PESQUISA!"+(" " * 18)+"#")
print(("#" * 60)+"\n")
print("Caminho do arquivo analisado: \n"+path_arquivo)
print("\nQuantidade de artigos no arquivo: "+str(qtd_trabalhos))
print("\n")
print("Artigos encontrados pela aplicação da string de busca: "+str(len(paginas))+"\n")
for pg in paginas:
    print(">>>>> Artigo encontrado na página: "+str(pg))
print("") 
print(("#" * 60))
