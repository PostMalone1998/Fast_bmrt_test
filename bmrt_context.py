import os
from utils import find_directories_with_file

def batch_bmrt_context(context_root_path):
    if not os.path.exists(context_root_path):
        print("path: {} not exist".format(context_root_path))
        return

    failure_commands = []
    success_commands = []
    model_list = find_directories_with_file(context_root_path, "compilation.bmodel")
    model_list.sort()

    commands = ["bmrt_test --context", "", "--loopnum 5"]

    for model_path in model_list:
        commands[1] = model_path
        exc_cmd = " ".join(commands)

        ret = os.system(exc_cmd)
        ret >>= 8
        if ret != 0: failure_commands.append(exc_cmd)
        else: success_commands.append(exc_cmd)

    if failure_commands:
        with open("./failure_bmrt_context_cases.txt", 'w') as o_file:
            for i in range(len(failure_commands)):
                o_file.writelines(failure_commands[i] + "\n")
        o_file.close()
        print("some case fail :(  more detail see failure_bmrt_context_cases.txt")
    else:
        print("all case success")

    if success_commands:
        with open("./success_bmrt_context_cases.txt", 'w') as o_file:
            for i in range(len(success_commands)):
                o_file.writelines(success_commands[i] + "\n")
        o_file.close()
        print("success case has write into success_bmrt_context_cases.txt")
