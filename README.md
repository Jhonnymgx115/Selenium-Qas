# 🚀 Automatización de Pruebas con Selenium IDE y Python

## 📌 Descripción del Proyecto
Este repositorio contiene una práctica de automatización de pruebas utilizando **Selenium IDE** con la extensión de **Chrome WebDriver** y **Selenium en Python**. La prueba automatiza una búsqueda en **SteamDB**, verificando que el título de la página coincida con el juego buscado.

---

## 🛠 Instalación y Configuración

### 🔹 Instalación de Selenium IDE
Para ejecutar pruebas en **Selenium IDE**, sigue estos pasos:

1. Instala la extensión de **Selenium IDE** en [Chrome Web Store](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd).
2. Abre **Selenium IDE** desde el navegador y carga el archivo `.side` de este proyecto.

### 🔹 Instalación de Selenium en Python
Para ejecutar pruebas en **Python**, necesitas:

```bash
pip install selenium webdriver-manager
```
Además, asegúrate de tener Google Chrome instalado.

## 📁 Archivos del Proyecto
📝 Archivo de Configuración (.side)
El archivo .side contiene: ✅ Definición de pruebas automatizadas
✅ Estructura del test suite
✅ Acciones en la web de SteamDB

### Configuración:

Abre Selenium IDE y carga el archivo .side.

Ejecuta la prueba desde el entorno de Selenium IDE.

## 🐍 Archivo Python
Este archivo ejecuta la misma prueba, pero usando Selenium en Python:

```bash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://steamdb.info/")

search_box = driver.find_element(By.CSS_SELECTOR, "header input[type='search']")
search_box.send_keys("Cyberpunk 2077")
search_box.send_keys(Keys.ENTER)

assert "Cyberpunk 2077 · SteamDB" in driver.title

driver.quit()
```

## 🚀 Implementación de Pruebas Futuras
📌 En Selenium IDE
Abre el entorno y graba una nueva prueba.

Guarda el archivo .side con los nuevos cambios.

📌 En Python
Agrega nuevas funciones con find_element y assert.

Ejecuta el script para validar los cambios.

📌 ¡Listo para automatizar más pruebas en SteamDB! 🔥
