from ast import IsNot
import datetime
import time
import git


class AutoSave:
    def __init__(self):
        self.loop_task()

    def loop_task(self):
        path = self.input_path()

        while True:
            print('start loop')
            try:
                result = self.save_code(path)
                if not result:
                    print('path is error')
            except BaseException as e:
                # print(e)
                pass
            time.sleep(10)

    def input_path(self):
        path = input("Please input program path:")
        if path is None:
            print('path is empty')
            return self.input_path()

        return path

    def save_code(self, path):

        try:
            repo = git.cmd.Git(path)

        except BaseException as e:
            print('path error')
            return False
        try:
            repo.add('.')
        except BaseException as e:
            print('nothing to add')
            pass
        try:
            repo.commit('-m update')
        except BaseException as e:
            print('nothing to commit')
            pass
        repo.push()
        print('push over')
        return True


if __name__ == '__main__':
    AutoSave()
