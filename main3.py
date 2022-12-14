import random
from navec import Navec
import json

good_words = [
    'идея', 'процедура', 'этап', 'порядок', 'сотня', 'мужик', 'магазин', 'представление', 'платье', 'книжка',
    'торговля', 'информация', 'ворота', 'разговор', 'министерство', 'редактор', 'пистолет', 'внимание',
    'творчество', 'труд', 'новость', 'озеро', 'покупатель', 'сюжет', 'вера', 'ставка', 'вершина', 'возраст',
    'старик', 'экран', 'команда', 'метод', 'высота', 'средство', 'речь', 'честь', 'эксперт', 'профессор',
    'бумага', 'чиновник', 'деньги', 'собственность', 'нож', 'помощь', 'заявление', 'образование', 'отрасль',
    'майор', 'враг', 'лед', 'воздух', 'миг', 'июнь', 'тысяча', 'удовольствие', 'толпа', 'слово', 'житель',
    'требование', 'бог', 'список', 'господь', 'школа', 'восторг', 'обеспечение', 'сон', 'ребята', 'стиль',
    'капитан', 'опасность', 'точка', 'роман', 'нефть', 'указание', 'основное', 'изменение', 'вопрос',
    'группа', 'среда', 'запад', 'давление', 'смена', 'обязательство', 'следователь', 'мама', 'выход', 'цвет',
    'сотрудник', 'осень', 'запас', 'главное', 'депутат', 'температура', 'предел', 'помещение', 'источник',
    'соглашение', 'кино', 'здание', 'объект', 'поведение', 'отличие', 'просьба', 'судья', 'живот', 'король',
    'положение', 'диван', 'начало', 'день', 'руководство', 'отказ', 'шум', 'дед', 'родина', 'смех',
    'действие', 'ожидание', 'море', 'технология', 'лев', 'свидетель', 'мешок', 'угол', 'канал', 'ящик',
    'ситуация', 'сентябрь', 'материал', 'девочка', 'зал', 'храм', 'сказка', 'борьба', 'убийство',
    'государство', 'черта', 'прошлое', 'глава', 'дядя', 'счастье', 'столик', 'преступление', 'признание',
    'дверь', 'сторона', 'замок', 'сумма', 'музей', 'строительство', 'кризис', 'жена', 'данные', 'лето',
    'продукция', 'производство', 'игра', 'автомат', 'сравнение', 'взаимодействие', 'профессия', 'республика',
    'длина', 'господин', 'энергия', 'проверка', 'повод', 'увеличение', 'изображение', 'дело', 'пиво',
    'достижение', 'баба', 'промышленность', 'представитель', 'конец', 'крест', 'водитель', 'герой', 'издание',
    'практика', 'конфликт', 'рот', 'победа', 'законодательство', 'музыка', 'слой', 'создание', 'спина',
    'стоимость', 'наличие', 'характеристика', 'угроза', 'категория', 'женщина', 'лист', 'интерес', 'режиссер',
    'коммунист', 'рынок', 'секретарь', 'рассмотрение', 'дружба', 'нога', 'потеря', 'хлеб', 'глубина', 'улица',
    'случай', 'обработка', 'пора', 'потребность', 'масло', 'сумка', 'цветок', 'кодекс', 'набор', 'брат',
    'мечта', 'впечатление', 'администрация', 'смысл', 'пример', 'множество', 'письмо', 'потолок', 'столица',
    'зеркало', 'отделение', 'середина', 'буква', 'жертва', 'спор', 'фон', 'линия', 'исключение',
    'родственник', 'зуб', 'кровать', 'революция', 'обстоятельство', 'прокурор', 'рыба', 'публика', 'система',
    'пара', 'месяц', 'план', 'зависимость', 'кресло', 'реклама', 'проблема', 'сообщение', 'деятельность',
    'фактор', 'станция', 'штат', 'стихи', 'последствие', 'цифра', 'снижение', 'лагерь', 'гость', 'воспитание',
    'свобода', 'почва', 'яблоко', 'постель', 'формула', 'акт', 'уровень', 'соответствие', 'работник', 'врач',
    'жизнь', 'пункт', 'услуга', 'редакция', 'переговоры', 'колено', 'сестра', 'камера', 'состав', 'понятие',
    'воля', 'дума', 'атмосфера', 'свет', 'охрана', 'предприятие', 'конкурс', 'обязанность', 'центр',
    'родитель', 'волос', 'вечер', 'поиск', 'фотография', 'произведение', 'контакт', 'участок', 'кредит',
    'поезд', 'район', 'статус', 'разработка', 'известие', 'комитет', 'немец', 'структура', 'мать', 'очередь',
    'серия', 'деревня', 'взгляд', 'голова', 'сутки', 'память', 'папа', 'рисунок', 'собрание', 'палец',
    'степень', 'председатель', 'объем', 'глаз', 'поселок', 'расстояние', 'январь', 'власть', 'явление',
    'учет', 'влияние', 'схема', 'разница', 'решение', 'губа', 'километр', 'кожа', 'основание', 'лес', 'мост',
    'безопасность', 'поверхность', 'город', 'кровь', 'год', 'обед', 'бой', 'фирма', 'статья', 'ресторан',
    'мероприятие', 'художник', 'покой', 'кабинет', 'служба', 'лестница', 'вывод', 'вкус', 'колесо', 'вход',
    'возможность', 'звонок', 'доллар', 'мгновение', 'кофе', 'голос', 'ряд', 'удивление', 'заказ', 'весна',
    'полет', 'механизм', 'обращение', 'подразделение', 'зима', 'сосед', 'реальность', 'окно', 'русский',
    'счет', 'неделя', 'фонд', 'жилье', 'слух', 'поэзия', 'норма', 'шанс', 'старуха', 'академия', 'тетя',
    'проведение', 'гора', 'знак', 'руководитель', 'поддержка', 'звук', 'страсть', 'улыбка', 'село',
    'активность', 'история', 'артист', 'масштаб', 'открытие', 'мир', 'огонь', 'мясо', 'должность', 'ноябрь',
    'элемент', 'офицер', 'животное', 'присутствие', 'приятель', 'тюрьма', 'талант', 'судьба', 'мощность',
    'утро', 'организм', 'корабль', 'июль', 'эффективность', 'цена', 'радость', 'принятие', 'круг', 'сигнал',
    'масса', 'товарищ', 'дача', 'стена', 'площадь', 'министр', 'газета', 'сеть', 'выполнение', 'специалист',
    'книга', 'начальство', 'тень', 'тон', 'стул', 'владелец', 'образ', 'еврей', 'партнер', 'ключ', 'условие',
    'банк', 'роль', 'получение', 'защита', 'существование', 'труба', 'объединение', 'монастырь', 'комплекс',
    'фильм', 'федерация', 'инициатива', 'философия', 'понимание', 'ответственность', 'основа', 'суть',
    'спорт', 'желание', 'миллион', 'способность', 'знакомый', 'партия', 'ребенок', 'концепция', 'величина',
    'показатель', 'растение', 'опыт', 'добро', 'часы', 'самолет', 'снег', 'учитель', 'оборудование',
    'концерт', 'документ', 'препарат', 'срок', 'отдел', 'писатель', 'приказ', 'аппарат', 'муж', 'соединение',
    'определение', 'граница', 'лошадь', 'плата', 'праздник', 'сезон', 'гостиница', 'союз', 'целое', 'оборона',
    'полковник', 'организация', 'постановление', 'факт', 'позиция', 'автор', 'культура', 'оценка', 'командир',
    'любовь', 'печать', 'пол', 'закон', 'экономика', 'крик', 'бутылка', 'устройство', 'спектакль', 'фамилия',
    'вино', 'назначение', 'сапог', 'карман', 'мастер', 'пост', 'возвращение', 'волна', 'усилие', 'отсутствие',
    'чтение', 'реформа', 'бюджет', 'слеза', 'продажа', 'дорога', 'итог', 'клетка', 'парк', 'клуб', 'ум',
    'грех', 'стекло', 'применение', 'сила', 'реакция', 'сигарета', 'тема', 'страница', 'темнота', 'лицо',
    'вид', 'период', 'армия', 'автомобиль', 'остров', 'коридор', 'скорость', 'тенденция', 'исследование',
    'том', 'восток', 'адрес', 'фраза', 'черт', 'предложение', 'ощущение', 'недостаток', 'строй', 'кусок',
    'автобус', 'душа', 'сомнение', 'обучение', 'студент', 'результат', 'дурак', 'песок', 'уход', 'одежда',
    'следствие', 'собака', 'настроение', 'хвост', 'рассказ', 'вариант', 'подарок', 'семья', 'сочинение',
    'таблица', 'наблюдение', 'солдат', 'вес', 'полоса', 'сотрудничество', 'война', 'запись', 'детство',
    'природа', 'частность', 'версия', 'премия', 'рамка', 'билет', 'земля', 'трава', 'время', 'доход',
    'размер', 'телефон', 'род', 'сделка', 'фигура', 'сущность', 'число', 'этаж', 'общение', 'отдых',
    'февраль', 'имущество', 'молоко', 'крыло', 'население', 'войско', 'противник', 'номер', 'дыхание',
    'эффект', 'зло', 'лидер', 'воспоминание', 'продукт', 'актер', 'чай', 'участник', 'порог', 'поворот',
    'событие', 'программа', 'газ', 'металл', 'машина', 'чувство', 'личность', 'количество', 'режим', 'карта',
    'коллега', 'ответ', 'движение', 'шея', 'психология', 'корпус', 'москвич', 'заключение', 'поездка', 'стол',
    'связь', 'красота', 'объяснение', 'традиция', 'зритель', 'фронт', 'значение', 'проект', 'ухо', 'дождь',
    'беседа', 'кость', 'кандидат', 'шаг', 'американец', 'помощник', 'образец', 'название', 'хозяин', 'дерево',
    'сфера', 'поколение', 'танец', 'дочка', 'журналист', 'камень', 'костюм', 'мужчина', 'транспорт', 'модель',
    'край', 'выставка', 'журнал', 'регион', 'институт', 'ветер', 'телевизор', 'театр', 'путь', 'стакан',
    'расчет', 'метр', 'зарплата', 'берег', 'форма', 'вода', 'записка', 'искусство', 'сбор', 'ракета',
    'субъект', 'сад', 'польза', 'деталь', 'вещество', 'секунда', 'дым', 'грудь', 'дама', 'вирус', 'поток',
    'тишина', 'библиотека', 'смерть', 'начальник', 'территория', 'процент', 'пенсия', 'река', 'час', 'слава',
    'подруга', 'выборы', 'мальчишка', 'тайна', 'птица', 'боль', 'бизнес', 'половина', 'зрение', 'член', 'дух',
    'небо', 'необходимость', 'площадка', 'функция', 'народ', 'совесть', 'единица', 'сердце', 'причина',
    'минута', 'текст', 'еда', 'человек', 'качество', 'мысль', 'золото', 'доктор', 'рост', 'встреча',
    'выражение', 'двор', 'суд', 'перевод', 'ладонь', 'производитель', 'успех', 'теория', 'здоровье',
    'описание', 'дно', 'десяток', 'март', 'мнение', 'вина', 'изучение', 'очки', 'передача', 'страна', 'тип',
    'направление', 'сожаление', 'тело', 'строка', 'краска', 'клиент', 'апрель', 'коллектив', 'вагон', 'пьеса',
    'ученый', 'октябрь', 'подготовка', 'ошибка', 'гражданин', 'выбор', 'хозяйка', 'договор', 'водка',
    'солнце', 'удар', 'сын', 'человечество', 'существо', 'директор', 'рука', 'остаток', 'конференция',
    'ценность', 'правило', 'пакет', 'выступление', 'обстановка', 'лейтенант', 'инженер', 'характер', 'песня',
    'блок', 'мозг', 'рабочий', 'заседание', 'установка', 'хозяйство', 'лодка', 'кадр', 'затрата', 'комиссия',
    'компьютер', 'забота', 'часть', 'друг', 'памятник', 'заместитель', 'способ', 'чудо', 'оплата', 'сведение',
    'доска', 'правда', 'чемпионат', 'парень', 'страх', 'параметр', 'шутка', 'повышение', 'болезнь',
    'операция', 'окончание', 'реализация', 'рубль', 'кольцо', 'губернатор', 'право', 'генерал', 'корень',
    'принцип', 'декабрь', 'риск', 'налог', 'предмет', 'больной', 'разрешение', 'читатель', 'кулак', 'рубеж',
    'нарушение', 'эпоха', 'мальчик', 'брак', 'компания', 'подход', 'управление', 'оружие', 'бабушка', 'штаб',
    'имя', 'переход', 'капитал', 'плечо', 'работа', 'анализ', 'сознание', 'пространство', 'беда', 'сцена',
    'появление', 'знание', 'дом', 'прием', 'август', 'штука', 'учреждение', 'литература', 'завод', 'урок',
    'правительство', 'квартира', 'куст', 'доклад', 'использование', 'исполнение', 'особенность',
    'формирование', 'нос', 'момент', 'испытание', 'округ', 'вещь', 'задача', 'техника', 'контроль', 'подъезд',
    'содержание', 'горло', 'признак', 'достоинство', 'кухня', 'взрыв', 'танк', 'выпуск', 'отец', 'орган',
    'молодежь', 'течение', 'милиция', 'звезда', 'ход', 'комната', 'запах', 'ручка', 'эксплуатация', 'пыль',
    'доля', 'большинство', 'наука', 'область', 'поле', 'конструкция', 'процесс', 'ресурс', 'политика',
    'свойство', 'цель', 'инструмент', 'дочь', 'акция', 'палата', 'университет', 'ремонт', 'отношение', 'щека',
    'долг', 'крыша', 'будущее', 'девушка', 'общество', 'товар', 'язык', 'класс', 'картина', 'ночь',
    'действительность', 'след', 'президент', 'мера', 'место', 'май', 'расход', 'лоб', 'дворец', 'совет',
    'эксперимент', 'век', 'зона', 'состояние', 'двигатель', 'ученик', 'воздействие', 'царь', 'поэт',
    'надежда', 'бок', 'раз', 'больница', 'рождение', 'участие', 'курс', 'доказательство', 'трубка',
    'перспектива', 'база', 'занятие', 'портрет', 'ужас', 'развитие', 'князь', 'попытка', 'церковь'
]

path = '/Users/m.materkov/Downloads/navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)


nouns_file = open('nouns.txt', 'r')
nouns = nouns_file.readlines()
nouns_file.close()

all_results = []

good_nouns = []
for noun in nouns:
    noun = noun.strip(" \t\r\n")
    good_nouns.append(noun)

total_count = len(good_words)
count = 0
for word in good_words:
    similar = {}
    for noun in good_nouns:
        if noun == word:
            continue
        if navec.get(noun) is None:
            continue

        sim = navec.sim(word, noun)
        if sim <= 0:
            continue
        similar[noun] = float(sim)

    similar = dict(reversed(sorted(similar.items(), key=lambda item: item[1])))

    all_results.append({
        "word": word,
        "similar": list(similar.keys()),
    })

    count += 1
    print(count/total_count*100)

f = open('results2.txt', 'w')
f.write(json.dumps(all_results))
f.close()
