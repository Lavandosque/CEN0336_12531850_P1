!/bin/bash
echo "Diretorio atual: $(pwd)"

ls -l ~ > lista_HOME.txt

echo "Lista de conteudo de home salvo em lista_HOME.txt"

data_atual=$(date)
echo "Data atual: $data_atual"

