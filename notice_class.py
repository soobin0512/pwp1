# notice_class.py
# 오라클 데이터베이스의 Notice 테이블의 한 행의 정보를 저장할 객체용
# Notice 클래스 제공 모듈

class Notice:
    # 멤버변수 (field)
    # self.필드명 = 초기값 (self. 생략함) => 필드명 = 초기값 (기본은 public)
    # private(비공개) 멤버(필드, 메소드)는 이름 앞에 '_'(underscore)를 2개 붙임
    __notice_no = 0
    __notice_title = ''
    __notice_writer = ''
    __notice_date = ''
    __notice_content = ''
    __notice_upfile = ''
    __readcount = 0

    # 생성자 (constructor)
    # 한 행의 notice 정보를 딕셔너리에 저장해서 객체 생성시
    # 초기값으로 전달받아, 각 필드에 초기값으로 기록 저장함
    def __init__(self, notice_dict):
        self.__notice_no = notice_dict['no']
        self.__notice_title = notice_dict['title']
        self.__notice_writer = notice_dict['writer']
        self.__notice_date = notice_dict['date']
        self.__notice_content = notice_dict['content']
        self.__notice_upfile = notice_dict['upfile']
        self.__readcount = notice_dict['rcount']

    # 소멸자 (destructor)
    def __del__(self):
        pass
        # print(self, ' 인스턴스 소멸됨.')

    # 멤버함수 (method)
    # setter : 각 필드값 변경용 메소드, set_필드명(바꿀값)
    def set_noticeno(self, noticeno):
        self.__notice_no = noticeno

    def set_noticetitle(self, ntitle):
        self.__notice_title = ntitle

    def set_noticewrtier(self, nwriter):
        self.__notice_writer = nwriter

    def set_ntocecontent(self, ncontent):
        self.__notice_content = ncontent

    def set_noticedate(self, ndate):
        self.__notice_date = ndate

    def set_noticeupfile(self, upfile):
        self.__notice_upfile = upfile

    def set_readcount(self, rcount):
        self.__readcount = rcount

    def info(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(self.__notice_no, \
                self.__notice_title, self.__notice_writer, self.__notice_date, \
                self.__notice_content, self.__notice_upfile, self.__readcount)

    def list(self, num):
        if num == 0:
            if self.__notice_no != None:
                return self.__notice_no
            else:
                return ''
        elif num == 1:
            if self.__notice_title != None:
                return self.__notice_title
            else:
                return ''
        elif num == 2:
            if self.__notice_writer != None:
                return self.__notice_writer
            else:
                return ''
        elif num == 3:
            if self.__notice_date != None:
                return self.__notice_date
            else:
                return ''
        elif num == 4:
            if self.__notice_content != None:
                return self.__notice_content
            else:
                return ''
        elif num == 5:
            if self.__notice_upfile != None:
                return self.__notice_upfile
            else:
                return ''
        elif num == 6:
            if self.__readcount != None:
                return self.__readcount
            else:
                return ''
