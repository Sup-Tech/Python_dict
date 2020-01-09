# -*- coding: utf-8 -*-
from aip import AipSpeech
from playsound import playsound
import os

class Voice:
    def __init__(self):
        self.APP_ID = '18038513'
        self.API_KEY = 'qLW1MLgVOa0kfCerl9ZUHDzw'
        self.SECRET_KEY = 'V4klgGVVinFOH7hageuT5oXr2ILIo9yt'
        self.my_file = './'  # 文件路径

    def do_manage(self, text, per):
        client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        # self.get_info = input('Msg>>')
        result = client.synthesis(text, 'zh', 1, {
            'vol': 10,  # 音量0-15，默认5中音量
            'spd': 6,  # 语速0-9，默认5
            'pit': 3,  # 音调0-9，默认5
            'per': per,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            self.file_path = self.my_file + text + ".wav"
            with open(self.file_path, 'wb') as f:
                f.write(result)

        # 读音频文件
        return self.file_path

    def del_v(self):
        os.remove(self.file_path)


# if __name__ == '__main__':
#     # APP_ID = '18038513'
#     # API_KEY = 'qLW1MLgVOa0kfCerl9ZUHDzw'
#     # SECRET_KEY = 'V4klgGVVinFOH7hageuT5oXr2ILIo9yt'
#     text = 'table'
#     re = Voie()
#     re.do_manage(text,1)  # 参数(朗读内容，发音人选择（0-4）)
#     re.del_v()  # 删除建立语音文件
