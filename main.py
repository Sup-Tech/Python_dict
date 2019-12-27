"""
客户端执行文件
"""
from app import ProcessApp


def main():

    pc = ProcessApp()
    pc.start()
    pc.close()


if __name__ == '__main__':
    main()
