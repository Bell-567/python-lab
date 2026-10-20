# Python数据处理A — 课程作业

**学号**：20244081112　**姓名**：杨俊堃　**课程**：Python数据处理A

本仓库收录 Python数据处理A 课程的作业 Notebook 与实验报告。

## 内容

| 文件 | 说明 |
|---|---|
| `20244081112_杨俊堃_hw01.ipynb` | 作业1：Data Types, Functions and Conditionals |
| `20244081112_杨俊堃_hw02.ipynb` | 作业2：列表，字典和类 |
| `20244081112_杨俊堃_exp01.ipynb` | 实验报告01：Python数据处理A |
| `20244081112_杨俊堃_exp02.ipynb` | 实验报告02：NumPy、SciPy、Matplotlib 与 pandas 数据处理 |
| `student_utils.py` | 实验4 第7题要求的工具模块，由 Notebook 自动生成 |
| `exp01_data/` | 实验4 的文件读写产物，由 Notebook 自动生成 |

## 作业1 要点

- **热身函数**：`say_hi` / `goat_pad` / `print_n`
- **欧几里得算法**：`gcd`，并分析参数为负数时的符号行为，给出 `gcd_safe` 修正版
- **自然常数 e 的近似**：`euler_limit`（伯努利极限式）、`euler_infinite_sum`（级数前 n 项）、`euler_approx`（精度 ϵ 控制）、`print_euler_sum_table`
- **整数性质**：`is_power_of_2`、`is_power(b, n)`，仅使用 `//` 与 `%`，不使用 `math.sqrt`

## 作业2 要点

- **字符串**：`is_palindrome`（忽略空格与大小写）、`is_abecedarian`（忽略空格后单调不减）、`remove_vowels`（仅 a/e/i/o/u）
- **列表**：`list_reverse` 检查类型并返回新列表；`is_sorted` 用迭代器**只遍历一次**，复杂度 O(n)
- **元组向量**：`vec_scalar_mult`、`vec_inner_product`（返回 `float`）、`check_valid_mx`、`mx_vec_mult`。类型错误抛 `TypeError`，长度/维度不一致抛 `ValueError`
- **`Vector` 类**：`dim` 与 `elements` 为实例属性；比较运算符按元组字典序，维度不同抛异常；`dot()` 求内积；支持 `2*v`、`v*2` 与逐元素 `v*w`

## 实验报告01 要点

覆盖五个实验：基本运算与字符串、函数与控制流、列表字典元组与统计、文件读写与异常处理、类与对象复制。

实验4 的数据文件中含三条故意设置的坏数据，程序会逐行捕获异常并跳过，最终统计结果：
**有效记录 6 条、无效记录 3 条，平均分 76.67，及格率 83.33%**。

## 实验报告02 要点

| 实验 | 内容与结论 |
|---|---|
| 1 | ndarray 的 `dtype`/`shape`/`ndim`；`reshape` 要求元素总数不变；布尔索引 `\|` 与 `&` 必须加括号，否则会触发数组真值歧义 |
| 2 | 1000 个 $N(70, 10)$ 成绩并用 `np.clip` 限制到 [0, 100]；不放回抽样与按大小加权抽样；`permutation` 返回副本、`shuffle` 原地修改；缺失 3 个值后 `mean` 变 `nan`，须用 `nanmean` |
| 3 | 线性方程组解为 $(2, 3)$；$x^2-2=0$ 的正负根由初值决定；$f(x)=x+\frac{2}{x+2}$ 的极小点为 $-2+\sqrt{2}\approx-0.5858$；两组样本 t 检验 $p\approx5.7\times10^{-12}$，拒绝原假设 |
| 4 | 以 `Name` 为行索引并计算 `Total`/`Average`；`loc`/`iloc`；`mean(axis=0/1)`；`apply`/`agg`/`rank`；`groupby` + `transform('mean')`；`filter` 保留 A、B 两组；协方差与皮尔森相关系数；用 `io.StringIO` 做内存中的 CSV 往返 |

实验2 的图表用 Matplotlib 直接在 Notebook 内显示，**未保存任何文件**；所有随机过程固定种子 `2024`，结果可复现。

## 运行环境

独立 conda 虚拟环境（Python 3.9），未使用 base 环境。

```bash
conda create -n exp01 python=3.9 ipykernel notebook jupyterlab numpy pandas scipy matplotlib
conda activate exp01
jupyter lab
```

打开的 Notebook 使用的内核为 `Python 3 (exp01)`。执行前请重启内核并运行全部代码，
`exp01_data/` 与 `student_utils.py` 会自动重新生成。

## 备注

课程讲义 PDF 未包含在本仓库中。
