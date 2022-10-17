import time

import requests
import parsel
import yagmail




def data():
    # 获取最新章节
    url = 'https://www.biquge9.com/book/1854/'
    html_data = requests.get(url=url).text
    return html_data


def parasel(html_data):
    # 转换对象
    selector = parsel.Selector(html_data)
    new_name = selector.css('.small :nth-child(4) a::text').get()
    # new_url = 'https://www.biquge9.com/' + selector.css('.small :nth-child(4) a::attr(href)').get()
    return new_name


# def save(new_name, new_url):
#     # 小说保存
#     html_data1 = requests.get(url=new_url).text
#     selector1 = parsel.Selector(html_data1)
#     novel = selector1.css('#chaptercontent::text').getall()
#     with open(f'{new_name}.txt', 'w', encoding='utf-8') as f:
#         for text in novel:
#             f.write(text)
#             f.write('\n')


def mail(new_name):
    # 将保存好的小说发送邮箱
    data = {
        'user': '2287585490@qq.com',
        'password': 'hmvcntwbmcdtecei',
        'host': 'smtp.qq.com'
    }
    yag = yagmail.SMTP(user=data['user'], password=data['password'], host=data['host'])
    contents = ''
    yag.send(to='2644276156@qq.com', subject=f'小说更新了,更新章节：{new_name}', contents=contents)


def renew():
    html_data = data()
    new_name = parasel(html_data)
    # 判断是否更新
    if new_name not in name_list:
        name_list.append(new_name)
        # save(new_name, new_url)
        mail(new_name)


if __name__ == '__main__':
    # 定义一个章节容器
    name_list = []
    count = 1
    while 1:
        count += 1
        renew()
        time.sleep(600)
        if count > 7:
            name_list = []
