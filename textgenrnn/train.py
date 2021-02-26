from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file(‘input.txt’, num_epochs=5)
