# url ="bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = " "

#Sanitização da URL
url = url.strip()

if url == "":
    raise ValueError("A URL está vazia")

#separa base e os parâmetros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]#se não colocar valor no começo ou no final no fatiamenet é entedido como, respectivamenet, primeiro e ulimto valor.
print(url_parametros)


# Busca o valor de um parâmetro
parametro_busca = "moedaDestino"
indice_paramentro = url_parametros.find(parametro_busca)
print(indice_paramentro)
indice_valor = indice_paramentro + len(parametro_busca) +1
indice_e_comercial = url_parametros.find("&", indice_valor)
if( indice_e_comercial == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


