def banco_dados() -> dict:
    """carrega os dados iniciais do banco de dados, que inclui usuario e configurações"""
    return{
        "usuarios":{
            "123456-7":{
                "senha":"9999",
                "nome":"José",
                "saldo":1500.00,
                "limite_cheque_especial": 500.00,
            },
        },
        "tentativas_login": 3,
        "ultima_conta_base": "123456",
        "digito_verificador": "7", 
    }
