import os
import sys
import webbrowser

BASE_PATH = os.path.abspath('.')


def run_main():
    sys.path.append("libs")
    url = 'http://127.0.0.1:8000/index/'
    webbrowser.open_new(url)
    main = BASE_PATH + "dist/manage/manage.exe runserver 8000 --noreload"
    print('--------------------------')
    print('Welcome!')
    print('--------------------------')
    os.system(main)


run_main()
