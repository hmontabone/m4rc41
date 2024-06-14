from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Ruta del ChromeDriver
chrome_driver_path = r'C:\\Users\\hmont\\Downloads\\proyecto-automacion\\chrome-win32\\chrome.exe'
service = Service(executable_path=chrome_driver_path)

print("Iniciando el WebDriver...")

# Inicializar el WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navegar a la página web
    print("Navegando a Google...")
    driver.get("http://www.google.com")

    # Confirmar que la URL ha sido cargada
    print(f"URL actual: {driver.current_url}")

    # Esperar para observar el resultado
    time.sleep(5)  # Ajustar este tiempo según sea necesario

finally:
    # Cerrar el navegador
    print("Cerrando el navegador...")
    driver.quit()
