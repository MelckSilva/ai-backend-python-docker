import os
import emoji

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
         content = f.read()
    
    # Remove emojis
    content = emoji.replace_emoji(content, replace='')
    
    # Replace travessões with hífens
    content = content.replace('—', '-')
    content = content.replace('–', '-')
    
    # Clean up cases where emoji removal left leading spaces before punctuation or double spaces
    # Example: "Hello 🚀!" -> "Hello !" -> "Hello!"
    content = content.replace(' !', '!')
    content = content.replace(' ?', '?')
    content = content.replace(' .', '.')
    content = content.replace(' ,', ',')
    
    # Clean up cases where removing emoji leaves empty bullet points or double spaces
    content = content.replace('  ', ' ')
    
    with open(filepath, 'w', encoding='utf-8') as f:
         f.write(content)

dirs_to_check = ['Materiais', 'Exercícios']
for d in dirs_to_check:
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file))
