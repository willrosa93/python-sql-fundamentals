# 1. Imagem base — Python 3.11 versão enxuta (slim = sem pacotes desnecessários)
FROM python:3.11-slim

# 2. Pasta de trabalho dentro do container
WORKDIR /app

# 3. Copia só o requirements primeiro (otimização de cache do Docker)
#    Se o código mudar mas as dependências não, o Docker reaproveita essa camada
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o restante do código
COPY . .

# 6. Variáveis de ambiente com valores padrão
#    Podem ser sobrescritas no docker-compose ou no docker run
ENV DB_HOST=postgres
ENV DB_NAME=banco_poo
ENV DB_USER=postgres
ENV DB_PASSWORD=123456

# 7. Porta — não abre porta de rede (app de terminal), mas boa prática documentar
EXPOSE 5432

# 8. Comando que roda quando o container sobe
CMD ["python", "__main__.py"]
