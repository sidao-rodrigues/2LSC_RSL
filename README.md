# 2LSC_RSL
Algoritmo em python utilizado na busca de artigos para anais de eventos em formato PDF para RSLs.

Há necessidade de instalação da biblioteca PDFminer para executar todas as funcionalidades do algoritmo. Link: https://pypi.org/project/pdfminer/

No exemplo exposto nesse algoritmo utilizou-se a seguinte string de busca para teste:

<strong><i>(mobilidade OR locomoção OR localização) AND ("deficiência visual" OR "deficiente visual" OR cegueira) AND ("tecnologia assistiva" OR "tecnologias assistivas")</strong></i>

Para o operador lógico AND utilizou-se o seguinte código <strong><i>re.search("palavra_pesquisada", texto)</strong></i>. Onde deve-se colocar a palavra que se quer pesquisar entre aspas. Já o operador lógico OR é representado pelo caratere | (pipe), que deve ser colocado entre as palavras dentro das aspas, como observa-se no código a seguir <strong><i>re.search("palavra_pesquisada1|palavra_pesquisada2", texto)</strong></i>.

O código pode ser modificado e utilizado livremente. 

Compartilhe e contribua para que nossa comunidade acadêmica possa ter mais trabalhos e bons frutos! (:  

Créditos: Sidney R., Lucas M., Leonardo A., Cynthia M.
