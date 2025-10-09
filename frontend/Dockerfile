FROM node:20-alpine

WORKDIR /app

# Copiamos primero los manifiestos para aprovechar la cache de Docker
COPY package*.json ./

# Instalamos dependencias
RUN npm install

# Copiamos el resto del código
COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]