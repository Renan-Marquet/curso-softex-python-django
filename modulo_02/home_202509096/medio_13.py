pratos_veganos={'salada','arroz','feijão'}
cardapio={'pizza','salada','arroz','feijão'}
inter=pratos_veganos.intersection(cardapio)
if pratos_veganos == inter:
    print('sim é um subconjunto')