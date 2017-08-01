import requests, json
from get_url import *
from tool import *
from dbcontroller import *


class battlelist(object):
    def __init__(self, userid='4006716018', zonepy='dx7', user=None):
        self.userid = userid
        self.zonepy = zonepy
        self.battleid_list = []
        self.battle_list = []
        if (user != None):
            self.userid = user.userid
            self.zonepy = user.zonepy

    def update_list(self):
        r = requests.get(get_battle_list_url(self.zonepy, self.userid))
        j = res_to_dic(r)
        for x in j["game_list"]:
            self.battleid_list.append(x["game_id"])
            b = battle(self.zonepy, self.userid, x["game_id"])
            self.battle_list.append(b)


class battle(object):
    def __init__(self, zonepy, userid, battleid):
        self.zonepy = zonepy
        self.userid = userid
        self.battleid = battleid
        r = requests.get(get_battle_detail_url(self.zonepy, self.userid, self.battleid))
        with open("./battle_details/%s.json" % (str(self.zonepy) + "-" + str(self.battleid)), 'w',
                  encoding='utf-8') as json_file:
            json.dump(r.text, json_file, ensure_ascii=False)
        self.detail = res_to_dic(r)
        r.close()
        print(self.battleid)


if __name__ == "__main__":
    b = battlelist()
    b.update_list()
    print(len(b.battle_list))