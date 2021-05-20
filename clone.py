#!/usr/bin/env python3

import os
import argparse


def init_parser():
    parser = argparse.ArgumentParser(
        description="A tool for cloning multiple repos")

    parser.add_argument('-u', '--user', help="Specify the gitlab user")
    parser.add_argument(
        '-f', '--file', help="file path with the list", required=True)

    parser.add_argument(
        '-d', '--destiny', help="file with reposlist")

    return parser.parse_args()


if __name__ == '__main__':
    args = init_parser()

    username = args.user
    file_path = args.file
    destiny = args.destiny

    repos = None
    with open(file_path, 'r') as f:
        repos = f.read().split('\n')

    if destiny:
        os.chdir(destiny)

    print(f'Cloning repos in {os.getcwd()}', end="\n\n")

    for repo in repos:
        repo_with_user = repo
        repo_name = repo.split('/')[-1].split('.')[0]

        double_slash_index = repo.index('//') + 2
        if username:
            repo_with_user = f'{repo[:double_slash_index]}{username}@{repo[double_slash_index:]}'

        repo_dir = os.popen(f'ls | grep "{repo_name}"').read()
        if not repo_dir:
            os.system(f'git clone {repo_with_user}')

    print(os.listdir())

    # print(os.system("ls"))
    # print('Done!')
