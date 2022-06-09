import datetime
import time
import git


class AutoSave:
    def __init__(self):
        self.loop_task()

    def loop_task(self):
        while True:
            print('执行循环-000')
            try:
                self.save_code()
            except BaseException as e:
                print(e)
                pass
            time.sleep(10)

    def save_code(self):
        repo = git.cmd.Git('~/Documents/code/timertask')
        repo.add('.')
        print('执行 add')
        repo.commit('-m update')
        print('执行 commit')
        repo.push()
        print('执行 push')


if __name__ == '__main__':
    AutoSave()
