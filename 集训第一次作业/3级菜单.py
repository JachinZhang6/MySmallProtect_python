#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Jachin Zhang
menu = {
    '广东':{
        '深圳':{
            '龙岗':{
                'didi':{},
                'MD':{},
                'KFC':{},
            },
            '福田':{
                'aiqiyi':{},
                'aili':{},
                'tengxun':{},
            },
            '南山':{
                'boos':{},
                'lagou':{},
                'dajie':{},
            },
        },
        '广州':{
            '白河':{
                'baiyunshang':{},
                'baiyungongyuan':{},
            },
            '九江':{},
            '从化':{},
        },
        '惠州':{},
        '揭阳':{},
    },
    '北京':{
        '一环':{
            '清华':{
                'tushuguan':{},
            }
        },
        '二环':{
            '中关村':{
                'keiguan':{}
            }
        },
        '三环':{},
    },
    '上海':{},
}
current_layer = menu
layers = []
while True:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if not choice:continue
    if choice in current_layer:
        # 进入下一层，保存当前层
        layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if len(layers) != 0:
            # pop()返回最后一层并删除
            current_layer = layers.pop()
        else:
            print("嘿！顶到头啦")
    elif choice == 'q':
        exit('bye')