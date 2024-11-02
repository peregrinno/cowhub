import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# Configuração de conexão
DATABASE_URL = "postgresql://postgres:postgres@localhost/coworking_db"
engine = create_engine(DATABASE_URL)

# Base para criação de tabelas
Base = declarative_base()

# Difinição da tabela usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

#Criar a sessão para inserir os dados
Session = sessionmaker(bind=engine)
session = Session()

def cria_usuario(session, nome, email, senha):
    senha_critpo = hash_password(senha)

    novo_usuario = Usuario(
        name=nome,
        email=email,
        password=senha_critpo
    )
    
    #Adicionando e salvando o usuario no banco de dados
    session.add(novo_usuario) # Aqui ainda não foi confirmado
    session.commit() # Aqui eu confirmo

    print("Usuário criado com sucesso!")


def buscar_usuario(session, usuario_id):
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    return usuario

cria_usuario(session, "Luan Araujo", "joseluan74@gmail.com", "12345Aa@")
user = buscar_usuario(session, 2)
print(f"# {user.id} - Nome: {user.name} - Email: {user.email}")



session.close()