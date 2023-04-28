from config_common import *

dist_backend = "nccl"

train_batch_size = 256
eval_batch_size = train_batch_size
max_steps = 10000000
max_samples_termination = 4391260000

learning_rate = 0.001

beta_1: float = 0.9
beta_2: float = 0.99
eps: float = 1e-08

seed = 23333
