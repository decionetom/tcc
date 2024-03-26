arquivo_entrada = './landing/landing.xml'
arquivo_saida = './trusted/saida.txt'
import re


def xml_file_to_string(filename):
    with open(filename, 'r', encoding="utf8",) as f:
        xml_content = f.read()
    return xml_content

def remover_tags(texto):
    # Define a expressão regular para encontrar texto entre '</' e '>'
    padrao = re.compile(r'</.*?>')
    # Substitui o texto correspondente pelo vazio
    texto_sem_tags = re.sub(padrao, '', texto)
    return texto_sem_tags

def save_string_to_txt(content, filename):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"String salva com sucesso no arquivo {filename}!")

texto = remover_tags(xml_file_to_string(arquivo_entrada))

save_string_to_txt(texto, arquivo_saida)
print(texto)


