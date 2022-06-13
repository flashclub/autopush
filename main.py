import time
import git
from colorama import Fore, Back, Style


class AutoSave:
    def __init__(self):
        self.loop_task()

    def loop_task(self):
        path = self.input_path()
        loopTime = self.input_loopTime()
        try:
            while True:
                print(Fore.GREEN + 'start loop')
                try:
                    result = self.save_code(path)
                    if not result:
                        print(Fore.RED + 'path is error')
                except BaseException as e:
                    pass
                time.sleep(loopTime * 60)
        except BaseException as e:
            print('error info')
            print(e)
            print(Fore.RED + '\n===============================================\n===================Task Stop===================\n===============================================\n')
            print(Style.RESET_ALL)
            return

    def input_loopTime(self):
        time = input(
            Fore.YELLOW + "Please enter the time of each push（in minutes）: ")
        if not time:
            print(Fore.YELLOW + 'time is 20 minute')
            return 20
        if not time.isdigit():
            print(Fore.RED + 'time is not number')
            return self.input_loopTime()
        print(Fore.GREEN + 'push frequency is once every ' + str(time) + 'minutes')
        return time.isdigit()

    def input_path(self):
        path = input(Fore.YELLOW + "Please input program path: ")
        if not path:
            print(Fore.YELLOW + 'path is empty')
            return self.input_path()
        return path

    def save_code(self, path):
        try:
            repo = git.cmd.Git(path)
        except BaseException as e:
            print(Fore.RED + 'path error')
            return False
        try:
            repo.add('.')
        except BaseException as e:
            print(Fore.YELLOW + 'nothing to add')
            pass
        try:
            repo.commit('-m update')
        except BaseException as e:
            print(Fore.YELLOW + 'nothing to commit')
            pass
        repo.push()
        print(Fore.GREEN + 'push over')
        return True

if __name__ == '__main__':
    AutoSave()
