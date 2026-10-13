"""student_utils.py —— 实验4 生成的工具模块。

提供 parse_student()：把 "name,score" 形式的一行解析成字典。
非法记录抛出 ValueError。
"""


def parse_student(line):
    """解析 'name,score' 形式的一行，返回 {'name': str, 'score': int}。"""
    fields = line.split(",")

    if len(fields) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(fields)}")

    name = fields[0].strip()
    raw_score = fields[1].strip()

    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(raw_score)
    except ValueError:
        raise ValueError(f"成绩不是整数：{raw_score!r}") from None

    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围：{score}")

    return {"name": name, "score": score}
