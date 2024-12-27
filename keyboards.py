
from aiogram import types

start_keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton("🍰🧁PISHIRIQLAR MENYUSI"),
        types.KeyboardButton("MA'LUMOTLAR"),
    ]
    ]
)

menu_keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton("🎂To'rt"),types.KeyboardButton("🍰Pishiriq"),types.KeyboardButton("🎂Bento"),types.KeyboardButton("Trayfel")
    ]])

razmer_keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton("5-k"),types.KeyboardButton("10-k"),types.KeyboardButton("15-k"),
       
    ]])

tasdiqlash_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton("✅ HA"), types.KeyboardButton("❌ YO'Q")
    ]
])


admin_tasdiqlash_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton("✅👑 HA"), types.KeyboardButton("❌👑 YO'Q")
    ]
])

contact_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton(text="📞 Telefon raqamingizni yuborish", request_contact=True)
    ]
])
