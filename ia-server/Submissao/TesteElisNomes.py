import requests
import csv
import os
import simplejson as json
import pandas as pd


url_submissao = 'http://127.0.0.1:5000/servicoELIS/Submeter'
url_pdf = 'http://127.0.0.1:5000/servicoELIS/Arquivo/Processar'
url_pdf_validar = 'http://127.0.0.1:5000/servicoELIS/Arquivo/Validar'
file_path = "D:\\Elis_Execucoes\\Olinda_1a_vara_teste_prescricao"
filename = "submissao_Olinda_13_01.csv"
filename_resultado = "resultado_submissao_Olinda_somente_prescricao.csv"
unidade = "ExecutivosFiscaisOlinda"
file_path_csv = os.path.join(file_path, filename)
file_path_csv_resultado = os.path.join(file_path, filename_resultado)
file_path_cda = os.path.join(file_path, 'PDF')

print(file_path_cda)


def gerar_dados_submissao_modelo():
    global data
    j = json.loads(response.content)
    # Junta e submete ao modelo definitivo
    peticao_inicial_endereco = str(j["PETICAO_INICIAL_ENDERECO"])
    peticao_inicial_endereco = peticao_inicial_endereco.replace("\\", "")
    peticao_inicial_devedor = str(j["PETICAO_INICIAL_DEVEDOR"])
    peticao_inicial_devedor = peticao_inicial_devedor.replace("\"", "\'")
    peticao_inicial_inscricao = str(j["PETICAO_INICIAL_INSCRICAO"])
    peticao_inicial_valor = str(j["PETICAO_INICIAL_VALOR"])
    peticao_inicial_cda_numero = str(j["PETICAO_INICIAL_CDA_NUMERO"])
    peticao_inicial_cda_tipo = str(j["PETICAO_INICIAL_CDA_TIPO"])
    cda_cda_numero = str(j["CDA_CDA_NUMERO"])
    cda_data_inscricao = str(j["CDA_DATA_INSCRICAO"])
    cda_serie_imobiliaria = str(j["CDA_SERIE_IMOBILIARIA"])
    cda_serie_mercantil = str(j["CDA_SERIE_MERCANTIL"])
    cda_serie_estimativa = str(j["CDA_SERIE_ESTIMATIVA"])
    cda_devedor = str(j["CDA_DEVEDOR"])
    cda_devedor = cda_devedor.replace("\"", "\'")
    cda_cpf_cnpj = str(j["CDA_CPF_CNPJ"])
    cda_inscricao = str(j["CDA_INSCRICAO"])
    cda_endereco = str(j["CDA_ENDERECO"])
    cda_endereco = cda_endereco.replace("\\", "")
    qtd_iptu = str(j["QTD_IPTU"])
    qtd_tlp = str(j["QTD_TLP"])
    qtd_outros = str(j["QTD_OUTROS"])
    cda_ano_menor_exercicio_iptu = str(j["CDA_ANO_MENOR_EXERCICIO_IPTU"])
    cda_ano_maior_exercicio_iptu = str(j["CDA_ANO_MAIOR_EXERCICIO_IPTU"])
    cda_ano_menor_exercicio_tlp = str(j["CDA_ANO_MENOR_EXERCICIO_TLP"])
    cda_ano_maior_exercicio_tlp = str(j["CDA_ANO_MAIOR_EXERCICIO_TLP"])
    cda_ano_menor_exercicio_outros = str(j["CDA_ANO_MENOR_EXERCICIO_OUTROS"])
    cda_ano_maior_exercicio_outros = str(j["CDA_ANO_MAIOR_EXERCICIO_OUTROS"])
    data = '''{
                                "chaves": {
                                    "NPU": "''' + npu + '''",
                                    "CDA": "''' + cda + '''"
                                },
                                "consolidar": false,
                                "unidade": "''' + unidade + '''",
                                "entradas": {
                                    "NPU" :  "''' + npu + '''",
                                    "Órgão Julgador" : "''' + orgao_julgador + '''",
                                    "Assunto" : "''' + assunto + '''",
                                    "Classe Judicial" : "''' + classe_judicial + '''",
                                    "Data da Distribuição" : "''' + data_distribuicao + '''",
                                    "Valor da Causa" : ''' + valor_causa.replace(".", "").replace(",", ".") + ''',
                                    "Executado" : "''' + executado + '''",
                                    "CPF/CNPJ do Executado" : "''' + cpf_cnpj_executado + '''",
                                    "CDA" : "''' + cda + '''",
                                    "Tarefa" : "''' + tarefa + '''",
                                    "PETICAO_INICIAL_ENDERECO": "''' + peticao_inicial_endereco + '''",
                                    "PETICAO_INICIAL_DEVEDOR": "''' + peticao_inicial_devedor + '''",
                                    "PETICAO_INICIAL_INSCRICAO": "''' + peticao_inicial_inscricao + '''",
                                    "PETICAO_INICIAL_VALOR": ''' + peticao_inicial_valor.replace(".", "").replace(",",
                                                                                                                  ".") + ''',
                                    "PETICAO_INICIAL_CDA_NUMERO": "''' + peticao_inicial_cda_numero + '''",
                                    "PETICAO_INICIAL_CDA_TIPO": "''' + peticao_inicial_cda_tipo + '''",
                                    "CDA_CDA_NUMERO": "''' + cda_cda_numero + '''",
                                    "CDA_DATA_INSCRICAO": "''' + cda_data_inscricao + '''",
                                    "CDA_SERIE_IMOBILIARIA": ''' + cda_serie_imobiliaria + ''',
                                    "CDA_SERIE_MERCANTIL": ''' + cda_serie_mercantil + ''',
                                    "CDA_SERIE_ESTIMATIVA": ''' + cda_serie_estimativa + ''',
                                    "CDA_DEVEDOR": "''' + cda_devedor + '''",
                                    "CDA_CPF_CNPJ": "''' + cda_cpf_cnpj + '''",
                                    "CDA_INSCRICAO": "''' + cda_inscricao + '''",
                                    "CDA_ENDERECO": "''' + cda_endereco + '''",
                                    "QTD_IPTU": ''' + qtd_iptu + ''',
                                    "QTD_TLP": ''' + qtd_tlp + ''',
                                    "QTD_OUTROS": ''' + qtd_outros + ''',
                                    "CDA_ANO_MENOR_EXERCICIO_IPTU": ''' + cda_ano_menor_exercicio_iptu + ''',
                                    "CDA_ANO_MAIOR_EXERCICIO_IPTU": ''' + cda_ano_maior_exercicio_iptu + ''',
                                    "CDA_ANO_MENOR_EXERCICIO_TLP": ''' + cda_ano_menor_exercicio_tlp + ''',
                                    "CDA_ANO_MAIOR_EXERCICIO_TLP": ''' + cda_ano_maior_exercicio_tlp + ''',
                                    "CDA_ANO_MENOR_EXERCICIO_OUTROS": ''' + cda_ano_menor_exercicio_outros + ''',
                                    "CDA_ANO_MAIOR_EXERCICIO_OUTROS": ''' + cda_ano_maior_exercicio_outros + '''
                                }
                            }'''


