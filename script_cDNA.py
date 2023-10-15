import sys


# Verifica se o número de argumentos é correto
if len(sys.argv) != 7:
    print("Uso: python script_CDS.py sequencia_DNA n1 n2 n3 n4 n5 n6")
    sys.exit(1)


# Obtém os argumentos da linha de comando
sequencia_DNA = sys.argv[1]
n1, n2, n3, n4, n5, n6 = sys.argv[2:8]


# Verifica se os argumentos n1-n6 são números inteiros e estão dentro dos limites da sequência de DNA
if not (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit()):
    print("Os argumentos n1-n6 devem ser números inteiros.")
    sys.exit(1)


n1, n2, n3, n4, n5, n6 = int(n1), int(n2), int(n3), int(n4), int(n5), int(n6)


if n1 < 1 or n2 > len(sequencia_DNA) or n3 < 1 or n4 > len(sequencia_DNA) or n5 < 1 or n6 > len(sequencia_DNA):
    print("Os argumentos n1-n6 devem estar dentro dos limites da sequência de DNA.")
    sys.exit(1)


# Função para extrair a sequência CDS
def extrair_CDS(sequencia, inicio, fim):
    return sequencia[inicio - 1:fim]


# Função para verificar se a sequência começa com "ATG"
def verifica_inicio_ATG(sequencia):
    return sequencia.startswith("ATG")


# Função para verificar se a sequência termina com "TAG", "TAA" ou "TGA"
def verifica_fim_codon_de_parada(sequencia):
    return sequencia.endswith("TAG") or sequencia.endswith("TAA") or sequencia.endswith("TGA")


# Extrair as sequências CDS 1, CDS 2 e CDS 3
CDS1 = extrair_CDS(sequencia_DNA, n1, n2)
CDS2 = extrair_CDS(sequencia_DNA, n3, n4)
CDS3 = extrair_CDS(sequencia_DNA, n5, n6)


# Verificar se CDS1 começa com "ATG" e se CDS3 termina com um códon de parada
if verifica_inicio_ATG(CDS1) and verifica_fim_codon_de_parada(CDS3):
    # Concatenar as sequências CDS 1, CDS 2 e CDS 3
    sequencia_final = CDS1 + CDS2 + CDS3
    print("A sequência resultante é: " + sequencia_final)
else:
    print("A sequência não atende aos critérios especificados.")


# Exemplo de uso: python script_CDS.py CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATGTGTGAGCCGACGAAAAGTAAAAGAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA 20 39 47 56 64 98



