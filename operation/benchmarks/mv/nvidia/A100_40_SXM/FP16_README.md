# 参评AI芯片信息

* 厂商：Nvidia

* 产品名称：A100
* 产品型号：A100-40GiB-SXM
* TDP：400W

# 所用服务器配置

* 服务器数量：1
* 单服务器内使用卡数: 1
* 服务器型号：DGX A100
* 操作系统版本：Ubuntu 20.04.4 LTS
* 操作系统内核：linux5.4.0-113
* CPU：AMD EPYC7742-64core
* docker版本：20.10.16
* 内存：1TiB
* 服务器间AI芯片直连规格及带宽：此评测项不涉及服务期间AI芯片直连

# 算子库版本

https://github.com/FlagOpen/FlagGems. Commit ID: 3c10679326b32ea5f037db50cc397d41c0ff1934

# 评测结果

## 核心评测结果

| 评测项  | correctness | TFLOPS(cpu wall clock) | TFLOPS(kernel clock) | FU(FLOPS Utilization)-cputime | FU-kerneltime |
| ---- | -------------- | -------------- | ------------ | ------ | ----- |
| flaggems | True    | 0.04TFLOPS       | 0.19TFLOPS        | 0.01% | 0.06% |
| nativetorch | True    | 0.14TFLOPS      | 0.17TFLOPS      | 0.04%      | 0.05%    |

## 其他评测结果

| 评测项  | cputime | kerneltime | cputime吞吐 | kerneltime吞吐 | 无预热时延 | 预热后时延 |
| ---- | -------------- | -------------- | ------------ | ------------ | -------------- | -------------- |
| flaggems | 52.9us       | 11.26us        | 18901.85op/s | 88778.41op/s | 16327512.33us | 73.89us |
| nativetorch | 15.44us       | 12.29us        | 64751.84op/s | 81380.21op/s | 148089.35us | 37.16us |

## 能耗监控结果

| 监控项  | 系统平均功耗  | 系统最大功耗  | 系统功耗标准差 | 单机TDP | 单卡平均功耗 | 单卡最大功耗 | 单卡功耗标准差 | 单卡TDP |
| ---- | ------- | ------- | ------- | ----- | ------------ | ------------ | ------------- | ----- |
| nativetorch监控结果 | 1482.0W | 1560.0W | 63.69W   | /     | 165.24W       | 178.0W      | 13.78W        | 400W  |
| flaggems监控结果 | 1482.0W | 1560.0W | 63.69W   | /     | 164.88W       | 177.0W      | 15.11W        | 400W  |

## 其他重要监控结果

| 监控项  | 系统平均CPU占用 | 系统平均内存占用 | 单卡平均温度 | 单卡最大显存占用 |
| ---- | --------- | -------- | ------------ | -------------- |
| nativetorch监控结果 | 1.982%    | 1.613%   | 37.37°C       | 2.519%        |
| flaggems监控结果 | 1.325%    | 1.548%   | 37.92°C       | 87.752%        |