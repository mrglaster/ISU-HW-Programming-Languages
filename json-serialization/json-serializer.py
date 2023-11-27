import json
from enum import Enum
import struct


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_child(self)

    def to_binary(self, generation=0, count_brother=0):
        d = {'MainWindow': 0, 'Layout': 1, 'LineEdit': 2, 'ComboBox': 3}
        result = {
            'type': d[self.__class__.__name__],
            'generation': generation,
            'count_brother': count_brother,
        }

        if isinstance(self, MainWindow):
            result['title'] = self.title
        elif isinstance(self, Layout):
            result['alignment'] = 1 if self.alignment.name.endswith('HORIZONTAL') else 2
            result['generation'] = generation + 1 + count_brother
        elif isinstance(self, LineEdit):
            result['max_length'] = self.max_length
            result['generation'] = generation + 1 + count_brother
        elif isinstance(self, ComboBox):
            result['items'] = self.items
            result['generation'] = generation + 1 + count_brother

        result['children'] = [child.to_binary(generation, i) for i, child in enumerate(self.children)]
        return result

    @classmethod
    def from_binary(cls, data, number=0, history=None, buf_generation=None):
        if buf_generation is None:
            buf_generation = [0]
        if history is None:
            history = []
        if isinstance(data, str):
            data_dict = json.loads(data)
        else:
            data_dict = data
        class_name = data_dict['type']
        h_buf = -1
        if class_name == 0:  # MainWindow
            title = data_dict.get('title', '')
            select = MainWindow(title)
            history.append(select)
        elif class_name == 1:  # Layout
            h_buf = data_dict.get('generation', 0)
            alignment = data_dict.get('alignment', 1)
            select = Layout(history[h_buf], Alignment(alignment))
            position = 1 + buf_generation[h_buf]
            for i in range(h_buf):
                position += buf_generation[i]
            history.insert(position, select)
        elif class_name == 2:  # LineEdit
            h_buf = data_dict.get('generation', 0)
            max_length = data_dict.get('max_length', "")
            select = LineEdit(history[h_buf], int(max_length))
            if len(buf_generation) < h_buf + 1:
                buf_generation.append(0)
            position = 1 + buf_generation[h_buf]
            for i in range(h_buf):
                position += buf_generation[i]
            history.insert(position, select)
        elif class_name == 3:  # ComboBox
            h_buf = data_dict.get('generation', 0)
            items = data_dict.get('items', [])
            select = ComboBox(history[h_buf], items)
            if len(buf_generation) < h_buf + 1:
                buf_generation.append(0)
            position = 1 + buf_generation[h_buf]
            for i in range(h_buf):
                position += buf_generation[i]
            history.insert(position, select)

        if 'children' in data_dict:
            for i, child_data in enumerate(data_dict['children']):
                cls.from_binary(json.dumps(child_data), 0, history, buf_generation)
        return history[0]

    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)

    def add_child(self, child: "Widget"):
        self.children.append(child)


class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

bts = app.to_binary()
print(f"Binary data length {len(bts)}")
print(bts)

new_app = MainWindow.from_binary(bts)
print(new_app)
print(new_app.children[1].children[1].items)
