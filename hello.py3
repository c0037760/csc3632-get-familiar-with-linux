#!/usr/bin/python3

import os

# cwd = os.getcwd()
# print(cwd)

basepath = '/home/student/known-cyber-attacks'
readme = 'README.md'
output_file = 'compile.md'

# TODO: check compile.md file exists, deletes it, then creates it again
# os.path.exists(compile.md)

with open(output_file, "a") as output:
    for filename in os.listdir(basepath):
        print(filename)

        # checks if a filename is a directory
        if os.path.isdir(os.path.join(basepath, filename) and not filename == ".git"):
            print(f'filename: {filename}')
            print(f'filepath: {os.path.join(basepath, filename)}')
            readme_path = os.path.join(basepath, filename, readme)

            # print(f'readme_path: {readme_path}')
            with open(readme_path, "r") as input:
                data = input.read()
                print(f'{readme_path}: {data}')
                output.write(data)

# create a single file - "compile.md"

# with open('compile.md', 'w') as f:
# contains all the attacks described in the repository
