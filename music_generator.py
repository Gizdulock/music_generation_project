import magenta
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
import numpy as np
import os

def generate_music():
    config = configs.CONFIG_MAP['cat-mel_2bar_big']
    model = TrainedModel(config, batch_size=4, checkpoint_dir_or_path='/path/to/pretrained/model.ckpt')

    num_sequences = 10
    temperature = 0.8

    sequences = model.sample(n=num_sequences, length=80, temperature=temperature)

    for i, sequence in enumerate(sequences):
        magenta.music.sequence_proto_to_midi_file(sequence, f'generated_sequence_{i}.mid')

def main():
    print("Music generation script")
    generate_music()

if __name__ == "__main__":
    main()
