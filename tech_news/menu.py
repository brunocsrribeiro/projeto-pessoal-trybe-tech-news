import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category, search_by_date, search_by_tag, search_by_title)


def start_close(option):
    if option == 0:
        get_tech_news(int(input("Digite quantas notícias serão buscadas: ")))
    elif option == 7:
        print("Encerrando script")
    else:
        menu_search_news(option)


def menu_search_news(option):
    if option == 1:
        print(search_by_title(input("Digite o título: ")))
    elif option == 2:
        print(search_by_date(input("Digite a data no formato aaaa-mm-dd: ")))
    elif option == 3:
        print(search_by_tag(input("Digite a tag: ")))
    elif option == 4:
        print(search_by_category(input("Digite a categoria: ")))
    else:
        menu_options_top_five(option)


def menu_options_top_five(option):
    if option == 5:
        print(top_5_news())
    elif option == 6:
        print(top_5_categories())


# Requisito 12
def analyzer_menu():
    try:
        options = int(
            input(
                "Selecione uma das opções a seguir:\n"
                " 0 - Popular o banco com notícias;\n"
                " 1 - Buscar notícias por título;\n"
                " 2 - Buscar notícias por data;\n"
                " 3 - Buscar notícias por tag;\n"
                " 4 - Buscar notícias por categoria;\n"
                " 5 - Listar top 5 notícias;\n"
                " 6 - Listar top 5 categorias;\n"
                " 7 - Sair.\n"
            )
        )

        if options in range(8):
            start_close(options)
        else:
            print("Opção inválida", file=sys.stderr)
    except ValueError as error:
        print(error, file=sys.stderr)
