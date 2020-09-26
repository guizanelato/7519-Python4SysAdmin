# Indica qual a imagem base a ser utilizada
FROM python:3.6

# Copia arquivos da sua maquina host para o container alvo
COPY ./app/requirements.txt /tmp

# instalar as dependencias da aplicação
RUN pip install -r /tmp/requirements.txt

# copiar o diretório da aplicação para o container
COPY ./app /app

# muda o diretório vigente para o diretório da aplicação
WORKDIR /app

# qual a porta será exposta 
EXPOSE 5000

# qual o comando será executado ao iniciar o container
CMD python app.py

