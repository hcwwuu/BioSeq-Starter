# BioSeq-Starter

**[English](README.md) | 中文**

> 一个围绕 **Learning by Building，在项目中学** 构建的生物信息学 Python 入门项目。

BioSeq-Starter 并不是为了做一个功能强大或可以用于实际科研生产环境的生物信息学工具。

这个项目的最终代码刻意保持简单。

这个仓库更重要的价值在于它的**逐步迭代过程**：从一个空的 Python 项目开始，一步一步加入生物数据读取、基础序列算法、Biopython、数据可视化、异常处理、模块化设计，最后再使用 Git 和 GitHub 把它整理成一个完整项目。

与分别学习 Python 语法、生信库、数据格式和工程化知识不同，这个项目希望把这些内容放进同一个具体任务中，让初学者在不断解决问题的过程中学习。

---

## 你可以学到什么？

按照这个项目一步一步完成后，可以接触：

### Python 基础

* 变量与数据类型
* 字符串
* 列表、集合与字典
* `if` 条件判断
* `for` 循环
* 函数
* 形参与实参
* 返回值
* 模块
* 异常处理
* `main()` 主程序结构

### 生物信息学基础

* FASTA 格式
* DNA 序列的计算机表示
* 序列合法性检查
* 碱基组成统计
* GC 含量
* 反向互补序列
* DNA 转录
* 蛋白质翻译

### Python 生信与绘图库

* Biopython
* Matplotlib

### 基础工程化思想

* Python 虚拟环境
* 依赖管理
* 模块化代码
* 输入检查
* 异常处理
* Git 版本控制
* GitHub 仓库
* README 文档

---

# 学习路线

这个仓库最推荐的使用方式并不是：

> 下载最终代码 → 直接运行。

而是：

> **建立一个空目录，从 Stage 0 开始，一步一步把最终项目重新构建出来。**

---

## Stage 0：搭建开发环境

在真正开始写生信代码之前，先建立一个独立的 Python 开发环境。

推荐：

* Windows
* VS Code
* Python 3.13
* Python `venv` 虚拟环境

首先建立：

```text
BioSeq-Starter/
```

创建虚拟环境：

```bash
py -3.13 -m venv .venv
```
如果系统默认的 python 已经指向 Python 3.13，也可以使用 ```python -m venv .venv```。

Windows PowerShell 中激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装需要的库：

```bash
python -m pip install biopython matplotlib
```

这一阶段需要理解：

```text
系统 Python
    ↓
项目自己的虚拟环境
    ↓
项目自己的依赖
```

### 这一阶段可以学到

* 什么是 Python 解释器
* `pip` 的作用
* 为什么项目需要虚拟环境
* VS Code 如何选择 Python Interpreter

---

## Stage 1：读取第一份 FASTA 文件

创建：

```text
data/
└── example.fasta
```

例如：

```text
>example_sequence
ATGGCCATTGTAATGGGCCGCTGA
```

导入：

```python
from Bio import SeqIO
```

使用：

```python
record = SeqIO.read("data/example.fasta", "fasta")
```

读取：

```python
record.id
record.description
record.seq
```

程序第一次形成数据流：

```text
FASTA 文件
    ↓
SeqIO
    ↓
SeqRecord
    ↓
DNA 序列
```

### 这一阶段可以学到

* FASTA 是什么
* 生物序列如何保存在文本文件中
* Python 如何读取外部数据
* `SeqIO`
* `SeqRecord`
* `Bio.Seq.Seq`

---

## Stage 2：自己实现最基础的序列算法

这一阶段暂时不急着调用 Biopython 已经提供的所有功能。

使用基础 Python 自己实现：

```python
validate_sequence()
count_bases()
gc_content()
reverse_complement()
```

### DNA 合法性检查

检查序列中是否只包含：

```text
A T C G
```

这里可以学习：

* 集合 `set`
* `for`
* `if`
* 布尔值 `True / False`

### 碱基数量统计

建立字典：

