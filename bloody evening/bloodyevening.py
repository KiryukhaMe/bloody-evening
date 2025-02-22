import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кровавый Закат")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
TRANSPARENT_BLACK = (50, 50, 50, 16)

# Шрифт
font = pygame.font.SysFont("Courier New", 30)

# Загрузка фонов
backgrounds = {
    "black_background": pygame.transform.scale(pygame.image.load("projectphotos/black_background.png"), (WIDTH, HEIGHT)),
    "intro": pygame.transform.scale(pygame.image.load("projectphotos/night.png"), (WIDTH, HEIGHT)),
    "open_case": pygame.transform.scale(pygame.image.load("projectphotos/case.png"), (WIDTH, HEIGHT)),
    "leave_case": pygame.transform.scale(pygame.image.load("projectphotos/garage.png"), (WIDTH, HEIGHT)),
    "search_blake": pygame.transform.scale(pygame.image.load("projectphotos/bar.png"), (WIDTH, HEIGHT)),
    "search_woman": pygame.transform.scale(pygame.image.load("projectphotos/carmen.png"), (WIDTH, HEIGHT)),
    "fight": pygame.transform.scale(pygame.image.load("projectphotos/fight.png"), (WIDTH, HEIGHT)),
    "run": pygame.transform.scale(pygame.image.load("projectphotos/run.png"), (WIDTH, HEIGHT)),
    "accept_deal": pygame.transform.scale(pygame.image.load("projectphotos/deal.png"), (WIDTH, HEIGHT)),
    "refuse_deal": pygame.transform.scale(pygame.image.load("projectphotos/refuse.png"), (WIDTH, HEIGHT)),
    "follow_plan": pygame.transform.scale(pygame.image.load("projectphotos/plan.png"), (WIDTH, HEIGHT)),
    "change_plan": pygame.transform.scale(pygame.image.load("projectphotos/change_plan.png"), (WIDTH, HEIGHT)),
    "help_carmen": pygame.transform.scale(pygame.image.load("projectphotos/help.png"), (WIDTH, HEIGHT)),
    "escape": pygame.transform.scale(pygame.image.load("projectphotos/escape.png"), (WIDTH, HEIGHT)),
    "continue_fight": pygame.transform.scale(pygame.image.load("projectphotos/continue_fight.png"), (WIDTH, HEIGHT)),
    "surrender": pygame.transform.scale(pygame.image.load("projectphotos/surrender.png"), (WIDTH, HEIGHT)),
    "capture_victor": pygame.transform.scale(pygame.image.load("projectphotos/capture.png"), (WIDTH, HEIGHT)),
    "return_case": pygame.transform.scale(pygame.image.load("projectphotos/return.png"), (WIDTH, HEIGHT)),
    "escape_with_money": pygame.transform.scale(pygame.image.load("projectphotos/escape_money.png"), (WIDTH, HEIGHT)),
    "trust_carmen": pygame.transform.scale(pygame.image.load("projectphotos/trust.png"), (WIDTH, HEIGHT)),
    "destroy_evidence": pygame.transform.scale(pygame.image.load("projectphotos/destroy.png"), (WIDTH, HEIGHT)),
    "go_to_authorities": pygame.transform.scale(pygame.image.load("projectphotos/authorities.png"), (WIDTH, HEIGHT)),
    "new_life_with_protection": pygame.transform.scale(pygame.image.load(
        "projectphotos/new_life_with_protection.png"), (WIDTH, HEIGHT)),
    "independent_life": pygame.transform.scale(pygame.image.load("projectphotos/independent_life.png"), (WIDTH, HEIGHT)),
    "hidden_life": pygame.transform.scale(pygame.image.load("projectphotos/hidden_life.png"), (WIDTH, HEIGHT)),
    "join_carmen": pygame.transform.scale(pygame.image.load("projectphotos/join_carmen.png"), (WIDTH, HEIGHT)),
    "ransom": pygame.transform.scale(pygame.image.load("projectphotos/ransom.png"), (WIDTH, HEIGHT)),
    "accept_fate": pygame.transform.scale(pygame.image.load("projectphotos/accept_fate.png"), (WIDTH, HEIGHT)),
    "deal_with_blake": pygame.transform.scale(pygame.image.load("projectphotos/deal_with_blake.png"), (WIDTH, HEIGHT)),
    "accept_help": pygame.transform.scale(pygame.image.load("projectphotos/accept_help.png"), (WIDTH, HEIGHT)),
    "contact_blake": pygame.transform.scale(pygame.image.load("projectphotos/contact_blake.png"), (WIDTH, HEIGHT)),
    "on_the_run": pygame.transform.scale(pygame.image.load("projectphotos/on_the_run.png"), (WIDTH, HEIGHT)),
    "new_life": pygame.transform.scale(pygame.image.load("projectphotos/new_life.png"), (WIDTH, HEIGHT)),
    "keep_hiding": pygame.transform.scale(pygame.image.load("projectphotos/keep_hiding.png"), (WIDTH, HEIGHT)),
    "return_to_game": pygame.transform.scale(pygame.image.load("projectphotos/return_to_game.png"), (WIDTH, HEIGHT)),
    "find_allies": pygame.transform.scale(pygame.image.load("projectphotos/find_allies.png"), (WIDTH, HEIGHT)),
    "find_shelter": pygame.transform.scale(pygame.image.load("projectphotos/find_shelter.png"), (WIDTH, HEIGHT)),
    "leave_game": pygame.transform.scale(pygame.image.load("projectphotos/leave_game.png"), (WIDTH, HEIGHT)),
    "hide_case": pygame.transform.scale(pygame.image.load("projectphotos/hide_case.png"), (WIDTH, HEIGHT)),

}

