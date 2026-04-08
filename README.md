# diversion-rules

用于分流规则与订阅转换配置管理，配合自建 [sub-web](https://github.com/CareyWang/sub-web) 和 [subconverter](https://github.com/tindy2013/subconverter) 使用。

## 目录说明

- `config/`：远程配置集合。
- `config/personal/`：个人自用配置。
- `rule/`：自定义规则文件，在配置中被引用。
- `subconverter/`：subconverter 运行配置（如 `pref.toml`）。

## 规则来源说明

部分规则直接引用了其他项目，例如 [ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)。

## 关于 subconverter 默认 64 条显示限制

当前自用配置较多，subconverter 默认可用数量不够时，可在配置文件 `advanced` 部分调整相关限制。

参考：
- [subconverter README-cn 配置文件说明（advanced）](https://github.com/tindy2013/subconverter/blob/master/README-cn.md#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)

本仓库已在 `subconverter/pref.toml` 的 `[advanced]` 中设置：
- `max_allowed_rulesets = 256`
