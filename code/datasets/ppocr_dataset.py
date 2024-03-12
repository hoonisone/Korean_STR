from torch.utils.data import Dataset
from PIL import Image
from pathlib import Path
from typing import Callable, Optional, Union

class PPOCRDataset(Dataset):
    """_summary_
        PPOCR에서 사용하는 형식의 레이블 파일을 통해 데이터 셋을 로드하는 torch.Dataset
    Args:
        datasets (_type_): _description_
    """
    def __init__(self, data_dir:str, label_file_path:str, transform:Optional[Callable]=None, *args, **kwargs):
        self.data_dir = Path(data_dir)
        self.samples = PPOCRDataset.load_samples(label_file_path) # [(img_path, label), ...]
        self.num_samples = len(self.samples)
        self.transform = transform
        
    @staticmethod
    def load_samples(path):
        with open(path, "r") as f:
            lines = [line.rstrip("\n").split("\t") for line in f.readlines()]
        return lines
    
    @staticmethod
    def load_image(path):
        return Image.open(path).convert("RGB")
        
    def __len__(self):
        return self.num_samples

    def __getitem__(self, index):
        img_path, label = self.samples[index]
        img = PPOCRDataset.load_image(self.data_dir/img_path)
        
        if self.transform is not None:
            img = self.transform(img)
        return img, label