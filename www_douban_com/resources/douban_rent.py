#!/usr/bin/env python 
# coding:utf-8
# @Time :11/24/18 17:35

from enum import Enum


class DoubanRent:

    rent_status = ["已租", "删除"]

    bedroom = ["主卧", "次卧"]
    duration = ["长租", "短租"]

    subway = ['登良', '上塘', '太安', '布心', '田贝', '下水径', '水贝', '横岗', '怡景', '坂田', '红岭', '湖贝', '华侨城', '西乡', '海上世界', '安托山', '湾厦', '新安', '香蜜湖', '香梅北', '莲花西', '桃园', '固戍', '大剧院', '前海湾', '岗厦北', '侨香', '燕南', '市民中心', '高新园', '后海', '老街', '车公庙', '水湾', '侨城北', '东角头', '赤湾', '景田', '岗厦', '华强北', '购物公园', '蛇口港', '科学馆', '世界之窗', '机场东', '红树湾', '后瑞', '香蜜', '海月', '白石洲', '东门', '宝安中心', '宝体', '竹子林', '国贸', '福田(暂定名)', '华强路', '新秀', '科苑', '会展中心', '鲤鱼门', '黄贝岭', '深康', '大新', '侨城东', '坪洲', '深大']

    sex = ["男女", "女", "男"]


if __name__ == '__main__':
    print(DoubanRent.bedroom)

    print([i.replace("站", "") for i in DoubanRent.subway])