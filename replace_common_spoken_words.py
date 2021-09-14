
def replace_common_spoken_words():
    common_spoken_words = {"嗯","呃","啊","哈","就是","这个","那","然后","的话","吧","就","呢","噢"}
    global data
    with open('9.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for common_word in common_spoken_words:
            data = str(data).replace(common_word, "")
        data = str(data).replace("，，","，")
        data = str(data).replace("。", "，")

        print(data)
        return data


data_after_replaced = replace_common_spoken_words()

with open('9-1.txt', 'w', encoding='utf-8') as f:
    f.write(data_after_replaced)
