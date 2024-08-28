# 介绍

这个例子演示了，如何在Spirit 平台构建Serverless 服务。完整文档请查看 [Serverless 文档](https://serverless.datastone.cn/sprite/docs/zh/quickstart/serverless-step-by-step-2)

## 构建模板

### 构建镜像

#### Docker 安装
你需要在机器上安装 Docker 和 Docker Compose

- [Docker](https://docs.docker.com/get-docker/)
- [Docker-compose](https://docs.docker.com/compose/install/)

#### 准备SDXL 模型

这个Serverless 应用，利用了huggingface的 `diffusers` 包， 由于众所周知的原因， 模型下载我们需要提前准备到本地目录 sdxl-base 目录下。 我已经把模型上传到阿里云盘，你只需要下载到项目的跟目录下即可，分享链接如下：

```
https://www.alipan.com/s/GVDVPFUbw26
```

#### 如何构建镜像

一单你下载了模型到项目的根目录下， 我们就可以开始构建我们的镜像了。 由于每个人都有自己的租户名和方便的拉取基础镜像。 所以我们需要提供一个环境变量 `tenant_name` 来指定你的租户名 和 `registry`， 来指定中心仓库的地址， 这两个环境变量没有默认值，都需要设置。

构建镜像命令如下：

```bash
registry=registry-serverless.datastone.cn tenant_name=kunzhao-7220 docker compose build sd-serverless
```

如果你需要修改构建的版本号， 可以修改 `compose.yml` 文件中的 `image` 字段， 例如：
```yaml
...
    image: $registry/${tenant_name}/sd-serverless:v1
...
```

#### 登录中心库

构建完毕后， 可以把镜像直接推送到我们Serverless 服务的中心仓库上。在推送中心仓库前，你需要通过如下的界面获取登录凭证。
通过如下的命令登录Serverless服务的中心仓库。：

```bash
docker login -u datastone.租户名+租户名 registry-serverless.datastone.cn
```

通过Serverless 平台镜像仓库信息的 `复制登录命令` 按钮，可以直接获取如上的命令。 

登录完成后，你就可以通过docker push 命令进行推送了。




# Remarks

- 本镜像的构建是基于 `registry-serverless.datastone.cn/library/pytorch:2.1.0-py3.10-cuda11.8.0` 镜像构建的， 所以在构建的时候会下载这个镜像， 如果网络不好， 可能会导致构建失败
- 本镜像的cuda 环境是11.8 环境，torch版本已经预装为 .2.1.0, 当前的torch和cuda版本已经可以足够好的运行comfyui
- 本镜像的构建是采用了multi-stage build的方式， 所以构建的时候会有两个阶段


