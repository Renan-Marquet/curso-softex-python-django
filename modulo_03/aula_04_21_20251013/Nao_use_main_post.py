from user_model import UserModel
from blog_model import BlogModel


def display_menu():
    """Exibe o menu de opções."""
    print("\n--- Gerenciador de Usuários ---")
    print("1. Cadastrar novo usuário")
    print("2. Buscar usuário por ID")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Listar todos os usuários")
    print("6. Sair")
    print("---------------------------------")
    print("\n--- Gerenciador de Postagem ---")
    print("A. Cadastrar nova Postagem")
    print("B. Buscar Postagem por ID da postagem")
    print("C. Buscar Postagem por ID do usuário")
    print("D. Atualizar Postagem")
    print("E. Deletar Postagem")
    print("F. Listar todos as postagenss")
    print("G. Sair")
    print("---------------------------------")





def main():
    """Função principal do programa."""
    user_model = UserModel()
    blog_model = BlogModel()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "A" or "a":
            print("\n--- Cadastro de Postagem ---")
            titulo = input("Título: ")
            conteudo = input("Conteúdo: ")
            user = input("user_id: ")
            blog_model.create_post(titulo, conteudo, user)
            print("opção A executada")

        elif choice == "B" or "b":
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

        elif choice == "C" or "c":
            print("\n--- Buscar Postagem por usuário ---")
            try:
                user_id = int(input("Digite o ID do usário: "))
                blog = blog_model.find_post_by_id_user(user_id)
                if blog:
                    print("\nPostagem encontrada:")
                    print(f"ID user:{blog['user_id']}")
                    print(f"ID: {blog['id_post']}")
                    print(f"titulo: {blog['titulo']}")
                    print(f"conteudo: {blog['conteudo']}")
                    print(f"Data de Criação: {blog['data_criacao']}")
                else:
                    print("Post não encontrado.")
            except ValueError:
                print("ID user inválido. Por favor, digite um número.")


        elif choice == "D" or "d":
            print("\n--- Atualizar Postagem ---")
            try:
                id_post = int(input("Digite o ID da postagem: "))
                print("Deixe em branco os campos que não deseja alterar.")
                titulo = input("Novo Título: ") or None
                conteudo = input("Novo conteudo: ") or None
                blog_model.update_post_by_id_post(id_post, titulo, conteudo)
            except ValueError:
                print("ID post inválido. Por favor, digite um número.")

        elif choice == "E" or "e":
            print("\n--- Deletar Postagem ---")
            try:
                id_post = int(input("Digite o ID da postagem: "))
                blog_model.delete_post_by_id_post(id_post)
            except ValueError:
                print("ID da postagem inválido. Por favor, digite um número.")

        elif choice == "F" or "f":
            print("\n--- Lista de Postagens ---")
            posts = blog_model.get_all_posts()
            if posts:
                for post in posts:
                    print(f"\nID: {post['id_post']}")
                    print(f"Titulo: {post['titulo']}")
                    print(f"Conteudo: {post['conteudo']}")
                    print(f"Criador: {post["user_id"]}")
                    print(f"Data de Criação: {user['data_criacao']}")
                    print(f"Data da ultima alteração: {user['data_atualizacao']}")
                print("\n--- Fim da lista ---")
            else:
                print("Nenhuma postagem cadastrada.")

        elif choice == "G" or "g":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main();
