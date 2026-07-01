from pathlib import Path
import json

print('-------------------Reading/Writing + Context Managers-------------------')
"""
"r"  → read
"w"  → write (overwrite)
"a"  → append
"x"  → create only
"rb" → binary read
"""
class TaskLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.create_file()

    
    def create_file(self):
        file_path = Path(self.file_name)
        if file_path.is_file():
            print(f'The file {self.file_name} already exists')
            return

        with open(self.file_name, 'x') as file:
            # json.dump({"tasks": []}, file)
            if '.json' in self.file_name:
                json.dump({"tasks":[]},file)
            else:
                pass

            

        print(f'The file {self.file_name} was create successfully!')

    def add_task(self, task):
        with open(self.file_name, 'a') as file:
            file.write(f'\n {task}')

    def list_tasks(self):
        content = ''
        with open(self.file_name, 'r') as file:
            content = file.read()
        
        return content

    # json tasks format
    """{
        "tasks": [
            "task 1",
            "task 2"
        ]
    }"""

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            return data
        
        except json.JSONDecodeError:
            return {"tasks":[]}
        except FileNotFoundError:
            return {"tasks":[]}



    def add_json_task(self, task):
        # with open(self.file_name, 'r') as file:
        #     # content = file.read()
        #     # data = json.loads(content) if content.strip() else {"tasks":[]}
        #     data = json.load(file)
        data = self.load_tasks()

        data['tasks'].append(task)

        with open(self.file_name, 'w') as file:
            json.dump(data, file)


    def list_json_tasks(self):
        # data = {}
        # with open(self.file_name, 'r') as file:
        #     data = json.load(file)
        data = self.load_tasks()
        return data



# logger = TaskLogger('tasks.txt')

# logger.add_task('This is an example task')
# logger.add_task('This is another example task')
# print(logger.list_tasks())

print('-------------------------------')
# Create json logger tasks file

logger = TaskLogger('tasks.json')

logger.add_json_task('This is an example json task')
logger.add_json_task('This is a 2nd example json task')
print(logger.list_json_tasks())



        

    
