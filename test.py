import hydra
from omegaconf import DictConfig, open_dict

@hydra.main(config_path='configs', config_name='main', version_base='1.2')
def main(config:DictConfig):
    dataset = hydra.utils.instantiate(config.datasets)
    print(dataset[0])
    pass

main()