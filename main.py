from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Ruta del ChromeDriver
chrome_driver_path = r'C:\\Users\\hmont\\Downloads\\proyecto-automacion\\chromedriver-win32\\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

print("Iniciando el WebDriver...")

# Inicializar el WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navegar a la primera página web
    print("Navegando a la página de inicio de sesión...")
    driver.get("https://controltopcaren.izytimecontrol.com/#/login")

    # Esperar unos segundos para que la página cargue completamente
    time.sleep(5)  # Ajustar este tiempo según sea necesario

    # Navegar a la segunda página web
    print("Navegando a la página de auto-consulta...")
    driver.get("https://controltopcaren.izytimecontrol.com/#/auto-consulta/login")

    # Confirmar que la URL ha sido cargada
    print(f"URL actual: {driver.current_url}")

    # Esperar a que la página cargue completamente
    time.sleep(5)  # Ajustar este tiempo según sea necesario

    # Encontrar y llenar el campo de usuario (RUT)
    try:
        print("Buscando el campo de usuario...")
        username_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="rut"]')
        print("Campo de usuario encontrado, ingresando datos...")
        username_input.send_keys("17.337.146-2")
    except Exception as e:
        print(f"Error al encontrar el campo de usuario: {e}")

    # Encontrar y llenar el campo de contraseña
    try:
        print("Buscando el campo de contraseña...")
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        print("Campo de contraseña encontrado, ingresando datos...")
        password_input.send_keys("7146")
        password_input.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Error al encontrar el campo de contraseña: {e}")

    # Esperar a que la página cargue después de iniciar sesión
    time.sleep(5)  # Ajustar este tiempo según sea necesario

    # Encontrar y activar el botón de ingreso
    try:
        print("Buscando el botón de ingreso...")
        activate_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        print("Botón de ingreso encontrado, haciendo clic...")
        activate_button.click()
    except Exception as e:
        print(f"Error al encontrar el botón de ingreso: {e}")

    # Esperar para asegurarse de que la acción se complete
    time.sleep(5)

    # Navegar a la URL adicional
    print("Navegando a la página de marcas web...")
    driver.get("https://controltopcaren.izytimecontrol.com/#/auto-consulta/web-marks")
    
    
    

    # Confirmar que la URL ha sido cargada
    print(f"URL actual: {driver.current_url}")

    # Esperar a que la página cargue completamente
    time.sleep(5)  # Ajustar este tiempo según sea necesario

    # Aquí puedes agregar las acciones adicionales que necesitas realizar en esta página
    
    try:
        print("Buscando el campo de contraseña...")
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        print("Campo de contraseña encontrado, ingresando datos...")
        password_input.send_keys("7146")
        password_input.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Error al encontrar el campo de contraseña: {e}")
    
    
    
    # Ejemplo: encontrar un elemento y hacer clic en él

    # Esperar para asegurarse de que la acción se complete
    time.sleep(5)

finally:
    # Cerrar el navegador
    print("Cerrando el navegador...")
    driver.quit()
