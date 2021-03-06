import time
from cv2 import log
import git
from colorama import Fore, Back, Style


class AutoSave:
    def __init__(self):
        self.path = ''
        try:
            self.loop_task()
        except BaseException as e:
            print(Style.RESET_ALL)
            pass

    def loop_task(self):
        path = self.input_path()
        self.path = path
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
            Fore.YELLOW + "How many minutes would you like to be pushed（default is 20 ）: ")
        return self.checkTime(time)
    
    def checkTime(self, inputTime):
        if not inputTime:
            print(Fore.YELLOW + 'time is 20 minutes')
            return 20
        if not inputTime.isdigit():
            print(Fore.RED + 'time is not number')
            return self.input_loopTime()
        print(Fore.GREEN + 'push frequency is once every ' + str(inputTime) + ' minutes')
        return int(inputTime)
    def input_path(self):
        path = input(Fore.YELLOW + "Which project do you want to sync automatically: ")
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
            print(Fore.GREEN + 'commit over')
        except BaseException as e:
            print(Fore.YELLOW + 'nothing to commit')
            pass
        repo.push()
        print(Fore.GREEN + '🎉🎉🎉 [' + self.path + '] push over 🎉🎉🎉')
        return True

if __name__ == '__main__':
    AutoSave()
