from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='wiki_celeb_gen_weights.hdf5',
                       vocab_path='wiki_celeb_gen_vocab.json',
                       config_path='wiki_celeb_gen_config.json')
 
textgen.generate_samples(max_gen_length=1000)
textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)
