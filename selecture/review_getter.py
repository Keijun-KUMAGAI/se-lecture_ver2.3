# from selecture.review_getter import review_getter



def review_getter():
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq
    from lecture.models import Lecture
    from review.models import Review
    from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
    import unicodedata
    url = 'http://meidaisei.undo.jp/?paged='
    for i in range(1,81):
        my_url = url + str(i)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        for lecture in page_soup.findAll("div",{"class":"panel"})[0:]:
            if lecture.div.h4  == None or lecture.div.h4  == "":
                title = 'ブラックリストより取得のため、データ無し'
            else:
                title = lecture.div.h4.text
            if lecture.div.strong.a == None:
                professor = 'ブラックリストより取得のため、データ無し'
            else:
                professor = lecture.div.strong.a.text
            if lecture.div.findAll("span")[1].a == None:
                year = lecture.div.findAll("span")[1].a
            else:
                year = lecture.div.findAll("span")[1].a.text
            if lecture.div.span.a == None:
                lecture_type = lecture.div.span.a
            else:
                lecture_type = lecture.div.span.a.text
            if lecture.div.findAll("span")[2].a==None:
                semester = lecture.div.findAll("span")[2].a
            else:
                semester = lecture.div.findAll("span")[2].a.text
            rate_professor = lecture.div.findAll("span",{"class":"tl-content"})[0].a["href"][-1]
            rate_pass = lecture.div.findAll("span",{"class":"tl-credit"})[0].a["href"][-3:]
            if rate_pass == 't=5':
                rate_pass = 100
            if rate_pass == 't=4' or rate_pass == '1-6':
                rate_pass = 90
            if rate_pass == 't=3':
                rate_pass = 80
            if rate_pass == 't=2':
                rate_pass = 70
            if rate_pass == '1-3' or rate_pass == '1-4' or rate_pass == '1-5' or rate_pass == 't=1':
                rate_pass = 60
            if rate_professor == '5':
                rate_professor = 100
            if rate_professor == '4':
                rate_professor = 90
            if rate_professor == '3':
                rate_professor = 80
            if rate_professor == '2':
                rate_professor = 70
            if rate_professor == '1':
                rate_professor = 60
            if lecture_type == 'その他' or lecture_type == None:
                lecture_type = '不明'
            if lecture_type != "開放科目":
                lecture_type = lecture_type.replace("科目","")
            comment = lecture.div.p.text.strip()

            professor = professor.replace("　", "").replace(" ", "")
            title = title.replace("　", "").replace(" ", "")
            professor = unicodedata.normalize('NFKC', professor)
            title = unicodedata.normalize('NFKC', title)

            comment = unicodedata.normalize('NFKC', comment)
            year = year + semester
            print(lecture_type)
            try:
                lecture = Lecture.objects.get(title__icontains=title,professor_name__icontains=professor)
            except ObjectDoesNotExist:
                lecture = Lecture.objects.create(title=title,professor_name=professor,year=year,lecture_type=lecture_type,credit=2)
            except MultipleObjectsReturned:
                lecture = Lecture.objects.filter(title__icontains=title,professor_name__icontains=professor).first()
            Review.objects.create(comment=comment,rate_pass=rate_pass,rate_professor=rate_professor,lecture=lecture,title='From Black List')
