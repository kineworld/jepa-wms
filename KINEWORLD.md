# KineWorld / 勘境 changes

Upstream: https://github.com/facebookresearch/jepa-wms

Inspected base: `13cf1d9c7e476f53c17714d2e0f1dc239a883ce0`. License: **CC-BY-NC-4.0; third-party components have separate terms**. Original license and notices remain unchanged; code, checkpoints and datasets can have separate terms.

## 致谢 / Acknowledgements

感谢 **JEPA-WMs authors / Meta FAIR** 以及所有贡献者的开源精神。你们公开研究成果、代码与复现方法，让更多研究者和小团队能够学习、验证和继续改进。勘境珍惜这些贡献，保留原始作者、提交历史、许可证与引用信息；我们的新增工作以可检查的改动和测试记录说明。

We thank JEPA-WMs authors / Meta FAIR and the broader open-source community for sharing their work. Original contributions remain attributed to their authors. KineWorld's changes are documented separately, with their validation limits.

## Implemented change

Thread checkpoint_path through the public hub entry points and validate it before constructing the model. Previously arbitrary kwargs were silently ignored. Unknown options now raise TypeError. This selects the predictor checkpoint only; encoder/config code can still require their own assets. It is not a full offline mode.

## Validation

2 focused tests passed locally. Run `python -m unittest discover -s tests_kineworld -v` (Python 3.10+; NumPy is required for OpenDW statistics).

These are engineering/numerical checks, not a model-quality benchmark. No full checkpoint reproduction, new weights, measured leaderboard improvement or upstream endorsement is claimed. Original model descriptions and scores in the upstream README remain the authors' results.

## Project map

[KineWorld source/validation directory](https://github.com/kineworld/.github/blob/main/world-models/open-source-adoption.md) · [KineJing integration research](https://github.com/kineworld/KineJing).

This fork is a noncommercial research track under CC-BY-NC-4.0. It is not approved as a commercial product dependency.