```text
A → 0
T → 0
C → 0
G → 0
```

遍历 DNA 序列并逐个累加。

这里可以学习：

* 字典
* 索引
* 循环
* 计数器

### GC 含量

利用已经写好的：

```python
count_bases()
```

得到 G 和 C 的数量，再计算 GC 比例。

这里会第一次接触一个很重要的编程思想：

> 已经实现的逻辑应该复用，而不是重新写一遍。

### 反向互补序列

建立：

```text
A ↔ T
C ↔ G
```

的映射关系，再使用：

```python
reversed()
```

反向遍历 DNA。

这里可以学习：

* 字典映射
* 迭代
* 字符串拼接

### 为什么不直接全部调用 Biopython？

因为这些功能本身比较简单。

对于初学者来说，自己实现一次，可以真正理解循环、字典、字符串和函数是怎样组合成一个小算法的。

等理解以后，再使用成熟库会更清楚库到底帮我们完成了什么。

---

## Stage 3：开始合理使用 Biopython

并不是所有功能都应该自己重新实现。

对于成熟、标准的生物学操作，直接使用可靠的库更加合理。

把普通字符串转换为：

```python
from Bio.Seq import Seq

dna = Seq(sequence)
```

然后：

```python
rna = dna.transcribe()
```

进行转录。

再：

```python
protein = rna.translate()
```

进行翻译。

数据流变成：

```text
DNA
 ↓
transcribe()
 ↓
RNA
 ↓
translate()
 ↓
Protein
```

### 这一阶段可以学到

* `str` 与 `Bio.Seq.Seq` 的区别
* 普通函数与对象方法的区别
* DNA 转录
* 密码子
* 蛋白质翻译
* 终止密码子

这一阶段还需要理解一个很重要的工程判断：

> 简单算法可以为了学习自己实现，但成熟且标准的复杂功能应该优先使用可靠的库。

---

## Stage 4：对结果进行可视化

导入：

```python
import matplotlib.pyplot as plt
```

将：

```text
A → 数量
T → 数量
C → 数量
G → 数量
```

转化成柱状图。

程序最终生成：

```text
results/nucleotide_distribution.png
```

### 示例结果

![碱基组成统计图](results/nucleotide_distribution.png)

### 这一阶段可以学到

* 字典的 `keys()`
* 字典的 `values()`
* `list`
* Matplotlib
* 柱状图
* 程序生成并保存文件

到这里，项目已经形成：

```text
输入
 ↓
分析
 ↓
生物学转换
 ↓
可视化
```

这一条完整的数据处理流程。

---

## Stage 5：从一个脚本整理成一个小项目

最早的代码可以全部写在：

```text
main.py
```

中。

但代码逐渐增加后，需要开始拆分职责。

将基础序列处理函数移动到：

```text
analyzer.py
```

例如：

```text
analyzer.py
├── validate_sequence()
├── count_bases()
├── gc_content()
└── reverse_complement()
```

然后在：

```text
main.py
```

中导入这些函数。

此时 `main.py` 不再负责实现每一个算法，而主要负责：

```text
读取数据
 ↓
检查输入
 ↓
调用分析函数
 ↓
DNA → RNA → Protein
 ↓
生成可视化
```

进一步加入：

```python
def main():
    ...
```

以及：

```python
if __name__ == "__main__":
    main()
```

同时开始处理：

* FASTA 文件不存在
* FASTA 内容为空
* DNA 中存在非法字符
* FASTA 文件内容不符合预期

### 这一阶段可以学到

* Module
* `import`
* 模块职责划分
* 局部变量
* 函数参数
* `main()`
* `if __name__ == "__main__"`
* `try`
* `except`
* `raise`
* `ValueError`
* `FileNotFoundError`

这是项目开始从：

```text
Python 练习代码
```

变成：

```text
一个小型 Python 工程
```

的阶段。

---

## Stage 6：使用 Git 和 GitHub 管理项目

代码跑通以后，再开始整理项目。

增加：

