# -*- coding: utf-8 -*-
#Програма кодирования/декодирования файлов

#Первичная обработка методом Барроуза-Уиллера
#Далее обработка стопкой книг
#Кодирование осуществляется кодом Хаффмана

#Загрузка необходимых библиотек:

from functools import reduce
import string
import math
import queue
import pickle

#Создадим класс, который будет использовать преобразование Барроуза-Уиллера:

class My_Burrows_Wheeler:
    
    def __init__(self, data):
        
        self.data = data

    def transform(self):

        # Зададим размер данных
        size = len(self.data)

        # Увеличиваем размер данных для совершения преобразования
        self.data *= 2

        # Вращаем данные по индексу, затем сортируем их. Переменная, которая будет хранить эти данные, является словарем:
        rotation = sorted(range(size), key=lambda i: self.data[i:])

        # "Запоминаем" индекс оригинальной строки
        index = rotation.index(0)
        
        # Добавляем индекс к конечной таблице, спец. символ для выделения индекса и саму таблицу. Функция вернет эти данные.
        return str(index) +'Ę'+ ''.join(self.data[(i - 1 + size) % size] for i in rotation)
        

    def restore(self):

        # Получаем индекс оригинальной строки из декодируемых данных. Определение происходит с помощью поиска спец. символа:
        search_original = next(i for i in range(len(self.data)-1) if self.data[i] == 'Ę')

        #Получаем индекс спец. символа. Данное действие необходимо для того, чтобы выделить номер оригинальной строки в данных:
        special_index = (self.data).find('Ę')


        # Присваиваем индекс
        index = self.data[:special_index]

        # Получаем зашифрованные данные:
        index = int(index)
        original_data = self.data[search_original + 1:]
        size = len(original_data)

        # Прокручиваем данные:
        lshift = [i for symbol in sorted(set(original_data)) for i, x in enumerate(original_data) if x == symbol]

        # Восстанавливаем иссходные данные:
        restored = ''
        for i in range(size):
            index = lshift[index]
            if index >= size: break
            restored += original_data[index]

        # Возвращаем исходные данные:
        return restored

#Создадим класс, который будет совершать кодирование и декодирование по алгоритму Хаффмана:
class Node:

    #Получаем данные:
    def __init__(self, x, k=-1, l=None, r=None, c=''):
        self.freq = x
        self.key = k
        self.left = l
        self.right = r
        self.code = c
    def __lt__(self, otr):
        return self.freq < otr.freq

#Кодирование с помощью алгоритма Хаффмана:
def huffman_code(data):

    #Таблица частот символов
    freq_Table = {}

    #Список, содержащий узлы:
    node_List = []

    #Очередь:
    que = queue.PriorityQueue()

    #Кодовая таблица:
    code_Table = {}
    
    # Определение частоты символа в данных:
    for n in data:
        if n in freq_Table:
            freq_Table[n] += 1
        else:
            freq_Table[n] = 1
    
    # Дерево Хаффмана:
    for k,v in freq_Table.items():
        node_List.append(Node(v,k))
        que.put(node_List[-1])
        
    # Построение дерева Хаффмана:
    while que.qsize()>1:
        n1 = que.get()
        n2 = que.get()
        n1.code = '1'
        n2.code = '0'
        nn = Node(n1.freq+n2.freq,l=n1,r=n2);
        node_List.append(nn);
        que.put(node_List[-1])

    # Составление кодовой таблицы:
    def bl(p,codestr=[]):
        codestr.append(p.code)
        if p.left:
            bl(p.left,codestr.copy())
            bl(p.right,codestr.copy())
        else:
            code_Table[p.key]=''.join(codestr)
    bl(node_List[-1])
    
    return code_Table

# Функция декодирования с помощью алгоритма Хаффмана:
def huffman_decode (encoded, code):

    # Создадим массив, который будет содержать выходные данные и строку, которая будет сравниваться с кодовой таблицей:
    end_massiv = []
    help_string = ""
    for ch in encoded:
        help_string += ch
        for dec_ch in code:
            if code.get(dec_ch) == help_string:
                end_massiv.append (dec_ch)
                help_string =""
                break

    return end_massiv

#Данная функция позволяет считывать файл блоками определенного размера (в данной програме размер блока = 42КВ)
def read_in_chunks(file_object, chunk_size=43008):
    while True:
        data = file_object.read(chunk_size).decode('utf-8', 'ignore')
        if not data:
            break
        yield data

#Сортировка с помощью метода стопка книг:
def move_2_front_encoder(data, alvafit):
    return [[alvafit.index(ch), alvafit.insert(0, alvafit.pop(alvafit.index(ch)))][0] for ch in data]

