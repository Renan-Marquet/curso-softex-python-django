# Comparação de Registros

vendas_concluidas=[('id_001','p_a'),('id_002','p_b'),('id_003','p_c')]
registros_envio=[('id_001','p_a'),('id_004','p_d'),('id_002','p_b')]

#em_ambas=set()
#print(em_ambas)
conj_de_vendas=set(vendas_concluidas)
#print("vendas", conj_de_vendas)
conj_de_envios=set(registros_envio)
#print("envios", conj_de_envios)
todos=conj_de_vendas.union(registros_envio)
#print("tudo", todos)
em_ambas=conj_de_vendas.intersection(conj_de_envios)
print("\n Vendido e enviado", em_ambas)
vendas_sem_envio=conj_de_vendas.difference(registros_envio)
print(" Vendido e não enviado", vendas_sem_envio ,"\n")