```text
.gitignore
requirements.txt
README.md
README.zh-CN.md
```

`.gitignore` 用来忽略：

```text
.venv/
__pycache__/
.vscode/
```

等只属于本地开发环境的内容。

`requirements.txt` 保存直接依赖：

```text
biopython
matplotlib
```

初始化 Git：

```bash
git init
```

查看文件状态：

```bash
git status
```

将修改加入暂存区：

```bash
git add .
```

创建一个版本：

```bash
git commit -m "Initial BioSeq Starter"
```

最后建立 GitHub 仓库并 push。

### 这一阶段可以学到

* Working Directory
* Staging Area
* Commit
* Branch
* `main`
* Remote Repository
* `origin`
* `push`
* `.gitignore`
* 依赖管理
* 项目文档

做到这里，项目就不再只是保存在某一台电脑上的代码，而变成一个可以被其他人获取、运行和继续开发的项目。

---

# 最终项目结构

全部阶段完成后：

```text
BioSeq-Starter/
│
├── main.py
├── analyzer.py
├── README.md
├── README.zh-CN.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── example.fasta
│
└── results/
    └── nucleotide_distribution.png
```

最终的数据流：

```text
example.fasta
      ↓
Biopython SeqIO
      ↓
DNA sequence
      ↓
序列合法性检查
      ↓
自己实现的基础算法
      ├── 碱基统计
      ├── GC 含量
      └── 反向互补
      ↓
Biopython Seq
      ↓
DNA → RNA → Protein
      ↓
Matplotlib
      ↓
nucleotide_distribution.png
```

---

# 最终版本能做什么？

当前基础版本支持：

* 读取 `data/example.fasta` 中的一条 DNA 序列
* DNA 序列合法性检查
* 序列长度计算
* A/T/C/G 碱基数量统计
* GC 含量计算
* DNA 反向互补
* DNA → RNA
* RNA → Protein
* 碱基组成可视化
* 基础文件与输入异常处理

这些功能本身并不复杂。

这是有意为之。

这个仓库的目标不是提供一个完整的生物信息学分析工具，而是让初学者能够完整理解这个小工具是怎样一步一步构建出来的。

---

# 快速运行最终版本

克隆：

```bash
git clone https://github.com/hcwwuu/BioSeq-Starter.git
```

进入目录：

```bash
cd BioSeq-Starter
```

创建虚拟环境：

```bash
py -3.13 -m venv .venv
```

Windows PowerShell 激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
python -m pip install -r requirements.txt
```

将需要分析的 DNA 保存或替换到：

```text
data/example.fasta
```

然后：

```bash
python main.py
```

---

# 下一步可以学什么？

完成基础版本以后，可以按照难度继续扩展。

### 多 FASTA 序列处理

从：

```python
SeqIO.read()
```

进一步学习：

```python
SeqIO.parse()
```

处理多条序列。

### ORF Finder

寻找：

```text
ATG
 ↓
编码区域
 ↓
TAA / TAG / TGA
```

从而进一步理解开放阅读框和阅读框算法。

### Motif 搜索

在 DNA 序列中搜索指定的序列模式。

### NCBI 数据获取

从公开生物数据库中获取真实基因或转录本序列。

### BLAST

进一步学习序列相似性搜索。

### 命令行参数

将固定读取：

```text
data/example.fasta
```

改造成：

```bash
python main.py data/example.fasta
```

让程序真正接收用户指定的输入文件。

---

# 为什么是 BioSeq-Starter？

最终程序本身可能只有很少的代码。

但从零把它构建出来，需要经历：

```text
Python 环境
    ↓
Python 基础语法
    ↓
FASTA 数据
    ↓
基础算法
    ↓
Biopython
    ↓
数据可视化
    ↓
异常处理
    ↓
模块化
    ↓
Git
    ↓
GitHub
```

**这条迭代路线才是 BioSeq-Starter 最重要的内容。**

这个项目的目标并不是“得到最终代码”，而是：

> **理解最终代码是怎样一步一步被构建出来的。**
