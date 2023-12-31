import pyfiglet
import argparse
import os
from time import monotonic, sleep
import shutil
from pomodoro.utils import notify


parser = argparse.ArgumentParser(
    description="This is a CLI tool for pomodoro"
)


parser.add_argument('--desc',
                    default=None,
                    type=str,
                    help='add description to the task')
parser.add_argument('-t', '--time',
                    help='time in minutes',
                    type=int)
parser.add_argument('-c', '--category',
                    default=None,
                    type=str,
                    help='specify the category of')
parser.add_argument('-f', '--font',
                    default='colossal',
                    type=str)
parser.add_argument('--no-sound',
                    action='store_true',
                    )

args = parser.parse_args()

category = args.category
desc = args.desc
duration = args.time * 60
font = args.font
no_sound = args.no_sound


f = pyfiglet.Figlet(font=font)


def DrawText(text, center=True):
    if center:
        print(*[x.center(shutil.get_terminal_size().columns)
              for x in f.renderText(text).split("\n")], sep="\n")
    else:
        print(f.renderText(text))


def print_on_screen(_TIME: int) -> None:
    m, s = divmod(_TIME, 60)
    h, m = divmod(m, 60)
    h, m, s = str(h), str(m), str(s)
    text = f'{h.zfill(2)} : {m.zfill(2)} : {s.zfill(2)}'
    os.system('clear')
    DrawText(text, center=True)


def Success() -> None:
    os.system('clear')
    text = 'GG'
    DrawText(text)


for t in range(duration, -1, -1):
    start = monotonic()
    print_on_screen(t)
    sleep(1 - monotonic() + start)
Success()

notify.notify(title='Timer Ended',
              message='Logs Saved',
              app_name='Pomodoro')
if not no_sound:
    notify.sound()
