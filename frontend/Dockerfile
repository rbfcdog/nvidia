# frontend/Dockerfile

# 1. Imagem Base
# Usamos uma imagem "alpine" que é leve, ideal para desenvolvimento.
FROM node:20-alpine

# 2. Diretório de Trabalho
# Define o diretório padrão dentro do container.
WORKDIR /app

# 3. Otimização de Cache de Dependências
# Copia primeiro os arquivos que definem as dependências.
# Se esses arquivos não mudarem, o Docker reutiliza o cache desta camada,
# tornando a instalação de dependências muito mais rápida nas próximas vezes.
COPY /src/package.json ./
COPY /src/package-lock.json ./

# 4. Instalação das Dependências
# Executa o 'npm install' para baixar as bibliotecas listadas no package-lock.json.
RUN npm install

# 5. Copia o Código da Aplicação
# Copia todo o resto do seu código para o diretório de trabalho.
# Esta camada muda com frequência, por isso fica por último.
COPY . .

# 6. Exposição da Porta
# Informa ao Docker que o container escutará na porta 3000.
EXPOSE 3000

# 7. Comando de Execução
# Roda o servidor de desenvolvimento do Next.js.
# Este servidor é otimizado para recarregar automaticamente quando detecta
# mudanças nos arquivos, o que é perfeito para desenvolver.
CMD ["npm", "run", "dev"]