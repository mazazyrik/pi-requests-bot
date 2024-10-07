from aiogram.fsm.state import State, StatesGroup


class Request(StatesGroup):
    message = State()
