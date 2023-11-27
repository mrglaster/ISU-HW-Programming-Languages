from enum import Enum
import json


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class AlignmentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Alignment):
            return obj.value
        return super().default(obj)


class Widget:
    ATTRIBUTE_MAP = {
        'MainWindow': {'title': 'title'},
        'Layout': {'alignment': 'alignment'},
        'LineEdit': {'max_length': 'max_length'},
        'ComboBox': {'items': 'items'},
    }

    TYPE_MAP = {'MainWindow': 0, 'Layout': 1, 'LineEdit': 2, 'ComboBox': 3}

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_children(self)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def add_children(self, children: "Widget"):
        self.children.append(children)

    def to_json(self):
        result = {}
        classname = self.__class__.__name__
        attr_map = self.ATTRIBUTE_MAP.get(classname, {})

        result[classname] = {attr_name: getattr(self, attr) for attr, attr_name in attr_map.items()}
        result['children'] = [child.to_json() for child in self.children]

        return result

    def to_binary(self, generation=0, count_brother=0):
        classname = self.__class__.__name__
        type_code = self.TYPE_MAP.get(classname, 0)
        result = {
            'type': type_code,
            'generation': generation + 1 + count_brother,
            'count_brother': count_brother,
        }

        if classname == 'MainWindow':
            result['title'] = self.title
        elif classname == 'Layout':
            result['alignment'] = 1 if self.alignment.name.endswith('HORIZONTAL') else 2
        elif classname == 'LineEdit':
            result['max_length'] = self.max_length
        elif classname == 'ComboBox':
            result['items'] = self.items

        result['children'] = [child.to_binary(generation, i) for i, child in enumerate(self.children)]
        return result

    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)


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

    def __str__(self):
        return f"{self.__class__.__name__}: {self.max_length}"


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items

    def __str__(self):
        return f"{self.__class__.__name__}: {self.items}"


def from_json(data, parent=None):
    class_name = next(iter(data))
    attr_map = Widget.ATTRIBUTE_MAP.get(class_name, {})
    attr_values = data[class_name]

    if class_name == 'MainWindow':
        widget = globals()[class_name](attr_values['title'])
    else:
        widget = globals()[class_name](parent, **{attr: attr_values[attr_name] for attr, attr_name in attr_map.items()})

    if 'children' in data:
        for child_data in data['children']:
            from_json(child_data, parent=widget)

    return widget





app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(f"app: {app}")
bts = app.to_json()
json_data = json.dumps(bts, cls=AlignmentEncoder)  # Use the custom encoder here
print(f"Serialized to JSON data: {json_data}")
parsed = json.loads(json_data)
print(f"Parsed from json: {from_json(parsed)}")
