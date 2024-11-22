import MeCab


mecab_tagger=MeCab.Tagger()
text="私は今日、スーパーで沢山のお菓子を買った。"
node=mecab_tagger.parseToNode(text)
print(node)

while node:
    print(f'{node.surface}\t{node.posid}\t{node.feature}')
    node=node.next