# Сцены
scenes = {
    "intro": {
        "sequence": [
            {"text": "Закат окрасил небо кровью. Джек Колт стоял на краю города, глядя на горизонт.", "background": "intro"},
            {"text": "Он решил начать новую жизнь, оставив позади свои старые грехи.", "background": "intro"},
            {"text": "Но судьба приготовила для него новый вызов...", "background": "intro"},
            {"text": "Внезапно, из тени появился незнакомец. Это был Мистер Блейк.", "background": "intro"},
            {"text": "Блейк: 'Джек, у меня для тебя дело. Ты не сможешь отказаться.'", "background": "intro"},
            {"text": "Джек: 'Я больше не в игре, Блейк. Оставь меня в покое.'", "background": "intro"},
            {"text": "Блейк: 'Это не просьба, Джек. Это приказ.'", "background": "intro"},
        ],
        "choices": [
            "Открыть кейс, который дал Блейк",
            "Оставить кейс закрытым и уйти",
            "Попытаться узнать больше о деле Блейка"
        ],
        "next": ["open_case", "leave_case", "search_blake"]
    },
    "open_case": {
        "sequence": [
            {"text": "Джек открывает кейс, который дал ему Блейк.", "background": "open_case"},
            {"text": "Внутри он находит пачку денег, пистолет и старую фотографию.", "background": "open_case"},
            {"text": "На фотографии изображена женщина с надписью на обороте: 'Она знает, где он.'", "background": "open_case"},
            {"text": "Джек: 'Кто она? И что это за игра, Блейк?'", "background": "open_case"},
            {"text": "Джек понимает, что его втянули в опасную игру, из которой не так просто выйти.", "background": "open_case"},
        ],
        "choices": [
            "Спрятать кейс и попытаться забыть о нём",
            "Найти женщину с фотографии и узнать правду"
        ],
        "next": ["hide_case", "search_woman"]
    },
    "leave_case": {
        "sequence": [
            {"text": "Джек решает оставить кейс в гараже и забыть о нём.", "background": "leave_case"},
            {"text": "Он возвращается домой, но ночью его будят звуки шагов за дверью.", "background": "leave_case"},
            {"text": "Джек: 'Кто там?'", "background": "leave_case"},
            {"text": "Незнакомец: 'Мы знаем, что у тебя есть кейс. Отдай его, и мы оставим тебя в живых.'", "background": "leave_case"},
            {"text": "Джек понимает, что его жизнь в опасности.", "background": "leave_case"},
        ],
        "choices": [
            "Драться с нападавшими",
            "Попытаться сбежать"
        ],
        "next": ["fight", "run"]
    },
    "search_blake": {
        "sequence": [
            {"text": "Джек решает найти Блейка и узнать, что происходит.", "background": "search_blake"},
            {"text": "Он отправляется в бар, где, по слухам, бывает Блейк.", "background": "search_blake"},
            {"text": "В баре Джек находит Блейка, но тот не один.", "background": "search_blake"},
            {"text": "Блейк: 'Я знал, что ты придёшь, Джек. Ты всегда был любопытным.'", "background": "search_blake"},
            {"text": "Джек: 'Что ты задумал, Блейк? Кто эта женщина на фото?'", "background": "search_blake"},
            {"text": "Блейк: 'Это Кармен Делакруз. Она знает, где спрятан Виктор Морено.'", "background": "search_blake"},
            {"text": "Джек понимает, что попал в ловушку.", "background": "search_blake"},
        ],
        "choices": [
            "Попытаться сбежать из бара",
            "Сражаться с людьми Блейка"
        ],
        "next": ["run", "fight"]
    },
    "search_woman": {
        "sequence": [
            {"text": "Джек начинает поиски женщины с фотографии.", "background": "search_woman"},
            {"text": "Он узнаёт, что её зовут Кармен Делакруз, и она связана с Виктором Морено.", "background": "search_woman"},
            {"text": "Джек находит Кармен в старом заброшенном доме на окраине города.", "background": "search_woman"},
            {"text": "Кармен: 'Ты должен быть Джек Колт. Блейк говорил о тебе.'", "background": "search_woman"},
            {"text": "Джек: 'Что ты знаешь о Викторе Морено?'", "background": "search_woman"},
            {"text": "Кармен: 'Я помогу тебе, но только если ты убьёшь Виктора.'", "background": "search_woman"},
        ],
        "choices": [
            "Принять предложение Кармен",
            "Отказаться и уйти"
        ],
        "next": ["accept_deal", "refuse_deal"]
    },
    "fight": {
        "sequence": [
            {"text": "Джек решает сражаться с нападавшими.", "background": "fight"},
            {"text": "После ожесточённой схватки он остаётся жив, но понимает, что игра только начинается.", "background": "fight"},
            {"text": "Джек: 'Кто эти люди? И почему они хотят кейс?'", "background": "fight"},
            {"text": "Он решает найти Кармен, чтобы узнать правду.", "background": "fight"},
        ],
        "choices": [
            "Искать Кармен",
            "Попытаться уйти из игры"
        ],
        "next": ["search_woman", "leave_game"]
    },
    "accept_deal": {
        "sequence": [
            {"text": "Джек соглашается на предложение Кармен.", "background": "accept_deal"},
            {"text": "Кармен: 'Виктор Морено — опасный человек. Он знает, что ты ищешь его.'",
             "background": "accept_deal"},
            {"text": "Джек: 'Почему ты хочешь, чтобы я убил его?'", "background": "accept_deal"},
            {"text": "Кармен: 'Он предал меня. И теперь я хочу, чтобы он заплатил.'", "background": "accept_deal"},
            {"text": "Джек и Кармен начинают планировать убийство Виктора.", "background": "accept_deal"},
        ],
        "choices": [
            "Следовать плану Кармен",
            "Попробовать изменить план"
        ],
        "next": ["follow_plan", "change_plan"]
    },
    "refuse_deal": {
        "sequence": [
            {"text": "Джек отказывается от предложения Кармен.", "background": "refuse_deal"},
            {"text": "Кармен: 'Ты совершаешь ошибку, Джек. Виктор найдёт тебя.'", "background": "refuse_deal"},
            {"text": "Джек: 'Я сам разберусь с этим.'", "background": "refuse_deal"},
            {"text": "Кармен уходит, оставляя Джека одного.", "background": "refuse_deal"},
            {"text": "Через несколько дней Джек понимает, что за ним следят.", "background": "refuse_deal"},
        ],
        "choices": [
            "Помочь Кармен в последний момент",
            "Бросить всё и скрыться"
        ],
        "next": ["help_carmen", "escape"]
    },
    "follow_plan": {
        "sequence": [
            {"text": "Джек и Кармен следуют плану.", "background": "follow_plan"},
            {"text": "Они находят Виктора Морено в его укрытии.", "background": "follow_plan"},
            {"text": "Кармен: 'Это твой конец, Виктор.'", "background": "follow_plan"},
            {"text": "Виктор: 'Ты думал, что всё будет так просто, Джек?'", "background": "follow_plan"},
            {"text": "Внезапно появляются люди Виктора, и начинается перестрелка.", "background": "follow_plan"},
        ],
        "choices": [
            "Продолжить бой",
            "Сдаться Виктору"
        ],
        "next": ["continue_fight", "surrender"]
    },
    "change_plan": {
        "sequence": [
            {"text": "Джек решает изменить план.", "background": "change_plan"},
            {"text": "Он предлагает Кармен захватить Виктора живым.", "background": "change_plan"},
            {"text": "Кармен: 'Это рискованно, но может сработать.'", "background": "change_plan"},
            {"text": "Они находят Виктора, но ситуация выходит из-под контроля.", "background": "change_plan"},
            {"text": "Виктор: 'Вы думали, что сможете меня перехитрить?'", "background": "change_plan"},
        ],
        "choices": [
            "Захватить Виктора",
            "Попробовать уйти"
        ],
        "next": ["capture_victor", "escape"]
    },
    "help_carmen": {
        "sequence": [
            {"text": "Джек решает помочь Кармен.", "background": "help_carmen"},
            {"text": "Он находит её в ловушке, устроенной людьми Виктора.", "background": "help_carmen"},
            {"text": "Джек: 'Держись, Кармен! Я тебя вытащу!'", "background": "help_carmen"},
            {"text": "Кармен: 'Я знала, что ты придёшь.'", "background": "help_carmen"},
            {"text": "Вместе они сражаются и выбираются из западни.", "background": "help_carmen"},
        ],
        "choices": [
            "Довериться Кармен и продолжить",
            "Попробовать самостоятельно уйти из игры"
        ],
        "next": ["trust_carmen", "leave_game"]
    },
    "escape": {
        "sequence": [
            {"text": "Джек решает уйти из игры.", "background": "escape"},
            {"text": "Он бросает всё и пытается начать новую жизнь.", "background": "escape"},
            {"text": "Но прошлое не отпускает его.", "background": "escape"},
            {"text": "Джек: 'Я думал, что смогу убежать, но это невозможно.'", "background": "escape"},
        ],
        "choices": [
            "Сдаться властям",
            "Жить в бегах"
        ],
        "next": ["surrender", "on_the_run"]
    },
    "continue_fight": {
        "sequence": [
            {"text": "Джек продолжает сражаться.", "background": "continue_fight"},
            {"text": "Он одерживает победу, но с большими потерями.", "background": "continue_fight"},
            {"text": "Кармен: 'Мы сделали это, Джек. Виктор мёртв.'", "background": "continue_fight"},
            {"text": "Джек: 'Но какой ценой...'", "background": "continue_fight"},
        ],
        "choices": [
            "Вернуться к Блейку с кейсом",
            "Скрыться с деньгами"
        ],
        "next": ["return_case", "escape_with_money"]
    },
    "surrender": {
        "sequence": [
            {"text": "Джек сдаётся Виктору.", "background": "surrender"},
            {"text": "Виктор: 'Ты сделал правильный выбор, Джек.'", "background": "surrender"},
            {"text": "Джек: 'Что ты собираешься со мной сделать?'", "background": "surrender"},
            {"text": "Виктор: 'Ты будешь работать на меня. Или умрёшь.'", "background": "surrender"},
        ],
        "choices": [
            "Попробовать выкупиться",
            "Принять свою судьбу"
        ],
        "next": ["ransom", "accept_fate"]
    },
    "capture_victor": {
        "sequence": [
            {"text": "Джек захватывает Виктора.", "background": "capture_victor"},
            {"text": "Виктор: 'Ты думаешь, что сможешь меня остановить?'", "background": "capture_victor"},
            {"text": "Джек: 'Это конец, Виктор.'", "background": "capture_victor"},
            {"text": "Но теперь Джек вынужден защищаться от людей Виктора.", "background": "capture_victor"},
        ],
        "choices": [
            "Сделать обмен с Блейком",
            "Попробовать скрыться"
        ],
        "next": ["deal_with_blake", "escape"]
    },
    "return_case": {
        "sequence": [
            {"text": "Джек возвращает кейс Блейку.", "background": "return_case"},
            {"text": "Блейк: 'Ты сделал правильный выбор, Джек.'", "background": "return_case"},
            {"text": "Джек: 'Что теперь?'", "background": "return_case"},
            {"text": "Блейк: 'Теперь ты свободен. Но будь осторожен.'", "background": "return_case"},
        ],
        "choices": [
            "Принять помощь Блейка",
            "Скрыться с деньгами"
        ],
        "next": ["accept_help", "escape_with_money"]
    },
    "escape_with_money": {
        "sequence": [
            {"text": "Джек решает скрыться с деньгами.", "background": "escape_with_money"},
            {"text": "Он начинает новую жизнь, но понимает, что опасность всё ещё рядом.",
             "background": "escape_with_money"},
            {"text": "Джек: 'Я думал, что деньги решат все проблемы, но я ошибался.'",
             "background": "escape_with_money"},
        ],
        "choices": [
            "Попробовать связаться с Блейком",
            "Начать всё заново под другим именем"
        ],
        "next": ["contact_blake", "new_life"]
    },
    "trust_carmen": {
        "sequence": [
            {"text": "Джек решает довериться Кармен.", "background": "trust_carmen"},
            {"text": "Они начинают работать вместе, чтобы покончить с Виктором.", "background": "trust_carmen"},
            {"text": "Кармен: 'Мы сможем сделать это, если будем вместе.'", "background": "trust_carmen"},
            {"text": "Джек: 'Я надеюсь, ты права.'", "background": "trust_carmen"},
        ],
        "choices": [
            "Обратиться к властям вместе",
            "Попытаться уничтожить компромат"
        ],
        "next": ["go_to_authorities", "destroy_evidence"]
    },
    "destroy_evidence": {
        "sequence": [
            {"text": "Джек уничтожает кейс с компроматом.", "background": "destroy_evidence"},
            {"text": "Кармен: 'Теперь мы свободны.'", "background": "destroy_evidence"},
            {"text": "Джек: 'Но что будет дальше?'", "background": "destroy_evidence"},
            {"text": "Они понимают, что теперь их жизни в их руках.", "background": "destroy_evidence"},
        ],
        "choices": [
            "Жить скрытно",
            "Присоединиться к Кармен в борьбе"
        ],
        "next": ["hidden_life", "join_carmen"]
    },
    "go_to_authorities": {
        "sequence": [
            {"text": "Джек и Кармен решают обратиться к властям.", "background": "go_to_authorities"},
            {"text": "Они передают всю информацию о Викторе и его сети.", "background": "go_to_authorities"},
            {"text": "Кармен: 'Это наш шанс начать всё с чистого листа.'", "background": "go_to_authorities"},
            {"text": "Джек: 'Но сможем ли мы когда-нибудь быть свободны?'", "background": "go_to_authorities"},
            {"text": "Власти предлагают им защиту в обмен на сотрудничество.", "background": "go_to_authorities"},
        ],
        "choices": [
            "Принять защиту и начать новую жизнь",
            "Отказаться и попытаться жить самостоятельно"
        ],
        "next": ["new_life_with_protection", "independent_life"]
    },
    "new_life_with_protection": {
        "sequence": [
            {"text": "Джек и Кармен принимают защиту от властей.", "background": "new_life_with_protection"},
            {"text": "Они начинают новую жизнь под новыми именами.", "background": "new_life_with_protection"},
            {"text": "Кармен: 'Мы сделали правильный выбор.'", "background": "new_life_with_protection"},
            {"text": "Джек: 'Теперь у нас есть шанс на нормальную жизнь.'", "background": "new_life_with_protection"},
            {"text": "Они живут в тихом городке, но всегда помнят о своём прошлом.", "background": "new_life_with_protection"},
        ],
        "choices": [],
        "next": []
    },
    "independent_life": {
        "sequence": [
            {"text": "Джек и Кармен решают жить самостоятельно.", "background": "independent_life"},
            {"text": "Они скрываются от властей и бывших врагов.", "background": "independent_life"},
            {"text": "Кармен: 'Мы всегда будем настороже.'", "background": "independent_life"},
            {"text": "Джек: 'Но это наша свобода.'", "background": "independent_life"},
            {"text": "Они продолжают жить в тени, но их связь становится только крепче.", "background": "independent_life"},
        ],
        "choices": [],
        "next": []
    },
    "hidden_life": {
        "sequence": [
            {"text": "Джек решает жить скрытно.", "background": "hidden_life"},
            {"text": "Он уезжает в маленький городок, где его никто не знает.", "background": "hidden_life"},
            {"text": "Джек: 'Теперь я могу начать всё заново.'", "background": "hidden_life"},
            {"text": "Но он всегда помнит о своём прошлом и остаётся настороже.", "background": "hidden_life"},
        ],
        "choices": [],
        "next": []
    },
    "join_carmen": {
        "sequence": [
            {"text": "Джек решает присоединиться к Кармен в борьбе.", "background": "join_carmen"},
            {"text": "Они становятся партнёрами, борясь с преступностью.", "background": "join_carmen"},
            {"text": "Кармен: 'Вместе мы сможем изменить этот мир.'", "background": "join_carmen"},
            {"text": "Джек: 'Я готов сражаться за то, во что верю.'", "background": "join_carmen"},
            {"text": "Они продолжают свою борьбу, становясь легендами в преступном мире.", "background": "join_carmen"},
        ],
        "choices": [],
        "next": []
    },
    "ransom": {
        "sequence": [
            {"text": "Джек пытается выкупиться у Виктора.", "background": "ransom"},
            {"text": "Виктор: 'Ты думаешь, что можешь купить свою свободу?'", "background": "ransom"},
            {"text": "Джек: 'У меня есть деньги. Отпусти меня.'", "background": "ransom"},
            {"text": "Виктор соглашается, но Джек понимает, что это лишь временное решение.", "background": "ransom"},
        ],
        "choices": [
            "Попытаться сбежать",
            "Принять свою судьбу"
        ],
        "next": ["escape", "accept_fate"]
    },
    "accept_fate": {
        "sequence": [
            {"text": "Джек решает принять свою судьбу.", "background": "accept_fate"},
            {"text": "Он продолжает работать на Виктора, но мечтает о свободе.", "background": "accept_fate"},
            {"text": "Джек: 'Возможно, однажды я смогу вырваться.'", "background": "accept_fate"},
            {"text": "Но пока он остаётся в тени, выполняя приказы Виктора.", "background": "accept_fate"},
        ],
        "choices": [],
        "next": []
    },
    "deal_with_blake": {
        "sequence": [
            {"text": "Джек решает сделать обмен с Блейком.", "background": "deal_with_blake"},
            {"text": "Блейк: 'Ты сделал правильный выбор, Джек.'", "background": "deal_with_blake"},
            {"text": "Джек: 'Что теперь?'", "background": "deal_with_blake"},
            {"text": "Блейк предлагает ему работу в ФБР в обмен на свободу.", "background": "deal_with_blake"},
        ],
        "choices": [
            "Принять предложение Блейка",
            "Отказаться и скрыться"
        ],
        "next": ["accept_help", "escape"]
    },
    "accept_help": {
        "sequence": [
            {"text": "Джек принимает предложение Блейка.", "background": "accept_help"},
            {"text": "Он начинает работать на ФБР, помогая бороться с преступностью.", "background": "accept_help"},
            {"text": "Блейк: 'Ты можешь искупить свои грехи, Джек.'", "background": "accept_help"},
            {"text": "Джек: 'Я надеюсь, что это того стоит.'", "background": "accept_help"},
            {"text": "Он находит новую цель в жизни, но его прошлое всё ещё преследует его.", "background": "accept_help"},
        ],
        "choices": [],
        "next": []
    },
    "contact_blake": {
        "sequence": [
            {"text": "Джек решает связаться с Блейком.", "background": "contact_blake"},
            {"text": "Блейк: 'Ты сделал правильный выбор, Джек.'", "background": "contact_blake"},
            {"text": "Джек: 'Я хочу начать всё заново.'", "background": "contact_blake"},
            {"text": "Блейк предлагает ему помощь в обмен на сотрудничество.", "background": "contact_blake"},
        ],
        "choices": [
            "Принять помощь Блейка",
            "Отказаться и жить в бегах"
        ],
        "next": ["accept_help", "on_the_run"]
    },
    "on_the_run": {
        "sequence": [
            {"text": "Джек решает жить в бегах.", "background": "on_the_run"},
            {"text": "Он постоянно меняет местоположение, чтобы избежать преследования.", "background": "on_the_run"},
            {"text": "Джек: 'Я всегда буду настороже.'", "background": "on_the_run"},
            {"text": "Но он понимает, что такая жизнь не может длиться вечно.", "background": "on_the_run"},
        ],
        "choices": [],
        "next": []
    },
    "new_life": {
        "sequence": [
            {"text": "Джек начинает новую жизнь под другим именем.", "background": "new_life"},
            {"text": "Он находит работу в маленьком городке и пытается забыть о своём прошлом.", "background": "new_life"},
            {"text": "Джек: 'Теперь я могу жить спокойно.'", "background": "new_life"},
            {"text": "Но он всегда помнит, что его прошлое может настигнуть его в любой момент.", "background": "new_life"},
        ],
        "choices": [],
        "next": []
    },
    "hide_case": {
        "sequence": [
            {"text": "Джек решает спрятать кейс в старом сарае на окраине города.", "background": "hide_case"},
            {"text": "Он закапывает его под полом, надеясь, что никто не найдёт.", "background": "hide_case"},
            {"text": "Джек: 'Этот кейс принесёт только беды. Лучше забыть о нём.'", "background": "hide_case"},
            {"text": "Но через несколько дней Джек замечает, что за ним следят.", "background": "hide_case"},
            {"text": "Незнакомец: 'Мы знаем, что ты спрятал кейс. Верни его, или тебе не поздоровится.'",
             "background": "hide_case"},
            {"text": "Джек понимает, что его попытки избежать проблем только усугубили ситуацию.",
             "background": "hide_case"},
        ],
        "choices": [
            "Вернуть кейс и попытаться договориться",
            "Попытаться сбежать и начать новую жизнь"
        ],
        "next": ["return_case", "escape"]
    },
    "run": {
        "sequence": [
            {"text": "Джек решает сбежать из бара, пока не стало слишком поздно.", "background": "run"},
            {"text": "Он пробирается через задний выход, но на улице его ждут люди Блейка.", "background": "run"},
            {"text": "Джек: 'Вы не оставите мне выбора...'", "background": "run"},
            {"text": "Он бросается в драку, пытаясь прорваться к свободе.", "background": "run"},
            {"text": "После короткой схватки Джеку удаётся сбежать, но он понимает, что теперь он в бегах.",
             "background": "run"},
        ],
        "choices": [
            "Найти убежище и спрятаться",
            "Попытаться найти союзников"
        ],
        "next": ["find_shelter", "find_allies"]
    },
    "leave_game": {
        "sequence": [
            {"text": "Джек решает бросить всё и уйти из игры.", "background": "leave_game"},
            {"text": "Он продаёт свои вещи, берёт деньги и уезжает из города.", "background": "leave_game"},
            {"text": "Джек: 'Я больше не хочу быть частью этого мира.'", "background": "leave_game"},
            {"text": "Но через несколько месяцев он понимает, что прошлое не отпускает.", "background": "leave_game"},
            {"text": "Он получает письмо с фотографией своего нового дома и надписью: 'Мы знаем, где ты.'",
             "background": "leave_game"},
            {"text": "Джек понимает, что ему не удастся просто так уйти.", "background": "leave_game"},
        ],
        "choices": [
            "Вернуться и закончить начатое",
            "Продолжать скрываться"
        ],
        "next": ["return_to_game", "keep_hiding"]
    },
"find_shelter": {
        "sequence": [
            {"text": "Джек находит убежище в заброшенном доме за городом.", "background": "find_shelter"},
            {"text": "Он прячется там несколько дней, планируя свои дальнейшие действия.", "background": "find_shelter"},
            {"text": "Джек: 'Мне нужно исчезнуть. Но как?'", "background": "find_shelter"},
            {"text": "Он решает связаться со старым другом, который может помочь ему.", "background": "find_shelter"},
            {"text": "Но когда друг приезжает, он оказывается предателем.", "background": "find_shelter"},
            {"text": "Джек: 'Ты работаешь на них?'", "background": "find_shelter"},
            {"text": "Друг: 'Прости, Джек. У меня не было выбора.'", "background": "find_shelter"},
            {"text": "Джек сражается и побеждает, но понимает, что теперь он совсем один.", "background": "find_shelter"},
            {"text": "Он решает уехать как можно дальше и начать всё с чистого листа.", "background": "find_shelter"},
        ],
        "choices": [],
        "next": []
    },
    "find_allies": {
        "sequence": [
            {"text": "Джек решает найти союзников среди старых знакомых.", "background": "find_allies"},
            {"text": "Он связывается с Кармен, которая соглашается помочь.", "background": "find_allies"},
            {"text": "Кармен: 'Мы сможем остановить их, если будем действовать вместе.'", "background": "find_allies"},
            {"text": "Джек и Кармен разрабатывают план, чтобы уничтожить своих врагов.", "background": "find_allies"},
            {"text": "Они успешно выполняют план, но Кармен погибает в последней схватке.", "background": "find_allies"},
            {"text": "Джек: 'Ты была единственной, кто мне помогал...'", "background": "find_allies"},
            {"text": "Он хоронит Кармен и решает уйти из криминального мира навсегда.", "background": "find_allies"},
        ],
        "choices": [],
        "next": []
    },
    "return_to_game": {
        "sequence": [
            {"text": "Джек решает вернуться и закончить начатое.", "background": "return_to_game"},
            {"text": "Он находит Блейка и требует ответов.", "background": "return_to_game"},
            {"text": "Блейк: 'Ты вернулся. Я знал, что ты не сможешь уйти.'", "background": "return_to_game"},
            {"text": "Джек: 'Это конец, Блейк. Ты больше не будешь мной манипулировать.'", "background": "return_to_game"},
            {"text": "Он убивает Блейка и забирает кейс.", "background": "return_to_game"},
            {"text": "Джек: 'Теперь я свободен.'", "background": "return_to_game"},
            {"text": "Но он понимает, что его жизнь никогда не будет прежней.", "background": "return_to_game"},
        ],
        "choices": [],
        "next": []
    },
    "keep_hiding": {
        "sequence": [
            {"text": "Джек решает продолжать скрываться.", "background": "keep_hiding"},
            {"text": "Он меняет имя, внешность и переезжает в другую страну.", "background": "keep_hiding"},
            {"text": "Джек: 'Теперь я в безопасности. Они никогда не найдут меня.'", "background": "keep_hiding"},
            {"text": "Годы спустя он живёт тихой жизнью, но всегда оглядывается через плечо.", "background": "keep_hiding"},
            {"text": "Однажды он видит в новостях, что его старые враги уничтожены.", "background": "keep_hiding"},
            {"text": "Джек: 'Это конец. Но какой ценой?'", "background": "keep_hiding"},
            {"text": "Он понимает, что его прошлое навсегда останется с ним.", "background": "keep_hiding"},
        ],
        "choices": [],
        "next": []
    }
}
#глобал переменные
# Глобальные переменные
current_scene = "intro"
sequence_index = 0

