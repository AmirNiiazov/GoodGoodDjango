def get_menu_items(request):
    menu_items = [
                  {'title': "О сайте", 'url_name': 'about'},
                  {'title': "Добавить статью", 'url_name': 'add_page'},
                  {'title': "Обратная связь", 'url_name': 'contact'},
                  {'title': "Войти", 'url_name': 'login'}
                  ]
    return {'menu': menu_items}