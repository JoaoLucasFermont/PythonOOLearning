import re

endereco = "rua altinopolis, 1512 - jd Belval, Osasco- SP 06643-191"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)