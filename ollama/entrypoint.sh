#!/bin/bash
set -e

# Inicia el servicio de Ollama en segundo plano
ollama serve &

# Esperamos unos segundos para que el servidor esté listo
sleep 5

# Descargamos el modelo si no existe aún
if ! ollama list | grep -q "llama3.2"; then
  echo "Descargando modelo llama3.2..."
  ollama pull llama3.2
else
  echo "El modelo llama3.2 ya está disponible."
fi

# Mantenemos el contenedor corriendo
wait
