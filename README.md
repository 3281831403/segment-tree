# 线段树：构建、区间和与更新

区间统计在大数组上频繁超时：建树没有递归填满，查询没有按区间剪枝，更新没有回溯父节点，最小值查询用了求和，树高按元素数而不是位数，空数组崩，批量更新只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
range/__init__.py
range/segment_tree.py
tests/test_segment_tree.py
```

## 当前状态

`range/segment_tree.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_segment_tree.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 递归建树
2. 区间查询剪枝
3. 更新回溯父节点
4. 最小值查询
5. 树高按位数
6. 空数组兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `range/segment_tree.py`
后 15 条用例应全部通过。
