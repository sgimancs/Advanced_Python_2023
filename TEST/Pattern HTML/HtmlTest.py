#! python
# coding=utf-8
########################################################
# PATTERNS
# Паттерны проектирования на Python: Паттерн Строитель
# https://www.youtube.com/watch?v=x5yGIuf13Rk
########################################################
# Writing by sgiman, May 2025

print('-' * 80)

text = 'hello'
parts = ['<p>', text, '</p>']

words = ['hello', 'world']
parts = ['<ul>']

for w in words:
    parts.append(f' <li>{w}</li')

parts.append('</ul>')
print('\n'.join(parts))

print('-' * 80)
