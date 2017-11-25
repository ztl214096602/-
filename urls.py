# coding:utf-8

import os
from handlers import Passport,VerifyCode,Profile
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler

handler = [
    (r"/api/login", Passport.LoginHandler),
    (r"/api/logout", Passport.LogoutHandler),
    (r"/api/register", Passport.RegisterHandler),
    (r"/api/piccode", VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.PhoneCodeHandler),
    (r"/api/check_login", Passport.CheckLoginHandler),
    (r"/api/profile", Profile.ProfileHandler),
    (r"/api/profile/avatar", Profile.AvatarHandler),
    (r"/api/profile/name", Profile.RenameHandler),
    (r"/(.*)", StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]
