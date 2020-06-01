import requests




def translater(URL, API_KEY, text, to_lang, on_lang):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(to_lang, on_lang),
    }

    response = requests.get(URL, params=params)
    return response



item = translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                  'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0', 'Hi, world', 'en', 'ru')
property = item.json()
print(property['text'])


