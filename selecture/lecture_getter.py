# from selecture.lecture_getter import lecture_getter


def lecture_getter():
    url_list = ['http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201329/201329.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201330/201330.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201331/201331.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201332/201332.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201333/201333.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201323/201323.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201324/201324.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201334/201334.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201325/201325.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201326/201326.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201327/201327.html',
                'http://www.ilas.nagoya-u.ac.jp/syllabus/syllabus2017/201328/201328.html']
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq
    from lecture.models import Lecture
    import unicodedata
    for url in url_list:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        lecture_list = page_soup.body.table.findAll("tr")

        for lecture in lecture_list[1:]:
            syllabus = url[:60] + lecture.a["href"]
            code = lecture.findAll("td")[0].text
            year = lecture.findAll("td")[1].text
            day = lecture.findAll("td")[2].text[0]
            time = lecture.findAll("td")[2].text[1]
            point_for = lecture.findAll("td")[3].text
            title = lecture.findAll("td")[4].text
            professor = lecture.findAll("td")[5].text
            target = lecture.findAll("td")[6].text

            if day == '月':
                day = '1'
            if day == '火':
                day = '2'
            if day == '水':
                day = '3'
            if day == '木':
                day = '4'
            if day == '金':
                day = '5'


            professor = professor.replace("　", "").replace(" ", "")
            title = title.replace("　", "").replace(" ", "")
            professor = unicodedata.normalize('NFKC', professor)
            title = unicodedata.normalize('NFKC', title)


            Lecture.objects.create(syllabus=syllabus,lecture_code=code,professor_name=professor,time=time,title=title,lecture_type=point_for,day=day,year='2017',target=target,credit=2)
