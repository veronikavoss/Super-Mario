from setting import *

class Map:
    def __init__(self):
        # self.stage={'1':{'1':[['_' for _ in range(176)] for _ in range(29)]}}
        # self.stage['1']['1'][24][0]='p'
        # self.stage['1']['1'][26][0]='0'
        # self.stage['1']['1'][25][8]='g'
        # self.stage['1']['1'][27][0]='h'
        
        # self.stage={'1':{'1':[]}}
        with open(os.path.join(CURRENT_PATH,'map_data.txt'),'r') as r:
            self.stage={'1':{'1':[list(data.strip()) for data in r.readlines()]}}
            # for data in r.readlines():
            #     self.stage['1']['1'].append(list(data.strip()))
        #     for i in range(27):
        #         for j in range(176):
        #             pass
        
        # self.stage['1']['1'][24][0]='p'
        # self.stage['1']['1'][26][0]='0'
        # self.stage['1']['1'][25][8]='g'
        # self.stage['1']['1'][27][0]='h'
        # self.stage={'1':{
            # '1':[
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________'),
            #     list('_p______________________________________________________________________________________________________________________________________________________________________________'),
            #     list('1_______012__g_2________________________________________________________________________________________________________________________________________________________________'),
            #     list('0111111144411112________________________________________________________________________________________________________________________________________________________________'),
            #     list('h_______________________________________________________________________________________________________________________________________________________________________________'),
            #     list('________________________________________________________________________________________________________________________________________________________________________________')
            #     ]
            # }}

stage={'1':{'1':[]}}
with open(os.path.join(CURRENT_PATH,'map_data.txt'),'r') as r:
    data=r.readlines()
    for i in data:
        print(list(i.strip()))
    # for i in range(27):
    #     for j in range(176):
    #         pass
