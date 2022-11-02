from playwright.sync_api import sync_playwright, expect
import csv

with sync_playwright() as p:
    navegador = p.chromium.launch(args=['--start-maximized'], headless=False, slow_mo=110)#headless

    #vai abrir o documento csv
    with open("casos.csv", "r", encoding='utf-8') as casos_teste:

        casos = csv.reader(casos_teste)
        next(casos)
        qntd_casos = 0
        casos_aprovados = 0
        lista_casos_reprovados = []

        #loop para todos os casos de teste
        for caso in casos:
            qntd_casos += 1

            nome_time = caso[0]
            mat1 = caso[1]
            mat2 = caso[2]
            mat3 = caso[3]
            email = caso[4]
            nivel = caso[5]
            resultado_esperado = caso[6]

            pagina = navegador.new_page(no_viewport=True)
            pagina.goto("http://127.0.0.1:5000/")

            if(qntd_casos == 1):
                pagina.wait_for_timeout(2000)

            #bloco para preencher os dados
            pagina.type('xpath=//*[@id="nome_time"]', nome_time)
            pagina.type('xpath=//*[@id="primeiro_int"]', mat1)
            pagina.type('xpath=//*[@id="segundo_int"]', mat2)
            pagina.type('xpath=//*[@id="terceiro_int"]', mat3)
            pagina.type('xpath=//*[@id="email"]', email)
            try:
                pagina.get_by_text(nivel).click()
            except:
                None

            #clicou para submeter o fomulário
            pagina.locator('xpath=//*[@id="formulario"]/button').click()

            #localizando o parágrafo da resposta da incrição
            resultado = pagina.locator("#resultado")
            texto_resultado = pagina.locator("#resultado").text_content()

            try:#vai tentar ver se o resutado exibido na página bate com o resultado esperado do caso de teste
                expect(resultado).to_have_text(resultado_esperado)
                casos_aprovados += 1
                print("Teste Aprovado")
            except:
                lista_casos_reprovados.append("Caso " + str(qntd_casos) + " reprovado. Mensagem exibida foi: " + texto_resultado)
                print("Teste Reprovado")

            pagina.wait_for_timeout(3000)
            pagina.close()

    porcentagem_sucesso = casos_aprovados/qntd_casos * 100
    arquivo_txt = open("resultado.txt","w",encoding='utf-8')
    arquivo_txt.write("Casos aprovados: " + str(round(porcentagem_sucesso, 2)) + "%\n")
    arquivo_txt.write("Casos reprovados: " + str(round(100.00 - porcentagem_sucesso, 2)) + "%\n\n")
    for caso in lista_casos_reprovados:
        arquivo_txt.write(caso + "\n")
    arquivo_txt.close()