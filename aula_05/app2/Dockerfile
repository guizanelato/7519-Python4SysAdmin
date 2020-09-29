# build #1

# definição de uma imagem leve, e adicionado um apelido
FROM python:3-alpine as base

# criação de um diretórios
RUN mkdir /install

# mudança do diretório vigente para o diretório /install
WORKDIR /install

# cópia do arquivo de dependencias da app
COPY ./requirements.txt /requirements.txt

# instalação das dependencias através do pip 
RUN pip install --prefix=/install -r /requirements.txt

## segundo passo - build #2 

FROM base 

# copiando a partir da imagem gerada
COPY --from=base /install /usr/local 

# copiar a aplicação para o container
COPY . /app

# define o diretório de trabalho
WORKDIR /app

# exposicão da porta
EXPOSE 8000

# comando a ser executando quando container subir
CMD ["gunicorn", "-w 4", "app:app", "-b 0.0.0.0:8000"  ]

