import datetime
import time
import git


class AutoSave:
    def __init__(self):
        self.loop_task()

    def loop_task(self):
        while True:
            print('start loop')
            try:
                self.save_code()
            except BaseException as e:
                print(e)
                pass
            time.sleep(10)

    def save_code(self):
        repo = git.cmd.Git('~/Documents/code/timertask')
        try:
            repo.add('.')
        except BaseException as e:
            print('nothing add')
            pass
        try:
            repo.commit('-m update')
        except BaseException as e:
            print('nothing commit')
            pass
        repo.push()
        print('push over')


if __name__ == '__main__':
    AutoSave()
