# Aplicaciones de Chat con Llama 4 Maverick utilizando OpenRouter

Este repositorio contiene dos aplicaciones Gradio separadas que demuestran diferentes formas de interactuar con el modelo Llama 4 Maverick a través de la API de OpenRouter:

1. **Chat LLM** - Una interfaz de chat simple para interacción directa con el LLM
2. **Chat con Agentes** - Una interfaz de chat mejorada con capacidades de agente LlamaIndex ReAct y herramientas personalizadas

## Características

**Aplicación de Chat LLM:**
- Interfaz de chat básica con el modelo Llama 4 Maverick
- Comunicación directa con la API de OpenRouter
- Historial de conversación mantenido durante la sesión

**Aplicación de Chat con Agentes:**
- Interfaz de chat mejorada con agente LlamaIndex ReAct
- Integración de herramientas para obtener precios de criptomonedas en tiempo real
- Capacidades avanzadas de razonamiento para manejar tareas complejas
- Soporte completo para historial de conversación

## Configuración

1. Clona este repositorio
2. Instala los requisitos (compartidos por ambas aplicaciones):
   ```
   pip install -r requirements.txt
   ```
3. Crea archivos `.env` en ambos directorios a partir de sus respectivos ejemplos:
   ```
   cp LLM/.env.example LLM/.env
   cp Agents/.env.example Agents/.env
   ```
4. Añade tu clave API de OpenRouter a ambos archivos `.env`:
   ```
   OPENROUTER_API_KEY=tu_clave_api_real
   ```

## Uso

### Ejecutando el Chat LLM Simple

```
python LLM/main.py
```

Esto iniciará una interfaz de chat básica con el modelo Llama 4 Maverick. La aplicación proporciona una forma sencilla de interactuar con el modelo para conversaciones generales y recuperación de información.

### Ejecutando el Chat con Agentes

```
python Agents/main.py
```

Esto iniciará la versión mejorada de la interfaz de chat que incorpora el agente LlamaIndex ReAct. Esta versión incluye herramientas como la verificación de precios de criptomonedas y demuestra cómo los agentes pueden realizar razonamientos en múltiples pasos para completar tareas.

Ambas aplicaciones iniciarán un servidor Gradio local, típicamente en http://127.0.0.1:7860

## Ejemplos de Consultas

**Para el Chat LLM:**
- "Hola, ¿cómo estás?"
- "¿Qué me puedes decir sobre la inteligencia artificial?"
- "Escribe un poema corto sobre la naturaleza."

**Para el Chat con Agentes:**
- "¿Cuál es el precio actual de bitcoin?"
- "Compara el precio de ethereum y solana"
- "¿Es bitcoin más caro que ethereum en este momento?"
- "¿Qué criptomoneda ha crecido más en las últimas 24 horas?"

## Requisitos

- Python 3.10 o superior
- Una clave API de OpenRouter
- Conexión a internet activa para comunicarse con la API de OpenRouter
- Para la versión de Agentes, acceso a internet para la API de CoinGecko para datos de criptomonedas 