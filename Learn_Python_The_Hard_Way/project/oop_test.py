import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "make a class named %%% that is-a %%%.",
    "calss %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params",
    "calss %%%(object):\n\tdef ***(self, @@@)" :
        "class %%% has-a dunction *** that takes self and @@@ params",
    "*** = %%%()" :
        "set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv)  == 2 and sys.argv[1] == "english":
    #len统计sys里的.argc的长度如果等于2且argv里的第一个元素时english则运行下面
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    #urlopen对变量里的连接访问，且通过readlines方法返回行通过word遍历保存
    WORDS.append(str(word.strip(), encoding="utf-8"))
    #word通过strip移除换行符,再通过str将对象转化为适于人阅读的形式。
    print(WORDS)


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    #count方法从snippet中统计%%%的个数n，sample方法从WORDS中随机抽样n个样本形成列表
    other_names = random.sample(WORDS, snippet.count("***"))
    #count方法从snippet中统计***的个数n，sample方法从WORDS中随机抽样n个样本形成列表
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1.3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)
        for word in other_names:
            result = result.replace("***", word, 1)
        for work in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, # QUESTION:

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
