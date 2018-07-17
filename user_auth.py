
from flask import Flask
from flask_restful import Resource,Api
from flask_restful import reqparse

app=Flask(__name__)
api=Api(app)

parser=reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('passwd')

class User:
    def __init__(self,username,id,passwd,roleid):
        self.username=username
        self.id=id
        self.passwd=passwd
        self.roleid=roleid

userlist=[]

class Login(Resource):
    def get(self):
        return ([user.__dict__ for user in userlist])

    def post(self):
        args=parser.parse_args()
        user=User(1,args['username'],args['passwd'],1);

        userlist.append(user)

        return{'username':user.username}

api.add_resource(Login,'/logins')

if __name__ == '__main__':
    app.run(debug=True)

