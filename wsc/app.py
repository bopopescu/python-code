import tornado.ioloop
import tornado.web
import tornado.websocket
import time
class ProStatus():
    connector = {}  # 记录当前连接的user

    def user_connect(self, user):
        if user not in self.connector:
            # 设置新来用户名
            self.connector[user] = "用户"+str(str(time.strftime("%Y%m%d%H%M%S", time.localtime())))



    def trigger(self, message):
        print(self.connector)
        ''' 向所有被记录的客户端推送最新内容 '''
        for user in self.connector:

            user.write_message(message)


class ReceiveHandler(tornado.web.RequestHandler):
    def get(self):
        msg = self.get_argument('msg', '')
        print(msg)
        ProStatus().trigger(msg) # 接收到消息之后推送


class ConnectHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin) :
        '''重写同源检查 解决跨域问题'''
        return True

    def open(self) :
        '''新的websocket连接后被调动'''
        ProStatus().user_connect(self)

        ProStatus().trigger('\n新用户加入聊天室,在线人数：'+str(len(ProStatus().connector)))

    def on_close(self) :
        '''websocket连接关闭后被调用'''
        # ProStatus().user_remove(self)
        del ProStatus().connector[self]
        ProStatus().trigger('\n已有用户退出聊天,在线人数：'+str(len(ProStatus().connector)))  # 向客服端发送

    def on_message(self, message) :
        '''接收到客户端消息时被调用'''
        ProStatus().trigger(ProStatus().connector[self]+message)  # 向客服端发送


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("ws.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/ws', ConnectHandler),
            (r'/receive', ReceiveHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == "__main__":
    app = Application()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()