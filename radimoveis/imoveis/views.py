from django.shortcuts import render
from .models import Imovel


def home(request):
    context = {
        'imoveis': [
            Imovel(breve_descricao='Apartamento muito legal!',
                   endereco='Rua Pedro Krisnki n 277',
                   preco='10',
                   detalhes="""O que temos que ter sempre em mente é que a constante'
                            divulgação das informações afeta positivamente a correta
                            previsão das condições financeiras e administrativas exigidas."""),
            Imovel(breve_descricao='Casa Bacana em madureira',
                   endereco='Madureira 881',
                   preco='50',
                   detalhes="""O que temos que ter sempre em mente é que a constante'
                           divulgação das informações afeta positivamente a correta
                           previsão das condições financeiras e administrativas exigidas."""),
            Imovel(breve_descricao='Outra casa legal!',
                   endereco='campo grande',
                   preco='30',
                   detalhes="Esse apartamento é tão legal cara, maneiro mesmo..."),
            Imovel(breve_descricao='Casa no centro da cidade',
                   endereco='Centro RJ',
                   preco='40',
                   detalhes="Esse aqui então, irado demais."),
        ]
    }
    return render(request, 'index.html', context)