with open(file_path_csv) as csv_file:
    print(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    session = requests.Session()
    session.trust_env = False
    colunas = {"NPU", "CDA", "Previsao"}
    resultado_final = pd.DataFrame(columns=colunas)
    total_cda_diferente_pje = 0
    total_cda_com_erro = 0
    total_justica_federal = 0
    total_espolio = 0
    total_fazenda_estadual = 0
    total_prescricao = 0
    total_ok = 0
    npu_cda_nao_localizadas = []
    npu_cda_vazias = []
    npu_cda_invalidas = []
    dados = { 'unidade': unidade }
    for row in csv_reader:
        if line_count > 0:
            #resgata os valores do CSV/Pje
            npu = row[0]
            orgao_julgador = row[1]
            assunto = row[2]
            classe_judicial = row[3]
            data_distribuicao = row[4]
            valor_causa = row[5]
            executado = row[6]
            cpf_cnpj_executado = row[7]
            cda = row[8]
            tarefa = row[9]
            suc_caixa = row[10]
            sucesso_envio_cda = True
            #Busca o arquivo da CDA
            arquivo_cda = cda + ".pdf"
            filename_pdf = os.path.join(file_path_cda, arquivo_cda)
            #print(filename_pdf)
            arquivo_valido = True
            arquivo_vazio = False
            arquivo_inexistente = False
            if cda == "":
                npu_cda_vazias.append(npu)
                arquivo_vazio = True
                print("CDA do NPU " + npu + " vazia")

            #Valida o pdf para saber se é uma CDA válida
            if os.path.isfile(filename_pdf):
                arquivo_inexistente = False
            else:
                npu_cda_nao_localizadas.append(npu)
                print("CDA " + cda + " da NPU " + npu + " inexistente")
                arquivo_inexistente = True

            if (not arquivo_vazio) and (not arquivo_inexistente):
                tentativas_validacao_max = 3
                tentativa_atual = 0
                sucesso_processo_validacao = False
                while tentativa_atual < tentativas_validacao_max and not sucesso_processo_validacao:
                    try:
                        tentativa_atual += 1
                        # Envia o arquivo
                        files = {'file': open(filename_pdf, 'rb')}
                        response = session.post(url_pdf_validar, files=files, data=dados)
                        #print(response.content)
                        retorno_validacao = json.loads(response.content)
                        if not retorno_validacao["Valido"]:
                            arquivo_valido = False
                        sucesso_processo_validacao = True
                    except:
                        #arquivo_valido = False
                        print("Falha na tentativa " + str(tentativa_atual))

                if not sucesso_processo_validacao:
                    arquivo_valido = False

                if not arquivo_valido:
                    print("Arquivo " + filename_pdf + " invalido")
                    npu_cda_invalidas.append(npu)
                else:
                    tentativas_submissao_max = 3
                    tentativa_atual = 0
                    sucesso_processo_submissao = False
                    while tentativa_atual < tentativas_submissao_max and not sucesso_processo_submissao:
                        tentativa_atual += 1
                        try:
                            files = {'file': open(filename_pdf, 'rb')}
                            response = session.post(url_pdf, files=files, data=dados)
                        except:
                            sucesso_envio_cda = False

                        arquivo_cda_ajustado = ""
                        if not sucesso_envio_cda:
                            sucesso_envio_cda = True
                            arquivo_cda = arquivo_cda.replace(".", "").replace("-","").replace("/","")
                            arquivo_cda_ajustado = arquivo_cda[:1] + "." + arquivo_cda[1:3] + "." + arquivo_cda[3:-4] + "-" + \
                                               arquivo_cda[-4:-3] + "." + arquivo_cda[-3:]
                            filename_pdf = os.path.join(file_path_cda, arquivo_cda_ajustado)
                            try:
                                files = {'file': open(filename_pdf, 'rb')}
                                response = session.post(url_pdf, files=files, data=dados)
                            except:
                                sucesso_envio_cda = False

                        if sucesso_envio_cda:
                            sucesso_processo_submissao = True


                    if not sucesso_processo_submissao and response.content != "":
                        sucesso_envio_cda = False

                    if sucesso_envio_cda:
                        try:
                            #gerar_dados_submissao_modelo()

                            #Imprime CDA, NPU e data
                            j = json.loads(response.content)
                            # Junta e submete ao modelo definitivo
                            #cda_ano_menor_exercicio_iptu = str(j["CDA_ANO_MENOR_EXERCICIO_IPTU"])
                            #cda_ano_maior_exercicio_iptu = str(j["CDA_ANO_MAIOR_EXERCICIO_IPTU"])
                            #cda_ano_menor_exercicio_tlp = str(j["CDA_ANO_MENOR_EXERCICIO_TLP"])
                            #cda_ano_maior_exercicio_tlp = str(j["CDA_ANO_MAIOR_EXERCICIO_TLP"])
                            #cda_ano_menor_exercicio_outros = str(j["CDA_ANO_MENOR_EXERCICIO_OUTROS"])
                            #cda_ano_maior_exercicio_outros = str(j["CDA_ANO_MAIOR_EXERCICIO_OUTROS"])
                            devedor_peticao_inicial = str(j["PETICAO_INICIAL_DEVEDOR"])
                            devedor_cda = str(j["PETICAO_INICIAL_DEVEDOR"])
                            executado

                            executado_igual_cda = 0
                            if executado == devedor_cda:
                                executado_igual_cda = 1
                            executado_igual_peticao = 0
                            if executado == devedor_peticao_inicial:
                                executado_igual_peticao = 1
                            cda_igual_peticao = 0
                            if devedor_cda == devedor_peticao_inicial:
                                cda_igual_peticao = 1


                            #npu_resultados = str(chaves["NPU"])
                            #cda_resultados = str(chaves["CDA"])

                            print(npu + "|" + cda + "|DPI:" + devedor_peticao_inicial +
                                  "|DCDA:" + devedor_cda + "|EXEC:" + executado +
                                  "|EIP:" + str(executado_igual_peticao) + "|EICDA:" +
                                  str(executado_igual_cda) + "|CDAIP:" + str(cda_igual_peticao))
                        except Exception as ex:
                            print("Arquivo " + filename_pdf + " invalido")
                            npu_cda_invalidas.append(npu)
                            print(ex)

        line_count += 1
        #A cada 10 processos guarda a tabela


    print("Fim")
    resultado_final = resultado_final.sort_values(by=["NPU"])
    resultado_final.to_csv(file_path_csv_resultado, header=True, columns=["NPU", "CDA", "Previsao"], index=False)





