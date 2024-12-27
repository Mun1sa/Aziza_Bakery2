from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class HodimState(StatesGroup):
    tort = State()
    razmer = State()
    telefon = State()


class IshJoyiState():
    pass