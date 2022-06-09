import datetime,time
import git
def loop_task():
  repo = git.cmd.Git('~/Documents/code/douyin2')
  while True:
    print('执行循环')
    time.sleep(2)
if __name__ == '__main__':
  loop_task()