#! python
# coding=utf-8
###########################################
# HtmlElementPattern.py
# CLASS
# СТРОИТЕЛЬ (PATTERNS)
###########################################
# Writing by sgiman, May 2025
#------------------------------------------
# HtmlElement
#------------------------------------------
class HtmlElement:
    # Properties
    indent_size = 2

    # Constructor
    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self,indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}')

        if self.text:
            i1 = '' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    # Override base
    def __str__(self):
        return self.__str(0)

    @staticmethod   # статический метод аналогичный С++
    def create(name):
        return HtmlBuilder(name)


#------------------------------------------
# HtmlBuilder
#------------------------------------------
class HtmlBuilder:
    # Конструктор верхнего уровня
    def __init__(self, root_name):
        self.root_name = root_name
        #self.__root = HtmlElement(name=root_name)
        self.__root = HtmlElement(root_name)

    # API
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    # Override
    def __str__(self):
        return str(self.__root)     # вернуть недоступный __root

#===================================================
# Testing html (patterns - HtmlBuilder)
#===================================================
# --- variant 1 ---
# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')

print('-' * 80)

# --- variant 2 (best) ---
builder = HtmlElement.create('ul')
builder.add_child_fluent('li','hello')\
    .add_child_fluent('li','world')

print('Ordinary builder:')
print(builder)

print('-' * 80)
