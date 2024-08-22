# Introduction


# Prequsites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker-compose](https://docs.docker.com/compose/install/)

# How to build the image

我们利用Docker compose来构建镜像， 所以要编译镜像需要执行相关的docker compose build 命令。 为了方便指定Registry的中心库地址，提供了一个环境变量 `REGISTRY` 来指定中心库地址， 如果不指定则默认为 dockerhub, 构建命令如下：

```bash
registry=registry-serverless.datastone.cn docker compose build v1
```

如果你需要修改构建的版本号， 可以修改 `compose.yml` 文件中的 `image` 字段， 例如：
```yaml
...
    image: $registry/kunzhao-7220/sd-serverless:v1
...
```

# Remarks

- 本镜像的构建是基于 `registry-serverless.datastone.cn/library/pytorch:2.1.0-py3.10-cuda11.8.0` 镜像构建的， 所以在构建的时候会下载这个镜像， 如果网络不好， 可能会导致构建失败
- 本镜像的cuda 环境是11.8 环境，torch版本已经预装为 .2.1.0, 当前的torch和cuda版本已经可以足够好的运行comfyui
- 本镜像的构建是采用了multi-stage build的方式， 所以构建的时候会有两个阶段