#Восстановление с помощью метода стопки книг:
def move_2_front_dencoder(data, alvafit):
    return ''.join([alvafit[i], alvafit.insert(0, alvafit.pop(i))][0] for i in data)

#Символы русского алфавита и другие, встречающиеся символы:
rus_alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯїѕЅј»є№·¶µґіІ±°Ї®¬«Є©§¦Ґ¤ЈўЎџћќњ›љ™—–•”“’‘ЂЏЋЌЊ‹Љ‰€‡†ºþ…„ѓ‚ЃЂ \x99\x9c\x9a¨¼҈ۄȨé۰\x8f\x85\x97\x9eÿäɀ\x80ǀ\x98\xad\x93£\x8dļ׀\x8eψ\x83\x90¢\x92\x84¯ľ¡\x96\x87Ϩ\x91\x9d²Ȍ\x89נ¿ڀ\x8aÐ³ռ\x94Ұ\x82ƠӄĴ½\u0600װɜ\x81ڬ\x8b¥ڴÄȸ¾Ǆ\u058cÓـ´݀ݸ\x86\u0590̀'Ĥ\x9bτذՔݏĘπϟϏχߟ߁ϾߏϿσހÀ߀燏營烿ǁ翀߃߇߾߿ǾǏǟǿǇϞǜǌß珏矜燀Ǽ぀ǈ燇燃珟ǎǞヿǰǃះñÞϘϼ߆߸Çￏ矟㏟߱Ǹ灏ρώ珀ʀ ƀЀΈŨȤڔɌ΀ܬǠƐ̀Ҩ¸ΌˀܼÌʌެĸȀʜˬÊÖÒָϐüãÃÚâÆùêӰÉμΤݴªԼθԜõÙÏëÔɴÑڈçæÝ×îÁËÍÎÕÅׄʄՀʹېûȘݐŔȬҸݔĐĽ׼ěĺĮđàޤíݜˌ݄úƘŜѼΜ̄ĬӀèØԌ͔¹אϴѐŤ֬ոՠ߬ͬ٠ĄŸ֜ӼÈɄŬΠظŀӔشɐۀք̐Ġ˼֤״̈Â҄؈ƴóøòżԤ߰ð׌̜̤ҬٜӸۨ܀å΄Ր٨ïΨҀìÛٸȐܜ٬րԀݬƨ܄ߌհ԰ݘӜܤڤǤ̼۬Ѩ̠ӌܨۈɠӤ׈פň͌ޘވѤִȔưʐ׬̌ͼلܴؤ͈ݭѠ쭜ݠʭ֡ԭ瑭敭䑭葭歐孌έԦԧլխ쑭ژȑѬݫѭ֭߭ѫիԽݼ֪֠׭ߘ֫ܕȏʏƏӈܒԫϩԝ޸݉ӠԠ㟼̓ŎŋɓƃѣƱǋŞӞ֘ٙٚ湮Ӂ҂ѩɡǑӮ݁Ҡ瀀Ω쩍詍ꩍةب̨쨝ꨤꨓꨑꨢʒȒʨܩ멿䨙Ԩѷ֨䨝Ԑΰ̲Βര媞ڨ訇ꨄꨌިĨĒ쨪谮Բ޲޴쨇쨊̒ΐƩ訌쨄ȩ訧ؐޒҒԒԞްְܰީਥҩ쩏쩳詹驹꩹멹詿驿ꩿ쩿ꩀ"

#Символы ASCII с 0 по 127:
eng_alf = ''.join([chr(i) for i in range(128)])

#Общий алфавит:
alfavit = list(eng_alf + rus_alf)



#________________________
#Получение файла на вход:
info_in = input('Введите, пожалуйста, адрес к файлу и его наименование в формате "Путь/Имя файла", название выходного файла и тип операции: Кодирование (Code)/ Декодирование (Decode) или "end", для выхода из программы: ').split()



#if len(info_in) > 1:
#    adress_file_in = info_in[0]
#    adress_file_out = info_in[1]
#    if adress_file_in[-4:] != '.RVM':
#        operation = 'Code'
#        adress_file_out = adress_file_out + '.RVM'
#    else:
#        operation = 'Decode'
#        adress_file_in = adress_file_in + '.'

adress_file_in = info_in[0]
adress_file_out = info_in[1] 
operation = info_in[2]
#operation = info_in[2]

#print(adress_file_in)
nomer = 1

