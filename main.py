import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, ADMIN_ID, CHANNEL_ID
from keyboards import start_keyboards, tasdiqlash_kb, admin_tasdiqlash_kb, contact_kb, razmer_keyboards, menu_keyboards
from database import create_table, insert_data, select, select_data
from states import HodimState, IshJoyiState
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
result_text = ""
result_dict = {}

@dp.message_handler(commands=['start'], state='*')
async def salom_ber(message: types.Message):
    await message.answer(text="🍰 Assalomu aleykum, Aziza_Bakery botga xush kelibsiz!\
         \nKerakli menuni tanlang", reply_markup=start_keyboards)
    
@dp.message_handler(lambda message: message.text=="🍰🧁PISHIRIQLAR MENYUSI")
async def menyu_handler(message: types.Message):
    await message.answer(text="Kerakli pishiriq tanlang:", reply_markup=menu_keyboards)
    await HodimState.tort.set()


menu_buttons = ["🎂To'rt", "🍰Pishiriq", "🎂Bento","Trayfel"],
razmer_buttons = ["5-k", "10-k", "15-k"]

@dp.message_handler(Text(equals=menu_buttons, ignore_case=True), state="*")
async def menu_and_razmer_handler(message: types.Message, state: FSMContext):
    if message.text in menu_buttons:
        if message.text == "🎂To'rt":
            await state.update_data(tort=message.text)
            rasm = types.InputFile("rasmlar/happy_b.jpg", 'rb')
            await message.answer_photo(photo=rasm, caption="🍫🎂Shokolad-To'rt\n\nKerakli razmer tanlang:", reply_markup=razmer_keyboards)
        elif message.text == "🍰Pishiriq":
            await state.update_data(tort=message.text)
            rasm = types.InputFile("rasmlar/pishiriq.jpg", 'rb')
            await message.answer_photo(photo=rasm, caption="🍰Pishiriq\n\nKerakli razmer tanlang:", reply_markup=razmer_keyboards)
        elif message.text == "🎂Bento":
            await state.update_data(tort=message.text)
            rasm = types.InputFile("rasmlar/bento.jpg", 'rb')
            await message.answer_photo(photo=rasm, caption="🎂Bento-To'rt\n\nKerakli razmer tanlang:", reply_markup=razmer_keyboards)
        elif message.text == "Trayfel":
            await state.update_data(tort=message.text)
            rasm = types.InputFile("rasmlar/images.jpeg", 'rb')
            await message.answer_photo(photo=rasm, caption="Trayfel\n\nKerakli razmer tanlang:", reply_markup=razmer_keyboards)

    elif message.text in razmer_buttons:
        await state.update_data(razmer=message.text)
        text = """Zakaz berish uchun ma'lumot kiritishingiz zarur

Telefon raqam jo'nating, va zakazingiz Adminga yuboriladi.💭"""
        await message.answer(text=text, reply_markup=contact_kb)
        await HodimState.telefon.set()
   
     
@dp.message_handler(state=HodimState.telefon, content_types='contact')
async def texnologiya_state(message: types.Message, state: FSMContext):
    global result_text, result_dict

    await state.update_data(telefon=message.contact.phone_number)
    data = await state.get_data()
    result_dict = data
    admin_uchun_text = f"""
🎉 **Yangi Zakaz!** 🎉

📌 **Mahsulot:** {data['tort']}
📏 **Razmer:** {data['razmer']}
📞 **Telefon raqam:** {data['telefon']}

❗ Iltimos, ushbu buyurtmani ko'rib chiqing va mijoz bilan bog'laning. ✅
"""
    result_text = admin_uchun_text
    await bot.send_message(chat_id=ADMIN_ID, text=admin_uchun_text, reply_markup=admin_tasdiqlash_kb)
    await state.finish()
   
   
@dp.message_handler(lambda message: message.text in ["✅👑 HA", "❌👑 YO'Q"], state='*')
async def admin_response_handler(message: types.Message, state: FSMContext):
    global result_text, result_dict


    if message.text == "✅👑 HA": 
        if message.from_user.id != ADMIN_ID:
                await message.answer("Siz admin emassiz! ❌")
                return
        await message.answer("Post tasdiqlandi! ✅\n\nZakaz kanalga yuborildi!", reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(chat_id=CHANNEL_ID, text=result_text)

    elif message.text == "❌👑 YO'Q":
        if message.from_user.id != ADMIN_ID:
            await message.answer("Siz admin emassiz! ❌")
            return
        await message.answer("Post bekor qilindi! ❌")
        result_text = ""
    else:
        if message.from_user.id != ADMIN_ID:
            await message.answer("Boshidan boshlash uchun /start ni bosing", reply_markup=types.ReplyKeyboardRemove())
            return
        else:
            await message.answer("Iltimos, faqat quyidagi tugmalardan birini bosing!", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


if __name__ == '__main__':
 executor.start_polling(dp, skip_updates=True, on_startup=create_table(dp))