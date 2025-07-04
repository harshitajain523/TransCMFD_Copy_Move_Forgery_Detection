"""Configuration management for TransCMFD"""

import yaml
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
from pathlib import Path

@dataclass
class ModelConfig:
    """Configuration for TransCMFD model architecture"""
    # Input specifications
    input_size: int = 256
    input_channels: int = 3

    # CNN Encoder
    encoder_backbone: str = "resnet50"
    encoder_pretrained: bool = True
    encoder_freeze: bool = False

    # Transformer
    patch_size: int = 16
    embed_dim: int = 768
    num_heads: int = 12
    num_layers: int = 12
    dropout: float = 0.1

    # Feature Similarity Module
    correlation_block_size: int = 16
    similarity_percentile: float = 0.95

    # Output
    num_classes: int = 1  # Binary segmentation

@dataclass
class TrainingConfig:
    """Training configuration"""
    # Training parameters
    batch_size: int = 16
    num_epochs: int = 100
    learning_rate: float = 1e-4
    weight_decay: float = 1e-5

    # Loss weights
    dice_weight: float = 0.5
    bce_weight: float = 0.4
    adaptive_weight: float = 0.1

    # Optimization
    optimizer: str = "adamw"
    scheduler: str = "cosine"
    warmup_epochs: int = 10

    # Hardware
    device: str = "cuda"
    num_workers: int = 4
    pin_memory: bool = True

    # Logging and saving
    save_freq: int = 10
    log_freq: int = 100
    val_freq: int = 1

@dataclass
class DataConfig:
    """Data configuration"""
    # Dataset paths
    train_data_path: str = "data/train"
    val_data_path: str = "data/val"
    test_data_path: str = "data/test"

    # Synthetic data generation
    synthetic_samples: int = 10000
    num_copies_range: tuple = (1, 3)
    copy_area_range: tuple = (0.05, 0.2)  # Fraction of image area

    # Data augmentation
    use_augmentation: bool = True
    rotation_range: int = 30
    brightness_range: float = 0.2
    contrast_range: float = 0.2

class ConfigManager:
    """Manages configuration loading and saving"""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path

    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def save_config(self, config: Dict[str, Any], save_path: str):
        """Save configuration to YAML file"""
        with open(save_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)

    def create_default_configs(self, save_dir: str = "experiments"):
        """Create default configuration files"""
        Path(save_dir).mkdir(exist_ok=True)

        # Default configurations
        configs = {
            "model": ModelConfig(),
            "training": TrainingConfig(),
            "data": DataConfig()
        }

        # Save each configuration
        for name, config in configs.items():
            config_dict = asdict(config)
            save_path = Path(save_dir) / f"{name}_config.yaml"
            self.save_config(config_dict, save_path)
            print(f"📄 Created: {save_path}")

# Test the configuration system
if __name__ == "__main__":
    config_manager = ConfigManager()
    config_manager.create_default_configs()
    print("Configuration system created")
