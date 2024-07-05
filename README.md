
Criando Ambiente Python:
python3 -m venv venv
win

.\venv\Scripts\activate 

Mac Linux
source ./venv/bin/activate

Instalando Dependências:
pip install flask
pip install SQLALchemy
pip install Flask-SQLAlchemy
pip install Flask-MySQL 
pip install PyMySQL
mysql-connector-python

ou 
Instalando Dependências:
pip install -r requiriments.txt

Rodar o app
flask --app init run

Criar tabela no banco
CREATE TABLE `cars` (
  `id` int NOT NULL,
  `brand` varchar(30) NOT NULL,
  `model` varchar(30) NOT NULL,
  `price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;


ou

def create_table():
    try:
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(255) NOT NULL,
                description TEXT
            )
            '''
        )
        mysql.commit()
        cur.close()
    except Exception as e:
        print("Error while creating table",e)