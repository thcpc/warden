```yaml
## 组件ID
## 必填项
id: "tsc"
## 组件名称
## 必填项
name: "表结构对比"
## 组件描述
## 必填项
description: "数据库结构比对工具，主要用来比对指定的两个 schema 的结构是否一致"
## 版本
## 必填项
version: 1_0_0
## 依赖的任务，顺序执行
## 可选项
pre_processors:
  - name: "processor1"
    plugin_id: btest1
    version: 1_0_0
  - name: "processor2"
    plugin_id: btest1
    version: 1_0_0
post_processors:
  - name: "processor1"
    plugin_id: btest1
    version: 1_0_0
  - name: "processor2"
    plugin_id: btest1
    version: 1_0_0
```