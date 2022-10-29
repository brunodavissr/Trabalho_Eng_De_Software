from queue import Full
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(args=['--start-maximized'], headless=False)#headless
    #context = navegador.new_context(record_video_dir="videos/",record_video_size={"width": 1366, "height": 768})

    pagina = navegador.new_page(no_viewport=True)
    pagina.goto("file:///C:/Users/BrunoD/Desktop/PLAYWRIGHT_TESTE/site/pagina.html")
    
    pagina.wait_for_timeout(2000)
    pagina.type('xpath=//*[@id="nome_time"]',"Vasco Da Gama", delay=100)
    pagina.wait_for_timeout(2000)
    pagina.type('xpath=//*[@id="primeiro_int"]',"Bruno", delay=100)
    pagina.wait_for_timeout(1000)
    pagina.type('xpath=//*[@id="segundo_int"]',"Raissa", delay=100)
    pagina.wait_for_timeout(1000)
    pagina.type('xpath=//*[@id="terceiro_int"]',"Eugênio", delay=100)
    pagina.wait_for_timeout(1000)
    pagina.type('xpath=//*[@id="email"]',"vasquinho123@gmail.com", delay=100)
    pagina.wait_for_timeout(1000)
    pagina.locator('xpath=//*[@id="radio-avancado"]').click()
    pagina.wait_for_timeout(1000)
    pagina.locator('xpath=//*[@id="formulario"]/button').click()
    pagina.locator('xpath=/html/body/footer/p[2]').scroll_into_view_if_needed()
    # pagina.screenshot(path="videos/screenshot.png", full_page=True)
    pagina.wait_for_timeout(2000)
    # context.close()
    navegador.close()