# Переменные для анимации текста
typing_text = ""  # Текст, который печатается
typing_index = 0  # Индекс текущего символа
last_typing_time = 0  # Время последнего обновления текста
typing_speed = 35  # Скорость печати текста (в миллисекундах)

# Музыка
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение

# Функция для увеличения громкости
def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(min(current_volume + 0.1, 1.0))


# Функция для уменьшения громкости
def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))


def render_scene(scene_key, sequence_index):
    global typing_text, typing_index, last_typing_time
    scene = scenes[scene_key]
    sequence = scene["sequence"]
    frame = sequence[sequence_index]
    screen.blit(backgrounds[frame["background"]], (0, 0))

    # Если текст еще не напечатан полностью
    if typing_index < len(frame["text"]):
        current_time = pygame.time.get_ticks()
        if current_time - last_typing_time > typing_speed:
            typing_text += frame["text"][typing_index]
            typing_index += 1
            last_typing_time = current_time

    text_surface = font.render(typing_text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, TRANSPARENT_BLACK, background_rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def render_choices(scene_key):
    scene = scenes[scene_key]
    screen.blit(backgrounds["black_background"], (0, 0))
    for idx, choice in enumerate(scene["choices"]):
        choice_surface = font.render(f"{idx + 1}. {choice}", True, RED)
        screen.blit(choice_surface, (50, 150 + idx * 50))
    pygame.display.flip()


def main():
    global current_scene, sequence_index, typing_text, typing_index, last_typing_time
    clock = pygame.time.Clock()

    while True:
        if not sequence_index >= len(scenes[current_scene]["sequence"]):
            render_scene(current_scene, sequence_index)
        else:
            render_choices(current_scene)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not sequence_index >= len(scenes[current_scene]["sequence"]):
                        # Сброс анимации текста при переходе к следующему кадру
                        typing_text = ""
                        typing_index = 0
                        sequence_index += 1
                if (event.key in [pygame.K_1, pygame.K_2, pygame.K_3] and
                        sequence_index >= len(scenes[current_scene]["sequence"])):
                    index = event.key - pygame.K_1
                    scene = scenes[current_scene]
                    if index < len(scene["next"]):
                        # Сброс анимации текста при переходе к новой сцене
                        typing_text = ""
                        typing_index = 0
                        current_scene = scene["next"][index]
                        sequence_index = 0
                # Управление громкостью
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Клавиша "+"
                    increase_volume()
                if event.key == pygame.K_MINUS:  # Клавиша "-"
                    decrease_volume()

        clock.tick(30)


if __name__ == "__main__":
    main()
