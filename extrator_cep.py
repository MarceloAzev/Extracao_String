endereco = "Rua da Flores 72 aparatamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-140"

import re # Regular expression -- RegEX
#5 digitios + hifen(opcional) + 3 digitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #[valores]{quantidade}
busca = padrao.search(endereco) #match

if busca:
    cep = busca.group()
    print(cep)