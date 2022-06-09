import datetime,time
import git
def loop_task():
  while True:
    print('执行循环-2')
    repo = git.cmd.Git('~/Documents/code/timertask')
    repo.add('.')
    print('执行 add')
    repo.commit('-m update')
    print('执行 commit')
    repo.push()
    print('执行 push')
    time.sleep(2)
if __name__ == '__main__':
  loop_task()