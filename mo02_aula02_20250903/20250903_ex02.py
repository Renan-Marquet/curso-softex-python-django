estoque_principal = [("Camiseta",101),("Calça",102),("Boné",103),("Tênis",104)]
estoque_online = [ ("Boné",103),("Camisa Polo",105),("Calça",102),("Chinelo",106)]

principal=set(estoque_principal)
online=set(estoque_online)

todos=principal.union(online)
loja_e_site=principal.intersection(online)
so_loja=principal.difference(online)
so_site=online.difference(principal)

print("Produtos disponíveis na loja e no site:")
print(loja_e_site)
print("Produtos disponíveis só na loja:")
print(so_loja)
print("Produtos disponíveis só no site:")
print(so_site)
