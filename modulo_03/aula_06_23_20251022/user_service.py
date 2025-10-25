# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:

    def __init__(self):
        self.user_model=UserModel()

        """
        crie um atributo que receberá a UserModel como composição
        """

    def _safe_user_data(self, user) -> dict | None:

        if user:       
            return {
                'id':user['id'],
                'email':user['email'],
                'nome_completo':user['nome_completo'],
                'perfil_acesso':user['perfil_acesso'],
                'data_criacao':user['data_criacao'],
                'data_atualizacao':user['data_atualizacao']
        }      
        else:
            return None
        
        """
        este é um método privado que recebe um usuarios do banco.
        verifique se o usuários existe e então retorne ele sem a sua senha
        caso ele ão exista retorne None
        """

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
       

        if current_user_profile == 'Diretoria':
            return True
        elif target_user_id == 0:
            return False
        elif action == 'edit_self':
            return current_user_id == target_user_id
        else:
            return False


        """
        Método que verifica o perfil do usuários, se for Diretoria retorne true
        Se não tiver target_user_id retorn false
        Se  action == "edit_self" retorne current_user_id == target_user_id
        No geral retorn false
        """

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        
        # senha=input("entre com a senha")
        # email=input("entre com o email")
        # nome_completo=input("digite seu nome comprelto")
        
        if len(senha)<8:
            print("Erro! A senha deve ter no mínimo 8 caracteres")
            return False
        if len(email)<10 or '@' not in email or ".com" not in email:
            print("Erro! Email inválido")
            return False
        else:
            cripsenha=hash_senha(senha)
            return self.user_model.create_user(cripsenha,email,nome_completo,perfil)
        
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorn o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """
        usuario=self.user_model.find_user_by_email(email)
        if verificar_senha(senha,usuario['senha_hash']):
            return self._safe_user_data(usuario),"Login bem sucedido."
        else:
            return None,"Acesso Negado"       
       

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        """
        Método para atualizar usuários.
        Chame o método privado _is_authorized, se o retorno for false, retorne false e acesso negado
        Confira as chaves em new_data (senha, nome_completo, email), se pelo menos um desses campos,
        Caso não haja nenhum valor a ser atualizado, encerre a função com False e mensagem de erro.
        Caso contrátio, chame o método da UserModel update_user_by_id passando o id e o new data
        """
        if not self._is_authorized(current_user_id,current_user_profile,target_user_id,'edit_self'):
            return False,"Acesso negado!"
        if new_data['senha'] != None or new_data['nome_completo'] != None or new_data['email'] != None:
            return self.user_model.update_user_by_id(target_user_id,new_data)
        else:
            return False,"Nenhum valor a ser atualizado."

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Método para deletar usuarios.
        So é permitido deletar usuarios se o current_user_profile for Diretoria.
        Caso não seja retorn false e a mensagem de acesso negado
        Senão chame o método delete_user_by_id, passando o id do usuários
        """

        if current_user_profile=='Diretoria':
            # "Usuário deletado como sucesso."
            return self.user_model.delete_user_by_id(user_id)
        else:
            # print("Nível de autorização não permite deletar o usuário.")
            # print("Acesso negado!")
            return False,"Nível de autorização não permite deletar o usuário."


    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Método para pegar um usuarios pelo id
        Retorne o usuarios apos passar pelo método _safe_user_data
        """
        usuario=self.user_model.find_user_by_id(user_id)

        return self._safe_user_data(usuario)
        


    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        retorne todos os usuáriso apos passar pelo método _safe_user_data
        """
        usuarios=self.user_model.get_all_users
        usuarios_tratados=[]
        for usuario in usuarios:
            usuarios_tratados.append(self._safe_user_data(usuario))
         
        return usuarios_tratados        
