import requests
from aiogram import types
from loader import dp, bot
from filters.private_filter import IsPrivates


@dp.message_handler(text='📖Quron')
async def list_quran_name(ms: types.Message):
    msg = f"1: Al-Fotiha✅\n"
    msg += f"2: Al-Baqara✅\n"
    msg += f"3: Aal-i-Imraan✅\n"
    msg += f"4: An-Nisaa✅\n"
    msg += f"5: Al-Maaida✅\n"
    msg += f"6: Al-An'aam✅\n"
    msg += f"7: Al-A'raaf✅\n"
    msg += f"8: Al-Anfaal✅\n"
    msg += f"9: At-Tawba✅\n"
    msg += f"10: Yunus✅\n"
    msg += f"11: Hud✅\n"
    msg += f"12: Yusuf✅\n"
    msg += f"13: Ar-Ra'd✅\n"
    msg += f"14: Ibrahim✅\n"
    msg += f"15: Al-Hijr✅\n"
    msg += f"16: An-Nahl✅\n"
    msg += f"17: Al-Israa✅\n"
    msg += f"18: Al-Kahf✅\n"
    msg += f"18: Al-Kahf✅\n"
    msg += f"19: Maryam✅\n"
    msg += f"20: Taa-Haa✅\n"
    msg += f"21: Al-Anbiyaa✅\n"
    msg += f"22: Al-Hajj✅\n"
    msg += f"23: Al-Muminoon✅\n"
    msg += f"24: An-Noor✅\n"
    msg += f"25: Al-Furqaan✅\n"
    msg += f"26: Ash-Shu'araa✅\n"
    msg += f"27: An-Naml✅\n"
    msg += f"28: Al-Qasas✅\n"
    msg += f"29: Al-Ankaboot✅\n"
    msg += f"30: Ar-Room✅\n"
    msg += f"31: Luqman✅\n"
    msg += f"32: As-Sajda✅\n"
    msg += f"33: Al-Ahzaab✅\n"
    msg += f"34: Saba✅\n"
    msg += f"35: Faatir✅\n"
    msg += f"36: Yaseen✅\n"
    msg += f"37: As-Saaffaat✅\n"
    msg += f"38: Saad✅\n"
    msg += f"39: Az-Zumar✅\n"
    msg += f"40: Ghafir✅\n"
    msg += f"41: Fussilat✅\n"
    msg += f"42: Ash-Shura✅\n"
    msg += f"43: Az-Zukhruf✅\n"
    msg += f"44: Ad-Dukhaan✅\n"
    msg += f"45: Al-Jaathiya✅\n"
    msg += f"46: Al-Ahqaf✅\n"
    msg += f"47: Muhammad✅\n"
    msg += f"48: Al-Fath✅\n"
    msg += f"49: Al-Hujuraat✅\n"
    msg += f"50: Qaaf✅\n"
    msg += f"51: Adh-Dhaariyat✅\n"
    msg += f"52: At-Tur✅\n"
    msg += f"53: An-Najm✅\n"
    msg += f"54: Al-Qamar✅\n"
    msg += f"55: Ar-Rahmaan✅\n"
    msg += f"56: Al-Waaqia✅\n"
    msg += f"57: Al-Hadid✅\n"
    msg += f"58: Al-Mujaadila✅\n"
    msg += f"59: Al-Hashr✅\n"
    msg += f"60: Al-Mumtahana✅\n"
    msg += f"61: As-Saff✅\n"
    msg += f"62: Al-Jumu'a✅\n"
    msg += f"63: Al-Munaafiqoon✅\n"
    msg += f"64: At-Taghaabun✅\n"
    msg += f"65: At-Talaaq✅\n"
    msg += f"66: At-Tahrim✅\n"
    msg += f"67: Al-Mulk✅\n"
    msg += f"68: Al-Qalam✅\n"
    msg += f"69: Al-Haaqqa✅\n"
    msg += f"70: Al-Ma'aarij✅\n"
    msg += f"71: Nooh✅\n"
    msg += f"72: Al-Jinn✅\n"
    msg += f"73: Al-Muzzammil✅\n"
    msg += f"74: Al-Muddaththir✅\n"
    msg += f"75: Al-Qiyaama✅\n"
    msg += f"76: Al-Insaan✅\n"
    msg += f"77: Al-Mursalaat✅\n"
    msg += f"78: An-Naba✅\n"
    msg += f"79: An-Naazi'aat✅\n"
    msg += f"80: Abasav\n"
    msg += f"81: At-Takwir✅\n"
    msg += f"82: Al-Infitaar✅\n"
    msg += f"83: Al-Mutaffifin✅\n"
    msg += f"84: Al-Inshiqaaq✅\n"
    msg += f"85: Al-Burooj✅\n"
    msg += f"86: At-Taariq✅\n"
    msg += f"87: Al-A'laa✅\n"
    msg += f"88: Al-Ghaashiya✅\n"
    msg += f"89: Al-Fajr✅\n"
    msg += f"90: Al-Balad✅\n"
    msg += f"91: Ash-Shams✅\n"
    msg += f"92: Al-Lail✅\n"
    msg += f"93: Ad-Dhuhaa✅\n"
    msg += f"94: Ash-Sharh✅\n"
    msg += f"95: At-Tin✅\n"
    msg += f"96: Al-Alaq✅\n"
    msg += f"97: Al-Qadr✅\n"
    msg += f"98: Al-Bayyina✅\n"
    msg += f"99: Az-Zalzala✅\n"
    msg += f"100: Al-Aadiyaat✅\n"
    msg += f"101: Al-Qaari'a✅\n"
    msg += f"102: At-Takaathur✅\n"
    msg += f"103: Al-Asr✅\n"
    msg += f"104: Al-Humaza✅\n"
    msg += f"105: Al-Fil✅\n"
    msg += f"106: Quraish✅\n"
    msg += f"107: Al-Maa'un✅\n"
    msg += f"108: Al-Kawthar✅\n"
    msg += f"109: Al-Kaafiroon✅\n"
    msg += f"110: An-Nasr✅\n"
    msg += f"111: Al-Masad✅\n"
    msg += f"112: Al-Ikhlaas✅\n"
    msg += f"113: Al-Falaq✅\n"
    msg += f"114: An-Naas✅\n"
    await ms.answer(msg)
    await ms.answer(f"Sizga kerakli surani tartib raqamini krirting...")
    await bot.delete_message(chat_id=ms.chat.id, message_id=ms.message_id)


