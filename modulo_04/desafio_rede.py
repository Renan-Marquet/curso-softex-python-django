# SIMULADOR DE REDE SOCIAL (Versão Texto)
class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

class Post:

    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono

class RedeSocial:

    def __init__(self):
        self.banco_de_posts = []

    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        print(f" Post criado por {usuario_logado.apelido}!")
        
    def ver_meu_perfil(self, usuario_logado):
        print(f"\n --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f" Usuário: {usuario_logado.apelido}")
        print("-" * 30)
#
# AQUI ESTÁ O PROBLEMA!
# Atualmente, ele mostra TUDO de TODO MUNDO.
# SUA MISSÃO: Use um 'if' para mostrar o post APENAS se
# o 'post.dono' for igual ao 'usuario_logado'
        encontrou_algo = False
        for post in self.banco_de_posts:
    # --- APAGUE A LINHA ABAIXO E CRIE SEU IF AQUI ---
            if self.dono == usuario_logado:

                print(f" {post.texto} (Postado por: {post.dono.apelido})")
        encontrou_algo = True
# --------------------------------------------------
        if not encontrou_algo:
            print(" (Nenhum post encontrado )")
            print("-" * 30 + "\n")
# --- ÁREA DE PERSONALIZAÇÃO (MUDE OS DADOS ABAIXO!) ---
# 1. Criando usuários
# TODO: Coloque seu nome e invente um apelido
usuario_principal = Usuario("Renan Marquet", "@renan")
# TODO: Crie um amigo (ou inimigo) fictício
usuario_secundario = Usuario("José Roberto", "@beto")
# 2. Ligando a rede
minha_rede_social = RedeSocial()
# 3. Criando posts (Misturados!)
# TODO: Escreva mensagens criativas nos posts abaixo!
minha_rede_social.criar_post("O dia 22 de novembro já era uma data histórica.", usuario_principal)
minha_rede_social.criar_post("Sim, aniversário de Niterói, sua cidade natal.", usuario_secundario)
minha_rede_social.criar_post("Ganhou mais importância agora!", usuario_principal)
# 4. O TESTE FINAL
# Se o seu código estiver certo, aqui só deve aparecer os posts do SEU USUÁRIO!
print("\n--- TESTANDO SEU CÓDIGO ---")
minha_rede_social.ver_meu_perfil(usuario_principal)