while adress_file_in != 'end':
    if operation == 'Code':
        print("Программа начала выполнение, ожидайте...")
        op = 0
        with open(adress_file_in, "rb") as f_in:
            for chunk in read_in_chunks(f_in):
                
                #Осуществим преобразование Барроуза-Уиллера:
                e = My_Burrows_Wheeler(chunk)
                q = e.transform()

                #Осуществим преобразование методом "Стопка книг":
                encode = move_2_front_encoder(q, alfavit[::])

                #Составим кодовую таблицу с помощью алгоритма Хаффмана:
                dictionary = huffman_code(encode)

                #Закодируем данные с помощью кодовой таблицы:
                my_code = '1' + "".join(dictionary[ch] for ch in encode)

                #Запишем данные в файл:
                f_out = open(adress_file_out, "ab")
                n = int(my_code,2)
                g = n.to_bytes((n.bit_length() + 7) // 8, 'big')
                f_out.write(g)
                f_out.close()
                
                #Добавим спец. символы, которые будут отделять зашифрованные данные от кодовой таблицы, т.к. таблица также содержится в файле:
                f_out = open(adress_file_out, "a", encoding="utf-8")
                f_out.write(chr(255)*2)
                f_out.close()

                #Добавим кодовую таблицу, полученную с помощью алгоритма Хаффмана:
                a = open(adress_file_out, "a")
                for key,val in dictionary.items():
                    a.write('{}:{}\n'.format(key,val))
                a.close()

                #Добавим спец. символы, которые отмечают конец кодовой таблицы:
                f_out = open(adress_file_out, "a", encoding="utf-8")
                f_out.write(chr(270)*2)
                f_out.close()
                op = op +1
                print('Выполнен этап № ', op)

                #v  = open('12345', "a")
                #v.write('Номер ')
                #v.write(str(nomer))
                #v.write(str(encode))
                #v.close()


    else:
        code = ''
        dictionary = ''
        nomer_dec = 0
        #with open(adress_file_in, "rb") as f_in, open(adress_file_out, "w", encoding="utf-8") as f_out:
        with open(adress_file_in, "rb") as f_in, open(adress_file_out, "wb") as f_out:
            print("Декодер начал работу...")
            file = f_in.read()
            schet = 0
            op = 0
            #Определяем конец данных и начала кодовой таблицы для них:
            for i in range(len(file)-3):
                if file[i] == 195:
                    if file[i+1] == 191:
                        if file[i+2] == 195:
                            if file[i+3] == 191:
                                code = file[schet:i]
                                code = bin(int.from_bytes(code, 'big'))
                                point = i + 4

                #Выделяем кодовую таблицу и преобразовываем ранее выделенные данные в исходные:
                if file [i] == 196:
                    if file[i+1] == 142:
                        if file [i+2] == 196:
                            if file[i+3] == 142:
                                b = open(adress_file_in,'rb')
                                g = b.read()[point:i]
                                g = str(g)
                                g = g.replace('\\r\\n', ' ')
                                g = g[2:-1]
                                dictionary = {}
                                f = ''
                                for j in g:
                                    if j != ' ':
                                        f = f + j
                                    else:
                                        key, val = f.strip().split(':')
                                        dictionary[int(key)] = val
                                        f = ''
                                schet = i+4
                                code = code[3:]

                                #Совершаем обратное декодирования с помощью алгоритма Хаффмана:
                                massiv = huffman_decode(code, dictionary)

                                nomer_dec = nomer_dec + 1

                                #Совершаем обратное преобразование методом "Стопка книг":
                                decode = move_2_front_dencoder(massiv, alfavit[::])

                                #Совершаем обратное преобразование методом Барроуза-Уиллера:
                                my_bwt = My_Burrows_Wheeler(decode)
                                
                                #Записываем восстановленные данные в файл:
                                f_out.write(my_bwt.restore())

                                op = op +1
                                print('Выполнен этап № ', op)

                                #print(massiv)
    
    print('Операция завершена')
    info_in = input('Введите, пожалуйста, адрес к файлу и его наименование в формате "Путь/Имя файла", название выходного файла и тип операции: Кодирование (Code)/ Декодирование (Decode) или "end", для выхода из программы: ').split()
    adress_file_in = info_in[0]
    adress_file_out = info_in[1] 
    operation = info_in[2]

    #if len(info_in) > 1:
    #    adress_file_in = info_in[0]
    #    adress_file_out = info_in[1]
    #    if adress_file_in[-4:] != '.RVM':
    #        operation = 'Code'
    #        adress_file_out = adress_file_out + '.RVM'
    #    else:
    #        operation = 'Decode'
    #        adress_file_in = adress_file_in[:-4]

print('Выключение программы')