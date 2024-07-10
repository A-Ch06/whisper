import os.path

import numpy as np
import pytest
import torch

from whisper.audio import SAMPLE_RATE, load_audio, log_mel_spectrogram, pad_or_trim, N_SAMPLES


def test_audio():
    audio_path = os.path.join(os.path.dirname(__file__), "jfk.flac")
    audio = load_audio(audio_path)
    assert audio.ndim == 1
    assert SAMPLE_RATE * 10 < audio.shape[0] < SAMPLE_RATE * 12
    assert 0 < audio.std() < 1

    mel_from_audio = log_mel_spectrogram(audio)
    mel_from_file = log_mel_spectrogram(audio_path)

    assert np.allclose(mel_from_audio, mel_from_file)
    assert mel_from_audio.max() - mel_from_audio.min() <= 2.0

    padding = 10
    device = 'cpu' 

    mel_spec = log_mel_spectrogram(audio, padding=padding, device=device)

    assert mel_spec.device == torch.device(device)

    with pytest.raises(RuntimeError):
        load_audio("non_existent_file.flac")

def test_pad_or_trim():
    #Tensor longer than N_SAMPLES
    long_audio = torch.ones((N_SAMPLES + 100,))
    trimmed_audio = pad_or_trim(long_audio)
    assert trimmed_audio.shape[0] == N_SAMPLES

    #Tensor shorter than N_SAMPLES
    short_audio = torch.ones((N_SAMPLES - 100,))
    padded_audio = pad_or_trim(short_audio)
    assert padded_audio.shape[0] == N_SAMPLES

    #NumPy array longer than N_SAMPLES
    long_audio_np = np.ones((N_SAMPLES + 100,))
    trimmed_audio_np = pad_or_trim(long_audio_np)
    assert trimmed_audio_np.shape[0] == N_SAMPLES

    #NumPy array shorter than N_SAMPLES
    short_audio_np = np.ones((N_SAMPLES - 100,))
    padded_audio_np = pad_or_trim(short_audio_np)
    assert padded_audio_np.shape[0] == N_SAMPLES
