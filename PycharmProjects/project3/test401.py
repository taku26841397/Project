import MeCab

mecab_tagger=MeCab.Tagger()
text="私は今日、スーパーで沢山のお菓子を買った。"

mecab_text=mecab_tagger.parse(text)

print(mecab_text)