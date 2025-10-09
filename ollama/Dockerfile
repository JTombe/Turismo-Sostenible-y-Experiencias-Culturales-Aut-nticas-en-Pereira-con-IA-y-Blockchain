FROM ollama/ollama

# Copiamos el script de inicio
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Usamos el script como entrypoint
ENTRYPOINT ["/entrypoint.sh"]
