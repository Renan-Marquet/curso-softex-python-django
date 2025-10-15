from user_model import UserModel
from blog_model import BlogModel


def display_menu():
    """Exibe o menu de opções."""
    print("\n---- Gerenciador de Usuários ---------- Gerenciador de Postagem ---------")
    print("1. Cadastrar novo usuário          7. Cadastrar nova Postagem")
    print("2. Buscar usuário por ID           8. Buscar Postagem por ID da postagem")
    print("3. Atualizar usuário               9. Buscar Postagem por ID do usuário")
    print("4. Deletar usuário                10. Atualizar Postagem")
    print("5. Listar todos os usuários       11. Deletar Postagem")
    print("6. ou  13. Sair                   12. Listar todos as postagenss")
    print("-------------------------------------------------------------------------")
  

def main():
    """Função principal do programa."""
    user_model = UserModel()
    blog_model = BlogModel()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            print("\n--- Cadastro de Usuário ---")
            senha = input("Senha: ")
            email = input("E-mail: ")
            user_model.create_user(senha, email)

        elif choice == "2":
            print("\n--- Buscar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user = user_model.find_user_by_id(user_id)
                if user:
                    print("\nUsuário encontrado:")
                    print(f"ID: {user['user_id']}")
                    print(f"E-mail: {user['email']}")
                    print(f"Data de Criação: {user['data_criacao']}")
                else:
                    print("Usuário não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "3":
            print("\n--- Atualizar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user = user_model.find_user_by_id(user_id)
                if user:
                    print("\nUsuário encontrado:")  
                    print("Deixe em branco os campos que não deseja alterar.")
                    senha = input("Nova senha: ") or None
                    email = input("Novo e-mail: ") or None
                    user_model.update_user_by_id(user_id, senha, email)
                else:
                    print("Usuário não encontrado, não pode ser atualizado")

            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "4":
            print("\n--- Deletar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user_model.delete_user_by_id(user_id)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "5":
            print("\n--- Lista de Usuários ---")
            users = user_model.get_all_users()
            if users:
                for user in users:
                    print(f"\nID: {user['id']}")
                    print(f"E-mail: {user['email']}")
                    print(f"Data de Criação: {user['data_criacao']}")
                print("\n--- Fim da lista ---")
            else:
                print("Nenhum usuário cadastrado.")

        elif choice == "6":
            print("Saindo do programa.")
            break

        elif choice == "7":
            print("\n--- Cadastro de Postagem ---")
            titulo = input("Título: ")
            conteudo = input("Conteúdo: ")
            user = input("user_id: ")
            blog_model.create_post(titulo, conteudo, user)
            print("opção A executada")

        elif choice == "8":
            print("\n--- Buscar Postagem por ID post")
            try:
                id_post = int(input("Digite o ID post: "))
                blog = blog_model.find_post_by_id_post(id_post)
                if blog:
                    print("\nPostagem encontrada:")
                    print(f"ID: {blog['id_post']}")
                    print(f"titulo: {blog['titulo']}")
                    print(f"conteudo: {blog['conteudo']}")
                    print(f"usuario: {blog['id_user']} ")
                    print(f"Data de Criação: {blog['data_criacao']}")
                else:
                    print("Post não encontrado.")
            except ValueError:
                print("ID post inválido. Por favor, digite um número.")

        elif choice == "9":
            print("\n--- Buscar Postagem por usuário ---")
            try:
                id_user = int(input("Digite o ID do usário: "))
                blog = blog_model.find_post_by_id_user(id_user)
                if blog:
                    print("\nPostagem encontrada:")
                    print(f"ID user:{blog['id_user']}")
                    print(f"ID: {blog['id_post']}")
                    print(f"titulo: {blog['titulo']}")
                    print(f"conteudo: {blog['conteudo']}")
                    print(f"Data de Criação: {blog['data_criacao']}")
                else:
                    print("Post não encontrado.")
            except ValueError:
                print("ID user inválido. Por favor, digite um número.")


        elif choice == "10":
            print("\n--- Atualizar Postagem ---")
            try:
                id_post = int(input("Digite o ID da postagem: "))
                blog = blog_model.find_post_by_id_post(id_post)
                if blog:
                    print("\nPostagem encontrada:")
                    print("Deixe em branco os campos que não deseja alterar.")
                    titulo = input("Novo Título: ") or None
                    conteudo = input("Novo conteúdo: ") or None
                    blog_model.update_post_by_id_post(id_post, titulo, conteudo)
                else:
                    print("Post não encontrado, não pode ser atualizado.") 
                
            except ValueError:
                print("ID post inválido. Por favor, digite um número.")

        elif choice == "11":
            print("\n--- Deletar Postagem ---")
            try:
                id_post = int(input("Digite o ID da postagem: "))
                blog_model.delete_post_by_id_post(id_post)
            except ValueError:
                print("ID da postagem inválido. Por favor, digite um número.")

        elif choice == "12":
            print("\n--- Lista de Postagens ---")
            posts = blog_model.get_all_posts()
            if posts:
                for post in posts:
                    print(f"\nID: {post['id_post']}")
                    print(f"Titulo: {post['titulo']}")
                    print(f"Conteudo: {post['conteudo']}")
                    print(f"Criador: {post["id_user"]}")
                    print(f"Data de Criação: {post['data_criacao']}")
                    print(f"Data da ultima alteração: {post['data_atualizacao']}")
                print("\n--- Fim da lista ---")
            else:
                print("Nenhuma postagem cadastrada.")

        elif choice == "13":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()

