# 10 .union

clientes_premium={'Maria','Pedro','Ana'}
clientes_recentes={'Ana','João','Lucas'}
todos_os_clientes=clientes_premium.union(clientes_recentes)
print(clientes_premium)
print(clientes_recentes)
print(todos_os_clientes)

# 11 .intrsection

clientes_vips_novos=clientes_recentes.intersection(clientes_premium)
print(clientes_vips_novos)

# 12 .difference

clientes_vips_antigos=clientes_premium.difference(clientes_recentes)
print(clientes_vips_antigos)