import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL base de la variable de entorno y construir la URL del endpoint
API_BASE_URL = os.getenv("API_BASE_URL")
POSTS_URL = f"{API_BASE_URL}/posts"

def obtener_posts_usuario_3():
    # Parámetros para filtrar por userId=3 en el lado del servidor
    params = {"userId": 3}      
    
    try:
        # Pasamos los parámetros a la petición GET
        response = requests.get(POSTS_URL, params=params)
        
        print(f"Status Code de la petición: {response.status_code}")
        
        response.raise_for_status()
        
        posts = response.json()
        print("\n--- Posts del usuario con ID 3 ---")
        for post in posts:
            # Ya no es necesario filtrar aquí, la API ya nos dio solo los posts correctos
            print(f"Título: {post['title']}")
            print("-" * 20)
                
    except requests.exceptions.HTTPError as err:
        print(f"Error de HTTP: {err}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# OBSERVACIÓN 1: Función para POST
def crear_nuevo_post():
    data = {
        "title": "Post de prueba desde Python",
        "body": "Este post fue creado automáticamente con requests",
        "userId": 3
    }
    
    try:
        response = requests.post(POSTS_URL, json=data)
        print(f"\nStatus Code de la creación (POST): {response.status_code}")
        response.raise_for_status()
        print("¡Post creado con éxito!")
        print(f"Respuesta del servidor: {response.json()}")
    except Exception as e:
        print(f"Error al crear el post: {e}")

# Ejecutamos ambas funciones
obtener_posts_usuario_3()
crear_nuevo_post()