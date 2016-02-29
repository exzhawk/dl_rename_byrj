# -*- encoding: utf-8 -*-
# Author: Epix
import codecs
import os
import pickle
import re

from lxml import etree

if __name__ == '__main__':
    rj_re = re.compile(r'/(RJ\d*.)\.html')
    offline_dir = 'offline'
    files = os.listdir(offline_dir)
    result_list = []
    result = {}
    for f in files:
        html_file = codecs.open(os.path.join(offline_dir, f), 'r', 'utf8')
        tree = etree.HTML(html_file.read())
        posts = tree.xpath('//table[@class="work_1col_table"]/tr/td/dl[@class="work_1col"]')
        for post in posts:
            try:
                title_element = post.xpath('./dt[@class="work_name"]/a')[0]
                title = unicode(title_element.xpath('./text()')[0])
                url = unicode(title_element.xpath('./@href')[0])
                group = unicode(post.xpath('./dd[@class="maker_name"]/a/text()')[0])
                rj_number = rj_re.search(url).group(1)
                result_list.append({'rj': rj_number, 'title': title, 'group': group})
                result[rj_number] = [title, group]
            except:
                print(post.xpath('./dt[@class="work_name"]/a/@href')[0])

    pickle.dump(result, open('db.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    # with codecs.open('rj.jl', 'w', 'utf8') as f_out:
    #     for p in result:
    #         f_out.write(json.dumps(p, ensure_ascii=False) + '\n')
