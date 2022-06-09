import datetime,time
import git
def loop_task():
  while True:
    print('执行循环')
    repo = git.cmd.Git('~/Documents/code/timertask')
    repo.add('.')
    repo.commit('-m update')
    repo.push()
    time.sleep(2)
if __name__ == '__main__':
  loop_task()