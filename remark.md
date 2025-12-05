
# 问题汇总

## 不支持直接输入docx, xlsx, pptx, 需要转成pdf

-  只支持图片+pdf类型
- issue 中有说明，不支持的类型需要先转成pdf

## 超连接在生成md时无法保留

## 通过api方式启动时，需要联网时要如下设置 
export MINERU_MODEL_SOURCE=modelscope

## 显卡

- 后端使用pipeline，会使用基本的工具类，如ocr，table，大概使用3G显存
- 后端如使用vllm-async-engine，大概需要19G显存, 会使用VLM进行处理
- pipeline可不使用GPU，速度慢一点，但是也还好, vllm方式必须要GPU


## 启动

- vscode debug


## docker 安装

- (MinerU) (base) double@CP-001:~/vsproject/MinerU/docker/china$ sudo docker build -t mineru:latest -f Dockerfile .
