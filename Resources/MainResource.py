from flask_restful import Resource, reqparse
import random, string

dic = {}
cnt = 0
n = 6


class LongShort(Resource):
    @classmethod
    def find_random(cls):
        global dic, cnt, n
        res = ""
        for i in range(n):
            res += random.choice(string.ascii_letters+string.digits)
        if res in dic:
            cnt += 1
            if cnt == 100000000:
                n += 1
                cnt = 0
                if n > 10:
                    return "Exhausted! or Is It ?"
            LongShort.find_random()
        return res

    def get(self):
        global dic
        _user_parser = reqparse.RequestParser()
        _user_parser.add_argument('LongShort', type=str, required=True, help="field cannot be empty")
        data = _user_parser.parse_args()
        rand = LongShort.find_random()
        dic[rand] = data['LongShort']
        print(dic)
        return {data['LongShort']: "myshortner.ly/"+rand}, 200


class ShortLong(Resource):

    def get(self):
        global dic
        _user_parser = reqparse.RequestParser()
        _user_parser.add_argument('ShortLong', type=str, required=True, help="field cannot be empty")
        data = _user_parser.parse_args()

        if dic[data['ShortLong']]:
            return {data['ShortLong']: dic[data['ShortLong']]}, 200
        else:
            return {"message": "not found"}, 404
