# Projeto Media Downloader
Este documento tem como objetivo servir como manual de referência para o Media Downloader, projeto desenvolvido por mim.

Recomenda-se a leitura atenta de todas as seções para compreender a estrutura, as funcionalidades e os procedimentos 
de instalação e utilização da aplicação.

Em caso de dúvidas, sugestões ou problemas relacionados ao projeto, entre em contato pelo e-mail: 
saulopintobrandaofilho@gmail.com.

--- 

## 1- Panorama 
Este projeto foi desenvolvido com dois objetivos principais.

O primeiro foi o aprendizado e a prática de programação em Python. 
Busquei expandir meus conhecimentos sobre bibliotecas e frameworks 
da linguagem, principalmente o Tkinter, que utilizei como ponto de 
partida para estudar o desenvolvimento de interfaces gráficas.

O segundo objetivo surgiu de uma necessidade de alguns amigos que são 
mestres de RPG. Eles buscavam uma alternativa prática para baixar músicas 
em formato MP3, sem precisar recorrer a sites com excesso de anúncios e adware. 
Pensando nisso, desenvolvi este programa e o disponibilizei para que pudessem 
utilizá-lo em suas sessões.

### 1.1 Estrutura do Projeto

O código do projeto está organizado em três componentes principais, que trabalham 
em conjunto para garantir o funcionamento da aplicação. Cada componente possui responsabilidades
específicas, facilitando a organização, a manutenção e a expansão do projeto.

### Interface
Responsável pela interface gráfica da aplicação, desenvolvida com **CustomTkinter**. 
Contém a instância principal da janela e as funções relacionadas à interação com o usuário, como:

- Iniciar downloads;
- Selecionar o diretório de destino;
- Escolher o formato do arquivo (MP3 ou MP4).

### Serviços
Responsável pela lógica de download da aplicação. Utiliza a biblioteca **yt-dlp** para processar as 
URLs fornecidas pelo usuário e realizar o download dos arquivos nos formatos MP3 ou MP4.

### Conteúdo
Responsável por armazenar os recursos utilizados pela interface gráfica.

Atualmente, contém apenas o ícone do programa, gerado por inteligência artificial. 
Futuramente, poderá armazenar outros recursos visuais necessários à aplicação.

### 1. 2 Uso de Inteligência Artificial
Durante o desenvolvimento deste projeto, utilizei ferramentas de inteligência artificial como recurso de consulta e 
apoio em dúvidas pontuais, além de auxílio na revisão e formatação desta documentação.

Entretanto, todo o código da aplicação foi desenvolvido por mim, sem a utilização de código gerado por inteligência 
artificial.

Como mencionado anteriormente, este projeto teve como objetivo principal o aprendizado e o aperfeiçoamento das minhas 
habilidades em Python. Por esse motivo, priorizei video aulas no Youtube e a consulta às documentações oficiais das tecnologias 
utilizadas, cujos links estão disponíveis na seção Tecnologias Utilizadas.

---

## 2 - Tecnologias utilizadas

O Media Downloader foi desenvolvido utilizando a linguagem Python, em conjunto com bibliotecas que permitem a 
criação da interface gráfica e o gerenciamento dos downloads

### CustomTkinter 
Biblioteca baseada no Tkinter, utilizada para desenvolver a interface gráfica,
<br>Documentação: https://customtkinter.tomschimansky.com
### YT-DLP
Biblioteca responsável pelo processamento das URLs e pelo download dos conteúdos de mídia. Permite obter arquivos de 
áudio e vídeo de diferentes plataformas. 
<br>Documentação: https://github.com/yt-dlp/yt-dlp

### FFmpeg

Ferramenta utilizada no processamento e na conversão dos arquivos de mídia, especialmente na extração e conversão de áudio 
para o formato MP3.
<br> Documentação: https://www.ffmpeg.org

De resto foram utilizados módulos padrão do Python, Estes são:
## pathlib
Módulo nativo do Python utilizado para manipular caminhos de arquivos e diretórios, facilitando a criação, localização e 
organização dos arquivos no sistema

## urllib.parse (urlparse)
Função da biblioteca padrão do Python utilizada para analisar e decompor URLs em seus componentes, como protocolo, domínio
e caminho, auxiliando na validação dos links fornecidos pelo usuário.

---

## 3 - Como utilizar
Para utilizar basta clonar o repositório, criar uma venv e ativa-lá e depois disso rodar os seguintes comandos:
<br> winget install Gyan.FFmpeg -> Esse comando instala o FFmpeg, é necessário para rodar o código.
<br> pip install -r requirements.txt -> Esse comando vai instalar as dependências na sua venv.

### 3.1 Fluxo de comandos

1. Clonar o repositório
<br> git clone (https://github.com/SauloBrandao/PS_ProjetoMediaDownloader.git)
2. Criar e Ativar a venv
<br> python -m venv .venv -> .\.venv\Scripts\Activate.ps1
3. Instalar as dependências Python
<br> pip install -r conteudo/Requerimentos/requirements.txt
4. Instalar o FFmpeg
<br> winget install Gyan.FFmpeg (Para verificar se foi instalado corretamente: ffmpeg -version)
5. Rodar o Código
<br> Basta executar o programa main.py (python main.py)

---

## 4 - Melhorias Futuras

Para as próximas versões do Media Downloader, estão previstas duas melhorias principais:

1. Aprimoramento da interface gráfica: melhorar o design da aplicação, tornando-a visualmente mais 
agradável, moderna e intuitiva para o usuário.

2. Seleção da qualidade de áudio e vídeo: implementar uma funcionalidade que permita ao usuário escolher 
a qualidade dos arquivos antes de iniciar o download, oferecendo maior controle sobre o conteúdo baixado.

