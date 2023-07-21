from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from random import randint



# Iniciando o navegador Chrome
webdriver = webdriver.Chrome()
webdriver.implicitly_wait(10)  # Aguarde até 10 segundos para que os elementos estejam presentes

# Navegando para a página de login do Instagram
webdriver.get('https://www.instagram.com')
sleep(3)

# Preenchendo o formulário de login e realizando login
username_input = webdriver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
password_input = webdriver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
login_button = webdriver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3)')

username_input.send_keys("elder_ribeiro_s")  # Substitua pelo seu nome de usuário do Instagram
password_input.send_keys("elderloucao")  # Substitua pela sua senha do Instagram
login_button.click()
sleep(3)

# Lidar com o diálogo "Salvar informações de login" (se ele aparecer)
try:
    save_login_button = webdriver.find_element(By.CSS_SELECTOR, '.cmbtv')
    save_login_button.click()
except:
    pass

# Lidar com o diálogo "Ativar notificações" (se ele aparecer)
try:
    activate_notifications_button = webdriver.find_element(By.XPATH, "//button[contains(text(), 'Ativar')]")
    activate_notifications_button.click()
except:
    pass

# Navegar para a URL da postagem específica onde você deseja deixar comentários
url_postagem = 'https://www.instagram.com/p/Cu5TnJ7P2jY/'  # Substitua pela URL da postagem desejada
webdriver.get(url_postagem)

comentarios = 0

try:
    for i in range(5):
        sleep(3)
        # Localizando o botão de comentário
        comment_button = webdriver.find_element(By.CLASS_NAME, 'x1lliihq')     
        comment_button.click()
        

        sleep(1)
        
        webdriver.find_element(By.CSS_SELECTOR,'[aria-label="Adicionar um comentário..."]').click()

        campo_comentario = webdriver.find_element(By.CSS_SELECTOR,'[aria-label="Adicionar um comentário..."]')
        
        # Preenchendo o comentário
        campo_comentario.send_keys('Castor!!')

        sleep(3)
        
        # Localizar o botão "Postar" ou "Enviar" no formulário de comentário
        post_button = webdriver.find_element(By.XPATH, '#mount_0_0_7U > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > section > div > form > div > div._am-5 > div')
        
        # Clicar no botão "Postar" ou "Enviar" para enviar o comentário
        post_button.click()

        comentarios += 1
        sleep(randint(3, 5))

        WebDriverWait(webdriver, 10).until(EC.staleness_of(campo_comentario))

        # Aguardar alguns segundos até que o formulário de comentário não esteja mais presente na página
        sleep(10)

except Exception as e:
    print('Ocorreu um erro:', str(e))

print('Qtd de comentários: {} '.format(comentarios))


# Fechando o navegador
webdriver.quit()