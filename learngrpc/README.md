1.环境准备
--
    1. 安装grpc
        pip install grpcio
    2. 安装grpc tools
        pip install grpcio-tools
    3. [grpc github官网](https://github.com/grpc/grpc) 
2.编译
--
    1. 按照proto协议编写协议文件（略）
    2. 编译命令
        protoc --python_out=. sigmob_ad_operation.proto
        python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sigmob_jion.proto
