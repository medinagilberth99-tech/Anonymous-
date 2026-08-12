import sys
import time
import socket
import json
import urllib.request
import urllib.error

def animar_texto(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

class JarvisAnonymous:
    def __init__(self):
        self.nombre = "Anonymous"
        self.hermano = "Nymos"
        self.notas = []
        self.api_key = "AQ.Ab8RN6LpO6Rx1W29atL7rl5jRlW-iSpTas4_WEtgL7TBWRcqkw"
        
    def consultar_gemini(self, prompt_usuario):
        # Usamos la API REST directa de Google sin dependencias complejas
        url = f"https://generativelanguage.googleapis.com/v1models/gemini-3.5-flash:generateContent?key={self.api_key}"
        # URL alternativa si el modelo varía:
        url_alt = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={self.api_key}"
        
        prompt_sistema = "Eres Anonymous, un asistente de hacking ético e inteligencia artificial, hermano de Nymos. Le hablas a tu creador Gilberth de forma directa, técnica y leal."
        texto_completo = f"{prompt_sistema}\n\nPetición de Gilberth: {prompt_usuario}"
        
        data = {
            "contents": [{
                "parts": [{"text": texto_completo}]
            }]
        }
        
        req = urllib.request.Request(
            url_alt,
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                resultado = json.loads(response.read().decode('utf-8'))
                texto_respuesta = resultado['candidates'][0]['content']['parts'][0]['text']
                return texto_respuesta
        except Exception as e:
            return f"[!] Error de enlace con el núcleo neuronal: {e}"

    def iniciar(self):
        print("========================================")
        animar_texto(f"[*] Inicializando sistemas de {self.nombre}...")
        animar_texto(f"[*] Sincronizando protocolos con {self.hermano}...")
        print("========================================")
        animar_texto(f"Hola Gilberth. Sistemas en línea. Soy {self.nombre}.")
        
        while True:
            print("\n----------------------------------------")
            comando = input("Anonymous@Core:~$ ").strip()
            
            if not comando:
                continue
                
            cmd_lower = comando.lower()
            
            if cmd_lower == "salir" or cmd_lower == "exit":
                animar_texto(f"[*] Desconectando protocolos. Hasta luego, creador.")
                break
                
            elif cmd_lower == "estado":
                animar_texto(f"[*] Todos los sistemas operando al 100%. Enlace con {self.hermano} estable.")
                
            elif cmd_lower == "ayuda":
                print("\n[ Comandos Disponibles ]")
                print(" - estado     : Revisa el estado del núcleo")
                print(" - escanear   : Simula un análisis de puertos y red")
                print(" - mi-ip      : Muestra información de red local")
                print(" - nota <txt> : Guarda una nota rápida")
                print(" - ver-notas  : Muestra las notas guardadas")
                print(" - ayuda      : Muestra este menú")
                print(" - salir      : Cierra el asistente")
                print(" (Cualquier otra frase será procesada por tu IA)")
                
            elif cmd_lower == "escanear":
                animar_texto("[*] Iniciando barrido de puertos en localhost...")
                time.sleep(1)
                print("[+] Puerto 21 (FTP): Cerrado")
                print("[+] Puerto 22 (SSH): Abierto (Seguro)")
                print("[+] Puerto 80 (HTTP): Abierto")
                animar_texto("[*] Barrido completado sin anomalías detectadas.")
                
            elif cmd_lower == "mi-ip":
                try:
                    hostname = socket.gethostname()
                    ip_local = socket.gethostbyname(hostname)
                    animar_texto(f"[*] Hostname: {hostname}")
                    animar_texto(f"[*] IP Local asignada: {ip_local}")
                except Exception as e:
                    animar_texto(f"[!] Error al obtener la red: {e}")
                    
            elif cmd_lower.startswith("nota "):
                contenido_nota = comando[5:]
                self.notas.append(contenido_nota)
                animar_texto(f"[*] Nota guardada en la memoria temporal de {self.nombre}.")
                
            elif cmd_lower == "ver-notas":
                if not self.notas:
                    animar_texto("[*] No hay notas registradas en el sistema.")
                else:
                    print("\n[ Notas Almacenadas ]")
                    for i, n in enumerate(self.notas, 1):
                        print(f" {i}. {n}")
            else:
                animar_texto(f"[*] Consultando al núcleo neuronal...")
                respuesta_ia = self.consultar_gemini(comando)
                print(f"\n{respuesta_ia}")

if __name__ == "__main__":
    ai = JarvisAnonymous()
    ai.iniciar()
