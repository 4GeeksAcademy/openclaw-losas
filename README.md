# Verificar la IA mediante LiteLLM

Este repositorio contiene una prueba mínima que envía una petición a una API compatible con LiteLLM y muestra la respuesta. No modifica OpenClaw ni incluye credenciales.

> **Importante:** la prueba confirma que el endpoint configurado responde para el modelo indicado. Por sí sola no demuestra que el modelo se ejecute físicamente en el mismo equipo: LiteLLM también puede reenviar peticiones a un proveedor remoto. Para demostrar ejecución local, el endpoint debe apuntar a un servidor local que use un modelo local.

## Requisitos

- Python 3.8 o superior (no requiere paquetes externos).
- LiteLLM Proxy activo o un endpoint compatible con la API Chat Completions.
- El modelo `gpt-6-luna` disponible en ese endpoint.

## Ejecutar

Por defecto, el script consulta `http://localhost:4000/v1/chat/completions` con el modelo `gpt-6-luna`:

```bash
python3 test_litellm.py
```

Si el proxy requiere autenticación, define la clave en el entorno; no la escribas en el código ni la subas al repositorio:

```bash
export LITELLM_API_KEY='tu-clave'
python3 test_litellm.py
```

Para usar otra dirección o nombre de modelo:

```bash
LITELLM_BASE_URL='http://localhost:4000' LITELLM_MODEL='gpt-6-luna' python3 test_litellm.py
```

La prueba envía el mensaje `Reply with exactly: LOCAL AI OK` e imprime la respuesta. Si falla, comprueba que el servicio está activo, que la URL no incluya `/v1` al final y que el modelo esté configurado en LiteLLM.
