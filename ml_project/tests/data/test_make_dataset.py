from src.data.make_dataset import load_data, split_train_val_data
from src.params import SplittingParams


def test_load_dataset(dataset_path: str, target_name: str):
    data = load_data(dataset_path)
    assert len(data) > 10
    assert target_name in data.keys()


def test_split_dataset(dataset_path: str):
    test_size = 0.2
    splitting_params = SplittingParams(random_state=666, test_size=test_size)
    data = load_data(dataset_path)
    train_data, val_data = split_train_val_data(data, splitting_params)
    assert train_data.shape[0] > 10
    assert val_data.shape[0] > 5
