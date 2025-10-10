# Etapa de desarrollo
FROM node:20

WORKDIR /app

# Copiar dependencias e instalar
COPY package*.json ./
RUN npm install

# Copiar el resto del código
COPY . .

# Exponer el puerto que usa Vite
EXPOSE 5173

# Comando para desarrollo
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
