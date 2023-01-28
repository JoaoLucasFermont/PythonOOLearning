#url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
url = '                   '

#Sanitização da URL
url = url.strip()

#validação URL

if url == '':
    raise ValueError('A Url está vazia')

#separa paramentros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

#busca valor no parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
ecomercial = url_parametros.find('&', indice_valor)
if ecomercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:ecomercial]

print(valor)