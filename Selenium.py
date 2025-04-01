from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SteamDBTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://steamdb.info/")

    def test_page_title(self):
        """Prueba 1: Validar el título de la página principal"""
        assert "Steam Database" in self.driver.title, "El título de la página no es el esperado."

    def test_search_game(self):
        """Prueba 2: Buscar un juego y verificar resultados"""
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Counter-Strike 2")
        search_box.send_keys(Keys.RETURN)

        # Esperar a que aparezca el primer resultado
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app")))
        
        first_result = self.driver.find_element(By.CLASS_NAME, "app").text
        assert "Counter-Strike 2" in first_result, "El juego no apareció en los resultados."

    def test_check_price(self):
        """Prueba 3: Verificar la información de precios en la página del juego"""
        self.test_search_game()  # Primero busca el juego
        self.driver.find_element(By.CLASS_NAME, "app").click()  # Click en el primer resultado
        
        # Esperar que cargue la información de precios
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price-container")))

        price_info = self.driver.find_element(By.CLASS_NAME, "price-container").text
        assert price_info, "No se encontró información de precio."

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = SteamDBTest()
    test.test_page_title()
    test.test_search_game()
    test.test_check_price()
    test.close()
