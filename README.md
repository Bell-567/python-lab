# Python 课程作业

**学号**：20244081112　**姓名**：杨俊堃

本仓库收录本课程的作业 Notebook 与实验报告。

## 内容

| 文件 | 说明 |
|---|---|
| `20244081112_杨俊堃_hw01.ipynb` | 作业1：Data Types, Functions and Conditionals |
| `20244081112_杨俊堃_exp01.ipynb` | 实验报告01：Python基础与数据处理入门 |
| `student_utils.py` | 实验4 第7题要求的工具模块，由 Notebook 自动生成 |
| `exp01_data/` | 实验4 的文件读写产物，由 Notebook 自动生成 |

## 作业1 要点

- **热身函数**：`say_hi` / `goat_pad` / `print_n`
- **欧几里得算法**：`gcd`，并分析参数为负数时的符号行为，给出 `gcd_safe` 修正版
- **自然常数 e 的近似**：`euler_limit`（伯努利极限式）、`euler_infinite_sum`（级数前 n 项）、`euler_approx`（精度 ϵ 控制）、`print_euler_sum_table`
- **整数性质**：`is_power_of_2`、`is_power(b, n)`，仅使用 `//` 与 `%`，不使用 `math.sqrt`

## 实验报告01 要点

覆盖五个实验：基本运算与字符串、函数与控制流、列表字典元组与统计、文件读写与异常处理、类与对象复制。

实验4 的数据文件中含三条故意设置的坏数据，程序会逐行捕获异常并跳过，最终统计结果：
**有效记录 6 条、无效记录 3 条，平均分 76.67，及格率 83.33%**。

## 运行环境

独立 conda 虚拟环境（Python 3.9），未使用 base 环境。

```bash
conda create -n exp01 python=3.9 ipykernel notebook jupyterlab numpy pandas
conda activate exp01
jupyter lab
```

打开的 Notebook 使用的内核为 `Python 3 (exp01)`。执行前请重启内核并运行全部代码，
`exp01_data/` 与 `student_utils.py` 会自动重新生成。

## 备注

课程讲义 PDF 未包含在本仓库中。
