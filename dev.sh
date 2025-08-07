#!/bin/bash

# Este script sobe todo o ambiente de desenvolvimento usando Docker Compose.

# Garante que o script pare se algum comando falhar
set -e

# Cores para o output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}▶ Iniciando todos os serviços com Docker Compose...${NC}"
echo "  (Isso pode levar alguns minutos na primeira vez para construir as imagens)"

# Constrói as imagens (se necessário) e sobe os containers em modo 'detached' (-d)
# CORREÇÃO: Usando 'docker compose' em vez de 'docker-compose'
docker compose up --build -d

echo ""
echo -e "${GREEN}✔ Ambiente iniciado com sucesso!${NC}"
echo ""
echo "Acesse os serviços nos seguintes endereços:"
echo "--------------------------------------------"
echo -e "🔗 Frontend (Aplicação Web): ${GREEN}http://localhost:3000${NC}"
echo -e "🔗 Backend (Documentação da API): ${GREEN}http://localhost:8000/docs${NC}"
echo -e "🔗 RabbitMQ (Painel de Gerenciamento): ${GREEN}http://localhost:15672${NC} (user: user, pass: password)"
echo "--------------------------------------------"
echo ""
echo "Para ver os logs de todos os serviços, use o comando: docker compose logs -f"
echo "Para parar todos os serviços, use o comando: docker compose down"
echo ""