@dp.message_handler(IsPrivates())
async def text(ms: types.Message):
    try:
        number = int(ms.text)
        if 1 < number <= 11:
            res = requests.get(f"https://api.alquran.cloud/v1/surah/{number}").json()
            response = res['data']['ayahs']
            name = res['data']['name']
            chunk_size = len(response) // 22  # Taqribiy qism soni
            chunk_sizes = len(response) % 22  # Taqribiy qism soni
            qisimlar = [response[i:i + chunk_size + chunk_sizes] for i in range(0, len(response), chunk_size)]
            await ms.answer(f"{number}: {name}")
            for qism in qisimlar:
                qism_text = ' '.join([ayah['text'] for ayah in qism])
                await ms.answer(f"{qism_text}")
        elif 11 <= number <= 30:
            res = requests.get(f"https://api.alquran.cloud/v1/surah/{number}").json()
            response = res['data']['ayahs']
            name = res['data']['name']
            chunk_size = len(response) // 10  # Taqribiy qism soni
            chunk_sizes = len(response) % 10  # Taqribiy qism soni
            qisimlar = [response[i:i + chunk_size + chunk_sizes] for i in range(0, len(response), chunk_size)]
            await ms.answer(f"{number}: {name}")
            for qism in qisimlar:
                qism_text = ' '.join([ayah['text'] for ayah in qism])
                await ms.answer(f"{qism_text}")
        elif 70 >= number >= 50:
            res = requests.get(f"https://api.alquran.cloud/v1/surah/{number}").json()
            response = res['data']['ayahs']
            name = res['data']['name']
            chunk_size = len(response) // 8  # Taqribiy qism soni
            chunk_sizes = len(response) % 8  # Taqribiy qism soni
            qisimlar = [response[i:i + chunk_size + chunk_sizes] for i in range(0, len(response), chunk_size)]
            await ms.answer(f"{number}: {name}")
            for qism in qisimlar:
                qism_text = ' '.join([ayah['text'] for ayah in qism])
                await ms.answer(f"{qism_text}")
        elif number == 1:
            res = requests.get(f"https://api.alquran.cloud/v1/surah/{number}").json()
            response = res['data']['ayahs']
            name = res['data']['name']
            await ms.answer(f"{number}: {name}")
            txt = str()
            for oyat in response:
                txt += (oyat['text'])
            await ms.answer(txt)
        elif number >= 70:
            res = requests.get(f"https://api.alquran.cloud/v1/surah/{number}").json()
            response = res['data']['ayahs']
            name = res['data']['name']
            await ms.answer(f"{number}: {name}")
            txt = str()
            for oyat in response:
                txt += oyat['text']
            await ms.answer(txt)
        elif number > 114:
            await ms.answer(f"Bunday Sura mavjud emas!")

        surah = '{:03}'.format(int(number))
        res = requests.get(f"https://server8.mp3quran.net/afs/{surah}.mp3")
        await ms.answer_audio(audio=res.url)
    except Exception as err:
        print(f"Xatolik {err}")





