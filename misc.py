import random


names = ['Alex', 'Matvey', 'Dima', 'Julia', 'Lila']


def chose_work_name() -> str:
    """
    Exact names from chat (future)

    :return:
    """
    return random.choice(names)


async def send_message(msg) -> None:
    await msg.answer(f'Next activity maker will be: __{chose_work_name()}__')


