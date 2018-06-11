from __future__ import print_function
import os
import glob
import re


with open('RISCV.txt') as file:
    linhas = file.readlines()




for arquivo in glob.glob('mips snippets/*.sublime-snippet'):
    print('Removendo:', arquivo)
    os.remove(arquivo)



for linha in linhas:
    print(linha)
    pedacos = re.split(r'\s{2,}', linha)



    funcName = pedacos[0]
    CDATA = pedacos[1]
    comentario = pedacos[2].strip()




    content = '''<snippet>
    <description>'''+comentario+'''</description>
    <content><![CDATA['''+CDATA+''']]></content>
    <tabTrigger>'''+funcName+'''</tabTrigger>
    <scope>source.riscv</scope>
</snippet>'''



    fileDest = 'mips snippets/'+funcName+'.sublime-snippet'
    with open(fileDest, 'w') as file:
        file.write(content)