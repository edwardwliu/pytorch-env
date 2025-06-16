import torch

print(f"PyTorch version: {torch.__version__}")
print(f"MPS available: {torch.backends.mps.is_available()}")
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
print(f"Using device: {device}")

x = torch.ones(3, 3).to(device)
y = torch.rand(3, 3).to(device)
z = x + y
print(f"PyTorch environment ready!")
