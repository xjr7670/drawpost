#-*- coding: utf-8 -*-

import os

img_lists = os.listdir('./images')
#print(img_lists)
img_tag_tpl = """   <div class="col-md-3 img">
        <img src="{addr}" />
    </div>
"""

span_tag_tpl = """  <div class="col-md-3 img">
        <span class="text-primary">{year}年{month}月{day}日<br>{name}</span>
    </div>
"""

def make_tpl(image_title):
    src = './images/' + image_title
    date, name = image_title.split(' ')
    year = '20' + date[:2]
    month = date[2:4]
    day = date[4:]
    name = name.split('.')[0]
    return (src, (year, month, day, name))

for idx in range(0, len(img_lists), 4):
    
    img = '<div class="row">\n'
    span = '<div class="row">\n'
    src1, meta1 = make_tpl(img_lists[idx])
    img_tag1 = img_tag_tpl.format(addr=src1)
    span_tag1 = span_tag_tpl.format(year=meta1[0], month=meta1[1], day=meta1[2], name=meta1[3])
    img += img_tag1
    span += span_tag1
    src2, meta2 = make_tpl(img_lists[idx+1])
    img_tag2 = img_tag_tpl.format(addr=src2)
    span_tag2 = span_tag_tpl.format(year=meta2[0], month=meta2[1], day=meta2[2], name=meta2[3])
    img += img_tag2
    span += span_tag2
    src3, meta3 = make_tpl(img_lists[idx+2])
    img_tag3 = img_tag_tpl.format(addr=src3)
    span_tag3 = span_tag_tpl.format(year=meta3[0], month=meta3[1], day=meta3[2], name=meta3[3])
    img += img_tag3
    span += span_tag3
    src4, meta4 = make_tpl(img_lists[idx+3])
    img_tag4 = img_tag_tpl.format(addr=src4)
    span_tag4 = span_tag_tpl.format(year=meta4[0], month=meta4[1], day=meta4[2], name=meta4[3])
    img += img_tag4 + '</div>'
    span += span_tag4 + '</div>\n<hr>'
    print(img + "\n")
    print(span)